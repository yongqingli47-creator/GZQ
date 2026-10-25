# Research Agent Workflow

This repository now supports literature-grounded AI workflows through repository-local Zotero resources.

## Literature Sources The Agent Should Read

1. `literature/bib/library.bib` when present, otherwise collection-specific `.bib` files in the same folder
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
- Run the `Repository: validate Copilot customizations` task after changing prompt files, skills, instructions, or agent workflow guidance.
- Treat abstract-based synthesis as a screening layer, not a substitute for full-paper verification.
- Narrow to a collection or topic if the library is too broad for a precise review.

## External AI Tool Evaluation And Research Gates

The supplied *Social Science AI Tool Map* is a discovery directory, not a vetted catalog. It mixes prompts, code packages, MCP servers, hosted services, and research systems. Its star counts, labels such as “standard” or “SOTA,” feature descriptions, and installation commands are not independently established by the directory and may become stale. Do not copy those claims into repository defaults.

Before adding an external tool:

1. Name the concrete research bottleneck and the improvement expected over the existing local workflow.
2. Check the tool's primary repository and documentation, license, release and maintenance status, supported versions, dependencies, data handling, credential scope, and any external write or paid-service behavior.
3. Start with the smallest read-only or dry-run task on non-sensitive data. Compare the output with an independent source, known fixture, or canonical local script.
4. Record the tool/version, configuration, inputs or queries, outputs, and validation decision. Keep it optional unless it has a demonstrated advantage; local evidence and reproducible scripts remain authoritative.
5. Confirm authorization and a suitable data path before installing software, exposing credentials, uploading restricted data, or allowing external writes.

Apply the following evidence boundaries across the workflow:

- **Literature:** use search services for discovery, then verify metadata and publication status and read the source before relying on a specific finding. Abstracts and AI summaries are screening aids.
- **Empirical analysis:** select the method from the design and estimand first. An MCP server is an execution interface, and a statistical package is an implementation; neither validates identification. Preserve code, environment, inputs, logs, and outputs.
- **Systematic review:** define screening rules before using automated ranking, retain a search/deduplication/screening record, and keep researcher adjudication visible.
- **Manuscript review:** use simulated reviewers to surface possible objections, then verify each against evidence. Simulated feedback is not real peer review or a source for factual claims.

Use `literature-synthesis`, `zotero-library-ops`, `empirical-analysis`, `manuscript-polish`, and `research-planning` for the corresponding detailed checks.
