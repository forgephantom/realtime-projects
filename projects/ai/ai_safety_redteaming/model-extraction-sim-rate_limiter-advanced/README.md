# Model Extraction Probe Simulator: Rate Limiter

**Domain:** ai | **Subdomain:** ai_safety_redteaming | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

Model Extraction Probe Simulator built as a rate limiter. Model extraction attacks query a black-box API to clone its behavior: with enough input-output pairs, an attacker trains a copycat model. Defenses include query rate limits, output watermarking, and monitoring for extraction-like query patterns. The simulator runs seeded query strategies against a mock API and measures copycat fidelity. A token-bucket rate limiter that refills continuously over time and reports allow/deny decisions for a scripted request schedule.

**Core concept — Model Extraction Probe Simulator:** Model extraction attacks query a black-box API to clone its behavior: with enough input-output pairs, an attacker trains a copycat model. Defenses include query rate limits, output watermarking, and monitoring for extraction-like query patterns. The simulator runs seeded query strategies against a mock API and measures copycat fidelity.

**Why this matters in the real world:** API providers monitor for extraction-pattern traffic to protect model IP.

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
cd projects/ai/ai_safety_redteaming/model-extraction-sim-rate_limiter-advanced
python3 src/main.py --help
python3 src/main.py
```
--rate, --capacity, and --requests override the demo configuration from {'budgets': 'query budgets tested', 'num_queries': 'extraction queries', 'strategies': 'query strategies'}.

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
