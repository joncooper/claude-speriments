#!/bin/bash
# Deploy 3D Scan Viewer to GitHub Pages

set -e

APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$APP_DIR/../.." && pwd)"
DOCS_DIR="$REPO_ROOT/docs/3d-scan-viewer"

echo "🔨 Building production bundle..."
cd "$APP_DIR"
bun run build

echo "📦 Deploying to GitHub Pages..."

# Remove old deployment
rm -rf "$DOCS_DIR"
mkdir -p "$DOCS_DIR"

# Copy built files
cp -r "$APP_DIR/dist"/* "$DOCS_DIR/"

# Remove build artifacts we don't need on GitHub Pages
rm -f "$DOCS_DIR"/.gitignore

echo "✅ Deployed to /docs/3d-scan-viewer/"
echo ""
echo "Next steps:"
echo "  1. Update /docs/index.html with a card for this app"
echo "  2. git add docs/"
echo "  3. git commit -m 'Deploy 3D Scan Viewer to GitHub Pages'"
echo "  4. git push"
echo ""
echo "The app will be live at:"
echo "  https://joncooper.github.io/claude-speriments/3d-scan-viewer/"
