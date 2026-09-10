#!/usr/bin/env python3
"""
ESE 2030 Problem Bank - Self-Study Quiz Tool

Reads the compiled problems.json (schema 2.x, produced by scripts/compile.py).

Examples:
  python quiz_me.py                        # 5 random problems
  python quiz_me.py --week 7 --count 10    # 10 problems from Week 7 (LAEF 2E Chapter 7)
  python quiz_me.py --source 2026A         # problems that appeared in the 2026-A offering
  python quiz_me.py --source 2025C:quiz3   # ... on one particular instrument
  python quiz_me.py --skill W06.S02        # problems tagged with one essential skill
  python quiz_me.py --topic eigenvalue     # free-text search of topics and statement
  python quiz_me.py --list-weeks
  python quiz_me.py --list-sources
"""
import json
import random
import argparse
from pathlib import Path


def load(problems_file: Path) -> tuple[dict, list[dict]]:
    with open(problems_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not str(data.get('metadata', {}).get('schema_version', '')).startswith('2'):
        raise SystemExit('problems.json is not schema 2.x -- run scripts/compile.py first')
    return data['metadata'], data['problems']


def quizzable(p: dict) -> bool:
    """A problem you can be scored on: has a key, is not retired, is not a survey."""
    return (p['answer']['correct'] is not None
            and p['status'] != 'retired-2e'
            and p.get('problem_type') != 'survey')


def filter_problems(problems, week=None, source=None, skill=None, topic=None):
    out = [p for p in problems if quizzable(p)]
    if week:
        out = [p for p in out if p['week'] == week]
    if source:
        sem, _, inst = source.partition(':')
        out = [p for p in out if any(s['semester'] == sem and (not inst or s['instrument'] == inst)
                                     for s in p['sources'])]
    if skill:
        out = [p for p in out if skill in p['skills']]
    if topic:
        t = topic.lower()
        out = [p for p in out if any(t in x.lower() for x in p['topics'])
               or t in p['statement'].lower()]
    return out


def titlecase(s: str) -> str:
    return s.title().replace(' Ai', ' AI')


def clean(s: str) -> str:
    """Light cleanup of LaTeX for a terminal."""
    return (s.replace('\\\\', '\n').replace('\\item', '\n  *')
             .replace('\\begin{itemize}', '').replace('\\end{itemize}', '')
             .replace('\\begin{enumerate}', '').replace('\\end{enumerate}', '')
             .replace('\\mathbf', '').replace('\\mathbb', '').replace('\\mathcal', ''))


def display_problem(p, i, n, weeks):
    print()
    print('=' * 70)
    src = ', '.join(f"{s['semester']} {s['instrument']} #{s['position']}" for s in p['sources'])
    print(f"[{i}/{n}] {p['id']}  -  Week {p['week']}: {titlecase(weeks.get(str(p['week']), '?'))}   ({src})")
    print('=' * 70)
    print()
    print(clean(p['statement']))
    for fig in p['figures']:
        print(f'  [figure: images/{fig}]')
    print()
    for c in p['choices']:
        print(f"  ({c['label']}) {clean(c['text'])}")
    print()


def display_answer(p, user):
    a = p['answer']
    ok = user == a['correct']
    if ok:
        print('  CORRECT.')
    elif user in a['partial_credit']:
        print(f"  PARTIAL CREDIT. The best answer is ({a['correct']}).")
    else:
        print(f"  Incorrect. The answer is ({a['correct']}).")
    why = a['distractor_rationale'].get(user)
    if why and not ok:
        print(f"  Why ({user}) tempts: {clean(why)}")
    if a.get('explanation'):
        print()
        print('  ' + clean(a['explanation']).replace('\n', '\n  '))
    if a.get('key_insight'):
        print()
        print('  Key insight: ' + clean(a['key_insight']))
    if not a['verified']:
        print('  (this key has not been verified against a source answer key)')
    return ok


def run_quiz(problems, count, weeks):
    if not problems:
        print('No problems match those filters.')
        return
    chosen = random.sample(problems, min(count, len(problems)))
    score = 0
    for i, p in enumerate(chosen, 1):
        display_problem(p, i, len(chosen), weeks)
        labels = [c['label'] for c in p['choices']]
        while True:
            ans = input(f"Your answer ({'/'.join(labels)}), or q to quit: ").strip().upper()
            if ans == 'Q':
                print(f'\nScore: {score}/{i - 1}')
                return
            if ans in labels:
                break
        score += display_answer(p, ans)
    print()
    print(f'Final score: {score}/{len(chosen)}')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--week', '-w', type=int, choices=range(1, 14), metavar='1-13')
    ap.add_argument('--source', '-s', help='semester, or semester:instrument (e.g. 2025C:quiz3)')
    ap.add_argument('--skill', '-k', help='essential-skill id, e.g. W06.S02')
    ap.add_argument('--topic', '-t', help='keyword in topics or statement')
    ap.add_argument('--count', '-c', type=int, default=5)
    ap.add_argument('--list-weeks', action='store_true')
    ap.add_argument('--list-sources', action='store_true')
    a = ap.parse_args()

    root = Path(__file__).resolve().parent.parent
    meta, problems = load(root / 'problems.json')
    weeks = meta['weeks']

    if a.list_weeks:
        for w in range(1, 14):
            n = len([p for p in problems if p['week'] == w and quizzable(p)])
            print(f"  Week {w:2d}: {titlecase(weeks.get(str(w), '?')):45s} {n:3d} problems")
        return
    if a.list_sources:
        for k, n in meta['by_source'].items():
            print(f'  {k:16s} {n:3d} problems')
        return

    chosen = filter_problems(problems, a.week, a.source, a.skill, a.topic)
    print(f'{len(chosen)} problems match.')
    run_quiz(chosen, a.count, weeks)


if __name__ == '__main__':
    main()
