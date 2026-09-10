# ESE 2030 Problem Bank

A structured database of multiple-choice linear algebra problems from ESE 2030 (Linear
Algebra for Engineers, Penn), keyed to **Linear Algebra: Essence & Form** (LAEF), second
edition. One chapter per week, thirteen weeks.

Every problem records where it appeared, what it tests, the correct answer, how that answer
was verified, and — in the instructor's own words — why each wrong choice tempts.

## Layout

```
problems/            ESE2030-NNNN.yaml   ONE FILE PER PROBLEM. The source of truth. Hand-editable.
problems.json        compiled from problems/ -- GENERATED, never hand-edited
by_week/             study views, one per week / LAEF 2E chapter        -- GENERATED
by_source/           study views, one per exam instrument (2025C-quiz3) -- GENERATED
COVERAGE.md          problems per week and per skill; untested skills   -- GENERATED
schema/
  problem.schema.json   JSON Schema every record must satisfy
  skills.json           index of the 113 essential skills, by id        -- GENERATED
  EXAMPLE-problem.yaml  worked template
weekly_topics/       one file per week: concepts, ESSENTIAL SKILLS, MCQ traps -- the spec
quizzes-exams/       source .tex files, by semester (2025-C, 2026-A), with answer keys / guides
images/              figures, named by problem id (ESE2030-0275-a.png)
skills/              MC-skill-2030.md, the problem-writing skill for AI assistants
book/                LAEF 2E corpus
scripts/             see below
SCHEMA.md            the schema, the reasons behind it, and the validation rules
```

The design decisions — week as a mutable attribute, quiz appearance as provenance, opaque
permanent ids, one file per problem — are explained in `SCHEMA.md`.

## Course map

| Week | Chapter | Title | Movement |
|---|---|---|---|
| 1 | 1 | Solving Linear Systems | THARMAS — body / material (coimage) |
| 2 | 2 | Abstract Vector Spaces | |
| 3 | 3 | Linear Transformations | |
| 4 | 4 | Bases & Coordinates | URIZEN — reason (image) |
| 5 | 5 | Inner Products & Orthogonality | |
| 6 | 6 | Orthogonal Decomposition & Data | |
| 7 | 7 | Diagonalization & Dynamics | LUVAH — passion (kernel) |
| 8 | 8 | Eigenvalue Complexities | |
| 9 | 9 | Linear Iterative Systems | |
| 10 | 10 | Singular Value Decomposition | URTHONA — imagination (cokernel) |
| 11 | 11 | Principal Components & Low-Rank Structure | |
| 12 | 12 | Probability & High Dimension | |
| 13 | 13 | Neural Networks & AI | ALBION — synthesis |

`weekly_topics/` is the **authoritative specification** of what each week covers. Each file
carries CORE CONCEPTS (with definition/theorem numbers), ESSENTIAL SKILLS (the examinable
core, tagged `[W06.S04]`), TYPICAL MCQ TRAPS (to seed distractors), PERIPHERAL material, and
CONNECTIONS to other weeks. Where the second edition changed emphasis, the file says so under
NOTE ON SCOPE. Notably: the pseudoinverse now precedes least squares (Week 6); **polar
decomposition is gone** from Week 10; Weeks 12 and 13 are new.

**Week numbers in this bank always mean LAEF 2E chapters**, whatever the syllabus of the term
a problem was written for. The 2026-A offering, for instance, taught neural networks as its
"week 12"; those problems are filed under Week 13 here, with a note.

## Workflow

```
edit problems/*.yaml            # the only thing you hand-edit
python scripts/validate.py      # schema + invariants (SCHEMA.md section 5)
python scripts/compile.py       # -> problems.json, by_week/, by_source/, COVERAGE.md
```

`compile.py` refuses to run while `validate.py` reports errors, so a broken record can never
reach the compiled outputs. Commit the generated files alongside the YAML.

### Ingesting a new semester

```
python scripts/build.py 2026-A 2026A            # ids continue from the highest existing
python scripts/build.py 2026-A 2026A --start-id 159
```

