# Presentation Guide — Login Attempt Throttler: Monitoring Agent

## 60-Second Pitch

A Login Attempt Throttler monitoring agent in pure Python that samples synthetic metrics on a cadence, checks them against thresholds, and reports every breach. Brute-force login attacks try thousands of password guesses, so throttling slows them down: failed attempts per account and per IP accumulate, triggering growing delays, CAPTCHAs, or temporary lockouts.

Login Attempt Throttler in two sentences: Brute-force login attacks try thousands of password guesses, so throttling slows them down: failed attempts per account and per IP accumulate, triggering growing delays, CAPTCHAs, or temporary lockouts. The design must not let attackers lock out legitimate users or enumerate which accounts exist. Exponential backoff per source balances security with usability.

## Architecture Talking Points

- Components: `Monitor` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Periodic sampling with static threshold evaluation; runs in O(cycles) total; O(1) per sample.
- Honest scaling limit: Single-process in-memory sampling; real fleet monitoring would need persistence, alerting integrations, and horizontal collectors.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Login Attempt Throttler monitoring agent in Python (stdlib) sampling synthetic CPU, memory, and latency metrics on a fixed cadence; evaluates threshold breaches and prints readings with alerts and a summary.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** Where do thresholds come from?

**A:** From PARAMS thresholds, overridable per template instance; defaults are 85% CPU, 90% memory, 500ms latency.

**Q:** Are the readings reproducible?

**A:** The RNG is seeded, so the same seed replays the same readings and alerts for debugging.

**Q:** Could it run persistently?

**A:** Yes, but it would be single-process and in-memory, so it fits demos and prototypes rather than fleet monitoring.
