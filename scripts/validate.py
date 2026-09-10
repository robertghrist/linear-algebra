#!/usr/bin/env python3
"""Validate problems/*.yaml against the schema and the invariants in SCHEMA.md section 5."""
import io
import sys
import json
import glob
from pathlib import Path

import yaml
import jsonschema

ROOT = Path(__file__).resolve().parent.parent


def main():
    schema = json.load(io.open(ROOT / 'schema' / 'problem.schema.json', encoding='utf-8'))
    skills = json.load(io.open(ROOT / 'schema' / 'skills.json', encoding='utf-8'))['weeks']
    files = sorted(glob.glob(str(ROOT / 'problems' / '*.yaml')))
    recs = {}
    errs = []

    for f in files:
        stem = Path(f).stem
        d = yaml.safe_load(io.open(f, encoding='utf-8'))
        try:
            jsonschema.validate(d, schema)
        except jsonschema.ValidationError as e:
            errs.append(f'{stem}: schema: {e.message} at {list(e.path)}')
            continue

        if d['id'] != stem:                                        # (2)
            errs.append(f'{stem}: id {d["id"]} != filename')
        if d['id'] in recs:
            errs.append(f'{stem}: duplicate id')
        recs[d['id']] = d

        labels = [c['label'] for c in d['choices']]
        if labels != sorted(labels) or len(set(labels)) != len(labels):
            errs.append(f'{stem}: choice labels not unique/ordered: {labels}')

        for s in d.get('skills') or []:                            # (3)
            wk = str(int(s[1:3]))
            if wk not in skills or s not in skills[wk]['skills']:
                errs.append(f'{stem}: skill {s} does not resolve')
            elif d['week'] is not None and int(wk) != d['week']:
                errs.append(f'{stem}: skill {s} is week {wk}, record is week {d["week"]}')

        a = d['answer']
        if a['correct'] is not None and a['correct'] not in labels:   # (4)
            errs.append(f'{stem}: correct {a["correct"]} is not a choice {labels}')
        for k in (a.get('distractor_rationale') or {}):               # (5)
            if k not in labels:
                errs.append(f'{stem}: distractor {k} is not a choice')
            elif k == a['correct']:
                errs.append(f'{stem}: distractor {k} is the correct answer')
        for k in a.get('partial_credit') or []:
            if k not in labels:
                errs.append(f'{stem}: partial_credit {k} is not a choice')
        survey = d.get('problem_type') == 'survey'
        if a['correct'] is None and a['verified']:
            errs.append(f'{stem}: verified with no correct answer')
        if survey and a['correct'] is not None:
            errs.append(f'{stem}: survey item must have no correct answer')

        # A survey item has no week and never will; that is not "awaiting review".
        if d['week'] is None and d['status'] != 'needs-review' and not survey:
            errs.append(f'{stem}: null week requires status needs-review')

        for g in d.get('figures') or []:                              # (7)
            if not (ROOT / 'images' / g).exists():
                errs.append(f'{stem}: figure {g} missing from images/')

    for d in recs.values():                                           # (6)
        if d['variant_of'] and d['variant_of'] not in recs:
            errs.append(f'{d["id"]}: variant_of {d["variant_of"]} does not resolve')

    print(f'records validated : {len(recs)}')
    print(f'errors            : {len(errs)}')
    for e in errs[:40]:
        print('    ' + e)
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main())
