# Rolling Forecast Engine: Task Scheduler

**Domain:** business_analyst | **Subdomain:** financial_modeling | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Rolling Forecast Engine built as a Task scheduler. A rolling forecast drops the oldest month and adds a new one every cycle, so the plan always looks twelve or eighteen months ahead. It adapts to reality instead of freezing a budget made last fall. The engine part is automating driver-based updates so reforecasting takes days, not weeks. Registers interval jobs on a heap scheduler, runs them for a fixed demo duration, and prints the execution log.

**Core concept — Rolling Forecast Engine:** A rolling forecast drops the oldest month and adds a new one every cycle, so the plan always looks twelve or eighteen months ahead. It adapts to reality instead of freezing a budget made last fall. The engine part is automating driver-based updates so reforecasting takes days, not weeks.

**Why this matters in the real world:** FP&A teams run rolling forecasts to keep plans current without annual budget theater.

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
cd projects/business_analyst/financial_modeling/rolling-forecast-engine-scheduler-intermediate
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
