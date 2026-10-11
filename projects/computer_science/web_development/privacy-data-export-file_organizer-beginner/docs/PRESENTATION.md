# Presentation Guide — Privacy Data Export Tool: File Organizer

## 60-Second Pitch

I built a Privacy Data Export Tool that tidies a messy folder into categorized subfolders, showing you the plan before it moves anything. Data-portability law lets users download their data: the export tool collects a user's records across services, packages them in machine-readable formats, and delivers a secure expiring download.

Privacy Data Export Tool in two sentences: Data-portability law lets users download their data: the export tool collects a user's records across services, packages them in machine-readable formats, and delivers a secure expiring download. It must include everything, exclude others' data, and complete within legal deadlines. Completeness is the compliance risk.

## Architecture Talking Points

- Components: `FileOrganizer` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Extension-to-folder mapping with a plan-then-execute move pass; runs in O(f) over f files.
- Honest scaling limit: Single-machine, single-threaded moves; fine for thousands of files, not a distributed file pipeline.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Privacy Data Export Tool in Python that sorts files into extension-mapped folders with a plan-then-execute pass and dry-run mode.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How does it decide which folder a file goes to?

**A:** The extension map comes from {'scope': 'data categories included', 'format': 'JSON/CSV packaging', 'expiry_hours': 'download link lifetime'}; any extension not listed is routed to a 'misc' folder.

**Q:** What is the point of plan() versus execute()?

**A:** plan() computes every move first, so --dry-run can show the full plan and execute() just carries it out.

**Q:** Is the demo safe to rerun?

**A:** Yes: the demo wipes and recreates ./demo_workspace at startup, so reruns are clean and deterministic.
