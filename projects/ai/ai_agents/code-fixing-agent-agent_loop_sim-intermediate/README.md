# Code Fixing Agent: Agent_Loop_Sim

**Domain:** ai | **Subdomain:** ai_agents | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Code Fixing Agent built as a agent_loop_sim. A code-fixing agent reproduces a reported bug in a sandbox, proposes a patch, runs the test suite, and iterates until tests pass. Regression checks make sure the fix does not break unrelated tests. The simulation plants known bugs and measures fix rate within the attempt budget. A ReAct-style agent loop simulator that cycles Thought, Action, and Observation over a calculator and a lookup table until it reaches a final answer.

**Core concept — Code Fixing Agent:** A code-fixing agent reproduces a reported bug in a sandbox, proposes a patch, runs the test suite, and iterates until tests pass. Regression checks make sure the fix does not break unrelated tests. The simulation plants known bugs and measures fix rate within the attempt budget.

**Why this matters in the real world:** Developer tools auto-fix failing tests and lint errors in CI.

---

## Features

- **Agent**: ReAct agent: think picks a tool, act calls it, observe formats the result, run loops to a final answer.
- **LookupTable**: Seeded key-value table exposed as a lookup tool.
- `make_calculator` (`make_calculator()`): Safe arithmetic evaluator built on the ast module.
- `make_lookup` (`make_lookup(seed: int) -> LookupTable`): Build the seeded lookup table for the demo.
- `Agent.think` (`think(self, question: str, history: list) -> tuple`): Decide the next action: (thought, tool_name, arg) or a final answer.
- `Agent.act` (`act(self, tool_name: str, arg: str)`): Call the named tool with the argument; returns the raw result.
- `Agent.observe` (`observe(self, result) -> str`): Format a tool result as an observation string.
- `Agent.run` (`run(self, question: str) -> str`): Thought/Action/Observation loop; returns the final answer.
- `run_demo` (`run_demo(seed: int) -> int`): Seeded demo: run the agent on three questions and print traces.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Entry point: seeded agent loop demo.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random, re, ast

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Rule-based ReAct loop: regex thought picks calculator for arithmetic or the lookup table for stored keys; observations feed the final answer.. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(S) for S loop steps; each step is a regex scan plus one tool call.. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/ai/ai_agents/code-fixing-agent-agent_loop_sim-intermediate
python3 src/main.py --help
python3 src/main.py
```
--steps caps the loop; --question runs a single custom question instead of the seeded set.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints the full Thought/Action/Observation trace for each demo question plus its final answer.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
