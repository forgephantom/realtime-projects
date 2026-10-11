# Chain-of-Thought Lab: Prompt_Playground

**Domain:** ai | **Subdomain:** prompt_engineering | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Chain-of-Thought Lab built as a prompt_playground. Chain-of-thought prompting asks the model to reason step by step before answering, which improves accuracy on math and logic problems. The lab compares direct answers against reasoned answers on a seeded problem set. Step-count analysis finds where extra reasoning stops helping. A prompt template playground that substitutes variables into templates, runs A/B variants over seeded test inputs, and scores them with a rubric heuristic.

**Core concept — Chain-of-Thought Lab:** Chain-of-thought prompting asks the model to reason step by step before answering, which improves accuracy on math and logic problems. The lab compares direct answers against reasoned answers on a seeded problem set. Step-count analysis finds where extra reasoning stops helping.

**Why this matters in the real world:** Analytical features use step-by-step reasoning for harder problems.

---

## Features

- `render_template` (`render_template(template: str, variables: dict) -> str`): Substitute {placeholders} with variables; unknown keys stay literal.
- `build_variants` (`build_variants() -> dict`): The A/B prompt variants sharing the same variable slots.
- `make_inputs` (`make_inputs(seed: int, n: int = 6) -> list`): Seeded test inputs: topic plus a sampled question each.
- `stub_generate` (`stub_generate(prompt: str, variant: str, topic: str) -> str`): Deterministic stand-in model: prompt hash picks canned content.
- `score_response` (`score_response(response: str, variables: dict, rubric: dict) -> float`): Heuristic 0..1 score: topic term, required words, length bounds.
- `run_variant` (`run_variant(name: str, template: str, inputs: list, rubric: dict) -> dict`): Run one variant over all inputs; returns per-input scores.
- `print_table` (`print_table(results: dict) -> None`): Print the variant-by-input score table and the winner.
- `run_demo` (`run_demo(seed: int) -> int`): Seeded demo: render prompts, score both variants, print the table.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Entry point: seeded prompt playground demo.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random, re, zlib

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Deterministic stub generation keyed by prompt hash, scored by a rubric heuristic over topic terms, required words, and length bounds.. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(V*I) for V variants over I test inputs; scoring is linear in response length.. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/ai/prompt_engineering/chain-of-thought-lab-prompt_playground-intermediate
python3 src/main.py --help
python3 src/main.py
```
--inputs sets the number of seeded test questions; the rubric lives in build_rubric().

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints rendered prompt samples, a variant-by-input score table with averages, and the winning variant.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
