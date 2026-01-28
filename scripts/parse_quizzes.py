#!/usr/bin/env python3
"""
ESE 2030 Quiz Problem Database Builder

Parses LaTeX quiz files and answer files to create a structured JSON database
of linear algebra problems.
"""

import re
import json
from pathlib import Path
from datetime import datetime
from typing import Optional


# Week topic mapping
WEEK_TOPICS = {
    1: "Solving Linear Systems",
    2: "Abstract Vector Spaces",
    3: "Linear Transformations",
    4: "Bases & Coordinates",
    5: "Inner Products",
    6: "Orthogonal Decomposition",
    7: "Diagonalization & Dynamics",
    8: "Eigenvalue Complexities",
    9: "Linear Iterative Systems",
    10: "Singular Value Decomposition",
    11: "Principal Components"
}

# Quiz coverage by week
QUIZ_WEEK_COVERAGE = {
    1: [1, 2, 3],
    2: [3, 4, 5],
    3: [5, 6, 7],
    4: [7, 8, 9],
    5: [10, 11]
}

# Keywords that strongly indicate a specific week (for inference when WEEK comment is missing)
WEEK_KEYWORDS = {
    1: [
        "row reduction", "row operation", "elementary matrix", "elementary matrices",
        "lu decomposition", "plu", "pivot", "triangular system", "forward substitution",
        "backward substitution", "gaussian elimination", "linear system", "augmented matrix",
        "row echelon", "rref", "permutation matrix", "condition number", "ill-conditioned"
    ],
    2: [
        "vector space", "subspace", "span", "linear independence", "linearly independent",
        "linearly dependent", "basis", "dimension", "polynomial space", "axiom",
        "closure", "zero vector", "scalar multiplication", "vector addition"
    ],
    3: [
        "linear transformation", "kernel", "image", "nullity", "rank", "cokernel",
        "coimage", "quotient space", "equivalence class", "isomorphism", "injective",
        "surjective", "fundamental theorem", "null space", "range"
    ],
    4: [
        "coordinate", "change of basis", "transition matrix", "coordinate vector",
        "basis representation", "coordinate system", "standard basis", "ordered basis"
    ],
    5: [
        "inner product", "dot product", "norm", "angle", "orthogonal", "perpendicular",
        "cauchy-schwarz", "triangle inequality", "orthonormal", "unit vector", "length",
        "distance", "pythagorean"
    ],
    6: [
        "orthogonal decomposition", "projection", "orthogonal complement", "gram-schmidt",
        "orthonormal", "qr decomposition", "least squares"
    ],
    7: [
        "eigenvalue", "eigenvector", "diagonalization", "diagonalizable", "characteristic polynomial",
        "matrix exponential", "dynamics", "differential equation", "ode"
    ],
    8: [
        "complex eigenvalue", "algebraic multiplicity", "geometric multiplicity",
        "defective", "jordan", "generalized eigenvector"
    ],
    9: [
        "iterative", "power method", "markov", "steady state", "convergence",
        "spectral radius", "dominant eigenvalue"
    ],
    10: [
        "svd", "singular value", "singular vector", "pseudoinverse", "low-rank",
        "matrix approximation"
    ],
    11: [
        "pca", "principal component", "covariance", "correlation", "variance",
        "data analysis", "dimensionality reduction"
    ]
}


