#!/usr/bin/env python3
"""
Extract problem records from quizzes-exams/<SEM>/*.tex into per-problem YAML.

Sources, and their hazards, are documented in claude/DATABASE-RESTRUCTURE-PLAN.md.
The three that matter here:

  * Discarded drafts hide in "% TRASH BIN" sections AND are commented out inline
    with no marker at all. Both are excluded; both are reported.
  * Answer keys live in three formats. All three are parsed; where two cover the
    same problem they are cross-checked and a disagreement is recorded as a
    conflict rather than silently resolved.
  * A problem's choices are the \\begin{enumerate}[(A)] list. A [(i)] list is part
    of the statement, not the choices.
"""
import re
import io
import sys
import json
import glob
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'quizzes-exams'

MARKER = re.compile(r'^\s*\{*\\bf PROBLEM\s*(\d+)?\s*:')
DEAD_MARKER = re.compile(r'^\s*%\s*\{*\\bf PROBLEM')
WEEK = re.compile(r'^\s*%\s*WEEK\s*=\s*(\d+)')
TOPICS = re.compile(r'^\s*%\s*TOPICS\s*=\s*(.+)$')
CHOICE_ENV = re.compile(r'\\begin\{enumerate\}\[\(A\)\]')
END_ENV = re.compile(r'\\end\{enumerate\}')
GRAPHIC = re.compile(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}')
# End-of-quiz survey items carry this marker. They have no correct answer BY DESIGN,
# which is different from a key that has not been found yet.
SURVEY = re.compile(r'All answers will receive full credit', re.I)
KEYLINE = re.compile(r'^\s*%\s*\\textbf\{([^}]+):\}\s*(.*)$')
LETTER = re.compile(r'\(([A-H])\)')

# Layout scaffolding stripped from statements. The optional [..] tail matters:
# "\\begin{figure}[h]" must drop as cleanly as "\\begin{figure}".
DROP = re.compile(r'^\s*(\\divider|\\newpage|\\hrulefill|\\vspace|\\bigskip|\\medskip'
                  r'|\\begin\{center\}|\\end\{center\}|\\begin\{figure\}|\\end\{figure\}'
                  r'|\\centering|%=+|%-+)(\[[^\]]*\])?(\{[^}]*\})?\s*$')


# ---------------------------------------------------------------- source split

def split_file(path: Path):
    """Return (live_problems, discarded) for one quiz/exam .tex."""
    lines = io.open(path, encoding='utf-8', errors='replace').read().split('\n')
    end = next((i for i, l in enumerate(lines)
                if l.strip().startswith(r'\end{document}')), len(lines))
    trash = next((i for i, l in enumerate(lines[:end])
                  if re.search(r'TRASH\s*BIN', l, re.I)), None)
    cut = trash if trash is not None else end

    discarded = [(i + 1, lines[i].strip()[:60])
                 for i, l in enumerate(lines) if DEAD_MARKER.match(l)]

    starts = [i for i in range(cut) if MARKER.match(lines[i])]
    out = []
    for n, s in enumerate(starts):
        e = starts[n + 1] if n + 1 < len(starts) else cut
        out.append({'position': n + 1,
                    'printed_number': MARKER.match(lines[s]).group(1),
                    'line': s + 1,
                    'body': lines[s + 1:e]})
    return out, discarded


# Inline choice markers appear after whitespace, after a math spacer (\,\, \quad),
# or at the start of a display. Only a run starting at (A) and stepping A,B,C,...
# is accepted, which is what keeps a stray "(A)" in prose from matching.
INLINE_MARK = re.compile(r'(?<![A-Za-z0-9])\(([A-H])\)')


def parse_inline_choices(body):
    """Fallback for problems whose choices are inline '(A) ... (B) ...' rather
    than an enumerate -- used where the choices are laid out side by side."""
    start = next((i for i, l in enumerate(body)
                  if re.match(r'^\s*\(A\)\s', l)), None)
    if start is None:
        return body, [], []
    stop = next((i for i in range(start, len(body))
                 if body[i].lstrip().startswith('%')), len(body))
    head, region, tail = body[:start], body[start:stop], body[stop:]

    text = ' '.join(l.strip() for l in region)
    marks = [(m.start(), m.group(1)) for m in INLINE_MARK.finditer(text)]
    keep, expect = [], 'A'
    for pos, letter in marks:
        if letter == expect:
            keep.append((pos, letter))
            expect = chr(ord(expect) + 1)
    if len(keep) < 2:
        return body, [], []

    choices = []
    for n, (pos, letter) in enumerate(keep):
        end = keep[n + 1][0] if n + 1 < len(keep) else len(text)
        seg = text[pos + 3:end]
        seg = re.sub(r'\\q?quad|\\bigskip|\\medskip|\\hfill|\\,|\\!|\\\[|\\\]', ' ', seg)
        seg = re.sub(r'\$\s*:\s*\$', ' ', seg)
        choices.append(re.sub(r'\s+', ' ', seg).strip(' :$'))
    return head, choices, tail


