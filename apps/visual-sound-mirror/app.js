// Visual Sound Mirror - v6.7.0 Hands-Free Edition
// Interactive music instrument with gesture-controlled mode switching and global audio controls
// No keyboard required - switch modes with hand gestures (1, 2, or 5 fingers)

class VisualSoundMirror {
    constructor() {
        // Canvas setup
        this.canvas = document.getElementById('canvas');
        this.ctx = this.canvas.getContext('2d');
        this.resizeCanvas();

        // Video setup
        this.video = document.getElementById('video');

        // Hand tracking
        this.hands = null;
        this.handResults = null;
        this.camera = null;
        this.gestureDetectionEnabled = false; // Default to OFF

        // Hand data
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

        // Sample pads
        this.padGrid = { rows: 4, cols: 4 };
        this.pads = [];
        this.padCalibration = {
            calibrated: false,
            fingertipPositions: [],
            fingertipDistances: [],
            handCenter: null,
            scale: 1.0
        };

        // Pad tuning parameters (adjustable via debug UI)
        this.padSettings = {
            basePadSize: 70,           // Base pad size in pixels (40-120)
            spacingMultiplier: 0.8,    // Spacing between pads (0.5-2.0)
            tapAlgorithm: 'z-velocity', // 'z-velocity', 'dwell-retreat', 'wiggle', 'hybrid'
            zThreshold: 0.02,          // Z-axis movement threshold (0.005-0.1) - MORE SENSITIVE
            dwellTime: 200,            // Time to hover before tap counts (100-500ms)
            wiggleThreshold: 10,       // XY wiggle distance in pixels (5-30)
            retreatThreshold: 0.02,    // Z-axis retreat speed (0.01-0.05)
            retriggerDelay: 100        // Cooldown between re-triggers in ms (50-300) - FAST for drums!
        };

        this.initPads();

        // Virtual knobs
        this.knobs = [];
        this.initKnobs();
        this.activeKnob = null;

        // Debug mode
        this.debugMode = false;
        this.debugPanelVisible = false;

        // VISUALIZATION SYSTEM
        this.visualizationMode = 1; // 1-6 for different visual effects
        this.vizDebugVisible = false;

        // Particle System (#1)
        this.particles = [];
        this.maxParticles = 150000;  // Increased for massive particle clouds
        this.lastParticleEmitTime = 0;
        this.particleSettings = {
            emissionRate: 30,          // Particles per finger per SECOND (10-500)
            lifetime: 4000,            // Milliseconds (500-8000)
            initialVelocity: 0.3,      // Speed multiplier (0.01-2.0)
            gravity: 0.08,             // Downward acceleration (0-0.5)
            drag: 0.995,               // Air resistance (0.9-0.999)
            attraction: 0.0,           // Inter-particle attraction (-0.5 to 0.5)
            repulsion: 0.0,            // Inter-particle repulsion (0-2)
            turbulence: 0.3,           // Curl noise strength (0-2)
            particleSizeMin: 0.5,      // Min particle size (0.5-5)
            particleSizeMax: 2.5,      // Max particle size (1-10)
            colorMode: 'velocity',     // 'velocity', 'lifetime', 'audio', 'rainbow'
            blendMode: 'normal',       // 'normal', 'additive', 'screen', 'multiply'
            alpha: 0.8,                // Base alpha/opacity (0.1-1.0)
            glow: true,                // Glow effect
            trails: false,             // Particle trails
            audioReactive: true        // React to audio
        };

        // Audio Bloom Pulses System (#2)
        this.blooms = [];
        this.lastBloomTime = 0;
        this.bloomSettings = {
            velocityThreshold: 5,      // Min velocity to trigger bloom (1-20)
            bloomInterval: 100,        // Min ms between blooms (50-500)
            lifetime: 2000,            // Bloom lifetime in ms (500-5000)
            maxRadius: 300,            // Max expansion radius (100-500)
            ringCount: 3,              // Number of concentric rings (1-8)
            ringSpacing: 30,           // Space between rings (10-60)
            pulseSpeed: 1.0,           // Animation speed multiplier (0.5-3.0)
            glowIntensity: 20,         // Glow blur amount (0-40)
            colorShift: true           // Shift color over lifetime
        };

        // Fluid Dynamics System (#3)
        this.fluidSettings = {
            tendrilCount: 8,           // Tendrils per fingertip (3-15)
            tendrilRadius: 25,         // Distance from center (10-60)
            flowSpeed: 0.002,          // Rotation speed (0.0005-0.01)
            pulseAmount: 10,           // Radius pulsing (0-30)
            gradientSize: 40,          // Gradient radius (20-80)
            opacity: 0.5,              // Base opacity (0.2-0.8)
            trailPersistence: 0.92,    // How long trails last (0.8-0.98)
            velocityInfluence: 2.0     // How much movement affects flow (0-5)
        };

        // Gravitational Orbits System (#4)
        this.orbitSettings = {
            orbiterCount: 8,           // Particles per fingertip (4-20)
            orbitRadius: 45,           // Orbit distance (20-100)
            orbitSpeed: 0.003,         // Rotation speed (0.001-0.01)
            orbiterSize: 5,            // Particle size (2-12)
            sunSize: 14,               // Central sun size (8-30)
            trailLength: 0.15,         // Orbital trail length (0-0.5)
            wobble: 5,                 // Orbit wobble amount (0-20)
            glowIntensity: 18          // Glow blur (0-40)
        };

        // Kaleidoscope Symmetry System (#5)
        this.kaleidoscopeSettings = {
            symmetryCount: 6,          // Fold count (3-12)
            fingerSize: 18,            // Reflected finger size (8-40)
            lineOpacity: 0.4,          // Line to center opacity (0-1)
            rotationSpeed: 0,          // Auto-rotation (0-0.01)
            trailPersistence: 0.85,    // Trail fade (0.7-0.95)
            glowIntensity: 25,         // Glow blur (0-50)
            pulseWithAudio: false,     // React to audio
            showCenter: true           // Show center point
        };

        // Temporal Echoes System (#6)
        this.handHistory = [];
        this.maxHistoryLength = 60; // Store up to 60 frames of history
        this.echoSettings = {
            trailLength: 30,           // Number of echoes to show (5-60)
            fadeSpeed: 0.03,           // How fast echoes fade (0.01-0.1)
            chromaticAberration: 3,    // RGB separation in pixels (0-10)
            motionBlur: true,          // Connect echoes with lines
            glowIntensity: 15,         // Glow blur amount (0-30)
            echoSpacing: 2,            // Frames between echoes (1-5)
            showPalm: true,            // Show palm echoes
            showFingers: true,         // Show finger echoes
            fingerSize: 12,            // Echo finger size (6-24)
            palmSize: 20               // Echo palm size (10-40)
        };

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
        // Arc-based layout - 5 arcs (one per finger), 5 pads per arc
        // Positioned based on actual hand geometry if calibrated
        const padsPerFinger = 5;

        // Define sounds for each finger's arc (5 fingers × 5 pads = 25 sounds)
        const fingerSounds = [
            // Thumb (0): Bass and low tones
            ['kick', 'bass1', 'bass2', 'bass3', 'subkick'],
            // Index (1): Snares and mid percussion
            ['snare', 'rimshot', 'clap', 'snap', 'sidestick'],
            // Middle (2): Hi-hats and cymbals
            ['hihat', 'hihat_open', 'crash', 'ride', 'splash'],
            // Ring (3): Toms and melodic percussion
            ['tom1', 'tom2', 'tom3', 'conga', 'bongo'],
            // Pinky (4): Synths and effects
            ['chord1', 'chord2', 'lead', 'fx1', 'fx2']
        ];

        this.pads = [];

        if (this.padCalibration.calibrated && this.padCalibration.fingertipPositions.length === 5) {
            // Use calibrated hand geometry
            console.log('Using calibrated pad layout');
            const scale = this.padCalibration.scale;
            const padSize = Math.max(40, Math.min(120, this.padSettings.basePadSize * scale));
            // Make pads adjacent: spacing = padSize * multiplier
            const padSpacing = padSize * this.padSettings.spacingMultiplier;

            for (let finger = 0; finger < 5; finger++) {
                const fingertip = this.padCalibration.fingertipPositions[finger];
                const handCenter = this.padCalibration.handCenter;

                // Calculate direction from hand center to fingertip
                const dx = fingertip.x - handCenter.x;
                const dy = fingertip.y - handCenter.y;
                const angle = Math.atan2(dy, dx);

                // Place pads along a line extending from fingertip away from hand center
                for (let padIdx = 0; padIdx < padsPerFinger; padIdx++) {
                    const distance = padSpacing * (padIdx + 1); // Adjacent pads starting from fingertip
                    const x = fingertip.x + Math.cos(angle) * distance;
                    const y = fingertip.y + Math.sin(angle) * distance;

                    // Clamp to screen bounds
                    const clampedX = Math.max(padSize / 2, Math.min(this.canvas.width - padSize / 2, x));
                    const clampedY = Math.max(padSize / 2, Math.min(this.canvas.height - padSize / 2, y));

                    this.pads.push({
                        x: clampedX - padSize / 2,
                        y: clampedY - padSize / 2,
                        size: padSize,
                        centerX: clampedX,
                        centerY: clampedY,
                        type: fingerSounds[finger][padIdx],
                        fingerIndex: finger,
                        triggered: false,
                        triggerTime: 0,
                        lastZ: null,
                        dwellStartTime: null,  // For dwell-retreat algorithm
                        lastXY: null,          // For wiggle detection
                        color: this.getPadColor(fingerSounds[finger][padIdx])
                    });
                }
            }
        } else {
            // Use default static layout (fallback)
            console.log('Using default pad layout (not calibrated)');
            const centerX = this.canvas.width / 2;
            const centerY = this.canvas.height * 0.7;
            const arcRadius = 200;
            const padSize = 50;

            for (let finger = 0; finger < 5; finger++) {
                const baseAngle = -Math.PI / 2;
                const angleSpread = Math.PI * 0.6;
                const startAngle = baseAngle - angleSpread / 2 + (finger * angleSpread / 4);

                for (let padIdx = 0; padIdx < padsPerFinger; padIdx++) {
                    const angle = startAngle + (padIdx / (padsPerFinger - 1)) * (angleSpread / 5);
                    const radius = arcRadius + (finger * 35);
                    const distance = radius - (padIdx * 30);

                    const x = centerX + Math.cos(angle) * distance;
                    const y = centerY + Math.sin(angle) * distance;

                    this.pads.push({
                        x: x - padSize / 2,
                        y: y - padSize / 2,
                        size: padSize,
                        centerX: x,
                        centerY: y,
                        type: fingerSounds[finger][padIdx],
                        fingerIndex: finger,
                        triggered: false,
                        triggerTime: 0,
                        lastZ: null,
                        color: this.getPadColor(fingerSounds[finger][padIdx])
                    });
                }
            }
        }
    }

    initKnobs() {
        // Smaller knobs positioned in top-right corner
        const knobRadius = 40; // Smaller for global control overlay
        const padding = 20;
        const spacing = 100;

        // Position in top-right, leaving room for video feed
        const startX = padding + knobRadius;
        const startY = padding + knobRadius;

        this.knobs = [
            { x: startX, y: startY, radius: knobRadius, value: 0.5, label: 'Filter', param: 'filter', angle: 0 },
            { x: startX + spacing, y: startY, radius: knobRadius, value: 0.3, label: 'Reverb', param: 'reverb', angle: 0 },
            { x: startX + spacing * 2, y: startY, radius: knobRadius, value: 0.4, label: 'Delay', param: 'delay', angle: 0 },
            { x: startX + spacing * 3, y: startY, radius: knobRadius, value: 0.7, label: 'Res', param: 'resonance', angle: 0 }
        ];
    }

    getPadColor(type) {
        const colors = {
            // Thumb - Bass (reds/oranges)
            kick: { r: 255, g: 60, b: 60 },
            bass1: { r: 200, g: 40, b: 40 },
            bass2: { r: 180, g: 60, b: 40 },
            bass3: { r: 160, g: 80, b: 60 },
            subkick: { r: 120, g: 40, b: 40 },

            // Index - Snares (blues)
            snare: { r: 60, g: 150, b: 255 },
            rimshot: { r: 80, g: 180, b: 255 },
            clap: { r: 100, g: 200, b: 255 },
            snap: { r: 120, g: 220, b: 255 },
            sidestick: { r: 60, g: 120, b: 200 },

            // Middle - Hi-hats/Cymbals (yellows/whites)
            hihat: { r: 200, g: 200, b: 60 },
            hihat_open: { r: 220, g: 220, b: 100 },
            crash: { r: 240, g: 240, b: 240 },
            ride: { r: 200, g: 200, b: 200 },
            splash: { r: 255, g: 255, b: 150 },

            // Ring - Toms (purples)
            tom1: { r: 180, g: 80, b: 200 },
            tom2: { r: 160, g: 100, b: 220 },
            tom3: { r: 140, g: 120, b: 240 },
            conga: { r: 200, g: 100, b: 180 },
            bongo: { r: 220, g: 120, b: 200 },

            // Pinky - Synths (greens/teals)
            chord1: { r: 100, g: 200, b: 100 },
            chord2: { r: 80, g: 220, b: 120 },
            lead: { r: 100, g: 255, b: 150 },
            fx1: { r: 60, g: 200, b: 200 },
            fx2: { r: 80, g: 180, b: 220 }
        };
        return colors[type] || { r: 150, g: 150, b: 150 };
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

                // Update debug panel to show controls for this mode
                this.populateVizDebugPanel();
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

        // Visualization Debug Panel Controls
        this.setupVizDebugListeners();
    }

    setupVizDebugListeners() {
        // Emission Rate
        document.getElementById('emissionRate').addEventListener('input', (e) => {
            this.particleSettings.emissionRate = parseFloat(e.target.value);
            document.getElementById('emissionRateValue').textContent = e.target.value;
        });

        // Lifetime
        document.getElementById('lifetime').addEventListener('input', (e) => {
            this.particleSettings.lifetime = parseInt(e.target.value);
            document.getElementById('lifetimeValue').textContent = e.target.value;
        });

        // Initial Velocity
        document.getElementById('initialVelocity').addEventListener('input', (e) => {
            this.particleSettings.initialVelocity = parseFloat(e.target.value);
            document.getElementById('initialVelocityValue').textContent = e.target.value;
        });

        // Gravity
        document.getElementById('gravity').addEventListener('input', (e) => {
            this.particleSettings.gravity = parseFloat(e.target.value);
            document.getElementById('gravityValue').textContent = e.target.value;
        });

        // Drag
        document.getElementById('drag').addEventListener('input', (e) => {
            this.particleSettings.drag = parseFloat(e.target.value);
            document.getElementById('dragValue').textContent = e.target.value;
        });

        // Attraction
        document.getElementById('attraction').addEventListener('input', (e) => {
            this.particleSettings.attraction = parseFloat(e.target.value);
            document.getElementById('attractionValue').textContent = e.target.value;
        });

        // Repulsion
        document.getElementById('repulsion').addEventListener('input', (e) => {
            this.particleSettings.repulsion = parseFloat(e.target.value);
            document.getElementById('repulsionValue').textContent = e.target.value;
        });

        // Turbulence
        document.getElementById('turbulence').addEventListener('input', (e) => {
            this.particleSettings.turbulence = parseFloat(e.target.value);
            document.getElementById('turbulenceValue').textContent = e.target.value;
        });

        // Particle Size Min
        document.getElementById('particleSizeMin').addEventListener('input', (e) => {
            this.particleSettings.particleSizeMin = parseFloat(e.target.value);
            document.getElementById('particleSizeMinValue').textContent = e.target.value;
        });

        // Particle Size Max
        document.getElementById('particleSizeMax').addEventListener('input', (e) => {
            this.particleSettings.particleSizeMax = parseFloat(e.target.value);
            document.getElementById('particleSizeMaxValue').textContent = e.target.value;
        });

        // Color Mode
        document.getElementById('colorMode').addEventListener('change', (e) => {
            this.particleSettings.colorMode = e.target.value;
            console.log(`Color mode: ${e.target.value}`);
        });

        // Glow
        document.getElementById('glow').addEventListener('change', (e) => {
            this.particleSettings.glow = e.target.checked;
        });

        // Trails
        document.getElementById('trails').addEventListener('change', (e) => {
            this.particleSettings.trails = e.target.checked;
        });

        // Audio Reactive
        document.getElementById('audioReactive').addEventListener('change', (e) => {
            this.particleSettings.audioReactive = e.target.checked;
        });

        // Clear Particles
        document.getElementById('clearParticles').addEventListener('click', () => {
            this.particles = [];
            console.log('Cleared all particles');
        });

        // Reset Viz Settings
        document.getElementById('resetViz').addEventListener('click', () => {
            this.resetVizSettings();
        });
    }

