#!/bin/zsh

set -euo pipefail

if [[ $# -eq 0 ]]; then
  echo "Usage: $0 <stata arguments>" >&2
  exit 64
fi

candidate_bins=()

if [[ -n "${STATA_BIN:-}" ]]; then
  candidate_bins+=("${STATA_BIN}")
fi

if [[ -n "${STATA_APP_DIR:-}" ]]; then
  candidate_bins+=(
    "${STATA_APP_DIR}/StataMP.app/Contents/MacOS/stata-mp"
    "${STATA_APP_DIR}/StataSE.app/Contents/MacOS/stata-se"
    "${STATA_APP_DIR}/StataBE.app/Contents/MacOS/stata-be"
  )
fi

candidate_bins+=(
  "/Applications/StataNow/StataMP.app/Contents/MacOS/stata-mp"
  "/Applications/StataNow/StataSE.app/Contents/MacOS/stata-se"
  "/Applications/StataNow/StataBE.app/Contents/MacOS/stata-be"
  "/Applications/Stata/StataMP.app/Contents/MacOS/stata-mp"
  "/Applications/Stata/StataSE.app/Contents/MacOS/stata-se"
  "/Applications/Stata/StataBE.app/Contents/MacOS/stata-be"
)

for candidate_bin in "${candidate_bins[@]}"; do
  if [[ -x "${candidate_bin}" ]]; then
    exec "${candidate_bin}" "$@"
  fi
done

echo "No Stata command-line binary was found." >&2
echo "Set STATA_BIN to the full binary path or STATA_APP_DIR to the Stata install directory." >&2
exit 127