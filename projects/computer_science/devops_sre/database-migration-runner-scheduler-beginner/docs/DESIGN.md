# Design (LLD) — Database Migration Runner: Task Scheduler

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| Scheduler | Minimal interval scheduler driven by a heap of next-run times. |

## Functions

| Function | Signature | Description |
|---|---|---|
| make_demo_job | make_demo_job(tag) | Build a demo job function that counts its own executions. |
| Scheduler.add_job | Scheduler.add_job(self, name, interval, func) | Register `func` to run every `interval` seconds under `name`. |
| Scheduler.run | Scheduler.run(self, duration) | Run scheduled jobs for `duration` seconds; return the log. |
| main | main() | Parse args, register demo jobs, run, and print the log. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Database Migration Runner:

| Parameter | Meaning |
|---|---|
| migrations | ordered versioned scripts |
| transactional | all-or-nothing per migration |
| dry_run | shadow execution before real |
| lock_timeout | DDL lock guard |

## Algorithm & Complexity

The core of this project is Heap-ordered next-run-time scheduling loop.

- **Time complexity:** O(log j) per execution for j jobs
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/devops_sre/database-migration-runner-scheduler-beginner
python3 src/main.py --help
python3 src/main.py
```

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