    resetVizSettings() {
        // Reset to defaults
        this.particleSettings = {
            emissionRate: 30,
            lifetime: 4000,
            initialVelocity: 0.3,
            gravity: 0.08,
            drag: 0.995,
            attraction: 0.0,
            repulsion: 0.0,
            turbulence: 0.3,
            particleSizeMin: 0.5,
            particleSizeMax: 2.5,
            colorMode: 'velocity',
            blendMode: 'normal',
            alpha: 0.8,
            glow: true,
            trails: false,
            audioReactive: true
        };

        // Update UI
        document.getElementById('emissionRate').value = '30';
        document.getElementById('emissionRateValue').textContent = '30';
        document.getElementById('lifetime').value = '4000';
        document.getElementById('lifetimeValue').textContent = '4000';
        document.getElementById('initialVelocity').value = '0.3';
        document.getElementById('initialVelocityValue').textContent = '0.3';
        document.getElementById('gravity').value = '0.08';
        document.getElementById('gravityValue').textContent = '0.08';
        document.getElementById('drag').value = '0.995';
        document.getElementById('dragValue').textContent = '0.995';
        document.getElementById('attraction').value = '0.0';
        document.getElementById('attractionValue').textContent = '0.0';
        document.getElementById('repulsion').value = '0.0';
        document.getElementById('repulsionValue').textContent = '0.0';
        document.getElementById('turbulence').value = '0.3';
        document.getElementById('turbulenceValue').textContent = '0.3';
        document.getElementById('particleSizeMin').value = '0.5';
        document.getElementById('particleSizeMinValue').textContent = '0.5';
        document.getElementById('particleSizeMax').value = '2.5';
        document.getElementById('particleSizeMaxValue').textContent = '2.5';
        document.getElementById('colorMode').value = 'velocity';
        document.getElementById('blendMode').value = 'normal';
        document.getElementById('alpha').value = '0.8';
        document.getElementById('alphaValue').textContent = '0.8';
        document.getElementById('glow').checked = true;
        document.getElementById('trails').checked = false;
        document.getElementById('audioReactive').checked = true;

        console.log('Reset visualization settings to defaults');
    }

    populateVizDebugPanel() {
        // Dynamically populate viz debug panel based on current visualization mode
        const container = document.querySelector('.viz-debug-content');
        if (!container) return;

        // Build HTML based on mode
        let html = `
            <h3>Visualization Tuning (Press 'V' to toggle)</h3>
            <p class="viz-mode-indicator">Mode <span id="currentVizMode">${this.visualizationMode}</span>: ${this.getVisualizationModeName(this.visualizationMode)} | Press 1-6 to switch modes</p>
        `;

        // Mode-specific controls
        if (this.visualizationMode === 1) {
            // Particle Fountain
            html += this.getParticleControls();
        } else if (this.visualizationMode === 2) {
            // Audio Bloom Pulses
            html += this.getBloomControls();
        } else if (this.visualizationMode === 3) {
            // Fluid Dynamics
            html += this.getFluidControls();
        } else if (this.visualizationMode === 4) {
            // Gravitational Orbits
            html += this.getOrbitControls();
        } else if (this.visualizationMode === 5) {
            // Kaleidoscope Symmetry
            html += this.getKaleidoscopeControls();
        } else if (this.visualizationMode === 6) {
            // Temporal Echoes
            html += this.getEchoControls();
        }

        container.innerHTML = html;

        // Attach event listeners for the new controls
        this.attachVizDebugListeners();
    }

    getParticleControls() {
        const s = this.particleSettings;
        return `
            <div class="control-group">
                <label>Emission Rate: <span id="emissionRateValue">${s.emissionRate}</span>/sec</label>
                <input type="range" id="emissionRate" min="10" max="500" value="${s.emissionRate}" step="10">
            </div>
            <div class="control-group">
                <label>Lifetime: <span id="lifetimeValue">${s.lifetime}</span>ms</label>
                <input type="range" id="lifetime" min="500" max="8000" value="${s.lifetime}" step="100">
            </div>
            <div class="control-group">
                <label>Initial Velocity: <span id="initialVelocityValue">${s.initialVelocity}</span>x</label>
                <input type="range" id="initialVelocity" min="0.01" max="2.0" value="${s.initialVelocity}" step="0.01">
            </div>
            <div class="control-group">
                <label>Gravity: <span id="gravityValue">${s.gravity}</span></label>
                <input type="range" id="gravity" min="0" max="0.5" value="${s.gravity}" step="0.01">
            </div>
            <div class="control-group">
                <label>Drag: <span id="dragValue">${s.drag}</span></label>
                <input type="range" id="drag" min="0.9" max="0.999" value="${s.drag}" step="0.001">
            </div>
            <div class="control-group">
                <label>Attraction: <span id="attractionValue">${s.attraction}</span></label>
                <input type="range" id="attraction" min="-0.5" max="0.5" value="${s.attraction}" step="0.05">
            </div>
            <div class="control-group">
                <label>Repulsion: <span id="repulsionValue">${s.repulsion}</span></label>
                <input type="range" id="repulsion" min="0" max="2" value="${s.repulsion}" step="0.1">
            </div>
            <div class="control-group">
                <label>Turbulence: <span id="turbulenceValue">${s.turbulence}</span></label>
                <input type="range" id="turbulence" min="0" max="2" value="${s.turbulence}" step="0.1">
            </div>
            <div class="control-group">
                <label>Size Min: <span id="particleSizeMinValue">${s.particleSizeMin}</span>px</label>
                <input type="range" id="particleSizeMin" min="0.5" max="5" value="${s.particleSizeMin}" step="0.1">
            </div>
            <div class="control-group">
                <label>Size Max: <span id="particleSizeMaxValue">${s.particleSizeMax}</span>px</label>
                <input type="range" id="particleSizeMax" min="1" max="10" value="${s.particleSizeMax}" step="0.1">
            </div>
            <div class="control-group">
                <label>Color Mode:</label>
                <select id="colorMode">
                    <option value="velocity" ${s.colorMode === 'velocity' ? 'selected' : ''}>Velocity</option>
                    <option value="lifetime" ${s.colorMode === 'lifetime' ? 'selected' : ''}>Lifetime</option>
                    <option value="audio" ${s.colorMode === 'audio' ? 'selected' : ''}>Audio Reactive</option>
                    <option value="rainbow" ${s.colorMode === 'rainbow' ? 'selected' : ''}>Rainbow</option>
                </select>
            </div>
            <div class="control-group">
                <label>Blend Mode:</label>
                <select id="blendMode">
                    <option value="normal" ${s.blendMode === 'normal' ? 'selected' : ''}>Normal</option>
                    <option value="additive" ${s.blendMode === 'additive' ? 'selected' : ''}>Additive (Energy)</option>
                    <option value="screen" ${s.blendMode === 'screen' ? 'selected' : ''}>Screen (Soft)</option>
                    <option value="multiply" ${s.blendMode === 'multiply' ? 'selected' : ''}>Multiply (Dark)</option>
                </select>
            </div>
            <div class="control-group">
                <label>Alpha/Opacity: <span id="alphaValue">${s.alpha}</span></label>
                <input type="range" id="alpha" min="0.05" max="1.0" value="${s.alpha}" step="0.05">
            </div>
            <div class="control-group checkbox-group">
                <label><input type="checkbox" id="glow" ${s.glow ? 'checked' : ''}> Glow Effect</label>
                <label><input type="checkbox" id="trails" ${s.trails ? 'checked' : ''}> Particle Trails</label>
                <label><input type="checkbox" id="audioReactive" ${s.audioReactive ? 'checked' : ''}> Audio Reactive</label>
            </div>
            <div class="control-group">
                <p>Particles: <span id="particleCount">${this.particles.length}</span> / 150,000</p>
            </div>
            <button id="clearParticles">Clear All Particles</button>
            <button id="resetViz">Reset to Defaults</button>
        `;
    }

    getBloomControls() {
        const s = this.bloomSettings;
        return `
            <div class="control-group">
                <label>Velocity Threshold: <span id="bloomVelocityValue">${s.velocityThreshold}</span></label>
                <input type="range" id="bloomVelocity" min="1" max="20" value="${s.velocityThreshold}" step="0.5">
            </div>
            <div class="control-group">
                <label>Bloom Interval: <span id="bloomIntervalValue">${s.bloomInterval}</span>ms</label>
                <input type="range" id="bloomInterval" min="50" max="500" value="${s.bloomInterval}" step="10">
            </div>
            <div class="control-group">
                <label>Lifetime: <span id="bloomLifetimeValue">${s.lifetime}</span>ms</label>
                <input type="range" id="bloomLifetime" min="500" max="5000" value="${s.lifetime}" step="100">
            </div>
            <div class="control-group">
                <label>Max Radius: <span id="bloomRadiusValue">${s.maxRadius}</span>px</label>
                <input type="range" id="bloomRadius" min="100" max="500" value="${s.maxRadius}" step="10">
            </div>
            <div class="control-group">
                <label>Ring Count: <span id="bloomRingsValue">${s.ringCount}</span></label>
                <input type="range" id="bloomRings" min="1" max="8" value="${s.ringCount}" step="1">
            </div>
            <div class="control-group">
                <label>Ring Spacing: <span id="bloomSpacingValue">${s.ringSpacing}</span>px</label>
                <input type="range" id="bloomSpacing" min="10" max="60" value="${s.ringSpacing}" step="5">
            </div>
            <div class="control-group">
                <label>Pulse Speed: <span id="bloomSpeedValue">${s.pulseSpeed}</span>x</label>
                <input type="range" id="bloomSpeed" min="0.5" max="3.0" value="${s.pulseSpeed}" step="0.1">
            </div>
            <div class="control-group">
                <label>Glow Intensity: <span id="bloomGlowValue">${s.glowIntensity}</span></label>
                <input type="range" id="bloomGlow" min="0" max="40" value="${s.glowIntensity}" step="2">
            </div>
            <div class="control-group checkbox-group">
                <label><input type="checkbox" id="bloomColorShift" ${s.colorShift ? 'checked' : ''}> Color Shift</label>
            </div>
            <div class="control-group">
                <p>Active Blooms: <span id="bloomCount">${this.blooms.length}</span></p>
            </div>
            <button id="clearBlooms">Clear All Blooms</button>
            <button id="resetViz">Reset to Defaults</button>
        `;
    }

    getFluidControls() {
        const s = this.fluidSettings;
        return `
            <div class="control-group">
                <label>Tendril Count: <span id="fluidTendrilsValue">${s.tendrilCount}</span></label>
                <input type="range" id="fluidTendrils" min="3" max="15" value="${s.tendrilCount}" step="1">
            </div>
            <div class="control-group">
                <label>Tendril Radius: <span id="fluidRadiusValue">${s.tendrilRadius}</span>px</label>
                <input type="range" id="fluidRadius" min="10" max="60" value="${s.tendrilRadius}" step="5">
            </div>
            <div class="control-group">
                <label>Flow Speed: <span id="fluidSpeedValue">${s.flowSpeed}</span></label>
                <input type="range" id="fluidSpeed" min="0.0005" max="0.01" value="${s.flowSpeed}" step="0.0005">
            </div>
            <div class="control-group">
                <label>Pulse Amount: <span id="fluidPulseValue">${s.pulseAmount}</span>px</label>
                <input type="range" id="fluidPulse" min="0" max="30" value="${s.pulseAmount}" step="2">
            </div>
            <div class="control-group">
                <label>Gradient Size: <span id="fluidGradientValue">${s.gradientSize}</span>px</label>
                <input type="range" id="fluidGradient" min="20" max="80" value="${s.gradientSize}" step="5">
            </div>
            <div class="control-group">
                <label>Opacity: <span id="fluidOpacityValue">${s.opacity}</span></label>
                <input type="range" id="fluidOpacity" min="0.2" max="0.8" value="${s.opacity}" step="0.05">
            </div>
            <div class="control-group">
                <label>Trail Persistence: <span id="fluidTrailValue">${s.trailPersistence}</span></label>
                <input type="range" id="fluidTrail" min="0.8" max="0.98" value="${s.trailPersistence}" step="0.01">
            </div>
            <div class="control-group">
                <label>Velocity Influence: <span id="fluidVelocityValue">${s.velocityInfluence}</span></label>
                <input type="range" id="fluidVelocity" min="0" max="5" value="${s.velocityInfluence}" step="0.2">
            </div>
            <button id="resetViz">Reset to Defaults</button>
        `;
    }

    getOrbitControls() {
        const s = this.orbitSettings;
        return `
            <div class="control-group">
                <label>Orbiter Count: <span id="orbitCountValue">${s.orbiterCount}</span></label>
                <input type="range" id="orbitCount" min="4" max="20" value="${s.orbiterCount}" step="1">
            </div>
            <div class="control-group">
                <label>Orbit Radius: <span id="orbitRadiusValue">${s.orbitRadius}</span>px</label>
                <input type="range" id="orbitRadius" min="20" max="100" value="${s.orbitRadius}" step="5">
            </div>
            <div class="control-group">
                <label>Orbit Speed: <span id="orbitSpeedValue">${s.orbitSpeed}</span></label>
                <input type="range" id="orbitSpeed" min="0.001" max="0.01" value="${s.orbitSpeed}" step="0.0005">
            </div>
            <div class="control-group">
                <label>Orbiter Size: <span id="orbitSizeValue">${s.orbiterSize}</span>px</label>
                <input type="range" id="orbitSize" min="2" max="12" value="${s.orbiterSize}" step="0.5">
            </div>
            <div class="control-group">
                <label>Sun Size: <span id="orbitSunValue">${s.sunSize}</span>px</label>
                <input type="range" id="orbitSun" min="8" max="30" value="${s.sunSize}" step="1">
            </div>
            <div class="control-group">
                <label>Trail Length: <span id="orbitTrailValue">${s.trailLength}</span></label>
                <input type="range" id="orbitTrail" min="0" max="0.5" value="${s.trailLength}" step="0.05">
            </div>
            <div class="control-group">
                <label>Wobble: <span id="orbitWobbleValue">${s.wobble}</span></label>
                <input type="range" id="orbitWobble" min="0" max="20" value="${s.wobble}" step="1">
            </div>
            <div class="control-group">
                <label>Glow Intensity: <span id="orbitGlowValue">${s.glowIntensity}</span></label>
                <input type="range" id="orbitGlow" min="0" max="40" value="${s.glowIntensity}" step="2">
            </div>
            <button id="resetViz">Reset to Defaults</button>
        `;
    }

    getKaleidoscopeControls() {
        const s = this.kaleidoscopeSettings;
        return `
            <div class="control-group">
                <label>Symmetry Count: <span id="kaleSymmetryValue">${s.symmetryCount}</span></label>
                <input type="range" id="kaleSymmetry" min="3" max="12" value="${s.symmetryCount}" step="1">
            </div>
            <div class="control-group">
                <label>Finger Size: <span id="kaleFingerValue">${s.fingerSize}</span>px</label>
                <input type="range" id="kaleFinger" min="8" max="40" value="${s.fingerSize}" step="2">
            </div>
            <div class="control-group">
                <label>Line Opacity: <span id="kaleLineValue">${s.lineOpacity}</span></label>
                <input type="range" id="kaleLine" min="0" max="1" value="${s.lineOpacity}" step="0.05">
            </div>
            <div class="control-group">
                <label>Rotation Speed: <span id="kaleRotationValue">${s.rotationSpeed}</span></label>
                <input type="range" id="kaleRotation" min="0" max="0.01" value="${s.rotationSpeed}" step="0.0005">
            </div>
            <div class="control-group">
                <label>Trail Persistence: <span id="kaleTrailValue">${s.trailPersistence}</span></label>
                <input type="range" id="kaleTrail" min="0.7" max="0.95" value="${s.trailPersistence}" step="0.01">
            </div>
            <div class="control-group">
                <label>Glow Intensity: <span id="kaleGlowValue">${s.glowIntensity}</span></label>
                <input type="range" id="kaleGlow" min="0" max="50" value="${s.glowIntensity}" step="2">
            </div>
            <div class="control-group checkbox-group">
                <label><input type="checkbox" id="kalePulse" ${s.pulseWithAudio ? 'checked' : ''}> Pulse With Audio</label>
                <label><input type="checkbox" id="kaleCenter" ${s.showCenter ? 'checked' : ''}> Show Center</label>
            </div>
            <button id="resetViz">Reset to Defaults</button>
        `;
    }

