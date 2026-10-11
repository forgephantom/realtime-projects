# Presentation Guide — gRPC Framing Demo (HTTP/2): Monitoring Agent

## 60-Second Pitch

A gRPC Framing Demo (HTTP/2) monitoring agent in pure Python that samples synthetic metrics on a cadence, checks them against thresholds, and reports every breach. gRPC frames messages in HTTP/2 DATA frames with a 5-byte prefix (compression flag + length): the demo encodes/decodes message streams, handles trailers for status, and multiplexes concurrent calls.

gRPC Framing Demo (HTTP/2) in two sentences: gRPC frames messages in HTTP/2 DATA frames with a 5-byte prefix (compression flag + length): the demo encodes/decodes message streams, handles trailers for status, and multiplexes concurrent calls. It shows the wire format behind microservice RPC.

## Architecture Talking Points

- Components: `Monitor` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Periodic sampling with static threshold evaluation; runs in O(cycles) total; O(1) per sample.
- Honest scaling limit: Single-process in-memory sampling; real fleet monitoring would need persistence, alerting integrations, and horizontal collectors.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a gRPC Framing Demo (HTTP/2) monitoring agent in Python (stdlib) sampling synthetic CPU, memory, and latency metrics on a fixed cadence; evaluates threshold breaches and prints readings with alerts and a summary.
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
