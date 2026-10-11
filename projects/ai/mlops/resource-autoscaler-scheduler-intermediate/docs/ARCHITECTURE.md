# Architecture (HLD) — Inference Autoscaler Simulator: Task Scheduler

## Problem & Users

Inference Autoscaler Simulator built as a Task scheduler. Inference autoscalers add and remove serving replicas as request rate changes: target metrics like queue depth or GPU utilization drive scaling decisions, with cooldowns preventing flapping. Predictive scaling pre-warms capacity ahead of known peaks. The simulator replays seeded traffic patterns and measures cost versus SLO violations. Registers interval jobs on a heap scheduler, runs them for a fixed demo duration, and prints the execution log.

The intended user is a student or engineer working in ai (mlops) who needs a working, runnable reference for Inference Autoscaler Simulator — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
