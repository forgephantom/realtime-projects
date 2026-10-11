# RACI Matrix Builder: Task Queue

**Domain:** business_analyst | **Subdomain:** process_modeling | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

RACI Matrix Builder built as a task queue. A RACI matrix assigns each activity one accountable owner, responsible doers, consulted parties, and informed watchers. Exactly one accountable per row is the rule that prevents diffusion of ownership. The builder assembles the matrix and flags rows with zero or multiple accountable owners. A multithreaded task queue that fans jobs out to a worker pool and reports per-job timing and result digests.

**Core concept — RACI Matrix Builder:** A RACI matrix assigns each activity one accountable owner, responsible doers, consulted parties, and informed watchers. Exactly one accountable per row is the rule that prevents diffusion of ownership. The builder assembles the matrix and flags rows with zero or multiple accountable owners.

**Why this matters in the real world:** Project managers publish RACI matrices so everyone knows who decides and who does.

---

## Features

- **Job**: A unit of work with a numeric id, a kind label, and a payload string.
- **TaskQueue**: Thread-pool queue that runs Jobs on worker threads and records per-job results.
- `TaskQueue.submit` (`submit(self, job: Job) -> None`): Enqueue a Job for the worker threads.
- `TaskQueue.run` (`run(self) -> None`): Start workers, wait until the queue drains, then shut them down.
- `TaskQueue.results` (`results(self) -> list`): Completed (job_id, kind, worker, elapsed_ms, digest) rows sorted by job id.
- `TaskQueue.stats` (`stats(self) -> dict`): Aggregate job count plus total and mean elapsed milliseconds.
- `make_jobs` (`make_jobs(n: int, kinds: list, rng: random.Random) -> list`): Build n demo Job objects with seeded random payloads.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Submit demo jobs, run the queue, print the results table, return exit code.

---

## Tech Stack

Python 3.8+, stdlib: argparse, hashlib, queue, random, threading, time

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Thread-pool work queue with a shared queue.Queue and sentinel shutdown. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(1) enqueue/dequeue; wall time scales with jobs/workers. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/business_analyst/process_modeling/raci-matrix-builder-task_queue-beginner
python3 src/main.py --help
python3 src/main.py
```
--workers, --jobs, and --kinds override the demo configuration from {'activities': 'process activities as rows', 'assignments': 'RACI letters per cell', 'roles': 'roles as columns'}.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints a per-job table (id, kind, worker, elapsed ms, digest) plus aggregate timing stats.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
