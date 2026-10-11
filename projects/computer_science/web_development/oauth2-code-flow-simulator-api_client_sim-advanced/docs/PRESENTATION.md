# Presentation Guide — OAuth2 Authorization Code Flow Simulator: Api Client Sim

## 60-Second Pitch

I built a OAuth2 Authorization Code Flow Simulator that pages through results and automatically retries failed requests, and I proved it against a simulated flaky server. OAuth2 lets users grant a third-party app limited access without sharing passwords: the app redirects to the provider, the user approves scopes, and the provider returns an authorization code that the app exchanges for tokens.

OAuth2 Authorization Code Flow Simulator in two sentences: OAuth2 lets users grant a third-party app limited access without sharing passwords: the app redirects to the provider, the user approves scopes, and the provider returns an authorization code that the app exchanges for tokens. PKCE adds a code challenge so mobile apps can do this without a client secret. Simulating all four roles (user, client, auth server, resource server) shows where each secret must live.

## Architecture Talking Points

- Components: `APIError`, `FakeAPI`, `APIClient` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Paginated fetching with retry-on-500 and linear backoff; runs in O(pages) requests to list all items.
- Honest scaling limit: In-process fake: no real HTTP, connection pooling, or TLS; the client logic is what is being demonstrated.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a OAuth2 Authorization Code Flow Simulator in Python with paginated fetching, retry-on-500 with backoff, and a full request history for debugging.
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
