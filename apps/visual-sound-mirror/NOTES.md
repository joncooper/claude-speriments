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

### Visual System - Flowing Ribbons & Constellations

**Version 4.0 - Ultra-Responsive, Ephemeral Design:**

The visualization now consists of three layered systems:

**1. Ribbon Trails (Primary)**
- Each fingertip maintains its own trail of up to 20 position points
- Trails rendered as smooth Bézier curves using quadraticCurveTo
- Linear gradients from transparent (old) to vibrant (current fingertip)
- Line width increases with motion intensity (3-7px)
- Soft glow effects (shadowBlur 20px)
- Trails clear immediately when finger leaves or hand exits frame

**2. Constellation Lines (Secondary)**
- Drawn between any two fingertips within 120px distance
- Alpha/width based on distance (closer = brighter/thicker)
- Gradient coloring between the two finger colors
- Creates dynamic web/constellation patterns as fingers move
- Only appears when multiple fingers/hands detected

**3. Velocity Particles (Accents)**
- Only spawn when movement speed exceeds threshold
- Size based on velocity (2-10px)
- Very short lifespan (40 frames = ~0.7 seconds)
- Limited to 200 max particles
- Each particle inherits velocity direction from finger
- Quick decay (0.95 friction)

**Fingertip Markers:**
- Glowing dots at each fingertip (4-8px based on intensity)
- Outer pulsing ring (8-14px)
- Each finger gets unique color from palette
- Intensity-based glow (shadowBlur 25-45px)

### Particle System - Swirly Bubbles (DEPRECATED - v3.0)

**Version 3.0 - Organic Bubble Motion:**

Physics-based bubbles with:
- Position, velocity, acceleration
- Swirling/orbital motion around origin point
- Breathing effect (grow/shrink like bubbles)
- Life span with smooth fade in/out
- Color based on motion properties
- Upward floating with wave patterns

Motion characteristics:
- Sine/cosine-based swirling forces
- Orbital attraction back to spawn point
- Slower initial velocities for gentle flow
- Less friction (0.98) for longer trails
- Palm spawns larger bubbles (10-25px)
- Fingertips spawn smaller bubbles (5-15px)

Rendering:
- Canvas 2D with alpha compositing
- Very long trail effects (alpha 0.05)
- Translucent bubble bodies (30% opacity)
- Radial gradient highlights for 3D bubble effect
- Subtle rim outline for definition
- Soft glow (shadowBlur 30px)

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

**Version 3.0 Improvements (Swirly Bubbles):**
- Fixed mirrored X-axis - hand movement now maps naturally
- Transformed from fireworks to swirly, flowing bubbles
- Added breathing/pulsing effect to bubbles
- Implemented orbital motion around spawn points
- Much longer, dreamier trails (reduced alpha to 0.05)
- Translucent bubble rendering with highlights and rims
- Slower, gentler movement for meditative feel
- Bigger, more visible bubbles (5-25px vs 2-7px)

**Version 4.0 Improvements (Flowing Ribbons - MAJOR OVERHAUL):**
- Complete redesign based on user feedback for responsiveness
- **Ribbon trails** - Each fingertip leaves a smooth, flowing trail (max 20 points)
- **Constellation lines** - Lines connect nearby fingers when within 120px
- **Velocity-based particles** - Only spawn when moving fast enough (ephemeral!)
- **Much shorter lifespans** - Particles live only 40 frames (vs 200)
- **Fingertip-focused** - Only track 5 fingertips per hand (not palm)
- **Quick fadeout** - 1 second timer clears screen when no hands detected
- **Performance optimized** - Reduced particle count (200 max vs 1000)
- **Glowing fingertip markers** - Each finger gets a pulsing dot with color
- **Smooth curves** - Using quadraticCurveTo for silky ribbon rendering
- **Used performance.now()** - Better timing for smoother animation
- **Gradient ribbons** - Trails fade from transparent to vibrant

**Version 5.0 Improvements (Silk & Symphony Edition):**
- Left hand controls filter cutoff and resonance via finger spread
- Right hand controls delay/echo amount via finger spread
- Two-hand gesture detection (touching fingertips, pulling apart)
- Multi-ribbon system (3 parallel ribbons per finger)
- Dynamic color theory with 5 curated schemes
- Advanced audio chain: Oscillator → Filter → Delay → Reverb → Master

**Version 6.2 Improvements (Hands-Free Edition - ARCHITECTURAL REDESIGN):**
- **Gesture-based mode switching** - Right hand finger count switches modes (1, 2, or 5 fingers)
- **Global knob controls** - Knobs now work in ALL modes, not just knobs mode
- **Removed knobs mode** - Reduced from 4 modes to 3 (ribbons, theremin, pads)
- **Repositioned knobs** - Smaller knobs in top-left corner, always visible
- **Finger counting algorithm** - Detects extended fingers to recognize gestures
- **2-second cooldown** - Prevents rapid mode switching from hand movements
- **Hands-free interaction** - No keyboard required for normal operation
- **Updated UI** - Removed knobs mode button, updated tooltips with gesture hints
- **Pinch gesture for knobs** - Both thumb AND index must be inside knob radius
- **Improved UX** - Goal achieved: don't touch the keyboard!

