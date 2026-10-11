# Presentation Guide — Mediator (Chatroom): Chat Server

## 60-Second Pitch

I built a Mediator (Chatroom) that relays messages between local clients in real time, with a self-test proving every message arrives. A mediator centralizes communication: chatroom members send messages to the mediator, which routes to recipients, instead of everyone referencing everyone.

Mediator (Chatroom) in two sentences: A mediator centralizes communication: chatroom members send messages to the mediator, which routes to recipients, instead of everyone referencing everyone. It turns N-to-N wiring into N-to-1. Private messages, moderation, and presence all live in the mediator.

## Architecture Talking Points

- Components: `ChatServer`, `ChatClient` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Thread-per-client TCP relay with line-based broadcast; runs in O(n) broadcast per message over n clients.
- Honest scaling limit: Thread-per-client suits a demo; hundreds of clients would want selectors or asyncio instead of one thread each.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Mediator (Chatroom) in Python with sockets and threads, including a scripted two-client self-test that verifies message relay.
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
