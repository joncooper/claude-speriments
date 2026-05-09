# Wake/Sleep Sounds

A tiny menu-bar app for modern macOS that plays a cheerful jingle when your
MacBook wakes from sleep, and a gentler one just before it drifts off.

**Status:** Initial Spike

## What it does

- Listens for the system sleep/wake notifications using AppKit's
  `NSWorkspace.willSleepNotification` and `NSWorkspace.didWakeNotification`.
- On wake (lid open, power button, etc.) — plays the configured "wake" jingle.
- On the moment just before sleep (lid close, idle) — plays the configured
  "sleep" jingle synchronously, with a short timeout so the sound has a chance
  to finish before the kernel halts audio.
- Lives in the menu bar (`moon.zzz` icon) — no Dock icon, no main window.
- Lets you pick from 10 bundled jingles for both events, test them, or disable
  the whole thing temporarily.
- Remembers your picks in `UserDefaults`.

## Bundled sounds

10 short musical jingles from [Kenney's Music Jingles](https://kenney.nl/assets/music-jingles)
(CC0 / public domain): two each from 8-bit, drum-hit, pizzicato, sax, and
steel-drum families. Defaults are `8bit-fanfare` for wake and `steel-breeze`
for sleep. See [`Resources/Sounds/CREDITS.md`](Resources/Sounds/CREDITS.md)
for the full list and licensing.

You can drop more `.wav` / `.aiff` / `.mp3` / `.m4a` files into
`Resources/Sounds/` before building — the app discovers them at launch.

## Requirements

- macOS 12 (Monterey) or newer
- Xcode command-line tools (for `swift` and `codesign`)

## Build & run

```bash
cd apps/wake-sleep-sounds
./build.sh
open "build/Wake Sleep Sounds.app"
```

`build.sh`:
1. Compiles the Swift package in release mode.
2. Assembles a proper `.app` bundle at `build/Wake Sleep Sounds.app` with
   `Info.plist` (including `LSUIElement = true` so it stays out of the Dock)
   and the bundled sounds in `Contents/Resources/Sounds/`.
3. Ad-hoc code signs it so Gatekeeper will let you launch it locally.

## Install permanently

```bash
cp -R "build/Wake Sleep Sounds.app" /Applications/
```

To launch it automatically at login: **System Settings → General → Login
Items → +** and pick the app.

## Sleep-sound caveat

macOS only gives apps a brief window between `willSleepNotification` and
the actual suspend. The app waits up to ~2 seconds for the sleep jingle to
finish; longer clips may be cut off. Short stingers (under 1.5 s) work most
reliably for the sleep direction. The wake direction has no such limit.

## Project layout

```
wake-sleep-sounds/
├── Package.swift
├── Sources/WakeSleepSounds/
│   ├── main.swift             # NSApplication bootstrap
│   └── AppDelegate.swift      # menu bar + sleep/wake observers + playback
├── Resources/
│   ├── Info.plist             # bundle metadata, LSUIElement = true
│   └── Sounds/                # 10 .wav jingles + CREDITS.md
├── build.sh                   # SPM build → .app bundle, ad-hoc signs it
├── NOTES.md
├── ICEBOX.md
└── README.md
```

## Uninstall

```bash
rm -rf "/Applications/Wake Sleep Sounds.app"
defaults delete com.claudespriments.wakesleepsounds
```
