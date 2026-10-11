# Architecture (HLD) — Reverse Complement Tool: Unit Converter

## Problem & Users

Reverse Complement Tool built as a unit converter. DNA is double-stranded, so a read may match either strand; the reverse complement applies Watson-Crick pairing then reverses the string. Ambiguity codes like N expand the pairing rules. Verifying the tool on seeded sequences with known complements catches off-by-one and pairing errors. A unit converter covering length, mass, volume, speed, data sizes, and temperature, with real conversion factors and offset-aware temperature math.

The intended user is a student or engineer working in healthcare (genomics) who needs a working, runnable reference for Reverse Complement Tool — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
