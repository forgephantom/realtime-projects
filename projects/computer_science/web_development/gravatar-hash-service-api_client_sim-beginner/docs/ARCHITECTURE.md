# Architecture (HLD) — Gravatar Hash Service: Api Client Sim

## Problem & Users

Gravatar Hash Service built as a API client sim. Gravatar maps emails to avatars via MD5: the service normalizes (trim, lowercase), hashes, and builds avatar URLs with size and default-image parameters. It handles the 404-vs-default fallback choice and caches lookups. The privacy trade-off is that email hashes are enumerable, which is why many sites moved to initials. A simulated REST API client that paginates through an in-process fake API, retrying simulated server errors with backoff.

The intended user is a student or engineer working in computer_science (web_development) who needs a working, runnable reference for Gravatar Hash Service — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| APIError | main | Raised when a simulated request fails after all retries. |
| FakeAPI | main | In-process fake HTTP-like API: no sockets, no network; serves paginated items. |
| APIClient | main | Tiny REST-style client with retries, pagination helpers, and a request history. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
APIClient.list_all -> request per page -> FakeAPI.handle
simulated 500 -> sleep backoff -> retry (up to max_retries)
200 responses -> combined item list + full request history printed
```

## Storage

In-memory only: the fake dataset and request history vanish when the process exits.

## Scaling & Limits

In-process fake: no real HTTP, connection pooling, or TLS; the client logic is what is being demonstrated.

## Trade-offs

A fake in-process API keeps the demo hermetic and fast, at the cost of not exercising real network behavior.

## Failure Handling

Simulated 500s are retried up to max_retries, then APIError is raised with status and body; 404s fail fast with no retry.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
