# Visual Sound Mirror - v6.0 Music Synthesis Edition

An interactive music instrument that transforms your gestures into sound and visuals. Features four distinct modes: flowing ribbons, theremin synthesis, drum pads, and parameter knobs - all controlled through webcam hand tracking.

## Overview

Visual Sound Mirror v6.0 transforms you into a multi-mode musical instrument with gesture-controlled synthesis:

### 🎨 **Ribbons Mode** (Default)
- Each fingertip creates 3 parallel flowing silk ribbons
- Width responds to finger spread
- Dynamic colors based on color theory (aurora, sunset, ocean, forest, cosmic)
- **Left hand**: Pinch/spread fingers to control filter cutoff and resonance (300-3000Hz)
- **Right hand**: Pinch/spread fingers to control delay/echo amount
- Touch fingertips together → harmonic chords
- Smooth, organic motion - ephemeral and responsive

### 🎵 **Theremin Mode**
- Play melodies with hand position in 3D space
- **X-axis**: Pitch (quantized to musical scale)
- **Y-axis**: Filter brightness (200-4000Hz)
- **Finger spread**: Resonance/vibrato intensity
- **Scale selection**: Pentatonic, Major, Minor, Blues, Dorian, Phrygian, Chromatic
- Visual scale guide shows note positions
- Continuous oscillator with smooth portamento

### 🥁 **Sample Pads Mode**
- 4x4 grid of gesture-triggered samples (16 pads total)
- Tap with any fingertip to trigger sounds
- **Drums**: Kick, Snare, Hi-hat, Clap, Toms, Rim, Cowbell
- **Cymbals**: Crash, Ride
- **Synths**: Bass, Chord pads (Major/Minor), Lead
- **Percussion**: Various percussive sounds
- Real-time synthesis - no audio files needed

### 🎛️ **Knobs Mode**
- Virtual rotary knobs controlled by index finger rotation
- **Filter**: Cutoff frequency (200-4000Hz)
- **Delay**: Echo/delay mix amount
- **Resonance**: Filter Q factor (0.1-20)
- **Reverb**: Reverb amount (coming soon)
- Visual feedback with arc indicators

**Core Features:**
- AI-powered hand tracking (up to 2 hands, 21 landmarks each)
- Sophisticated Web Audio synthesis engine
- Real-time visual feedback for all interactions
- Privacy-first: all processing happens locally in browser

## Features

- **AI-powered hand tracking** using Google MediaPipe (tracks up to 2 hands with 21 landmarks each)
- **Real-time motion detection** from your webcam
- **Generative particle system** with physics-based animation
- **Web Audio synthesis** for organic, bloopy sounds with reverb
- **Debug mode** to see hand tracking in action
- **Visual feedback** - circles show where your hands are detected
- **Privacy-first** - all processing happens locally in your browser

## Quick Start

1. Open `index.html` in a modern web browser (Chrome, Firefox, Edge, Safari)
2. Grant camera permissions when prompted
3. Move in front of your camera and watch the magic happen!

## Controls

### Mode Switching
- **🎨 button** or **Press 1** - Ribbons Mode (flowing silk ribbons)
- **🎵 button** or **Press 2** - Theremin Mode (melodic instrument)
- **🥁 button** or **Press 3** - Sample Pads Mode (drum machine)
- **🎛️ button** or **Press 4** - Knobs Mode (parameter control)

### General Controls
- **🔊 button** - Toggle audio on/off
- **🔍 button** - Toggle debug mode (shows hand tracking skeleton)
- **ℹ️ button** - Show detailed help information
- **S key** - Cycle through musical scales (Theremin mode only)
- **Click anywhere** - Play a chord (Ribbons mode only)

### Gestures
- **Pinch/spread fingers** - Modulate sound parameters
- **Touch fingertips together** - Trigger harmonic chords (Ribbons mode)
- **Tap pads with fingertips** - Trigger drum samples (Pads mode)
- **Circle index finger around knob** - Rotate parameter value (Knobs mode)
- **Move hand across screen** - Control pitch/filter (Theremin mode)

## Technical Details

- **Camera:** Uses MediaDevices API for webcam access
- **Hand Tracking:** Google MediaPipe Hands ML model (tracks 21 hand landmarks per hand)
- **Motion Detection:** AI-powered hand tracking with position and movement analysis
- **Visuals:** HTML5 Canvas with particle system and real-time hand position indicators
- **Audio:** Web Audio API with oscillators, filters, and reverb
- **Performance:** Optimized for smooth 60fps experience
- **Dependencies:** MediaPipe Hands library (loaded from CDN)

## Browser Support

Requires a modern browser with support for:
- getUserMedia API (webcam access)
- Canvas 2D
- Web Audio API

Tested on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Privacy

All processing happens locally in your browser. No video or audio data is transmitted, recorded, or stored anywhere. The camera feed is only used for motion detection calculations.

## Customization

See `NOTES.md` for details on customizing:
- Particle behavior and appearance
- Sound synthesis parameters
- Motion sensitivity
- Color palettes

## License

MIT License - feel free to remix and experiment!
