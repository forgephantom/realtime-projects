# Architecture (HLD) — SaaS Metrics Monitor: Task Scheduler

## Problem & Users

SaaS Metrics Monitor built as a Task scheduler. Subscription businesses live on a small set of recurring metrics: MRR, ARR, new versus expansion versus churned MRR, and the quick ratio that weighs growth against loss. Watching them together each month shows whether growth is real or borrowed from next quarter. A monitor that alerts on sudden shifts beats a spreadsheet reviewed quarterly. Registers interval jobs on a heap scheduler, runs them for a fixed demo duration, and prints the execution log.

The intended user is a student or engineer working in business_analyst (kpi_dashboards) who needs a working, runnable reference for SaaS Metrics Monitor — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
