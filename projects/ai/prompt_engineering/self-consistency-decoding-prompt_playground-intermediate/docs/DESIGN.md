# Design (LLD) — Self-Consistency Decoding: Prompt_Playground

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
| render_template | render_template(template: str, variables: dict) -> str | Substitute {placeholders} with variables; unknown keys stay literal. |
| build_variants | build_variants() -> dict | The A/B prompt variants sharing the same variable slots. |
| make_inputs | make_inputs(seed: int, n: int = 6) -> list | Seeded test inputs: topic plus a sampled question each. |
| stub_generate | stub_generate(prompt: str, variant: str, topic: str) -> str | Deterministic stand-in model: prompt hash picks canned content. |
| score_response | score_response(response: str, variables: dict, rubric: dict) -> float | Heuristic 0..1 score: topic term, required words, length bounds. |
| run_variant | run_variant(name: str, template: str, inputs: list, rubric: dict) -> dict | Run one variant over all inputs; returns per-input scores. |
| print_table | print_table(results: dict) -> None | Print the variant-by-input score table and the winner. |
| run_demo | run_demo(seed: int) -> int | Seeded demo: render prompts, score both variants, print the table. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Entry point: seeded prompt playground demo. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Self-Consistency Decoding:

| Parameter | Meaning |
|---|---|
| majority_rule | how ties are broken |
| problem_count | problems in the test set |
| samples | reasoning paths per problem |

## Algorithm & Complexity

The core of this project is Deterministic stub generation keyed by prompt hash, scored by a rubric heuristic over topic terms, required words, and length bounds..

- **Time complexity:** O(V*I) for V variants over I test inputs; scoring is linear in response length.
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/ai/prompt_engineering/self-consistency-decoding-prompt_playground-intermediate
python3 src/main.py --help
python3 src/main.py
```
--inputs sets the number of seeded test questions; the rubric lives in build_rubric().

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
