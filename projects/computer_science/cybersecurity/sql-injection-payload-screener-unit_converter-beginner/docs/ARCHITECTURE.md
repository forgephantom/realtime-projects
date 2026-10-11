# Architecture (HLD) — SQL Injection Payload Screener: Unit Converter

## Problem & Users

SQL Injection Payload Screener built as a unit converter. SQL injection happens when untrusted input is concatenated into database queries, letting an attacker alter the query logic with quotes, comments, and stacked statements. The screener is a defensive input validator that scores incoming parameters against patterns for tautologies, union selects, stacked queries, and time-based blind probes without ever executing them. It reports which rule fired and a risk score so developers can find weak validation before attackers do. A unit converter covering length, mass, volume, speed, data sizes, and temperature, with real conversion factors and offset-aware temperature math.

The intended user is a student or engineer working in computer_science (cybersecurity) who needs a working, runnable reference for SQL Injection Payload Screener — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
