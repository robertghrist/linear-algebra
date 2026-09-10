# Problem Bank Schema

**Status: FROZEN 2026-09-10 (Phase 1); v2.1 2026-09-10.** Changes from here require a version bump and a
migration note.

> **v2.1 migration note.** `sources[].semester` admits `POOL` and `sources[].instrument` admits
> `pool`, for generated problems that have not yet appeared on an instrument. Such a record has
> exactly one source `{semester: POOL, instrument: pool, position: n}`; when it is first used, the
> real appearance is APPENDED and the POOL entry removed. No existing record changes. The plan this implements is `claude/DATABASE-RESTRUCTURE-PLAN.md` in the
LAEF project.

| artefact | role |
|---|---|
| `problems/ESE2030-NNNN.yaml` | one problem per file — **the source of truth**, hand-editable |
| `problems.json` | compiled from `problems/` by `scripts/compile.py`, **generated**, never hand-edited |
| `schema/problem.schema.json` | JSON Schema; every record must validate |
| `schema/skills.json` | generated index of the 126 essential skills (v2), by id |
| `schema/EXAMPLE-problem.yaml` | worked template, validates against the schema |
| `weekly_topics/*.txt` | human-authored source of the skill ids |
| `by_week/`, `by_source/`, `COVERAGE.md` | **generated** study views and the skill-coverage report (`scripts/compile.py`) |

---

## 1. The three decisions this schema encodes

### 1.1 Week is an attribute; the quiz is provenance

The old database was keyed on quiz number. Quizzes are not stable: 2025-C ran five, 2026-A
ran four, and coverage shifts every term. **Week number — equivalently, LAEF 2E chapter — is
the stable axis**, so `week` is a first-class field and everything about which instrument a
problem appeared on moves into `sources`.

`sources` is a **list of appearances**, because a problem reused next term is one problem
with two appearances, not two problems:

```yaml
sources:
  - {semester: 2025C, instrument: quiz3, position: 12}
  - {semester: 2026A, instrument: final,  position: 31}
```

`instrument` is free text (`quiz1`…`quizN`, `final`, `midterm`), so a term running a
different number of quizzes needs no schema change. That is the whole point.

### 1.2 Identifiers encode nothing

`ESE2030-0001`, assigned once, never reassigned, never reused. **The id must not encode the
week.** Week assignment is exactly what changed for chapters 11–13 in the second edition and
will change again; an id like `W07-0012` would force a rename cascade every time the syllabus
moves, and every external reference would rot. Week is a field, and fields change.

`legacy_id` preserves the old `Q1-P03` where one exists, so anything written against the
pre-2026 bank stays traceable.

### 1.3 One file per problem

Hand-correction is a first-class activity here — reconciling three answer-key formats,
assigning ~99 missing weeks, tagging skills. A single ~292-record JSON makes that
unpleasant and produces unreadable diffs. Per-problem YAML gives one file per unit of work,
a readable diff, and no merge conflicts between unrelated edits.

`problems.json` remains as the **compiled** distribution artefact, for `quiz_me.py` and for
handing to an AI assistant in one piece.

---

## 2. YAML conventions

**Every field that can hold LaTeX uses a block scalar.** Inside `|` (literal) or `>-`
(folded) YAML reads text verbatim: backslashes, braces, `$`, `%`, and `:` all survive
untouched, and the LaTeX stays readable in the file.

```yaml
statement: |
  Consider the vector space $\mathcal{P}_3$ of polynomials of degree at most 3.
  The dimension of this space is:
```

Never put LaTeX on a plain inline scalar. `statement: The dimension is: 4` is a YAML parse
error, and `text: \mathcal{P}` is a different string than you think.

Three further rules:

- **Numeric-looking choice text must be quoted.** `text: "4"` — unquoted `4` is an integer,
  and `text: 3.10` becomes `3.1`.
- **Never use tabs.** LaTeX pasted from an editor sometimes carries them; they are illegal
  as YAML indentation.
- **LaTeX is stored verbatim from source.** Preamble macros are not expanded, `\divider`
  and layout commands are stripped, nothing is prettified. The renderer's job, not the
  database's.

---

## 3. Field reference

`schema/problem.schema.json` is authoritative; this is the prose gloss.

### Required