def parse_block(body):
    """Split one problem body into statement / choices / figures / tags / key."""
    week = topics = None
    figures = []
    stmt, choices = [], []
    keyblock = []

    # A commented-out enumerate is a discarded draft of the choices; ignore it.
    ci = next((i for i, l in enumerate(body)
               if CHOICE_ENV.search(l) and not l.lstrip().startswith('%')), None)
    if ci is None:
        head, choices, tail = parse_inline_choices(body)
    else:
        depth = 0
        cj = None
        for i in range(ci, len(body)):
            if body[i].lstrip().startswith('%'):
                continue
            if re.search(r'\\begin\{enumerate\}', body[i]):
                depth += 1
            if END_ENV.search(body[i]):
                depth -= 1
                if depth == 0:
                    cj = i
                    break
        cj = cj if cj is not None else len(body) - 1
        head, choice_lines, tail = body[:ci], body[ci + 1:cj], body[cj + 1:]

        cur = None
        for l in choice_lines:
            if l.strip().startswith(r'\item'):
                if cur is not None:
                    choices.append(cur)
                cur = l.strip()[5:].strip()
            elif cur is not None and l.strip() and not l.strip().startswith('%'):
                cur += ' ' + l.strip()
        if cur is not None:
            choices.append(cur)

    for l in head:
        m = WEEK.match(l)
        if m:
            week = int(m.group(1))
            continue
        m = TOPICS.match(l)
        if m:
            topics = [t.strip() for t in m.group(1).split(',') if t.strip()]
            continue
        for g in GRAPHIC.findall(l):
            figures.append(g)
        if l.strip().startswith('%') or DROP.match(l) or GRAPHIC.search(l):
            continue
        stmt.append(l.rstrip())

    # A commented-out draft sitting between this problem and the next LIVE one is
    # not a live marker, so its lines fall inside this problem's block. Everything
    # from the draft's marker onward belongs to the draft, not to this key.
    for l in tail:
        if DEAD_MARKER.match(l):
            break
        if l.strip().startswith('%'):
            keyblock.append(l)

    while stmt and not stmt[0].strip():
        stmt.pop(0)
    while stmt and not stmt[-1].strip():
        stmt.pop()

    statement_text = '\n'.join(stmt)
    return {'week': week, 'topics': topics, 'figures': figures,
            'survey': bool(SURVEY.search(statement_text)),
            'statement': '\n'.join(stmt), 'choices': choices,
            'key': parse_embedded_key(keyblock)}


def parse_embedded_key(lines):
    """Parse the '% \\textbf{Correct Answer:} D' comment block."""
    if not lines:
        return None
    fields, cur = {}, None
    traps = []
    for l in lines:
        m = KEYLINE.match(l)
        if m:
            name, rest = m.group(1).strip(), m.group(2).strip()
            if name.lower().startswith('trick'):
                traps.append(rest)
                cur = ('trap', len(traps) - 1)
            else:
                cur = name.lower()
                fields[cur] = rest
        elif cur is not None:
            cont = re.sub(r'^\s*%\s?', '', l).rstrip()
            if not cont.strip():
                continue
            if isinstance(cur, tuple):
                traps[cur[1]] += ' ' + cont.strip()
            else:
                fields[cur] += ' ' + cont.strip()
    if not fields and not traps:
        return None

    correct = None
    if 'correct answer' in fields:
        m = re.search(r'\b([A-H])\b', fields['correct answer'])
        correct = m.group(1) if m else None

    partial, partial_note = [], None
    if 'partial credit' in fields:
        raw = fields['partial credit'].strip()
        if raw.lower() not in ('none', 'none.', '--', ''):
            # "B (closely related to D, ...)" grants partial credit to B, not to D.
            # Letters are read from the leading enumeration only -- everything from
            # the first parenthesis on is prose about why (standing check 63).
            lead = raw.split('(')[0]
            partial = sorted(set(re.findall(r'\b([A-H])\b', lead)))
            partial_note = raw

    rationale = {}
    for t in traps:
        # The letter is the FIRST token of a trap line ("C (confuses ...)").
        # Searching for "(X)" anywhere first is wrong: prose like "$\\det(A) = 0$"
        # yields a spurious (A) and files the rationale under the wrong choice.
        m = re.match(r'\s*\(?([A-H])\)?(?=[\s:.,;)(-]|$)', t) or LETTER.search(t)
        if m:
            letter = m.group(1)
            text = t[m.end():].strip(' :–—-')
            text = text.strip()
            if text.startswith('(') and text.endswith(')'):
                text = text[1:-1].strip()
            rationale[letter] = text

    return {'correct': correct, 'partial_credit': partial,
            'partial_note': partial_note,
            'explanation': fields.get('explanation'),
            'distractor_rationale': rationale}


