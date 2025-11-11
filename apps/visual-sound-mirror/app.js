// Visual Sound Mirror - v6.9.0 Modular Edition
// Interactive music instrument with gesture-controlled mode switching and global audio controls
// Now with modular architecture for better maintainability

import { AudioSystem } from './src/core/AudioSystem.js';
import { HandTracker } from './src/core/HandTracker.js';
import { ColorSchemes } from './src/utils/ColorSchemes.js';
import { Knobs } from './src/ui/Knobs.js';
import { PadsMode } from './src/modes/PadsMode.js';
import { RibbonsMode } from './src/modes/RibbonsMode.js';
import { ThereminMode } from './src/modes/ThereminMode.js';
import { ParticleFountain } from './src/visualizations/ParticleFountain.js';
import { AudioBloom } from './src/visualizations/AudioBloom.js';
import { FluidDynamics } from './src/visualizations/FluidDynamics.js';
import { GravitationalOrbits } from './src/visualizations/GravitationalOrbits.js';
import { Kaleidoscope } from './src/visualizations/Kaleidoscope.js';
import { TemporalEchoes } from './src/visualizations/TemporalEchoes.js';
import { DebugPanels } from './src/ui/DebugPanels.js';
import { RenderHelpers } from './src/ui/RenderHelpers.js';
import { MODES, DEFAULT_SETTINGS, GESTURE_SETTINGS, SCALES } from './src/utils/Constants.js';


class VisualSoundMirror {
    constructor() {
        // Canvas setup
        this.canvas = document.getElementById('canvas');
        this.ctx = this.canvas.getContext('2d');
        this.resizeCanvas();

        // Video setup
        this.video = document.getElementById('video');

        // === MODULAR SYSTEMS ===
        // Initialize core modules
        this.audioSystem = new AudioSystem();
        this.colorSystem = new ColorSchemes(); // Renamed to avoid conflict with inline colorSchemes map
        // HandTracker will be initialized after video is ready
        this.handTracker = null;

        // Hand tracking
        this.hands = null;
        this.handResults = null;
        this.camera = null;
        this.gestureDetectionEnabled = false; // Default to OFF

        // Hand data (will be populated by handTracker)
        this.leftHand = null;   // { landmarks, fingertips, palm, fingerSpread }
        this.rightHand = null;  // { landmarks, fingertips, palm, fingerSpread }
        this.prevLeftHand = null;
        this.prevRightHand = null;

        // Mode system
        this.mode = 'ribbons'; // 'ribbons', 'theremin', 'pads'
        this.modes = ['ribbons', 'theremin', 'pads'];

        // Gesture-based mode switching
        this.gestureHoldStartTime = 0;
        this.currentGestureFingerCount = null;
        this.gestureHoldRequired = 2500; // 2.5 seconds
        this.gestureInProgress = false;
        this.lastModeSwitch = 0;

        // Mode switch animation
        this.modeSwitchAnimation = {
            active: false,
            startTime: 0,
            duration: 1000
        };

        // Scale system for theremin mode
        this.scales = {
            chromatic: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            major: [0, 2, 4, 5, 7, 9, 11],
            minor: [0, 2, 3, 5, 7, 8, 10],
            pentatonic: [0, 2, 4, 7, 9],
            blues: [0, 3, 5, 6, 7, 10],
            dorian: [0, 2, 3, 5, 7, 9, 10],
            phrygian: [0, 1, 3, 5, 7, 8, 10]
        };
        this.currentScale = 'pentatonic';
        this.rootNote = 60; // Middle C (MIDI note number)

        // Fingertip trails - multi-ribbon per finger
        this.fingerTrails = {};
        this.maxTrailLength = 25;

        // Audio setup
        this.audioContext = null;
        this.masterGain = null;
        this.filterNode = null;
        this.delayNode = null;
        this.delayGain = null;
        this.audioEnabled = false;
        this.isMuted = false;
        this.lastSoundTime = 0;

        // Theremin mode audio
        this.thereminOsc = null;
        this.thereminGain = null;
        this.thereminFilter = null;
        this.thereminActive = false;

        // === MODE MODULES ===
        this.padsMode = new PadsMode(this.canvas);
        this.padsMode.init();
        this.ribbonsMode = new RibbonsMode(this.canvas, this.ctx);
        this.thereminMode = new ThereminMode(this.canvas, this.ctx);

        // Backwards compatibility references
        this.pads = this.padsMode.getPads();
        this.padCalibration = this.padsMode.getCalibration();
        this.padSettings = this.padsMode.padSettings;

        // Virtual knobs (delegated to Knobs module)
        this.knobsSystem = new Knobs(this.canvas);
        this.knobs = this.knobsSystem.getKnobs(); // Backwards compatibility
        this.activeKnob = null;

        // Debug mode
        this.debugMode = false;
        this.debugPanelVisible = false;

        // === VISUALIZATION MODULES ===
        this.visualizationMode = 1; // 1-6 for different visual effects
        this.vizDebugVisible = false;

        // Initialize visualization modules
        this.particleViz = new ParticleFountain(this.canvas, this.ctx);
        this.bloomViz = new AudioBloom(this.canvas, this.ctx);
        this.fluidViz = new FluidDynamics(this.canvas, this.ctx);
        this.orbitViz = new GravitationalOrbits(this.canvas, this.ctx);
        this.kaleidoscopeViz = new Kaleidoscope(this.canvas, this.ctx);
        this.echoViz = new TemporalEchoes(this.canvas, this.ctx);

        // Backwards compatibility references for settings access
        this.particles = this.particleViz.particles;
        this.particleSettings = this.particleViz.settings;
        this.blooms = this.bloomViz.blooms;
        this.bloomSettings = this.bloomViz.settings;
        this.fluidSettings = this.fluidViz.settings;
        this.orbitSettings = this.orbitViz.settings;
        this.kaleidoscopeSettings = this.kaleidoscopeViz.settings;
        this.handHistory = this.echoViz.handHistory;
        this.echoSettings = this.echoViz.settings;

        // Initialize UI helper modules
        this.debugPanels = new DebugPanels(this);
        this.renderHelpers = new RenderHelpers(this);

        // No hands timer
        this.noHandsTime = 0;
        this.fadeoutStarted = false;

        // Color palette - dynamic and intentional
        this.time = 0;
        this.colorPhase = 0;
        this.baseHue = 220; // Start with blue

        // Color palettes based on color theory
        this.colorSchemes = {
            aurora: { base: 220, type: 'analogous' },    // Blues to greens
            sunset: { base: 30, type: 'analogous' },     // Oranges to purples
            ocean: { base: 200, type: 'monochromatic' }, // Deep blues
            forest: { base: 140, type: 'analogous' },    // Greens
            cosmic: { base: 280, type: 'triadic' }       // Purples, oranges, greens
        };
        this.currentScheme = 'aurora';

        // Two-hand gesture detection
        this.handsDistance = 0;
        this.handsAreTouching = false;
        this.touchingFingers = [];

        // Settings
        this.settings = {
            trailAlpha: 0.12,
            soundInterval: 70,
            minVelocityForSound: 1,
            ribbonWidth: 2.5,
            ribbonOffsets: 3, // Number of parallel ribbons per finger
            ribbonSpacing: 8  // Spacing between parallel ribbons
        };

        // Animation
        this.lastTime = 0;
        this.isRunning = false;

        this.setupEventListeners();
    }

