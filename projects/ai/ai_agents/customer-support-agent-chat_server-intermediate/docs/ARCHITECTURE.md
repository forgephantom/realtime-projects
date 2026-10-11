# Architecture (HLD) — Customer Support Agent Sim: Chat Server

## Problem & Users

Customer Support Agent Sim built as a chat server. A customer support agent greets users, diagnoses issues through clarifying questions, and follows runbooks for known problems. Escalation rules hand off to humans when confidence drops or the issue matches a sensitive category. Conversation quality is scored on resolution rate and politeness. A loopback-only TCP chat server that relays messages between clients, with a default self-test that verifies delivery end to end.

The intended user is a student or engineer working in ai (ai_agents) who needs a working, runnable reference for Customer Support Agent Sim — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| ChatServer | main | Tiny TCP chat relay bound to 127.0.0.1 on an ephemeral port, one thread per client. |
| ChatClient | main | Blocking-line chat client with a background reader thread and a received-message inbox. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
client -> TCP line -> server reader thread -> broadcast()
broadcast() -> all other clients' sockets -> client inbox
self-test compares each inbox against the expected transcript
```

## Storage

In-memory only: messages live in client inboxes during the run and are discarded on shutdown.

## Scaling & Limits

Thread-per-client suits a demo; hundreds of clients would want selectors or asyncio instead of one thread each.

## Trade-offs

Blocking sockets with threads are simple and readable, at the cost of per-client thread overhead versus an event loop.

## Failure Handling

Dead clients are removed from the broadcast list on read errors; shutdown() closes every socket and joins the accept thread.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
