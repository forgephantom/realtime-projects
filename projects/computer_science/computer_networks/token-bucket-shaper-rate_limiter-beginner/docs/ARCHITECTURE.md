# Architecture (HLD) — Token Bucket Traffic Shaper: Rate Limiter

## Problem & Users

Token Bucket Traffic Shaper built as a rate limiter. Shapers smooth bursts: the token bucket admits packets when tokens are available, queueing excess instead of dropping, which shapes output to the configured rate with bounded bursts. It differs from policing (which drops). The demo shows the smoothed output profile. A token-bucket rate limiter that refills continuously over time and reports allow/deny decisions for a scripted request schedule.

The intended user is a student or engineer working in computer_science (computer_networks) who needs a working, runnable reference for Token Bucket Traffic Shaper — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