def infer_week_from_topics(topics: list[str], quiz_num: int, statement: str = "") -> Optional[int]:
    """Infer the week number from problem topics and/or statement when WEEK comment is missing."""
    # Combine topics and statement for analysis
    text_to_analyze = ' '.join(topics).lower()
    if statement:
        text_to_analyze += ' ' + statement.lower()

    if not text_to_analyze.strip():
        return None

    possible_weeks = QUIZ_WEEK_COVERAGE.get(quiz_num, list(range(1, 12)))

    # Score each possible week based on keyword matches
    week_scores = {week: 0 for week in possible_weeks}

    for week in possible_weeks:
        keywords = WEEK_KEYWORDS.get(week, [])
        for keyword in keywords:
            if keyword in text_to_analyze:
                week_scores[week] += 1

    # Return the week with highest score (if any matches found)
    if max(week_scores.values()) > 0:
        return max(week_scores, key=week_scores.get)

    # Default to middle week of quiz coverage if no matches
    return possible_weeks[len(possible_weeks) // 2]


def parse_quiz_file(filepath: Path, quiz_num: int) -> list[dict]:
    """Parse a quiz LaTeX file and extract all problems."""
    content = filepath.read_text(encoding='utf-8')

    # Remove fully commented lines to avoid picking up commented-out problems
    lines = content.split('\n')
    cleaned_lines = []
    for line in lines:
        # Skip lines that are entirely comments (start with %)
        if line.strip().startswith('%'):
            # But keep % WEEK, % TOPICS, % CORRECT lines as they contain metadata
            if not any(marker in line for marker in ['% WEEK', '% TOPICS', '% CORRECT', '% PARTIAL', '% TRICK']):
                cleaned_lines.append('')  # Replace with empty line to preserve structure
                continue
        cleaned_lines.append(line)
    content = '\n'.join(cleaned_lines)

    problems = []

    # Split by problem markers (only non-commented ones now)
    problem_pattern = r'\{\\bf PROBLEM (\d+):\s*\}(.*?)(?=\{\\bf PROBLEM \d+:\s*\}|\\end\{document\})'
    matches = re.findall(problem_pattern, content, re.DOTALL)

    for prob_num_str, prob_content in matches:
        prob_num = int(prob_num_str)
        problem = extract_problem_data(prob_content, quiz_num, prob_num)
        problems.append(problem)

    return problems


def extract_problem_data(content: str, quiz_num: int, prob_num: int) -> dict:
    """Extract all data from a single problem's content."""

    # Extract WEEK
    week_match = re.search(r'% WEEK\s*=\s*(\d+)', content)
    week = int(week_match.group(1)) if week_match else None

    # Extract TOPICS
    topics_match = re.search(r'% TOPICS\s*=\s*(.+?)(?:\n|$)', content)
    topics = []
    if topics_match:
        topics = [t.strip() for t in topics_match.group(1).split(',')]

    # Extract problem statement early (for week inference)
    # Try enumerate format first, then fall back to looking for answer markers
    statement_match = re.search(r'^(.*?)\\begin\{enumerate\}', content, re.DOTALL)
    if not statement_match:
        # Try inline format: look for (A) or \begin{center} as answer delimiter
        statement_match = re.search(r'^(.*?)(?:\\begin\{center\}|\n\s*\(A\)\s)', content, re.DOTALL)
    if not statement_match:
        # Fall back to everything before \divider
        statement_match = re.search(r'^(.*?)\\divider', content, re.DOTALL)

    statement = ""
    if statement_match:
        statement = clean_statement(statement_match.group(1))

    # Infer week from topics and statement if not explicitly specified
    week_inferred = False
    if week is None:
        week = infer_week_from_topics(topics, quiz_num, statement)
        week_inferred = week is not None

    # Extract correct answer from comment
    correct_match = re.search(r'% CORRECT ANSWER:\s*\(([A-E])\)[:\s]*(.*)$', content, re.MULTILINE)
    correct_answer = correct_match.group(1) if correct_match else None
    brief_explanation = correct_match.group(2).strip() if correct_match else ""

    # Extract partial credit annotations
    partial_credit = {}
    partial_matches = re.findall(r'% (?:SMALL )?PARTIAL CREDIT[:\s]*\(?([A-E,\s]+)\)?[:\s\-]*(.*)$', content, re.MULTILINE)
    for letters, reason in partial_matches:
        for letter in re.findall(r'[A-E]', letters):
            partial_credit[letter] = reason.strip() if reason.strip() else "Partial understanding shown"

    # Extract trick answer annotations
    trick_answers = {}
    trick_matches = re.findall(r'% TRICK ANSWER:\s*\(([A-E])\)[:\s]*(.*)$', content, re.MULTILINE)
    for letter, reason in trick_matches:
        trick_answers[letter] = reason.strip()

    # Extract choices
    choices = extract_choices(content)

    # Extract figure references
    figures = re.findall(r'\\includegraphics(?:\[.*?\])?\{([^}]+)\}', content)

    # Determine problem type based on content analysis
    problem_type = classify_problem_type(statement, topics)

    return {
        "id": f"Q{quiz_num}-P{prob_num:02d}",
        "quiz": quiz_num,
        "problem_number": prob_num,
        "week": week,
        "chapter_topic": WEEK_TOPICS.get(week, "Unknown") if week else "Unknown",
        "topics": topics,
        "concepts_tested": [],  # Will be filled in by cross-referencing
        "problem_type": problem_type,
        "statement": statement,
        "choices": choices,
        "figures": figures,
        "correct_answer": correct_answer,
        "explanation": brief_explanation,
        "partial_credit": partial_credit,
        "trick_answers": trick_answers,
        "key_insight": ""
    }


def clean_statement(text: str) -> str:
    """Clean up the problem statement text."""
    # Remove comment lines
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        # Skip pure comment lines (but keep inline comments stripped)
        stripped = line.strip()
        if stripped.startswith('%'):
            continue
        # Remove trailing comments
        if '%' in line:
            line = line[:line.index('%')]
        cleaned_lines.append(line)

    text = '\n'.join(cleaned_lines)

    # Remove LaTeX commands we don't need
    text = re.sub(r'\\newpage', '', text)
    text = re.sub(r'\\divider', '', text)

    # Clean up whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()

    return text


def extract_choices(content: str) -> list[dict]:
    """Extract the multiple choice options."""
    choices = []
    labels = ['A', 'B', 'C', 'D', 'E']

    # Try enumerate format first
    enum_match = re.search(r'\\begin\{enumerate\}\[\(A\)\](.*?)\\end\{enumerate\}', content, re.DOTALL)
    if enum_match:
        enum_content = enum_match.group(1)
        # Split by \item
        items = re.split(r'\\item\s*', enum_content)

        for i, item in enumerate(items[1:6]):  # Skip first empty split, take up to 5
            if i < len(labels):
                item_text = item.strip()
                item_text = re.sub(r'\s*%.*$', '', item_text, flags=re.MULTILINE)
                item_text = item_text.strip()
                choices.append({"label": labels[i], "text": item_text})
        return choices

    # Try inline format: (A) ... (B) ... etc.
    # Look for patterns like (A) text (B) text or with \quad separators
    inline_pattern = r'\(([A-E])\)\s*([^(]*?)(?=\s*\([A-E]\)|\\divider|\\bigskip|$)'
    inline_matches = re.findall(inline_pattern, content, re.DOTALL)

    if inline_matches:
        for label, text in inline_matches:
            text = text.strip()
            # Clean up LaTeX formatting
            text = re.sub(r'\\qquad|\\quad|\\:', ' ', text)
            text = re.sub(r'\s*%.*$', '', text, flags=re.MULTILINE)
            text = text.strip()
            if text:
                choices.append({"label": label, "text": text})
        return choices

    # Try center block format
    center_match = re.search(r'\\begin\{center\}(.*?)\\end\{center\}', content, re.DOTALL)
    if center_match:
        center_content = center_match.group(1)
        inline_matches = re.findall(inline_pattern, center_content, re.DOTALL)
        for label, text in inline_matches:
            text = text.strip()
            text = re.sub(r'\\qquad|\\quad|\\:', ' ', text)
            text = re.sub(r'\s*%.*$', '', text, flags=re.MULTILINE)
            text = text.strip()
            if text:
                choices.append({"label": label, "text": text})

    return choices


def classify_problem_type(statement: str, topics: list[str]) -> str:
    """Classify the problem type based on content."""
    statement_lower = statement.lower()
    topics_str = ' '.join(topics).lower()

    if any(word in statement_lower for word in ['compute', 'calculate', 'find', 'solve']):
        return "computational"
    elif any(word in statement_lower for word in ['which statement', 'which of the following', 'must be true']):
        return "conceptual"
    elif any(word in statement_lower for word in ['definition', 'by definition']):
        return "definitional"
    elif any(word in statement_lower for word in ['prove', 'show that']):
        return "proof"
    elif 'example' in topics_str or 'non-example' in topics_str:
        return "identification"
    else:
        return "conceptual"


def parse_answer_file(filepath: Path, quiz_num: int) -> dict[int, dict]:
    """Parse an answer file and extract explanations for each problem."""
    content = filepath.read_text(encoding='utf-8')
    answers = {}

    # Split by section headers
    section_pattern = r'\\section\*\{Problem (\d+):\s*([^}]+)\}(.*?)(?=\\section\*\{Problem \d+:|\\section\*\{Study Tips\}|\\end\{document\})'
    matches = re.findall(section_pattern, content, re.DOTALL)

    for prob_num_str, title, section_content in matches:
        prob_num = int(prob_num_str)
        answer_data = extract_answer_data(section_content)
        answer_data['title'] = title.strip()
        answers[prob_num] = answer_data

    return answers


def extract_answer_data(content: str) -> dict:
    """Extract answer data from a problem's answer section."""

    # Extract correct answer
    correct_match = re.search(r'\\correct\{([^}]+)\}', content)
    correct_text = correct_match.group(1) if correct_match else ""

    # Extract partial credit from answer file (may have multiple)
    partial_credits = {}
    partial_matches = re.findall(r'\\partcred\{([^}]+)\}', content)
    for partial_text in partial_matches:
        # Try to extract letter and reason: "(X) reason" or "(X) - reason"
        pc_match = re.match(r'\(([A-E])\)\s*[-:]?\s*(.+)', partial_text.strip())
        if pc_match:
            letter, reason = pc_match.groups()
            partial_credits[letter] = reason.strip()
        else:
            # Store as general partial credit info
            partial_credits['_info'] = partial_text.strip()

    # Extract hint
    hint_match = re.search(r'\\hint\s+(.+?)(?=\\(?:trap|hrulefill|section)|$)', content, re.DOTALL)
    hint_text = ""
    if hint_match:
        hint_text = hint_match.group(1).strip()
        # Clean up LaTeX
        hint_text = re.sub(r'\n+', ' ', hint_text)
        hint_text = hint_text.strip()

    # Extract trap
    trap_match = re.search(r'\\trap\s+(.+?)(?=\\(?:hint|hrulefill|section)|$)', content, re.DOTALL)
    trap_text = ""
    if trap_match:
        trap_text = trap_match.group(1).strip()
        trap_text = re.sub(r'\n+', ' ', trap_text)
        trap_text = trap_text.strip()

    # Extract full explanation (the textbf{Explanation:} section)
    explanation_match = re.search(r'\\textbf\{Explanation:\}\s*(.*?)(?=\\hint|\\trap|\\hrulefill|$)', content, re.DOTALL)
    explanation = ""
    if explanation_match:
        explanation = explanation_match.group(1).strip()
        # Clean up but preserve structure
        explanation = re.sub(r'\n{3,}', '\n\n', explanation)

    return {
        "correct_text": correct_text,
        "partial_credits": partial_credits,
        "hint": hint_text,
        "trap": trap_text,
        "full_explanation": explanation
    }


def merge_problem_with_answer(problem: dict, answer_data: Optional[dict]) -> dict:
    """Merge problem data with answer file data."""
    if answer_data:
        # Use full explanation from answer file if available
        if answer_data.get('full_explanation'):
            problem['explanation'] = answer_data['full_explanation']

        # Add key insight from hint
        if answer_data.get('hint'):
            problem['key_insight'] = answer_data['hint']

        # Add trap info to trick_answers if not already present
        if answer_data.get('trap') and not problem['trick_answers']:
            problem['trick_answers']['_general'] = answer_data['trap']

        # Merge partial credits from answer file (higher quality than quiz file comments)
        if answer_data.get('partial_credits'):
            for letter, reason in answer_data['partial_credits'].items():
                # Skip if reason looks like LaTeX command (parsing artifact)
                if reason.startswith('\\') or len(reason) < 3:
                    continue
                problem['partial_credit'][letter] = reason

    # Clean up partial_credit - remove any entries that are just LaTeX commands
    problem['partial_credit'] = {
        k: v for k, v in problem['partial_credit'].items()
        if not v.startswith('\\') and len(v) >= 3
    }

    return problem


def build_concepts_tested(problem: dict) -> list[str]:
    """Build refined concepts_tested list based on topics and week."""
    concepts = []
    topics_lower = [t.lower() for t in problem['topics']]

    # Map common topic keywords to formal concept names
    concept_mapping = {
        'dimension': 'Dimension of vector spaces',
        'bases': 'Basis and dimension',
        'basis': 'Basis and dimension',
        'linear independence': 'Linear independence',
        'span': 'Spanning sets',
        'kernel': 'Kernel (null space)',
        'nullity': 'Rank-Nullity Theorem',
        'rank': 'Rank-Nullity Theorem',
        'image': 'Image (range)',
        'subspace': 'Subspace properties',
        'vector space axioms': 'Vector space axioms',
        'linear transformation': 'Linear transformation properties',
        'matrix representation': 'Matrix representations',
        'lu decomposition': 'LU decomposition',
        'elementary matrices': 'Elementary row operations',
        'determinant': 'Determinants',
        'invertibility': 'Matrix invertibility',
        'forward substitution': 'Triangular system solving',
        'backward substitution': 'Triangular system solving',
        'quotient space': 'Quotient spaces',
        'coimage': 'Coimage and cokernel',
        'cokernel': 'Coimage and cokernel',
        'isomorphism': 'Isomorphisms',
        'polynomial spaces': 'Polynomial vector spaces',
        'permutation matrices': 'Permutation matrices',
    }

    for topic in topics_lower:
        for keyword, concept in concept_mapping.items():
            if keyword in topic and concept not in concepts:
                concepts.append(concept)

    return concepts if concepts else problem['topics'][:3]


def parse_all_quizzes(base_dir: Path) -> dict:
    """Parse all quiz files and build the complete database."""

    all_problems = []

    for quiz_num in range(1, 6):
        quiz_file = base_dir / f"2030-Q{quiz_num}.tex"
        answer_file = base_dir / f"2030-Q{quiz_num}-ANSWERS.tex"

        if not quiz_file.exists():
            print(f"Warning: {quiz_file} not found")
            continue

        # Parse quiz problems
        problems = parse_quiz_file(quiz_file, quiz_num)

        # Parse answers if available
        answers = {}
        if answer_file.exists():
            answers = parse_answer_file(answer_file, quiz_num)

        # Merge and enhance
        for problem in problems:
            prob_num = problem['problem_number']
            answer_data = answers.get(prob_num)
            problem = merge_problem_with_answer(problem, answer_data)
            problem['concepts_tested'] = build_concepts_tested(problem)
            all_problems.append(problem)

    # Build final database structure
    database = {
        "metadata": {
            "course": "ESE 2030",
            "title": "Linear Algebra for Engineers",
            "semester": "Fall 2025",
            "generated": datetime.now().isoformat(),
            "total_problems": len(all_problems),
            "quizzes": 5,
            "weeks_covered": list(range(1, 12))
        },
        "problems": all_problems
    }

    return database


def parse_single_quiz(base_dir: Path, quiz_num: int) -> dict:
    """Parse a single quiz for preview purposes."""
    quiz_file = base_dir / f"2030-Q{quiz_num}.tex"
    answer_file = base_dir / f"2030-Q{quiz_num}-ANSWERS.tex"

    problems = parse_quiz_file(quiz_file, quiz_num)

    answers = {}
    if answer_file.exists():
        answers = parse_answer_file(answer_file, quiz_num)

    for problem in problems:
        prob_num = problem['problem_number']
        answer_data = answers.get(prob_num)
        problem = merge_problem_with_answer(problem, answer_data)
        problem['concepts_tested'] = build_concepts_tested(problem)

    return {
        "metadata": {
            "course": "ESE 2030",
            "title": "Linear Algebra for Engineers",
            "semester": "Fall 2025",
            "generated": datetime.now().isoformat(),
            "quiz_number": quiz_num,
            "total_problems": len(problems)
        },
        "problems": problems
    }


if __name__ == "__main__":
    import sys

    # Default to parent of scripts directory
    base_dir = Path(__file__).parent.parent.parent

    if len(sys.argv) > 1:
        # Parse single quiz for preview
        quiz_num = int(sys.argv[1])
        db = parse_single_quiz(base_dir, quiz_num)
    else:
        # Parse all quizzes
        db = parse_all_quizzes(base_dir)

    print(json.dumps(db, indent=2))
