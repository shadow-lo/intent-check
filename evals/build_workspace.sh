#!/usr/bin/env bash
# Builds one throwaway git workspace per scenario:
#   commit 1 = "before" (baseline), working tree = "after" (uncommitted agent work).
# Usage: evals/build_workspace.sh <output-dir>
# Writes only inside <output-dir>. No network access. No global git config changes.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
out="${1:?usage: build_workspace.sh <output-dir>}"
umask 077
mkdir -p "$out"
for s in "$here"/scenarios/*/; do
  name="$(basename "$s")"
  ws="$out/$name"
  rm -rf "$ws"; mkdir -p "$ws/repo"
  cp -R "$s/before/." "$ws/repo/"
  printf '__pycache__/\n' > "$ws/repo/.gitignore"
  git -C "$ws/repo" init -q -b main
  git -C "$ws/repo" -c user.name=eval -c user.email=eval@example.invalid add -A
  git -C "$ws/repo" -c user.name=eval -c user.email=eval@example.invalid commit -q -m baseline
  cp -R "$s/after/." "$ws/repo/"
  cp "$s/transcript.md" "$ws/transcript.md"
  [ -f "$s/contract.v1.md" ] && mkdir -p "$ws/contracts" && cp "$s/contract.v1.md" "$ws/contracts/contract.v1.md"
  echo "built $ws"
done
