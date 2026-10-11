# Architecture (HLD) — JSON:API Relationship Expander: Api Client Sim

## Problem & Users

JSON:API Relationship Expander built as a API client sim. JSON:API standardizes compound documents: primary data plus an included section with related resources, sparse fieldsets limiting attributes, and links for pagination. The expander resolves relationship paths, dedupes included resources by type+id, and applies fieldset filtering. It eliminates both over-fetching and N+1 client round trips. A simulated REST API client that paginates through an in-process fake API, retrying simulated server errors with backoff.

The intended user is a student or engineer working in computer_science (web_development) who needs a working, runnable reference for JSON:API Relationship Expander — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
