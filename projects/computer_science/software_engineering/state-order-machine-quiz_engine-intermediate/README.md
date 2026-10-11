# State (Order Machine): Quiz Engine

**Domain:** computer_science | **Subdomain:** software_engineering | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

State (Order Machine) built as a quiz engine. The state pattern encodes each state as an object with legal transitions: an order moves new -> paid -> shipped -> delivered, and each state object defines valid next steps. Illegal transitions become impossible by construction. It replaces sprawling switch statements. A multiple-choice quiz engine that shuffles options deterministically, scores auto-answered or interactive sessions, and assigns letter grades.

**Core concept — State (Order Machine):** The state pattern encodes each state as an object with legal transitions: an order moves new -> paid -> shipped -> delivered, and each state object defines valid next steps. Illegal transitions become impossible by construction. It replaces sprawling switch statements.

**Why this matters in the real world:** Order systems, TCP stacks, and game entities model lifecycles as state machines.

---

## Features

- **Question**: One multiple-choice question: prompt, options, and the correct index.
- **Quiz**: Holds questions and runs auto-answered or interactive quiz sessions with scoring.
- `Question.check` (`check(self, choice: int) -> bool`): True when the 1-based choice matches the correct option.
- `Question.correct_text` (`correct_text(self) -> str`): The text of the correct option.
- `Quiz.add_question` (`add_question(self, question: Question) -> None`): Append a question to the quiz.
- `Quiz.run_auto` (`run_auto(self, accuracy: float, seed: int) -> dict`): Simulate a test taker with per-question accuracy; return results plus score.
- `Quiz.run_interactive` (`run_interactive(self) -> dict`): Ask each question via input(); return results plus score.
- `Quiz.grade` (`grade(percent: float) -> str`): Letter grade for a 0-100 score.
- `build_questions` (`build_questions(rng: random.Random) -> list`): Build the question bank; option order is shuffled deterministically.
- `print_report` (`print_report(quiz: Quiz, outcome: dict) -> None`): Print the per-question breakdown plus score and grade.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Auto-answered demo by default; --interactive to answer yourself.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Seeded shuffle of options; simulated test taker with configurable accuracy. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(q) per session over q questions. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/software_engineering/state-order-machine-quiz_engine-intermediate
python3 src/main.py --help
python3 src/main.py
```
--interactive answers the quiz via input(); --accuracy and --num-questions tune the auto-answered demo.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints a per-question breakdown (chosen option, correct/wrong) plus score, percentage, and letter grade.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
