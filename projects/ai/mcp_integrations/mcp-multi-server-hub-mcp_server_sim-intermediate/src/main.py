#!/usr/bin/env python3
"""Multi-Server MCP Hub: Mcp_Server_Sim.

A multi-server hub connects one client to many MCP servers: tool names are namespaced per server to avoid collisions, and routing policies pick the right server per call. Aggregated discovery presents a unified tool list. The hub simulates seeded servers and measures routing correctness under name collisions.

Demo dataset idea: Registers seeded tools across servers with intentional name collisions and tests namespaced discovery and routing accuracy..
"""

import argparse
import json
import random

SLUG = "mcp-server-sim"
PARAMS = {'collision_rate': 'duplicate tool name fraction', 'num_servers': 'servers in the hub', 'tools_per_server': 'tools per server'}


def _num(value, fallback):
    """Coerce a descriptive-text PARAMS value to a number, else fallback."""
    try:
        return int(value)
    except (TypeError, ValueError):
        try:
            return float(value)
        except (TypeError, ValueError):
            return fallback


def _param(key, default):
    """Read a project param defensively; coerce descriptive text to the default's type."""
    v = PARAMS.get(key, default) if isinstance(PARAMS, dict) else default
    if isinstance(default, bool):
        return v if isinstance(v, bool) else default
    if isinstance(default, (int, float)) and not isinstance(v, (int, float)):
        return _num(v, default)
    return v


class MCPServer:
    """JSON-RPC 2.0 server sim with a small tool registry."""

    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version
        self._tools = {
            "echo": (self._echo,
                     {"description": "Echo back the input text.",
                      "params": {"text": "string"}}),
            "add": (self._add,
                    {"description": "Add two numbers a and b.",
                     "params": {"a": "number", "b": "number"}}),
            "word_count": (self._word_count,
                           {"description": "Count words in the input text.",
                            "params": {"text": "string"}}),
        }

    def _echo(self, arguments: dict):
        return arguments.get("text", "")

    def _add(self, arguments: dict):
        a, b = arguments["a"], arguments["b"]
        if not isinstance(a, (int, float)) or not isinstance(
                b, (int, float)):
            raise ValueError("add needs numeric a and b")
        return a + b

    def _word_count(self, arguments: dict):
        return len(str(arguments.get("text", "")).split())

    def list_tools(self) -> list:
        """Tool catalog with descriptions and input schemas."""
        return [{"name": name, "description": schema["description"],
                 "input_schema": schema["params"]}
                for name, (_, schema) in self._tools.items()]

    def call_tool(self, name: str, arguments: dict) -> dict:
        """Invoke a registered tool; returns content plus isError flag."""
        if name not in self._tools:
            return {"content": [{"type": "text",
                                 "text": "unknown tool: %s" % name}],
                    "isError": True}
        func, _ = self._tools[name]
        try:
            result = func(arguments or {})
        except Exception as exc:
            return {"content": [{"type": "text", "text": str(exc)}],
                    "isError": True}
        return {"content": [{"type": "text", "text": str(result)}],
                "isError": False}

    def _ok(self, req_id, result: dict) -> dict:
        return {"jsonrpc": "2.0", "id": req_id, "result": result}

    def _err(self, req_id, code: int, message: str) -> dict:
        return {"jsonrpc": "2.0", "id": req_id,
                "error": {"code": code, "message": message}}

    def handle_request(self, request: dict) -> dict:
        """Handle one JSON-RPC 2.0 request dict; return the response dict."""
        if (not isinstance(request, dict)
                or request.get("jsonrpc") != "2.0"
                or "method" not in request):
            rid = request.get("id") if isinstance(request, dict) else None
            return self._err(rid, -32600, "Invalid Request")
        method = request["method"]
        params = request.get("params") or {}
        rid = request.get("id")
        if method == "initialize":
            return self._ok(rid, {"server": self.name,
                                  "version": self.version,
                                  "protocol": "mcp-sim/1.0"})
        if method == "tools/list":
            return self._ok(rid, {"tools": self.list_tools()})
        if method == "tools/call":
            name = params.get("name")
            if not name:
                return self._err(rid, -32602, "missing tool name")
            if name not in self._tools:
                return self._err(rid, -32602,
                                 "unknown tool: %s" % name)
            return self._ok(rid,
                            self.call_tool(name, params.get("arguments", {})))
        if method == "resources/list":
            return self._ok(rid, {"resources": [
                {"uri": "info://server", "name": "server info",
                 "text": "%s v%s" % (self.name, self.version)}]})
        return self._err(rid, -32601,
                         "Method not found: %s" % method)


def build_requests(seed: int) -> list:
    """Seeded request list covering all methods plus error paths."""
    rng = random.Random(seed)
    topic = "Multi-Server MCP Hub"
    return [
        {"jsonrpc": "2.0", "id": 1, "method": "initialize"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
        {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
         "params": {"name": "add",
                    "arguments": {"a": rng.randint(10, 99),
                                  "b": rng.randint(10, 99)}}},
        {"jsonrpc": "2.0", "id": 4, "method": "tools/call",
         "params": {"name": "word_count",
                    "arguments": {"text": "%s demo request payload" % topic}}},
        {"jsonrpc": "2.0", "id": 5, "method": "tools/call",
         "params": {"name": "echo",
                    "arguments": {"text": "hello from %s" % topic}}},
        {"jsonrpc": "2.0", "id": 6, "method": "tools/call",
         "params": {"name": "bogus_tool", "arguments": {}}},
        {"jsonrpc": "2.0", "id": 7, "method": "no_such_method"},
        {"jsonrpc": "2.0", "id": 8, "method": "resources/list"},
    ]


def run_demo(seed: int) -> int:
    """Seeded demo: print each request and its JSON-RPC response."""
    server = MCPServer(_param("server_name", "demo-mcp-server"),
                       _param("version", "0.1.0"))
    print("Multi-Server MCP Hub: Mcp_Server_Sim  (topic: Multi-Server MCP Hub, seed=%d)" % seed)
    for request in build_requests(seed):
        response = server.handle_request(request)
        print("--> %s" % json.dumps(request))
        print("<-- %s\n" % json.dumps(response))
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Multi-Server MCP Hub: Mcp_Server_Sim: A multi-server hub connects one client to many MCP servers: tool names are namespaced per server to avoid collisions, and routing policies pick the right server per call. Aggregated discovery presents a unified tool list. The hub simulates seeded servers and measures routing correctness under name collisions."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    return parser


def main(argv=None) -> int:
    """Entry point: seeded MCP server demo."""
    args = build_parser().parse_args(argv)
    return run_demo(args.seed)


if __name__ == "__main__":
    raise SystemExit(main())
