// Visual Sound Mirror - Fixed and Improved
// An interactive art piece that transforms movement into visuals and sound

class VisualSoundMirror {
    constructor() {
        // Canvas setup
        this.canvas = document.getElementById('canvas');
        this.ctx = this.canvas.getContext('2d');
        this.resizeCanvas();

        // Video setup
        this.video = document.getElementById('video');
        this.videoCanvas = document.createElement('canvas');
        this.videoCtx = this.videoCanvas.getContext('2d');

        // Hand tracking
        this.hands = null;
        this.handResults = null;
        this.camera = null;

        // Motion detection (fallback)
        this.motionData = {
            intensity: 0,
            x: 0.5,
            y: 0.5,
            prevFrame: null
        };

        // Hand positions for tracking
        this.handPositions = [];

        // Particle system
        this.particles = [];
        this.maxParticles = 1000;

        // Audio setup
        this.audioContext = null;
        this.masterGain = null;
        this.audioEnabled = false;
        this.isMuted = false;
        this.lastSoundTime = 0;

        // Debug mode
        this.debugMode = false;

        // Color palette (dreamy, soothing colors)
        this.colors = [
            { r: 147, g: 197, b: 253 }, // Soft blue
            { r: 196, g: 181, b: 253 }, // Lavender
            { r: 252, g: 211, b: 77 },  // Soft yellow
            { r: 134, g: 239, b: 172 }, // Mint green
            { r: 251, g: 146, b: 195 }, // Pink
            { r: 165, g: 180, b: 252 }  // Periwinkle
        ];

        // Settings
        this.settings = {
            motionThreshold: 5,  // Much lower threshold
            particleLifespan: 120,
            soundEnabled: true,
            trailAlpha: 0.15,
            motionSmoothing: 0.5,
            soundInterval: 100  // Minimum ms between sounds
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

        // Click to add particles
        this.canvas.addEventListener('click', (e) => {
            this.createParticleBurst(e.clientX, e.clientY);
            // Play sound on click too
            if (this.audioContext && this.audioContext.state === 'suspended') {
                this.audioContext.resume();
            }
            this.playBloop(400 + Math.random() * 400, 0.3);
        });

        // Start button
        document.getElementById('startButton').addEventListener('click', () => {
            this.start();
        });

        // Mute button
        document.getElementById('muteButton').addEventListener('click', () => {
            this.toggleMute();
        });

        // Debug button
        document.getElementById('debugButton').addEventListener('click', () => {
            this.debugMode = !this.debugMode;
            document.getElementById('debug').classList.toggle('hidden');
        });

        // Info button
        document.getElementById('infoButton').addEventListener('click', () => {
            document.getElementById('info').classList.remove('hidden');
        });

        document.getElementById('closeInfo').addEventListener('click', () => {
            document.getElementById('info').classList.add('hidden');
        });
    }

    async start() {
        try {
            // Hide overlay
            document.getElementById('overlay').classList.add('hidden');

            // Show status
            const status = document.getElementById('status');
            status.textContent = 'Initializing camera...';
            status.classList.add('visible');

            // Initialize audio FIRST (important!)
            status.textContent = 'Initializing audio...';
            await this.initAudio();

            // Initialize camera
            status.textContent = 'Starting camera...';
            await this.initCamera();

            // Initialize hand tracking
            status.textContent = 'Loading hand tracking...';
            await this.initHandTracking();

            status.textContent = 'Ready! Wave your hands!';
            setTimeout(() => status.classList.remove('visible'), 3000);

            // Start animation loop
            this.isRunning = true;
            this.animate(0);

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

        // Wait for video to be ready
        return new Promise((resolve) => {
            this.video.onloadedmetadata = () => {
                this.videoCanvas.width = this.video.videoWidth;
                this.videoCanvas.height = this.video.videoHeight;
                resolve();
            };
        });
    }

    async initAudio() {
        // Create audio context
        this.audioContext = new (window.AudioContext || window.webkitAudioContext)();

        // CRITICAL: Resume audio context on user interaction
        const resumeAudio = async () => {
            if (this.audioContext.state === 'suspended') {
                await this.audioContext.resume();
                console.log('Audio context resumed!');
                this.updateDebug();
            }
        };

        // Try to resume on various user interactions
        document.body.addEventListener('click', resumeAudio, { once: true });
        document.body.addEventListener('touchstart', resumeAudio, { once: true });
        document.body.addEventListener('keydown', resumeAudio, { once: true });

        // Master gain (volume control)
        this.masterGain = this.audioContext.createGain();
        this.masterGain.gain.value = 0.2;  // Start with reasonable volume
        this.masterGain.connect(this.audioContext.destination);

        // Create reverb
        this.reverb = this.createReverb();
        this.reverb.connect(this.masterGain);

        this.audioEnabled = true;

        console.log('Audio initialized. State:', this.audioContext.state);
    }

    createReverb() {
        const convolver = this.audioContext.createConvolver();
        const rate = this.audioContext.sampleRate;
        const length = rate * 2.5;
        const impulse = this.audioContext.createBuffer(2, length, rate);

        for (let channel = 0; channel < 2; channel++) {
            const channelData = impulse.getChannelData(channel);
            for (let i = 0; i < length; i++) {
                channelData[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / length, 2);
            }
        }

        convolver.buffer = impulse;
        return convolver;
    }

    async initHandTracking() {
        // Initialize MediaPipe Hands
        this.hands = new Hands({
            locateFile: (file) => {
                return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
            }
        });

        this.hands.setOptions({
            maxNumHands: 2,
            modelComplexity: 1,
            minDetectionConfidence: 0.5,
            minTrackingConfidence: 0.5
        });

        this.hands.onResults((results) => this.onHandResults(results));

        // Start camera with MediaPipe
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

        // Update hand positions
        this.handPositions = [];

        if (results.multiHandLandmarks) {
            for (const landmarks of results.multiHandLandmarks) {
                // Get palm center (landmark 9 is middle of palm)
                const palm = landmarks[9];

                // Also get fingertips for more interaction points
                const fingertips = [
                    landmarks[4],   // Thumb
                    landmarks[8],   // Index
                    landmarks[12],  // Middle
                    landmarks[16],  // Ring
                    landmarks[20]   // Pinky
                ];

                // Add palm
                this.handPositions.push({
                    x: palm.x * this.canvas.width,
                    y: palm.y * this.canvas.height,
                    z: palm.z,
                    isPalm: true
                });

                // Add fingertips
                for (const tip of fingertips) {
                    this.handPositions.push({
                        x: tip.x * this.canvas.width,
                        y: tip.y * this.canvas.height,
                        z: tip.z,
                        isPalm: false
                    });
                }
            }
        }

        // Calculate motion intensity from hand movement
        if (this.handPositions.length > 0) {
            // Use average hand position
            let totalX = 0, totalY = 0;
            for (const pos of this.handPositions) {
                totalX += pos.x;
                totalY += pos.y;
            }

            const avgX = totalX / this.handPositions.length;
            const avgY = totalY / this.handPositions.length;

            // Calculate movement
            const dx = Math.abs(avgX - this.motionData.x * this.canvas.width);
            const dy = Math.abs(avgY - this.motionData.y * this.canvas.height);
            const movement = Math.sqrt(dx * dx + dy * dy);

            // Update motion data
            const smoothing = this.settings.motionSmoothing;
            this.motionData.x = this.motionData.x * smoothing + (avgX / this.canvas.width) * (1 - smoothing);
            this.motionData.y = this.motionData.y * smoothing + (avgY / this.canvas.height) * (1 - smoothing);
            this.motionData.intensity = Math.min(movement / 100, 1);
        } else {
            // No hands detected, decay motion
            this.motionData.intensity *= 0.9;
        }

        this.updateDebug();
    }

    updateDebug() {
        if (!this.debugMode) return;

        document.getElementById('debugMotion').textContent = this.motionData.intensity.toFixed(3);
        document.getElementById('debugPosition').textContent =
            `${(this.motionData.x * 100).toFixed(1)}%, ${(this.motionData.y * 100).toFixed(1)}%`;
        document.getElementById('debugParticles').textContent = this.particles.length;
        document.getElementById('debugAudio').textContent =
            this.audioContext ? `${this.audioContext.state} (${this.isMuted ? 'muted' : 'active'})` : 'Not initialized';
        document.getElementById('debugHands').textContent =
            this.handResults && this.handResults.multiHandLandmarks ?
            this.handResults.multiHandLandmarks.length : 0;
    }

    updateParticles(deltaTime) {
        // Create particles from hand positions
        if (this.handPositions.length > 0 && this.particles.length < this.maxParticles) {
            for (const handPos of this.handPositions) {
                // More particles for faster movement
                if (Math.random() < this.motionData.intensity * 0.5 + 0.1) {
                    this.createParticle(
                        handPos.x,
                        handPos.y,
                        this.motionData.intensity * 0.5 + 0.3
                    );
                }
            }
        }

        // Fallback: create particles from general motion
        if (this.handPositions.length === 0 && this.motionData.intensity > 0.05 && this.particles.length < this.maxParticles) {
            const numParticles = Math.floor(this.motionData.intensity * 3);
            for (let i = 0; i < numParticles; i++) {
                this.createParticle(
                    this.motionData.x * this.canvas.width,
                    this.motionData.y * this.canvas.height,
                    this.motionData.intensity
                );
            }
        }

        // Update existing particles
        for (let i = this.particles.length - 1; i >= 0; i--) {
            const p = this.particles[i];

            // Update physics
            p.vx += p.ax;
            p.vy += p.ay;
            p.vx *= 0.97;  // Friction
            p.vy *= 0.97;
            p.x += p.vx;
            p.y += p.vy;

            // Update life
            p.life--;
            p.alpha = p.life / this.settings.particleLifespan;

            // Remove dead particles
            if (p.life <= 0) {
                this.particles.splice(i, 1);
            }
        }
    }

    createParticle(x, y, intensity) {
        const color = this.colors[Math.floor(Math.random() * this.colors.length)];
        const angle = Math.random() * Math.PI * 2;
        const speed = intensity * 4 + Math.random() * 3;

        this.particles.push({
            x: x + (Math.random() - 0.5) * 30,
            y: y + (Math.random() - 0.5) * 30,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed,
            ax: 0,
            ay: 0.03,  // Slight gravity
            size: Math.random() * 5 + 2,
            color: color,
            alpha: 1,
            life: this.settings.particleLifespan
        });
    }

    createParticleBurst(x, y) {
        for (let i = 0; i < 40; i++) {
            const angle = (Math.PI * 2 * i) / 40;
            const speed = Math.random() * 6 + 3;
            const color = this.colors[Math.floor(Math.random() * this.colors.length)];

            this.particles.push({
                x: x,
                y: y,
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
                ax: 0,
                ay: 0.02,
                size: Math.random() * 6 + 3,
                color: color,
                alpha: 1,
                life: this.settings.particleLifespan * 1.5
            });
        }
    }

    updateAudio() {
        if (!this.audioEnabled || this.isMuted || !this.audioContext) {
            return;
        }

        // Resume audio context if needed
        if (this.audioContext.state === 'suspended') {
            this.audioContext.resume();
        }

        const now = Date.now();

        // Play bloopy sounds based on hand positions
        if (this.handPositions.length > 0) {
            // Throttle sound generation
            if (now - this.lastSoundTime > this.settings.soundInterval) {
                // Play a sound for each hand/finger detected
                for (let i = 0; i < Math.min(this.handPositions.length, 3); i++) {
                    const pos = this.handPositions[i];
                    const freq = 200 + (pos.x / this.canvas.width) * 600;
                    const volume = 0.1 + this.motionData.intensity * 0.15;

                    // Random delay for polyphonic effect
                    setTimeout(() => {
                        this.playBloop(freq, volume);
                    }, i * 50);
                }

                this.lastSoundTime = now;
            }
        }
    }

    playBloop(frequency, volume = 0.15) {
        if (!this.audioEnabled || this.isMuted || !this.audioContext) {
            return;
        }

        // Make sure audio context is running
        if (this.audioContext.state === 'suspended') {
            console.log('Audio context suspended, attempting to resume...');
            this.audioContext.resume();
            return;
        }

        const now = this.audioContext.currentTime;

        try {
            // Create oscillator
            const osc = this.audioContext.createOscillator();
            const gain = this.audioContext.createGain();
            const filter = this.audioContext.createBiquadFilter();

            // Configure oscillator for bloopy sound
            osc.type = 'sine';
            osc.frequency.setValueAtTime(frequency, now);
            osc.frequency.exponentialRampToValueAtTime(frequency * 0.6, now + 0.4);

            // Configure filter for character
            filter.type = 'lowpass';
            filter.frequency.setValueAtTime(frequency * 2, now);
            filter.Q.setValueAtTime(3, now);

            // Configure envelope (attack-release)
            gain.gain.setValueAtTime(0, now);
            gain.gain.linearRampToValueAtTime(volume, now + 0.03);  // Quick attack
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.4);  // Smooth release

            // Connect nodes
            osc.connect(filter);
            filter.connect(gain);
            gain.connect(this.reverb);

            // Play
            osc.start(now);
            osc.stop(now + 0.4);

            console.log(`Playing bloop at ${frequency.toFixed(0)}Hz, volume ${volume.toFixed(2)}`);
        } catch (error) {
            console.error('Error playing sound:', error);
        }
    }

    render() {
        // Create trail effect
        this.ctx.fillStyle = `rgba(0, 0, 0, ${this.settings.trailAlpha})`;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw hand tracking visualizations (if hands detected)
        if (this.debugMode && this.handResults && this.handResults.multiHandLandmarks) {
            for (const landmarks of this.handResults.multiHandLandmarks) {
                // Draw connections
                this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
                this.ctx.lineWidth = 2;

                // Draw hand skeleton
                const connections = [
                    [0, 1], [1, 2], [2, 3], [3, 4],  // Thumb
                    [0, 5], [5, 6], [6, 7], [7, 8],  // Index
                    [0, 9], [9, 10], [10, 11], [11, 12],  // Middle
                    [0, 13], [13, 14], [14, 15], [15, 16],  // Ring
                    [0, 17], [17, 18], [18, 19], [19, 20],  // Pinky
                    [5, 9], [9, 13], [13, 17]  // Palm
                ];

                for (const [start, end] of connections) {
                    const startPoint = landmarks[start];
                    const endPoint = landmarks[end];

                    this.ctx.beginPath();
                    this.ctx.moveTo(startPoint.x * this.canvas.width, startPoint.y * this.canvas.height);
                    this.ctx.lineTo(endPoint.x * this.canvas.width, endPoint.y * this.canvas.height);
                    this.ctx.stroke();
                }

                // Draw landmarks
                for (const landmark of landmarks) {
                    this.ctx.fillStyle = 'rgba(255, 100, 100, 0.5)';
                    this.ctx.beginPath();
                    this.ctx.arc(
                        landmark.x * this.canvas.width,
                        landmark.y * this.canvas.height,
                        5, 0, Math.PI * 2
                    );
                    this.ctx.fill();
                }
            }
        }

        // Draw particles
        for (const p of this.particles) {
            this.ctx.save();

            // Glow effect
            this.ctx.shadowBlur = 25;
            this.ctx.shadowColor = `rgba(${p.color.r}, ${p.color.g}, ${p.color.b}, ${p.alpha})`;

            // Draw particle
            this.ctx.fillStyle = `rgba(${p.color.r}, ${p.color.g}, ${p.color.b}, ${p.alpha * 0.9})`;
            this.ctx.beginPath();
            this.ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            this.ctx.fill();

            this.ctx.restore();
        }

        // Draw motion indicator circles at hand positions
        for (const pos of this.handPositions) {
            this.ctx.save();
            this.ctx.strokeStyle = pos.isPalm ?
                'rgba(255, 200, 100, 0.6)' :
                'rgba(100, 200, 255, 0.4)';
            this.ctx.lineWidth = 3;
            this.ctx.beginPath();
            this.ctx.arc(pos.x, pos.y, pos.isPalm ? 30 : 15, 0, Math.PI * 2);
            this.ctx.stroke();
            this.ctx.restore();
        }
    }

    animate(timestamp) {
        if (!this.isRunning) return;

        const deltaTime = timestamp - this.lastTime;
        this.lastTime = timestamp;

        // Update systems
        this.updateParticles(deltaTime);
        this.updateAudio();

        // Render
        this.render();

        // Update debug
        if (this.debugMode) {
            this.updateDebug();
        }

        // Continue loop
        requestAnimationFrame((t) => this.animate(t));
    }

    toggleMute() {
        this.isMuted = !this.isMuted;
        const button = document.getElementById('muteButton');
        button.textContent = this.isMuted ? '🔇' : '🔊';

        if (this.masterGain && this.audioContext) {
            const now = this.audioContext.currentTime;
            this.masterGain.gain.linearRampToValueAtTime(
                this.isMuted ? 0 : 0.2,
                now + 0.1
            );
        }
    }
}

// Initialize when page loads
window.addEventListener('load', () => {
    const app = new VisualSoundMirror();
});
