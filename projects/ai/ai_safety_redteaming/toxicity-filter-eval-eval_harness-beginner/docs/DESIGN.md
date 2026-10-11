# Design (LLD) — Toxicity Filter Evaluator: Eval_Harness

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|

## Functions

| Function | Signature | Description |
|---|---|---|
| build_cases | build_cases(seed: int, n: int = 8) -> list | Seeded arithmetic test cases with expected answers. |
| stub_model | stub_model(case: dict, seed: int) -> str | Deterministic stub model: usually right, sometimes off by one. |
| run_case | run_case(case: dict, model_fn, seed: int) -> dict | Run one case: model output, latency, exact-match correctness. |
| judge_score | judge_score(output: str, rubric: dict) -> float | LLM-as-judge sim: rubric checks over the output text, 0..1. |
| summarize | summarize(results: list, judged: list) -> dict | Aggregate accuracy, avg/p95 latency, and average judge score. |
| run_demo | run_demo(seed: int) -> int | Seeded demo: run cases, judge them, print the table and summary. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Entry point: seeded eval harness demo. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Toxicity Filter Evaluator:

| Parameter | Meaning |
|---|---|
| edge_cases | adversarial edge cases |
| num_samples | texts evaluated |
| thresholds | filter thresholds swept |

## Algorithm & Complexity

The core of this project is Each case runs a seeded stub model with latency timing, correctness is exact-match, and an LLM-as-judge rubric scores the output text..

- **Time complexity:** O(N) over N test cases; each case is one stub call plus rubric checks.
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/ai/ai_safety_redteaming/toxicity-filter-eval-eval_harness-beginner
python3 src/main.py --help
python3 src/main.py
```
--cases sets the number of seeded test cases; the judge rubric lives in build_rubric().

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
