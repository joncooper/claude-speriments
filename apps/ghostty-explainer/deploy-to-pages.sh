#!/bin/bash
# Deploy Ghostty Explainer to GitHub Pages
set -e

APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$APP_DIR/../.." && pwd)"
DOCS_DIR="$REPO_ROOT/docs/ghostty-explainer"

echo "Deploying Ghostty Explainer to GitHub Pages..."
echo "  Source: $APP_DIR"
echo "  Target: $DOCS_DIR"

# Remove old deployment and copy fresh
rm -rf "$DOCS_DIR"
mkdir -p "$DOCS_DIR"

# Copy web files
cp "$APP_DIR/index.html" "$DOCS_DIR/"
cp "$APP_DIR/styles.css" "$DOCS_DIR/"
cp "$APP_DIR/app.js" "$DOCS_DIR/"

echo "Deployed to /docs/ghostty-explainer/"
echo "View at: https://joncooper.github.io/claude-speriments/ghostty-explainer/"
