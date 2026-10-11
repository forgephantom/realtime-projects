# Design (LLD) — Prompt Injection Defense Tester: Agent_Loop_Sim

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| Agent | ReAct agent: think picks a tool, act calls it, observe formats the result, run loops to a final answer. |
| LookupTable | Seeded key-value table exposed as a lookup tool. |

## Functions

| Function | Signature | Description |
|---|---|---|
| make_calculator | make_calculator() | Safe arithmetic evaluator built on the ast module. |
| make_lookup | make_lookup(seed: int) -> LookupTable | Build the seeded lookup table for the demo. |
| Agent.think | think(self, question: str, history: list) -> tuple | Decide the next action: (thought, tool_name, arg) or a final answer. |
| Agent.act | act(self, tool_name: str, arg: str) | Call the named tool with the argument; returns the raw result. |
| Agent.observe | observe(self, result) -> str | Format a tool result as an observation string. |
| Agent.run | run(self, question: str) -> str | Thought/Action/Observation loop; returns the final answer. |
| run_demo | run_demo(seed: int) -> int | Seeded demo: run the agent on three questions and print traces. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Entry point: seeded agent loop demo. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Prompt Injection Defense Tester:

| Parameter | Meaning |
|---|---|
| defenses | defense mechanisms enabled |
| documents | test documents |
| payloads | injection payloads |

## Algorithm & Complexity

The core of this project is Rule-based ReAct loop: regex thought picks calculator for arithmetic or the lookup table for stored keys; observations feed the final answer..

- **Time complexity:** O(S) for S loop steps; each step is a regex scan plus one tool call.
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/ai/ai_safety_redteaming/prompt-injection-defense-agent_loop_sim-intermediate
python3 src/main.py --help
python3 src/main.py
```
--steps caps the loop; --question runs a single custom question instead of the seeded set.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
