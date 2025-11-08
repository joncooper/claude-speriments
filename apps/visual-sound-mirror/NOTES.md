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

**Version 2.0 - MediaPipe Hand Tracking:**

The app now uses Google's MediaPipe Hands ML model for precise hand tracking:
- Detects up to 2 hands in real-time
- Tracks 21 3D landmarks per hand (fingertips, knuckles, palm, wrist)
- Palm center (landmark 9) and 5 fingertips become particle sources
- Movement calculated from position delta between frames
- Much more responsive and accurate than pixel difference

Key improvements:
- Particles spawn directly from fingertips - obvious visual connection
- Each finger can create its own particle stream
- Hand position circles show exactly where tracking is working
- Debug mode displays full hand skeleton for verification

Audio responsiveness:
- Horizontal hand position (X) maps to pitch (200-800Hz)
- Motion intensity maps to volume
- Multiple sounds play polyphonically for multiple detected points
- Sound generation throttled to 100ms intervals for musicality

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

**CRITICAL FIX - Audio Context Resume:**

Browsers (especially Safari/iOS) suspend the AudioContext by default until user interaction. The app now:
1. Initializes AudioContext immediately on start
2. Sets up event listeners for click/touch/keydown to resume audio
3. Checks and resumes audio context state before playing each sound
4. Logs audio state to console for debugging

Web Audio graph:
- Sine oscillators with frequency glide (400ms envelope)
- Lowpass filters (Q=3) for warm, bloopy character
- Gain envelopes with quick attack (30ms) and smooth release (400ms)
- Reverb (2.5s decay) for ambient space
- Master gain set to 0.2 (comfortable volume)

Sound mapping:
- Hand position X → Pitch (200-800Hz range)
- Motion intensity → Volume (0.1-0.25 range)
- Multiple hands/fingers → Polyphonic bloops with 50ms stagger
- Throttled to 100ms minimum between sound bursts

Debug mode shows audio context state (running/suspended/muted)

## Design Decisions

### Why Web-Based?

- No installation required
- Cross-platform compatibility
- Easy to share and remix
- Access to powerful browser APIs

### Dependencies

**MediaPipe Hands** (loaded from CDN):
- Google's production-ready hand tracking ML model
- ~2MB download, cached by browser
- Runs efficiently on CPU (no GPU required)
- 60fps performance on modern hardware

Why MediaPipe over pixel difference:
- Much more accurate and responsive
- Works in varied lighting conditions
- Provides precise fingertip locations
- Natural interaction model (point with fingers)
- Industry-standard solution used in production apps

### Performance Considerations

Target: 60fps with smooth audio

Optimizations:
- RequestAnimationFrame for rendering
- Web Workers for heavy computation (future enhancement)
- Particle pooling to avoid GC pressure
- Efficient canvas operations (transform/restore)

## Debug Mode

Press the 🔍 button to toggle debug mode, which shows:

**Debug Panel (top-left):**
- Motion Intensity: Current movement level (0-1)
- Position: Average hand position as percentage
- Particles: Current particle count
- Audio: AudioContext state (running/suspended) and mute status
- Hands Detected: Number of hands currently tracked (0-2)

**Visual Debugging:**
- Hand skeleton overlay with all 21 landmarks
- Connection lines showing hand structure
- Red dots at each landmark point
- Yellow circles at palm centers
- Blue circles at fingertips

Use debug mode to:
- Verify hand tracking is working
- See exactly where particles are spawning
- Troubleshoot audio issues (check if "running")
- Understand how the system responds to movement
- Fine-tune sensitivity settings

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

**Version 1.0 Issues:**
- Audio didn't work due to AudioContext suspension
- Motion detection (pixel diff) was too subtle
- No obvious connection between movement and effects
- Difficult to debug what was happening

**Version 2.0 Improvements:**
- Fixed AudioContext resume issues with proper event listeners
- Switched to MediaPipe Hands for precise tracking
- Added visual indicators (circles) at hand positions
- Particles spawn directly from fingertips
- Added comprehensive debug mode
- Console logging for audio troubleshooting
- Much more responsive and obvious interaction

Key insights:
- Browser audio restrictions require careful handling
- MediaPipe provides much better UX than pixel difference
- Visual feedback is critical for interactive experiences
- Debug mode is essential for understanding behavior
- Web Audio API is powerful but requires careful gain management
- Canvas trail effects create mesmerizing visuals with minimal code
- User experience is greatly enhanced by smooth audio/visual transitions
- Testing with actual hands in frame is critical (not just moving around)
