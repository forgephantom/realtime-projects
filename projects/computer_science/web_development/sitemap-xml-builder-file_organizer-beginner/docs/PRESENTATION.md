# Presentation Guide — Sitemap XML Builder: File Organizer

## 60-Second Pitch

I built a Sitemap XML Builder that tidies a messy folder into categorized subfolders, showing you the plan before it moves anything. Search engines discover pages through sitemap.xml: the builder lists URLs with lastmod, changefreq, and priority, splits large sites into sitemap index files capped at 50k URLs each, and gzips the output.

Sitemap XML Builder in two sentences: Search engines discover pages through sitemap.xml: the builder lists URLs with lastmod, changefreq, and priority, splits large sites into sitemap index files capped at 50k URLs each, and gzips the output. It should only include canonical, indexable URLs. A clean sitemap shortens the time from publish to indexed.

## Architecture Talking Points

- Components: `FileOrganizer` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Extension-to-folder mapping with a plan-then-execute move pass; runs in O(f) over f files.
- Honest scaling limit: Single-machine, single-threaded moves; fine for thousands of files, not a distributed file pipeline.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Sitemap XML Builder in Python that sorts files into extension-mapped folders with a plan-then-execute pass and dry-run mode.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How does it decide which folder a file goes to?

**A:** The extension map comes from {'url_cap': 'URLs per sitemap file', 'include_policy': 'which pages qualify (canonical, 200, indexable)', 'gzip': 'whether output is compressed'}; any extension not listed is routed to a 'misc' folder.

**Q:** What is the point of plan() versus execute()?

**A:** plan() computes every move first, so --dry-run can show the full plan and execute() just carries it out.

**Q:** Is the demo safe to rerun?

**A:** Yes: the demo wipes and recreates ./demo_workspace at startup, so reruns are clean and deterministic.
