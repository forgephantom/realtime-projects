# Architecture (HLD) — Canary Deployment Orchestrator: Rest Api Service

## Problem & Users

Canary Deployment Orchestrator built as a REST API service. Canary deployment shifts a slice of traffic to the new model and watches guardrail metrics before proceeding: error rate, latency, and key business metrics must stay within bounds. Automated analysis promotes or rolls back based on statistical comparison with the stable version. The orchestrator steps traffic percentages on seeded metric streams. Serves a small JSON REST API for the topic records, with health, list, create, and stats endpoints.

The intended user is a student or engineer working in ai (mlops) who needs a working, runnable reference for Canary Deployment Orchestrator — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| Store | main | In-memory record collection backing the API. |
| ApiHandler | main | BaseHTTPRequestHandler routing GET/POST to the Store. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
urllib client -> HTTP request -> ApiHandler
ApiHandler -> Store (in-memory list) -> JSON response
Store: list_records / add_record / stats
```

## Storage

In-memory only: records live in a Python list inside the Store and vanish when the process exits. No database or files are used.

## Scaling & Limits

ThreadingHTTPServer handles modest concurrency, but the shared list is not lock-protected and everything is single-process, so this suits local demos, not production traffic.

## Trade-offs

Stdlib-only keeps the template dependency-free, at the cost of hand-rolled routing and no request validation framework.

## Failure Handling

Malformed JSON bodies are treated as empty objects; unknown routes return 404 JSON. The server shuts down cleanly via server.shutdown() after the self-test.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
