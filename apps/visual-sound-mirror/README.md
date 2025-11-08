# Visual Sound Mirror

An interactive art piece that creates mesmerizing visuals and soothing bloopy sounds in response to movements detected through your webcam.

## Overview

Visual Sound Mirror transforms you into a living instrument with sophisticated multi-hand interactions:

**Fluid Silk Ribbons:**
- Each fingertip creates 3 parallel flowing ribbons
- Width responds to finger spread
- Dynamic colors based on color theory (aurora, sunset, ocean schemes)
- Smooth, organic motion - no hyperactive particles

**Sophisticated Audio:**
- **Left hand**: Pinch/spread fingers to control filter cutoff and resonance (300-3000Hz)
- **Right hand**: Pinch/spread fingers to control delay/echo amount
- Horizontal position controls pitch (200-800Hz)
- Movement velocity controls volume

**Two-Hand Gestures:**
- Touch fingertips together → harmonic chords
- Bring hands close → special pulsing glow effect
- Stretch hands apart like pulling dough → dynamic audio modulation

**Responsive & Ephemeral:**
- Every effect tied directly to your fingertips
- Screen clears to black within 1 second when hands leave

Perfect for meditation, creative expression, or just zoning out with some mesmerizing audio-visual feedback.

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

- **Wave your hands** to create particles and sounds at your fingertips
- **Move quickly** for intense visual and audio effects
- **Click anywhere** to add a burst of particles
- **🔊 button** - Toggle audio on/off
- **🔍 button** - Toggle debug mode (shows hand tracking skeleton and stats)
- **ℹ️ button** - Show help information
- **Stay still** to let the art settle into ambient mode

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
