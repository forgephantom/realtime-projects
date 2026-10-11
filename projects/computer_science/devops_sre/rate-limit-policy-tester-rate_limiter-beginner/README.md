# Rate Limit Policy Tester: Rate Limiter

**Domain:** computer_science | **Subdomain:** devops_sre | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Rate Limit Policy Tester built as a rate limiter. Rate limits protect backends, but misconfigured ones block legitimate users or let abuse through. The tester fires scripted request patterns at a simulated limiter, verifying allow and deny decisions match policy across burst, sustained, and distributed scenarios. Policy becomes testable code. A token-bucket rate limiter that refills continuously over time and reports allow/deny decisions for a scripted request schedule.

**Core concept — Rate Limit Policy Tester:** Rate limits protect backends, but misconfigured ones block legitimate users or let abuse through. The tester fires scripted request patterns at a simulated limiter, verifying allow and deny decisions match policy across burst, sustained, and distributed scenarios. Policy becomes testable code.

**Why this matters in the real world:** Used by API teams validating throttling behavior.

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
cd projects/computer_science/devops_sre/rate-limit-policy-tester-rate_limiter-beginner
python3 src/main.py --help
python3 src/main.py
```
--rate, --capacity, and --requests override the demo configuration from {'policies': 'token bucket, fixed window, sliding', 'scenarios': 'burst, sustained, distributed', 'expectations': 'allowed versus denied per scenario', 'headers': 'retry-after and limit headers checked'}.

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
