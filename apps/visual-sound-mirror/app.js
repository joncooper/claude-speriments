// Visual Sound Mirror - v4.0 Flowing Ribbons Edition
// Ultra-responsive, ephemeral, musical visualization

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

        // Hand positions for tracking
        this.handPositions = [];
        this.prevHandPositions = [];

        // Motion data
        this.motionData = {
            intensity: 0,
            x: 0.5,
            y: 0.5
        };

        // Fingertip trails - each finger gets its own trail
        this.fingerTrails = {};  // key: finger index, value: array of trail points
        this.maxTrailLength = 20;  // Keep trails short and responsive

        // Particles - minimal, velocity-based
        this.particles = [];
        this.maxParticles = 200;  // Much fewer particles

        // Audio setup
        this.audioContext = null;
        this.masterGain = null;
        this.audioEnabled = false;
        this.isMuted = false;
        this.lastSoundTime = 0;

        // Debug mode
        this.debugMode = false;

        // No hands timer
        this.noHandsTime = 0;
        this.fadeoutStarted = false;

        // Color palette
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
            particleLifespan: 40,  // Much shorter - ephemeral!
            trailAlpha: 0.15,      // More aggressive clearing
            soundInterval: 80,      // More frequent sounds
            connectionDistance: 120, // Distance to draw lines between fingers
            minVelocityForParticles: 2  // Only spawn particles when moving
        };

        // Animation
        this.lastTime = 0;
        this.isRunning = false;
        this.time = 0;

        this.setupEventListeners();
    }

    resizeCanvas() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    setupEventListeners() {
        window.addEventListener('resize', () => this.resizeCanvas());

        this.canvas.addEventListener('click', (e) => {
            this.createParticleBurst(e.clientX, e.clientY);
            if (this.audioContext && this.audioContext.state === 'suspended') {
                this.audioContext.resume();
            }
            this.playBloop(400 + Math.random() * 400, 0.3);
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

        this.masterGain = this.audioContext.createGain();
        this.masterGain.gain.value = 0.2;
        this.masterGain.connect(this.audioContext.destination);

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
        this.prevHandPositions = [...this.handPositions];
        this.handPositions = [];

        if (results.multiHandLandmarks && results.multiHandLandmarks.length > 0) {
            // Reset no hands timer
            this.noHandsTime = 0;
            this.fadeoutStarted = false;

            for (let handIndex = 0; handIndex < results.multiHandLandmarks.length; handIndex++) {
                const landmarks = results.multiHandLandmarks[handIndex];

                // Get fingertips only - more focused
                const fingertipIndices = [4, 8, 12, 16, 20];  // Thumb, Index, Middle, Ring, Pinky

                for (let i = 0; i < fingertipIndices.length; i++) {
                    const tip = landmarks[fingertipIndices[i]];
                    const fingerId = `hand${handIndex}_finger${i}`;

                    const pos = {
                        x: (1 - tip.x) * this.canvas.width,
                        y: tip.y * this.canvas.height,
                        z: tip.z,
                        fingerId: fingerId,
                        fingerIndex: i,
                        handIndex: handIndex
                    };

                    this.handPositions.push(pos);

                    // Update trail for this finger
                    if (!this.fingerTrails[fingerId]) {
                        this.fingerTrails[fingerId] = [];
                    }

                    this.fingerTrails[fingerId].push({
                        x: pos.x,
                        y: pos.y,
                        time: this.time,
                        color: this.colors[i % this.colors.length]
                    });

                    // Keep trails short
                    if (this.fingerTrails[fingerId].length > this.maxTrailLength) {
                        this.fingerTrails[fingerId].shift();
                    }
                }

                // Calculate palm position for motion intensity
                const palm = landmarks[9];
                const palmPos = {
                    x: (1 - palm.x) * this.canvas.width,
                    y: palm.y * this.canvas.height
                };

                // Calculate movement for this palm
                const avgX = palmPos.x / this.canvas.width;
                const avgY = palmPos.y / this.canvas.height;

                if (this.prevHandPositions.length > 0) {
                    // Find closest previous position
                    let minDist = Infinity;
                    let closestPrev = null;

                    for (const prev of this.prevHandPositions) {
                        const dist = Math.sqrt(
                            Math.pow(palmPos.x - prev.x, 2) +
                            Math.pow(palmPos.y - prev.y, 2)
                        );
                        if (dist < minDist) {
                            minDist = dist;
                            closestPrev = prev;
                        }
                    }

                    if (closestPrev) {
                        const dx = palmPos.x - closestPrev.x;
                        const dy = palmPos.y - closestPrev.y;
                        const movement = Math.sqrt(dx * dx + dy * dy);
                        this.motionData.intensity = Math.min(movement / 20, 1);
                    }
                }

                this.motionData.x = avgX;
                this.motionData.y = avgY;
            }
        } else {
            // No hands detected - start fadeout timer
            this.noHandsTime += 16; // ~16ms per frame
            if (this.noHandsTime > 1000) {  // 1 second
                this.fadeoutStarted = true;
                // Clear trails
                this.fingerTrails = {};
                this.particles = [];
            }
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
        this.time += deltaTime;

        // Only spawn particles when hands are moving
        if (this.handPositions.length > 0 && this.motionData.intensity > 0.1) {
            for (const pos of this.handPositions) {
                // Calculate velocity
                let velocity = { x: 0, y: 0 };
                for (const prev of this.prevHandPositions) {
                    if (prev.fingerId === pos.fingerId) {
                        velocity.x = pos.x - prev.x;
                        velocity.y = pos.y - prev.y;
                        break;
                    }
                }

                const speed = Math.sqrt(velocity.x * velocity.x + velocity.y * velocity.y);

                // Only spawn if moving fast enough
                if (speed > this.settings.minVelocityForParticles && Math.random() < 0.3) {
                    this.createVelocityParticle(pos, velocity, speed);
                }
            }
        }

        // Update existing particles
        for (let i = this.particles.length - 1; i >= 0; i--) {
            const p = this.particles[i];

            p.vx *= 0.95;
            p.vy *= 0.95;
            p.x += p.vx;
            p.y += p.vy;

            p.life--;
            p.alpha = p.life / this.settings.particleLifespan;

            if (p.life <= 0) {
                this.particles.splice(i, 1);
            }
        }
    }

    createVelocityParticle(pos, velocity, speed) {
        if (this.particles.length >= this.maxParticles) return;

        const color = this.colors[pos.fingerIndex % this.colors.length];

        this.particles.push({
            x: pos.x,
            y: pos.y,
            vx: velocity.x * 0.5,
            vy: velocity.y * 0.5,
            size: Math.min(speed * 0.5, 8) + 2,
            color: color,
            alpha: 1,
            life: this.settings.particleLifespan
        });
    }

    createParticleBurst(x, y) {
        for (let i = 0; i < 15; i++) {
            const angle = Math.random() * Math.PI * 2;
            const speed = Math.random() * 4 + 2;
            const color = this.colors[Math.floor(Math.random() * this.colors.length)];

            this.particles.push({
                x: x,
                y: y,
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
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

        if (this.audioContext.state === 'suspended') {
            this.audioContext.resume();
        }

        const now = Date.now();

        if (this.handPositions.length > 0 && this.motionData.intensity > 0.05) {
            if (now - this.lastSoundTime > this.settings.soundInterval) {
                // Play sounds for up to 3 fingers
                for (let i = 0; i < Math.min(this.handPositions.length, 3); i++) {
                    const pos = this.handPositions[i];
                    const freq = 200 + (pos.x / this.canvas.width) * 600;
                    const volume = 0.08 + this.motionData.intensity * 0.12;

                    setTimeout(() => {
                        this.playBloop(freq, volume);
                    }, i * 40);
                }

                this.lastSoundTime = now;
            }
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
            const filter = this.audioContext.createBiquadFilter();

            osc.type = 'sine';
            osc.frequency.setValueAtTime(frequency, now);
            osc.frequency.exponentialRampToValueAtTime(frequency * 0.6, now + 0.4);

            filter.type = 'lowpass';
            filter.frequency.setValueAtTime(frequency * 2, now);
            filter.Q.setValueAtTime(3, now);

            gain.gain.setValueAtTime(0, now);
            gain.gain.linearRampToValueAtTime(volume, now + 0.03);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.4);

            osc.connect(filter);
            filter.connect(gain);
            gain.connect(this.reverb);

            osc.start(now);
            osc.stop(now + 0.4);
        } catch (error) {
            console.error('Error playing sound:', error);
        }
    }

    render() {
        // Aggressive clearing when no hands, gentle trails when hands present
        if (this.fadeoutStarted || this.handPositions.length === 0) {
            this.ctx.fillStyle = 'rgba(0, 0, 0, 0.3)';  // Quick fadeout
        } else {
            this.ctx.fillStyle = `rgba(0, 0, 0, ${this.settings.trailAlpha})`;
        }
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw constellation lines between nearby fingers
        if (this.handPositions.length > 1) {
            for (let i = 0; i < this.handPositions.length; i++) {
                for (let j = i + 1; j < this.handPositions.length; j++) {
                    const pos1 = this.handPositions[i];
                    const pos2 = this.handPositions[j];

                    const dist = Math.sqrt(
                        Math.pow(pos2.x - pos1.x, 2) +
                        Math.pow(pos2.y - pos1.y, 2)
                    );

                    if (dist < this.settings.connectionDistance) {
                        const alpha = 1 - (dist / this.settings.connectionDistance);

                        const gradient = this.ctx.createLinearGradient(pos1.x, pos1.y, pos2.x, pos2.y);
                        const color1 = this.colors[pos1.fingerIndex % this.colors.length];
                        const color2 = this.colors[pos2.fingerIndex % this.colors.length];

                        gradient.addColorStop(0, `rgba(${color1.r}, ${color1.g}, ${color1.b}, ${alpha * 0.6})`);
                        gradient.addColorStop(1, `rgba(${color2.r}, ${color2.g}, ${color2.b}, ${alpha * 0.6})`);

                        this.ctx.strokeStyle = gradient;
                        this.ctx.lineWidth = 2 + alpha * 2;
                        this.ctx.shadowBlur = 15;
                        this.ctx.shadowColor = `rgba(255, 255, 255, ${alpha * 0.5})`;
                        this.ctx.beginPath();
                        this.ctx.moveTo(pos1.x, pos1.y);
                        this.ctx.lineTo(pos2.x, pos2.y);
                        this.ctx.stroke();
                        this.ctx.shadowBlur = 0;
                    }
                }
            }
        }

        // Draw flowing ribbon trails for each finger
        for (const fingerId in this.fingerTrails) {
            const trail = this.fingerTrails[fingerId];

            if (trail.length < 2) continue;

            // Draw as smooth curve
            this.ctx.beginPath();
            this.ctx.moveTo(trail[0].x, trail[0].y);

            for (let i = 1; i < trail.length; i++) {
                const point = trail[i];
                const prevPoint = trail[i - 1];

                // Smooth curve
                const cpx = (prevPoint.x + point.x) / 2;
                const cpy = (prevPoint.y + point.y) / 2;
                this.ctx.quadraticCurveTo(prevPoint.x, prevPoint.y, cpx, cpy);
            }

            // Gradient along trail
            const lastPoint = trail[trail.length - 1];
            const firstPoint = trail[0];
            const gradient = this.ctx.createLinearGradient(
                firstPoint.x, firstPoint.y,
                lastPoint.x, lastPoint.y
            );

            const color = lastPoint.color;
            gradient.addColorStop(0, `rgba(${color.r}, ${color.g}, ${color.b}, 0.1)`);
            gradient.addColorStop(1, `rgba(${color.r}, ${color.g}, ${color.b}, 0.8)`);

            this.ctx.strokeStyle = gradient;
            this.ctx.lineWidth = 3 + this.motionData.intensity * 4;
            this.ctx.shadowBlur = 20;
            this.ctx.shadowColor = `rgba(${color.r}, ${color.g}, ${color.b}, 0.6)`;
            this.ctx.stroke();
            this.ctx.shadowBlur = 0;
        }

        // Draw particles
        for (const p of this.particles) {
            this.ctx.save();

            this.ctx.shadowBlur = 15;
            this.ctx.shadowColor = `rgba(${p.color.r}, ${p.color.g}, ${p.color.b}, ${p.alpha})`;

            this.ctx.fillStyle = `rgba(${p.color.r}, ${p.color.g}, ${p.color.b}, ${p.alpha * 0.8})`;
            this.ctx.beginPath();
            this.ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            this.ctx.fill();

            this.ctx.restore();
        }

        // Draw fingertip positions as glowing dots
        for (const pos of this.handPositions) {
            const color = this.colors[pos.fingerIndex % this.colors.length];
            const intensity = this.motionData.intensity;

            this.ctx.save();
            this.ctx.shadowBlur = 25 + intensity * 20;
            this.ctx.shadowColor = `rgba(${color.r}, ${color.g}, ${color.b}, 0.8)`;

            this.ctx.fillStyle = `rgba(${color.r}, ${color.g}, ${color.b}, 0.9)`;
            this.ctx.beginPath();
            this.ctx.arc(pos.x, pos.y, 4 + intensity * 4, 0, Math.PI * 2);
            this.ctx.fill();

            // Outer ring
            this.ctx.strokeStyle = `rgba(${color.r}, ${color.g}, ${color.b}, 0.5)`;
            this.ctx.lineWidth = 2;
            this.ctx.beginPath();
            this.ctx.arc(pos.x, pos.y, 8 + intensity * 6, 0, Math.PI * 2);
            this.ctx.stroke();

            this.ctx.restore();
        }

        // Debug overlay
        if (this.debugMode && this.handResults && this.handResults.multiHandLandmarks) {
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
                this.ctx.lineWidth = 2;

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
    }

    animate(timestamp) {
        if (!this.isRunning) return;

        const deltaTime = timestamp - this.lastTime;
        this.lastTime = timestamp;

        this.updateParticles(deltaTime);
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