    getEchoControls() {
        const s = this.echoSettings;
        return `
            <div class="control-group">
                <label>Trail Length: <span id="echoLengthValue">${s.trailLength}</span></label>
                <input type="range" id="echoLength" min="5" max="60" value="${s.trailLength}" step="1">
            </div>
            <div class="control-group">
                <label>Fade Speed: <span id="echoFadeValue">${s.fadeSpeed}</span></label>
                <input type="range" id="echoFade" min="0.01" max="0.1" value="${s.fadeSpeed}" step="0.005">
            </div>
            <div class="control-group">
                <label>Chromatic Aberration: <span id="echoChromaticValue">${s.chromaticAberration}</span>px</label>
                <input type="range" id="echoChromatic" min="0" max="10" value="${s.chromaticAberration}" step="0.5">
            </div>
            <div class="control-group">
                <label>Echo Spacing: <span id="echoSpacingValue">${s.echoSpacing}</span></label>
                <input type="range" id="echoSpacing" min="1" max="5" value="${s.echoSpacing}" step="1">
            </div>
            <div class="control-group">
                <label>Glow Intensity: <span id="echoGlowValue">${s.glowIntensity}</span></label>
                <input type="range" id="echoGlow" min="0" max="30" value="${s.glowIntensity}" step="2">
            </div>
            <div class="control-group">
                <label>Finger Size: <span id="echoFingerValue">${s.fingerSize}</span>px</label>
                <input type="range" id="echoFinger" min="6" max="24" value="${s.fingerSize}" step="1">
            </div>
            <div class="control-group">
                <label>Palm Size: <span id="echoPalmValue">${s.palmSize}</span>px</label>
                <input type="range" id="echoPalm" min="10" max="40" value="${s.palmSize}" step="2">
            </div>
            <div class="control-group checkbox-group">
                <label><input type="checkbox" id="echoMotionBlur" ${s.motionBlur ? 'checked' : ''}> Motion Blur</label>
                <label><input type="checkbox" id="echoPalm" ${s.showPalm ? 'checked' : ''}> Show Palm</label>
                <label><input type="checkbox" id="echoFingers" ${s.showFingers ? 'checked' : ''}> Show Fingers</label>
            </div>
            <button id="resetViz">Reset to Defaults</button>
        `;
    }

