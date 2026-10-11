# MCP Cancellation Flow Simulator: Rate Limiter

**Domain:** ai | **Subdomain:** mcp_integrations | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

MCP Cancellation Flow Simulator built as a rate limiter. Cancellation stops in-flight requests: clients send cancel notifications, and servers must halt work and release resources promptly. Idempotent handlers tolerate duplicate cancels, and timeouts bound how long a cancel takes. The simulator injects seeded cancellations and measures stop latency and cleanup. A token-bucket rate limiter that refills continuously over time and reports allow/deny decisions for a scripted request schedule.

**Core concept — MCP Cancellation Flow Simulator:** Cancellation stops in-flight requests: clients send cancel notifications, and servers must halt work and release resources promptly. Idempotent handlers tolerate duplicate cancels, and timeouts bound how long a cancel takes. The simulator injects seeded cancellations and measures stop latency and cleanup.

**Why this matters in the real world:** Interactive agents let users stop runaway tool calls.

---

## Features

- **FakeClock**: Deterministic clock for the demo: time moves only when advance() is called.
- **TokenBucket**: Token-bucket rate limiter with continuous refill and an injectable clock.
- `FakeClock.advance` (`advance(self, dt: float) -> None`): Move the fake clock forward by dt seconds.
- `TokenBucket.peek` (`peek(self) -> float`): Tokens currently available, after refilling up to now.
- `TokenBucket.allow` (`allow(self) -> bool`): Consume one token if available; True means allowed, False denied.
- `TokenBucket.stats` (`stats(self) -> dict`): Allowed/denied counters and the admission rate.
- `run_demo` (`run_demo(seed: int, rate: float, capacity: int, n_requests: int) -> int`): Replay a seeded bursty arrival schedule against the bucket and print decisions.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Parse flags and run the rate-limiter demo, returning the exit code.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random, time

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Token bucket with continuous time-based refill. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(1) per allow() call. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/ai/mcp_integrations/mcp-cancellation-flow-rate_limiter-beginner
python3 src/main.py --help
python3 src/main.py
```
--rate, --capacity, and --requests override the demo configuration from {'cancel_points': 'injection points per request', 'num_requests': 'requests tested', 'timeout_ms': 'cancellation timeout'}.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints a per-request table (request number, timestamp, tokens, ALLOW/DENY) plus the admission-rate summary.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
