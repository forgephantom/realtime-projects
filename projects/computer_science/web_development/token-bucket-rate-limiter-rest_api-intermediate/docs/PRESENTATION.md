# Presentation Guide — Token-Bucket Rate Limit Middleware: Rest Api Service

## 60-Second Pitch

A self-contained Token-Bucket Rate Limit Middleware REST API in pure Python that starts on localhost, proves every endpoint works with a live self-test, and shuts itself down. Rate limiting protects APIs from abuse: a token bucket refills at a fixed rate up to a capacity, and each request spends a token, so bursts are allowed but sustained rates are capped.

Token-Bucket Rate Limit Middleware in two sentences: Rate limiting protects APIs from abuse: a token bucket refills at a fixed rate up to a capacity, and each request spends a token, so bursts are allowed but sustained rates are capped. The middleware keys buckets per API key or IP, returns 429 with Retry-After when empty, and exposes limit headers. Distributed deployments share bucket state so limits hold across instances.

## Architecture Talking Points

- Components: `Store`, `ApiHandler` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: In-memory CRUD over HTTP with JSON bodies; runs in O(n) per list/stats request, O(1) per create.
- Honest scaling limit: ThreadingHTTPServer handles modest concurrency, but the shared list is not lock-protected and everything is single-process, so this suits local demos, not production traffic.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Token-Bucket Rate Limit Middleware REST API in Python (stdlib http.server) with JSON endpoints, an in-memory store, and a threaded self-test that exercises every route via urllib; demo binds 127.0.0.1, verifies all endpoints, and exits cleanly.
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