    attachVizDebugListeners() {
        // Remove old listeners by replacing setupVizDebugListeners
        // Mode-specific listeners based on current mode
        if (this.visualizationMode === 1) {
            this.attachParticleListeners();
        } else if (this.visualizationMode === 2) {
            this.attachBloomListeners();
        } else if (this.visualizationMode === 3) {
            this.attachFluidListeners();
        } else if (this.visualizationMode === 4) {
            this.attachOrbitListeners();
        } else if (this.visualizationMode === 5) {
            this.attachKaleidoscopeListeners();
        } else if (this.visualizationMode === 6) {
            this.attachEchoListeners();
        }

        // All modes have reset button
        const resetBtn = document.getElementById('resetViz');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => this.resetCurrentModeSettings());
        }
    }

    attachParticleListeners() {
        document.getElementById('emissionRate').addEventListener('input', (e) => {
            this.particleSettings.emissionRate = parseFloat(e.target.value);
            document.getElementById('emissionRateValue').textContent = e.target.value;
        });
        document.getElementById('lifetime').addEventListener('input', (e) => {
            this.particleSettings.lifetime = parseInt(e.target.value);
            document.getElementById('lifetimeValue').textContent = e.target.value;
        });
        document.getElementById('initialVelocity').addEventListener('input', (e) => {
            this.particleSettings.initialVelocity = parseFloat(e.target.value);
            document.getElementById('initialVelocityValue').textContent = e.target.value;
        });
        document.getElementById('gravity').addEventListener('input', (e) => {
            this.particleSettings.gravity = parseFloat(e.target.value);
            document.getElementById('gravityValue').textContent = e.target.value;
        });
        document.getElementById('drag').addEventListener('input', (e) => {
            this.particleSettings.drag = parseFloat(e.target.value);
            document.getElementById('dragValue').textContent = e.target.value;
        });
        document.getElementById('attraction').addEventListener('input', (e) => {
            this.particleSettings.attraction = parseFloat(e.target.value);
            document.getElementById('attractionValue').textContent = e.target.value;
        });
        document.getElementById('repulsion').addEventListener('input', (e) => {
            this.particleSettings.repulsion = parseFloat(e.target.value);
            document.getElementById('repulsionValue').textContent = e.target.value;
        });
        document.getElementById('turbulence').addEventListener('input', (e) => {
            this.particleSettings.turbulence = parseFloat(e.target.value);
            document.getElementById('turbulenceValue').textContent = e.target.value;
        });
        document.getElementById('particleSizeMin').addEventListener('input', (e) => {
            this.particleSettings.particleSizeMin = parseFloat(e.target.value);
            document.getElementById('particleSizeMinValue').textContent = e.target.value;
        });
        document.getElementById('particleSizeMax').addEventListener('input', (e) => {
            this.particleSettings.particleSizeMax = parseFloat(e.target.value);
            document.getElementById('particleSizeMaxValue').textContent = e.target.value;
        });
        document.getElementById('colorMode').addEventListener('change', (e) => {
            this.particleSettings.colorMode = e.target.value;
        });
        document.getElementById('blendMode').addEventListener('change', (e) => {
            this.particleSettings.blendMode = e.target.value;
        });
        document.getElementById('alpha').addEventListener('input', (e) => {
            this.particleSettings.alpha = parseFloat(e.target.value);
            document.getElementById('alphaValue').textContent = e.target.value;
        });
        document.getElementById('glow').addEventListener('change', (e) => {
            this.particleSettings.glow = e.target.checked;
        });
        document.getElementById('trails').addEventListener('change', (e) => {
            this.particleSettings.trails = e.target.checked;
        });
        document.getElementById('audioReactive').addEventListener('change', (e) => {
            this.particleSettings.audioReactive = e.target.checked;
        });
        const clearBtn = document.getElementById('clearParticles');
        if (clearBtn) {
            clearBtn.addEventListener('click', () => {
                this.particles = [];
                console.log('Cleared all particles');
            });
        }
    }

    attachBloomListeners() {
        document.getElementById('bloomVelocity').addEventListener('input', (e) => {
            this.bloomSettings.velocityThreshold = parseFloat(e.target.value);
            document.getElementById('bloomVelocityValue').textContent = e.target.value;
        });
        document.getElementById('bloomInterval').addEventListener('input', (e) => {
            this.bloomSettings.bloomInterval = parseInt(e.target.value);
            document.getElementById('bloomIntervalValue').textContent = e.target.value;
        });
        document.getElementById('bloomLifetime').addEventListener('input', (e) => {
            this.bloomSettings.lifetime = parseInt(e.target.value);
            document.getElementById('bloomLifetimeValue').textContent = e.target.value;
        });
        document.getElementById('bloomRadius').addEventListener('input', (e) => {
            this.bloomSettings.maxRadius = parseInt(e.target.value);
            document.getElementById('bloomRadiusValue').textContent = e.target.value;
        });
        document.getElementById('bloomRings').addEventListener('input', (e) => {
            this.bloomSettings.ringCount = parseInt(e.target.value);
            document.getElementById('bloomRingsValue').textContent = e.target.value;
        });
        document.getElementById('bloomSpacing').addEventListener('input', (e) => {
            this.bloomSettings.ringSpacing = parseInt(e.target.value);
            document.getElementById('bloomSpacingValue').textContent = e.target.value;
        });
        document.getElementById('bloomSpeed').addEventListener('input', (e) => {
            this.bloomSettings.pulseSpeed = parseFloat(e.target.value);
            document.getElementById('bloomSpeedValue').textContent = e.target.value;
        });
        document.getElementById('bloomGlow').addEventListener('input', (e) => {
            this.bloomSettings.glowIntensity = parseInt(e.target.value);
            document.getElementById('bloomGlowValue').textContent = e.target.value;
        });
        document.getElementById('bloomColorShift').addEventListener('change', (e) => {
            this.bloomSettings.colorShift = e.target.checked;
        });
        const clearBtn = document.getElementById('clearBlooms');
        if (clearBtn) {
            clearBtn.addEventListener('click', () => {
                this.blooms = [];
                console.log('Cleared all blooms');
            });
        }
    }

    attachFluidListeners() {
        document.getElementById('fluidTendrils').addEventListener('input', (e) => {
            this.fluidSettings.tendrilCount = parseInt(e.target.value);
            document.getElementById('fluidTendrilsValue').textContent = e.target.value;
        });
        document.getElementById('fluidRadius').addEventListener('input', (e) => {
            this.fluidSettings.tendrilRadius = parseInt(e.target.value);
            document.getElementById('fluidRadiusValue').textContent = e.target.value;
        });
        document.getElementById('fluidSpeed').addEventListener('input', (e) => {
            this.fluidSettings.flowSpeed = parseFloat(e.target.value);
            document.getElementById('fluidSpeedValue').textContent = e.target.value;
        });
        document.getElementById('fluidPulse').addEventListener('input', (e) => {
            this.fluidSettings.pulseAmount = parseInt(e.target.value);
            document.getElementById('fluidPulseValue').textContent = e.target.value;
        });
        document.getElementById('fluidGradient').addEventListener('input', (e) => {
            this.fluidSettings.gradientSize = parseInt(e.target.value);
            document.getElementById('fluidGradientValue').textContent = e.target.value;
        });
        document.getElementById('fluidOpacity').addEventListener('input', (e) => {
            this.fluidSettings.opacity = parseFloat(e.target.value);
            document.getElementById('fluidOpacityValue').textContent = e.target.value;
        });
        document.getElementById('fluidTrail').addEventListener('input', (e) => {
            this.fluidSettings.trailPersistence = parseFloat(e.target.value);
            document.getElementById('fluidTrailValue').textContent = e.target.value;
        });
        document.getElementById('fluidVelocity').addEventListener('input', (e) => {
            this.fluidSettings.velocityInfluence = parseFloat(e.target.value);
            document.getElementById('fluidVelocityValue').textContent = e.target.value;
        });
    }

    attachOrbitListeners() {
        document.getElementById('orbitCount').addEventListener('input', (e) => {
            this.orbitSettings.orbiterCount = parseInt(e.target.value);
            document.getElementById('orbitCountValue').textContent = e.target.value;
        });
        document.getElementById('orbitRadius').addEventListener('input', (e) => {
            this.orbitSettings.orbitRadius = parseInt(e.target.value);
            document.getElementById('orbitRadiusValue').textContent = e.target.value;
        });
        document.getElementById('orbitSpeed').addEventListener('input', (e) => {
            this.orbitSettings.orbitSpeed = parseFloat(e.target.value);
            document.getElementById('orbitSpeedValue').textContent = e.target.value;
        });
        document.getElementById('orbitSize').addEventListener('input', (e) => {
            this.orbitSettings.orbiterSize = parseFloat(e.target.value);
            document.getElementById('orbitSizeValue').textContent = e.target.value;
        });
        document.getElementById('orbitSun').addEventListener('input', (e) => {
            this.orbitSettings.sunSize = parseInt(e.target.value);
            document.getElementById('orbitSunValue').textContent = e.target.value;
        });
        document.getElementById('orbitTrail').addEventListener('input', (e) => {
            this.orbitSettings.trailLength = parseFloat(e.target.value);
            document.getElementById('orbitTrailValue').textContent = e.target.value;
        });
        document.getElementById('orbitWobble').addEventListener('input', (e) => {
            this.orbitSettings.wobble = parseInt(e.target.value);
            document.getElementById('orbitWobbleValue').textContent = e.target.value;
        });
        document.getElementById('orbitGlow').addEventListener('input', (e) => {
            this.orbitSettings.glowIntensity = parseInt(e.target.value);
            document.getElementById('orbitGlowValue').textContent = e.target.value;
        });
    }

    attachKaleidoscopeListeners() {
        document.getElementById('kaleSymmetry').addEventListener('input', (e) => {
            this.kaleidoscopeSettings.symmetryCount = parseInt(e.target.value);
            document.getElementById('kaleSymmetryValue').textContent = e.target.value;
        });
        document.getElementById('kaleFinger').addEventListener('input', (e) => {
            this.kaleidoscopeSettings.fingerSize = parseInt(e.target.value);
            document.getElementById('kaleFingerValue').textContent = e.target.value;
        });
        document.getElementById('kaleLine').addEventListener('input', (e) => {
            this.kaleidoscopeSettings.lineOpacity = parseFloat(e.target.value);
            document.getElementById('kaleLineValue').textContent = e.target.value;
        });
        document.getElementById('kaleRotation').addEventListener('input', (e) => {
            this.kaleidoscopeSettings.rotationSpeed = parseFloat(e.target.value);
            document.getElementById('kaleRotationValue').textContent = e.target.value;
        });
        document.getElementById('kaleTrail').addEventListener('input', (e) => {
            this.kaleidoscopeSettings.trailPersistence = parseFloat(e.target.value);
            document.getElementById('kaleTrailValue').textContent = e.target.value;
        });
        document.getElementById('kaleGlow').addEventListener('input', (e) => {
            this.kaleidoscopeSettings.glowIntensity = parseInt(e.target.value);
            document.getElementById('kaleGlowValue').textContent = e.target.value;
        });
        document.getElementById('kalePulse').addEventListener('change', (e) => {
            this.kaleidoscopeSettings.pulseWithAudio = e.target.checked;
        });
        document.getElementById('kaleCenter').addEventListener('change', (e) => {
            this.kaleidoscopeSettings.showCenter = e.target.checked;
        });
    }

    attachEchoListeners() {
        document.getElementById('echoLength').addEventListener('input', (e) => {
            this.echoSettings.trailLength = parseInt(e.target.value);
            document.getElementById('echoLengthValue').textContent = e.target.value;
        });
        document.getElementById('echoFade').addEventListener('input', (e) => {
            this.echoSettings.fadeSpeed = parseFloat(e.target.value);
            document.getElementById('echoFadeValue').textContent = e.target.value;
        });
        document.getElementById('echoChromatic').addEventListener('input', (e) => {
            this.echoSettings.chromaticAberration = parseFloat(e.target.value);
            document.getElementById('echoChromaticValue').textContent = e.target.value;
        });
        document.getElementById('echoSpacing').addEventListener('input', (e) => {
            this.echoSettings.echoSpacing = parseInt(e.target.value);
            document.getElementById('echoSpacingValue').textContent = e.target.value;
        });
        document.getElementById('echoGlow').addEventListener('input', (e) => {
            this.echoSettings.glowIntensity = parseInt(e.target.value);
            document.getElementById('echoGlowValue').textContent = e.target.value;
        });
        document.getElementById('echoFinger').addEventListener('input', (e) => {
            this.echoSettings.fingerSize = parseInt(e.target.value);
            document.getElementById('echoFingerValue').textContent = e.target.value;
        });
        document.getElementById('echoPalm').addEventListener('input', (e) => {
            this.echoSettings.palmSize = parseInt(e.target.value);
            document.getElementById('echoPalmValue').textContent = e.target.value;
        });
        document.getElementById('echoMotionBlur').addEventListener('change', (e) => {
            this.echoSettings.motionBlur = e.target.checked;
        });
    }

    resetCurrentModeSettings() {
        if (this.visualizationMode === 1) {
            this.resetVizSettings();
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
        this.populateVizDebugPanel();
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
        // Capture hand geometry at moment of entering pads mode (5 fingers spread)
        if (!hand || !hand.fingertips || hand.fingertips.length !== 5) {
            console.log('Cannot calibrate: need all 5 fingertips');
            return;
        }

        // Store fingertip positions
        this.padCalibration.fingertipPositions = hand.fingertips.map(ft => ({
            x: ft.x,
            y: ft.y,
            fingerIndex: ft.fingerIndex
        }));

        // Calculate distances between adjacent fingers
        this.padCalibration.fingertipDistances = [];
        for (let i = 0; i < 4; i++) {
            const ft1 = hand.fingertips[i];
            const ft2 = hand.fingertips[i + 1];
            const dist = Math.hypot(ft2.x - ft1.x, ft2.y - ft1.y);
            this.padCalibration.fingertipDistances.push(dist);
        }

        // Calculate hand center (palm position or average of fingertips)
        if (hand.palm) {
            this.padCalibration.handCenter = { x: hand.palm.x, y: hand.palm.y };
        } else {
            const avgX = hand.fingertips.reduce((sum, ft) => sum + ft.x, 0) / 5;
            const avgY = hand.fingertips.reduce((sum, ft) => sum + ft.y, 0) / 5;
            this.padCalibration.handCenter = { x: avgX, y: avgY };
        }

        // Calculate scale factor (average finger spacing compared to baseline)
        const avgDistance = this.padCalibration.fingertipDistances.reduce((a, b) => a + b, 0) / 4;
        const baselineDistance = 100; // Expected distance for "normal" hand size
        this.padCalibration.scale = avgDistance / baselineDistance;

        this.padCalibration.calibrated = true;

        console.log(`Pads calibrated! Scale: ${this.padCalibration.scale.toFixed(2)}x, Hand center: (${Math.round(this.padCalibration.handCenter.x)}, ${Math.round(this.padCalibration.handCenter.y)})`);
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
        this.audioContext = new (window.AudioContext || window.webkitAudioContext)();

        const resumeAudio = async () => {
            if (this.audioContext.state === 'suspended') {
                await this.audioContext.resume();
                console.log('Audio context resumed!');
            }
        };

        document.body.addEventListener('click', resumeAudio, { once: true });
        document.body.addEventListener('touchstart', resumeAudio, { once: true });
        document.body.addEventListener('keydown', resumeAudio, { once: true });

        // Master gain
        this.masterGain = this.audioContext.createGain();
        this.masterGain.gain.value = 0.25;

        // Global filter (controlled by left hand finger spread)
        this.filterNode = this.audioContext.createBiquadFilter();
        this.filterNode.type = 'lowpass';
        this.filterNode.frequency.value = 2000;
        this.filterNode.Q.value = 1;

        // Delay effect (controlled by right hand finger spread)
        this.delayNode = this.audioContext.createDelay(1.0);
        this.delayNode.delayTime.value = 0.3;

        this.delayGain = this.audioContext.createGain();
        this.delayGain.gain.value = 0;

        this.delayFeedback = this.audioContext.createGain();
        this.delayFeedback.gain.value = 0.4;

        // Connect delay feedback loop
        this.delayNode.connect(this.delayFeedback);
        this.delayFeedback.connect(this.delayNode);
        this.delayNode.connect(this.delayGain);

        // Create reverb
        this.reverb = this.createReverb();

        // Audio chain: filter -> delay -> reverb -> master
        this.filterNode.connect(this.reverb);
        this.delayGain.connect(this.reverb);
        this.reverb.connect(this.masterGain);
        this.masterGain.connect(this.audioContext.destination);

        this.audioEnabled = true;
        console.log('Audio initialized with advanced routing');
    }

    createReverb() {
        const convolver = this.audioContext.createConvolver();
        const rate = this.audioContext.sampleRate;
        const length = rate * 3;
        const impulse = this.audioContext.createBuffer(2, length, rate);

        for (let channel = 0; channel < 2; channel++) {
            const channelData = impulse.getChannelData(channel);
            for (let i = 0; i < length; i++) {
                channelData[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / length, 2.5);
            }
        }

        convolver.buffer = impulse;
        return convolver;
    }

    // Theremin mode audio control
    startTheremin() {
        if (!this.audioEnabled || this.isMuted || !this.audioContext || this.thereminActive) {
            return;
        }

        const now = this.audioContext.currentTime;

        // Create continuous oscillator
        this.thereminOsc = this.audioContext.createOscillator();
        this.thereminOsc.type = 'triangle';
        this.thereminOsc.frequency.value = 440;

        // Theremin-specific filter
        this.thereminFilter = this.audioContext.createBiquadFilter();
        this.thereminFilter.type = 'lowpass';
        this.thereminFilter.frequency.value = 2000;
        this.thereminFilter.Q.value = 5;

        // Theremin gain with smooth attack
        this.thereminGain = this.audioContext.createGain();
        this.thereminGain.gain.setValueAtTime(0, now);
        this.thereminGain.gain.linearRampToValueAtTime(0.3, now + 0.05);

        // Connect: osc -> filter -> gain -> reverb -> master
        this.thereminOsc.connect(this.thereminFilter);
        this.thereminFilter.connect(this.thereminGain);
        this.thereminGain.connect(this.reverb);

        this.thereminOsc.start(now);
        this.thereminActive = true;
        console.log('Theremin started');
    }

    stopTheremin() {
        if (!this.thereminActive || !this.thereminOsc) {
            return;
        }

        const now = this.audioContext.currentTime;

        // Smooth release
        this.thereminGain.gain.linearRampToValueAtTime(0, now + 0.2);

        setTimeout(() => {
            if (this.thereminOsc) {
                this.thereminOsc.stop();
                this.thereminOsc = null;
                this.thereminGain = null;
                this.thereminFilter = null;
            }
            this.thereminActive = false;
        }, 250);

        console.log('Theremin stopped');
    }

    updateTheremin(hand) {
        if (!this.thereminActive || !this.thereminOsc || !hand) {
            return;
        }

        const now = this.audioContext.currentTime;

        // X-axis controls pitch (quantized to scale)
        const normalizedX = hand.palm.x / this.canvas.width;
        const frequency = this.quantizeToScale(normalizedX);
        this.thereminOsc.frequency.exponentialRampToValueAtTime(frequency, now + 0.05);

        // Y-axis controls filter cutoff
        const normalizedY = hand.palm.y / this.canvas.height;
        const filterFreq = 200 + (1 - normalizedY) * 3800; // Inverted: top = bright
        this.thereminFilter.frequency.exponentialRampToValueAtTime(Math.max(200, filterFreq), now + 0.05);

        // Finger spread controls vibrato/resonance
        const spread = Math.max(50, Math.min(250, hand.fingerSpread));
        const resonance = 1 + ((spread - 50) / 200) * 15; // Q: 1-16
        this.thereminFilter.Q.linearRampToValueAtTime(resonance, now + 0.05);
    }

    // Drum synthesis for sample pads
    playDrumSample(type) {
        if (!this.audioEnabled || this.isMuted || !this.audioContext) {
            return;
        }

        const now = this.audioContext.currentTime;

        try {
            switch (type) {
                // Thumb - Bass sounds
                case 'kick':
                    this.playKick(now);
                    break;
                case 'bass1':
                    this.playBass(now, 55);
                    break;
                case 'bass2':
                    this.playBass(now, 65);
                    break;
                case 'bass3':
                    this.playBass(now, 82);
                    break;
                case 'subkick':
                    this.playKick(now, 100, 30);
                    break;

                // Index - Snares
                case 'snare':
                    this.playSnare(now);
                    break;
                case 'rimshot':
                    this.playRim(now, 600);
                    break;
                case 'clap':
                    this.playClap(now);
                    break;
                case 'snap':
                    this.playSnap(now);
                    break;
                case 'sidestick':
                    this.playRim(now, 800);
                    break;

                // Middle - Hi-hats/Cymbals
                case 'hihat':
                    this.playHihat(now, 0.1);
                    break;
                case 'hihat_open':
                    this.playHihat(now, 0.3);
                    break;
                case 'crash':
                    this.playCrash(now);
                    break;
                case 'ride':
                    this.playRide(now);
                    break;
                case 'splash':
                    this.playCrash(now, 0.8);
                    break;

                // Ring - Toms
                case 'tom1':
                    this.playTom(now, 120);
                    break;
                case 'tom2':
                    this.playTom(now, 90);
                    break;
                case 'tom3':
                    this.playTom(now, 70);
                    break;
                case 'conga':
                    this.playTom(now, 200);
                    break;
                case 'bongo':
                    this.playTom(now, 250);
                    break;

                // Pinky - Synths
                case 'chord1':
                    this.playChordPad(now, [261.63, 329.63, 392.00]); // C major
                    break;
                case 'chord2':
                    this.playChordPad(now, [293.66, 349.23, 440.00]); // D minor
                    break;
                case 'lead':
                    this.playLead(now);
                    break;
                case 'fx1':
                    this.playFX(now, 800, 2000);
                    break;
                case 'fx2':
                    this.playFX(now, 400, 1200);
                    break;
            }
        } catch (error) {
            console.error('Error playing drum sample:', error);
        }
    }

    playKick(now, startFreq = 150, endFreq = 40) {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();

        osc.frequency.setValueAtTime(startFreq, now);
        osc.frequency.exponentialRampToValueAtTime(endFreq, now + 0.1);

        gain.gain.setValueAtTime(1, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.5);

        osc.connect(gain);
        gain.connect(this.masterGain);

        osc.start(now);
        osc.stop(now + 0.5);
    }

    playSnare(now) {
        // Tone component
        const osc = this.audioContext.createOscillator();
        const oscGain = this.audioContext.createGain();
        osc.frequency.value = 200;
        oscGain.gain.setValueAtTime(0.3, now);
        oscGain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
        osc.connect(oscGain);

        // Noise component
        const bufferSize = this.audioContext.sampleRate * 0.2;
        const buffer = this.audioContext.createBuffer(1, bufferSize, this.audioContext.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
            data[i] = Math.random() * 2 - 1;
        }

        const noise = this.audioContext.createBufferSource();
        noise.buffer = buffer;
        const noiseGain = this.audioContext.createGain();
        noiseGain.gain.setValueAtTime(0.5, now);
        noiseGain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
        noise.connect(noiseGain);

        oscGain.connect(this.masterGain);
        noiseGain.connect(this.masterGain);

        osc.start(now);
        osc.stop(now + 0.2);
        noise.start(now);
    }

    playHihat(now, decay = 0.1) {
        const bufferSize = this.audioContext.sampleRate * decay;
        const buffer = this.audioContext.createBuffer(1, bufferSize, this.audioContext.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
            data[i] = Math.random() * 2 - 1;
        }

        const noise = this.audioContext.createBufferSource();
        noise.buffer = buffer;

        const filter = this.audioContext.createBiquadFilter();
        filter.type = 'highpass';
        filter.frequency.value = 7000;

        const gain = this.audioContext.createGain();
        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + decay);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(this.masterGain);

        noise.start(now);
    }

    playClap(now) {
        for (let i = 0; i < 3; i++) {
            const delay = i * 0.02;
            const bufferSize = this.audioContext.sampleRate * 0.1;
            const buffer = this.audioContext.createBuffer(1, bufferSize, this.audioContext.sampleRate);
            const data = buffer.getChannelData(0);
            for (let j = 0; j < bufferSize; j++) {
                data[j] = Math.random() * 2 - 1;
            }

            const noise = this.audioContext.createBufferSource();
            noise.buffer = buffer;
            const gain = this.audioContext.createGain();
            gain.gain.setValueAtTime(0.4, now + delay);
            gain.gain.exponentialRampToValueAtTime(0.01, now + delay + 0.15);

            noise.connect(gain);
            gain.connect(this.masterGain);
            noise.start(now + delay);
        }
    }

    playTom(now, freq) {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();

        osc.frequency.setValueAtTime(freq, now);
        osc.frequency.exponentialRampToValueAtTime(freq * 0.5, now + 0.3);

        gain.gain.setValueAtTime(0.7, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);

        osc.connect(gain);
        gain.connect(this.masterGain);

        osc.start(now);
        osc.stop(now + 0.3);
    }

    playRim(now, freq = 400) {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();
        osc.frequency.value = freq;
        osc.type = 'square';

        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.05);

        osc.connect(gain);
        gain.connect(this.masterGain);

        osc.start(now);
        osc.stop(now + 0.05);
    }

    playSnap(now) {
        // Short, sharp noise burst
        const bufferSize = this.audioContext.sampleRate * 0.05;
        const buffer = this.audioContext.createBuffer(1, bufferSize, this.audioContext.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
            data[i] = Math.random() * 2 - 1;
        }

        const noise = this.audioContext.createBufferSource();
        noise.buffer = buffer;

        const filter = this.audioContext.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.value = 2000;
        filter.Q.value = 10;

        const gain = this.audioContext.createGain();
        gain.gain.setValueAtTime(0.5, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.05);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(this.masterGain);

        noise.start(now);
    }

    playCowbell(now) {
        const osc1 = this.audioContext.createOscillator();
        const osc2 = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();

        osc1.frequency.value = 540;
        osc2.frequency.value = 800;
        osc1.type = 'square';
        osc2.type = 'square';

        gain.gain.setValueAtTime(0.4, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);

        osc1.connect(gain);
        osc2.connect(gain);
        gain.connect(this.masterGain);

        osc1.start(now);
        osc2.start(now);
        osc1.stop(now + 0.2);
        osc2.stop(now + 0.2);
    }

    playCrash(now, decay = 1.5) {
        const bufferSize = this.audioContext.sampleRate * decay;
        const buffer = this.audioContext.createBuffer(1, bufferSize, this.audioContext.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
            data[i] = Math.random() * 2 - 1;
        }

        const noise = this.audioContext.createBufferSource();
        noise.buffer = buffer;

        const filter = this.audioContext.createBiquadFilter();
        filter.type = 'highpass';
        filter.frequency.value = 5000;

        const gain = this.audioContext.createGain();
        gain.gain.setValueAtTime(0.5, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + decay);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(this.masterGain);

        noise.start(now);
    }

    playRide(now) {
        const osc1 = this.audioContext.createOscillator();
        const osc2 = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();

        osc1.frequency.value = 3000;
        osc2.frequency.value = 4500;
        osc1.type = 'square';
        osc2.type = 'square';

        gain.gain.setValueAtTime(0.15, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.5);

        osc1.connect(gain);
        osc2.connect(gain);
        gain.connect(this.masterGain);

        osc1.start(now);
        osc2.start(now);
        osc1.stop(now + 0.5);
        osc2.stop(now + 0.5);
    }

    playPerc(now, freq) {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();
        osc.frequency.value = freq;
        osc.type = 'sine';

        gain.gain.setValueAtTime(0.4, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.15);

        osc.connect(gain);
        gain.connect(this.masterGain);

        osc.start(now);
        osc.stop(now + 0.15);
    }

    playBass(now, freq = 55) {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();
        osc.frequency.value = freq;
        osc.type = 'sawtooth';

        const filter = this.audioContext.createBiquadFilter();
        filter.type = 'lowpass';
        filter.frequency.value = 300;

        gain.gain.setValueAtTime(0.6, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.4);

        osc.connect(filter);
        filter.connect(gain);
        gain.connect(this.masterGain);

        osc.start(now);
        osc.stop(now + 0.4);
    }

    playFX(now, startFreq, endFreq) {
        // Sweep effect sound
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();
        osc.type = 'sawtooth';

        osc.frequency.setValueAtTime(startFreq, now);
        osc.frequency.exponentialRampToValueAtTime(endFreq, now + 0.4);

        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.4);

        osc.connect(gain);
        gain.connect(this.filterNode);

        osc.start(now);
        osc.stop(now + 0.4);
    }

    playChordPad(now, frequencies) {
        for (let i = 0; i < frequencies.length; i++) {
            const osc = this.audioContext.createOscillator();
            const gain = this.audioContext.createGain();
            osc.frequency.value = frequencies[i];
            osc.type = 'sawtooth';

            gain.gain.setValueAtTime(0.2, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 1.5);

            osc.connect(gain);
            gain.connect(this.filterNode);

            osc.start(now);
            osc.stop(now + 1.5);
        }
    }

    playLead(now) {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();
        osc.frequency.value = 523.25; // C5
        osc.type = 'square';

        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);

        osc.connect(gain);
        gain.connect(this.filterNode);

        osc.start(now);
        osc.stop(now + 0.3);
    }

    async initHandTracking() {
        this.hands = new Hands({
            locateFile: (file) => {
                return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
            }
        });

        this.hands.setOptions({
            maxNumHands: 2,
            modelComplexity: 1,
            minDetectionConfidence: 0.6,
            minTrackingConfidence: 0.6
        });

        this.hands.onResults((results) => this.onHandResults(results));

        this.camera = new Camera(this.video, {
            onFrame: async () => {
                await this.hands.send({ image: this.video });
            },
            width: 640,
            height: 480
        });

        await this.camera.start();
    }

    onHandResults(results) {
        this.handResults = results;
        this.prevLeftHand = this.leftHand;
        this.prevRightHand = this.rightHand;
        this.leftHand = null;
        this.rightHand = null;

        if (results.multiHandLandmarks && results.multiHandLandmarks.length > 0) {
            this.noHandsTime = 0;
            this.fadeoutStarted = false;

            for (let handIndex = 0; handIndex < results.multiHandLandmarks.length; handIndex++) {
                const landmarks = results.multiHandLandmarks[handIndex];
                const handedness = results.multiHandedness[handIndex].label; // "Left" or "Right"

                // Get fingertips (mirror X for canvas mapping to match user perspective)
                const fingertipIndices = [4, 8, 12, 16, 20];
                const fingertips = fingertipIndices.map((idx, i) => ({
                    x: (1 - landmarks[idx].x) * this.canvas.width,
                    y: landmarks[idx].y * this.canvas.height,
                    z: landmarks[idx].z,
                    fingerIndex: i,
                    fingerId: `${handedness}_finger${i}`
                }));

                // Calculate palm position (mirror X for canvas mapping)
                const palm = {
                    x: (1 - landmarks[9].x) * this.canvas.width,
                    y: landmarks[9].y * this.canvas.height,
                    z: landmarks[9].z
                };

                // Calculate finger spread (thumb to pinky distance)
                const thumb = fingertips[0];
                const pinky = fingertips[4];
                const fingerSpread = Math.sqrt(
                    Math.pow(pinky.x - thumb.x, 2) +
                    Math.pow(pinky.y - thumb.y, 2)
                );

                const handData = {
                    landmarks: landmarks,
                    fingertips: fingertips,
                    palm: palm,
                    fingerSpread: fingerSpread,
                    handedness: handedness
                };

                // Assign to left or right
                if (handedness === 'Left') {
                    this.leftHand = handData;
                } else {
                    this.rightHand = handData;
                }

                // Update trails for each finger
                for (const tip of fingertips) {
                    if (!this.fingerTrails[tip.fingerId]) {
                        this.fingerTrails[tip.fingerId] = [];
                    }

                    this.fingerTrails[tip.fingerId].push({
                        x: tip.x,
                        y: tip.y,
                        time: this.time
                    });

                    if (this.fingerTrails[tip.fingerId].length > this.maxTrailLength) {
                        this.fingerTrails[tip.fingerId].shift();
                    }
                }
            }

            // Detect two-hand gestures
            if (this.leftHand && this.rightHand) {
                this.detectTwoHandGestures();
            } else {
                this.handsAreTouching = false;
                this.touchingFingers = [];
            }

        } else {
            // No hands detected
            this.noHandsTime += 16;
            if (this.noHandsTime > 1000) {
                this.fadeoutStarted = true;
                this.fingerTrails = {};
            }
        }

        this.updateDebug();
    }

    detectTwoHandGestures() {
        // Calculate distance between palms
        const palmDist = Math.sqrt(
            Math.pow(this.rightHand.palm.x - this.leftHand.palm.x, 2) +
            Math.pow(this.rightHand.palm.y - this.leftHand.palm.y, 2)
        );

        this.handsDistance = palmDist;
        this.handsAreTouching = palmDist < 100;

        // Detect touching fingertips
        this.touchingFingers = [];
        for (const leftFinger of this.leftHand.fingertips) {
            for (const rightFinger of this.rightHand.fingertips) {
                const dist = Math.sqrt(
                    Math.pow(rightFinger.x - leftFinger.x, 2) +
                    Math.pow(rightFinger.y - leftFinger.y, 2)
                );

                if (dist < 40) {
                    this.touchingFingers.push({
                        left: leftFinger,
                        right: rightFinger,
                        distance: dist
                    });
                }
            }
        }
    }

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
        if (!this.leftHand && !this.rightHand) return;

        const hands = [];
        if (this.leftHand) hands.push(this.leftHand);
        if (this.rightHand) hands.push(this.rightHand);

        const now = Date.now();

        for (const hand of hands) {
            for (const fingertip of hand.fingertips) {
                // Find pads that match this finger
                for (const pad of this.pads) {
                    // Only check pads for this specific finger
                    if (pad.fingerIndex !== fingertip.fingerIndex) continue;

                    const dx = fingertip.x - pad.centerX;
                    const dy = fingertip.y - pad.centerY;
                    const dist = Math.sqrt(dx * dx + dy * dy);

                    const isOver = dist < pad.size * 0.6; // Larger hit radius

                    if (isOver) {
                        // Fingertip is over pad - use selected algorithm
                        let tapDetected = false;

                        switch (this.padSettings.tapAlgorithm) {
                            case 'z-velocity':
                                tapDetected = this.detectTap_ZVelocity(pad, fingertip, now);
                                break;
                            case 'dwell-retreat':
                                tapDetected = this.detectTap_DwellRetreat(pad, fingertip, now);
                                break;
                            case 'wiggle':
                                tapDetected = this.detectTap_Wiggle(pad, fingertip, now);
                                break;
                            case 'hybrid':
                                tapDetected = this.detectTap_Hybrid(pad, fingertip, now);
                                break;
                        }

                        if (tapDetected && (!pad.triggered || now - pad.triggerTime > this.padSettings.retriggerDelay)) {
                            pad.triggered = true;
                            pad.triggerTime = now;
                            this.playDrumSample(pad.type);
                            console.log(`[${this.padSettings.tapAlgorithm}] Tapped: ${pad.type}`);
                        }
                    } else {
                        // Finger left the pad area - reset all state
                        pad.lastZ = null;
                        pad.dwellStartTime = null;
                        pad.lastXY = null;
                    }
                }
            }
        }

        // Reset triggered state after visual feedback timeout
        for (const pad of this.pads) {
            if (pad.triggered && now - pad.triggerTime > 150) {
                pad.triggered = false;
            }
        }
    }

    // Algorithm 1: Z-Velocity (forward motion detection)
    detectTap_ZVelocity(pad, fingertip, now) {
        if (pad.lastZ !== null) {
            const zDelta = pad.lastZ - fingertip.z; // Positive = toward camera
            if (zDelta > this.padSettings.zThreshold) {
                pad.lastZ = fingertip.z;
                return true;
            }
        }
        pad.lastZ = fingertip.z;
        return false;
    }

    // Algorithm 2: Dwell + Retreat (hover then pull back)
    detectTap_DwellRetreat(pad, fingertip, now) {
        if (pad.dwellStartTime === null) {
            pad.dwellStartTime = now;
            pad.lastZ = fingertip.z;
        } else {
            const dwellDuration = now - pad.dwellStartTime;
            if (dwellDuration >= this.padSettings.dwellTime && pad.lastZ !== null) {
                // Check for retreat (Z increases = away from camera)
                const zDelta = fingertip.z - pad.lastZ; // Positive = away
                if (zDelta > this.padSettings.retreatThreshold) {
                    pad.dwellStartTime = null;
                    pad.lastZ = null;
                    return true;
                }
            }
            pad.lastZ = fingertip.z;
        }
        return false;
    }

    // Algorithm 3: Wiggle (rapid XY movement)
    detectTap_Wiggle(pad, fingertip, now) {
        if (pad.lastXY !== null) {
            const xyDist = Math.hypot(fingertip.x - pad.lastXY.x, fingertip.y - pad.lastXY.y);
            if (xyDist > this.padSettings.wiggleThreshold) {
                pad.lastXY = { x: fingertip.x, y: fingertip.y };
                return true;
            }
        }
        pad.lastXY = { x: fingertip.x, y: fingertip.y };
        return false;
    }

    // Algorithm 4: Hybrid (combines Z-velocity + small wiggle)
    detectTap_Hybrid(pad, fingertip, now) {
        let score = 0;

        // Check Z-velocity
        if (pad.lastZ !== null) {
            const zDelta = pad.lastZ - fingertip.z;
            if (zDelta > this.padSettings.zThreshold * 0.5) {
                score += 1;
            }
        }

        // Check wiggle
        if (pad.lastXY !== null) {
            const xyDist = Math.hypot(fingertip.x - pad.lastXY.x, fingertip.y - pad.lastXY.y);
            if (xyDist > this.padSettings.wiggleThreshold * 0.5) {
                score += 1;
            }
        }

        pad.lastZ = fingertip.z;
        pad.lastXY = { x: fingertip.x, y: fingertip.y };

        return score >= 2; // Need both indicators
    }

    detectKnobInteractions() {
        if (!this.leftHand && !this.rightHand) return;

        const hands = [];
        if (this.leftHand) hands.push(this.leftHand);
        if (this.rightHand) hands.push(this.rightHand);

        for (const hand of hands) {
            // Require BOTH thumb and index finger for pinch control
            const thumb = hand.fingertips[0];
            const index = hand.fingertips[1];

            for (const knob of this.knobs) {
                // Check if both fingers are inside knob area
                const thumbDist = Math.sqrt(
                    Math.pow(thumb.x - knob.x, 2) +
                    Math.pow(thumb.y - knob.y, 2)
                );
                const indexDist = Math.sqrt(
                    Math.pow(index.x - knob.x, 2) +
                    Math.pow(index.y - knob.y, 2)
                );

                // Both fingers must be within the knob radius
                if (thumbDist < knob.radius && indexDist < knob.radius) {
                    // Calculate pinch center (midpoint between thumb and index)
                    const pinchX = (thumb.x + index.x) / 2;
                    const pinchY = (thumb.y + index.y) / 2;

                    // Calculate angle from knob center to pinch center
                    const dx = pinchX - knob.x;
                    const dy = pinchY - knob.y;
                    const angle = Math.atan2(dy, dx);

                    // Map angle to value (0-1)
                    // Start at bottom (-π/2) and rotate clockwise
                    const startAngle = -Math.PI / 2;
                    const normalizedAngle = ((angle - startAngle + 2 * Math.PI) % (2 * Math.PI)) / (2 * Math.PI);
                    knob.value = Math.max(0, Math.min(1, normalizedAngle));

                    this.activeKnob = knob;
                    break;
                } else {
                    // Reset active knob if fingers leave
                    if (this.activeKnob === knob) {
                        this.activeKnob = null;
                    }
                }
            }
        }
    }

    applyKnobParameters() {
        const now = this.audioContext.currentTime;

        for (const knob of this.knobs) {
            switch (knob.param) {
                case 'filter':
                    const filterFreq = 200 + knob.value * 3800;
                    this.filterNode.frequency.linearRampToValueAtTime(filterFreq, now + 0.1);
                    break;
                case 'reverb':
                    // Can't easily change reverb, but could implement dry/wet mix
                    break;
                case 'delay':
                    const delayMix = knob.value * 0.7;
                    this.delayGain.gain.linearRampToValueAtTime(delayMix, now + 0.1);
                    break;
                case 'resonance':
                    const resonance = 0.1 + knob.value * 19.9; // Q: 0.1-20
                    this.filterNode.Q.linearRampToValueAtTime(resonance, now + 0.1);
                    break;
            }
        }
    }

    playHandSounds(hand, prevHand, delay) {
        for (let i = 0; i < hand.fingertips.length; i++) {
            const curr = hand.fingertips[i];
            const prev = prevHand.fingertips.find(f => f.fingerIndex === i);

            if (prev) {
                const dx = curr.x - prev.x;
                const dy = curr.y - prev.y;
                const velocity = Math.sqrt(dx * dx + dy * dy);

                if (velocity > this.settings.minVelocityForSound) {
                    const freq = 200 + (curr.x / this.canvas.width) * 600;
                    const volume = Math.min(0.15, velocity / 100);

                    setTimeout(() => {
                        this.playBloop(freq, volume);
                    }, delay + i * 30);
                }
            }
        }
    }

    playTouchingSound() {
        // Harmonic chord when fingers are touching
        const baseFreq = 300 + (this.handsDistance / 200) * 200;
        const volumes = [0.12, 0.08, 0.06];
        const harmonics = [1, 1.5, 2]; // Root, fifth, octave

        for (let i = 0; i < harmonics.length; i++) {
            setTimeout(() => {
                this.playBloop(baseFreq * harmonics[i], volumes[i]);
            }, i * 20);
        }
    }

    playBloop(frequency, volume = 0.15) {
        if (!this.audioEnabled || this.isMuted || !this.audioContext) {
            return;
        }

        if (this.audioContext.state === 'suspended') {
            this.audioContext.resume();
            return;
        }

        const now = this.audioContext.currentTime;

        try {
            const osc = this.audioContext.createOscillator();
            const gain = this.audioContext.createGain();

            osc.type = 'sine';
            osc.frequency.setValueAtTime(frequency, now);
            osc.frequency.exponentialRampToValueAtTime(frequency * 0.7, now + 0.5);

            gain.gain.setValueAtTime(0, now);
            gain.gain.linearRampToValueAtTime(volume, now + 0.04);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);

            osc.connect(gain);
            gain.connect(this.filterNode);

            osc.start(now);
            osc.stop(now + 0.5);
        } catch (error) {
            console.error('Error playing sound:', error);
        }
    }

    playChord(x, y) {
        const baseFreq = 200 + (x / this.canvas.width) * 400;
        const chord = [1, 1.25, 1.5]; // Major chord

        for (let i = 0; i < chord.length; i++) {
            setTimeout(() => {
                this.playBloop(baseFreq * chord[i], 0.2);
            }, i * 50);
        }
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

        // VISUALIZATION SYSTEM - Update and render based on current viz mode
        if (this.visualizationMode === 1) {
            this.updateParticles();
            this.renderParticles();
        } else if (this.visualizationMode === 2) {
            this.updateAudioBlooms();
            this.renderAudioBlooms();
        } else if (this.visualizationMode === 3) {
            this.renderFluidDynamics();
        } else if (this.visualizationMode === 4) {
            this.renderGravitationalOrbits();
        } else if (this.visualizationMode === 5) {
            this.renderKaleidoscope();
        } else if (this.visualizationMode === 6) {
            this.updateHandHistory();
            this.renderTemporalEchoes();
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

        // Draw mode indicator
        this.drawModeIndicator();

        // Draw gesture hold progress indicator
        if (this.gestureInProgress && this.gestureHoldStartTime > 0) {
            this.drawGestureHoldProgress();
        }

        // Draw mode switch animation (celebratory visual burst)
        if (this.modeSwitchAnimation.active) {
            this.drawModeSwitchAnimation();
        }

        // Debug overlay
        if (this.debugMode && this.handResults && this.handResults.multiHandLandmarks) {
            this.drawDebugSkeleton();
        }
    }

    renderRibbonsMode() {
        // Draw special effect when hands are touching
        if (this.handsAreTouching && this.touchingFingers.length > 0) {
            this.drawTouchingEffect();
        }

        // Draw fluid silk ribbons for each finger
        for (const fingerId in this.fingerTrails) {
            const trail = this.fingerTrails[fingerId];
            if (trail.length < 3) continue;

            // Determine color based on finger ID
            const parts = fingerId.split('_');
            const handedness = parts[0];
            const fingerIndex = parseInt(parts[1].replace('finger', ''));

            this.drawFluidRibbon(trail, fingerIndex, handedness);
        }

        // Draw fingertip markers
        if (this.leftHand) {
            this.drawFingertipMarkers(this.leftHand);
        }
        if (this.rightHand) {
            this.drawFingertipMarkers(this.rightHand);
        }
    }

    renderThereminMode() {
        const hand = this.leftHand || this.rightHand;

        if (!hand) return;

        // Draw pitch indicator (vertical lines showing scale notes)
        this.drawScaleGuide();

        // Draw hand position with frequency visualization
        const normalizedX = hand.palm.x / this.canvas.width;
        const normalizedY = hand.palm.y / this.canvas.height;

        // Draw horizontal line showing pitch
        this.ctx.strokeStyle = 'rgba(100, 200, 255, 0.7)';
        this.ctx.lineWidth = 3;
        this.ctx.beginPath();
        this.ctx.moveTo(0, hand.palm.y);
        this.ctx.lineTo(this.canvas.width, hand.palm.y);
        this.ctx.stroke();

        // Draw vertical line showing filter
        this.ctx.strokeStyle = 'rgba(255, 200, 100, 0.7)';
        this.ctx.lineWidth = 3;
        this.ctx.beginPath();
        this.ctx.moveTo(hand.palm.x, 0);
        this.ctx.lineTo(hand.palm.x, this.canvas.height);
        this.ctx.stroke();

        // Draw glow at palm center
        const gradient = this.ctx.createRadialGradient(
            hand.palm.x, hand.palm.y, 0,
            hand.palm.x, hand.palm.y, 100
        );
        gradient.addColorStop(0, 'rgba(255, 255, 255, 0.8)');
        gradient.addColorStop(0.5, 'rgba(100, 200, 255, 0.4)');
        gradient.addColorStop(1, 'rgba(100, 200, 255, 0)');

        this.ctx.fillStyle = gradient;
        this.ctx.beginPath();
        this.ctx.arc(hand.palm.x, hand.palm.y, 100, 0, Math.PI * 2);
        this.ctx.fill();

        // Draw fingertips
        this.drawFingertipMarkers(hand);

        // Show current note and frequency
        const freq = this.quantizeToScale(normalizedX);
        this.ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
        this.ctx.font = '24px monospace';
        this.ctx.fillText(`${freq.toFixed(1)} Hz`, hand.palm.x + 20, hand.palm.y - 20);
        this.ctx.fillText(`Scale: ${this.currentScale.toUpperCase()}`, 20, this.canvas.height - 40);
    }

    drawScaleGuide() {
        const scale = this.scales[this.currentScale];
        const octaveRange = 3;

        for (let octave = -1; octave <= octaveRange - 1; octave++) {
            for (const degree of scale) {
                const midiNote = this.rootNote + (octave * 12) + degree;
                const freq = this.midiToFreq(midiNote);

                // Map frequency to X position (approximately)
                const minFreq = this.midiToFreq(this.rootNote - 12);
                const maxFreq = this.midiToFreq(this.rootNote - 12 + (octaveRange * 12));
                const x = ((freq - minFreq) / (maxFreq - minFreq)) * this.canvas.width;

                // Draw vertical line for scale note
                this.ctx.strokeStyle = 'rgba(100, 100, 150, 0.2)';
                this.ctx.lineWidth = 1;
                this.ctx.beginPath();
                this.ctx.moveTo(x, 0);
                this.ctx.lineTo(x, this.canvas.height);
                this.ctx.stroke();
            }
        }
    }

    renderPadsMode() {
        // Draw arc guides showing finger paths (subtle)
        const centerX = this.canvas.width / 2;
        const centerY = this.canvas.height * 0.7;

        for (let finger = 0; finger < 5; finger++) {
            const radius = 200 + (finger * 35);
            this.ctx.strokeStyle = `rgba(100, 100, 150, 0.15)`;
            this.ctx.lineWidth = 1;
            this.ctx.setLineDash([5, 5]);
            this.ctx.beginPath();
            this.ctx.arc(centerX, centerY, radius, -Math.PI * 0.8, -Math.PI * 0.2);
            this.ctx.stroke();
            this.ctx.setLineDash([]);
        }

        // Draw sample pads in arc layout
        for (const pad of this.pads) {
            const alpha = pad.triggered ? 1.0 : 0.5;
            const size = pad.triggered ? pad.size * 1.2 : pad.size;

            // Draw circular pads instead of squares for better visibility
            this.ctx.save();

            // Pad background (circle)
            this.ctx.fillStyle = `rgba(${pad.color.r}, ${pad.color.g}, ${pad.color.b}, ${alpha * 0.3})`;
            this.ctx.beginPath();
            this.ctx.arc(pad.centerX, pad.centerY, size / 2, 0, Math.PI * 2);
            this.ctx.fill();

            // Pad border (circle)
            this.ctx.strokeStyle = `rgba(${pad.color.r}, ${pad.color.g}, ${pad.color.b}, ${alpha})`;
            this.ctx.lineWidth = 3;
            this.ctx.beginPath();
            this.ctx.arc(pad.centerX, pad.centerY, size / 2, 0, Math.PI * 2);
            this.ctx.stroke();

            // Glow effect when triggered
            if (pad.triggered) {
                this.ctx.shadowBlur = 30;
                this.ctx.shadowColor = `rgba(${pad.color.r}, ${pad.color.g}, ${pad.color.b}, 0.8)`;
                this.ctx.beginPath();
                this.ctx.arc(pad.centerX, pad.centerY, size / 2, 0, Math.PI * 2);
                this.ctx.stroke();
            }

            // Pad label
            this.ctx.shadowBlur = 0;
            this.ctx.fillStyle = `rgba(255, 255, 255, ${alpha})`;
            this.ctx.font = '11px monospace';
            this.ctx.textAlign = 'center';
            this.ctx.textBaseline = 'middle';
            this.ctx.fillText(pad.type, pad.centerX, pad.centerY);

            this.ctx.restore();
        }

        // Draw hand fingertips
        if (this.leftHand) {
            this.drawFingertipMarkers(this.leftHand);
        }
        if (this.rightHand) {
            this.drawFingertipMarkers(this.rightHand);
        }

        // Draw instructions
        this.ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
        this.ctx.font = '16px monospace';
        this.ctx.textAlign = 'center';
        this.ctx.textBaseline = 'top';
        this.ctx.fillText('Tap pads with corresponding finger', this.canvas.width / 2, 20);

        this.ctx.textAlign = 'left';
        this.ctx.textBaseline = 'alphabetic';
    }

    drawKnobs() {
        // Draw virtual knobs (global controls, always visible)
        for (const knob of this.knobs) {
            // Knob background circle
            this.ctx.fillStyle = 'rgba(50, 50, 60, 0.7)';
            this.ctx.beginPath();
            this.ctx.arc(knob.x, knob.y, knob.radius, 0, Math.PI * 2);
            this.ctx.fill();

            // Knob ring
            this.ctx.strokeStyle = 'rgba(100, 150, 200, 0.6)';
            this.ctx.lineWidth = 2;
            this.ctx.beginPath();
            this.ctx.arc(knob.x, knob.y, knob.radius, 0, Math.PI * 2);
            this.ctx.stroke();

            // Value indicator (arc from bottom)
            const startAngle = Math.PI * 0.75; // Start at 135 degrees
            const endAngle = startAngle + (knob.value * Math.PI * 1.5); // 270 degree range

            this.ctx.strokeStyle = 'rgba(100, 200, 255, 0.9)';
            this.ctx.lineWidth = 4;
            this.ctx.beginPath();
            this.ctx.arc(knob.x, knob.y, knob.radius - 8, startAngle, endAngle);
            this.ctx.stroke();

            // Knob pointer
            const pointerAngle = startAngle + (knob.value * Math.PI * 1.5);
            const pointerX = knob.x + Math.cos(pointerAngle) * (knob.radius - 10);
            const pointerY = knob.y + Math.sin(pointerAngle) * (knob.radius - 10);

            this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.9)';
            this.ctx.lineWidth = 3;
            this.ctx.lineCap = 'round';
            this.ctx.beginPath();
            this.ctx.moveTo(knob.x, knob.y);
            this.ctx.lineTo(pointerX, pointerY);
            this.ctx.stroke();

            // Knob label (smaller for overlay)
            this.ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
            this.ctx.font = '11px monospace';
            this.ctx.textAlign = 'center';
            this.ctx.textBaseline = 'middle';
            this.ctx.fillText(knob.label, knob.x, knob.y + knob.radius + 15);
        }

        this.ctx.textAlign = 'left';
        this.ctx.textBaseline = 'alphabetic';
    }

    drawModeIndicator() {
        this.ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
        this.ctx.font = '18px monospace';
        this.ctx.textAlign = 'left';
        this.ctx.textBaseline = 'top';

        const modeText = `Mode: ${this.mode.toUpperCase()}`;
        this.ctx.fillText(modeText, 20, 20);

        if (this.mode === 'theremin') {
            this.ctx.fillText(`Scale: ${this.currentScale}`, 20, 50);
        }

        this.ctx.textAlign = 'left';
        this.ctx.textBaseline = 'alphabetic';
    }

    drawGestureHoldProgress() {
        // Show circular progress indicator around hand position
        if (!this.leftHand || !this.leftHand.palm) return;

        const now = Date.now();
        const elapsed = now - this.gestureHoldStartTime;
        const progress = Math.min(elapsed / this.gestureHoldRequired, 1.0);

        const centerX = this.leftHand.palm.x;
        const centerY = this.leftHand.palm.y;
        const radius = 80;

        // Background circle
        this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
        this.ctx.lineWidth = 8;
        this.ctx.beginPath();
        this.ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
        this.ctx.stroke();

        // Progress arc
        this.ctx.strokeStyle = `rgba(100, 255, 150, ${0.5 + progress * 0.5})`;
        this.ctx.lineWidth = 10;
        this.ctx.lineCap = 'round';
        this.ctx.beginPath();
        this.ctx.arc(centerX, centerY, radius, -Math.PI / 2, -Math.PI / 2 + (progress * Math.PI * 2));
        this.ctx.stroke();

        // Gesture indicator text
        const gestureNames = { 1: '1 FINGER', 2: 'PEACE', 5: 'OPEN HAND' };
        const gestureName = gestureNames[this.currentGestureFingerCount] || '';

        this.ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
        this.ctx.font = 'bold 16px monospace';
        this.ctx.textAlign = 'center';
        this.ctx.textBaseline = 'middle';
        this.ctx.fillText(gestureName, centerX, centerY - 5);

        const pct = Math.round(progress * 100);
        this.ctx.font = '14px monospace';
        this.ctx.fillText(`${pct}%`, centerX, centerY + 15);

        this.ctx.textAlign = 'left';
        this.ctx.textBaseline = 'alphabetic';
    }

    drawModeSwitchAnimation() {
        const now = Date.now();
        const elapsed = now - this.modeSwitchAnimation.startTime;
        const progress = elapsed / this.modeSwitchAnimation.duration;

        if (progress >= 1.0) {
            this.modeSwitchAnimation.active = false;
            return;
        }

        // Burst of colorful particles from center
        const centerX = this.canvas.width / 2;
        const centerY = this.canvas.height / 2;
        const numParticles = 50;

        for (let i = 0; i < numParticles; i++) {
            const angle = (i / numParticles) * Math.PI * 2;
            const distance = progress * 400; // Expand outward
            const x = centerX + Math.cos(angle) * distance;
            const y = centerY + Math.sin(angle) * distance;

            const hue = (this.baseHue + i * 7) % 360;
            const alpha = 1 - progress; // Fade out

            this.ctx.fillStyle = `hsla(${hue}, 100%, 60%, ${alpha})`;
            this.ctx.beginPath();
            this.ctx.arc(x, y, 8 * (1 - progress * 0.5), 0, Math.PI * 2);
            this.ctx.fill();
        }

        // Flash effect
        const flashAlpha = Math.max(0, 0.3 - progress * 0.6);
        this.ctx.fillStyle = `rgba(255, 255, 255, ${flashAlpha})`;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Mode text in center
        if (progress < 0.5) {
            const textAlpha = (0.5 - progress) * 2;
            this.ctx.fillStyle = `rgba(255, 255, 255, ${textAlpha})`;
            this.ctx.font = 'bold 48px monospace';
            this.ctx.textAlign = 'center';
            this.ctx.textBaseline = 'middle';
            this.ctx.fillText(this.mode.toUpperCase(), centerX, centerY);
        }

        this.ctx.textAlign = 'left';
        this.ctx.textBaseline = 'alphabetic';
    }

    // ============================================================
    // PARTICLE SYSTEM (#1) - Particle Fountain
    // ============================================================

    updateParticles() {
        const now = Date.now();

        // Emit particles from fingertips
        this.emitParticles();

        // Build spatial grid for inter-particle forces (only if needed)
        let spatialGrid = null;
        if (this.particleSettings.attraction !== 0 || this.particleSettings.repulsion !== 0) {
            spatialGrid = this.buildSpatialGrid();
        }

        // Update existing particles - use filter for efficient removal
        this.particles = this.particles.filter(p => {
            // Check lifetime
            const age = now - p.birthTime;
            if (age > this.particleSettings.lifetime) {
                return false; // Remove dead particles
            }

            // Apply physics
            // 1. Gravity
            p.vy += this.particleSettings.gravity;

            // 2. Drag
            p.vx *= this.particleSettings.drag;
            p.vy *= this.particleSettings.drag;

            // 3. Turbulence (curl noise for organic swirling)
            if (this.particleSettings.turbulence > 0) {
                const turb = this.curlNoise(p.x * 0.01, p.y * 0.01, this.time * 0.001);
                p.vx += turb.x * this.particleSettings.turbulence;
                p.vy += turb.y * this.particleSettings.turbulence;
            }

            // 4. Inter-particle forces (using spatial grid for O(n) instead of O(n²))
            if (spatialGrid) {
                this.applyInterParticleForcesFast(p, spatialGrid);
            }

            // Update position
            p.x += p.vx;
            p.y += p.vy;

            // Update trail history (only if needed)
            if (this.particleSettings.trails) {
                if (!p.trail) p.trail = [];
                p.trail.push({ x: p.x, y: p.y });
                if (p.trail.length > 10) p.trail.shift();
            }

            // Bounce off edges (optional - creates interesting contained effect)
            if (p.x < 0) {
                p.x = 0;
                p.vx *= -0.5;
            }
            if (p.x > this.canvas.width) {
                p.x = this.canvas.width;
                p.vx *= -0.5;
            }
            if (p.y > this.canvas.height) {
                p.y = this.canvas.height;
                p.vy *= -0.5;
            }

            return true; // Keep particle
        });
    }

    emitParticles() {
        // Don't emit if no hands detected
        if (!this.leftHand && !this.rightHand) return;

        // Limit total particles for performance
        if (this.particles.length >= this.maxParticles) return;

        const now = Date.now();

        // TIME-BASED EMISSION (not frame-based!)
        // Calculate how much time has passed since last emission
        if (this.lastParticleEmitTime === 0) {
            this.lastParticleEmitTime = now;
            return; // Skip first frame to establish timing
        }

        const deltaTime = now - this.lastParticleEmitTime;
        this.lastParticleEmitTime = now;

        const hands = [];
        if (this.leftHand) hands.push(this.leftHand);
        if (this.rightHand) hands.push(this.rightHand);

        for (const hand of hands) {
            if (!hand.fingertips) continue;

            for (const fingertip of hand.fingertips) {
                // Calculate finger velocity for initial particle velocity
                let velX = 0, velY = 0;
                const prevHand = hand === this.leftHand ? this.prevLeftHand : this.prevRightHand;
                if (prevHand && prevHand.fingertips[fingertip.fingerIndex]) {
                    const prev = prevHand.fingertips[fingertip.fingerIndex];
                    velX = (fingertip.x - prev.x);
                    velY = (fingertip.y - prev.y);
                }

                // Calculate particles to emit based on TIME (not frames!)
                // emissionRate is particles per SECOND, convert to particles this frame
                const particlesToEmit = (this.particleSettings.emissionRate * deltaTime) / 1000;
                const numToEmit = Math.floor(particlesToEmit);

                for (let e = 0; e < numToEmit; e++) {
                    if (this.particles.length >= this.maxParticles) break;

                    // Randomize initial position slightly around fingertip
                    const spread = 2;
                    const px = fingertip.x + (Math.random() - 0.5) * spread;
                    const py = fingertip.y + (Math.random() - 0.5) * spread;

                    // Initial velocity = finger movement + random spread
                    const angle = Math.random() * Math.PI * 2;
                    const speed = this.particleSettings.initialVelocity;
                    const randomVel = 0.2;

                    const particle = {
                        x: px,
                        y: py,
                        vx: velX * speed + Math.cos(angle) * randomVel,
                        vy: velY * speed + Math.sin(angle) * randomVel,
                        birthTime: now,
                        size: this.particleSettings.particleSizeMin +
                              Math.random() * (this.particleSettings.particleSizeMax - this.particleSettings.particleSizeMin),
                        hue: this.baseHue + fingertip.fingerIndex * 30, // Color per finger
                        fingerIndex: fingertip.fingerIndex,
                        trail: []
                    };

                    this.particles.push(particle);
                }
            }
        }
    }

    renderParticles() {
        const now = Date.now();

        // Apply blend mode for different visual effects
        const blendModeMap = {
            'normal': 'source-over',
            'additive': 'lighter',
            'screen': 'screen',
            'multiply': 'multiply'
        };
        this.ctx.globalCompositeOperation = blendModeMap[this.particleSettings.blendMode] || 'source-over';

        // OPTIMIZATION: Batch all particles into a single path
        // Apply glow once instead of per-particle
        if (this.particleSettings.glow) {
            this.ctx.shadowBlur = 8;
            this.ctx.shadowColor = 'rgba(255, 255, 255, 0.5)';
        }

        // Draw trails first (if enabled) - batched by color
        if (this.particleSettings.trails) {
            for (const p of this.particles) {
                if (!p.trail || p.trail.length < 2) continue;

                const age = now - p.birthTime;
                const lifeProgress = age / this.particleSettings.lifetime;
                const lifetimeAlpha = 1 - Math.pow(lifeProgress, 2);
                const alpha = lifetimeAlpha * this.particleSettings.alpha;

                const { hue, saturation, lightness } = this.getParticleColor(p, lifeProgress, now);

                this.ctx.strokeStyle = `hsla(${hue}, ${saturation}%, ${lightness}%, ${alpha * 0.3})`;
                this.ctx.lineWidth = p.size * 0.5;
                this.ctx.beginPath();
                this.ctx.moveTo(p.trail[0].x, p.trail[0].y);
                for (let i = 1; i < p.trail.length; i++) {
                    this.ctx.lineTo(p.trail[i].x, p.trail[i].y);
                }
                this.ctx.stroke();
            }
        }

        // Draw particles - batch by similar properties for better performance
        // Group particles to minimize state changes
        this.ctx.beginPath();
        for (const p of this.particles) {
            this.ctx.moveTo(p.x + p.size, p.y);
            this.ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        }

        // Fill all particles at once with gradient or single color
        // For best performance, use single color mode
        if (this.particleSettings.colorMode === 'rainbow' || this.particleSettings.colorMode === 'audio') {
            // Single color fill for all particles (fastest)
            const baseColor = this.getParticleColor(this.particles[0] || { hue: this.baseHue }, 0.5, now);
            this.ctx.fillStyle = `hsla(${baseColor.hue}, ${baseColor.saturation}%, ${baseColor.lightness}%, ${this.particleSettings.alpha})`;
            this.ctx.fill();
        } else {
            // Individual coloring (slower but more dynamic)
            for (const p of this.particles) {
                const age = now - p.birthTime;
                const lifeProgress = age / this.particleSettings.lifetime;
                const lifetimeAlpha = 1 - Math.pow(lifeProgress, 2);
                const alpha = lifetimeAlpha * this.particleSettings.alpha;

                const { hue, saturation, lightness } = this.getParticleColor(p, lifeProgress, now);

                this.ctx.fillStyle = `hsla(${hue}, ${saturation}%, ${lightness}%, ${alpha})`;
                this.ctx.beginPath();
                this.ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }

        // Reset shadow and blend mode
        this.ctx.shadowBlur = 0;
        this.ctx.globalCompositeOperation = 'source-over';
    }

    getParticleColor(p, lifeProgress, now) {
        let hue, saturation, lightness;

        switch (this.particleSettings.colorMode) {
            case 'velocity':
                const speed = Math.sqrt(p.vx * p.vx + p.vy * p.vy);
                hue = (this.baseHue + speed * 20) % 360;
                saturation = 70 + Math.min(speed * 3, 20);
                lightness = 50 + Math.min(speed * 2, 20);
                break;

            case 'lifetime':
                hue = (p.hue + lifeProgress * 120) % 360;
                saturation = 80;
                lightness = 60;
                break;

            case 'audio':
                // React to audio (filter frequency affects hue)
                const filterFreq = this.knobs[0] ? this.knobs[0].value : 0.5;
                hue = (this.baseHue + filterFreq * 180) % 360;
                saturation = 85;
                lightness = 55;
                break;

            case 'rainbow':
            default:
                hue = (p.hue + this.time * 0.05) % 360;
                saturation = 90;
                lightness = 60;
                break;
        }

        return { hue, saturation, lightness };
    }

    buildSpatialGrid() {
        // Spatial hashing for O(n) particle interactions instead of O(n²)
        const cellSize = 100; // Same as max interaction distance
        const grid = new Map();

        for (const p of this.particles) {
            const cellX = Math.floor(p.x / cellSize);
            const cellY = Math.floor(p.y / cellSize);
            const key = `${cellX},${cellY}`;

            if (!grid.has(key)) {
                grid.set(key, []);
            }
            grid.get(key).push(p);
        }

        return { grid, cellSize };
    }

    applyInterParticleForcesFast(particle, spatialGrid) {
        const { grid, cellSize } = spatialGrid;
        const maxDistance = 100;

        // Only check particles in neighboring cells
        const cellX = Math.floor(particle.x / cellSize);
        const cellY = Math.floor(particle.y / cellSize);

        // Check 9 cells (current + 8 neighbors)
        for (let dx = -1; dx <= 1; dx++) {
            for (let dy = -1; dy <= 1; dy++) {
                const key = `${cellX + dx},${cellY + dy}`;
                const neighbors = grid.get(key);
                if (!neighbors) continue;

                for (const other of neighbors) {
                    if (other === particle) continue;

                    const dx = other.x - particle.x;
                    const dy = other.y - particle.y;
                    const distSq = dx * dx + dy * dy;

                    if (distSq < maxDistance * maxDistance && distSq > 0.1) {
                        const dist = Math.sqrt(distSq);
                        const force = (this.particleSettings.attraction - this.particleSettings.repulsion / dist);
                        const fx = (dx / dist) * force * 0.01; // Scale down for stability
                        const fy = (dy / dist) * force * 0.01;

                        particle.vx += fx;
                        particle.vy += fy;
                    }
                }
            }
        }
    }

    // Legacy method - kept for compatibility but not used
    applyInterParticleForces(particle, currentIndex) {
        // DEPRECATED: This O(n²) method replaced by applyInterParticleForcesFast
        // Only check nearby particles for performance
        const maxDistance = 100;

        for (let i = 0; i < this.particles.length; i++) {
            if (i === currentIndex) continue;

            const other = this.particles[i];
            const dx = other.x - particle.x;
            const dy = other.y - particle.y;
            const distSq = dx * dx + dy * dy;
            const dist = Math.sqrt(distSq);

            if (dist < maxDistance && dist > 0.1) {
                const force = (this.particleSettings.attraction - this.particleSettings.repulsion / dist);
                const fx = (dx / dist) * force;
                const fy = (dy / dist) * force;

                particle.vx += fx;
                particle.vy += fy;
            }
        }
    }

    // Simpli curl noise for organic turbulence
    curlNoise(x, y, t) {
        // Simple Perlin-like noise approximation using sin waves
        const noise = (x, y) => {
            return Math.sin(x * 1.3 + t) * Math.cos(y * 1.7 + t) +
                   Math.sin(x * 2.1 - t * 0.5) * Math.cos(y * 2.3 - t * 0.5);
        };

        // Calculate curl (rotation) of noise field
        const eps = 0.1;
        const n = noise(x, y);
        const nx = noise(x + eps, y);
        const ny = noise(x, y + eps);

        // Curl = (dN/dy, -dN/dx)
        return {
            x: (ny - n) / eps,
            y: -(nx - n) / eps
        };
    }

    // ============================================================
    // END PARTICLE SYSTEM
    // ============================================================

    // ============================================================
    // TEMPORAL ECHOES SYSTEM (#6) - Ghost Images / Motion Blur
    // ============================================================

    updateHandHistory() {
        // Capture current hand state
        if (this.leftHand || this.rightHand) {
            const snapshot = {
                timestamp: Date.now(),
                leftHand: this.leftHand ? this.copyHandState(this.leftHand) : null,
                rightHand: this.rightHand ? this.copyHandState(this.rightHand) : null
            };

            this.handHistory.push(snapshot);

            // Limit history length
            if (this.handHistory.length > this.maxHistoryLength) {
                this.handHistory.shift();
            }
        }
    }

    copyHandState(hand) {
        return {
            palm: { x: hand.palm.x, y: hand.palm.y },
            fingertips: hand.fingertips.map(ft => ({
                x: ft.x,
                y: ft.y,
                fingerIndex: ft.fingerIndex
            }))
        };
    }

    renderTemporalEchoes() {
        if (this.handHistory.length < 2) return;

        const now = Date.now();
        const spacing = this.echoSettings.echoSpacing;
        const trailLength = Math.min(this.echoSettings.trailLength, this.handHistory.length);

        // Enable glow effect
        if (this.echoSettings.glowIntensity > 0) {
            this.ctx.shadowBlur = this.echoSettings.glowIntensity;
        }

        // Draw echoes from oldest to newest (so newest is on top)
        for (let i = 0; i < trailLength; i += spacing) {
            const historyIndex = this.handHistory.length - 1 - i;
            if (historyIndex < 0) break;

            const snapshot = this.handHistory[historyIndex];
            const age = i / trailLength; // 0 = newest, 1 = oldest
            const alpha = (1 - age) * (1 - this.echoSettings.fadeSpeed * i);

            if (alpha <= 0) continue;

            // Draw chromatic aberration (RGB separation for dreamy effect)
            const aberration = this.echoSettings.chromaticAberration;

            // Red channel (shifted right/down)
            if (aberration > 0) {
                this.drawHandEcho(snapshot, alpha * 0.6, aberration, 0, 'rgba(255, 100, 100, ');
            }

            // Green channel (center)
            this.drawHandEcho(snapshot, alpha, 0, 0, null);

            // Blue channel (shifted left/up)
            if (aberration > 0) {
                this.drawHandEcho(snapshot, alpha * 0.6, -aberration, 0, 'rgba(100, 100, 255, ');
            }

            // Draw motion blur connections
            if (this.echoSettings.motionBlur && i < trailLength - spacing && historyIndex > 0) {
                const prevSnapshot = this.handHistory[historyIndex - spacing];
                if (prevSnapshot) {
                    this.drawMotionBlurConnections(snapshot, prevSnapshot, alpha * 0.3);
                }
            }
        }

        // Reset shadow
        this.ctx.shadowBlur = 0;
    }

    drawHandEcho(snapshot, alpha, offsetX, offsetY, colorOverride) {
        // Draw left hand echo
        if (snapshot.leftHand && this.echoSettings.showFingers) {
            this.drawHandGhost(snapshot.leftHand, alpha, offsetX, offsetY, colorOverride, 'left');
        }

        // Draw right hand echo
        if (snapshot.rightHand && this.echoSettings.showFingers) {
            this.drawHandGhost(snapshot.rightHand, alpha, offsetX, offsetY, colorOverride, 'right');
        }
    }

    drawHandGhost(hand, alpha, offsetX, offsetY, colorOverride, handedness) {
        if (alpha <= 0) return;

        const s = this.echoSettings;

        // Draw palm if enabled
        if (s.showPalm && hand.palm) {
            const palmX = hand.palm.x + offsetX;
            const palmY = hand.palm.y + offsetY;

            const palmHue = handedness === 'left' ? this.baseHue - 20 : this.baseHue + 20;
            const color = colorOverride || `hsla(${palmHue}, 70%, 60%, `;

            this.ctx.shadowColor = color.replace('(', '(').replace(', ', ', 80%, 60%)');
            this.ctx.fillStyle = color + alpha + ')';
            this.ctx.beginPath();
            this.ctx.arc(palmX, palmY, s.palmSize, 0, Math.PI * 2);
            this.ctx.fill();
        }

        // Draw fingertips
        if (s.showFingers && hand.fingertips) {
            for (const fingertip of hand.fingertips) {
                const x = fingertip.x + offsetX;
                const y = fingertip.y + offsetY;

                const hue = (this.baseHue + fingertip.fingerIndex * 30) % 360;
                const color = colorOverride || `hsla(${hue}, 80%, 60%, `;

                this.ctx.shadowColor = color.replace('(', '(').replace(', ', ', 90%, 70%)');
                this.ctx.fillStyle = color + alpha + ')';
                this.ctx.beginPath();
                this.ctx.arc(x, y, s.fingerSize, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }
    }

    drawMotionBlurConnections(snapshot1, snapshot2, alpha) {
        if (alpha <= 0) return;

        this.ctx.lineWidth = 2;
        this.ctx.lineCap = 'round';

        // Connect left hand fingertips
        if (snapshot1.leftHand && snapshot2.leftHand) {
            for (let i = 0; i < snapshot1.leftHand.fingertips.length; i++) {
                const ft1 = snapshot1.leftHand.fingertips[i];
                const ft2 = snapshot2.leftHand.fingertips[i];

                const hue = (this.baseHue + i * 30) % 360;
                this.ctx.strokeStyle = `hsla(${hue}, 80%, 60%, ${alpha})`;

                this.ctx.beginPath();
                this.ctx.moveTo(ft1.x, ft1.y);
                this.ctx.lineTo(ft2.x, ft2.y);
                this.ctx.stroke();
            }
        }

        // Connect right hand fingertips
        if (snapshot1.rightHand && snapshot2.rightHand) {
            for (let i = 0; i < snapshot1.rightHand.fingertips.length; i++) {
                const ft1 = snapshot1.rightHand.fingertips[i];
                const ft2 = snapshot2.rightHand.fingertips[i];

                const hue = (this.baseHue + i * 30) % 360;
                this.ctx.strokeStyle = `hsla(${hue}, 80%, 60%, ${alpha})`;

                this.ctx.beginPath();
                this.ctx.moveTo(ft1.x, ft1.y);
                this.ctx.lineTo(ft2.x, ft2.y);
                this.ctx.stroke();
            }
        }
    }

    // ============================================================
    // END TEMPORAL ECHOES SYSTEM
    // ============================================================

    // ============================================================
    // AUDIO BLOOM PULSES (#2) - Expanding Waves from Sound
    // ============================================================

    updateAudioBlooms() {
        const now = Date.now();
        const s = this.bloomSettings;

        // Create blooms from fingertip movements
        if (this.leftHand || this.rightHand) {
            const hands = [];
            if (this.leftHand) hands.push(this.leftHand);
            if (this.rightHand) hands.push(this.rightHand);

            for (const hand of hands) {
                if (!hand.fingertips) continue;

                for (const fingertip of hand.fingertips) {
                    // Calculate velocity
                    let velocity = 0;
                    const prevHand = hand === this.leftHand ? this.prevLeftHand : this.prevRightHand;
                    if (prevHand && prevHand.fingertips[fingertip.fingerIndex]) {
                        const prev = prevHand.fingertips[fingertip.fingerIndex];
                        const dx = fingertip.x - prev.x;
                        const dy = fingertip.y - prev.y;
                        velocity = Math.sqrt(dx * dx + dy * dy);
                    }

                    // Create bloom on fast movement (use settings)
                    if (velocity > s.velocityThreshold && now - this.lastBloomTime > s.bloomInterval) {
                        this.blooms.push({
                            x: fingertip.x,
                            y: fingertip.y,
                            birthTime: now,
                            hue: (this.baseHue + fingertip.fingerIndex * 30) % 360,
                            velocity: velocity,
                            fingerIndex: fingertip.fingerIndex
                        });
                        this.lastBloomTime = now;
                    }
                }
            }
        }

        // Remove old blooms (use lifetime setting)
        this.blooms = this.blooms.filter(bloom => now - bloom.birthTime < s.lifetime);
    }

    renderAudioBlooms() {
        const now = Date.now();
        const s = this.bloomSettings;

        this.ctx.shadowBlur = s.glowIntensity;

        for (const bloom of this.blooms) {
            const age = now - bloom.birthTime;
            const progress = age / s.lifetime;

            // Expanding ring with pulse speed
            const radius = Math.pow(progress, s.pulseSpeed) * s.maxRadius;
            const alpha = 1 - progress;

            // Hue shift over lifetime if enabled
            let hue = bloom.hue;
            if (s.colorShift) {
                hue = (bloom.hue + progress * 60) % 360;
            }

            // Draw multiple concentric rings
            for (let i = 0; i < s.ringCount; i++) {
                const ringRadius = radius - i * s.ringSpacing;
                if (ringRadius < 0) continue;

                // Pulsing effect based on velocity
                const pulse = 1 + Math.sin(progress * Math.PI * 4) * 0.1 * (bloom.velocity / 20);
                const finalRadius = ringRadius * pulse;

                this.ctx.shadowColor = `hsl(${hue}, 80%, 60%)`;
                this.ctx.strokeStyle = `hsla(${hue}, 80%, 60%, ${alpha * 0.6})`;
                this.ctx.lineWidth = 3 + i * 0.5; // Vary line width
                this.ctx.beginPath();
                this.ctx.arc(bloom.x, bloom.y, finalRadius, 0, Math.PI * 2);
                this.ctx.stroke();
            }
        }

        this.ctx.shadowBlur = 0;
    }

    // ============================================================
    // FLUID DYNAMICS (#3) - Flowing Smoke Effect
    // ============================================================

    renderFluidDynamics() {
        if (!this.leftHand && !this.rightHand) return;

        const s = this.fluidSettings;
        const hands = [];
        if (this.leftHand) hands.push(this.leftHand);
        if (this.rightHand) hands.push(this.rightHand);

        // Apply trail persistence for smokey effect
        this.ctx.fillStyle = `rgba(0, 0, 0, ${1 - s.trailPersistence})`;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        this.ctx.shadowBlur = 25;

        for (const hand of hands) {
            if (!hand.fingertips) continue;

            for (const fingertip of hand.fingertips) {
                // Calculate velocity
                let velocity = { x: 0, y: 0 };
                let velocityMag = 0;
                const prevHand = hand === this.leftHand ? this.prevLeftHand : this.prevRightHand;
                if (prevHand && prevHand.fingertips[fingertip.fingerIndex]) {
                    const prev = prevHand.fingertips[fingertip.fingerIndex];
                    velocity.x = (fingertip.x - prev.x) * s.velocityInfluence;
                    velocity.y = (fingertip.y - prev.y) * s.velocityInfluence;
                    velocityMag = Math.sqrt(velocity.x * velocity.x + velocity.y * velocity.y);
                }

                // Draw flowing smoke tendrils
                const hue = (this.baseHue + fingertip.fingerIndex * 30) % 360;

                for (let i = 0; i < s.tendrilCount; i++) {
                    // Rotating flow with velocity influence
                    const baseAngle = (i / s.tendrilCount) * Math.PI * 2;
                    const flowAngle = baseAngle + this.time * s.flowSpeed + fingertip.fingerIndex * 0.5;

                    // Pulsing radius
                    const pulse = Math.sin(this.time * 0.003 + i) * s.pulseAmount;
                    const radius = s.tendrilRadius + pulse;

                    // Add velocity offset for flow field effect
                    const x = fingertip.x + Math.cos(flowAngle) * radius + velocity.x * 0.5;
                    const y = fingertip.y + Math.sin(flowAngle) * radius + velocity.y * 0.5;

                    // Draw gradient circle with dynamic opacity
                    const dynamicOpacity = s.opacity * (1 + velocityMag * 0.02);
                    const gradient = this.ctx.createRadialGradient(x, y, 0, x, y, s.gradientSize);
                    gradient.addColorStop(0, `hsla(${hue}, 70%, 60%, ${dynamicOpacity})`);
                    gradient.addColorStop(1, `hsla(${hue}, 70%, 60%, 0)`);

                    this.ctx.fillStyle = gradient;
                    this.ctx.fillRect(x - s.gradientSize, y - s.gradientSize, s.gradientSize * 2, s.gradientSize * 2);
                }

                // Draw connecting wisps between tendrils for more fluid feel
                this.ctx.strokeStyle = `hsla(${hue}, 70%, 60%, ${s.opacity * 0.3})`;
                this.ctx.lineWidth = 2;
                this.ctx.beginPath();
                for (let i = 0; i < s.tendrilCount; i++) {
                    const angle1 = (i / s.tendrilCount) * Math.PI * 2 + this.time * s.flowSpeed;
                    const angle2 = ((i + 1) / s.tendrilCount) * Math.PI * 2 + this.time * s.flowSpeed;
                    const x1 = fingertip.x + Math.cos(angle1) * s.tendrilRadius;
                    const y1 = fingertip.y + Math.sin(angle1) * s.tendrilRadius;
                    const x2 = fingertip.x + Math.cos(angle2) * s.tendrilRadius;
                    const y2 = fingertip.y + Math.sin(angle2) * s.tendrilRadius;

                    if (i === 0) this.ctx.moveTo(x1, y1);
                    this.ctx.lineTo(x2, y2);
                }
                this.ctx.stroke();
            }
        }

        this.ctx.shadowBlur = 0;
    }

    // ============================================================
    // GRAVITATIONAL ORBITS (#4) - Particles Orbit Fingertips
    // ============================================================

    renderGravitationalOrbits() {
        if (!this.leftHand && !this.rightHand) return;

        const s = this.orbitSettings;
        const hands = [];
        if (this.leftHand) hands.push(this.leftHand);
        if (this.rightHand) hands.push(this.rightHand);

        this.ctx.shadowBlur = s.glowIntensity;

        for (const hand of hands) {
            if (!hand.fingertips) continue;

            for (const fingertip of hand.fingertips) {
                const hue = (this.baseHue + fingertip.fingerIndex * 30) % 360;

                // Draw orbiting particles around fingertip
                for (let i = 0; i < s.orbiterCount; i++) {
                    // Variable speed per orbiter for more dynamic feel
                    const speedVar = 1 + (i % 3) * 0.2 - 0.2; // Some faster, some slower
                    const angle = (i / s.orbiterCount) * Math.PI * 2 + this.time * s.orbitSpeed * speedVar + fingertip.fingerIndex;

                    // Add wobble to orbit radius
                    const wobbleAmount = Math.sin(this.time * 0.005 + i) * s.wobble;
                    const wobbledRadius = s.orbitRadius + wobbleAmount;

                    const x = fingertip.x + Math.cos(angle) * wobbledRadius;
                    const y = fingertip.y + Math.sin(angle) * wobbledRadius;

                    // Draw orbital particle with size variation
                    const sizeVar = 1 + Math.sin(this.time * 0.003 + i) * 0.3;
                    this.ctx.shadowColor = `hsl(${hue}, 90%, 70%)`;
                    this.ctx.fillStyle = `hsla(${hue}, 90%, 70%, 0.8)`;
                    this.ctx.beginPath();
                    this.ctx.arc(x, y, s.orbiterSize * sizeVar, 0, Math.PI * 2);
                    this.ctx.fill();

                    // Draw orbital trail if enabled
                    if (s.trailLength > 0) {
                        const trailAngle = angle - s.trailLength;
                        const trailX = fingertip.x + Math.cos(trailAngle) * wobbledRadius;
                        const trailY = fingertip.y + Math.sin(trailAngle) * wobbledRadius;

                        const gradient = this.ctx.createLinearGradient(trailX, trailY, x, y);
                        gradient.addColorStop(0, `hsla(${hue}, 90%, 70%, 0)`);
                        gradient.addColorStop(1, `hsla(${hue}, 90%, 70%, 0.4)`);

                        this.ctx.strokeStyle = gradient;
                        this.ctx.lineWidth = s.orbiterSize * 0.5;
                        this.ctx.beginPath();
                        this.ctx.moveTo(trailX, trailY);
                        this.ctx.lineTo(x, y);
                        this.ctx.stroke();
                    }
                }

                // Draw central "sun" with pulsing
                const sunPulse = 1 + Math.sin(this.time * 0.004) * 0.15;
                this.ctx.shadowColor = `hsl(${hue}, 90%, 80%)`;
                this.ctx.fillStyle = `hsla(${hue}, 90%, 80%, 0.7)`;
                this.ctx.beginPath();
                this.ctx.arc(fingertip.x, fingertip.y, s.sunSize * sunPulse, 0, Math.PI * 2);
                this.ctx.fill();

                // Draw sun corona
                const gradient = this.ctx.createRadialGradient(
                    fingertip.x, fingertip.y, s.sunSize * sunPulse,
                    fingertip.x, fingertip.y, s.sunSize * sunPulse * 1.8
                );
                gradient.addColorStop(0, `hsla(${hue}, 90%, 80%, 0.4)`);
                gradient.addColorStop(1, `hsla(${hue}, 90%, 80%, 0)`);
                this.ctx.fillStyle = gradient;
                this.ctx.beginPath();
                this.ctx.arc(fingertip.x, fingertip.y, s.sunSize * sunPulse * 1.8, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }

        this.ctx.shadowBlur = 0;
    }

    // ============================================================
    // KALEIDOSCOPE SYMMETRY (#5) - Radial Mirroring
    // ============================================================

    renderKaleidoscope() {
        if (!this.leftHand && !this.rightHand) return;

        const s = this.kaleidoscopeSettings;
        const centerX = this.canvas.width / 2;
        const centerY = this.canvas.height / 2;

        // Apply trail persistence
        this.ctx.fillStyle = `rgba(0, 0, 0, ${1 - s.trailPersistence})`;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        this.ctx.save();
        this.ctx.shadowBlur = s.glowIntensity;

        const hands = [];
        if (this.leftHand) hands.push(this.leftHand);
        if (this.rightHand) hands.push(this.rightHand);

        // Auto-rotation offset
        const rotationOffset = this.time * s.rotationSpeed;

        for (const hand of hands) {
            if (!hand.fingertips) continue;

            for (const fingertip of hand.fingertips) {
                const hue = (this.baseHue + fingertip.fingerIndex * 30) % 360;

                // Draw the fingertip reflected around the center with radial symmetry
                for (let sym = 0; sym < s.symmetryCount; sym++) {
                    const angle = (sym / s.symmetryCount) * Math.PI * 2 + rotationOffset;

                    this.ctx.save();
                    this.ctx.translate(centerX, centerY);
                    this.ctx.rotate(angle);
                    this.ctx.translate(-centerX, -centerY);

                    // Pulsing size with audio if enabled
                    let pulseMultiplier = 1;
                    if (s.pulseWithAudio && this.audioContext) {
                        pulseMultiplier = 1 + Math.sin(this.time * 0.005 + fingertip.fingerIndex) * 0.3;
                    }

                    // Draw reflected fingertip with glow
                    this.ctx.shadowColor = `hsl(${hue}, 90%, 70%)`;
                    this.ctx.fillStyle = `hsla(${hue}, 90%, 70%, 0.7)`;
                    this.ctx.beginPath();
                    this.ctx.arc(fingertip.x, fingertip.y, s.fingerSize * pulseMultiplier, 0, Math.PI * 2);
                    this.ctx.fill();

                    // Draw outer ring for more visual interest
                    this.ctx.strokeStyle = `hsla(${hue}, 90%, 80%, 0.5)`;
                    this.ctx.lineWidth = 2;
                    this.ctx.beginPath();
                    this.ctx.arc(fingertip.x, fingertip.y, s.fingerSize * pulseMultiplier * 1.3, 0, Math.PI * 2);
                    this.ctx.stroke();

                    // Draw connecting line to center
                    if (s.lineOpacity > 0) {
                        const gradient = this.ctx.createLinearGradient(centerX, centerY, fingertip.x, fingertip.y);
                        gradient.addColorStop(0, `hsla(${hue}, 80%, 60%, ${s.lineOpacity * 0.5})`);
                        gradient.addColorStop(1, `hsla(${hue}, 80%, 60%, ${s.lineOpacity})`);
                        this.ctx.strokeStyle = gradient;
                        this.ctx.lineWidth = 2;
                        this.ctx.beginPath();
                        this.ctx.moveTo(centerX, centerY);
                        this.ctx.lineTo(fingertip.x, fingertip.y);
                        this.ctx.stroke();
                    }

                    this.ctx.restore();
                }
            }
        }

        // Draw center point if enabled
        if (s.showCenter) {
            const centerPulse = 1 + Math.sin(this.time * 0.003) * 0.2;
            this.ctx.shadowColor = `hsl(${this.baseHue}, 90%, 80%)`;
            this.ctx.fillStyle = `hsla(${this.baseHue}, 90%, 80%, 0.8)`;
            this.ctx.beginPath();
            this.ctx.arc(centerX, centerY, 10 * centerPulse, 0, Math.PI * 2);
            this.ctx.fill();

            // Center glow
            const gradient = this.ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, 25 * centerPulse);
            gradient.addColorStop(0, `hsla(${this.baseHue}, 90%, 80%, 0.5)`);
            gradient.addColorStop(1, `hsla(${this.baseHue}, 90%, 80%, 0)`);
            this.ctx.fillStyle = gradient;
            this.ctx.beginPath();
            this.ctx.arc(centerX, centerY, 25 * centerPulse, 0, Math.PI * 2);
            this.ctx.fill();
        }

        this.ctx.restore();
        this.ctx.shadowBlur = 0;
    }

    // ============================================================
    // END VISUALIZATION MODES
    // ============================================================

    drawFluidRibbon(trail, fingerIndex, handedness) {
        // Draw multiple parallel ribbons with varying width for silk effect
        const numRibbons = this.settings.ribbonOffsets;

        for (let r = 0; r < numRibbons; r++) {
            const offset = (r - Math.floor(numRibbons / 2)) * this.settings.ribbonSpacing;
            const alpha = 1 - (Math.abs(offset) / (numRibbons * this.settings.ribbonSpacing)) * 0.7;

            this.ctx.save();
            this.ctx.globalAlpha = alpha * 0.6;

            // Create smooth curve with varying width
            this.ctx.beginPath();

            for (let i = 0; i < trail.length; i++) {
                const point = trail[i];
                const t = i / trail.length;

                // Get perpendicular offset direction
                let perpX = 0, perpY = 0;
                if (i < trail.length - 1) {
                    const next = trail[i + 1];
                    const dx = next.x - point.x;
                    const dy = next.y - point.y;
                    const len = Math.sqrt(dx * dx + dy * dy);
                    if (len > 0) {
                        perpX = -dy / len * offset;
                        perpY = dx / len * offset;
                    }
                }

                const x = point.x + perpX;
                const y = point.y + perpY;

                if (i === 0) {
                    this.ctx.moveTo(x, y);
                } else {
                    const prev = trail[i - 1];
                    const prevPerpX = perpX;
                    const prevPerpY = perpY;
                    const cpx = (prev.x + prevPerpX + x) / 2;
                    const cpy = (prev.y + prevPerpY + y) / 2;
                    this.ctx.quadraticCurveTo(prev.x + prevPerpX, prev.y + prevPerpY, cpx, cpy);
                }
            }

            // Get color
            const color = this.getColorForFinger(fingerIndex, handedness, this.time * 0.001);

            // Gradient from transparent to solid
            const gradient = this.ctx.createLinearGradient(
                trail[0].x, trail[0].y,
                trail[trail.length - 1].x, trail[trail.length - 1].y
            );

            gradient.addColorStop(0, `rgba(${color.r}, ${color.g}, ${color.b}, 0.05)`);
            gradient.addColorStop(0.5, `rgba(${color.r}, ${color.g}, ${color.b}, 0.5)`);
            gradient.addColorStop(1, `rgba(${color.r}, ${color.g}, ${color.b}, 0.9)`);

            // Varying width based on position in trail
            let widthMultiplier = 1;
            if (this.leftHand && handedness === 'Left') {
                widthMultiplier = 1 + (this.leftHand.fingerSpread / 200);
            } else if (this.rightHand && handedness === 'Right') {
                widthMultiplier = 1 + (this.rightHand.fingerSpread / 200);
            }

            this.ctx.strokeStyle = gradient;
            this.ctx.lineWidth = this.settings.ribbonWidth * widthMultiplier;
            this.ctx.lineCap = 'round';
            this.ctx.lineJoin = 'round';
            this.ctx.shadowBlur = 15;
            this.ctx.shadowColor = `rgba(${color.r}, ${color.g}, ${color.b}, 0.6)`;
            this.ctx.stroke();

            this.ctx.restore();
        }
    }

    drawTouchingEffect() {
        // Draw pulsing glow between touching fingers
        for (const touch of this.touchingFingers) {
            const midX = (touch.left.x + touch.right.x) / 2;
            const midY = (touch.left.y + touch.right.y) / 2;

            const pulse = Math.sin(this.time * 0.005) * 0.3 + 0.7;
            const radius = 30 * pulse;

            const gradient = this.ctx.createRadialGradient(midX, midY, 0, midX, midY, radius);
            gradient.addColorStop(0, 'rgba(255, 255, 200, 0.8)');
            gradient.addColorStop(0.5, 'rgba(200, 150, 255, 0.4)');
            gradient.addColorStop(1, 'rgba(100, 200, 255, 0)');

            this.ctx.fillStyle = gradient;
            this.ctx.beginPath();
            this.ctx.arc(midX, midY, radius, 0, Math.PI * 2);
            this.ctx.fill();
        }
    }

    drawFingertipMarkers(hand) {
        for (const tip of hand.fingertips) {
            const color = this.getColorForFinger(tip.fingerIndex, hand.handedness, this.time * 0.001);
            const spread = hand.fingerSpread;
            const size = 3 + (spread / 200) * 3;

            this.ctx.save();

            // Inner glow
            this.ctx.shadowBlur = 20;
            this.ctx.shadowColor = `rgba(${color.r}, ${color.g}, ${color.b}, 0.8)`;

            this.ctx.fillStyle = `rgba(${color.r}, ${color.g}, ${color.b}, 0.9)`;
            this.ctx.beginPath();
            this.ctx.arc(tip.x, tip.y, size, 0, Math.PI * 2);
            this.ctx.fill();

            // Outer ring
            this.ctx.strokeStyle = `rgba(${color.r}, ${color.g}, ${color.b}, 0.4)`;
            this.ctx.lineWidth = 1.5;
            this.ctx.beginPath();
            this.ctx.arc(tip.x, tip.y, size + 4, 0, Math.PI * 2);
            this.ctx.stroke();

            this.ctx.restore();
        }
    }

    drawDebugSkeleton() {
        for (const landmarks of this.handResults.multiHandLandmarks) {
            const connections = [
                [0, 1], [1, 2], [2, 3], [3, 4],
                [0, 5], [5, 6], [6, 7], [7, 8],
                [0, 9], [9, 10], [10, 11], [11, 12],
                [0, 13], [13, 14], [14, 15], [15, 16],
                [0, 17], [17, 18], [18, 19], [19, 20],
                [5, 9], [9, 13], [13, 17]
            ];

            this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
            this.ctx.lineWidth = 1.5;

            for (const [start, end] of connections) {
                const startPoint = landmarks[start];
                const endPoint = landmarks[end];

                this.ctx.beginPath();
                this.ctx.moveTo((1 - startPoint.x) * this.canvas.width, startPoint.y * this.canvas.height);
                this.ctx.lineTo((1 - endPoint.x) * this.canvas.width, endPoint.y * this.canvas.height);
                this.ctx.stroke();
            }
        }
    }

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
        this.isMuted = !this.isMuted;
        const button = document.getElementById('muteButton');
        button.textContent = this.isMuted ? '🔇' : '🔊';

        if (this.masterGain && this.audioContext) {
            const now = this.audioContext.currentTime;
            this.masterGain.gain.linearRampToValueAtTime(
                this.isMuted ? 0 : 0.25,
                now + 0.1
            );
        }
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
