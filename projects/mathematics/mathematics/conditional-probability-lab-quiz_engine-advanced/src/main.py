#!/usr/bin/env python3
"""Conditional Probability Lab: Quiz Engine.

Conditional probability P(A given B) rescales the sample space to B, and Bayes' rule chains these updates through evidence. Tree diagrams make multi-stage problems mechanical. The lab walks through urn, card, and test-accuracy problems with step-by-step trees.

Demo dataset idea: The demo builds seeded-RNG random urn compositions and verifies tree-computed probabilities against brute-force enumeration..
"""

import argparse
import random

SLUG = "conditional-probability-lab-quiz_engine-advanced"
PARAMS = {'problem': 'preset scenario name', 'show_tree': 'print the probability tree', 'stages': 'number of conditional stages'}


class Question:
    """One multiple-choice question: prompt, options, and the correct index."""

    def __init__(self, prompt: str, options: list, answer: int):
        if not 0 <= answer < len(options):
            raise ValueError("answer index out of range")
        self.prompt = prompt
        self.options = options
        self.answer = answer  # 0-based index into options

    def check(self, choice: int) -> bool:
        """True when the 1-based choice matches the correct option."""
        return (choice - 1) == self.answer

    def correct_text(self) -> str:
        """The text of the correct option."""
        return self.options[self.answer]


class Quiz:
    """A small quiz engine: holds questions, runs auto or interactive sessions."""

    def __init__(self, title: str, questions: list = None):
        self.title = title
        self.questions = list(questions) if questions else []

    def add_question(self, question: Question) -> None:
        """Append a question to the quiz."""
        self.questions.append(question)

    def run_auto(self, accuracy: float, seed: int) -> dict:
        """Simulate a test taker who answers each question correctly with
        probability accuracy; return per-question results plus the score."""
        rng = random.Random(seed)
        results = []
        for question in self.questions:
            if rng.random() < accuracy:
                choice = question.answer + 1
            else:
                wrong = [i for i in range(len(question.options)) if i != question.answer]
                choice = rng.choice(wrong) + 1
            results.append({"question": question,
                            "choice": choice,
                            "correct": question.check(choice)})
        score = sum(1 for r in results if r["correct"])
        return {"results": results, "score": score, "total": len(results)}

    def run_interactive(self) -> dict:
        """Ask each question via input(); return results plus the score."""
        results = []
        for number, question in enumerate(self.questions, 1):
            print("\nQ%d: %s" % (number, question.prompt))
            for i, option in enumerate(question.options, 1):
                print("  %d) %s" % (i, option))
            while True:
                raw = input("Your answer (1-%d, or q to quit): " % len(question.options))
                if raw.strip().lower() == "q":
                    print("Quitting the quiz.")
                    score = sum(1 for r in results if r["correct"])
                    return {"results": results, "score": score,
                            "total": len(self.questions), "quit": True}
                try:
                    choice = int(raw.strip())
                except ValueError:
                    choice = -1
                if 1 <= choice <= len(question.options):
                    break
                print("Please enter a number between 1 and %d." % len(question.options))
            correct = question.check(choice)
            print("Correct!" if correct else "Not quite. Answer: %s" % question.correct_text())
            results.append({"question": question, "choice": choice, "correct": correct})
        score = sum(1 for r in results if r["correct"])
        return {"results": results, "score": score, "total": len(results)}

    @staticmethod
    def grade(percent: float) -> str:
        """Letter grade for a 0-100 score."""
        if percent >= 90:
            return "A"
        if percent >= 80:
            return "B"
        if percent >= 70:
            return "C"
        if percent >= 60:
            return "D"
        return "F"


