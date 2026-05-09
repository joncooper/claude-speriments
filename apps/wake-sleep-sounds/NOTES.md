# Implementation Notes

## Why `NSWorkspace` notifications instead of IOKit?

The Apple-supported way to detect sleep/wake from a regular app is
`NSWorkspace.shared.notificationCenter` with `willSleepNotification` /
`didWakeNotification`. They fire reliably for both **lid close → sleep** and
**lid open → wake**, and don't require any entitlements.

The lower-level alternative is `IORegisterForSystemPower` (IOKit). It gives
you a few extra notification types and finer cancellation control, but it has
to be registered from a CFRunLoop and is overkill for "play a sound." Stuck
with `NSWorkspace`.

## Why a menu-bar (`LSUIElement`) app instead of a launchd agent?

A LaunchAgent daemon would also work, but then the user has no UI to pick
sounds, toggle it off, or test them. A menu bar app is a single binary the
user can drag into `/Applications`, add to Login Items, and forget — no
plist editing.

`LSUIElement = true` in `Info.plist` keeps it out of the Dock and out of
Cmd-Tab. The `moon.zzz` SF Symbol is the menu bar indicator.

## Why `AVAudioPlayer` instead of `NSSound`?

`NSSound` works fine for `.aiff` and `.wav`, but choking on some MP3/OGG
edge cases is well documented. `AVAudioPlayer` is the modern equivalent,
plays everything Core Audio can decode, and gives us `isPlaying` polling
which we need for the synchronous sleep playback.

## The "play before sleep" trick

`willSleepNotification` arrives on the main thread very shortly before the
kernel actually suspends. If we just kick off playback async, the jingle
gets cut off mid-sound. So `playSync(...)` runs the run-loop in a tight
loop until either the player reports it's done or a 2-second deadline
expires. macOS appears to give us roughly that long; longer is risky.

This means **short jingles work best for the sleep direction**. The defaults
(`steel-breeze` 1.55 s) fit comfortably; anything over ~1.8 s will likely
get clipped.

## Why convert OGG → WAV at the project level?

Kenney distributes the Music Jingles pack as OGG Vorbis. Core Audio on
macOS doesn't natively decode OGG, so playing them from `AVAudioPlayer`
would require a third-party decoder. Converting once to 44.1 kHz / 16-bit
PCM WAV via `ffmpeg` keeps the runtime dependency-free at the cost of
~1.6 MB of bundled audio.

If we need smaller bundle size later, AAC `.m4a` would cut that to maybe
300 KB with no audible difference at this length.

## Sound discovery is dynamic

`AppDelegate.discoverBundledSounds()` walks the `Sounds/` resource
directory and lists every `.wav`/`.aiff`/`.mp3`/`.m4a`. So users can drop
their own files in `Resources/Sounds/` before running `build.sh` and they
appear in the menu without code changes.

## Code signing

`build.sh` ad-hoc signs the bundle with `codesign --force --deep --sign -`.
Without signing, recent macOS versions will refuse to launch a freshly-built
app even from the same machine ("damaged" warning). Ad-hoc signing is enough
for local use; distribution would require a Developer ID cert and notarization,
both deliberately out of scope.

## Trade-offs / known limitations

- **No dynamic sound preview while picking** beyond playing the chosen
  one. Could add hover-to-preview, but submenus + AppKit hover events are
  surprisingly fiddly.
- **No volume control** in the app — relies on system volume. Users can
  always pick a quieter jingle from the bundle.
- **Sleep clip cutoff** as discussed above. Could try caching `playSync`'s
  loop into a higher-priority QoS, but the kernel deadline is the real
  ceiling.
- **No login item self-registration**. We could call
  `SMAppService.mainApp.register()` to handle this, but it adds a dependency
  on macOS 13+ and another permission prompt. Manual install via System
  Settings is fine for an experiment.
