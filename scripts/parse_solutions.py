#!/usr/bin/env python3
"""
Parse a SOLUTIONS-GUIDE .tex (2026-A format) into per-problem answer records,
and match them to problems extracted from the corresponding quiz .tex.

The guides are written for students, organised by WEEK and topic, and cover
several permuted versions of the quiz at once. Consequently:

  * problem ORDER in the guide does not match the quiz file;
  * choice ORDER in the guide may not match the quiz file either;
  * the correct answer is marked one of two ways -- an explicit
    "\\textbf{Correct Answer:} \\textcolor{blue}{\\textbf{(B)}}" line (Q1), or the
    correct \\item wrapped in \\textcolor{blue}{...} inside the list (Q2-Q4, final).

So NOTHING here trusts a position or a letter. A guide problem is matched to a
quiz problem by statement text, and the guide's correct choice is mapped to a
quiz letter by choice text. Letters in the guide's trap / partial-credit prose
are remapped the same way. Anything that fails to match is reported, never
guessed.

Usage (report only):
    python scripts/parse_solutions.py quizzes-exams/2026-A/2030-Q1.tex
"""
import re
import sys
import difflib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import extract as EX

ROOT = Path(__file__).resolve().parent.parent

SECTION = re.compile(r'\\section\*\{WEEK\s*(\d+)')
SUBSECTION = re.compile(r'\\subsection\*\{Problem:\s*(.*)\}\s*$')
CHOICE_ENV = re.compile(r'\\begin\{enumerate\}\[\(A\)\]')
END_ENV = re.compile(r'\\end\{enumerate\}')
INLINE_CHOICE = re.compile(r'^\s*\(([A-H])\)\s*(.*)$')
FIELD = re.compile(r'^\s*\\textbf\{([^}]+):\}\s*(.*)$')
BLUE = re.compile(r'\\textcolor\{blue\}')
LETTER_LEAD = re.compile(r'^\s*\(?([A-H])\)?(?=[\s:.,;)(\-]|$)')


def _strip_markup(s: str) -> str:
    """Remove the highlight wrappers so choice text compares equal across files."""
    s = re.sub(r'\\textcolor\{blue\}', '', s)
    s = re.sub(r'\\(?:textbf|boldsymbol|mathbf|operatorname|mathrm|text|emph|mathcal|mathbb'
               r'|left|right|displaystyle|quad|qquad|,|;|!)\b\s*', '', s)
    # unwrap braces left behind by the removed commands: {X} -> X, repeatedly
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r'\{([^{}]*)\}', r'\1', s)
    return s


