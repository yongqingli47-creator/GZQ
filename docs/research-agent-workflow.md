# Research Agent Workflow

This repository now supports literature-grounded AI workflows through repository-local Zotero resources.

## Literature Sources The Agent Should Read

1. `literature/bib/library.bib` or collection-specific `.bib` files
2. `literature/metadata/zotero_items.json`
3. `literature/metadata/zotero_items.md`

## Agent Rules Added To The Repository

- `AGENTS.md` now points literature-heavy work to `zotero-library-ops`.
- `.github/instructions/zotero-library.instructions.md` defines source priority and reproducibility rules.
- `.github/skills/zotero-library-ops/SKILL.md` defines how to organize, triage, and synthesize library content.

## Prompt Files For Batch Tasks

Use these prompt files from chat:

- `/zotero-batch-organize`
- `/zotero-review-outline`
- `/literature-review`
- `/literature-matrix`

## Recommended Usage Patterns

### Batch literature organization

Ask for:

```text
Use /zotero-batch-organize and focus on digital innovation and corporate governance.
```

### Literature review drafting

Ask for:

```text
Use /zotero-review-outline and build a review for executive compensation and ESG disclosure.
```

### Paper outline generation

Ask for:

```text
Use /zotero-review-outline and convert the current literature set into a paper outline.
```

## Quality Control

- Refresh the metadata snapshot before major literature tasks.
- Treat abstract-based synthesis as a screening layer, not a substitute for full-paper verification.
- Narrow to a collection or topic if the library is too broad for a precise review.