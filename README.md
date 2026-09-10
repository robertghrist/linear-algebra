# ESE 2030 Problem Bank

A structured database of linear algebra quiz problems for self-study and AI-assisted
learning, keyed to **Linear Algebra: Essence & Form** (LAEF), second edition.

The course runs thirteen weeks, one week per chapter of the text.

## Contents

```
problem_bank/
├── problems.json          # Complete database
├── README.md              # This file
├── weekly_topics/         # Authoritative topic specification, one file per week
│   ├── WEEK 1 SOLVING LINEAR SYSTEMS.txt
│   ├── WEEK 2 ABSTRACT VECTOR SPACES.txt
│   └── ... (13 files)
├── by_week/               # Problems organized by course week
│   ├── week01_solving_linear_systems.md
│   ├── week02_abstract_vector_spaces.md
│   └── ...
├── by_quiz/               # Problems organized by quiz
│   ├── quiz1_weeks_1_3.md
│   ├── quiz2_weeks_3_5.md
│   └── ...
├── images/                # Figures referenced in problems
└── scripts/               # Tools for parsing and studying
    ├── parse_quizzes.py   # Parser (regenerate database)
    ├── generate_markdown.py
    └── quiz_me.py         # Interactive study tool
```

## Course Map: Weeks, Chapters, Topics

Each week corresponds to exactly one chapter of LAEF 2E. The text is organized in four
movements, after Blake's Four Zoas, mapped onto the four fundamental subspaces.

### THARMAS — body / material (coimage)

| Week | Chapter | Title |
|---|---|---|
| 1 | 1 | Solving Linear Systems |
| 2 | 2 | Abstract Vector Spaces |
| 3 | 3 | Linear Transformations |

### URIZEN — reason (image)

| Week | Chapter | Title |
|---|---|---|
| 4 | 4 | Bases & Coordinates |
| 5 | 5 | Inner Products & Orthogonality |
| 6 | 6 | Orthogonal Decomposition & Data |

### LUVAH — passion (kernel)

| Week | Chapter | Title |
|---|---|---|
| 7 | 7 | Diagonalization & Dynamics |
| 8 | 8 | Eigenvalue Complexities |
| 9 | 9 | Linear Iterative Systems |

### URTHONA — imagination (cokernel)

| Week | Chapter | Title |
|---|---|---|
| 10 | 10 | Singular Value Decomposition |
| 11 | 11 | Principal Components & Low-Rank Structure |
| 12 | 12 | Probability & High Dimension |

### ALBION — synthesis

| Week | Chapter | Title |
|---|---|---|
| 13 | 13 | Neural Networks & AI |

## Weekly Topic Files

`weekly_topics/` is the **authoritative specification** of what each week covers, and is
the reference any problem-generation pass should be given. Each file carries:

- the LAEF 2E chapter and section range, plus the chapter's application sections
- **CORE CONCEPTS** — section by section, with definition/theorem numbers from the text
- **ESSENTIAL SKILLS** — what a student is expected to do without hesitation; this is the
  examinable core, and problems should concentrate here
- **TYPICAL MCQ TRAPS** — the standard misconceptions, written to seed distractors and the
  `trick_answers` field
- **PERIPHERAL — CONTEXT ONLY** — application sections and out-of-scope variants, at most
  a light conceptual question
- **CONNECTIONS** — what the week depends on and what depends on it

Where the second edition changed emphasis, the topic file says so at the top under
NOTE ON SCOPE. The significant shifts from the first edition:

- **Week 6** — the pseudoinverse is promoted to its own section, placed *before* least
  squares; least squares is now its consequence
- **Week 10** — polar decomposition is **removed**; the chapter opens with the Spectral
  Theorem, and matrix norms and the condition number are defined here
- **Week 11** — the first edition's Chapters 11 and 12 are merged; Eckart-Young-Mirsky is
  core, and matrix completion, nuclear norm, and Robust PCA are full sections
- **Week 12** — new chapter: probability as inner-product geometry, concentration,
  Marchenko-Pastur, Johnson-Lindenstrauss, and the randomized SVD
- **Week 13** — new chapter: activations, backpropagation, SGD, attention, and
  representation learning

## Quick Start

