# Implementation Notes

## Architecture

The Visual Sound Mirror is built as a single-page web application using vanilla JavaScript and browser APIs.

### Core Components

1. **Camera Manager** - Handles webcam access and frame capture
2. **Motion Detector** - Analyzes pixel differences to detect movement
3. **Particle System** - Generates and animates visual particles
4. **Sound Engine** - Synthesizes audio using Web Audio API
5. **Main Loop** - Coordinates updates at 60fps

## Technical Approach

### Motion Detection

Uses a simple but effective pixel difference algorithm:
- Capture current frame from webcam
- Compare with previous frame pixel-by-pixel
- Calculate motion intensity and position
- Use motion data to drive visuals and sound

Optimizations:
- Scale down video for faster processing (320x240)
- Sample every nth pixel for performance
- Use threshold to filter out noise

### Particle System

Physics-based particles with:
- Position, velocity, acceleration
- Life span and fade-out
- Color based on motion properties
- Attraction/repulsion forces

Rendering:
- Canvas 2D with alpha compositing
- Trail effects via canvas clearing with low alpha
- Glow effects using shadow blur

### Audio Synthesis

Web Audio graph:
- Multiple oscillator nodes (sine, triangle)
- Bandpass filters for bloopy character
- Gain envelopes for smooth attack/release
- Reverb for ambient space

Sound mapping:
- Motion intensity → Volume + Filter frequency
- Motion position X → Pitch
- Motion position Y → Timbre/waveform blend
- Overall activity → Reverb amount

## Design Decisions

### Why Web-Based?

- No installation required
- Cross-platform compatibility
- Easy to share and remix
- Access to powerful browser APIs

### Why No Dependencies?

- Faster loading
- Easier to understand and modify
- No build process needed
- Better for learning and experimentation

### Performance Considerations

Target: 60fps with smooth audio

Optimizations:
- RequestAnimationFrame for rendering
- Web Workers for heavy computation (future enhancement)
- Particle pooling to avoid GC pressure
- Efficient canvas operations (transform/restore)

## Customization Guide

### Adjusting Visual Style

In `app.js`, look for:

```javascript
// Particle colors
const PARTICLE_COLORS = [...];

// Particle physics
const PARTICLE_FRICTION = 0.95;
const PARTICLE_GRAVITY = 0.1;

// Trail effect
ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
```

### Tuning Sound

In `app.js`, modify:

```javascript
// Base frequency range
const MIN_FREQ = 200;
const MAX_FREQ = 800;

// Sound character
const OSCILLATOR_TYPE = 'sine'; // sine, triangle, square, sawtooth

// Volume envelope
const ATTACK_TIME = 0.1;
const RELEASE_TIME = 0.5;
```

### Motion Sensitivity

```javascript
// Motion threshold
const MOTION_THRESHOLD = 20; // Lower = more sensitive

// Motion smoothing
const MOTION_SMOOTHING = 0.7; // 0-1, higher = smoother
```

## Future Enhancements (ICEBOX)

- Hand tracking with MediaPipe for more precise control
- Multiple sound layers and scales
- Recording/screenshot capabilities
- Preset visual/audio themes
- MIDI output for controlling external synths
- Multi-user support (multiple people → multiple sound layers)
- VR mode using WebXR

## Known Issues

- Performance may vary on older devices
- Safari sometimes requires user gesture before audio plays
- Camera initialization can be slow on first load
- Motion detection struggles in low light

## Development Notes

Built during Claude Code session: claude/interactive-art-sound-visuals-011CUvuEddjAfeBTuyfHDNat

Key insights:
- Simple motion detection is surprisingly effective
- Web Audio API is powerful but requires careful gain management
- Canvas trail effects create mesmerizing visuals with minimal code
- User experience is greatly enhanced by smooth audio/visual transitions
