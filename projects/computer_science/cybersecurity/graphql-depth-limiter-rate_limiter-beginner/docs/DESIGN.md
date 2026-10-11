# Design (LLD) — GraphQL Depth Limiter: Rate Limiter

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| FakeClock | Deterministic clock for the demo: time moves only when advance() is called. |
| TokenBucket | Token-bucket rate limiter with continuous refill and an injectable clock. |

## Functions

| Function | Signature | Description |
|---|---|---|
| FakeClock.advance | advance(self, dt: float) -> None | Move the fake clock forward by dt seconds. |
| TokenBucket.peek | peek(self) -> float | Tokens currently available, after refilling up to now. |
| TokenBucket.allow | allow(self) -> bool | Consume one token if available; True means allowed, False denied. |
| TokenBucket.stats | stats(self) -> dict | Allowed/denied counters and the admission rate. |
| run_demo | run_demo(seed: int, rate: float, capacity: int, n_requests: int) -> int | Replay a seeded bursty arrival schedule against the bucket and print decisions. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Parse flags and run the rate-limiter demo, returning the exit code. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for GraphQL Depth Limiter:

| Parameter | Meaning |
|---|---|
| max_depth | nesting depth permitted |
| max_cost | computed complexity budget |
| cost_weights | per-field resolution costs |
| introspection | whether introspection queries are allowed |

## Algorithm & Complexity

The core of this project is Token bucket with continuous time-based refill.

- **Time complexity:** O(1) per allow() call
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/cybersecurity/graphql-depth-limiter-rate_limiter-beginner
python3 src/main.py --help
python3 src/main.py
```
--rate, --capacity, and --requests override the demo configuration from {'max_depth': 'nesting depth permitted', 'max_cost': 'computed complexity budget', 'cost_weights': 'per-field resolution costs', 'introspection': 'whether introspection queries are allowed'}.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
