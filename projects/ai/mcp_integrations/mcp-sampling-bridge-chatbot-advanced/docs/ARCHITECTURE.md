# Architecture (HLD) — MCP Sampling Bridge: Chatbot

## Problem & Users

MCP Sampling Bridge built as a chatbot. Sampling lets a server ask the client to generate text: the server sends a sampling request, the client's model produces a completion, and the server continues its work. This inverts the usual direction so servers can use model intelligence mid-tool. The bridge simulates seeded sampling round trips with context limits. A rule-based chatbot that matches intents by keyword overlap and replies from canned responses, with scripted and interactive chat modes.

The intended user is a student or engineer working in ai (mcp_integrations) who needs a working, runnable reference for MCP Sampling Bridge — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