`build.py` reads `quizzes-exams/<semester>/*.tex`, extracts one record per live problem
(commented-out drafts are excluded and reported), and cross-checks every answer key it can
find: the key embedded in the exam source, a `-ANSWERS.tex` file (2025-C formats), or a
student-facing `-SOLUTIONS.tex` guide (2026-A format, matched by *text* because the guides
permute both problem and choice order — see `scripts/parse_solutions.py`). Two independent
sources that agree are both recorded in `answer.verified_from`; a disagreement is recorded as
`answer.conflict`, never resolved silently. **It never overwrites an existing record** without
`--force`, because hand edits (week, skills, notes) live only in the YAML.

### Scripts

| script | role |
|---|---|
| `validate.py` | every record against the schema and the invariants; exit 1 on any error |
| `compile.py` | YAML → `problems.json`, `by_week/`, `by_source/`, `COVERAGE.md` |
| `build.py` | one-shot import of a semester's `.tex` into new YAML records |
| `extract.py` | the `.tex` parser used by `build.py` |
| `parse_solutions.py` | parser + text-matcher for the 2026-A solutions guides |
| `build_skills_index.py` | regenerate `schema/skills.json` after editing ESSENTIAL SKILLS |
| `quiz_me.py` | interactive self-study tool over `problems.json` |

## Self-study

```
python scripts/quiz_me.py --week 7 --count 10     # ten Week 7 problems
python scripts/quiz_me.py --source 2025C:quiz3    # the problems from one quiz
python scripts/quiz_me.py --skill W06.S02         # one essential skill
python scripts/quiz_me.py --topic eigenvalue
python scripts/quiz_me.py --list-weeks
```

Or open any file in `by_week/` — each problem is followed by a collapsed **Answer** section
with the explanation and the distractor rationale.

## Using with AI assistants

`problems.json` is one document with everything, for handing to Claude or ChatGPT. For
problem *generation*, supply the relevant `weekly_topics/` file and `skills/MC-skill-2030.md`
alongside it, and aim at the gaps `COVERAGE.md` reports.

```
"Using weekly_topics/WEEK 12 PROBABILITY & HIGH DIMENSION.txt and the style of the
Week 10-11 problems in problems.json, write five multiple-choice problems on the
ESSENTIAL SKILLS list, drawing distractors from the TYPICAL MCQ TRAPS section."

"Explain why the answer to ESE2030-0130 is correct and what each distractor
diagnoses."
```

## Record structure

One problem, abbreviated (see `schema/EXAMPLE-problem.yaml` for a full one):

```yaml
id: ESE2030-0130            # opaque, permanent
legacy_id: null             # pre-2026 id (Q3-P12), where one exists
week: 6                     # LAEF 2E chapter -- mutable
skills: [W06.S04]           # ids into schema/skills.json; week must match
status: active              # active | needs-review | retired-2e
statement: |                # LaTeX, verbatim from source
  ...
choices: [{label: A, text: ...}, ...]
answer:
  correct: B
  partial_credit: []
  verified: true
  verified_from:            # two entries = two independent keys agreed
    - quizzes-exams/2025-C/2030-FINAL-EXAM.tex
  conflict: null
  explanation: ...
  distractor_rationale: {A: ..., C: ...}   # the instructor's own words, verbatim
sources:                    # every appearance; a reused problem is ONE problem
  - {semester: 2025C, instrument: final, position: 15, file: ..., line: ...}
```

## Status

| | |
|---|---|
| records | 292 — all of 2025-C (Q1–Q5 + final) and 2026-A (Q1–Q4 + final) |
| answer keys | 0 conflicts; 2026-A keys 92% double-verified against the solutions guides |
| weeks | assigned everywhere except the two end-of-quiz survey items |
| skills | not yet tagged — the next phase; `COVERAGE.md` will then show untested skills |
| retired-2e | 2 (polar decomposition, 2026-A) |
| thin weeks | Week 12 has one problem, Week 13 eleven — the generation targets |

---

*For study purposes only. ESE 2030, University of Pennsylvania.*
