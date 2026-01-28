# ESE 2030 Problem Bank

A structured database of linear algebra quiz problems for self-study and AI-assisted learning.

## Contents

```
problem_bank/
├── problems.json          # Complete database (115 problems)
├── README.md              # This file
├── by_week/               # Problems organized by course week
│   ├── week01_solving_linear_systems.md
│   ├── week02_abstract_vector_spaces.md
│   └── ... (11 files)
├── by_quiz/               # Problems organized by quiz
│   ├── quiz1_weeks_1_3.md
│   ├── quiz2_weeks_3_5.md
│   └── ... (5 files)
├── images/                # Figures referenced in problems
└── scripts/               # Tools for parsing and studying
    ├── parse_quizzes.py   # Parser (regenerate database)
    ├── generate_markdown.py
    └── quiz_me.py         # Interactive study tool
```

## Quick Start

### Interactive Quiz
```bash
cd scripts
python quiz_me.py --week 7 --count 5
```

### Browse by Week
Open any file in `by_week/` to study problems organized by topic:
- Week 1: Solving Linear Systems
- Week 2: Abstract Vector Spaces
- Week 3: Linear Transformations
- Week 4: Bases & Coordinates
- Week 5: Inner Products
- Week 6: Orthogonal Decomposition
- Week 7: Diagonalization & Dynamics
- Week 8: Eigenvalue Complexities
- Week 9: Linear Iterative Systems
- Week 10: Singular Value Decomposition
- Week 11: Principal Components

### Browse by Quiz
Open files in `by_quiz/` to practice for specific exams:
- Quiz 1: Weeks 1-3 (25 problems)
- Quiz 2: Weeks 3-5 (24 problems)
- Quiz 3: Weeks 5-7 (24 problems)
- Quiz 4: Weeks 7-9 (22 problems)
- Quiz 5: Weeks 10-11 (20 problems)

## Using with AI Assistants

The `problems.json` file is designed for use with AI assistants like Claude or ChatGPT. You can:

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
usage: quiz_me.py [-h] [--week {1-11}] [--quiz {1-5}] [--topic TOPIC]
                  [--count COUNT] [--list-weeks] [--list-topics]

ESE 2030 Problem Bank - Self-Study Quiz Tool

options:
  -h, --help            show this help message and exit
  --week, -w {1-11}     Filter by week number
  --quiz, -q {1-5}      Filter by quiz number
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

## Statistics

- **Total Problems**: 115
- **Quizzes**: 5
- **Weeks Covered**: 1-11
- **Problem Types**: Conceptual, Computational, Definitional, Identification

## Course Information

- **Course**: ESE 2030 - Linear Algebra for Engineers
- **Semester**: Fall 2025
- **Topics**: From solving linear systems through principal component analysis

---

*Generated from course quiz materials. For study purposes only.*
