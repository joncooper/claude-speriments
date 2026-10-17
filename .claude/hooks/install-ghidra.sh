#!/bin/bash
# SessionStart hook: install Ghidra for the REA MCP server in Claude Code cloud
# sessions, where /opt is wiped between containers. No-op locally or when
# Ghidra is already present.
set -euo pipefail

[ "${CLAUDE_CODE_REMOTE:-}" = "true" ] || exit 0

GHIDRA_VERSION=12.1.4
GHIDRA_DATE=20260921
GHIDRA_SHA256=ddac49f903da9d5bac833e5cc79395098b9c33cfd3279be5f31bd00387d2d4db
GHIDRA_DIR=/opt/ghidra_${GHIDRA_VERSION}_PUBLIC

[ -x "$GHIDRA_DIR/support/analyzeHeadless" ] && exit 0

zip=$(mktemp --suffix=.zip)
trap 'rm -f "$zip"' EXIT
curl -sSfL -o "$zip" \
  "https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_${GHIDRA_VERSION}_build/ghidra_${GHIDRA_VERSION}_PUBLIC_${GHIDRA_DATE}.zip"
echo "$GHIDRA_SHA256  $zip" | sha256sum -c --quiet
unzip -q "$zip" -d /opt
echo "Installed Ghidra $GHIDRA_VERSION to $GHIDRA_DIR"
