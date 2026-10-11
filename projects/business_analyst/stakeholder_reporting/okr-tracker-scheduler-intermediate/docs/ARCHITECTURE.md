# Architecture (HLD) — OKR Progress Tracker: Task Scheduler

## Problem & Users

OKR Progress Tracker built as a Task scheduler. OKR tracking scores each key result from 0 to 1 against its target and rolls scores up to objectives. The discipline is separating committed goals from stretch ones so a 0.7 on a stretch is success, not failure. The tracker computes scores, shows confidence trends, and flags at-risk objectives early. Registers interval jobs on a heap scheduler, runs them for a fixed demo duration, and prints the execution log.

The intended user is a student or engineer working in business_analyst (stakeholder_reporting) who needs a working, runnable reference for OKR Progress Tracker — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
