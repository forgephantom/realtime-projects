# Architecture (HLD) — Model Extraction Probe Simulator: Rate Limiter

## Problem & Users

Model Extraction Probe Simulator built as a rate limiter. Model extraction attacks query a black-box API to clone its behavior: with enough input-output pairs, an attacker trains a copycat model. Defenses include query rate limits, output watermarking, and monitoring for extraction-like query patterns. The simulator runs seeded query strategies against a mock API and measures copycat fidelity. A token-bucket rate limiter that refills continuously over time and reports allow/deny decisions for a scripted request schedule.

The intended user is a student or engineer working in ai (ai_safety_redteaming) who needs a working, runnable reference for Model Extraction Probe Simulator — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| FakeClock | main | Deterministic clock for the demo: time moves only when advance() is called. |
| TokenBucket | main | Token-bucket rate limiter with continuous refill and an injectable clock. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
seeded arrival schedule -> FakeClock.advance -> TokenBucket._refill
TokenBucket.allow -> ALLOW (token consumed) or DENY (bucket empty)
allowed/denied counters -> stats() -> printed table + admission rate
```

## Storage

In-memory only: token balance and counters reset when the process exits.

## Scaling & Limits

Single-process bucket; a distributed service would need a shared store like Redis so all instances draw from one bucket.

## Trade-offs

Continuous refill is smoother than fixed windows but needs a monotonic clock; float token math is approximate by design.

## Failure Handling

Invalid rate or capacity raises ValueError at construction; the demo never sleeps, so it cannot stall on timing.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