    initPads() {
        // Delegate to PadsMode module
        this.padsMode.init();
        // Update backwards compatibility references
        this.pads = this.padsMode.getPads();
        this.padCalibration = this.padsMode.getCalibration();
    }


    getPadColor(type) {
        // Delegate to PadsMode module
        return this.padsMode.getPadColor(type);
    }

    resizeCanvas() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    setupEventListeners() {
        window.addEventListener('resize', () => {
            this.resizeCanvas();
            // Reinit pads and knobs on resize
            if (this.pads.length > 0) {
                this.pads = [];
                this.initPads();
            }
        });

        this.canvas.addEventListener('click', (e) => {
            if (this.audioContext && this.audioContext.state === 'suspended') {
                this.audioContext.resume();
            }
            this.playChord(e.clientX, e.clientY);
        });

        // Keyboard controls
        document.addEventListener('keydown', (e) => {
            // Don't handle keys if typing in an input field
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') {
                return;
            }

            // Visualization modes (1-6)
            if (e.key >= '1' && e.key <= '6') {
                e.preventDefault();
                const newMode = parseInt(e.key);
                this.visualizationMode = newMode;
                console.log(`[KEYBOARD] Switched to Visualization Mode ${newMode}`);

                // Reset state when switching modes
                if (newMode === 1) {
                    this.particles = [];
                } else if (newMode === 2) {
                    this.blooms = [];
                } else if (newMode === 6) {
                    this.handHistory = [];
                }

                // Update debug panel to show controls for this mode (delegated to DebugPanels)
                this.debugPanels.populate();
            }

            // Toggle visualization debug panel
            if (e.key === 'v' || e.key === 'V') {
                e.preventDefault();
                this.vizDebugVisible = !this.vizDebugVisible;
                document.getElementById('vizDebugPanel').classList.toggle('hidden');
                console.log(`[KEYBOARD] Viz debug panel: ${this.vizDebugVisible ? 'OPEN' : 'CLOSED'}`);
            }

            // Toggle pad debug panel
            if (e.key === 'p' || e.key === 'P') {
                e.preventDefault();
                this.debugPanelVisible = !this.debugPanelVisible;
                document.getElementById('padDebugPanel').classList.toggle('hidden');
                console.log(`[KEYBOARD] Pad debug panel: ${this.debugPanelVisible ? 'OPEN' : 'CLOSED'}`);
            }

            // Scale cycling
            if (e.key === 's') {
                e.preventDefault();
                this.cycleScale();
            }
        });

        document.getElementById('startButton').addEventListener('click', () => {
            this.start();
        });

        document.getElementById('gestureButton').addEventListener('click', () => {
            this.toggleGestureDetection();
        });

        document.getElementById('muteButton').addEventListener('click', () => {
            this.toggleMute();
        });

        document.getElementById('debugButton').addEventListener('click', () => {
            this.debugMode = !this.debugMode;
            document.getElementById('debug').classList.toggle('hidden');
        });

        document.getElementById('infoButton').addEventListener('click', () => {
            document.getElementById('info').classList.remove('hidden');
        });

        document.getElementById('closeInfo').addEventListener('click', () => {
            document.getElementById('info').classList.add('hidden');
        });

