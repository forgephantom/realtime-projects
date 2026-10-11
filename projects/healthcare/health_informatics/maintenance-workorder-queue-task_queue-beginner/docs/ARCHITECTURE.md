# Architecture (HLD) — Facilities Work-Order Queue: Task Queue

## Problem & Users

Facilities Work-Order Queue built as a task queue. A hospital facilities ticket system for synthetic work orders with priority, trade, location, and SLA targets. It ages open tickets, escalates SLA breaches, and reports completion rates by trade. Technicians are fictional staff. A multithreaded task queue that fans jobs out to a worker pool and reports per-job timing and result digests.

The intended user is a student or engineer working in healthcare (health_informatics) who needs a working, runnable reference for Facilities Work-Order Queue — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| Job | main | A unit of work with a numeric id, a kind label, and a payload string. |
| TaskQueue | main | Thread-pool queue that runs Jobs on worker threads and records per-job results. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
jobs -> TaskQueue.submit -> queue.Queue
queue.Queue -> worker threads -> (job_id, digest, ms) rows
rows -> TaskQueue.results (sorted) -> printed table + stats
```

## Storage

In-memory only: queued jobs and results live in process memory and are gone when the program exits.

## Scaling & Limits

Single process and GIL-bound; fine for dozens of workers on I/O or hashing-style work, not a substitute for a distributed queue.

## Trade-offs

Threads keep the code simple versus processes, at the cost of true parallelism for CPU-heavy jobs under the GIL.

## Failure Handling

Per-job exceptions are captured as ERROR digests so one bad job cannot kill a worker; shutdown uses sentinels for a clean join.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
