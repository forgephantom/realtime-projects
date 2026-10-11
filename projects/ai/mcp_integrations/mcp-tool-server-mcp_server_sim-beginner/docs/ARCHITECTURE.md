# Architecture (HLD) — MCP Tool Server: Mcp_Server_Sim

## Problem & Users

MCP Tool Server built as a mcp_server_sim. An MCP tool server exposes functions that AI clients can call: each tool declares a name, description, and JSON input schema, and the server validates arguments before executing the handler. Tool discovery happens through a list call, and results return as content blocks. The simulator implements a tool registry with schema validation on seeded tool definitions. An MCP server simulator that exposes echo, add, and word_count tools plus server info through JSON-RPC 2.0 request handling.

The intended user is a student or engineer working in ai (mcp_integrations) who needs a working, runnable reference for MCP Tool Server — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
