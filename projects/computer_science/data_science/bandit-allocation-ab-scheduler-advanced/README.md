# Bandit Allocation for A/B Tests: Task Scheduler

**Domain:** computer_science | **Subdomain:** data_science | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

Bandit Allocation for A/B Tests built as a Task scheduler. Bandits adapt traffic toward winning variants during the test, reducing opportunity cost: Thompson sampling reallocates as evidence accumulates. The trade-off is biased estimation versus fixed-horizon tests, so the demo compares regret against statistical power. It suits optimization more than learning. Registers interval jobs on a heap scheduler, runs them for a fixed demo duration, and prints the execution log.

**Core concept — Bandit Allocation for A/B Tests:** Bandits adapt traffic toward winning variants during the test, reducing opportunity cost: Thompson sampling reallocates as evidence accumulates. The trade-off is biased estimation versus fixed-horizon tests, so the demo compares regret against statistical power. It suits optimization more than learning.

**Why this matters in the real world:** Dynamic creative optimization and always-on testing use bandit allocation.

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
cd projects/computer_science/data_science/bandit-allocation-ab-scheduler-advanced
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
