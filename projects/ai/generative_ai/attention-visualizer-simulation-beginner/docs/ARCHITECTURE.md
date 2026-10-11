# Architecture (HLD) — Attention Map Visualizer: Simulation (Logistic Growth)

## Problem & Users

Attention Map Visualizer built as a Simulation (logistic growth). Attention weights show which input tokens each output token looks at: the softmax of query-key dot products. Visualizing the weight matrix as a heatmap reveals patterns like attending to the previous token or to sentence starts. Multi-head attention runs several such views in parallel, each specializing differently. Euler-integrates logistic growth dP/dt = r*P*(1-P/K) and prints the trajectory table with summary statistics.

The intended user is a student or engineer working in ai (generative_ai) who needs a working, runnable reference for Attention Map Visualizer — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
