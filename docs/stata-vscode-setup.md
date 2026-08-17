# Stata VS Code Setup

This workspace includes a minimal Stata workflow for macOS with local validation.

## Current configuration

- VS Code extension recommendation: `deepecon.stata-mcp`
- VS Code extension recommendation: `kylebarron.stata-enhanced`
- Workspace Stata path: `/Applications/StataNow`
- Workspace Stata edition: `mp`
- CLI wrapper: `scripts/stata_exec.sh`

## One-time validation

Run the workspace task:

- `Stata: verify environment`

Expected output includes:

- `STATA_SMOKE: START`
- `STATA_ARITH: 4`
- `STATA_SMOKE: OK`

## Daily usage

Use the command palette or task runner for these flows:

- `Stata: run current file` to batch-run the active `.do` file.
- `Stata: Run Current File` from the `stata-vscode` extension for interactive editor-driven execution.
- `Stata: Run Selection/Current Line` from the same extension for focused checks.

## If Stata moves

If the app is no longer under `/Applications/StataNow`, update one of these:

- Set `STATA_BIN` to the exact CLI binary path.
- Set `STATA_APP_DIR` to the Stata install directory.
- Or adjust `stata-vscode.stataPath` in `.vscode/settings.json`.

The wrapper already checks these common app bundles:

- `/Applications/StataNow/StataMP.app`
- `/Applications/StataNow/StataSE.app`
- `/Applications/StataNow/StataBE.app`
- `/Applications/Stata/StataMP.app`
- `/Applications/Stata/StataSE.app`
- `/Applications/Stata/StataBE.app`