// Visual Sound Mirror - Main Application
// An interactive art piece that transforms movement into visuals and sound

class VisualSoundMirror {
    constructor() {
        // Canvas setup
        this.canvas = document.getElementById('canvas');
        this.ctx = this.canvas.getContext('2d');
        this.resizeCanvas();

        // Video setup for motion detection
        this.video = document.getElementById('video');
        this.videoCanvas = document.createElement('canvas');
        this.videoCtx = this.videoCanvas.getContext('2d');

        // Motion detection
        this.motionData = {
            intensity: 0,
            x: 0.5,
            y: 0.5,
            prevFrame: null
        };

        // Particle system
        this.particles = [];
        this.maxParticles = 500;

        // Audio setup
        this.audioContext = null;
        this.masterGain = null;
        this.oscillators = [];
        this.audioEnabled = false;
        this.isMuted = false;

        // Animation
        this.lastTime = 0;
        this.isRunning = false;

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
            motionThreshold: 15,
            particleLifespan: 180,
            soundEnabled: true,
            trailAlpha: 0.08,
            motionSmoothing: 0.7
        };

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
        });

        // Start button
        document.getElementById('startButton').addEventListener('click', () => {
            this.start();
        });

        // Mute button
        document.getElementById('muteButton').addEventListener('click', () => {
            this.toggleMute();
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

            // Initialize camera
            await this.initCamera();

            status.textContent = 'Initializing audio...';

            // Initialize audio
            this.initAudio();

            status.textContent = 'Ready!';
            setTimeout(() => status.classList.remove('visible'), 2000);

            // Start animation loop
            this.isRunning = true;
            this.animate(0);

        } catch (error) {
            console.error('Error starting:', error);
            alert('Could not access camera. Please grant permissions and try again.');
        }
    }

    async initCamera() {
        const stream = await navigator.mediaDevices.getUserMedia({
            video: { width: 320, height: 240 },
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

    initAudio() {
        this.audioContext = new (window.AudioContext || window.webkitAudioContext)();

        // Master gain (volume control)
        this.masterGain = this.audioContext.createGain();
        this.masterGain.gain.value = 0;
        this.masterGain.connect(this.audioContext.destination);

        // Create reverb
        this.reverb = this.createReverb();
        this.reverb.connect(this.masterGain);

        // Create oscillator pool
        this.oscillatorPool = [];
        for (let i = 0; i < 5; i++) {
            this.oscillatorPool.push({
                osc: null,
                gain: null,
                filter: null,
                active: false
            });
        }

        this.audioEnabled = true;
    }

    createReverb() {
        const convolver = this.audioContext.createConvolver();
        const rate = this.audioContext.sampleRate;
        const length = rate * 2; // 2 second reverb
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

    detectMotion() {
        if (!this.video.readyState === this.video.HAVE_ENOUGH_DATA) {
            return;
        }

        // Draw video frame to canvas
        this.videoCtx.drawImage(this.video, 0, 0, this.videoCanvas.width, this.videoCanvas.height);
        const currentFrame = this.videoCtx.getImageData(0, 0, this.videoCanvas.width, this.videoCanvas.height);

        if (!this.motionData.prevFrame) {
            this.motionData.prevFrame = currentFrame;
            return;
        }

        // Calculate motion
        let totalMotion = 0;
        let motionX = 0;
        let motionY = 0;
        let motionCount = 0;

        const step = 4; // Sample every 4th pixel for performance

        for (let y = 0; y < currentFrame.height; y += step) {
            for (let x = 0; x < currentFrame.width; x += step) {
                const i = (y * currentFrame.width + x) * 4;

                // Calculate difference in RGB values
                const rDiff = Math.abs(currentFrame.data[i] - this.motionData.prevFrame.data[i]);
                const gDiff = Math.abs(currentFrame.data[i + 1] - this.motionData.prevFrame.data[i + 1]);
                const bDiff = Math.abs(currentFrame.data[i + 2] - this.motionData.prevFrame.data[i + 2]);

                const motion = (rDiff + gDiff + bDiff) / 3;

                if (motion > this.settings.motionThreshold) {
                    totalMotion += motion;
                    motionX += x;
                    motionY += y;
                    motionCount++;
                }
            }
        }

        // Update motion data with smoothing
        const smoothing = this.settings.motionSmoothing;
        const rawIntensity = Math.min(totalMotion / 10000, 1);
        this.motionData.intensity = this.motionData.intensity * smoothing + rawIntensity * (1 - smoothing);

        if (motionCount > 0) {
            const rawX = motionX / motionCount / currentFrame.width;
            const rawY = motionY / motionCount / currentFrame.height;
            this.motionData.x = this.motionData.x * smoothing + rawX * (1 - smoothing);
            this.motionData.y = this.motionData.y * smoothing + rawY * (1 - smoothing);
        }

        this.motionData.prevFrame = currentFrame;
    }

    updateParticles(deltaTime) {
        // Create particles based on motion
        if (this.motionData.intensity > 0.05 && this.particles.length < this.maxParticles) {
            const numParticles = Math.floor(this.motionData.intensity * 5);
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
            p.vx *= 0.98; // Friction
            p.vy *= 0.98;
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
        const speed = intensity * 3 + Math.random() * 2;

        this.particles.push({
            x: x + (Math.random() - 0.5) * 20,
            y: y + (Math.random() - 0.5) * 20,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed,
            ax: 0,
            ay: 0.02, // Slight gravity
            size: Math.random() * 4 + 2,
            color: color,
            alpha: 1,
            life: this.settings.particleLifespan
        });
    }

    createParticleBurst(x, y) {
        for (let i = 0; i < 30; i++) {
            const angle = (Math.PI * 2 * i) / 30;
            const speed = Math.random() * 5 + 2;
            const color = this.colors[Math.floor(Math.random() * this.colors.length)];

            this.particles.push({
                x: x,
                y: y,
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
                ax: 0,
                ay: 0.02,
                size: Math.random() * 5 + 3,
                color: color,
                alpha: 1,
                life: this.settings.particleLifespan * 1.5
            });
        }

        // Play a bloopy sound
        this.playBloop(500 + Math.random() * 300, 0.3);
    }

    updateAudio() {
        if (!this.audioEnabled || this.isMuted) {
            return;
        }

        const now = this.audioContext.currentTime;

        // Map motion to audio parameters
        const targetVolume = this.motionData.intensity * 0.3;
        this.masterGain.gain.linearRampToValueAtTime(targetVolume, now + 0.1);

        // Create bloopy sounds based on motion
        if (this.motionData.intensity > 0.1 && Math.random() < this.motionData.intensity * 0.3) {
            // Map position to frequency
            const freq = 200 + this.motionData.x * 600;
            this.playBloop(freq, this.motionData.intensity * 0.2);
        }
    }

    playBloop(frequency, volume = 0.2) {
        if (!this.audioEnabled || this.isMuted) {
            return;
        }

        const now = this.audioContext.currentTime;

        // Create oscillator
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();
        const filter = this.audioContext.createBiquadFilter();

        // Configure oscillator
        osc.type = 'sine';
        osc.frequency.setValueAtTime(frequency, now);
        osc.frequency.exponentialRampToValueAtTime(frequency * 0.7, now + 0.5);

        // Configure filter for bloopy sound
        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(frequency * 1.5, now);
        filter.Q.setValueAtTime(5, now);

        // Configure envelope
        gain.gain.setValueAtTime(0, now);
        gain.gain.linearRampToValueAtTime(volume, now + 0.05); // Attack
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.5); // Release

        // Connect nodes
        osc.connect(filter);
        filter.connect(gain);
        gain.connect(this.reverb);

        // Play
        osc.start(now);
        osc.stop(now + 0.5);
    }

    render() {
        // Create trail effect
        this.ctx.fillStyle = `rgba(0, 0, 0, ${this.settings.trailAlpha})`;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw particles
        for (const p of this.particles) {
            this.ctx.save();

            // Glow effect
            this.ctx.shadowBlur = 20;
            this.ctx.shadowColor = `rgba(${p.color.r}, ${p.color.g}, ${p.color.b}, ${p.alpha})`;

            // Draw particle
            this.ctx.fillStyle = `rgba(${p.color.r}, ${p.color.g}, ${p.color.b}, ${p.alpha * 0.8})`;
            this.ctx.beginPath();
            this.ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            this.ctx.fill();

            this.ctx.restore();
        }

        // Draw motion indicator (subtle)
        if (this.motionData.intensity > 0.05) {
            const x = this.motionData.x * this.canvas.width;
            const y = this.motionData.y * this.canvas.height;
            const radius = this.motionData.intensity * 50;

            this.ctx.save();
            this.ctx.strokeStyle = `rgba(255, 255, 255, ${this.motionData.intensity * 0.3})`;
            this.ctx.lineWidth = 2;
            this.ctx.beginPath();
            this.ctx.arc(x, y, radius, 0, Math.PI * 2);
            this.ctx.stroke();
            this.ctx.restore();
        }
    }

    animate(timestamp) {
        if (!this.isRunning) return;

        const deltaTime = timestamp - this.lastTime;
        this.lastTime = timestamp;

        // Detect motion
        this.detectMotion();

        // Update systems
        this.updateParticles(deltaTime);
        this.updateAudio();

        // Render
        this.render();

        // Continue loop
        requestAnimationFrame((t) => this.animate(t));
    }

    toggleMute() {
        this.isMuted = !this.isMuted;
        const button = document.getElementById('muteButton');
        button.textContent = this.isMuted ? '🔇' : '🔊';

        if (this.masterGain) {
            const now = this.audioContext.currentTime;
            this.masterGain.gain.linearRampToValueAtTime(this.isMuted ? 0 : 0.3, now + 0.1);
        }
    }
}

// Initialize when page loads
window.addEventListener('load', () => {
    const app = new VisualSoundMirror();
});