### Interactive Quiz
```bash
cd scripts
python quiz_me.py --week 7 --count 5
```

### Browse by Week
Open any file in `by_week/` to study problems organized by topic.

## Using with AI Assistants

The `problems.json` file is designed for use with AI assistants like Claude or ChatGPT.
For problem generation, supply the relevant `weekly_topics/` file alongside it. You can:

1. **Ask for explanations**: "Explain the concept tested in problem Q3-P12"
2. **Request similar problems**: "Generate a problem similar to Q1-P05"
3. **Get study guidance**: "What concepts should I review for Week 7?"
4. **Practice sessions**: "Quiz me on 5 problems about eigenvalues"

### Example Prompts

```
"Using the problem bank, explain why the answer to Q2-P15 is correct
and what common mistakes students make."

"Based on the Week 6 problems, what are the key concepts I need to
understand about orthogonal decomposition?"

"Create a practice problem similar to Q4-P08 but with different numbers."

"Using weekly_topics/WEEK 12 PROBABILITY & HIGH DIMENSION.txt, write five
multiple-choice problems on the ESSENTIAL SKILLS list, drawing distractors
from the TYPICAL MCQ TRAPS section."
```

## JSON Structure

Each problem in `problems.json` has this structure:

```json
{
  "id": "Q1-P03",
  "quiz": 1,
  "problem_number": 3,
  "week": 3,
  "chapter_topic": "Linear Transformations",
  "topics": ["Linear transformations", "kernel", "matrix representation"],
  "concepts_tested": ["Rank-Nullity Theorem", "Kernel computation"],
  "problem_type": "conceptual",
  "statement": "Let T: R^3 -> R^3 be...",
  "choices": [
    {"label": "A", "text": "0"},
    {"label": "B", "text": "1"},
    ...
  ],
  "figures": [],
  "correct_answer": "C",
  "explanation": "All three rows are scalar multiples...",
  "partial_credit": {},
  "trick_answers": {"B": "Miscounts rank as 2"},
  "key_insight": "Recognize row proportionality..."
}
```

## quiz_me.py Usage

```
usage: quiz_me.py [-h] [--week WEEK] [--quiz QUIZ] [--topic TOPIC]
                  [--count COUNT] [--list-weeks] [--list-topics]

ESE 2030 Problem Bank - Self-Study Quiz Tool

options:
  -h, --help            show this help message and exit
  --week, -w WEEK       Filter by week number
  --quiz, -q QUIZ       Filter by quiz number
  --topic, -t TOPIC     Filter by topic keyword
  --count, -c COUNT     Number of problems (default: 5)
  --list-weeks          List all weeks and topics
  --list-topics         List all available topics

Examples:
  python quiz_me.py                      # 5 random problems
  python quiz_me.py --week 7 --count 10  # 10 problems from Week 7
  python quiz_me.py --quiz 3             # Problems from Quiz 3
  python quiz_me.py --topic eigenvalue   # Problems about eigenvalues
```

## Current Database Status

The problem set below **predates the second edition** and is slated for a full rebuild.
The `weekly_topics/` files are current; `problems.json` is not.

- **Total Problems**: 115
- **Quizzes**: 5
- **Weeks Represented**: 1-11 (7, 9, 16, 9, 8, 10, 16, 9, 11, 13, 7 respectively)
- **Weeks With No Problems Yet**: 12, 13
- **Problem Types**: Conceptual, Computational, Definitional, Identification

Two known gaps to close in the rebuild:

1. Weeks 12 and 13 have no problems at all.
2. Existing Week 6, 10, and 11 problems were written against first-edition emphasis and
   need review against the revised topic files — in particular any Week 10 problem on
   polar decomposition, which the second edition no longer contains.

`scripts/quiz_me.py` also hardcodes weeks 1-11 in its `WEEK_TOPICS` table and its
`--week` argument; both need extending to 13 as part of the rebuild.

## Course Information

- **Course**: ESE 2030 — Linear Algebra for Engineers
- **Text**: *Linear Algebra: Essence & Form*, second edition (Agenbyte Press)
- **Structure**: 13 weeks, one chapter per week
- **Source quizzes**: Fall 2025 offering
- **Scope**: From solving linear systems through neural networks

---

*Generated from course quiz materials. For study purposes only.*
