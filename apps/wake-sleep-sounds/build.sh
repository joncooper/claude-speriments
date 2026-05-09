#!/usr/bin/env bash
# Build a self-contained Wake/Sleep Sounds.app bundle.
# Requires Swift 5.9+ (Xcode command-line tools) on macOS 12+.

set -euo pipefail

cd "$(dirname "$0")"

APP_NAME="Wake_Sleep Sounds"   # final display name uses slash; filesystem uses underscore-ish
APP_DIR="build/Wake Sleep Sounds.app"
EXE_NAME="WakeSleepSounds"

echo "[1/4] Compiling Swift package (release)..."
swift build -c release

EXE_PATH="$(swift build -c release --show-bin-path)/$EXE_NAME"

if [[ ! -x "$EXE_PATH" ]]; then
    echo "Build failed: $EXE_PATH not found" >&2
    exit 1
fi

echo "[2/4] Assembling app bundle at $APP_DIR ..."
rm -rf "$APP_DIR"
mkdir -p "$APP_DIR/Contents/MacOS"
mkdir -p "$APP_DIR/Contents/Resources/Sounds"

cp "$EXE_PATH" "$APP_DIR/Contents/MacOS/$EXE_NAME"
cp "Resources/Info.plist" "$APP_DIR/Contents/Info.plist"

echo "[3/4] Copying bundled sounds..."
shopt -s nullglob
for f in Resources/Sounds/*.{wav,aiff,aif,mp3,m4a,caf}; do
    cp "$f" "$APP_DIR/Contents/Resources/Sounds/"
done
# Copy CREDITS as a plain reference too (optional).
[[ -f Resources/Sounds/CREDITS.md ]] && cp Resources/Sounds/CREDITS.md "$APP_DIR/Contents/Resources/Sounds/"

echo "[4/4] Ad-hoc code signing (so macOS lets you run it locally)..."
codesign --force --deep --sign - "$APP_DIR" || \
    echo "  (codesign failed — you may need to right-click → Open the first time.)"

echo
echo "Done.  Open it with:"
echo "  open \"$APP_DIR\""
echo
echo "To install permanently:"
echo "  cp -R \"$APP_DIR\" /Applications/"
echo
echo "To run at login: System Settings → General → Login Items → add the app."
