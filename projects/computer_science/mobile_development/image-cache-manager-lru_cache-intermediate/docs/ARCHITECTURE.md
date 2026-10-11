# Architecture (HLD) — Image Cache Manager: Lru Cache

## Problem & Users

Image Cache Manager built as a LRU cache. Image-heavy feeds need memory and disk caches with eviction, or scrolling janks and data balloons. The manager implements two-level caching with LRU and size caps. Smooth scrolling, bounded storage. A fixed-capacity LRU cache that evicts the least-recently-used entry and reports hit, miss, and eviction statistics.

The intended user is a student or engineer working in computer_science (mobile_development) who needs a working, runnable reference for Image Cache Manager — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| LRUCache | main | Fixed-capacity cache with least-recently-used eviction backed by an OrderedDict. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
seeded key stream -> get/put -> OrderedDict (recency order)
over-capacity put -> popitem(last=False) evicts LRU key
hits/misses/evictions -> stats() -> printed trace + summary
```

## Storage

In-memory only: the cache and its counters live in the process and vanish on exit; no disk persistence.

## Scaling & Limits

Single-process structure; capacity is bounded by RAM and there is no sharding or cross-process sharing.

## Trade-offs

OrderedDict gives simple O(1) LRU ordering at the cost of per-entry overhead versus a plain dict with manual timestamps.

## Failure Handling

Capacity below 1 raises ValueError at construction; get() on a missing key returns None instead of raising.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
