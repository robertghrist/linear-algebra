#!/usr/bin/env python3
"""
ESE 2030 Problem Bank - Self-Study Quiz Tool

A simple CLI tool for practicing linear algebra problems.
"""

import json
import random
import argparse
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


def load_problems(problems_file: Path) -> list[dict]:
    """Load problems from JSON file."""
    with open(problems_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('problems', [])


def filter_problems(problems: list[dict], week: int = None, quiz: int = None,
                    topic: str = None) -> list[dict]:
    """Filter problems based on criteria."""
    filtered = problems

    if week:
        filtered = [p for p in filtered if p.get('week') == week]

    if quiz:
        filtered = [p for p in filtered if p.get('quiz') == quiz]

    if topic:
        topic_lower = topic.lower()
        filtered = [p for p in filtered
                    if any(topic_lower in t.lower() for t in p.get('topics', []))
                    or any(topic_lower in c.lower() for c in p.get('concepts_tested', []))]

    return filtered


def display_problem(problem: dict, problem_num: int, total: int):
    """Display a problem for the user."""
    print()
    print("=" * 60)
    print(f"[{problem_num}/{total}] {problem['id']} - Week {problem.get('week', '?')}: {problem.get('chapter_topic', 'Unknown')}")
    print("=" * 60)
    print()

    # Statement
    statement = problem.get('statement', 'No statement available')
    # Simple cleanup for terminal display
    statement = statement.replace('\\\\', '\n')
    statement = statement.replace('\\begin{itemize}', '').replace('\\end{itemize}', '')
    statement = statement.replace('\\begin{enumerate}', '').replace('\\end{enumerate}', '')
    statement = statement.replace('\\item', '\n  *')
    print(statement)
    print()

    # Choices
    for choice in problem.get('choices', []):
        print(f"  ({choice['label']}) {choice['text']}")
    print()


def display_answer(problem: dict, user_answer: str):
    """Display the answer and explanation."""
    correct = problem.get('correct_answer', '?')
    is_correct = user_answer.upper() == correct.upper()

    print()
    if is_correct:
        print("✓ CORRECT!")
    else:
        print(f"✗ Incorrect. The correct answer is ({correct})")

    print()

    # Explanation
    explanation = problem.get('explanation', '')
    if explanation:
        print("Explanation:")
        # Simple cleanup
        explanation = explanation.replace('\\begin{itemize}', '').replace('\\end{itemize}', '')
        explanation = explanation.replace('\\begin{enumerate}', '').replace('\\end{enumerate}', '')
        explanation = explanation.replace('\\item', '\n  *')
        explanation = explanation.replace('\\textbf{', '').replace('}', '')
        print(explanation[:500] + "..." if len(explanation) > 500 else explanation)
        print()

    # Key insight
    key_insight = problem.get('key_insight', '')
    if key_insight:
        print(f"Key Insight: {key_insight}")
        print()

    # Partial credit
    partial = problem.get('partial_credit', {})
    if user_answer.upper() in partial:
        print(f"Partial Credit Note: {partial[user_answer.upper()]}")
        print()

    return is_correct


def run_quiz(problems: list[dict], count: int):
    """Run an interactive quiz session."""
    if not problems:
        print("No problems match your criteria.")
        return

    # Select random problems
    if count > len(problems):
        count = len(problems)
        print(f"Only {count} problems available.")

    selected = random.sample(problems, count)

    score = 0
    attempted = 0

    print()
    print("=" * 60)
    print("  ESE 2030 Problem Bank - Quiz Session")
    print("=" * 60)
    print(f"  {count} problems selected")
    print("  Enter A-E to answer, 's' to skip, 'q' to quit")
    print("=" * 60)

    for i, problem in enumerate(selected, 1):
        display_problem(problem, i, count)

        while True:
            try:
                answer = input("Your answer: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\n\nQuiz ended.")
                break

            if answer == 'q':
                print("\nQuiz ended early.")
                break
            elif answer == 's':
                print(f"\nSkipped. Correct answer was ({problem.get('correct_answer', '?')})")
                break
            elif answer in ['a', 'b', 'c', 'd', 'e']:
                attempted += 1
                if display_answer(problem, answer):
                    score += 1
                break
            else:
                print("Please enter A-E, 's' to skip, or 'q' to quit.")

        if answer == 'q':
            break

        input("\nPress Enter to continue...")

    # Final score
    print()
    print("=" * 60)
    print("  Quiz Complete!")
    print("=" * 60)
    if attempted > 0:
        percentage = (score / attempted) * 100
        print(f"  Score: {score}/{attempted} ({percentage:.1f}%)")
    print("=" * 60)
    print()


def list_topics(problems: list[dict]):
    """List all available topics."""
    all_topics = set()
    for p in problems:
        all_topics.update(p.get('topics', []))
        all_topics.update(p.get('concepts_tested', []))

    print("\nAvailable topics:")
    for topic in sorted(all_topics):
        count = len([p for p in problems
                     if topic in p.get('topics', []) or topic in p.get('concepts_tested', [])])
        print(f"  {topic}: {count} problems")


def main():
    parser = argparse.ArgumentParser(
        description='ESE 2030 Problem Bank - Self-Study Quiz Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python quiz_me.py                      # Quiz on 5 random problems
  python quiz_me.py --week 7 --count 10  # 10 problems from Week 7
  python quiz_me.py --quiz 3             # Problems from Quiz 3
  python quiz_me.py --topic eigenvalue   # Problems about eigenvalues
  python quiz_me.py --list-weeks         # Show week topics
  python quiz_me.py --list-topics        # Show all topics
        """
    )

    parser.add_argument('--week', '-w', type=int, choices=range(1, 12),
                        help='Filter by week number (1-11)')
    parser.add_argument('--quiz', '-q', type=int, choices=range(1, 6),
                        help='Filter by quiz number (1-5)')
    parser.add_argument('--topic', '-t', type=str,
                        help='Filter by topic keyword')
    parser.add_argument('--count', '-c', type=int, default=5,
                        help='Number of problems (default: 5)')
    parser.add_argument('--list-weeks', action='store_true',
                        help='List all weeks and topics')
    parser.add_argument('--list-topics', action='store_true',
                        help='List all available topics')

    args = parser.parse_args()

    # Find problems.json
    script_dir = Path(__file__).parent
    problems_file = script_dir.parent / "problems.json"

    if not problems_file.exists():
        print(f"Error: {problems_file} not found.")
        print("Run parse_quizzes.py first to generate the problem database.")
        return

    print("Loading ESE 2030 Problem Bank...")
    problems = load_problems(problems_file)
    print(f"Loaded {len(problems)} problems.")

    if args.list_weeks:
        print("\nWeek Topics:")
        for week, topic in WEEK_TOPICS.items():
            count = len([p for p in problems if p.get('week') == week])
            print(f"  Week {week:2d}: {topic} ({count} problems)")
        return

    if args.list_topics:
        list_topics(problems)
        return

    # Filter problems
    filtered = filter_problems(problems, week=args.week, quiz=args.quiz, topic=args.topic)

    if args.week:
        print(f"Filtering: Week {args.week} ({WEEK_TOPICS.get(args.week, 'Unknown')})")
    if args.quiz:
        print(f"Filtering: Quiz {args.quiz}")
    if args.topic:
        print(f"Filtering: Topic '{args.topic}'")

    print(f"Found {len(filtered)} matching problems.")

    run_quiz(filtered, args.count)


if __name__ == "__main__":
    main()
