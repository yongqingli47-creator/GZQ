---
applyTo: "literature/**/*.bib,literature/**/*.json,literature/**/*.md,papers/**/*.md,scripts/zotero_*.py,docs/**/*.md"
---

When working with repository literature resources:

## Source Priority
- Treat `literature/bib/*.bib` as the citekey and bibliography source of truth.
- Treat `literature/metadata/zotero_items.json` as the structured metadata and abstract snapshot generated from Zotero.
- Treat `literature/metadata/zotero_items.md` as the quick human-readable library digest.

## Working Standard
- Ground claims in available titles, abstracts, creators, years, venues, tags, and collections before inferring contributions.
- If asked to compare many papers, cluster them by question, mechanism, method, and findings.
- Flag when the local snapshot is stale, empty, or narrower than the user request.
- Do not invent findings beyond what the local literature files support.

## Batch Research Tasks
- For literature organization, produce sortable structures such as matrices, coding frames, priority tiers, and gap maps.
- For literature reviews, separate consensus, disagreement, identification limits, and contribution space.
- For paper outlines, map references to specific sections rather than appending a generic reading list.

## Reproducibility
- Prefer workflows that can be rerun after each Zotero update.
- Keep generated metadata files deterministic and easy to diff.