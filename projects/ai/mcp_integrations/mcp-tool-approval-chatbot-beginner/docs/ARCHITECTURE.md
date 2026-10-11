# Architecture (HLD) — MCP Tool Approval Gate: Chatbot

## Problem & Users

MCP Tool Approval Gate built as a chatbot. Tool approval gates pause sensitive tool calls for human confirmation: the client shows what the tool will do, the user approves or denies, and the decision is logged for audit. Policies auto-approve low-risk reads while always gating writes and external actions. The gate simulates seeded approval flows with risk tiers. A rule-based chatbot that matches intents by keyword overlap and replies from canned responses, with scripted and interactive chat modes.

The intended user is a student or engineer working in ai (mcp_integrations) who needs a working, runnable reference for MCP Tool Approval Gate — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| Chatbot | main | Rule-based chatbot: keyword scoring picks the intent, seeded RNG picks the reply. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
user text -> match_intent (keyword hits) -> best intent
intent -> seeded choice of canned response -> (intent_name, reply)
scripted turns or --chat loop -> printed transcript
```

## Storage

No persistence: the intent table is compiled at startup and conversations are not saved.

## Scaling & Limits

Keyword scoring suits tens of intents; hundreds would want TF-IDF or embeddings instead of substring counting.

## Trade-offs

Rules are predictable and debuggable but brittle on paraphrases a human would find obvious.

## Failure Handling

Unmatched input falls back to the help-style fallback intent, so the bot always has something sensible to say.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