**Version 6.2.2 Deliberate Gesture Hold System:**
- **Gesture hold requirement** - Must hold gesture steady for 2.5 seconds to switch modes
- **Stricter finger detection** - Increased thresholds (1.3x for thumb, 0.05 for fingers) for more deliberate gestures
- **Progress indicator** - Circular progress bar around palm shows hold progress
  - Background circle shows target area
  - Green arc fills clockwise as gesture is held
  - Shows gesture name ("1 FINGER", "PEACE", "OPEN HAND") and percentage
- **Celebration animation** - Visual burst effect when mode switches successfully
  - 50 colored particles expanding from center
  - White flash effect
  - Mode name displayed prominently
  - Ascending arpeggio sound (C-E-G-C)
- **Gesture stability tracking** - Resets if finger count changes during hold
- **Non-twitchy behavior** - Eliminates accidental mode switching from hand movements
- **Visual feedback loop** - User always knows if gesture is being recognized

**Version 6.2.1 MediaPipe Handedness & Coordinate System:**
- **MediaPipe labels hands from camera perspective** - User's RIGHT hand = MediaPipe "Left" label
- **Canvas coordinates require mirroring** - Using (1 - x) transformation for proper visual mapping
- **Gesture detection uses MediaPipe "Left"** - Which is user's anatomical RIGHT hand
- **Video feed shows true orientation** - Right hand appears on right side of screen
- **XY mapping mirrors X-axis** - Visual elements appear where user expects (mirror effect for intuitiveness)
- **Key insight**: Camera POV vs user POV requires coordinate mirroring for natural interaction

**Version 6.0 Improvements (Music Synthesis Edition - MAJOR FEATURE UPDATE):**
- **Mode system** - Three distinct interaction modes with seamless switching
- **Scale quantization** - Musical note quantization with 7 scales (Pentatonic, Major, Minor, Blues, Dorian, Phrygian, Chromatic)
- **Theremin mode** - Continuous melodic instrument with scale-quantized pitch
  - X-axis: pitch (quantized to musical scale)
  - Y-axis: filter brightness (200-4000Hz)
  - Finger spread: resonance/vibrato (Q: 1-16)
  - Visual scale guide showing note positions
  - Smooth frequency transitions with exponentialRampToValueAtTime
- **Sample Pads mode** - 4x4 grid of gesture-triggered drum samples
  - 16 synthesized drum sounds (kick, snare, hi-hat, clap, toms, etc.)
  - Real-time synthesis (no audio files)
  - Tap detection with 200ms debounce
  - Visual feedback on trigger
- **Knobs mode** - Virtual rotary controls
  - 4 knobs: Filter, Reverb, Delay, Resonance
  - Angle-based rotation detection
  - Visual arc indicators showing value
  - Real-time parameter application
- **Enhanced UI**
  - Mode switcher buttons with active state highlighting
  - Keyboard shortcuts (1-4 for modes, S for scales)
  - Mode indicator overlay
  - Improved info panel with detailed instructions
- **Audio architecture**
  - MIDI note to frequency conversion
  - Scale quantization algorithm
  - Theremin continuous oscillator system
  - 16 synthesized drum/percussion sounds
  - Parameter mapping for knobs

Key synthesis implementations:
- **Kick**: Frequency sweep from 150Hz to 40Hz with envelope
- **Snare**: Tone (200Hz) + filtered noise
- **Hi-hat**: High-pass filtered noise (7000Hz cutoff)
- **Clap**: Triple-layered noise bursts
- **Toms**: Frequency sweep with octave drop
- **Cowbell**: Dual square waves (540Hz + 800Hz)
- **Crash/Ride**: Long-decay filtered noise
- **Bass/Chords**: Sawtooth waves through lowpass filter

Technical insights:
- Browser audio restrictions require careful handling
- MediaPipe provides much better UX than pixel difference
- Visual feedback is critical for interactive experiences
- Debug mode is essential for understanding behavior
- Web Audio API is powerful but requires careful gain management
- Canvas trail effects create mesmerizing visuals with minimal code
- User experience is greatly enhanced by smooth audio/visual transitions
- Testing with actual hands in frame is critical (not just moving around)
- **Ephemeral is better than persistent** - short lifespans feel more responsive
- **Less is more** - fewer, well-placed effects > many scattered effects
- **Direct coupling** - effects must be obviously tied to hand positions
- **Quick fadeout essential** - blank screen signals "ready for input"
- **Velocity matters** - movement speed should affect visual intensity
- **Performance** - using performance.now() and reducing particle count improves framerate significantly
- **Mode-based architecture** - Clean separation of concerns for different interaction models
- **Quantization is powerful** - Constraining pitch to scales makes everything sound musical
- **Synthesis > Samples** - Real-time synthesis gives more control and smaller file size
- **Gesture vocabulary** - Different gestures for different modes creates intuitive interactions
- **Global controls architecture** - Controls that affect all modes are better than mode-specific ones
- **Hands-free is the goal** - Keyboard shortcuts defeat the purpose of a gesture-controlled instrument
- **Finger counting is reliable** - Using extended finger count for gestures is intuitive and robust
- **Cooldowns prevent chaos** - 2-second cooldown essential to prevent accidental mode switching
