// AudioBloom.js - Expanding bloom pulses triggered by fast movements

export class AudioBloom {
    constructor(canvas, ctx) {
        this.canvas = canvas;
        this.ctx = ctx;

        this.blooms = [];
        this.lastBloomTime = 0;

        this.settings = {
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
    }

    update(leftHand, rightHand, prevLeftHand, prevRightHand, baseHue) {
        const now = Date.now();
        const s = this.settings;

        // Create blooms from fingertip movements
        if (leftHand || rightHand) {
            const hands = [];
            if (leftHand) hands.push({ hand: leftHand, prev: prevLeftHand });
            if (rightHand) hands.push({ hand: rightHand, prev: prevRightHand });

            for (const { hand, prev } of hands) {
                if (!hand.fingertips) continue;

                for (const fingertip of hand.fingertips) {
                    // Calculate velocity
                    let velocity = 0;
                    if (prev && prev.fingertips[fingertip.fingerIndex]) {
                        const prevFinger = prev.fingertips[fingertip.fingerIndex];
                        const dx = fingertip.x - prevFinger.x;
                        const dy = fingertip.y - prevFinger.y;
                        velocity = Math.sqrt(dx * dx + dy * dy);
                    }

                    // Create bloom on fast movement (use settings)
                    if (velocity > s.velocityThreshold && now - this.lastBloomTime > s.bloomInterval) {
                        this.blooms.push({
                            x: fingertip.x,
                            y: fingertip.y,
                            birthTime: now,
                            hue: (baseHue + fingertip.fingerIndex * 30) % 360,
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

    render() {
        const now = Date.now();
        const s = this.settings;

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

    updateSettings(newSettings) {
        Object.assign(this.settings, newSettings);
    }

    clearBlooms() {
        this.blooms = [];
    }
}
