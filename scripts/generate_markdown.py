#!/usr/bin/env python3
"""
Generate Markdown study guides from the problem database.
"""

import json
from pathlib import Path


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

QUIZ_COVERAGE = {
    1: (1, 3, "Weeks 1-3"),
    2: (3, 5, "Weeks 3-5"),
    3: (5, 7, "Weeks 5-7"),
    4: (7, 9, "Weeks 7-9"),
    5: (10, 11, "Weeks 10-11")
}


def format_problem_markdown(problem: dict, show_figures: bool = True) -> str:
    """Format a single problem as markdown."""
    lines = []

    # Header
    lines.append(f"## Problem {problem['id']}")
    lines.append("")

    # Metadata
    week = problem.get('week', 'Unknown')
    chapter = problem.get('chapter_topic', 'Unknown')
    concepts = problem.get('concepts_tested', [])

    lines.append(f"**Week {week}** | **{chapter}**")
    if concepts:
        lines.append(f"**Concepts:** {', '.join(concepts)}")
    lines.append("")

    # Statement
    statement = problem.get('statement', '')
    lines.append(statement)
    lines.append("")

    # Figures
    if show_figures and problem.get('figures'):
        for fig in problem['figures']:
            lines.append(f"![Figure](../images/{fig})")
        lines.append("")

    # Choices
    lines.append("**Choices:**")
    for choice in problem.get('choices', []):
        lines.append(f"- ({choice['label']}) {choice['text']}")
    lines.append("")

    # Answer section (collapsible)
    lines.append("<details>")
    lines.append("<summary>Show Answer</summary>")
    lines.append("")

    correct = problem.get('correct_answer', '?')
    lines.append(f"**Correct: ({correct})**")
    lines.append("")

    explanation = problem.get('explanation', '')
    if explanation:
        lines.append(explanation)
        lines.append("")

    key_insight = problem.get('key_insight', '')
    if key_insight:
        lines.append(f"**Key Insight:** {key_insight}")
        lines.append("")

    partial = problem.get('partial_credit', {})
    if partial:
        lines.append("**Partial Credit:**")
        for letter, reason in partial.items():
            if letter != '_info':
                lines.append(f"- ({letter}) {reason}")
        lines.append("")

    tricks = problem.get('trick_answers', {})
    if tricks:
        lines.append("**Watch Out:**")
        for letter, reason in tricks.items():
            if letter == '_general':
                lines.append(f"- {reason}")
            else:
                lines.append(f"- ({letter}) {reason}")
        lines.append("")

    lines.append("</details>")
    lines.append("")
    lines.append("---")
    lines.append("")

    return '\n'.join(lines)


def generate_weekly_markdown(problems: list[dict], output_dir: Path):
    """Generate markdown files organized by week."""
    by_week_dir = output_dir / "by_week"
    by_week_dir.mkdir(exist_ok=True)

    # Group problems by week
    problems_by_week = {}
    for p in problems:
        week = p.get('week')
        if week:
            if week not in problems_by_week:
                problems_by_week[week] = []
            problems_by_week[week].append(p)

    # Generate a file for each week
    for week in sorted(problems_by_week.keys()):
        week_problems = problems_by_week[week]
        topic = WEEK_TOPICS.get(week, "Unknown Topic")
        filename = f"week{week:02d}_{topic.lower().replace(' ', '_').replace('&', 'and')}.md"

        lines = []
        lines.append(f"# Week {week}: {topic}")
        lines.append("")
        lines.append(f"*{len(week_problems)} problems*")
        lines.append("")

        # List topics covered
        all_concepts = set()
        for p in week_problems:
            all_concepts.update(p.get('concepts_tested', []))

        if all_concepts:
            lines.append("## Topics Covered")
            for concept in sorted(all_concepts):
                lines.append(f"- {concept}")
            lines.append("")

        lines.append("---")
        lines.append("")

        # Add each problem
        for problem in sorted(week_problems, key=lambda x: (x['quiz'], x['problem_number'])):
            lines.append(format_problem_markdown(problem))

        filepath = by_week_dir / filename
        filepath.write_text('\n'.join(lines), encoding='utf-8')
        print(f"  Generated {filename}")


def generate_quiz_markdown(problems: list[dict], output_dir: Path):
    """Generate markdown files organized by quiz."""
    by_quiz_dir = output_dir / "by_quiz"
    by_quiz_dir.mkdir(exist_ok=True)

    # Group problems by quiz
    problems_by_quiz = {}
    for p in problems:
        quiz = p.get('quiz')
        if quiz:
            if quiz not in problems_by_quiz:
                problems_by_quiz[quiz] = []
            problems_by_quiz[quiz].append(p)

    # Generate a file for each quiz
    for quiz in sorted(problems_by_quiz.keys()):
        quiz_problems = problems_by_quiz[quiz]
        coverage = QUIZ_COVERAGE.get(quiz, (0, 0, "Unknown"))
        filename = f"quiz{quiz}_{coverage[2].lower().replace(' ', '_').replace('-', '_')}.md"

        lines = []
        lines.append(f"# Quiz {quiz}: {coverage[2]}")
        lines.append("")
        lines.append(f"*{len(quiz_problems)} problems*")
        lines.append("")

        # Week breakdown
        week_counts = {}
        for p in quiz_problems:
            w = p.get('week')
            if w:
                week_counts[w] = week_counts.get(w, 0) + 1

        lines.append("## Week Breakdown")
        for w in sorted(week_counts.keys()):
            topic = WEEK_TOPICS.get(w, "Unknown")
            lines.append(f"- Week {w} ({topic}): {week_counts[w]} problems")
        lines.append("")

        lines.append("---")
        lines.append("")

        # Add each problem
        for problem in sorted(quiz_problems, key=lambda x: x['problem_number']):
            lines.append(format_problem_markdown(problem))

        filepath = by_quiz_dir / filename
        filepath.write_text('\n'.join(lines), encoding='utf-8')
        print(f"  Generated {filename}")


def main():
    base_dir = Path(__file__).parent.parent
    problems_file = base_dir / "problems.json"

    if not problems_file.exists():
        print(f"Error: {problems_file} not found. Run parse_quizzes.py first.")
        return

    with open(problems_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    problems = data.get('problems', [])
    print(f"Loaded {len(problems)} problems")

    print("\nGenerating weekly markdown files...")
    generate_weekly_markdown(problems, base_dir)

    print("\nGenerating quiz markdown files...")
    generate_quiz_markdown(problems, base_dir)

    print("\nDone!")


if __name__ == "__main__":
    main()
