#!/usr/bin/env python3
"""
Build problems/ESE2030-NNNN.yaml for one semester from quizzes-exams/.

Ids are assigned in a fixed order -- semester, then instrument (quiz1..quizN,
then final), then position -- so a rebuild is deterministic. Ids are permanent:
once a record exists, its id is read from the existing file and never reassigned.
"""
import re
import io
import sys
import json
import shutil
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import extract as EX
import parse_solutions as PS

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'problems'
IMAGES = ROOT / 'images'

ORDER = ['quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'quiz6', 'final']
FMT_A = {'quiz1', 'quiz2'}          # \section*/\correct/\hint/\trap
FMT_B = {'quiz3', 'quiz4', 'quiz5'}  # Answer Key Summary table
# FMT_C: a student-facing SOLUTIONS guide (2026-A), matched by text -- see parse_solutions.py
DIFFICULTY = re.compile(r'^\s*%\s*DIFFICULTY\s*=\s*(.+)$')


def instrument(path: Path) -> str:
    n = path.stem.upper()
    if 'FINAL' in n:
        return 'final'
    m = re.search(r'-Q(\d+)', n)
    return f'quiz{m.group(1)}' if m else n.lower()


def norm(s: str) -> str:
    """Normalize a statement for content matching.

    Legacy statements retain the float scaffolding that the extractor now strips,
    so environment names and graphics paths are removed on both sides before the
    generic reduction -- otherwise a figure-bearing problem fails to match itself.
    """
    s = re.sub(r'\\includegraphics(?:\[[^\]]*\])?\{[^}]*\}', ' ', s)
    s = re.sub(r'\\(?:begin|end)\{[^}]*\}(?:\[[^\]]*\])?', ' ', s)
    s = re.sub(r'\\[a-zA-Z]+\*?', ' ', s)
    s = re.sub(r'[^0-9a-zA-Z]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip().lower()


def build(semester_dir: str, sem_code: str, start_id: int = 1):
    src = ROOT / 'quizzes-exams' / semester_dir
    files = sorted([p for p in src.glob('*.tex') if 'ANSWERS' not in p.name],
                   key=lambda p: ORDER.index(instrument(p)) if instrument(p) in ORDER else 99)

    records, discarded_all, report = [], [], []
    next_id = start_id

    for f in files:
        inst = instrument(f)
        live, discarded = EX.split_file(f)
        discarded_all += [(f.name, ln, txt) for ln, txt in discarded]

        ans_a = ans_b = {}
        afile = f.with_name(f.stem + '-ANSWERS.tex')
        if afile.exists():
            if inst in FMT_A:
                ans_a = EX.parse_answers_A(afile)
            if inst in FMT_B:
                ans_b = EX.parse_answers_B(afile)

        parsed = [EX.parse_block(p['body']) for p in live]

        guide = {}
        gfile = f.with_name(f.stem.replace('-EXAM', '') + '-SOLUTIONS.tex')
        if gfile.exists():
            qrecs = [{'statement': d['statement'],
                      'choices': [{'label': chr(65 + i), 'text': c} for i, c in enumerate(d['choices'])],
                      'embedded': (d['key'] or {}).get('correct')} for d in parsed]
            guide, grep = PS.match(PS.parse_guide(gfile), qrecs)
            report += [f'GUIDE {f.name}: {x}' for x in grep]

        for pi, p in enumerate(live):
            d = parsed[pi]
            num = int(p['printed_number']) if p['printed_number'] else p['position']

            embedded = d['key'] or {}
            ka, kb = ans_a.get(num), ans_b.get(num)
            kg = guide.get(pi)
            guide_notes = []
            if kg:
                if kg.get('weak') and kg['correct'] and kg['correct'] != embedded.get('correct'):
                    # A loose statement match whose key disagrees is most likely the
                    # wrong problem. Do not record a conflict; report and ignore.
                    report.append(f'GUIDE WEAK-MATCH DISAGREES {f.name} #{num}: '
                                  f'embedded={embedded.get("correct")} guide={kg["correct"]} '
                                  f'"{kg["title"]}" -- guide ignored')
                    kg = None
                elif kg['correct'] is None:
                    guide_notes.append(f'solutions guide matched ("{kg["title"]}") but its '
                                       f'correct choice could not be mapped to a letter here')

            sources_used, letters = [], {}
            if embedded.get('correct'):
                letters['embedded'] = embedded['correct']
                sources_used.append(str(f.relative_to(ROOT)).replace('\\', '/'))
            if ka and ka.get('correct'):
                letters['answers_A'] = ka['correct']
                sources_used.append(str(afile.relative_to(ROOT)).replace('\\', '/'))
            if kb and kb.get('correct'):
                letters['answers_B'] = kb['correct']
                sources_used.append(str(afile.relative_to(ROOT)).replace('\\', '/'))
            if kg and kg.get('correct'):
                letters['guide'] = kg['correct']
                sources_used.append(str(gfile.relative_to(ROOT)).replace('\\', '/'))

            distinct = set(letters.values())
            conflict = None
            correct = None
            if len(distinct) == 1:
                correct = distinct.pop()
            elif len(distinct) > 1:
                correct = letters.get('embedded') or sorted(letters.values())[0]
                conflict = '; '.join(f'{k}={v}' for k, v in sorted(letters.items()))
                report.append(f'CONFLICT {f.name} #{num}: {conflict}')

            partial = embedded.get('partial_credit') or []
            if not partial and ka:
                partial = ka.get('partial_credit') or []
            if not partial and kb:
                partial = kb.get('partial_credit') or []
            if not partial and kg:
                partial = kg.get('partial_credit') or []

            week = d['week']
            if week is None and kg and kg.get('week'):
                week = kg['week']
                guide_notes.append(f'week {week} taken from the solutions guide section heading')
            difficulty = next((m.group(1).strip() for l in p['body']
                               for m in [DIFFICULTY.match(l)] if m), None)

            rid = f'ESE2030-{next_id:04d}'
            next_id += 1

            figs = []
            for i, g in enumerate(d['figures']):
                ext = Path(g).suffix.lower() or '.jpg'
                new = f'{rid}-{chr(97 + i)}{ext}'
                figs.append(new)
                old = IMAGES / g
                if old.exists() and not (IMAGES / new).exists():
                    shutil.copy2(old, IMAGES / new)
                elif not old.exists():
                    report.append(f'MISSING FIGURE {f.name} #{num}: {g}')

            # A trap naming the correct answer is a contradiction in the source.
            # Surface it: pull it out of the rationale, record it, flag for review.
            rationale = dict(embedded.get('distractor_rationale') or {})
            if kg:
                for L, why in (kg.get('distractor_rationale') or {}).items():
                    rationale.setdefault(L, why)
            self_trap = None
            if correct and correct in rationale:
                self_trap = rationale.pop(correct)
                report.append(f'SELF-TRAP {f.name} #{num}: '
                              f'"{correct}" is both the correct answer and a trick answer')

            notes = []
            if self_trap:
                notes.append(f'source contradiction: trick answer listed for the correct '
                             f'choice {correct} -- "{self_trap}"')
            if embedded.get('partial_note') and not partial:
                notes.append(f'partial credit note: {embedded["partial_note"]}')
            if ka and ka.get('trap'):
                notes.append(f'trap (Q{num} answers): {ka["trap"]}')
            if difficulty:
                notes.append(f'difficulty: {difficulty}')
            notes += guide_notes

            rec = {
                'id': rid,
                'legacy_id': None,
                'week': week,
                'skills': [],
                'status': 'active' if d.get('survey')
                          else ('needs-review' if (self_trap or not week) else 'active'),
                'problem_type': 'survey' if d.get('survey') else None,
                'statement': d['statement'],
                'choices': [{'label': chr(65 + i), 'text': c}
                            for i, c in enumerate(d['choices'])],
                'figures': figs,
                'answer': {
                    'correct': correct,
                    'partial_credit': partial,
                    'verified': bool(correct),
                    'verified_from': sorted(set(sources_used)),
                    'conflict': conflict,
                    'explanation': embedded.get('explanation')
                                   or (ka.get('explanation') if ka else None)
                                   or (kg.get('explanation') if kg else None),
                    'key_insight': ka.get('key_insight') if ka else None,
                    'distractor_rationale': rationale,
                },
                'sources': [{'semester': sem_code, 'instrument': inst,
                             'position': p['position'],
                             'file': str(f.relative_to(ROOT)).replace('\\', '/'),
                             'line': p['line']}],
                'variant_of': None,
                'topics': d['topics'] or [],
                'notes': ' | '.join(notes) if notes else None,
            }
            if not rec['choices']:
                report.append(f'NO CHOICES {f.name} #{num}')
            records.append(rec)

    return records, discarded_all, report, next_id


def attach_legacy(records):
    """Match legacy problems.json records by statement content."""
    legacy = json.load(io.open(ROOT / 'problems.json', encoding='utf-8'))['problems']
    index = {}
    for r in records:
        index.setdefault(norm(r['statement'])[:120], []).append(r)
    matched, unmatched = 0, []
    for lp in legacy:
        k = norm(lp['statement'])[:120]
        hits = index.get(k)
        if hits:
            for h in hits:
                if h['legacy_id'] is None:
                    h['legacy_id'] = lp['id']
                    matched += 1
                    break
        else:
            unmatched.append(lp['id'])
    return matched, unmatched


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('semester_dir')
    ap.add_argument('semester_code')
    ap.add_argument('--start-id', type=int, default=None,
                    help='first id to assign; default = one past the highest id in problems/')
    ap.add_argument('--legacy', action='store_true',
                    help='attach legacy Q1-P03 ids from the pre-2026 problems.json (2025-C only)')
    ap.add_argument('--force', action='store_true',
                    help='overwrite existing records (DESTROYS hand edits: week, skills, notes)')
    a = ap.parse_args()

    OUT.mkdir(exist_ok=True)
    existing = sorted(int(p.stem.split('-')[1]) for p in OUT.glob('ESE2030-*.yaml'))
    start = a.start_id if a.start_id is not None else (existing[-1] + 1 if existing else 1)
    recs, discarded, report, _ = build(a.semester_dir, a.semester_code, start)

    clobber = [r['id'] for r in recs if (OUT / f'{r["id"]}.yaml').exists()]
    if clobber and not a.force:
        sys.exit(f'refusing to overwrite {len(clobber)} existing records '
                 f'({clobber[0]}..{clobber[-1]}); pass --force to discard their hand edits')

    matched, unmatched = attach_legacy(recs) if a.legacy else (0, [])

    for r in recs:
        EX.emit(dict(r), OUT / f'{r["id"]}.yaml')

    print(f'records written : {len(recs)}')
    print(f'drafts excluded : {len(discarded)}')
    for n, ln, txt in discarded:
        print(f'    {n}:{ln}  {txt}')
    if a.legacy:
        print(f'legacy matched  : {matched} / 115')
    if unmatched:
        print(f'legacy UNMATCHED: {len(unmatched)} -> {unmatched}')
    print(f'reports         : {len(report)}')
    for line in report:
        print('    ' + line)
