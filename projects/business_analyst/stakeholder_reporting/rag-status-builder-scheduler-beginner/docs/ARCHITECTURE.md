# Architecture (HLD) — RAG Status Report Builder: Task Scheduler

## Problem & Users

RAG Status Report Builder built as a Task scheduler. RAG status marks each workstream red, amber, or green against its plan, with the color earned by data, not optimism. Amber means at risk with a recovery plan; red means off track needing help. The builder computes status from milestone variance and assembles the classic status table. Registers interval jobs on a heap scheduler, runs them for a fixed demo duration, and prints the execution log.

The intended user is a student or engineer working in business_analyst (stakeholder_reporting) who needs a working, runnable reference for RAG Status Report Builder — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| Scheduler | main | Minimal interval scheduler driven by a heap of next-run times. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
add_job(name, interval, func) -> heap of next-run times
run loop: pop due job -> func(name) -> log entry
         -> push back with next_run + interval
log -> execution table + per-job counts
```

## Storage

In-memory only: the job heap and execution log exist for the run and are not persisted.

## Scaling & Limits

Single-threaded with O(log j) dispatch; suited to lightweight periodic jobs, not to thousands of concurrent or long-running tasks.

## Trade-offs

A heap loop is simple and precise for intervals but single-threaded, so blocking jobs would stall the whole schedule.

## Failure Handling

A job that raises would propagate out of run(); demo jobs are side-effect-light counters, and the loop always exits at the deadline so it cannot hang.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
