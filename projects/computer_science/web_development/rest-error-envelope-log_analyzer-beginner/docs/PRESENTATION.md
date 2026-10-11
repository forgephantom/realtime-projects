# Presentation Guide — REST Error Envelope (RFC 7807): Log Analyzer

## 60-Second Pitch

A REST Error Envelope (RFC 7807) log analyzer in pure Python that synthesizes a service log in memory, parses it with a regex, and reports where the errors really are. Inconsistent error shapes force every client to guess; RFC 7807 fixes this with problem+json: a type URI identifying the problem, a human title, the status, a detail message, and the instance that failed.

REST Error Envelope (RFC 7807) in two sentences: Inconsistent error shapes force every client to guess; RFC 7807 fixes this with problem+json: a type URI identifying the problem, a human title, the status, a detail message, and the instance that failed. Validation errors extend it with per-field breakdowns. A uniform envelope lets clients, SDKs, and monitoring all parse failures the same way.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Regex parsing with Counter aggregation; runs in O(n) to generate, parse, and aggregate n lines.
- Honest scaling limit: Lines are held in memory, so multi-gigabyte logs would need a streaming line-by-line variant of the same pipeline.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a REST Error Envelope (RFC 7807) log analyzer in Python (stdlib re) generating a synthetic service log in memory, parsing it with a named-group regex, and reporting level and service counts with top error messages.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** What does the parser extract?

**A:** The regex names timestamp, level, service, and message groups; anything not matching is skipped.

**Q:** Does it read a real log file?

**A:** No; generate_log builds the whole log in memory, so the demo needs no input files.

**Q:** Could it analyze real logs?

**A:** Yes; adapt generate_log to read lines from a file and the parse/analyze/report stages work unchanged.