        // Mode switcher buttons
        document.querySelectorAll('.mode-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const mode = btn.getAttribute('data-mode');
                this.switchMode(mode);
                this.updateModeButtons();
            });
        });

        // Pad Debug Panel Controls
        document.getElementById('tapAlgorithm').addEventListener('change', (e) => {
            this.padSettings.tapAlgorithm = e.target.value;
            console.log(`Tap algorithm: ${e.target.value}`);
        });

        document.getElementById('padSize').addEventListener('input', (e) => {
            this.padSettings.basePadSize = parseFloat(e.target.value);
            document.getElementById('padSizeValue').textContent = e.target.value;
        });

        document.getElementById('spacing').addEventListener('input', (e) => {
            this.padSettings.spacingMultiplier = parseFloat(e.target.value);
            document.getElementById('spacingValue').textContent = e.target.value;
        });

        document.getElementById('zThreshold').addEventListener('input', (e) => {
            this.padSettings.zThreshold = parseFloat(e.target.value);
            document.getElementById('zThresholdValue').textContent = e.target.value;
        });

        document.getElementById('dwellTime').addEventListener('input', (e) => {
            this.padSettings.dwellTime = parseInt(e.target.value);
            document.getElementById('dwellTimeValue').textContent = e.target.value;
        });

        document.getElementById('wiggle').addEventListener('input', (e) => {
            this.padSettings.wiggleThreshold = parseFloat(e.target.value);
            document.getElementById('wiggleValue').textContent = e.target.value;
        });

        document.getElementById('retreat').addEventListener('input', (e) => {
            this.padSettings.retreatThreshold = parseFloat(e.target.value);
            document.getElementById('retreatValue').textContent = e.target.value;
        });

        document.getElementById('retriggerDelay').addEventListener('input', (e) => {
            this.padSettings.retriggerDelay = parseInt(e.target.value);
            document.getElementById('retriggerDelayValue').textContent = e.target.value;
        });

        document.getElementById('resetPads').addEventListener('click', () => {
            // Reset to defaults
            this.padSettings.basePadSize = 70;
            this.padSettings.spacingMultiplier = 0.8;
            this.padSettings.tapAlgorithm = 'z-velocity';
            this.padSettings.zThreshold = 0.02;
            this.padSettings.dwellTime = 200;
            this.padSettings.wiggleThreshold = 10;
            this.padSettings.retreatThreshold = 0.02;
            this.padSettings.retriggerDelay = 100;

            // Update UI
            document.getElementById('tapAlgorithm').value = 'z-velocity';
            document.getElementById('padSize').value = '70';
            document.getElementById('padSizeValue').textContent = '70';
            document.getElementById('spacing').value = '0.8';
            document.getElementById('spacingValue').textContent = '0.8';
            document.getElementById('zThreshold').value = '0.02';
            document.getElementById('zThresholdValue').textContent = '0.02';
            document.getElementById('dwellTime').value = '200';
            document.getElementById('dwellTimeValue').textContent = '200';
            document.getElementById('wiggle').value = '10';
            document.getElementById('wiggleValue').textContent = '10';
            document.getElementById('retreat').value = '0.02';
            document.getElementById('retreatValue').textContent = '0.02';
            document.getElementById('retriggerDelay').value = '100';
            document.getElementById('retriggerDelayValue').textContent = '100';

            // Reinit pads if in pads mode
            if (this.mode === 'pads') {
                this.initPads();
            }

            console.log('Reset pad settings to defaults');
        });

        document.getElementById('recalibrate').addEventListener('click', () => {
            if (this.leftHand && this.leftHand.fingertips.length === 5) {
                this.calibratePadsFromHand(this.leftHand);
                this.initPads();
                console.log('Recalibrated pads');
            } else {
                console.log('Cannot recalibrate: need to detect left hand with 5 fingers');
            }
        });

        // Visualization Debug Panel Controls handled by DebugPanels module
    }

    // setupVizDebugListeners() and resetVizSettings() have been removed
    // This functionality is now handled by DebugPanels module

    // === DEBUG PANEL METHODS ===
    // All debug panel generation methods (populateVizDebugPanel, get*Controls, attach*Listeners)
    // have been moved to src/ui/DebugPanels.js and are accessed via this.debugPanels.populate()


    resetCurrentModeSettings() {
        if (this.visualizationMode === 1) {
            // Reset Particle Fountain settings
            this.particleSettings = {
                emissionRate: 30,
                lifetime: 4000,
                initialVelocity: 0.3,
                gravity: 0.1,
                drag: 0.995,
                attraction: 0,
                repulsion: 0.5,
                turbulence: 0.5,
                particleSizeMin: 1,
                particleSizeMax: 4,
                colorMode: 'velocity',
                blendMode: 'normal',
                alpha: 0.8,
                glow: true,
                trails: false,
                audioReactive: true
            };
        } else if (this.visualizationMode === 2) {
            this.bloomSettings = {
                velocityThreshold: 5,
                bloomInterval: 100,
                lifetime: 2000,
                maxRadius: 300,
                ringCount: 3,
                ringSpacing: 30,
                pulseSpeed: 1.0,
                glowIntensity: 20,
                colorShift: true
            };
        } else if (this.visualizationMode === 3) {
            this.fluidSettings = {
                tendrilCount: 8,
                tendrilRadius: 25,
                flowSpeed: 0.002,
                pulseAmount: 10,
                gradientSize: 40,
                opacity: 0.5,
                trailPersistence: 0.92,
                velocityInfluence: 2.0
            };
        } else if (this.visualizationMode === 4) {
            this.orbitSettings = {
                orbiterCount: 8,
                orbitRadius: 45,
                orbitSpeed: 0.003,
                orbiterSize: 5,
                sunSize: 14,
                trailLength: 0.15,
                wobble: 5,
                glowIntensity: 18
            };
        } else if (this.visualizationMode === 5) {
            this.kaleidoscopeSettings = {
                symmetryCount: 6,
                fingerSize: 18,
                lineOpacity: 0.4,
                rotationSpeed: 0,
                trailPersistence: 0.85,
                glowIntensity: 25,
                pulseWithAudio: false,
                showCenter: true
            };
        } else if (this.visualizationMode === 6) {
            this.echoSettings = {
                trailLength: 30,
                fadeSpeed: 0.03,
                chromaticAberration: 3,
                motionBlur: true,
                glowIntensity: 15,
                echoSpacing: 2,
                showPalm: true,
                showFingers: true,
                fingerSize: 12,
                palmSize: 20
            };
        }
        this.debugPanels.populate();  // Delegated to DebugPanels
        console.log(`Reset mode ${this.visualizationMode} settings to defaults`);
    }

    updateModeButtons() {
        document.querySelectorAll('.mode-btn').forEach(btn => {
            const mode = btn.getAttribute('data-mode');
            if (mode === this.mode) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
    }

    switchMode(newMode) {
        this.mode = newMode;
        console.log(`Switched to ${newMode} mode`);

        // Stop theremin when leaving theremin mode
        if (newMode !== 'theremin') {
            this.stopTheremin();
        }

        // Calibrate pads from hand geometry when entering pads mode
        if (newMode === 'pads' && this.leftHand && this.leftHand.fingertips.length === 5) {
            this.calibratePadsFromHand(this.leftHand);
            this.initPads(); // Reinitialize pads with calibration
        }

        // Show status
        const status = document.getElementById('status');
        status.textContent = `Mode: ${newMode.toUpperCase()}`;
        status.classList.add('visible');
        setTimeout(() => status.classList.remove('visible'), 2000);
    }

    calibratePadsFromHand(hand) {
        // Delegate to PadsMode module
        this.padsMode.calibrateFromHand(hand);
        // Update backwards compatibility reference
        this.padCalibration = this.padsMode.getCalibration();
    }

    triggerModeSwitchAnimation() {
        this.modeSwitchAnimation.active = true;
        this.modeSwitchAnimation.startTime = Date.now();

        // Play a celebratory sound
        if (this.audioContext && this.audioEnabled) {
            this.playModeSwitchSound();
        }
    }

    playModeSwitchSound() {
        const now = this.audioContext.currentTime;

        // Ascending arpeggio
        const notes = [262, 330, 392, 523]; // C, E, G, high C
        notes.forEach((freq, i) => {
            const osc = this.audioContext.createOscillator();
            const gain = this.audioContext.createGain();

            osc.type = 'sine';
            osc.frequency.value = freq;

            const startTime = now + (i * 0.08);
            gain.gain.setValueAtTime(0.2, startTime);
            gain.gain.exponentialRampToValueAtTime(0.01, startTime + 0.2);

            osc.connect(gain);
            gain.connect(this.masterGain);

            osc.start(startTime);
            osc.stop(startTime + 0.2);
        });
    }

    cycleScale() {
        const scaleNames = Object.keys(this.scales);
        const currentIndex = scaleNames.indexOf(this.currentScale);
        const nextIndex = (currentIndex + 1) % scaleNames.length;
        this.currentScale = scaleNames[nextIndex];

        console.log(`Scale: ${this.currentScale}`);
        const status = document.getElementById('status');
        status.textContent = `Scale: ${this.currentScale.toUpperCase()}`;
        status.classList.add('visible');
        setTimeout(() => status.classList.remove('visible'), 1500);
    }

    // Detect hand gesture for mode switching (requires deliberate hold)
    detectModeGesture() {
        const now = Date.now();

        // Use LEFT hand for mode gestures (which is user's right hand - MediaPipe labels from camera POV)
        if (!this.leftHand || !this.leftHand.landmarks) {
            // Hand not detected - reset gesture tracking
            this.currentGestureFingerCount = null;
            this.gestureHoldStartTime = 0;
            this.gestureInProgress = false;
            return;
        }

        // Count extended fingers with stricter detection
        const extendedFingers = this.countExtendedFingers(this.leftHand.landmarks);

        // Map finger count to mode (only specific counts)
        let targetMode = null;
        if (extendedFingers === 1) {
            targetMode = 'ribbons';  // One finger = ribbons
        } else if (extendedFingers === 2) {
            targetMode = 'theremin'; // Two fingers (peace sign) = theremin
        } else if (extendedFingers === 5) {
            targetMode = 'pads';     // Open hand (5 fingers) = pads
        }

        // If no valid gesture detected, reset
        if (!targetMode) {
            this.currentGestureFingerCount = null;
            this.gestureHoldStartTime = 0;
            this.gestureInProgress = false;
            return;
        }

        // If already in this mode, don't do anything
        if (targetMode === this.mode) {
            this.currentGestureFingerCount = null;
            this.gestureHoldStartTime = 0;
            this.gestureInProgress = false;
            return;
        }

        // Check if gesture changed (user changed finger count)
        if (this.currentGestureFingerCount !== extendedFingers) {
            // New gesture started - reset timer
            this.currentGestureFingerCount = extendedFingers;
            this.gestureHoldStartTime = now;
            this.gestureInProgress = true;
            return;
        }

        // Same gesture is being held - check if held long enough
        const holdDuration = now - this.gestureHoldStartTime;

        if (holdDuration >= this.gestureHoldRequired) {
            // Gesture held long enough - switch mode!
            this.switchMode(targetMode);
            this.triggerModeSwitchAnimation();

            // Reset gesture tracking
            this.currentGestureFingerCount = null;
            this.gestureHoldStartTime = 0;
            this.gestureInProgress = false;
            this.lastModeSwitch = now;
        }
    }

    // Count extended fingers on a hand (stricter detection for deliberate gestures)
    countExtendedFingers(landmarks) {
        // Check each finger individually with VERY strict requirements
        const wrist = landmarks[0];

        // Thumb: check if tip is significantly further from wrist than knuckle
        const thumbTip = landmarks[4];
        const thumbKnuckle = landmarks[2];
        const thumbTipDist = Math.hypot(thumbTip.x - wrist.x, thumbTip.y - wrist.y);
        const thumbKnuckleDist = Math.hypot(thumbKnuckle.x - wrist.x, thumbKnuckle.y - wrist.y);
        const thumbExtended = thumbTipDist > thumbKnuckleDist * 1.4; // Even stricter: 1.4

        // Index finger
        const indexTip = landmarks[8];
        const indexPip = landmarks[6];
        const indexMcp = landmarks[5]; // Knuckle
        const indexExtended = indexTip.y < indexPip.y - 0.06 && indexTip.y < indexMcp.y - 0.08;

        // Middle finger
        const middleTip = landmarks[12];
        const middlePip = landmarks[10];
        const middleMcp = landmarks[9];
        const middleExtended = middleTip.y < middlePip.y - 0.06 && middleTip.y < middleMcp.y - 0.08;

        // Ring finger - check it's CURLED when should be down
        const ringTip = landmarks[16];
        const ringPip = landmarks[14];
        const ringMcp = landmarks[13];
        const ringExtended = ringTip.y < ringPip.y - 0.06 && ringTip.y < ringMcp.y - 0.08;
        const ringCurled = ringTip.y > ringPip.y; // Tip below PIP = curled

        // Pinky - check it's CURLED when should be down
        const pinkyTip = landmarks[20];
        const pinkyPip = landmarks[18];
        const pinkyMcp = landmarks[17];
        const pinkyExtended = pinkyTip.y < pinkyPip.y - 0.06 && pinkyTip.y < pinkyMcp.y - 0.08;
        const pinkyCurled = pinkyTip.y > pinkyPip.y;

        // STRICT GESTURE DETECTION:
        // 1 finger = ONLY index extended, others must be actively curled
        if (indexExtended && !middleExtended && !ringExtended && !pinkyExtended &&
            !thumbExtended && ringCurled && pinkyCurled) {
            return 1;
        }

        // 2 fingers (peace sign) = ONLY index + middle extended, others actively curled
        if (indexExtended && middleExtended && !ringExtended && !pinkyExtended &&
            !thumbExtended && ringCurled && pinkyCurled) {
            return 2;
        }

        // 5 fingers = all fingers extended
        if (thumbExtended && indexExtended && middleExtended && ringExtended && pinkyExtended) {
            return 5;
        }

        // Any other combination = 0 (no recognized gesture)
        return 0;
    }

    // Convert MIDI note number to frequency
    midiToFreq(midiNote) {
        return 440 * Math.pow(2, (midiNote - 69) / 12);
    }

    // Quantize position to nearest note in scale
    quantizeToScale(normalizedX) {
        const scale = this.scales[this.currentScale];
        const octaveRange = 3; // 3 octaves
        const totalNotes = octaveRange * 12;

        // Map X position to MIDI note range
        const rawMidiNote = this.rootNote - 12 + (normalizedX * totalNotes);

        // Find nearest note in scale
        const octave = Math.floor((rawMidiNote - this.rootNote) / 12);
        const semitone = Math.round(rawMidiNote - this.rootNote - (octave * 12));

        // Find closest scale degree
        let closestDegree = scale[0];
        let minDist = Math.abs(semitone - scale[0]);

        for (const degree of scale) {
            const dist = Math.abs(semitone - degree);
            if (dist < minDist) {
                minDist = dist;
                closestDegree = degree;
            }
        }

        const quantizedMidi = this.rootNote + (octave * 12) + closestDegree;
        return this.midiToFreq(quantizedMidi);
    }

    async start() {
        try {
            document.getElementById('overlay').classList.add('hidden');

            const status = document.getElementById('status');
            status.textContent = 'Initializing audio...';
            status.classList.add('visible');

            await this.initAudio();

            status.textContent = 'Starting camera...';
            await this.initCamera();

            status.textContent = 'Loading hand tracking...';
            await this.initHandTracking();

            status.textContent = 'Ready! Wave your hands!';
            setTimeout(() => status.classList.remove('visible'), 3000);

            // Initialize mode buttons
            this.updateModeButtons();

            this.isRunning = true;
            this.animate(performance.now());

        } catch (error) {
            console.error('Error starting:', error);
            alert('Could not initialize. Please grant permissions and try again.\n\nError: ' + error.message);
        }
    }

    async initCamera() {
        const stream = await navigator.mediaDevices.getUserMedia({
            video: {
                width: { ideal: 640 },
                height: { ideal: 480 }
            },
            audio: false
        });

        this.video.srcObject = stream;

        return new Promise((resolve) => {
            this.video.onloadedmetadata = () => {
                resolve();
            };
        });
    }

    async initAudio() {
        // Use modular AudioSystem
        await this.audioSystem.init();

        // Keep references for backwards compatibility
        this.audioContext = this.audioSystem.audioContext;
        this.masterGain = this.audioSystem.masterGain;
        this.filterNode = this.audioSystem.filterNode;
        this.delayNode = this.audioSystem.delayNode;
        this.delayGain = this.audioSystem.delayGain;
        this.reverb = this.audioSystem.reverb;
        this.audioEnabled = this.audioSystem.audioEnabled;
        this.isMuted = this.audioSystem.isMuted;
    }

    // === AUDIO SYSTEM DELEGATION ===
    // Theremin mode audio control (delegated to AudioSystem)
    startTheremin() {
        this.audioSystem.startTheremin();
        this.thereminActive = this.audioSystem.thereminActive;
    }

    stopTheremin() {
        this.audioSystem.stopTheremin();
        // Update state after async operation completes
        setTimeout(() => {
            this.thereminActive = this.audioSystem.thereminActive;
        }, 300);
    }

    updateTheremin(hand) {
        this.audioSystem.updateTheremin(hand, this.canvas);
    }

    // Drum synthesis for sample pads (delegated to AudioSystem)
    playDrumSample(type) {
        this.audioSystem.playDrumSample(type);
    }

    // === DEPRECATED: All drum synthesis methods moved to AudioSystem ===
    // playKick, playSnare, playHihat, playClap, playTom, playRim, playSnap,
    // playCowbell, playCrash, playRide, playPerc, playBass, playFX, playChordPad, playLead
    // All now handled by AudioSystem module

    // Scale cycling (delegated to AudioSystem)
    cycleScale() {
        this.currentScale = this.audioSystem.cycleScale();
        return this.currentScale;
    }

    // Helper methods still used by non-audio code
    midiToFreq(midiNote) {
        return this.audioSystem.midiToFreq(midiNote);
    }

    quantizeToScale(normalizedX) {
        return this.audioSystem.quantizeToScale(normalizedX);
    }

    // === HAND TRACKING DELEGATION ===
    async initHandTracking() {
        // Initialize HandTracker module
        this.handTracker = new HandTracker(this.video, this.canvas);
        await this.handTracker.init();

        // Keep references for backwards compatibility
        this.hands = this.handTracker.hands;
        this.camera = this.handTracker.camera;
    }

    onHandResults(results) {
        // Delegate to HandTracker
        this.handTracker.processResults(results);
        this.handTracker.updateTime(this.time);

        // Update local hand references for backwards compatibility
        const hands = this.handTracker.getHands();
        this.leftHand = hands.left;
        this.rightHand = hands.right;
        this.prevLeftHand = hands.prevLeft;
        this.prevRightHand = hands.prevRight;

        // Update trail and gesture references
        this.fingerTrails = this.handTracker.getFingerTrails();
        this.touchingFingers = this.handTracker.getTouchingFingers();
        this.handsAreTouching = this.handTracker.isHandsAreTouching();

        // Update state
        this.noHandsTime = this.handTracker.noHandsTime;
        this.fadeoutStarted = this.handTracker.fadeoutStarted;
        this.handResults = this.handTracker.handResults;

        this.updateDebug();
    }

    detectTwoHandGestures() {
        // Delegated to HandTracker (called automatically in processResults)
        // This method kept for backwards compatibility
    }

    countExtendedFingers(landmarks) {
        return this.handTracker.countExtendedFingers(landmarks);
    }

    // === REMOVED: ~400 lines of drum synthesis methods ===
    // All drum methods (playKick, playSnare, etc.) moved to AudioSystem.js


    getVisualizationModeName(mode) {
        const modeNames = {
            1: 'Particle Fountain',
            2: 'Audio Bloom Pulses',
            3: 'Fluid Dynamics',
            4: 'Gravitational Orbits',
            5: 'Kaleidoscope Symmetry',
            6: 'Temporal Echoes'
        };
        return modeNames[mode] || 'Unknown';
    }

    updateDebug() {
        // Always update viz debug panel (independent of main debug mode)
        if (this.vizDebugVisible) {
            const modeName = this.getVisualizationModeName(this.visualizationMode);
            const modeElement = document.getElementById('currentVizMode');
            if (modeElement) {
                modeElement.textContent = this.visualizationMode;
            }
            // Update the mode indicator text
            const modeIndicator = document.querySelector('.viz-mode-indicator');
            if (modeIndicator) {
                modeIndicator.innerHTML = `Mode <span id="currentVizMode">${this.visualizationMode}</span>: ${modeName} | Press 1-6 to switch modes`;
            }

            // Update mode-specific counters (only if they exist)
            const particleCountEl = document.getElementById('particleCount');
            if (particleCountEl) {
                particleCountEl.textContent = this.particles.length;
            }
            const bloomCountEl = document.getElementById('bloomCount');
            if (bloomCountEl) {
                bloomCountEl.textContent = this.blooms.length;
            }
        }

        // Main debug panel only when debug mode is on
        if (!this.debugMode) return;

        const leftSpread = this.leftHand ? this.leftHand.fingerSpread.toFixed(0) : 'N/A';
        const rightSpread = this.rightHand ? this.rightHand.fingerSpread.toFixed(0) : 'N/A';

        document.getElementById('debugMotion').textContent =
            `L: ${leftSpread}px, R: ${rightSpread}px`;
        document.getElementById('debugPosition').textContent =
            `Hands touching: ${this.handsAreTouching ? 'YES' : 'NO'}`;
        document.getElementById('debugParticles').textContent =
            `${this.particles.length} | Viz Mode: ${this.visualizationMode}`;
        document.getElementById('debugAudio').textContent =
            this.audioContext ? `${this.audioContext.state} (${this.isMuted ? 'muted' : 'active'})` : 'Not initialized';
        document.getElementById('debugHands').textContent =
            (this.leftHand ? 1 : 0) + (this.rightHand ? 1 : 0);
    }

    getColorForFinger(fingerIndex, handedness, t = 0) {
        // Dynamic color based on color theory
        const scheme = this.colorSchemes[this.currentScheme];
        let hue = (this.baseHue + t * 20) % 360;

        if (scheme.type === 'analogous') {
            // Spread across 60 degrees
            hue += (fingerIndex * 12) - 24;
        } else if (scheme.type === 'triadic') {
            // 120 degree separation
            hue += fingerIndex * 24;
        } else if (scheme.type === 'monochromatic') {
            // Same hue, vary saturation/lightness
            hue += fingerIndex * 5;
        }

        // Left hand slightly cooler, right hand slightly warmer
        if (handedness === 'Left') {
            hue -= 10;
        } else {
            hue += 10;
        }

        hue = hue % 360;
        const saturation = 70 + Math.sin(t * 0.5) * 15;
        const lightness = 55 + Math.sin(t * 0.3 + fingerIndex) * 10;

        return this.hslToRgb(hue, saturation, lightness);
    }

    hslToRgb(h, s, l) {
        s /= 100;
        l /= 100;
        const k = n => (n + h / 30) % 12;
        const a = s * Math.min(l, 1 - l);
        const f = n => l - a * Math.max(-1, Math.min(k(n) - 3, Math.min(9 - k(n), 1)));
        return {
            r: Math.round(255 * f(0)),
            g: Math.round(255 * f(8)),
            b: Math.round(255 * f(4))
        };
    }

    updateAudio() {
        if (!this.audioEnabled || this.isMuted || !this.audioContext) {
            return;
        }

        if (this.audioContext.state === 'suspended') {
            this.audioContext.resume();
        }

        const now = this.audioContext.currentTime;

        // Global knob controls - always active in all modes
        this.detectKnobInteractions();
        this.applyKnobParameters();

        // Mode-specific audio behavior
        if (this.mode === 'theremin') {
            // Theremin mode: continuous tone controlled by hand position
            if (this.leftHand || this.rightHand) {
                const activeHand = this.leftHand || this.rightHand;

                if (!this.thereminActive) {
                    this.startTheremin();
                }

                this.updateTheremin(activeHand);
            } else {
                // Stop theremin when no hands detected
                if (this.thereminActive) {
                    this.stopTheremin();
                }
            }
        } else if (this.mode === 'pads') {
            // Pads mode: detect fingertip taps on sample pads
            this.detectPadInteractions();
        } else {
            // Ribbons mode: original behavior

            // Left hand controls filter cutoff and resonance
            if (this.leftHand) {
                // Map finger spread (50-250px) to filter frequency (300-3000Hz)
                const spread = Math.max(50, Math.min(250, this.leftHand.fingerSpread));
                const filterFreq = 300 + ((spread - 50) / 200) * 2700;
                const resonance = 1 + ((spread - 50) / 200) * 8; // Q: 1-9

                this.filterNode.frequency.linearRampToValueAtTime(filterFreq, now + 0.1);
                this.filterNode.Q.linearRampToValueAtTime(resonance, now + 0.1);
            }

            // Right hand controls delay amount
            if (this.rightHand) {
                // Map finger spread to delay mix (0-0.6)
                const spread = Math.max(50, Math.min(250, this.rightHand.fingerSpread));
                const delayMix = ((spread - 50) / 200) * 0.6;

                this.delayGain.gain.linearRampToValueAtTime(delayMix, now + 0.1);
            }

            // Play sounds based on hand movements
            const nowMs = Date.now();
            if (nowMs - this.lastSoundTime > this.settings.soundInterval) {
                // Left hand sounds
                if (this.leftHand && this.prevLeftHand) {
                    this.playHandSounds(this.leftHand, this.prevLeftHand, 0);
                }

                // Right hand sounds (slightly different timbre)
                if (this.rightHand && this.prevRightHand) {
                    this.playHandSounds(this.rightHand, this.prevRightHand, 50);
                }

                // Special sound when hands are touching
                if (this.handsAreTouching && this.touchingFingers.length > 0) {
                    this.playTouchingSound();
                }

                this.lastSoundTime = nowMs;
            }
        }
    }

    detectPadInteractions() {
        // Delegate to PadsMode module, passing audio callback
        const leftHand = this.leftHand;
        this.padsMode.detect(leftHand, (drumType) => {
            this.playDrumSample(drumType);
        });
        // Update backwards compatibility reference
        this.pads = this.padsMode.getPads();
    }

    // === KNOBS DELEGATION ===
    detectKnobInteractions() {
        this.knobsSystem.detect(this.leftHand, this.rightHand);
        this.activeKnob = this.knobsSystem.activeKnob;
    }

    applyKnobParameters() {
        this.knobsSystem.apply(this.audioContext, this.filterNode, this.delayGain);
    }

    drawKnobs() {
        this.knobsSystem.render(this.ctx);
    }

    render() {
        // Gentle clearing
        if (this.fadeoutStarted || (!this.leftHand && !this.rightHand)) {
            this.ctx.fillStyle = 'rgba(0, 0, 0, 0.25)';
        } else {
            this.ctx.fillStyle = `rgba(0, 0, 0, ${this.settings.trailAlpha})`;
        }
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Update color phase
        this.baseHue = (this.baseHue + 0.1) % 360;

        // VISUALIZATION SYSTEM - Delegate to visualization modules
        if (this.visualizationMode === 1) {
            // Particle Fountain
            this.particleViz.update(this.leftHand, this.rightHand, this.prevLeftHand, this.prevRightHand, this.time);
            this.particleViz.render(this.baseHue, this.time, this.knobs);
            this.particles = this.particleViz.particles; // Sync backwards compatibility
        } else if (this.visualizationMode === 2) {
            // Audio Bloom Pulses
            this.bloomViz.update(this.leftHand, this.rightHand, this.prevLeftHand, this.prevRightHand, this.baseHue);
            this.bloomViz.render();
            this.blooms = this.bloomViz.blooms; // Sync backwards compatibility
        } else if (this.visualizationMode === 3) {
            // Fluid Dynamics
            this.fluidViz.render(this.leftHand, this.rightHand, this.prevLeftHand, this.prevRightHand, this.baseHue, this.time);
        } else if (this.visualizationMode === 4) {
            // Gravitational Orbits
            this.orbitViz.render(this.leftHand, this.rightHand, this.baseHue, this.time);
        } else if (this.visualizationMode === 5) {
            // Kaleidoscope
            this.kaleidoscopeViz.render(this.leftHand, this.rightHand, this.baseHue, this.time, this.audioContext);
        } else if (this.visualizationMode === 6) {
            // Temporal Echoes
            this.echoViz.update(this.leftHand, this.rightHand);
            this.echoViz.render(this.baseHue);
            this.handHistory = this.echoViz.handHistory; // Sync backwards compatibility
        }

        // Mode-specific rendering
        if (this.mode === 'theremin') {
            this.renderThereminMode();
        } else if (this.mode === 'pads') {
            this.renderPadsMode();
        } else {
            // Ribbons mode: original visualization
            this.renderRibbonsMode();
        }

        // Always draw knobs (global controls in all modes)
        this.drawKnobs();

        // Draw mode indicator (delegated to RenderHelpers)
        this.renderHelpers.drawModeIndicator();

        // Draw gesture hold progress indicator (delegated to RenderHelpers)
        if (this.gestureInProgress && this.gestureHoldStartTime > 0) {
            this.renderHelpers.drawGestureHoldProgress();
        }

        // Draw mode switch animation (celebated to RenderHelpers)
        if (this.modeSwitchAnimation.active) {
            this.renderHelpers.drawModeSwitchAnimation();
        }

        // Debug overlay (delegated to RenderHelpers)
        if (this.debugMode && this.handResults && this.handResults.multiHandLandmarks) {
            this.renderHelpers.drawDebugSkeleton();
        }
    }

    renderRibbonsMode() {
        // Delegate to RibbonsMode module
        const ribbonSettings = {
            ribbonOffsets: 2,
            ribbonWidth: 3,
            ribbonSpacing: 8
        };
        this.ribbonsMode.render(
            this.leftHand,
            this.rightHand,
            this.fingerTrails,
            this.touchingFingers,
            ribbonSettings,
            (fingerIndex, handedness, t) => this.getColorForFinger(fingerIndex, handedness, t)
        );
    }

    renderThereminMode() {
        // Delegate to ThereminMode module
        const hand = this.leftHand || this.rightHand;
        if (!hand) return;

        this.thereminMode.render(hand, this.audioSystem);

        // Draw scale name at bottom
        this.ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
        this.ctx.font = '18px monospace';
        this.ctx.textAlign = 'left';
        this.ctx.fillText(`Scale: ${this.currentScale.toUpperCase()}`, 20, this.canvas.height - 40);
    }

    renderPadsMode() {
        // Delegate to PadsMode module
        this.padsMode.render(this.ctx, this.leftHand);
    }

    // === RENDER HELPER METHODS ===
    // All render helper methods (drawModeIndicator, drawGestureHoldProgress, drawModeSwitchAnimation,
    // drawFluidRibbon, drawTouchingEffect, drawFingertipMarkers, drawDebugSkeleton) have been moved
    // to src/ui/RenderHelpers.js and are accessed via this.renderHelpers.*

    animate(timestamp) {
        if (!this.isRunning) return;

        const deltaTime = timestamp - this.lastTime;
        this.lastTime = timestamp;
        this.time += deltaTime;

        // Detect hand gestures for mode switching (only if gesture detection is enabled)
        if (this.gestureDetectionEnabled) {
            this.detectModeGesture();
        }

        this.updateAudio();
        this.render();

        // Always update debug (handles both main debug and viz debug panels)
        this.updateDebug();

        requestAnimationFrame((t) => this.animate(t));
    }

    toggleMute() {
        // Delegate to AudioSystem
        this.isMuted = this.audioSystem.toggleMute();

        // Update UI
        const button = document.getElementById('muteButton');
        button.textContent = this.isMuted ? '🔇' : '🔊';
    }

    toggleGestureDetection() {
        this.gestureDetectionEnabled = !this.gestureDetectionEnabled;
        const button = document.getElementById('gestureButton');

        if (this.gestureDetectionEnabled) {
            button.classList.remove('inactive');
            button.title = 'Gesture Detection ON (Click to disable)';
        } else {
            button.classList.add('inactive');
            button.title = 'Gesture Detection OFF (Click to enable)';
        }
    }
}

// Initialize when page loads
window.addEventListener('load', () => {
    const app = new VisualSoundMirror();
});
