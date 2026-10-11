# Design (LLD) — MCP JSON-RPC Client: Mcp_Server_Sim

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| MCPServer | JSON-RPC 2.0 server sim: tool registry, JSON-RPC dispatch, resources, and error envelopes. |

## Functions

| Function | Signature | Description |
|---|---|---|
| MCPServer.list_tools | list_tools(self) -> list | Tool catalog with descriptions and input schemas. |
| MCPServer.call_tool | call_tool(self, name: str, arguments: dict) -> dict | Invoke a registered tool; returns content plus isError flag. |
| MCPServer.handle_request | handle_request(self, request: dict) -> dict | Handle one JSON-RPC 2.0 request dict; returns the response dict. |
| build_requests | build_requests(seed: int) -> list | Seeded request list covering all methods plus error paths. |
| run_demo | run_demo(seed: int) -> int | Seeded demo: print each request and its JSON-RPC response. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Entry point: seeded MCP server demo. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for MCP JSON-RPC Client:

| Parameter | Meaning |
|---|---|
| batch_size | requests per batch |
| error_rate | injected error probability |
| num_requests | requests simulated |

## Algorithm & Complexity

The core of this project is JSON-RPC 2.0 dispatch over a request dict list: method lookup, tool call with validated args, result/error envelopes..

- **Time complexity:** O(1) per request: method dispatch plus one tool call.
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/ai/mcp_integrations/mcp-jsonrpc-client-mcp_server_sim-beginner
python3 src/main.py --help
python3 src/main.py
```
No extra flags beyond --seed; the request list is rebuilt from the seed each run.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