def norm(s: str) -> str:
    """Statement normalizer: words only. Loose, for locating a problem."""
    s = _strip_markup(s)
    s = re.sub(r'\\[a-zA-Z]+\*?', ' ', s)
    s = re.sub(r'[^0-9a-zA-Z]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip().lower()


def cnorm(s: str) -> str:
    """Choice normalizer: keeps math operators, since choices often differ ONLY in
    an exponent, a sign, or an operator symbol. Backslash commands keep their name
    as a token (\\oplus -> oplus) so distinct symbols stay distinct."""
    s = _strip_markup(s)
    s = re.sub(r'\\([a-zA-Z]+)\*?', r' \1 ', s)
    s = s.replace('boxplus', 'oplus')          # the text uses both for direct sum
    s = re.sub(r'[\s${}]+', '', s)
    return s.lower()


def parse_guide(path: Path):
    lines = path.read_text(encoding='utf-8').splitlines()
    week = None
    blocks = []
    cur = None
    for ln, l in enumerate(lines, 1):
        m = SECTION.search(l)
        if m:
            week = int(m.group(1))
            continue
        m = SUBSECTION.search(l)
        if m:
            cur = {'week': week, 'title': m.group(1).strip(), 'line': ln, 'body': []}
            blocks.append(cur)
            continue
        if l.strip().startswith(r'\end{document}'):
            cur = None
        if cur is not None:
            cur['body'].append(l)
    return [_parse_block(b) for b in blocks]


def _parse_block(b):
    body = b['body']
    stmt, choices, tail = [], [], []
    blue_idx = None

    ci = next((i for i, l in enumerate(body) if CHOICE_ENV.search(l)), None)
    if ci is not None:
        cj = next((i for i in range(ci + 1, len(body)) if END_ENV.search(body[i])), len(body) - 1)
        head, choice_lines, tail = body[:ci], body[ci + 1:cj], body[cj + 1:]
        cur = None
        for l in choice_lines:
            s = l.strip()
            if s.startswith(r'\item'):
                if cur is not None:
                    choices.append(cur)
                cur = s[5:].strip()
            elif cur is not None and s and not s.startswith('%'):
                cur += ' ' + s
        if cur is not None:
            choices.append(cur)
    else:
        # inline "(A) ..." choices
        head, in_choices = [], False
        for i, l in enumerate(body):
            m = INLINE_CHOICE.match(l)
            if m:
                in_choices = True
                choices.append(m.group(2).strip())
                continue
            if in_choices and FIELD.match(l):
                tail = body[i:]
                break
            if in_choices and l.strip() and choices and not FIELD.match(l):
                choices[-1] += ' ' + l.strip()
                continue
            if not in_choices:
                head.append(l)

    for i, c in enumerate(choices):
        if BLUE.search(c):
            blue_idx = i
    choices = [_strip_markup(c).strip() for c in choices]

    for l in head:
        if l.strip().startswith('%') or EX.DROP.match(l):
            continue
        stmt.append(l.rstrip())
    while stmt and not stmt[0].strip():
        stmt.pop(0)
    while stmt and not stmt[-1].strip():
        stmt.pop()

    fields, traps, cur = {}, [], None
    for l in tail:
        if l.strip().startswith(r'\divider') or l.strip().startswith('%'):
            continue
        m = FIELD.match(l)
        if m:
            name, rest = m.group(1).strip().lower(), m.group(2).strip()
            if name.startswith('trick') or name.startswith('wrong'):
                traps.append(rest)
                cur = ('trap', len(traps) - 1)
            else:
                fields[name] = rest
                cur = name
        elif cur is not None and l.strip():
            if isinstance(cur, tuple):
                traps[cur[1]] += ' ' + l.strip()
            else:
                fields[cur] += ' ' + l.strip()

    correct_text = None
    if blue_idx is not None:
        correct_text = choices[blue_idx]
    elif 'correct answer' in fields:
        m = re.search(r'\(([A-H])\)', fields['correct answer']) or \
            re.search(r'\b([A-H])\b', _strip_markup(fields['correct answer']))
        if m and ord(m.group(1)) - 65 < len(choices):
            correct_text = choices[ord(m.group(1)) - 65]

    trap_map = {}
    for t in traps:
        m = LETTER_LEAD.match(t)
        if m:
            k = ord(m.group(1)) - 65
            if k < len(choices):
                text = t[m.end():].strip(' :–—-')
                if text.startswith('(') and text.endswith(')'):
                    text = text[1:-1].strip()
                trap_map[choices[k]] = text

    partial_texts, partial_note = [], None
    raw = fields.get('partial credit', '').strip()
    if raw and raw.lower().rstrip('.') not in ('none', '--', ''):
        partial_note = raw
        lead = raw.split('(', 1)[0] if not raw.startswith('(') else raw
        for L in re.findall(r'\(?([A-H])\)?', lead[:12]):
            k = ord(L) - 65
            if k < len(choices):
                partial_texts.append(choices[k])

    return {
        'week': b['week'], 'title': b['title'], 'line': b['line'],
        'statement': '\n'.join(stmt), 'choices': choices,
        'correct_text': correct_text,
        'explanation': fields.get('explanation', '').strip() or None,
        'partial_texts': partial_texts, 'partial_note': partial_note,
        'traps': trap_map,
    }


# ------------------------------------------------------------------ matching

def _ratio(a, b):
    """Similarity on WORD tokens with autojunk off. difflib's default autojunk
    heuristic discards frequent characters in strings over 200 chars, which made
    long statements score near zero against their own paraphrase."""
    return difflib.SequenceMatcher(None, a.split(), b.split(), autojunk=False).ratio()


def _best(key, candidates, cutoff):
    """Index of the best match of key among candidates, or None."""
    best, bi = 0.0, None
    for i, c in enumerate(candidates):
        r = _ratio(key, c)
        if r > best:
            best, bi = r, i
    return (bi, best) if best >= cutoff else (None, best)


def match(guide_recs, quiz_recs, stmt_cutoff=0.75, choice_cutoff=0.8):
    """Return {quiz_index: result}, plus a report of what did not match.

    quiz_recs: dicts with 'statement' and 'choices' ([{label,text}]) as build.py makes.
    """
    qn = [norm(r['statement']) for r in quiz_recs]
    results, report = {}, []
    used = set()
    for g in guide_recs:
        gn = norm(g['statement'])
        # exact prefix first, then fuzzy
        hits = [i for i, q in enumerate(qn) if q[:120] == gn[:120] and i not in used]
        if len(hits) == 1:
            qi, score = hits[0], 1.0
        else:
            qi, score = _best(gn, [q if i not in used else '' for i, q in enumerate(qn)], stmt_cutoff)
        if qi is None:
            report.append(f'UNMATCHED guide problem "{g["title"]}" (line {g["line"]}, best {score:.2f})')
            continue
        used.add(qi)
        q = quiz_recs[qi]
        qchoices = [cnorm(c['text']) for c in q['choices']]

        def to_letter(text):
            t = cnorm(text)
            exact = [i for i, c in enumerate(qchoices) if c == t]
            if len(exact) == 1:
                return q['choices'][exact[0]]['label'], 1.0
            # The exam's choice may carry an extra explanatory clause. A choice
            # that BEGINS with the guide's text is the same choice; a fuzzy ratio
            # would prefer a shorter sibling that differs by one symbol.
            pre = [i for i, c in enumerate(qchoices) if len(t) >= 12 and c.startswith(t.rstrip('.'))]
            if len(pre) == 1:
                return q['choices'][pre[0]]['label'], 0.99
            scores = sorted(((difflib.SequenceMatcher(None, t, c, autojunk=False).ratio(), i)
                             for i, c in enumerate(qchoices)), reverse=True)
            if not scores:
                return None, 0.0
            if scores[0][0] < choice_cutoff:
                # A reworded choice (e.g. "R^7 = W (+) W^perp" vs "W (+) W^perp = R^7")
                # is accepted only when it lands on the letter the exam's own key
                # names -- agreement is the evidence that the mapping is right.
                emb = q.get('embedded')
                if emb and scores[0][0] >= 0.6 and q['choices'][scores[0][1]]['label'] == emb:
                    return emb, scores[0][0]
                return None, scores[0][0]
            if len(scores) > 1 and scores[0][0] - scores[1][0] < 0.05:
                report.append(f'AMBIGUOUS CHOICE "{g["title"]}": {text[:60]} ~ '
                              f'{scores[0][0]:.2f} vs {scores[1][0]:.2f}')
                return None, scores[0][0]
            return q['choices'][scores[0][1]]['label'], scores[0][0]

        correct, cs = (None, 0.0)
        if g['correct_text'] is not None:
            correct, cs = to_letter(g['correct_text'])
            if correct is None:
                report.append(f'CHOICE MISMATCH "{g["title"]}": correct choice text not found in quiz '
                              f'(best {cs:.2f}): {g["correct_text"][:80]}')
        else:
            report.append(f'NO KEY in guide for "{g["title"]}"')

        traps = {}
        for text, why in g['traps'].items():
            L, s = to_letter(text)
            if L:
                traps[L] = why
            else:
                report.append(f'TRAP UNMAPPED "{g["title"]}": {text[:60]}')
        partial = []
        for text in g['partial_texts']:
            L, s = to_letter(text)
            if L:
                partial.append(L)

        results[qi] = {
            'correct': correct, 'match_score': score, 'week': g['week'],
            'explanation': g['explanation'], 'partial_credit': sorted(set(partial)),
            'partial_note': g['partial_note'], 'distractor_rationale': traps,
            'title': g['title'], 'guide_line': g['line'],
        }
    # Second pass: the guides paraphrase some statements heavily. Pair the
    # leftovers at a lower threshold, greedily by score, and mark them weak. A
    # weak pairing is only USED downstream when its key agrees with the exam's
    # embedded key (see build.py); otherwise it is reported and ignored.
    left_g = [g for g in guide_recs if not any(r['guide_line'] == g['line'] for r in results.values())]
    left_q = [i for i in range(len(quiz_recs)) if i not in results]
    pairs = sorted(((_ratio(norm(g['statement']), qn[i]), gi, i)
                    for gi, g in enumerate(left_g) for i in left_q), reverse=True)
    taken_g, taken_q = set(), set()
    for score, gi, i in pairs:
        if score < 0.3 or gi in taken_g or i in taken_q:
            continue
        taken_g.add(gi); taken_q.add(i)
        sub, subrep = match([left_g[gi]], [quiz_recs[i]], stmt_cutoff=0.0, choice_cutoff=choice_cutoff)
        r = sub.get(0)
        if r:
            r['match_score'] = score
            r['weak'] = True
            results[i] = r
            report.extend(x for x in subrep if not x.startswith('UNMATCHED'))
    report = [x for x in report if not x.startswith('UNMATCHED')]
    for gi, g in enumerate(left_g):
        if gi not in taken_g:
            report.append(f'UNMATCHED guide problem "{g["title"]}" (line {g["line"]})')
    return results, report


if __name__ == '__main__':
    import build as B
    qpath = Path(sys.argv[1])
    gpath = qpath.with_name(qpath.stem.replace('-EXAM', '') + '-SOLUTIONS.tex')
    live, _ = EX.split_file(qpath)
    quiz = []
    for p in live:
        d = EX.parse_block(p['body'])
        quiz.append({'statement': d['statement'],
                     'choices': [{'label': chr(65 + i), 'text': c} for i, c in enumerate(d['choices'])],
                     'embedded': (d['key'] or {}).get('correct'), 'week': d['week'],
                     'position': p['position']})
    guide = parse_guide(gpath)
    res, rep = match(guide, quiz)
    print(f'{qpath.name}: quiz problems {len(quiz)}, guide problems {len(guide)}, matched {len(res)}')
    agree = disagree = filled = 0
    for i, q in enumerate(quiz):
        r = res.get(i)
        if not r:
            print(f'  #{q["position"]:>2} NO GUIDE MATCH')
            continue
        e, c = q['embedded'], r['correct']
        tag = 'agree' if e == c else ('FILLED' if e is None else ('no-key' if c is None else 'CONFLICT'))
        if r.get('weak'):
            tag = 'weak-' + tag
        agree += tag == 'agree'; disagree += tag == 'CONFLICT'; filled += tag == 'FILLED'
        wk = f'week {q["week"]}' if q['week'] else f'week ? -> {r["week"]}'
        print(f'  #{q["position"]:>2} embedded={e} guide={c} {tag:8} {wk:14} '
              f'score={r["match_score"]:.2f} "{r["title"][:50]}"')
    print(f'agree {agree}, conflict {disagree}, filled {filled}')
    for line in rep:
        print('  ' + line)
