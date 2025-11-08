# Visual Sound Mirror

An interactive art piece that creates mesmerizing visuals and soothing bloopy sounds in response to movements detected through your webcam.

## Overview

Visual Sound Mirror transforms you into a living instrument. As you move in front of your camera, the application tracks your motion and translates it into:
- **Fluid, mesmerizing particle effects** that flow and pulse with your movements
- **Soothing, bloopy sounds** that respond to motion intensity and position
- **Calming color gradients** that shift based on activity

Perfect for meditation, creative expression, or just zoning out with some mesmerizing audio-visual feedback.

## Features

- **Real-time motion detection** using your webcam
- **Generative particle system** with physics-based animation
- **Web Audio synthesis** for organic, bloopy sounds
- **Zero dependencies** - pure HTML5, Canvas, and Web Audio API
- **Privacy-first** - all processing happens locally in your browser

## Quick Start

1. Open `index.html` in a modern web browser (Chrome, Firefox, Edge, Safari)
2. Grant camera permissions when prompted
3. Move in front of your camera and watch the magic happen!

## Controls

- **Click anywhere** to add a burst of particles
- **Wave your hands** for gentle ripples
- **Move quickly** for intense visual and audio effects
- **Stay still** to let the art settle into ambient mode

## Technical Details

- **Camera:** Uses MediaDevices API for webcam access
- **Motion Detection:** Pixel difference analysis between frames
- **Visuals:** HTML5 Canvas with particle system
- **Audio:** Web Audio API with oscillators and filters
- **Performance:** Optimized for smooth 60fps experience

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
