# ESE 2030 Problem Bank

Conceptual multiple-choice problems for **ESE 2030 — Linear Algebra for Engineers** (Penn), keyed
to *Linear Algebra: Essence & Form* (LAEF), second edition. One chapter per week, thirteen weeks,
**346 problems**, every one of the course's 126 essential skills covered.

Every problem records what it tests, the correct answer, how that answer was verified, and — in
the instructor's own words — why each wrong choice tempts. That last part is the point: the
distractors are the diagnosis.

There are two ways to use this repository. **Students**: skip to the next section. **Faculty
and problem writers**: skip to [For faculty](#for-faculty-writing-problems).

---

## For students: practice

### The quickest route

Open a file in `by_week/`. Each week's file lists every problem for that chapter with the choices,
followed by a collapsed **Answer** block holding the correct letter, an explanation, and a line on
why each wrong choice is wrong. Read the problem, commit to an answer, then open the block.

| week | file | what it covers |
|---|---|---|
| 1 | `by_week/week01_solving_linear_systems.md` | row reduction, rank, LU, conditioning |
| 2 | `by_week/week02_abstract_vector_spaces.md` | subspaces, span, independence, dimension |
| 3 | `by_week/week03_linear_transformations.md` | kernel, image, quotients, the Fundamental Theorem |
| 4 | `by_week/week04_bases_and_coordinates.md` | coordinates, change of basis, similarity |
| 5 | `by_week/week05_inner_products_and_orthogonality.md` | inner products, orthonormal bases, adjoints, QR |
| 6 | `by_week/week06_orthogonal_decomposition_and_data.md` | projection, pseudoinverse, least squares, ridge |
| 7 | `by_week/week07_diagonalization_and_dynamics.md` | eigenvalues, diagonalization, matrix exponential |
| 8 | `by_week/week08_eigenvalue_complexities.md` | complex eigenvalues, Jordan form, the QR algorithm |
| 9 | `by_week/week09_linear_iterative_systems.md` | powers, Markov chains, Perron–Frobenius, symmetric matrices |
| 10 | `by_week/week10_singular_value_decomposition.md` | SVD, condition number, the four subspaces |
| 11 | `by_week/week11_principal_components_and_low_rank_structure.md` | covariance, PCA, Eckart–Young, nuclear norm |
| 12 | `by_week/week12_probability_and_high_dimension.md` | expectation as projection, softmax, random matrices, JL |
| 13 | `by_week/week13_neural_networks_and_ai.md` | activations, backpropagation, SGD, attention, autoencoders |

`by_source/` holds the same problems arranged by the quiz or final they appeared on, if you
want to sit a past Quizzam end to end.

### The interactive route

`scripts/quiz_me.py` asks you problems at the terminal and scores you. It needs only Python 3.

```
python scripts/quiz_me.py                          # five random problems
python scripts/quiz_me.py --week 7 --count 10      # ten from Week 7
python scripts/quiz_me.py --skill W06.S02          # one essential skill, drilled
python scripts/quiz_me.py --topic eigenvalue       # keyword search
python scripts/quiz_me.py --source 2025C:quiz3     # a past quiz, as given
python scripts/quiz_me.py --list-weeks
```

### Knowing what to study

`weekly_topics/` has one file per week. Each names the chapter's CORE CONCEPTS, then an
**ESSENTIAL SKILLS** list — the things you are expected to be able to do without hesitation,
each tagged like `[W06.S04]` — and a **TYPICAL MCQ TRAPS** list of the mistakes students make
on exams. The traps are where the distractors come from. If you can read the trap list for a week
and say *why* each one is a mistake, you are ready.

`COVERAGE.md` counts the problems per skill, so `--skill W09.S08` tells you exactly what is
there to practice on the Rayleigh quotient.

### Generating more practice with an AI assistant

`problems.json` is the whole bank in one file. Hand it, plus the `weekly_topics/` file for the
week you are studying, to Claude or ChatGPT:

> *"Here are the Week 6 problems from my course and the Week 6 topic file. Write five new
> multiple-choice problems in the same style on the ESSENTIAL SKILLS I have fewest problems for,
> with distractors drawn from the TYPICAL MCQ TRAPS. Don't show me the answers until I ask."*

> *"Explain why the answer to ESE2030-0130 is correct and what each wrong choice was testing."*

> *"Quiz me on Week 10 one problem at a time, and after each answer tell me which trap I fell
> into, if any."*

The problems are conceptual by design — there is nothing to compute — so an assistant that has
read the topic file writes very good ones.

---

## For faculty: writing problems

### What a problem looks like

One file per problem under `problems/`, YAML, hand-editable. Abbreviated (full template at
`schema/EXAMPLE-problem.yaml`):

```yaml
id: ESE2030-0340            # opaque, permanent, never reused
week: 6                     # LAEF 2E chapter -- the stable axis; mutable
skills: [W06.S10]           # ids into schema/skills.json; week must match
status: active              # active | needs-review | retired-2e
statement: |                # LaTeX, in a block scalar
  Ridge regression minimizes ...
choices:
  - {label: A, text: ...}   # exactly one correct; five choices by convention
  ...
answer:
  correct: A
  partial_credit: [D]       # letters earning half credit, if any
  verified: true            # false = solved after the fact, awaiting review
  verified_from: [prof-g review 2026-09-10]
  explanation: |
    ...
  distractor_rationale:     # why a student picks each wrong letter -- the diagnosis
    B: "Trick: the listed trap. Ridge cannot lower the residual ..."
    C: "Distractor: ..."
sources:                    # every appearance; a reused problem is ONE problem
  - {semester: 2025C, instrument: quiz3, position: 12}
  - {semester: POOL,  instrument: pool,  position: 14}   # generated, not yet used
notes: 'FORM = PRT | SOURCE = WEEK_6 CORE 6 | difficulty: Core'
```

The design decisions — week as a mutable attribute, quiz appearance as provenance, opaque ids,
one file per problem — are argued in `SCHEMA.md`. The schema is frozen at v2.1; changes need a
version bump and a migration note there.

### House rules for a good problem

The full skill file is `skills/MC-skill-2030.md` (written for AI assistants, but it is the
style guide for humans too). The short version:

1. **Conceptual over computational.** Students have tools. Test *why* an object exists, what it
   represents, which tool applies, what changes when a hypothesis changes.
2. **Don't give it away.** The stem must not name the theorem or state the formula the student is
   supposed to supply.
3. **Bare answer choices.** Expressions or short phrases; no "because…" clauses.
4. **Every distractor implements a named error**, preferably one from the week's TYPICAL MCQ
   TRAPS. If you cannot say in one line which mistake produces a wrong choice, replace it.
5. **Vary the cognitive task.** Each problem carries a FORM tag — DIM-COUNT, CLASSIFY,
   MUST-BE-TRUE, COUNTEREXAMPLE, HYPOTHESIS-REMOVAL, WELL-FORMED, IDENTIFY-THE-OBJECT,
   TOOL-SELECTION, INVARIANCE, PERTURB-THE-SETUP, FIGURE-READ, FIGURE-SELECT, TRANSLATE,
   BOUNDARY-CASE, and so on. Topic spread does not make variety; form spread does.
6. **Partial credit is rare and earned.** Only on a problem that decomposes into two insights,
   only for a choice that demonstrates one of them, at most one such choice per problem.
7. **Match the week's vocabulary.** Null/column space in Weeks 1–2, kernel/image from Week 3;
   `A = VΛV⁻¹`, column-stochastic Markov matrices, `[C] = (1/n)XᵀX`; in Week 13 `Λ` counts
   layers, so never let it meet an eigenvalue matrix in one problem.
8. **Nothing from a week's PERIPHERAL list**, however true.

### Adding a problem

```
cp schema/EXAMPLE-problem.yaml problems/ESE2030-0348.yaml    # next unused id; see COVERAGE.md
# edit it; set status: needs-review, verified: false until a second pair of eyes has checked it
python scripts/validate.py       # schema + invariants; must report 0 errors
python scripts/compile.py        # regenerates problems.json, by_week/, by_source/, COVERAGE.md
```

Commit the YAML *and* the generated files. `compile.py` refuses to run while `validate.py`
reports errors, so a broken record can never reach the compiled views. Figures go in `images/`,
named by problem id (`ESE2030-0321-a.png`), greyscale, no numeric tick labels — nothing in a
figure should be solvable with a ruler.

Ids are never reused: a rejected draft leaves a permanent gap (0312 is one).

### Drafting with an AI assistant

The bank was extended this way and the protocol held up. Give the assistant the week's
`weekly_topics/` file, `skills/MC-skill-2030.md`, and `problems.json`, and ask for a
**distribution table first** — one row per proposed problem with its skill, hook, FORM, and
source citation — before any drafting. Approve or revise the table, then let it draft YAML at
`status: needs-review` with labelled distractors. Review in the `by_week/` view, and flip the
accepted records to `active` / `verified: true` with your name in `verified_from`.

`COVERAGE.md` tells you where to aim: it lists problems per skill, and a skill with a count of
1 or 2 is thin. Generated problems carry `{semester: POOL, instrument: pool}` as their source
until they first appear on an instrument, at which point the real appearance is appended and the
POOL entry removed.

### Ingesting a new semester's Quizzams

```
python scripts/build.py 2026-A 2026A            # reads quizzes-exams/2026-A/*.tex
```

`build.py` extracts one record per live problem and cross-checks every answer key it can find
(embedded key, `-ANSWERS.tex`, or a permuted student solutions guide, matched by text). Two
agreeing keys are both recorded; a disagreement is recorded as `answer.conflict` and never
resolved silently. It never overwrites an existing record without `--force`.

### Scripts

| script | role |
|---|---|
| `validate.py` | every record against the schema and the invariants; exit 1 on any error |
| `compile.py` | YAML → `problems.json`, `by_week/`, `by_source/`, `COVERAGE.md` |
| `build.py` | one-shot import of a semester's `.tex` into new YAML records |
| `extract.py` | the `.tex` parser used by `build.py` |
| `parse_solutions.py` | parser + text-matcher for permuted solutions guides |
| `build_skills_index.py` | regenerate `schema/skills.json` after editing an ESSENTIAL SKILLS list |
| `quiz_me.py` | the student self-study tool |

---

## Layout

```
problems/            ESE2030-NNNN.yaml   ONE FILE PER PROBLEM. The source of truth.
problems.json        the whole bank, compiled                          -- GENERATED
by_week/             study views, one per week / LAEF 2E chapter        -- GENERATED
by_source/           study views, one per exam instrument, plus POOL    -- GENERATED
COVERAGE.md          problems per week and per skill                    -- GENERATED
schema/              problem.schema.json, skills.json (GENERATED), EXAMPLE-problem.yaml
weekly_topics/       one file per week: concepts, ESSENTIAL SKILLS, MCQ traps -- the spec
quizzes-exams/       source .tex files by semester, with answer keys and solutions guides
images/              figures, named by problem id
skills/              MC-skill-2030.md, the problem-writing skill / style guide
book/                the LAEF 2E corpus, for checking notation and scope
scripts/             see above
SCHEMA.md            the schema, the reasons behind it, and the validation rules
```

## Course map

| Week | Chapter | Title |
|---|---|---|
| 1 | 1 | Solving Linear Systems |
| 2 | 2 | Abstract Vector Spaces |
| 3 | 3 | Linear Transformations |
| 4 | 4 | Bases & Coordinates |
| 5 | 5 | Inner Products & Orthogonality |
| 6 | 6 | Orthogonal Decomposition & Data |
| 7 | 7 | Diagonalization & Dynamics |
| 8 | 8 | Eigenvalue Complexities |
| 9 | 9 | Linear Iterative Systems |
| 10 | 10 | Singular Value Decomposition |
| 11 | 11 | Principal Components & Low-Rank Structure |
| 12 | 12 | Probability & High Dimension |
| 13 | 13 | Neural Networks & AI |

**Week numbers always mean LAEF 2E chapters**, whatever the syllabus of the term a problem was
written for. Where the second edition changed emphasis, the `weekly_topics/` file says so under
NOTE ON SCOPE: the pseudoinverse now precedes least squares (Week 6); polar decomposition is gone
from Week 10; Weeks 12 and 13 are new.

## Status

| | |
|---|---|
| records | 346: 2025-C (158), 2026-A (134), generated pools (54) |
| answer keys | 344 verified, 0 conflicts |
| skills | all 126 essential skills covered — see `COVERAGE.md` for the thin ones |
| needs-review | 10, all with open key checks from the source semesters |
| retired-2e | 2 (polar decomposition, 2026-A) |

---

*For study purposes only. ESE 2030, University of Pennsylvania.*
