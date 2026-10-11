# Architecture (HLD) — MCP Sampling Bridge: Mcp_Server_Sim

## Problem & Users

MCP Sampling Bridge built as a mcp_server_sim. Sampling lets a server ask the client to generate text: the server sends a sampling request, the client's model produces a completion, and the server continues its work. This inverts the usual direction so servers can use model intelligence mid-tool. The bridge simulates seeded sampling round trips with context limits. An MCP server simulator that exposes echo, add, and word_count tools plus server info through JSON-RPC 2.0 request handling.

The intended user is a student or engineer working in ai (mcp_integrations) who needs a working, runnable reference for MCP Sampling Bridge — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| MCPServer | main | JSON-RPC 2.0 server sim: tool registry, JSON-RPC dispatch, resources, and error envelopes. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
request list -> MCPServer.handle_request -> method dispatch
tools/call -> call_tool(name, args) -> echo | add | word_count
any method -> {jsonrpc 2.0, id, result|error} response dict
```

## Storage

No persistence: the tool registry is compiled at startup and no request state is kept.

## Scaling & Limits

The in-process dispatch suits demos and tests; a real server would add stdio/HTTP transport and concurrency.

## Trade-offs

Simulating over dicts keeps it dependency-free and testable, but skips real transport framing.

## Failure Handling

Unknown methods and tools return proper JSON-RPC error envelopes (-32601/-32602) instead of raising.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
