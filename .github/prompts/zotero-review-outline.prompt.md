---
description: "Use repository Zotero resources to build a literature review structure and paper outline."
argument-hint: "Describe the topic, chapter, or paper you want to outline"
agent: "agent"
---

# Zotero Review And Outline Builder

Use the repository literature resources to draft a review structure and a paper outline.

Task:

1. Read `literature/metadata/zotero_items.json`, `literature/metadata/zotero_items.md`, and `literature/bib/library.bib` when present; otherwise read other `.bib` exports under `literature/bib/`.
2. Infer the most relevant literature subset for my topic.
3. Produce a literature review structure organized by question, mechanism, identification, and findings.
4. Convert that structure into a paper outline with section goals and candidate references for each section.
5. State what still needs full-text verification.

Output format:

- Research question
- Literature map
- Review section structure
- Paper outline
- Reference placement
- Verification gaps

Tool selection logic:

- Treat repository Zotero exports as the default source base.
- If the snapshot is stale or the target topic is under-covered, first say so explicitly.
- Upgrade to live Zotero tooling when the task depends on current collections, tags, or recently added papers.
- Upgrade to OpenAlex, Semantic Scholar, or paper-search tools only if topic expansion is necessary after narrowing the scope.
- Recommend citation-checking tools before finalizing a reference-heavy outline when metadata quality is uncertain.

If the current repository sources are too broad, first propose a narrower scope and proceed with that scope.