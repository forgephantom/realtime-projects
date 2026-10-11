# Presentation Guide — 6in4 Tunnel Broker (Concept): Simulation (Logistic Growth)

## 60-Second Pitch

A 6in4 Tunnel Broker (Concept) simulation in pure Python that integrates logistic growth with Euler steps and prints the full trajectory toward carrying capacity. Transition tunnels carry IPv6 over IPv4: the broker sets up 6in4 encapsulation (protocol 41), assigns /64s to clients, and routes between the tunnel and native IPv6.

6in4 Tunnel Broker (Concept) in two sentences: Transition tunnels carry IPv6 over IPv4: the broker sets up 6in4 encapsulation (protocol 41), assigns /64s to clients, and routes between the tunnel and native IPv6. The demo models encapsulation overhead and MTU effects. It was the practical IPv6 on-ramp for years.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Explicit Euler integration of logistic growth; runs in O(steps).
- Honest scaling limit: The trajectory is a plain list, so millions of steps would use noticeable memory; streaming or downsampling would fix that.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a 6in4 Tunnel Broker (Concept) simulator in Python (stdlib) implementing Euler integration of logistic growth with seeded parameters; demo runs end-to-end and prints the trajectory table with summary statistics.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** What dynamics does the model show?

**A:** Logistic growth: fast early rise that levels off at the carrying capacity K, a common shape for adoption and saturation processes.

**Q:** How is accuracy controlled?

**A:** --steps and --dt; smaller dt is more accurate, larger dt runs faster but can overshoot.

**Q:** Why Euler instead of RK4?

**A:** Euler is first-order and simple to read; the template favors clarity over the accuracy of higher-order integrators.
