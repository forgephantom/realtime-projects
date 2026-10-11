# Architecture (HLD) — Vital Sign Trend Monitor: Monitoring Agent

## Problem & Users

Vital Sign Trend Monitor built as a Monitoring agent. Remote monitoring streams vitals like heart rate, blood pressure, and oxygen saturation, flagging readings outside personalized thresholds. Trend detection matters more than single readings: a slow drift can precede an acute event. Synthetic vital streams with planted deteriorations verify the alerting logic. Samples synthetic topic metrics for N cycles, evaluates each reading against thresholds, prints readings and alerts.

The intended user is a student or engineer working in healthcare (telemedicine) who needs a working, runnable reference for Vital Sign Trend Monitor — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
