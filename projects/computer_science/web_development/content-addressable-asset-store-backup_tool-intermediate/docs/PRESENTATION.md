# Presentation Guide — Content-Addressable Asset Store: Backup Tool

## 60-Second Pitch

I built a Content-Addressable Asset Store that copies your files and proves the copy is exact by verifying SHA-256 checksums. Content addressing names files by their hash: identical content dedupes automatically, and the hash doubles as an integrity check on every read.

Content-Addressable Asset Store in two sentences: Content addressing names files by their hash: identical content dedupes automatically, and the hash doubles as an integrity check on every read. The store shards blobs by hash prefix, serves them with immutable cache headers, and garbage-collects unreferenced blobs. It is how CDNs and caches get infinite cache lifetimes safely.

## Architecture Talking Points

- Components: `BackupJob` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Full copy with SHA-256 manifest, then re-hash verification; runs in O(bytes) to copy and hash every file.
- Honest scaling limit: Single-machine full copies; large trees would want incremental backups and parallel hashing.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Content-Addressable Asset Store in Python that copies a folder tree and verifies integrity with SHA-256 checksums stored in a JSON manifest.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How are checksums recorded?

**A:** After copying, run() hashes each destination file and writes path, size, and SHA-256 into backup/manifest.json.

**Q:** How does verification work?

**A:** verify() re-hashes every file in the backup and compares against the manifest, reporting ok and failed lists.

**Q:** Does it preserve file metadata?

**A:** shutil.copy2 preserves file metadata like modification times along with the content.
