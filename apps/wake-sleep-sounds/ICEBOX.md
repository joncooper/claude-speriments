# Future Ideas

Captured during initial spike — not committed to any of these.

## Polish
- **Hover-to-preview** in the sound picker submenu, so you can audition
  jingles without committing.
- **Volume slider** in the menu, separate from system volume.
- **Random mode**: pick a different jingle each wake/sleep instead of a
  fixed default. Could be tied to time of day (mellower at night).
- **Quiet hours**: disable sounds between, e.g., 22:00 and 07:00.

## More events worth jingling
- AC power connect / disconnect
- Headphones plug / unplug
- External display attach / detach
- macOS lock-screen engage / disengage (`com.apple.screenIsLocked`)

## Self-installation
- One-click "Launch at login" using `SMAppService.mainApp.register()` so
  users don't have to dig through System Settings.
- Sparkle-style auto-update (probably overkill for a hobby app).

## Distribution
- Notarized DMG with drag-to-Applications layout.
- Homebrew Cask formula.

## Sound-pack expansion
- Categorize bundled sounds by mood (Cheerful / Subtle / Retro / Tropical)
  and group submenus accordingly.
- Ship a separate "voice line" pack (e.g., "good morning!", "see you soon")
  — would need TTS-generated CC0 clips or hand-recorded voiceover.
- User-provided sound directory at `~/Library/Application Support/WakeSleepSounds/Sounds/`
  scanned at launch, in addition to bundle resources.

## Telemetry-free feedback
- Optional local log of wake/sleep events with chosen sound — could be a
  fun "you woke up your Mac 138 times this month" stat.
