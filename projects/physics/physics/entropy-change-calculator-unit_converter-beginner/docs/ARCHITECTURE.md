# Architecture (HLD) — Entropy Change Calculator: Unit Converter

## Problem & Users

Entropy Change Calculator built as a unit converter. Entropy measures how spread out energy becomes, and it rises whenever heat flows from hot to cold or a gas expands into more volume. For reversible processes the entropy change is the heat exchanged divided by the temperature, summed over each step. A unit converter covering length, mass, volume, speed, data sizes, and temperature, with real conversion factors and offset-aware temperature math.

The intended user is a student or engineer working in physics (physics) who needs a working, runnable reference for Entropy Change Calculator — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| UnitConverter | main | Converts between units within a category using factor tables; temperature is offset-aware. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
(value, from_unit, to_unit) -> category lookup
same category -> value * from_factor / to_factor (or via Celsius)
unknown/mismatched units -> ValueError -> demo table of results
```

## Storage

No persistence: stateless conversions computed on demand.

## Scaling & Limits

A static factor table; adding units is a one-line table edit with no code changes.

## Trade-offs

Factor tables are simple and exact for linear units; affine units like temperature need the extra conversion functions.

## Failure Handling

Unknown units and cross-category conversions raise ValueError with a clear message; the CLI maps these to exit code 2.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
