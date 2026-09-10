#!/usr/bin/env python3
"""
Build schema/skills.json from the ESSENTIAL SKILLS blocks in weekly_topics/*.txt.

The weekly_topics files are the human-authored source of truth for what each week
covers. This script extracts their tagged skill lines -- "- [W06.S04] State which
fundamental subspace ..." -- into a machine-readable index that problem records
reference by id.

Run after editing any ESSENTIAL SKILLS block.  Never hand-edit schema/skills.json.
"""
import re
import json
import io
import glob
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAG = re.compile(r'^- \[(W\d\d\.S\d\d)\] (.*)$')


def build() -> dict:
    files = sorted(glob.glob(str(ROOT / 'weekly_topics' / '*.txt')),
                   key=lambda f: int(re.search(r'WEEK (\d+)', f).group(1)))
    out = {
        "_comment": ("GENERATED from weekly_topics/*.txt ESSENTIAL SKILLS blocks. "
                     "Do not hand-edit; re-run scripts/build_skills_index.py."),
        "weeks": {},
    }
    for f in files:
        week = int(re.search(r'WEEK (\d+)', f).group(1))
        lines = io.open(f, encoding='utf-8').read().split('\n')
        start = next(i for i, l in enumerate(lines) if l.startswith('ESSENTIAL SKILLS'))
        end = next(i for i, l in enumerate(lines) if l.startswith('TYPICAL MCQ TRAPS'))
        skills, cur = {}, None
        for i in range(start + 1, end):
            m = TAG.match(lines[i])
            if m:
                cur = m.group(1)
                skills[cur] = m.group(2).rstrip()
            elif cur and lines[i].startswith('  ') and lines[i].strip():
                skills[cur] += ' ' + lines[i].strip()   # continuation line
        out["weeks"][str(week)] = {
            "title": lines[0].split(':', 1)[1].strip(),
            "chapter": lines[1],
            "source_file": str(Path(f).relative_to(ROOT)).replace('\\', '/'),
            "skills": skills,
        }
    return out


if __name__ == '__main__':
    data = build()
    dest = ROOT / 'schema' / 'skills.json'
    io.open(dest, 'w', encoding='utf-8').write(
        json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    n = sum(len(w['skills']) for w in data['weeks'].values())
    print(f'wrote {dest.relative_to(ROOT)}: {len(data["weeks"])} weeks, {n} skills')