# ------------------------------------------------------------- answer files

def parse_answers_A(path: Path):
    """\\section*{Problem N: Title} + \\correct{} + \\partcred{} + \\hint + \\trap."""
    text = io.open(path, encoding='utf-8', errors='replace').read()
    body = text.split(r'\begin{document}', 1)[-1]
    out = {}
    parts = re.split(r'\\section\*\{Problem\s+(\d+)[^}]*\}', body)
    for i in range(1, len(parts) - 1, 2):
        num, chunk = int(parts[i]), parts[i + 1]
        c = re.search(r'\\correct\{([^}]*)\}', chunk)
        letter = None
        if c:
            m = LETTER.search(c.group(1)) or re.search(r'\b([A-H])\b', c.group(1))
            letter = m.group(1) if m else None
        partial = []
        for p in re.findall(r'\\partcred\{([^}]*)\}', chunk):
            m = LETTER.search(p)
            if m:
                partial.append(m.group(1))
        hint = re.search(r'\\hint\s+(.+?)(?:\n\n|\\trap|\\hrulefill|$)', chunk, re.S)
        trap = re.search(r'\\trap\s+(.+?)(?:\n\n|\\hrulefill|$)', chunk, re.S)
        expl = re.search(r'\\textbf\{Explanation:\}\s*(.+?)(?:\\hint|\\trap|\\hrulefill|$)',
                         chunk, re.S)
        out[num] = {'correct': letter, 'partial_credit': sorted(set(partial)),
                    'key_insight': _tidy(hint.group(1)) if hint else None,
                    'trap': _tidy(trap.group(1)) if trap else None,
                    'explanation': _tidy(expl.group(1)) if expl else None}
    return out


def parse_answers_B(path: Path):
    """Answer Key Summary table -> {number: {correct, partial_credit}}."""
    text = io.open(path, encoding='utf-8', errors='replace').read()
    m = re.search(r'Answer Key Summary(.*?)\\end\{tabular\}', text, re.S)
    if not m:
        return {}
    out = {}
    for row in m.group(1).split('\n'):
        r = re.match(r'\s*(\d+)\s*&\s*([A-H])\s*&\s*(.*?)\s*\\\\', row)
        if r:
            partial = [] if r.group(3).strip() in ('--', '') \
                else sorted(set(re.findall(r'\b([A-H])\b', r.group(3))))
            out[int(r.group(1))] = {'correct': r.group(2), 'partial_credit': partial}
    return out


def _tidy(s):
    s = re.sub(r'\s+', ' ', s).strip()
    return s or None


# ------------------------------------------------------------------- emitter

class Block(str):
    pass


def _block_rep(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', str(data), style='|')


yaml.add_representer(Block, _block_rep)


def emit(record, path: Path):
    for k in ('statement',):
        if record.get(k):
            record[k] = Block(record[k].rstrip() + '\n')
    a = record['answer']
    for k in ('explanation', 'key_insight'):
        if a.get(k):
            a[k] = Block(a[k].rstrip() + '\n')
    if a.get('distractor_rationale'):
        a['distractor_rationale'] = {kk: Block(vv.rstrip() + '\n')
                                     for kk, vv in a['distractor_rationale'].items()}
    with io.open(path, 'w', encoding='utf-8', newline='\n') as fh:
        yaml.dump(record, fh, sort_keys=False, allow_unicode=True, width=100,
                  default_flow_style=False)
