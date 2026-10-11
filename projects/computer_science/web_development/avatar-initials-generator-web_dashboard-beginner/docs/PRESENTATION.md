# Presentation Guide — Avatar Initials Generator (SVG): Web Dashboard

## 60-Second Pitch

A zero-dependency Avatar Initials Generator (SVG) dashboard that renders live metrics as HTML and JSON, verified end to end by its own self-test. Default avatars from initials are everywhere: the generator picks a deterministic background color from the name hash, renders 1-2 initials in SVG with proper contrast, and sizes for retina displays.

Avatar Initials Generator (SVG) in two sentences: Default avatars from initials are everywhere: the generator picks a deterministic background color from the name hash, renders 1-2 initials in SVG with proper contrast, and sizes for retina displays. Deterministic colors mean the same user always gets the same avatar. It is a tiny service with outsized visual impact.

## Architecture Talking Points

- Components: `DashboardHandler` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Server-side HTML rendering of a metrics table; runs in O(n) to render n metric rows.
- Honest scaling limit: Single-process threaded server rendering small pages; fine for local demos, not for high-traffic or large metric sets.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Avatar Initials Generator (SVG) web dashboard in Python (stdlib http.server) rendering a server-side HTML metrics table with a JSON API; default run self-tests both endpoints on 127.0.0.1 and prints verification results.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** Does the page need JavaScript?

**A:** No; the table is rendered server-side as plain HTML, with a meta refresh tag for periodic updates.

**Q:** Where do the metrics come from?

**A:** A seeded RNG generates deterministic synthetic rows, so the dashboard is reproducible without any external data source.

**Q:** Can it serve persistently?

**A:** Yes, pass --serve to keep the ThreadingHTTPServer running on 127.0.0.1 until interrupted.
