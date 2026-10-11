# Architecture (HLD) — Burnout Signal Monitor: Monitoring Agent

## Problem & Users

Burnout Signal Monitor built as a Monitoring agent. Burnout monitors combine workload, sleep, and self-reported exhaustion signals into early-warning indicators, flagging sustained overload patterns rather than single bad days. The tool frames results as wellness prompts to rest and rebalance, with clear text that it is not a medical assessment. Includes prominent disclaimer text that the tool is for wellness self-tracking and screening only, never a diagnosis, and encourages consulting a professional. Samples synthetic topic metrics for N cycles, evaluates each reading against thresholds, prints readings and alerts.

The intended user is a student or engineer working in healthcare (mental_health_tech) who needs a working, runnable reference for Burnout Signal Monitor — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| Monitor | main | Samples metrics, evaluates thresholds, and collects alerts. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
seeded RNG -> read_metrics (cpu, memory, latency)
reading -> check_thresholds -> alert strings
Monitor.run: sample, print, alert, sleep -> summary
```

## Storage

In-memory only: readings and alerts are printed to stdout and kept in a list for the run summary; nothing is persisted.

## Scaling & Limits

Single-process in-memory sampling; real fleet monitoring would need persistence, alerting integrations, and horizontal collectors.

## Trade-offs

Synthetic seeded metrics keep the demo self-contained and deterministic, at the cost of not observing any real system.

## Failure Handling

A reading exactly at the threshold does not alert (strictly-greater comparison); with zero cycles the run prints only the summary line.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
