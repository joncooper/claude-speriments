// ParticleFountain.js - Particle system visualization with physics

export class ParticleFountain {
    constructor(canvas, ctx) {
        this.canvas = canvas;
        this.ctx = ctx;

        this.particles = [];
        this.maxParticles = 150000;
        this.lastParticleEmitTime = 0;

        this.settings = {
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
    }

    update(leftHand, rightHand, prevLeftHand, prevRightHand, time) {
        const now = Date.now();

        // Emit particles from fingertips
        this.emitParticles(leftHand, rightHand, prevLeftHand, prevRightHand);

        // Build spatial grid for inter-particle forces (only if needed)
        let spatialGrid = null;
        if (this.settings.attraction !== 0 || this.settings.repulsion !== 0) {
            spatialGrid = this.buildSpatialGrid();
        }

        // Update existing particles - use filter for efficient removal
        this.particles = this.particles.filter(p => {
            // Check lifetime
            const age = now - p.birthTime;
            if (age > this.settings.lifetime) {
                return false; // Remove dead particles
            }

            // Apply physics
            // 1. Gravity
            p.vy += this.settings.gravity;

            // 2. Drag
            p.vx *= this.settings.drag;
            p.vy *= this.settings.drag;

            // 3. Turbulence (curl noise for organic swirling)
            if (this.settings.turbulence > 0) {
                const turb = this.curlNoise(p.x * 0.01, p.y * 0.01, time * 0.001);
                p.vx += turb.x * this.settings.turbulence;
                p.vy += turb.y * this.settings.turbulence;
            }

            // 4. Inter-particle forces (using spatial grid for O(n) instead of O(n²))
            if (spatialGrid) {
                this.applyInterParticleForcesFast(p, spatialGrid);
            }

            // Update position
            p.x += p.vx;
            p.y += p.vy;

            // Update trail history (only if needed)
            if (this.settings.trails) {
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

    emitParticles(leftHand, rightHand, prevLeftHand, prevRightHand) {
        // Don't emit if no hands detected
        if (!leftHand && !rightHand) return;

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
        if (leftHand) hands.push({ hand: leftHand, prev: prevLeftHand });
        if (rightHand) hands.push({ hand: rightHand, prev: prevRightHand });

        for (const { hand, prev } of hands) {
            if (!hand.fingertips) continue;

            for (const fingertip of hand.fingertips) {
                // Calculate finger velocity for initial particle velocity
                let velX = 0, velY = 0;
                if (prev && prev.fingertips[fingertip.fingerIndex]) {
                    const prevFinger = prev.fingertips[fingertip.fingerIndex];
                    velX = (fingertip.x - prevFinger.x);
                    velY = (fingertip.y - prevFinger.y);
                }

                // Calculate particles to emit based on TIME (not frames!)
                // emissionRate is particles per SECOND, convert to particles this frame
                const particlesToEmit = (this.settings.emissionRate * deltaTime) / 1000;
                const numToEmit = Math.floor(particlesToEmit);

                for (let e = 0; e < numToEmit; e++) {
                    if (this.particles.length >= this.maxParticles) break;

                    // Randomize initial position slightly around fingertip
                    const spread = 2;
                    const px = fingertip.x + (Math.random() - 0.5) * spread;
                    const py = fingertip.y + (Math.random() - 0.5) * spread;

                    // Initial velocity = finger movement + random spread
                    const angle = Math.random() * Math.PI * 2;
                    const speed = this.settings.initialVelocity;
                    const randomVel = 0.2;

                    const particle = {
                        x: px,
                        y: py,
                        vx: velX * speed + Math.cos(angle) * randomVel,
                        vy: velY * speed + Math.sin(angle) * randomVel,
                        birthTime: now,
                        size: this.settings.particleSizeMin +
                              Math.random() * (this.settings.particleSizeMax - this.settings.particleSizeMin),
                        hue: (fingertip.fingerIndex * 30) % 360, // Color per finger
                        fingerIndex: fingertip.fingerIndex,
                        trail: []
                    };

                    this.particles.push(particle);
                }
            }
        }
    }

    render(baseHue, time, knobs) {
        const now = Date.now();

        // Apply blend mode for different visual effects
        const blendModeMap = {
            'normal': 'source-over',
            'additive': 'lighter',
            'screen': 'screen',
            'multiply': 'multiply'
        };
        this.ctx.globalCompositeOperation = blendModeMap[this.settings.blendMode] || 'source-over';

        // OPTIMIZATION: Batch all particles into a single path
        // Apply glow once instead of per-particle
        if (this.settings.glow) {
            this.ctx.shadowBlur = 8;
            this.ctx.shadowColor = 'rgba(255, 255, 255, 0.5)';
        }

        // Draw trails first (if enabled) - batched by color
        if (this.settings.trails) {
            for (const p of this.particles) {
                if (!p.trail || p.trail.length < 2) continue;

                const age = now - p.birthTime;
                const lifeProgress = age / this.settings.lifetime;
                const lifetimeAlpha = 1 - Math.pow(lifeProgress, 2);
                const alpha = lifetimeAlpha * this.settings.alpha;

                const { hue, saturation, lightness } = this.getParticleColor(p, lifeProgress, now, baseHue, time, knobs);

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
        if (this.settings.colorMode === 'rainbow' || this.settings.colorMode === 'audio') {
            // Single color fill for all particles (fastest)
            const baseColor = this.getParticleColor(this.particles[0] || { hue: baseHue }, 0.5, now, baseHue, time, knobs);
            this.ctx.fillStyle = `hsla(${baseColor.hue}, ${baseColor.saturation}%, ${baseColor.lightness}%, ${this.settings.alpha})`;
            this.ctx.fill();
        } else {
            // Individual coloring (slower but more dynamic)
            for (const p of this.particles) {
                const age = now - p.birthTime;
                const lifeProgress = age / this.settings.lifetime;
                const lifetimeAlpha = 1 - Math.pow(lifeProgress, 2);
                const alpha = lifetimeAlpha * this.settings.alpha;

                const { hue, saturation, lightness } = this.getParticleColor(p, lifeProgress, now, baseHue, time, knobs);

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

    getParticleColor(p, lifeProgress, now, baseHue, time, knobs) {
        let hue, saturation, lightness;

        switch (this.settings.colorMode) {
            case 'velocity':
                const speed = Math.sqrt(p.vx * p.vx + p.vy * p.vy);
                hue = (baseHue + speed * 20) % 360;
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
                const filterFreq = knobs[0] ? knobs[0].value : 0.5;
                hue = (baseHue + filterFreq * 180) % 360;
                saturation = 85;
                lightness = 55;
                break;

            case 'rainbow':
            default:
                hue = (p.hue + time * 0.05) % 360;
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
                        const force = (this.settings.attraction - this.settings.repulsion / dist);
                        const fx = (dx / dist) * force * 0.01; // Scale down for stability
                        const fy = (dy / dist) * force * 0.01;

                        particle.vx += fx;
                        particle.vy += fy;
                    }
                }
            }
        }
    }

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

    updateSettings(newSettings) {
        Object.assign(this.settings, newSettings);
    }

    getParticleCount() {
        return this.particles.length;
    }

    clearParticles() {
        this.particles = [];
    }
}
