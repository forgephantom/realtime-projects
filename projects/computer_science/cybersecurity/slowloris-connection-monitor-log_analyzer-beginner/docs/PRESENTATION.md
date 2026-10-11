# Presentation Guide — Slowloris Connection Monitor: Log Analyzer

## 60-Second Pitch

A Slowloris Connection Monitor log analyzer in pure Python that synthesizes a service log in memory, parses it with a regex, and reports where the errors really are. Slowloris keeps many connections open by sending headers at a trickle, starving the server's connection pool without high bandwidth.

Slowloris Connection Monitor in two sentences: Slowloris keeps many connections open by sending headers at a trickle, starving the server's connection pool without high bandwidth. The monitor tracks connection duration, bytes-per-second, and header completion rates, flagging connections that look deliberately stalled. It distinguishes slow legitimate clients on bad networks from attack patterns.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Regex parsing with Counter aggregation; runs in O(n) to generate, parse, and aggregate n lines.
- Honest scaling limit: Lines are held in memory, so multi-gigabyte logs would need a streaming line-by-line variant of the same pipeline.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Slowloris Connection Monitor log analyzer in Python (stdlib re) generating a synthetic service log in memory, parsing it with a named-group regex, and reporting level and service counts with top error messages.
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
