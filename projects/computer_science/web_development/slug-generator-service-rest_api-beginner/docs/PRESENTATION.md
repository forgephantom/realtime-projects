# Presentation Guide — Slug Generator Service: Rest Api Service

## 60-Second Pitch

A self-contained Slug Generator Service REST API in pure Python that starts on localhost, proves every endpoint works with a live self-test, and shuts itself down. Slugs turn titles into URL-safe identifiers: the generator lowercases, strips accents, replaces spaces with hyphens, removes unsafe characters, and appends counters for uniqueness.

Slug Generator Service in two sentences: Slugs turn titles into URL-safe identifiers: the generator lowercases, strips accents, replaces spaces with hyphens, removes unsafe characters, and appends counters for uniqueness. It must handle Unicode titles, reserved words, and length caps. Good slugs are readable, stable, and permanent once published.

## Architecture Talking Points

- Components: `Store`, `ApiHandler` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: In-memory CRUD over HTTP with JSON bodies; runs in O(n) per list/stats request, O(1) per create.
- Honest scaling limit: ThreadingHTTPServer handles modest concurrency, but the shared list is not lock-protected and everything is single-process, so this suits local demos, not production traffic.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Slug Generator Service REST API in Python (stdlib http.server) with JSON endpoints, an in-memory store, and a threaded self-test that exercises every route via urllib; demo binds 127.0.0.1, verifies all endpoints, and exits cleanly.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** Why bind only 127.0.0.1?

**A:** The demo and --serve mode are for local development; binding loopback only avoids accidentally exposing the unauthenticated in-memory store on a network.

**Q:** Where does data persist?

**A:** Nowhere; the Store lives in process memory and resets on every run, which keeps the demo deterministic.

**Q:** How is the default run verified?

**A:** run_self_test issues real HTTP requests against the threaded server with urllib and prints a PASSED/FAILED verdict.
