# Presentation Guide — Long-Polling Fallback Transport: Chat Server

## 60-Second Pitch

I built a Long-Polling Fallback Transport that relays messages between local clients in real time, with a self-test proving every message arrives. Where WebSockets are blocked, long polling emulates push: the client holds a request open until the server has data or a timeout fires, then immediately re-issues it.

Long-Polling Fallback Transport in two sentences: Where WebSockets are blocked, long polling emulates push: the client holds a request open until the server has data or a timeout fires, then immediately re-issues it. The server needs per-client queues, timeout management, and message ordering so nothing is lost between polls. It is less efficient than a persistent socket but works through the most restrictive proxies.

## Architecture Talking Points

- Components: `ChatServer`, `ChatClient` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Thread-per-client TCP relay with line-based broadcast; runs in O(n) broadcast per message over n clients.
- Honest scaling limit: Thread-per-client suits a demo; hundreds of clients would want selectors or asyncio instead of one thread each.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Long-Polling Fallback Transport in Python with sockets and threads, including a scripted two-client self-test that verifies message relay.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** Why does the server bind only 127.0.0.1?

**A:** Loopback-only binding keeps the demo safe: no traffic ever leaves the machine and no firewall port is opened.

**Q:** How does the default run verify the relay?

**A:** Two scripted clients exchange messages; the test compares each client's inbox against the exact expected transcript and prints PASS or FAIL.

**Q:** How are messages framed?

**A:** Newline-delimited lines; each side buffers bytes and splits on newlines so partial TCP reads are reassembled correctly.
