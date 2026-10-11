# Design (LLD) — Airway Trainer (Educational): Quiz Engine

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| Question | One multiple-choice question: prompt, options, and the correct index. |
| Quiz | Holds questions and runs auto-answered or interactive quiz sessions with scoring. |

## Functions

| Function | Signature | Description |
|---|---|---|
| Question.check | check(self, choice: int) -> bool | True when the 1-based choice matches the correct option. |
| Question.correct_text | correct_text(self) -> str | The text of the correct option. |
| Quiz.add_question | add_question(self, question: Question) -> None | Append a question to the quiz. |
| Quiz.run_auto | run_auto(self, accuracy: float, seed: int) -> dict | Simulate a test taker with per-question accuracy; return results plus score. |
| Quiz.run_interactive | run_interactive(self) -> dict | Ask each question via input(); return results plus score. |
| Quiz.grade | grade(percent: float) -> str | Letter grade for a 0-100 score. |
| build_questions | build_questions(rng: random.Random) -> list | Build the question bank; option order is shuffled deterministically. |
| print_report | print_report(quiz: Quiz, outcome: dict) -> None | Print the per-question breakdown plus score and grade. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Auto-answered demo by default; --interactive to answer yourself. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Airway Trainer (Educational):

| Parameter | Meaning |
|---|---|
| cases | synthetic case count |
| findings | assessment findings |
| plans | airway plans |

## Algorithm & Complexity

The core of this project is Seeded shuffle of options; simulated test taker with configurable accuracy.

- **Time complexity:** O(q) per session over q questions
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/healthcare/clinical_tools/airway-trainer-quiz_engine-intermediate
python3 src/main.py --help
python3 src/main.py
```
--interactive answers the quiz via input(); --accuracy and --num-questions tune the auto-answered demo.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
