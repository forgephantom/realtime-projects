# Architecture (HLD) — MCP Roots Manager: Mcp_Server_Sim

## Problem & Users

MCP Roots Manager built as a mcp_server_sim. Roots define the filesystem or URI boundaries a server may access: clients declare which directories are in scope, and servers must refuse paths outside them. Multiple roots support multi-project workspaces, and root change notifications let servers refresh. The manager enforces seeded root policies on path requests. An MCP server simulator that exposes echo, add, and word_count tools plus server info through JSON-RPC 2.0 request handling.

The intended user is a student or engineer working in ai (mcp_integrations) who needs a working, runnable reference for MCP Roots Manager — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
