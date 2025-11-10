// Kaleidoscope.js - Radial symmetry mirroring effect

export class Kaleidoscope {
    constructor(canvas, ctx) {
        this.canvas = canvas;
        this.ctx = ctx;

        this.settings = {
            symmetryCount: 6,          // Fold count (3-12)
            fingerSize: 18,            // Reflected finger size (8-40)
            lineOpacity: 0.4,          // Line to center opacity (0-1)
            rotationSpeed: 0,          // Auto-rotation (0-0.01)
            trailPersistence: 0.85,    // Trail fade (0.7-0.95)
            glowIntensity: 25,         // Glow blur (0-50)
            pulseWithAudio: false,     // React to audio
            showCenter: true           // Show center point
        };
    }

    render(leftHand, rightHand, baseHue, time, audioContext) {
        if (!leftHand && !rightHand) return;

        const s = this.settings;
        const centerX = this.canvas.width / 2;
        const centerY = this.canvas.height / 2;

        // Apply trail persistence
        this.ctx.fillStyle = `rgba(0, 0, 0, ${1 - s.trailPersistence})`;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        this.ctx.save();
        this.ctx.shadowBlur = s.glowIntensity;

        const hands = [];
        if (leftHand) hands.push(leftHand);
        if (rightHand) hands.push(rightHand);

        // Auto-rotation offset
        const rotationOffset = time * s.rotationSpeed;

        for (const hand of hands) {
            if (!hand.fingertips) continue;

            for (const fingertip of hand.fingertips) {
                const hue = (baseHue + fingertip.fingerIndex * 30) % 360;

                // Draw the fingertip reflected around the center with radial symmetry
                for (let sym = 0; sym < s.symmetryCount; sym++) {
                    const angle = (sym / s.symmetryCount) * Math.PI * 2 + rotationOffset;

                    this.ctx.save();
                    this.ctx.translate(centerX, centerY);
                    this.ctx.rotate(angle);
                    this.ctx.translate(-centerX, -centerY);

                    // Pulsing size with audio if enabled
                    let pulseMultiplier = 1;
                    if (s.pulseWithAudio && audioContext) {
                        pulseMultiplier = 1 + Math.sin(time * 0.005 + fingertip.fingerIndex) * 0.3;
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
            const centerPulse = 1 + Math.sin(time * 0.003) * 0.2;
            this.ctx.shadowColor = `hsl(${baseHue}, 90%, 80%)`;
            this.ctx.fillStyle = `hsla(${baseHue}, 90%, 80%, 0.8)`;
            this.ctx.beginPath();
            this.ctx.arc(centerX, centerY, 10 * centerPulse, 0, Math.PI * 2);
            this.ctx.fill();

            // Center glow
            const gradient = this.ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, 25 * centerPulse);
            gradient.addColorStop(0, `hsla(${baseHue}, 90%, 80%, 0.5)`);
            gradient.addColorStop(1, `hsla(${baseHue}, 90%, 80%, 0)`);
            this.ctx.fillStyle = gradient;
            this.ctx.beginPath();
            this.ctx.arc(centerX, centerY, 25 * centerPulse, 0, Math.PI * 2);
            this.ctx.fill();
        }

        this.ctx.restore();
        this.ctx.shadowBlur = 0;
    }

    updateSettings(newSettings) {
        Object.assign(this.settings, newSettings);
    }
}
