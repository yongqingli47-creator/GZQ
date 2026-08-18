---
description: "Build a reproducible data cleaning and analysis plan from attached data, code, notebooks, or variable lists."
argument-hint: "Describe the dataset, variables, scripts, or cleaning problem"
agent: "agent"
---

# Data Cleaning And Analysis Plan

Review the attached dataset description, code, notebook, or variable list and produce a rigorous data workflow.

Focus on:

1. Raw data structure and likely schema issues.
2. Variable type conversion and consistency checks.
3. Duplicate handling, missing-value rules, and outlier treatment.
4. Derived variable construction.
5. Validation checks before analysis.
6. Baseline analysis path and robustness priorities.

Output format:

- Data risks
- Cleaning pipeline
- Variable construction notes
- Validation checklist
- Baseline analysis plan
- Robustness priorities

Tool selection logic:

- Start from the attached data, scripts, notebooks, and repository environment.
- Recommend Stata, R, or Jupyter execution tooling only when the bottleneck is reproducible execution, inspection, or kernel control.
- Recommend causal or machine-learning packages only after the cleaning and baseline analysis path is clear.
- Keep external tool suggestions tied to a concrete implementation need, not as generic upgrades.

Prefer a plan that can be translated directly into code or a student task list.