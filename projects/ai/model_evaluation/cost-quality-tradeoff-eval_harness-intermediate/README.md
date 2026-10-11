# Cost-Quality Tradeoff Analyzer: Eval_Harness

**Domain:** ai | **Subdomain:** model_evaluation | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Cost-Quality Tradeoff Analyzer built as a eval_harness. Every model choice trades quality against cost per token and latency. The analyzer plots the Pareto frontier across candidate models so teams can pick the cheapest model that clears a quality bar. Routing easy queries to small models and hard ones to large models beats any single model on the frontier. An evaluation harness that runs test cases against a stub model, measures accuracy and latency, and adds an LLM-as-judge rubric score per case.

**Core concept — Cost-Quality Tradeoff Analyzer:** Every model choice trades quality against cost per token and latency. The analyzer plots the Pareto frontier across candidate models so teams can pick the cheapest model that clears a quality bar. Routing easy queries to small models and hard ones to large models beats any single model on the frontier.

**Why this matters in the real world:** AI platforms route queries across model tiers to control inference spend.

---

## Features

- `build_cases` (`build_cases(seed: int, n: int = 8) -> list`): Seeded arithmetic test cases with expected answers.
- `stub_model` (`stub_model(case: dict, seed: int) -> str`): Deterministic stub model: usually right, sometimes off by one.
- `run_case` (`run_case(case: dict, model_fn, seed: int) -> dict`): Run one case: model output, latency, exact-match correctness.
- `judge_score` (`judge_score(output: str, rubric: dict) -> float`): LLM-as-judge sim: rubric checks over the output text, 0..1.
- `summarize` (`summarize(results: list, judged: list) -> dict`): Aggregate accuracy, avg/p95 latency, and average judge score.
- `run_demo` (`run_demo(seed: int) -> int`): Seeded demo: run cases, judge them, print the table and summary.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Entry point: seeded eval harness demo.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random, time, zlib

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Each case runs a seeded stub model with latency timing, correctness is exact-match, and an LLM-as-judge rubric scores the output text.. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(N) over N test cases; each case is one stub call plus rubric checks.. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/ai/model_evaluation/cost-quality-tradeoff-eval_harness-intermediate
python3 src/main.py --help
python3 src/main.py
```
--cases sets the number of seeded test cases; the judge rubric lives in build_rubric().

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints a per-case table (input, expected, output, correct, latency, judge score) and a summary line with accuracy and latency stats.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
