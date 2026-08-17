# Zotero Batch Organizer

Use the repository literature resources to organize the current paper set.

Task:

1. Read `literature/metadata/zotero_items.json` and `literature/bib/library.bib` if present.
2. Build a structured literature matrix grouped by question, mechanism, method, and main findings.
3. Mark each paper as `must-read`, `useful`, or `peripheral` for the stated topic.
4. Flag where abstracts are missing, where metadata is stale, or where full-text reading is still necessary.
5. End with a short action list titled `Next Reading Moves`.

Output format:

- Topic assumption
- Paper clusters
- Literature matrix
- Reading priority
- Missing information
- Next reading moves

If I do not specify a topic, infer one from the most common themes in the repository library files.