def build_questions(rng: random.Random) -> list:
    """Build the question bank; option order is shuffled deterministically."""
    topic = "Conditional Probability Lab"
    concept = "Conditional probability P(A given B) rescales the sample space to B, and Bayes' rule chains these updates through evidence. Tree diagrams make multi-stage problems mechanical. The lab walks through urn, card, and test-accuracy problems with step-by-step trees."
    bank = [
        ("Which statement best describes %s?" % topic,
         [concept,
          "A sorting algorithm that orders lists in place",
          "A network protocol for encrypted file transfer",
          "A markup language for styling web pages"], 0),
        ("Running `python3 src/main.py` with no arguments will ...",
         ["Run a scripted demo and exit with status 0",
          "Prompt for a username and password",
          "Open a network connection to the public internet",
          "Delete every file in the working directory"], 0),
        ("Which standard-library module parses this program's command-line flags?",
         ["argparse", "optparse", "click", "getopt"], 0),
        ("The demo run is deterministic because it ...",
         ["Seeds the random number generator from --seed",
          "Downloads the same fixture file on every run",
          "Sleeps a fixed number of seconds between steps",
          "Writes its output to a fixed path in /tmp"], 0),
        ("What does `python3 src/main.py --help` do?",
         ["Print usage information and exit with status 0",
          "Run the demo with extra debug logging",
          "Install the project's dependencies",
          "Open the documentation in a web browser"], 0),
        ("Where is this program allowed to write files?",
         ["Only inside the current working directory (demo_workspace / demo_output)",
          "Anywhere on the filesystem, including system folders",
          "Directly into the user's home directory",
          "To a shared system temp folder used by all users"], 0),
    ]
    questions = []
    for prompt, options, answer in bank:
        order = list(range(len(options)))
        rng.shuffle(order)
        shuffled = [options[i] for i in order]
        questions.append(Question(prompt, shuffled, order.index(answer)))
    return questions


def print_report(quiz: Quiz, outcome: dict) -> None:
    """Print the per-question breakdown plus score and grade."""
    print("Conditional Probability Lab: Quiz Engine  (topic: Conditional Probability Lab)")
    print("Quiz: %s - %d questions\n" % (quiz.title, outcome["total"]))
    for number, row in enumerate(outcome["results"], 1):
        question = row["question"]
        mark = "correct" if row["correct"] else "wrong  "
        print("Q%d [%s] chose %d) %s" % (
            number, mark, row["choice"], question.options[row["choice"] - 1]))
        print("     %s" % question.prompt)
    percent = 100.0 * outcome["score"] / outcome["total"] if outcome["total"] else 0.0
    print("\nScore: %d/%d (%.1f%%) - grade %s" % (
        outcome["score"], outcome["total"], percent, Quiz.grade(percent)))


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Conditional Probability Lab: Quiz Engine: Conditional probability P(A given B) rescales the sample space to B, and Bayes' rule chains these updates through evidence. Tree diagrams make multi-stage problems mechanical. The lab walks through urn, card, and test-accuracy problems with step-by-step trees."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--interactive", action="store_true",
                        help="Answer the quiz yourself via input() prompts.")
    parser.add_argument("--accuracy", type=float, default=None,
                        help="Simulated test-taker accuracy 0-1 (see the topic params).")
    parser.add_argument("--num-questions", type=int, default=None,
                        help="How many questions to ask (see the topic params).")
    return parser


def main(argv=None) -> int:
    """Entry point: auto-answered demo by default, --interactive to play."""
    args = build_parser().parse_args(argv)
    random.seed(args.seed)
    rng = random.Random(args.seed)

    questions = build_questions(rng)
    num = args.num_questions or int(PARAMS.get("num_questions", len(questions)))
    quiz = Quiz("Conditional Probability Lab: Quiz Engine", questions[:num])

    if args.interactive:
        print("Conditional Probability Lab: Quiz Engine  (topic: Conditional Probability Lab)")
        outcome = quiz.run_interactive()
        print_report(quiz, outcome)
        return 0

    accuracy = args.accuracy if args.accuracy is not None else float(
        PARAMS.get("accuracy", 0.75))
    print("Auto-answering with a simulated test taker (accuracy %.0f%%).\n" % (
        100.0 * accuracy))
    outcome = quiz.run_auto(accuracy, args.seed)
    print_report(quiz, outcome)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
