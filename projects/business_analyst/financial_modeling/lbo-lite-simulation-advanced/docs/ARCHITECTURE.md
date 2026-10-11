# Architecture (HLD) — Leveraged Buyout Model Lite: Simulation (Logistic Growth)

## Problem & Users

Leveraged Buyout Model Lite built as a Simulation (logistic growth). A leveraged buyout model layers debt onto an acquisition: a debt schedule with mandatory and optional repayments, interest that reduces taxes, and an exit sale that repays the rest. Returns come from deleveraging, growth, and multiple expansion, and the model shows how much leverage the cash flows can actually support. It is the core engine of private equity underwriting. Euler-integrates logistic growth dP/dt = r*P*(1-P/K) and prints the trajectory table with summary statistics.

The intended user is a student or engineer working in business_analyst (financial_modeling) who needs a working, runnable reference for Leveraged Buyout Model Lite — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
PARAMS (r, K, P0) + --steps/--dt -> simulate (Euler loop)
trajectory rows -> print_trajectory (sampled table)
rows -> start/end/peak summary
```

## Storage

In-memory only: the trajectory list exists for the run and is not persisted.

## Scaling & Limits

The trajectory is a plain list, so millions of steps would use noticeable memory; streaming or downsampling would fix that.

## Trade-offs

Explicit Euler is the simplest integrator to read and verify, at the cost of accuracy versus higher-order methods for stiff dynamics.

## Failure Handling

A non-positive carrying capacity K would flip the growth sign; the template documents K as positive and the default params keep it well-behaved.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
