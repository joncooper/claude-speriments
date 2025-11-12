# Visual Sound Mirror - Architecture Guide

## Overview

Visual Sound Mirror is a gesture-controlled interactive music instrument built as a **monolithic single-file application**. This architectural decision prioritizes:
- ✅ Simplicity: Works everywhere (file://, any server, no build step)
- ✅ Maintainability: One file to debug, no module dependencies
- ✅ Performance: Single HTTP request, no module loading overhead  
- ✅ Reliability: No scope/binding bugs from module boundaries

**File**: `app.js` (4,506 lines, 111 methods)
**Version**: v6.7.0 Hands-Free Edition

## File Organization

The monolithic file is organized into logical sections. Use your editor's "Go to Symbol" feature (`Cmd+Shift+O` / `Ctrl+Shift+O`) to quickly navigate between methods.

### Method Groups by Functionality

**Initialization**
- `constructor()` - Set up all state (lines 6-245)
- `initPads()` - Create 25-pad drum grid
- `initKnobs()` - Virtual rotary controls

**Audio System - Theremin**
- `startTheremin()` - Start continuous oscillator
- `stopTheremin()` - Stop oscillator  
- `updateTheremin()` - Update pitch/filter from hand position
- `quantizeToScale()` - Snap pitch to musical scale
- `midiToFreq()` - MIDI note to frequency conversion

**Audio System - Drums** (25+ synthesized sounds)
- `playDrumSample()` - Route to specific drum type
- `playKick()`, `playSnare()`, `playHihat()`, `playClap()`
- `playTom()`, `playRim()`, `playSnap()`, `playCowbell()`
- `playCrash()`, `playRide()`, `playPerc()`, `playBass()`
- `playFX()`, `playChordPad()`, `playLead()`

**Hand Tracking & Gestures**
- `onHandResults()` - MediaPipe callback, normalizes hand data
- `detectModeGesture()` - Detect 1/2/5 finger holds
- `countExtendedFingers()` - Gesture recognition helper
- `calibratePadsFromHand()` - Auto-position pads to hand geometry
- `detectTwoHandGestures()` - Two-hand chord detection

**Mode System**
- `switchMode()` - Transition between ribbons/theremin/pads
- `updateModeButtons()` - Sync UI state
- `triggerModeSwitchAnimation()` - Celebration effect
- `cycleScale()` - Change musical scale (theremin mode)

**Visualization System** (6 modes)
1. Particle Fountain - Physics-based particles with spatial grid
2. Audio Bloom - Velocity-triggered expanding ripples
3. Fluid Dynamics - Smoke-like tendrils with curl noise
4. Gravitational Orbits - Planetary motion around fingertips
5. Kaleidoscope - 6-fold radial symmetry
6. Temporal Echoes - Ghost images with chromatic aberration

**Rendering**
- `render()` - Master render dispatch
- `renderRibbons()` - Multi-ribbon finger trails
- `renderPads()` - Drum pad grid with tap detection
- `renderTheremin()` - Frequency display and scale guide
- `drawFluidRibbon()` - Individual ribbon with gradients
- `drawTouchingEffect()` - Harmonic chord visualization
- `drawDebugSkeleton()` - Hand landmark overlay

**UI & Debug**
- `setupEventListeners()` - Wire up all UI interactions
- `setupVizDebugListeners()` - Visualization tuning panels
- `populateVizDebugPanel()` - Dynamic HTML generation
- `updateDebug()` - FPS and performance metrics

**Animation Loop**
- `animate()` - Main 60fps game loop
- `updateAudio()` - Audio state management

## Code Navigation Tips

### Editor Features (VS Code / Cursor)
1. **Outline View**: Shows all methods in a tree - click to jump
2. **Breadcrumbs**: Shows current method at top of editor
3. **Go to Symbol**: `Cmd+Shift+O` / `Ctrl+Shift+O` - fuzzy search methods
4. **Find in File**: `Cmd+F` / `Ctrl+F` to search for method names

### Command Line
```bash
# List all methods with line numbers
grep -n "^    [a-zA-Z_].*(" app.js | less

# Find a specific method
grep -n "playDrumSample" app.js

# Jump to line in vim
vim +2000 app.js
```

## Key Design Patterns

### Centralized State
All state lives in the single `VisualSoundMirror` class instance:
```javascript
this.mode = 'ribbons';
this.leftHand = null;
this.audioContext = null;
```

### Mode-Based Behavior
```javascript
render() {
    if (this.mode === 'ribbons') this.renderRibbons();
    else if (this.mode === 'theremin') this.renderTheremin();  
    else if (this.mode === 'pads') this.renderPads();
}
```

### Web Audio Graph
```
AudioContext → MasterGain → FilterNode → Delay/Reverb → Destination
```

## Performance

**Target**: 60fps with hand tracking + audio + particles

**Optimizations Applied**:
- Spatial grid for particle collisions (O(n) instead of O(n²))
- Trail length limiting (25 points max)
- Conditional visualization updates
- Batched canvas draw calls

**Monitor**: Particle count > 5,000 can drop frames

## Testing Checklist

Test after any changes:

- [ ] Ribbons mode renders with finger trails
- [ ] Theremin mode plays pitch/filter control
- [ ] Pads mode triggers drum sounds on tap
- [ ] Gesture switching works (1/2/5 fingers)
- [ ] Mute/debug buttons function
- [ ] No console errors
- [ ] 60fps maintained

## Why Monolithic?

**Benefits**:
- Works with `file://` protocol (no server needed)
- Single file to debug
- No module loading bugs
- Fast: one HTTP request
- Simple deployment

**When to Split**:
- File exceeds 10,000 lines (currently 4,506)
- Multiple developers
- Need code reuse across projects

**Don't Split Because**:
- "It's cleaner" (subjective, adds complexity)
- "Best practice" (depends on context)
- Previous failed refactoring proved monolithic works better

---

**Last Updated**: November 2025  
**License**: MIT
