# Presentation Guide — VCF-Style Parser: File Organizer

## 60-Second Pitch

I built a VCF-Style Parser that tidies a messy folder into categorized subfolders, showing you the plan before it moves anything. Variant call format records variants with fixed columns for chromosome, position, reference and alternate alleles, quality, and filter status, plus a flexible INFO field and per-sample genotype columns.

VCF-Style Parser in two sentences: Variant call format records variants with fixed columns for chromosome, position, reference and alternate alleles, quality, and filter status, plus a flexible INFO field and per-sample genotype columns. Parsing must handle multi-allelic sites and missing data gracefully. Synthetic records with valid structure exercise the parser thoroughly.

## Architecture Talking Points

- Components: `FileOrganizer` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Extension-to-folder mapping with a plan-then-execute move pass; runs in O(f) over f files.
- Honest scaling limit: Single-machine, single-threaded moves; fine for thousands of files, not a distributed file pipeline.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a VCF-Style Parser in Python that sorts files into extension-mapped folders with a plan-then-execute pass and dry-run mode.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How does it decide which folder a file goes to?

**A:** The extension map comes from {'variant_count': 'number of variant records', 'sample_count': 'number of samples per record', 'seed': 'random seed for record generation', 'version': 'format version to emulate'}; any extension not listed is routed to a 'misc' folder.

**Q:** What is the point of plan() versus execute()?

**A:** plan() computes every move first, so --dry-run can show the full plan and execute() just carries it out.

**Q:** Is the demo safe to rerun?

**A:** Yes: the demo wipes and recreates ./demo_workspace at startup, so reruns are clean and deterministic.
