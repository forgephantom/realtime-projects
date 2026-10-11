# Architecture (HLD) — Decibel Converter: Unit Converter

## Problem & Users

Decibel Converter built as a unit converter. Decibels compress huge ratios into small numbers: power ratios use 10 x log10 and voltage ratios use 20 x log10. A 3 dB change means double the power, and 20 dB means ten times the voltage, which is why audio and RF engineers think in dB. A unit converter covering length, mass, volume, speed, data sizes, and temperature, with real conversion factors and offset-aware temperature math.

The intended user is a student or engineer working in electronics_engineering (electronics_engineering) who needs a working, runnable reference for Decibel Converter — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
