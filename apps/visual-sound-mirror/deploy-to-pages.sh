#!/bin/bash
# Deploy Visual Sound Mirror to GitHub Pages
# This script copies the necessary files from the app to /docs/visual-sound-mirror/
# for hosting via GitHub Pages.

set -e  # Exit on error

APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$APP_DIR/../.." && pwd)"
DOCS_DIR="$REPO_ROOT/docs/visual-sound-mirror"

echo "Deploying Visual Sound Mirror to GitHub Pages..."
echo "App directory: $APP_DIR"
echo "Docs directory: $DOCS_DIR"

# Create docs directory if it doesn't exist
mkdir -p "$DOCS_DIR"

# Remove old deployment
rm -rf "$DOCS_DIR"
mkdir -p "$DOCS_DIR"

# Copy all files from app directory
cp -r "$APP_DIR"/* "$DOCS_DIR/"

# Remove documentation and script files (not needed for web deployment)
find "$DOCS_DIR" -type f -name '*.md' -delete
rm -f "$DOCS_DIR/deploy-to-pages.sh"

echo "✅ Deployment complete!"
echo "The app is now available at: /docs/visual-sound-mirror/"
echo ""
echo "To test locally:"
echo "  cd $DOCS_DIR"
echo "  python3 -m http.server 8000"
echo "  # Then visit http://localhost:8000"
