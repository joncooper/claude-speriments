# Sound Credits

The 10 sounds bundled here are short musical jingles from
[Kenney's Music Jingles](https://kenney.nl/assets/music-jingles) pack by
Kenney Vleugels, released under [Creative Commons CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)
(public domain, no attribution required).

Files were converted from OGG Vorbis to 44.1 kHz / 16-bit stereo PCM WAV via
ffmpeg so they play natively through `NSSound` on macOS.

## Bundled jingles

| Filename | Family | Duration | Vibe |
|----------|--------|----------|------|
| `8bit-fanfare.wav` | NES 8-bit | 1.76s | Triumphant chiptune fanfare |
| `8bit-coin.wav` | NES 8-bit | 0.44s | Snappy coin-grab arpeggio |
| `hit-bright.wav` | Drum hit | 0.28s | Quick stinger, upbeat |
| `hit-warm.wav` | Drum hit | 0.75s | Warm closing thud |
| `pizzicato-skip.wav` | Pizzicato strings | 0.49s | Skipping plucks |
| `pizzicato-stroll.wav` | Pizzicato strings | 1.32s | Lighthearted little tune |
| `sax-hello.wav` | Saxophone | 0.39s | Cheeky greeting |
| `sax-noir.wav` | Saxophone | 1.74s | Smooth jazzy phrase |
| `steel-island.wav` | Steel drum | 0.93s | Tropical "ta-da" |
| `steel-breeze.wav` | Steel drum | 1.55s | Mellow island ripple |

## Adding your own sounds

Drop any `.wav`, `.aiff`, `.mp3`, or `.m4a` file into this directory before
running `./build.sh`. The app discovers everything in its `Sounds/` resource
folder at launch and adds it to the menu automatically.

## Source

- Original pack: <https://kenney.nl/assets/music-jingles>
- Mirror used for downloads in this project's history: same as above
