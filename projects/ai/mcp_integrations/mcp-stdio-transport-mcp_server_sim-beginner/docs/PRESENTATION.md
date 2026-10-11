# Presentation Guide — MCP Stdio Transport Simulator: Mcp_Server_Sim

## 60-Second Pitch

I built a MCP Stdio Transport Simulator that serves tools over JSON-RPC 2.0 with proper result and error envelopes. The stdio transport runs the server as a child process and speaks JSON-RPC over its standard input and output: simple, local, and the default for desktop integrations.

MCP Stdio Transport Simulator in two sentences: The stdio transport runs the server as a child process and speaks JSON-RPC over its standard input and output: simple, local, and the default for desktop integrations. Message framing uses newline-delimited JSON, and stderr carries logs separately. The simulator spawns a seeded mock server process and exchanges messages.

## Architecture Talking Points

- Components: `MCPServer` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: JSON-RPC 2.0 dispatch over a request dict list: method lookup, tool call with validated args, result/error envelopes.; runs in O(1) per request: method dispatch plus one tool call..
- Honest scaling limit: The in-process dispatch suits demos and tests; a real server would add stdio/HTTP transport and concurrency.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a MCP Stdio Transport Simulator in Python implementing JSON-RPC 2.0 dispatch with a tool registry and structured error handling.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How are requests routed?

**A:** Method names dispatch to handlers: initialize, tools/list, tools/call, and resources/list; anything else is a -32601 error.

**Q:** How do tools plug in?

**A:** A dict maps tool names to (function, schema) pairs; call_tool validates args, runs the function, and wraps the result.

**Q:** What resources are exposed?

**A:** resources/list exposes a server-info resource with the name and version.
