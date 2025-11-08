// Visual Sound Mirror - v6.0 Music Synthesis Edition
// Interactive music instrument with gesture-controlled synthesis, theremin mode, sample pads, and virtual knobs

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

        // Hand data
        this.leftHand = null;   // { landmarks, fingertips, palm, fingerSpread }
        this.rightHand = null;  // { landmarks, fingertips, palm, fingerSpread }
        this.prevLeftHand = null;
        this.prevRightHand = null;

        // Mode system
        this.mode = 'ribbons'; // 'ribbons', 'theremin', 'pads', 'knobs'
        this.modes = ['ribbons', 'theremin', 'pads', 'knobs'];

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
        this.initPads();

        // Virtual knobs
        this.knobs = [];
        this.initKnobs();
        this.activeKnob = null;

        // Debug mode
        this.debugMode = false;

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
        const padding = 40;
        const gridWidth = 400;
        const gridHeight = 400;
        const startX = this.canvas.width - gridWidth - padding;
        const startY = (this.canvas.height - gridHeight) / 2;
        const padSize = (gridWidth - (this.padGrid.cols + 1) * 10) / this.padGrid.cols;

        // Define drum samples for each pad
        const drumTypes = [
            'kick', 'snare', 'hihat', 'clap',
            'tom1', 'tom2', 'rim', 'cowbell',
            'crash', 'ride', 'perc1', 'perc2',
            'bass', 'chord1', 'chord2', 'lead'
        ];

        for (let row = 0; row < this.padGrid.rows; row++) {
            for (let col = 0; col < this.padGrid.cols; col++) {
                const idx = row * this.padGrid.cols + col;
                this.pads.push({
                    x: startX + col * (padSize + 10) + 10,
                    y: startY + row * (padSize + 10) + 10,
                    size: padSize,
                    type: drumTypes[idx],
                    triggered: false,
                    triggerTime: 0,
                    color: this.getPadColor(drumTypes[idx])
                });
            }
        }
    }

    initKnobs() {
        const padding = 40;
        const knobRadius = 50;
        const knobY = 100;

        this.knobs = [
            { x: padding + 70, y: knobY, radius: knobRadius, value: 0.5, label: 'Filter', param: 'filter', angle: 0 },
            { x: padding + 200, y: knobY, radius: knobRadius, value: 0.3, label: 'Reverb', param: 'reverb', angle: 0 },
            { x: padding + 330, y: knobY, radius: knobRadius, value: 0.4, label: 'Delay', param: 'delay', angle: 0 },
            { x: padding + 460, y: knobY, radius: knobRadius, value: 0.7, label: 'Res', param: 'resonance', angle: 0 }
        ];
    }

    getPadColor(type) {
        const colors = {
            kick: { r: 255, g: 60, b: 60 },
            snare: { r: 60, g: 150, b: 255 },
            hihat: { r: 200, g: 200, b: 60 },
            clap: { r: 255, g: 150, b: 60 },
            tom1: { r: 180, g: 80, b: 200 },
            tom2: { r: 150, g: 100, b: 220 },
            rim: { r: 100, g: 200, b: 150 },
            cowbell: { r: 220, g: 180, b: 100 },
            crash: { r: 200, g: 200, b: 200 },
            ride: { r: 180, g: 180, b: 180 },
            perc1: { r: 100, g: 255, b: 150 },
            perc2: { r: 150, g: 100, b: 255 },
            bass: { r: 80, g: 80, b: 200 },
            chord1: { r: 200, g: 100, b: 100 },
            chord2: { r: 100, g: 200, b: 100 },
            lead: { r: 255, g: 200, b: 100 }
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

        // Keyboard controls for mode switching
        document.addEventListener('keydown', (e) => {
            if (e.key === '1') this.switchMode('ribbons');
            if (e.key === '2') this.switchMode('theremin');
            if (e.key === '3') this.switchMode('pads');
            if (e.key === '4') this.switchMode('knobs');
            if (e.key === 's') this.cycleScale();
        });

        document.getElementById('startButton').addEventListener('click', () => {
            this.start();
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

        // Show status
        const status = document.getElementById('status');
        status.textContent = `Mode: ${newMode.toUpperCase()}`;
        status.classList.add('visible');
        setTimeout(() => status.classList.remove('visible'), 2000);
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
                case 'kick':
                    this.playKick(now);
                    break;
                case 'snare':
                    this.playSnare(now);
                    break;
                case 'hihat':
                    this.playHihat(now);
                    break;
                case 'clap':
                    this.playClap(now);
                    break;
                case 'tom1':
                    this.playTom(now, 120);
                    break;
                case 'tom2':
                    this.playTom(now, 80);
                    break;
                case 'rim':
                    this.playRim(now);
                    break;
                case 'cowbell':
                    this.playCowbell(now);
                    break;
                case 'crash':
                    this.playCrash(now);
                    break;
                case 'ride':
                    this.playRide(now);
                    break;
                case 'perc1':
                    this.playPerc(now, 800);
                    break;
                case 'perc2':
                    this.playPerc(now, 400);
                    break;
                case 'bass':
                    this.playBass(now);
                    break;
                case 'chord1':
                    this.playChordPad(now, [261.63, 329.63, 392.00]); // C major
                    break;
                case 'chord2':
                    this.playChordPad(now, [293.66, 349.23, 440.00]); // D minor
                    break;
                case 'lead':
                    this.playLead(now);
                    break;
            }
        } catch (error) {
            console.error('Error playing drum sample:', error);
        }
    }

    playKick(now) {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();

        osc.frequency.setValueAtTime(150, now);
        osc.frequency.exponentialRampToValueAtTime(40, now + 0.1);

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

    playHihat(now) {
        const bufferSize = this.audioContext.sampleRate * 0.1;
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
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.1);

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

    playRim(now) {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();
        osc.frequency.value = 400;
        osc.type = 'square';

        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.05);

        osc.connect(gain);
        gain.connect(this.masterGain);

        osc.start(now);
        osc.stop(now + 0.05);
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

    playCrash(now) {
        const bufferSize = this.audioContext.sampleRate * 1.5;
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
        gain.gain.exponentialRampToValueAtTime(0.01, now + 1.5);

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

    playBass(now) {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();
        osc.frequency.value = 55; // A1
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

                // Get fingertips
                const fingertipIndices = [4, 8, 12, 16, 20];
                const fingertips = fingertipIndices.map((idx, i) => ({
                    x: (1 - landmarks[idx].x) * this.canvas.width,
                    y: landmarks[idx].y * this.canvas.height,
                    z: landmarks[idx].z,
                    fingerIndex: i,
                    fingerId: `${handedness}_finger${i}`
                }));

                // Calculate palm position
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

    updateDebug() {
        if (!this.debugMode) return;

        const leftSpread = this.leftHand ? this.leftHand.fingerSpread.toFixed(0) : 'N/A';
        const rightSpread = this.rightHand ? this.rightHand.fingerSpread.toFixed(0) : 'N/A';

        document.getElementById('debugMotion').textContent =
            `L: ${leftSpread}px, R: ${rightSpread}px`;
        document.getElementById('debugPosition').textContent =
            `Hands touching: ${this.handsAreTouching ? 'YES' : 'NO'}`;
        document.getElementById('debugParticles').textContent =
            `Touching fingers: ${this.touchingFingers.length}`;
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
        } else if (this.mode === 'knobs') {
            // Knobs mode: detect knob rotation
            this.detectKnobInteractions();

            // Apply knob values to audio parameters
            this.applyKnobParameters();
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

        for (const hand of hands) {
            for (const fingertip of hand.fingertips) {
                for (const pad of this.pads) {
                    const dx = fingertip.x - (pad.x + pad.size / 2);
                    const dy = fingertip.y - (pad.y + pad.size / 2);
                    const dist = Math.sqrt(dx * dx + dy * dy);

                    if (dist < pad.size / 2) {
                        // Fingertip is over pad
                        const now = Date.now();
                        if (!pad.triggered || now - pad.triggerTime > 200) {
                            pad.triggered = true;
                            pad.triggerTime = now;
                            this.playDrumSample(pad.type);
                            console.log(`Triggered pad: ${pad.type}`);
                        }
                    }
                }
            }
        }

        // Reset triggered state after timeout
        const now = Date.now();
        for (const pad of this.pads) {
            if (pad.triggered && now - pad.triggerTime > 100) {
                pad.triggered = false;
            }
        }
    }

    detectKnobInteractions() {
        if (!this.leftHand && !this.rightHand) return;

        const hands = [];
        if (this.leftHand) hands.push(this.leftHand);
        if (this.rightHand) hands.push(this.rightHand);

        for (const hand of hands) {
            // Use index finger for knob control
            const indexFinger = hand.fingertips[1]; // Index is finger 1

            for (const knob of this.knobs) {
                const dx = indexFinger.x - knob.x;
                const dy = indexFinger.y - knob.y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < knob.radius * 1.5) {
                    // Finger is over knob - calculate rotation angle
                    const angle = Math.atan2(dy, dx);
                    knob.angle = angle;

                    // Map angle to value (0-1)
                    // Angle ranges from -π to π, map to 0-1
                    const normalizedAngle = (angle + Math.PI) / (2 * Math.PI);
                    knob.value = normalizedAngle;

                    this.activeKnob = knob;
                    break;
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

        // Mode-specific rendering
        if (this.mode === 'theremin') {
            this.renderThereminMode();
        } else if (this.mode === 'pads') {
            this.renderPadsMode();
        } else if (this.mode === 'knobs') {
            this.renderKnobsMode();
        } else {
            // Ribbons mode: original visualization
            this.renderRibbonsMode();
        }

        // Draw mode indicator
        this.drawModeIndicator();

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
        // Draw sample pad grid
        for (const pad of this.pads) {
            const alpha = pad.triggered ? 1.0 : 0.6;
            const size = pad.triggered ? pad.size * 1.1 : pad.size;
            const x = pad.triggered ? pad.x - (size - pad.size) / 2 : pad.x;
            const y = pad.triggered ? pad.y - (size - pad.size) / 2 : pad.y;

            // Pad background
            this.ctx.fillStyle = `rgba(${pad.color.r}, ${pad.color.g}, ${pad.color.b}, ${alpha * 0.4})`;
            this.ctx.fillRect(x, y, size, size);

            // Pad border
            this.ctx.strokeStyle = `rgba(${pad.color.r}, ${pad.color.g}, ${pad.color.b}, ${alpha})`;
            this.ctx.lineWidth = 2;
            this.ctx.strokeRect(x, y, size, size);

            // Pad label
            this.ctx.fillStyle = `rgba(255, 255, 255, ${alpha})`;
            this.ctx.font = '14px monospace';
            this.ctx.textAlign = 'center';
            this.ctx.textBaseline = 'middle';
            this.ctx.fillText(pad.type, x + size / 2, y + size / 2);
        }

        // Draw hand fingertips
        if (this.leftHand) {
            this.drawFingertipMarkers(this.leftHand);
        }
        if (this.rightHand) {
            this.drawFingertipMarkers(this.rightHand);
        }

        this.ctx.textAlign = 'left';
        this.ctx.textBaseline = 'alphabetic';
    }

    renderKnobsMode() {
        // Draw virtual knobs
        for (const knob of this.knobs) {
            // Knob background circle
            this.ctx.fillStyle = 'rgba(50, 50, 60, 0.8)';
            this.ctx.beginPath();
            this.ctx.arc(knob.x, knob.y, knob.radius, 0, Math.PI * 2);
            this.ctx.fill();

            // Knob ring
            this.ctx.strokeStyle = 'rgba(100, 150, 200, 0.8)';
            this.ctx.lineWidth = 3;
            this.ctx.beginPath();
            this.ctx.arc(knob.x, knob.y, knob.radius, 0, Math.PI * 2);
            this.ctx.stroke();

            // Value indicator (arc from bottom)
            const startAngle = Math.PI * 0.75; // Start at 135 degrees
            const endAngle = startAngle + (knob.value * Math.PI * 1.5); // 270 degree range

            this.ctx.strokeStyle = 'rgba(100, 200, 255, 1.0)';
            this.ctx.lineWidth = 6;
            this.ctx.beginPath();
            this.ctx.arc(knob.x, knob.y, knob.radius - 10, startAngle, endAngle);
            this.ctx.stroke();

            // Knob pointer
            const pointerAngle = startAngle + (knob.value * Math.PI * 1.5);
            const pointerX = knob.x + Math.cos(pointerAngle) * (knob.radius - 15);
            const pointerY = knob.y + Math.sin(pointerAngle) * (knob.radius - 15);

            this.ctx.strokeStyle = 'rgba(255, 255, 255, 1.0)';
            this.ctx.lineWidth = 4;
            this.ctx.lineCap = 'round';
            this.ctx.beginPath();
            this.ctx.moveTo(knob.x, knob.y);
            this.ctx.lineTo(pointerX, pointerY);
            this.ctx.stroke();

            // Knob label
            this.ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
            this.ctx.font = '16px monospace';
            this.ctx.textAlign = 'center';
            this.ctx.textBaseline = 'middle';
            this.ctx.fillText(knob.label, knob.x, knob.y + knob.radius + 25);

            // Value text
            const valuePercent = Math.round(knob.value * 100);
            this.ctx.font = '12px monospace';
            this.ctx.fillText(`${valuePercent}%`, knob.x, knob.y + knob.radius + 45);
        }

        // Draw hand fingertips
        if (this.leftHand) {
            this.drawFingertipMarkers(this.leftHand);
        }
        if (this.rightHand) {
            this.drawFingertipMarkers(this.rightHand);
        }

        this.ctx.textAlign = 'left';
        this.ctx.textBaseline = 'alphabetic';
    }

    drawModeIndicator() {
        this.ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
        this.ctx.font = '18px monospace';
        this.ctx.textAlign = 'left';
        this.ctx.textBaseline = 'top';

        const modeText = `Mode: ${this.mode.toUpperCase()} (Press 1-4 to switch)`;
        this.ctx.fillText(modeText, 20, 20);

        if (this.mode === 'theremin') {
            this.ctx.fillText('Press S to cycle scales', 20, 50);
        }

        this.ctx.textAlign = 'left';
        this.ctx.textBaseline = 'alphabetic';
    }

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

        this.updateAudio();
        this.render();

        if (this.debugMode) {
            this.updateDebug();
        }

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
}

// Initialize when page loads
window.addEventListener('load', () => {
    const app = new VisualSoundMirror();
});
