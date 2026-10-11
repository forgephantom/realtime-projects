# Presentation Guide — Traceroute Simulator: Port Scanner

## 60-Second Pitch

I built a Traceroute Simulator that checks which local ports are listening and proves itself with a self-test against a dummy listener. Traceroute maps the path by sending probes with increasing TTLs: each hop's router returns time-exceeded, revealing the route hop by hop with per-hop RTT.

Traceroute Simulator in two sentences: Traceroute maps the path by sending probes with increasing TTLs: each hop's router returns time-exceeded, revealing the route hop by hop with per-hop RTT. The simulator models a topology and produces traceroute output including asterisks for silent hops. It is path discovery from first principles.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Parallel TCP connect scan over a loopback target; runs in O(p) connects over p ports, parallelized across worker threads.
- Honest scaling limit: Connect scanning is the slowest scan type; fine for tens of ports locally, not designed for internet-wide sweeping.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Traceroute Simulator in Python using parallel TCP connects, restricted to loopback targets with a self-test that validates scan accuracy.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** What stops it from scanning other machines?

**A:** check_target() only allows 127.0.0.1, localhost, and ::1; anything else prints an error and exits with status 2.

**Q:** How does the self-test guarantee an open port?

**A:** A throwaway listener is opened on an ephemeral port, the range around it is scanned, and the test passes only if exactly that port is open.

**Q:** Why scan in parallel?

**A:** A thread pool runs up to --workers concurrent connects, so a 100-port scan finishes in roughly one timeout instead of 100.
