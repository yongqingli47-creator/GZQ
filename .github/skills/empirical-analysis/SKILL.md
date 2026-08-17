---
name: empirical-analysis
description: "Use this skill for empirical research tasks involving data cleaning, variable construction, estimation strategy, robustness checks, reproducibility, or notebook and script review"
---

# Empirical Analysis Skill

Use this skill for data cleaning, data construction, empirical analysis, and estimation work.

## Core Priorities

1. Reproducibility before sophistication.
2. Clear mapping from theory to variables.
3. Explicit sample restrictions and missing-data handling.
4. Identification assumptions stated in plain language.
5. Robustness checks chosen to challenge the main claim, not decorate it.
6. Data cleaning choices documented so another researcher can reproduce them.

## Review Checklist

- What is the unit of analysis?
- How are key variables defined and transformed?
- What observations are excluded, and why?
- How are duplicates, outliers, and missing values handled?
- What is the baseline model and why is it appropriate?
- What alternative explanations remain?
- What output or diagnostic would falsify the current claim?

## Implementation Guidance

- Prefer scripts over manual spreadsheet operations.
- Keep paths, seeds, and environment assumptions explicit.
- When reviewing notebooks, separate exploratory cells from reproducible pipeline logic.
- When asked to clean data, propose a pipeline covering import, schema checks, type conversion, duplicate handling, missing values, outlier rules, derived variables, validation, and export.