# Presentation Guide — HATEOAS Link Builder: Api Client Sim

## 60-Second Pitch

I built a HATEOAS Link Builder that pages through results and automatically retries failed requests, and I proved it against a simulated flaky server. HATEOAS makes APIs self-describing by embedding links to related actions in each response, so clients discover workflows instead of hardcoding URLs.

HATEOAS Link Builder in two sentences: HATEOAS makes APIs self-describing by embedding links to related actions in each response, so clients discover workflows instead of hardcoding URLs. The builder attaches templated links (self, next, cancel, pay) with the HTTP method each expects, driven by the resource's current state. A state machine decides which transitions are legal, so the links always reflect what the client may do next.

## Architecture Talking Points

- Components: `APIError`, `FakeAPI`, `APIClient` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Paginated fetching with retry-on-500 and linear backoff; runs in O(pages) requests to list all items.
- Honest scaling limit: In-process fake: no real HTTP, connection pooling, or TLS; the client logic is what is being demonstrated.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a HATEOAS Link Builder in Python with paginated fetching, retry-on-500 with backoff, and a full request history for debugging.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How are server errors simulated?

**A:** The first fail_first handle() calls return 500 regardless of path, so the client must retry before any data flows.

**Q:** Which failures get retried?

**A:** Only 500s are retried, with a 0.01s * attempt linear backoff; 404s raise APIError immediately.

**Q:** How does pagination know when to stop?

**A:** list_all keeps requesting page N+1 until the accumulated items reach the total reported by the API.
