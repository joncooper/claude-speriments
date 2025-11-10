# Visual Sound Mirror - Modular Refactoring Plan

## Status: Phase 1 Complete ✅

### Completed Modules

#### 1. `src/utils/Constants.js` ✅
- Exported MODES, VISUALIZATION_MODES, SCALES
- Exported FINGERTIP_INDICES, DEFAULT_SETTINGS, GESTURE_SETTINGS, DRUM_SAMPLES
- ~50 lines

#### 2. `src/utils/ColorSchemes.js` ✅
- Extracted ColorSchemes class with all color theory logic
- Methods: setScheme(), getFingerColor(), getParticleColor(), getBloomColor()
- ~110 lines

#### 3. `src/core/AudioSystem.js` ✅
- Complete audio synthesis system
- Theremin control, drum synthesis (15+ sounds)
- Effects chain: filter, delay, reverb
- Scale quantization and MIDI utilities
- ~650 lines

#### 4. `src/core/HandTracker.js` ✅
- MediaPipe hand tracking initialization
- Hand data processing and normalization
- Gesture detection (countExtendedFingers)
- Two-hand gesture detection
- Finger trails management
- ~270 lines

### Total Extracted: ~1,080 lines → 4 focused modules

## Phase 2: Integration (NEXT)

### Approach: Incremental Refactoring
Rather than rewriting app.js from scratch (risky!), we'll:
1. Add ES6 module imports at the top
2. Update constructor to instantiate modules
3. Replace inline implementations with module delegation
4. Keep visualization/rendering code inline (can extract later)

### Integration Steps

1. **Update index.html**
   ```html
   <script type="module" src="app.js"></script>
   ```

2. **Add imports to app.js**
   ```javascript
   import { AudioSystem } from './src/core/AudioSystem.js';
   import { HandTracker } from './src/core/HandTracker.js';
   import { ColorSchemes } from './src/utils/ColorSchemes.js';
   import { MODES, DEFAULT_SETTINGS } from './src/utils/Constants.js';
   ```

3. **Constructor changes**
   ```javascript
   // Replace inline audio setup
   this.audioSystem = new AudioSystem();

   // Replace inline hand tracking
   this.handTracker = new HandTracker(this.video, this.canvas);

   // Replace inline color schemes
   this.colorSchemes = new ColorSchemes();
   ```

4. **Method delegation**
   - `initAudio()` → `this.audioSystem.init()`
   - `initHandTracking()` → `this.handTracker.init()`
   - `playDrumSample()` → `this.audioSystem.playDrumSample()`
   - `startTheremin()` → `this.audioSystem.startTheremin()`
   - `updateTheremin()` → `this.audioSystem.updateTheremin(hand, canvas)`
   - Color methods → `this.colorSchemes.getFingerColor()` etc.

### Benefits Achieved
- ✅ **~1000 lines extracted** from monolithic app.js
- ✅ **Clear separation of concerns**
- ✅ **Reusable modules** (AudioSystem can be used standalone)
- ✅ **Easier testing** (each module can be tested independently)
- ✅ **Better maintainability** (audio bugs → check AudioSystem.js)
- ✅ **Incremental approach** (low risk, fully functional)

## Phase 3: Further Modularization (FUTURE)

### Potential Modules (if desired)
- `src/modes/RibbonsMode.js` - Ribbons rendering (~200 lines)
- `src/modes/ThereminMode.js` - Theremin rendering (~100 lines)
- `src/modes/PadsMode.js` - Pads system, calibration, tap detection (~800 lines)
- `src/ui/Knobs.js` - Virtual knobs system (~150 lines)
- `src/ui/DebugPanels.js` - Debug UI controls (~400 lines)
- `src/visualizations/*` - 6 visualization modes (~2000 lines)

### Would reduce app.js from 4450 → ~600 lines (orchestrator only)

## File Structure

```
apps/visual-sound-mirror/
├── app.js                    # Main orchestrator (will be reduced)
├── app.js.backup             # Original monolith (safety)
├── index.html
├── styles.css
├── REFACTORING_PLAN.md       # This file
└── src/
    ├── core/
    │   ├── AudioSystem.js    # ✅ Complete
    │   └── HandTracker.js    # ✅ Complete
    └── utils/
        ├── Constants.js      # ✅ Complete
        └── ColorSchemes.js   # ✅ Complete
```

## Next Steps
1. Update index.html to use `type="module"`
2. Integrate modules into app.js
3. Test thoroughly
4. Commit modular refactoring
5. (Optional) Extract visualization/mode modules
