# MCP Stdio Transport Simulator: Mcp_Server_Sim

**Domain:** ai | **Subdomain:** mcp_integrations | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

MCP Stdio Transport Simulator built as a mcp_server_sim. The stdio transport runs the server as a child process and speaks JSON-RPC over its standard input and output: simple, local, and the default for desktop integrations. Message framing uses newline-delimited JSON, and stderr carries logs separately. The simulator spawns a seeded mock server process and exchanges messages. An MCP server simulator that exposes echo, add, and word_count tools plus server info through JSON-RPC 2.0 request handling.

**Core concept — MCP Stdio Transport Simulator:** The stdio transport runs the server as a child process and speaks JSON-RPC over its standard input and output: simple, local, and the default for desktop integrations. Message framing uses newline-delimited JSON, and stderr carries logs separately. The simulator spawns a seeded mock server process and exchanges messages.

**Why this matters in the real world:** Desktop assistants launch local tool servers as child processes over stdio.

---

## Features

- **MCPServer**: JSON-RPC 2.0 server sim: tool registry, JSON-RPC dispatch, resources, and error envelopes.
- `MCPServer.list_tools` (`list_tools(self) -> list`): Tool catalog with descriptions and input schemas.
- `MCPServer.call_tool` (`call_tool(self, name: str, arguments: dict) -> dict`): Invoke a registered tool; returns content plus isError flag.
- `MCPServer.handle_request` (`handle_request(self, request: dict) -> dict`): Handle one JSON-RPC 2.0 request dict; returns the response dict.
- `build_requests` (`build_requests(seed: int) -> list`): Seeded request list covering all methods plus error paths.
- `run_demo` (`run_demo(seed: int) -> int`): Seeded demo: print each request and its JSON-RPC response.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Entry point: seeded MCP server demo.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random, json

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around JSON-RPC 2.0 dispatch over a request dict list: method lookup, tool call with validated args, result/error envelopes.. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(1) per request: method dispatch plus one tool call.. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/ai/mcp_integrations/mcp-stdio-transport-mcp_server_sim-intermediate
python3 src/main.py --help
python3 src/main.py
```
No extra flags beyond --seed; the request list is rebuilt from the seed each run.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints each JSON-RPC request and its response (results for valid calls, error envelopes for bad methods/tools).

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
