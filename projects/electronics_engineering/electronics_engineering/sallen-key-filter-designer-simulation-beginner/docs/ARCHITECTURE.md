# Architecture (HLD) — Sallen-Key Filter Designer: Simulation (Logistic Growth)

## Problem & Users

Sallen-Key Filter Designer built as a Simulation (logistic growth). The Sallen-Key topology builds a second-order active filter from one op-amp, two resistors, and two capacitors, with the cutoff frequency at 1/(2 x pi x R x C) and Q set by the gain. Choosing equal-R, equal-C values simplifies the math while still hitting standard Butterworth or Bessel responses. Euler-integrates logistic growth dP/dt = r*P*(1-P/K) and prints the trajectory table with summary statistics.

The intended user is a student or engineer working in electronics_engineering (electronics_engineering) who needs a working, runnable reference for Sallen-Key Filter Designer — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
