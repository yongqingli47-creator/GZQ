#!/bin/zsh

set -euo pipefail

script_dir=${0:A:h}
workspace_dir=${script_dir:h}
replication_dir="${workspace_dir}/replications/ai_innovation"

cd "${replication_dir}"
exec "${workspace_dir}/scripts/stata_exec.sh" -b do 00_run_replication.do