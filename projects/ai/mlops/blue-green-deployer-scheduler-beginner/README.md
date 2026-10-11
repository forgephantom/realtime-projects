# Blue-Green Deployment Runner: Task Scheduler

**Domain:** ai | **Subdomain:** mlops | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Blue-Green Deployment Runner built as a Task scheduler. Blue-green deployment runs two full environments and flips a router from blue to green: instant cutover with instant rollback by flipping back. The green environment is validated with smoke tests and shadow traffic before the switch. The runner models both environments on seeded traffic with a failure-injection drill. Registers interval jobs on a heap scheduler, runs them for a fixed demo duration, and prints the execution log.

**Core concept — Blue-Green Deployment Runner:** Blue-green deployment runs two full environments and flips a router from blue to green: instant cutover with instant rollback by flipping back. The green environment is validated with smoke tests and shadow traffic before the switch. The runner models both environments on seeded traffic with a failure-injection drill.

**Why this matters in the real world:** API providers use blue-green flips for zero-downtime model swaps.

---

## Features

- **Scheduler**: Minimal interval scheduler driven by a heap of next-run times.
- `make_demo_job` (`make_demo_job(tag)`): Build a demo job function that counts its own executions.
- `Scheduler.add_job` (`Scheduler.add_job(self, name, interval, func)`): Register `func` to run every `interval` seconds under `name`.
- `Scheduler.run` (`Scheduler.run(self, duration)`): Run scheduled jobs for `duration` seconds; return the log.
- `main` (`main()`): Parse args, register demo jobs, run, and print the log.

---

## Tech Stack

Python 3.8+, stdlib: argparse, heapq, random, time

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Heap-ordered next-run-time scheduling loop. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(log j) per execution for j jobs. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/ai/mlops/blue-green-deployer-scheduler-beginner
python3 src/main.py --help
python3 src/main.py
```

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

A timestamped execution table (time, job, result) plus per-job execution counts and a total.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
