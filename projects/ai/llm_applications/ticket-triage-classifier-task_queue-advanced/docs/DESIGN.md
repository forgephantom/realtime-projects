# Design (LLD) — Support Ticket Triage: Task Queue

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| Job | A unit of work with a numeric id, a kind label, and a payload string. |
| TaskQueue | Thread-pool queue that runs Jobs on worker threads and records per-job results. |

## Functions

| Function | Signature | Description |
|---|---|---|
| TaskQueue.submit | submit(self, job: Job) -> None | Enqueue a Job for the worker threads. |
| TaskQueue.run | run(self) -> None | Start workers, wait until the queue drains, then shut them down. |
| TaskQueue.results | results(self) -> list | Completed (job_id, kind, worker, elapsed_ms, digest) rows sorted by job id. |
| TaskQueue.stats | stats(self) -> dict | Aggregate job count plus total and mean elapsed milliseconds. |
| make_jobs | make_jobs(n: int, kinds: list, rng: random.Random) -> list | Build n demo Job objects with seeded random payloads. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Submit demo jobs, run the queue, print the results table, return exit code. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Support Ticket Triage:

| Parameter | Meaning |
|---|---|
| priority_weights | urgency signal weights |
| queues | support queue definitions |
| sla_hours | response targets per priority |

## Algorithm & Complexity

The core of this project is Thread-pool work queue with a shared queue.Queue and sentinel shutdown.

- **Time complexity:** O(1) enqueue/dequeue; wall time scales with jobs/workers
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/ai/llm_applications/ticket-triage-classifier-task_queue-advanced
python3 src/main.py --help
python3 src/main.py
```
--workers, --jobs, and --kinds override the demo configuration from {'priority_weights': 'urgency signal weights', 'queues': 'support queue definitions', 'sla_hours': 'response targets per priority'}.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
