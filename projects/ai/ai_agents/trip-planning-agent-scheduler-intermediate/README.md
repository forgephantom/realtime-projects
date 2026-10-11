# Trip Planning Agent Sim: Task Scheduler

**Domain:** ai | **Subdomain:** ai_agents | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Trip Planning Agent Sim built as a Task scheduler. A trip-planning agent turns constraints like budget, dates, and interests into a day-by-day itinerary with bookings and backups. It balances travel time against activity density and flags infeasible legs. Constraint relaxation proposes trade-offs when no plan fits the budget. Registers interval jobs on a heap scheduler, runs them for a fixed demo duration, and prints the execution log.

**Core concept — Trip Planning Agent Sim:** A trip-planning agent turns constraints like budget, dates, and interests into a day-by-day itinerary with bookings and backups. It balances travel time against activity density and flags infeasible legs. Constraint relaxation proposes trade-offs when no plan fits the budget.

**Why this matters in the real world:** Travel assistants build personalized itineraries from natural-language requests.

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
cd projects/ai/ai_agents/trip-planning-agent-scheduler-intermediate
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
