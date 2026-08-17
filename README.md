# GitHub Copilot Customization Starter Kit

This folder contains a curated starter kit for GitHub Copilot customizations.

What is included:

- Repository-wide instructions in `.github/copilot-instructions.md`
- Agent workflow guidance in `AGENTS.md`
- Path-specific workflow instructions in `.github/instructions/`
- Reusable prompt files in `.github/prompts/`
- Reusable skills in `.github/skills/`
- VS Code workspace settings in `.vscode/settings.json`

Source basis:

- GitHub Docs: repository custom instructions, prompt files, and support matrix
- GitHub Docs customization library: code review, debugging, testing automation, and GitHub Actions helper
- GitHub official repositories: skill directory structure and `SKILL.md` format

Recommended next step:

Open this folder in VS Code, keep GitHub Copilot enabled, and invoke prompt files with `/` in chat after confirming `chat.promptFiles` is enabled.

For ongoing maintenance, run the `Repository: validate Copilot customizations` task after editing prompts, skills, instructions, or agent guidance files.

## Stata In VS Code

This workspace is now prepared for local Stata usage on macOS.

- Run `Research: verify all environments` for a single workspace-wide health check covering Stata, PostgreSQL, and Zotero.
- VS Code settings include a Stata MCP path pointing to `/Applications/StataNow` with MP edition selected.
- Workspace tasks include `Stata: verify environment` and `Stata: run current file`.
- The wrapper script `scripts/stata_exec.sh` auto-detects common Stata app bundles if the install location changes.

Use [docs/stata-vscode-setup.md](docs/stata-vscode-setup.md) for the full workflow and validation steps.

## Zotero Research Workflow

This repository now includes a VS Code + Zotero workflow built around:

- Zotero official API via `pyzotero`
- `socksio` support so Zotero requests remain stable when the shell exports SOCKS proxy variables
- Better BibTeX auto-export into `literature/bib/`, with `library.bib` preferred but not required
- Repository-local metadata snapshots in `literature/metadata/`
- Prompt files and skills for batch literature organization and review drafting

Start with [docs/zotero-vscode-setup.md](docs/zotero-vscode-setup.md) for the end-to-end setup.

For a no-write connectivity check, run `./.venv/bin/python scripts/zotero_sync.py --limit 1 --dry-run`.

## PostgreSQL In VS Code

This workspace is now prepared for local PostgreSQL usage on macOS with a Homebrew installation.

- Use TCP loopback settings in `.env` so VS Code Agent and sandboxed commands avoid local socket path issues.
- Install Python database dependencies with `Python: install research dependencies`.
- Run `PostgreSQL: verify environment` to confirm Python connectivity and PostGIS availability against the configured database.
- For a workspace-wide check, run `Research: verify all environments`.
- If you call scripts directly from a shell without activating the environment, prefer `./.venv/bin/python` over the system `python3`.

Recommended `.env` baseline:

- `PGHOST=127.0.0.1`
- `PGPORT=5432`
- `PGDATABASE=postgres`
- `PGUSER=` your macOS username unless you created another database role
- `PGSSLMODE=disable`

If you prefer a single connection string, set `POSTGRES_DSN` and leave the individual `PG*` variables as defaults or blanks.