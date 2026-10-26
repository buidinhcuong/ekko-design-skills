#!/usr/bin/env bash
# Zip every skill into dist/<skill>.zip for upload to claude.ai
# (Settings → Capabilities → Skills → Upload skill).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIST="$ROOT/dist"
rm -rf "$DIST"
mkdir -p "$DIST"

for skill_dir in "$ROOT"/plugins/*/skills/*/; do
  name="$(basename "$skill_dir")"
  [ -f "$skill_dir/SKILL.md" ] || continue
  (cd "$(dirname "$skill_dir")" && zip -qr "$DIST/$name.zip" "$name" -x '*.DS_Store' -x '*/__pycache__/*')
  echo "dist/$name.zip  ($(du -h "$DIST/$name.zip" | cut -f1))"
done
