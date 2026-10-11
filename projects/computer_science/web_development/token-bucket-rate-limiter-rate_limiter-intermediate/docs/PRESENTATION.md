# Presentation Guide — Token-Bucket Rate Limit Middleware: Rate Limiter

## 60-Second Pitch

I built a Token-Bucket Rate Limit Middleware that smooths bursty traffic with a token bucket and shows exactly which requests get admitted or denied. Rate limiting protects APIs from abuse: a token bucket refills at a fixed rate up to a capacity, and each request spends a token, so bursts are allowed but sustained rates are capped.

Token-Bucket Rate Limit Middleware in two sentences: Rate limiting protects APIs from abuse: a token bucket refills at a fixed rate up to a capacity, and each request spends a token, so bursts are allowed but sustained rates are capped. The middleware keys buckets per API key or IP, returns 429 with Retry-After when empty, and exposes limit headers. Distributed deployments share bucket state so limits hold across instances.

## Architecture Talking Points

- Components: `FakeClock`, `TokenBucket` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Token bucket with continuous time-based refill; runs in O(1) per allow() call.
- Honest scaling limit: Single-process bucket; a distributed service would need a shared store like Redis so all instances draw from one bucket.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Token-Bucket Rate Limit Middleware in Python using the token-bucket algorithm with an injectable clock for deterministic testing.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How do tokens refill?

**A:** On every call, tokens increase by elapsed_seconds * rate_per_sec, capped at capacity, so refills are continuous rather than per-tick.

**Q:** Why does the demo use a fake clock?

**A:** A FakeClock makes the arrival schedule fully deterministic, so the allow/deny table is identical on every run.

**Q:** How would this differ from a fixed-window limiter?

**A:** A fixed window can admit 2x the rate at window boundaries; the bucket smooths bursts because tokens accrue gradually.
