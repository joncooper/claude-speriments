// Visual Sound Mirror - v5.0 Silk & Symphony Edition
// Sophisticated multi-hand interactions with fluid ribbons and rich audio

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

    resizeCanvas() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    setupEventListeners() {
        window.addEventListener('resize', () => this.resizeCanvas());

        this.canvas.addEventListener('click', (e) => {
            if (this.audioContext && this.audioContext.state === 'suspended') {
                this.audioContext.resume();
            }
            this.playChord(e.clientX, e.clientY);
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

        // Debug overlay
        if (this.debugMode && this.handResults && this.handResults.multiHandLandmarks) {
            this.drawDebugSkeleton();
        }
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
