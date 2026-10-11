# Architecture (HLD) — Canary Deployment Orchestrator: Monitoring Agent

## Problem & Users

Canary Deployment Orchestrator built as a Monitoring agent. Canary deployment shifts a slice of traffic to the new model and watches guardrail metrics before proceeding: error rate, latency, and key business metrics must stay within bounds. Automated analysis promotes or rolls back based on statistical comparison with the stable version. The orchestrator steps traffic percentages on seeded metric streams. Samples synthetic topic metrics for N cycles, evaluates each reading against thresholds, prints readings and alerts.

The intended user is a student or engineer working in ai (mlops) who needs a working, runnable reference for Canary Deployment Orchestrator — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