| field | notes |
|---|---|
| `id` | `ESE2030-NNNN`. Opaque, permanent. |
| `week` | 1–13, = LAEF 2E chapter. Mutable. |
| `status` | `active` · `needs-review` · `retired-2e` |
| `statement` | LaTeX, block scalar. |
| `choices` | list of `{label, text}`, labels `A`–`H`. |
| `answer` | see below. |
| `sources` | ≥1 appearance. |

### `answer`

| field | notes |
|---|---|
| `correct` | single letter, or `null` where no key exists yet. |
| `partial_credit` | letters earning partial credit, per the source key. |
| `verified` | `true` = key came from a source file. `false` = solved after the fact, **awaiting prof-g**. |
| `verified_from` | list of source paths. **Two entries means two independent keys agreed** — that is the cross-validation record, not redundancy. |
| `conflict` | set when two sources disagree, recording both readings. Never resolved silently. |
| `explanation`, `key_insight` | prose from the answer key. |
| `distractor_rationale` | why a student picks each wrong letter. **Preserved verbatim** — this is prof-g's `\trap` / `Trick answer:` prose, written to students, and paraphrasing it loses the diagnosis. |

### `skills`

Ids into `schema/skills.json`: `W06.S04` is the fourth essential skill of Week 6. Generated
from the tagged `- [W06.S04] ...` lines in `weekly_topics/*.txt` by
`scripts/build_skills_index.py`.

Two invariants a validator must enforce:

1. every id resolves in `skills.json`;
2. **the week in the id equals the record's `week`** — a Week 6 problem cannot carry a
   `W09.*` skill. If it genuinely does, the week assignment is wrong.

This is what makes coverage reportable: problems per week, per skill, and which of the 113
skills no problem yet tests.

### `status`

`retired-2e` marks a problem the second edition orphaned — Week 10 polar decomposition
being the known case. **Retire, never delete.** A retired problem is still evidence of what
was once asked and may return if the text does.

### Other

`figures` are filenames under `images/`, keyed to the problem id (`ESE2030-0043-a.jpg`), not
to the quiz they first appeared on. `variant_of` links a problem that is the same question
with changed numbers. `topics` carries the free-text `% TOPICS` comments from source as
search bait; it is **not** authoritative — `skills` is. `notes` is editorial, never shown to
students.

---

## 4. Skill ids

**v2 (2026-09-10).** The v1 lists (113 skills) were computational; the exams are conceptual.
v2 rewrote every week's ESSENTIAL SKILLS block as things a student does on a conceptual
multiple-choice item — recognize, decide, distinguish, predict, explain why, know when — and
dropped pure procedures (inverting by hand, computing an SVD, Cauchy–Schwarz, Mahalanobis,
Markov/Chebyshev, Marchenko–Pastur arithmetic). Ids were renumbered and the bank re-tagged;
v1 ids are not comparable. 126 skills across 13 weeks, 8–12 per week:

```
W01 10  W02 9   W03 10  W04 8   W05 11  W06 10  W07 10
W08 8   W09 9   W10 10  W11 10  W12 9   W13 12
```

Ids are **positional within a week's ESSENTIAL SKILLS list**, so inserting a skill in the
middle renumbers everything after it. Two rules follow:

- **Append new skills at the end of a week's list**, never in the middle.
- After editing any ESSENTIAL SKILLS block, re-run `scripts/build_skills_index.py` and
  re-validate; a renumbering silently re-points every problem tagged with the moved ids.

---

## 5. Validation

Every record must satisfy:

1. validates against `schema/problem.schema.json`;
2. `id` unique across `problems/`, and equal to the filename stem;
3. every `skills` id resolves, and its week matches `week`;
4. `answer.correct`, when non-null, names an existing choice label;
5. every `distractor_rationale` key names an existing choice label, and is not `correct`;
6. `variant_of`, when set, resolves to another record;
7. every `figures` entry exists under `images/`.

Rules 4 and 5 are the ones that catch a misaligned answer key — the failure mode that
produces no error anywhere else.

---

## 6. Frozen, and not

**Frozen:** id format, `sources` as a list, `week` as a mutable field, the `answer` object,
skill-id format, per-problem YAML as source of truth.

**Deliberately open:** whether `topics` survives once `skills` is populated everywhere;
whether `problem_type` earns its place (the old classifier put 108 of 115 records in one
bucket, so it is re-derived in Phase 2 and may simply be dropped); whether `midterm` is ever
a real instrument value.
