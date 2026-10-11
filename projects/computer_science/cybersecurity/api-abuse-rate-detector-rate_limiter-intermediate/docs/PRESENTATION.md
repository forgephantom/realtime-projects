# Presentation Guide — API Abuse Rate Detector: Rate Limiter

## 60-Second Pitch

I built a API Abuse Rate Detector that smooths bursty traffic with a token bucket and shows exactly which requests get admitted or denied. Legitimate API clients behave predictably while scrapers and attackers hammer endpoints at inhuman rates or probe for IDOR patterns.

API Abuse Rate Detector in two sentences: Legitimate API clients behave predictably while scrapers and attackers hammer endpoints at inhuman rates or probe for IDOR patterns. The detector profiles per-key request rates, endpoint entropy, and error ratios, flagging keys whose behavior diverges from their historical norm. It separates a viral launch from an attack by looking at error and spread patterns.

## Architecture Talking Points

- Components: `FakeClock`, `TokenBucket` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Token bucket with continuous time-based refill; runs in O(1) per allow() call.
- Honest scaling limit: Single-process bucket; a distributed service would need a shared store like Redis so all instances draw from one bucket.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a API Abuse Rate Detector in Python using the token-bucket algorithm with an injectable clock for deterministic testing.
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
