# Canary Deployment Orchestrator: Task Scheduler

**Domain:** ai | **Subdomain:** mlops | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Canary Deployment Orchestrator built as a Task scheduler. Canary deployment shifts a slice of traffic to the new model and watches guardrail metrics before proceeding: error rate, latency, and key business metrics must stay within bounds. Automated analysis promotes or rolls back based on statistical comparison with the stable version. The orchestrator steps traffic percentages on seeded metric streams. Registers interval jobs on a heap scheduler, runs them for a fixed demo duration, and prints the execution log.

**Core concept — Canary Deployment Orchestrator:** Canary deployment shifts a slice of traffic to the new model and watches guardrail metrics before proceeding: error rate, latency, and key business metrics must stay within bounds. Automated analysis promotes or rolls back based on statistical comparison with the stable version. The orchestrator steps traffic percentages on seeded metric streams.

**Why this matters in the real world:** Model platforms canary every production model update before full rollout.

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
cd projects/ai/mlops/canary-deployer-scheduler-beginner
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
