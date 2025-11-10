// GravitationalOrbits.js - Particles orbit around fingertips like planets

export class GravitationalOrbits {
    constructor(canvas, ctx) {
        this.canvas = canvas;
        this.ctx = ctx;

        this.settings = {
            orbiterCount: 8,           // Particles per fingertip (4-20)
            orbitRadius: 45,           // Orbit distance (20-100)
            orbitSpeed: 0.003,         // Rotation speed (0.001-0.01)
            orbiterSize: 5,            // Particle size (2-12)
            sunSize: 14,               // Central sun size (8-30)
            trailLength: 0.15,         // Orbital trail length (0-0.5)
            wobble: 5,                 // Orbit wobble amount (0-20)
            glowIntensity: 18          // Glow blur (0-40)
        };
    }

    render(leftHand, rightHand, baseHue, time) {
        if (!leftHand && !rightHand) return;

        const s = this.settings;
        const hands = [];
        if (leftHand) hands.push(leftHand);
        if (rightHand) hands.push(rightHand);

        this.ctx.shadowBlur = s.glowIntensity;

        for (const hand of hands) {
            if (!hand.fingertips) continue;

            for (const fingertip of hand.fingertips) {
                const hue = (baseHue + fingertip.fingerIndex * 30) % 360;

                // Draw orbiting particles around fingertip
                for (let i = 0; i < s.orbiterCount; i++) {
                    // Variable speed per orbiter for more dynamic feel
                    const speedVar = 1 + (i % 3) * 0.2 - 0.2; // Some faster, some slower
                    const angle = (i / s.orbiterCount) * Math.PI * 2 + time * s.orbitSpeed * speedVar + fingertip.fingerIndex;

                    // Add wobble to orbit radius
                    const wobbleAmount = Math.sin(time * 0.005 + i) * s.wobble;
                    const wobbledRadius = s.orbitRadius + wobbleAmount;

                    const x = fingertip.x + Math.cos(angle) * wobbledRadius;
                    const y = fingertip.y + Math.sin(angle) * wobbledRadius;

                    // Draw orbital particle with size variation
                    const sizeVar = 1 + Math.sin(time * 0.003 + i) * 0.3;
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
                const sunPulse = 1 + Math.sin(time * 0.004) * 0.15;
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

    updateSettings(newSettings) {
        Object.assign(this.settings, newSettings);
    }
}
