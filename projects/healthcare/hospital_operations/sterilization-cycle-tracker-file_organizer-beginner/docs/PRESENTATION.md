# Presentation Guide — Sterilization Cycle Tracker: File Organizer

## 60-Second Pitch

I built a Sterilization Cycle Tracker that tidies a messy folder into categorized subfolders, showing you the plan before it moves anything. Sterile processing tracks instrument sets through washing, sterilization, and storage, verifying cycle parameters like temperature and exposure time.

Sterilization Cycle Tracker in two sentences: Sterile processing tracks instrument sets through washing, sterilization, and storage, verifying cycle parameters like temperature and exposure time. Biological indicators confirm sterilization efficacy. Synthetic cycle logs with known failures let developers verify the compliance checks.

## Architecture Talking Points

- Components: `FileOrganizer` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Extension-to-folder mapping with a plan-then-execute move pass; runs in O(f) over f files.
- Honest scaling limit: Single-machine, single-threaded moves; fine for thousands of files, not a distributed file pipeline.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Sterilization Cycle Tracker in Python that sorts files into extension-mapped folders with a plan-then-execute pass and dry-run mode.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How does it decide which folder a file goes to?

**A:** The extension map comes from {'set_count': 'instrument sets tracked', 'cycle_count': 'sterilization cycles logged', 'seed': 'random seed for log generation', 'param_limits': 'acceptable cycle parameter ranges'}; any extension not listed is routed to a 'misc' folder.

**Q:** What is the point of plan() versus execute()?

**A:** plan() computes every move first, so --dry-run can show the full plan and execute() just carries it out.

**Q:** Is the demo safe to rerun?

**A:** Yes: the demo wipes and recreates ./demo_workspace at startup, so reruns are clean and deterministic.
