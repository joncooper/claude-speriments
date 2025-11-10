// RenderHelpers.js - Helper methods for rendering visual effects

export class RenderHelpers {
    constructor(app) {
        this.app = app;
    }

    drawModeIndicator() {
        this.app.ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
        this.app.ctx.font = '18px monospace';
        this.app.ctx.textAlign = 'left';
        this.app.ctx.textBaseline = 'top';

        const modeText = `Mode: ${this.app.mode.toUpperCase()}`;
        this.app.ctx.fillText(modeText, 20, 20);

        if (this.app.mode === 'theremin') {
            this.app.ctx.fillText(`Scale: ${this.app.currentScale}`, 20, 50);
        }

        this.app.ctx.textAlign = 'left';
        this.app.ctx.textBaseline = 'alphabetic';
    }

    drawGestureHoldProgress() {
        // Show circular progress indicator around hand position
        if (!this.app.leftHand || !this.app.leftHand.palm) return;

        const now = Date.now();
        const elapsed = now - this.app.gestureHoldStartTime;
        const progress = Math.min(elapsed / this.app.gestureHoldRequired, 1.0);

        const centerX = this.app.leftHand.palm.x;
        const centerY = this.app.leftHand.palm.y;
        const radius = 80;

        // Background circle
        this.app.ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
        this.app.ctx.lineWidth = 8;
        this.app.ctx.beginPath();
        this.app.ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
        this.app.ctx.stroke();

        // Progress arc
        this.app.ctx.strokeStyle = `rgba(100, 255, 150, ${0.5 + progress * 0.5})`;
        this.app.ctx.lineWidth = 10;
        this.app.ctx.lineCap = 'round';
        this.app.ctx.beginPath();
        this.app.ctx.arc(centerX, centerY, radius, -Math.PI / 2, -Math.PI / 2 + (progress * Math.PI * 2));
        this.app.ctx.stroke();

        // Gesture indicator text
        const gestureNames = { 1: '1 FINGER', 2: 'PEACE', 5: 'OPEN HAND' };
        const gestureName = gestureNames[this.app.currentGestureFingerCount] || '';

        this.app.ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
        this.app.ctx.font = 'bold 16px monospace';
        this.app.ctx.textAlign = 'center';
        this.app.ctx.textBaseline = 'middle';
        this.app.ctx.fillText(gestureName, centerX, centerY - 5);

        const pct = Math.round(progress * 100);
        this.app.ctx.font = '14px monospace';
        this.app.ctx.fillText(`${pct}%`, centerX, centerY + 15);

        this.app.ctx.textAlign = 'left';
        this.app.ctx.textBaseline = 'alphabetic';
    }

    drawModeSwitchAnimation() {
        const now = Date.now();
        const elapsed = now - this.app.modeSwitchAnimation.startTime;
        const progress = elapsed / this.app.modeSwitchAnimation.duration;

        if (progress >= 1.0) {
            this.app.modeSwitchAnimation.active = false;
            return;
        }

        // Burst of colorful particles from center
        const centerX = this.app.canvas.width / 2;
        const centerY = this.app.canvas.height / 2;
        const numParticles = 50;

        for (let i = 0; i < numParticles; i++) {
            const angle = (i / numParticles) * Math.PI * 2;
            const distance = progress * 400; // Expand outward
            const x = centerX + Math.cos(angle) * distance;
            const y = centerY + Math.sin(angle) * distance;

            const hue = (this.app.baseHue + i * 7) % 360;
            const alpha = 1 - progress; // Fade out

            this.app.ctx.fillStyle = `hsla(${hue}, 100%, 60%, ${alpha})`;
            this.app.ctx.beginPath();
            this.app.ctx.arc(x, y, 8 * (1 - progress * 0.5), 0, Math.PI * 2);
            this.app.ctx.fill();
        }

        // Flash effect
        const flashAlpha = Math.max(0, 0.3 - progress * 0.6);
        this.app.ctx.fillStyle = `rgba(255, 255, 255, ${flashAlpha})`;
        this.app.ctx.fillRect(0, 0, this.app.canvas.width, this.app.canvas.height);

        // Mode text in center
        if (progress < 0.5) {
            const textAlpha = (0.5 - progress) * 2;
            this.app.ctx.fillStyle = `rgba(255, 255, 255, ${textAlpha})`;
            this.app.ctx.font = 'bold 48px monospace';
            this.app.ctx.textAlign = 'center';
            this.app.ctx.textBaseline = 'middle';
            this.app.ctx.fillText(this.app.mode.toUpperCase(), centerX, centerY);
        }

        this.app.ctx.textAlign = 'left';
        this.app.ctx.textBaseline = 'alphabetic';
    }

    drawFluidRibbon(trail, fingerIndex, handedness) {
        // Draw multiple parallel ribbons with varying width for silk effect
        const numRibbons = this.app.settings.ribbonOffsets;

        for (let r = 0; r < numRibbons; r++) {
            const offset = (r - Math.floor(numRibbons / 2)) * this.app.settings.ribbonSpacing;
            const alpha = 1 - (Math.abs(offset) / (numRibbons * this.app.settings.ribbonSpacing)) * 0.7;

            this.app.ctx.save();
            this.app.ctx.globalAlpha = alpha * 0.6;

            // Create smooth curve with varying width
            this.app.ctx.beginPath();

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
                    this.app.ctx.moveTo(x, y);
                } else {
                    const prev = trail[i - 1];
                    const prevPerpX = perpX;
                    const prevPerpY = perpY;
                    const cpx = (prev.x + prevPerpX + x) / 2;
                    const cpy = (prev.y + prevPerpY + y) / 2;
                    this.app.ctx.quadraticCurveTo(prev.x + prevPerpX, prev.y + prevPerpY, cpx, cpy);
                }
            }

            // Get color
            const color = this.app.getColorForFinger(fingerIndex, handedness, this.app.time * 0.001);

            // Gradient from transparent to solid
            const gradient = this.app.ctx.createLinearGradient(
                trail[0].x, trail[0].y,
                trail[trail.length - 1].x, trail[trail.length - 1].y
            );

            gradient.addColorStop(0, `rgba(${color.r}, ${color.g}, ${color.b}, 0.05)`);
            gradient.addColorStop(0.5, `rgba(${color.r}, ${color.g}, ${color.b}, 0.5)`);
            gradient.addColorStop(1, `rgba(${color.r}, ${color.g}, ${color.b}, 0.9)`);

            // Varying width based on position in trail
            let widthMultiplier = 1;
            if (this.app.leftHand && handedness === 'Left') {
                widthMultiplier = 1 + (this.app.leftHand.fingerSpread / 200);
            } else if (this.app.rightHand && handedness === 'Right') {
                widthMultiplier = 1 + (this.app.rightHand.fingerSpread / 200);
            }

            this.app.ctx.strokeStyle = gradient;
            this.app.ctx.lineWidth = this.app.settings.ribbonWidth * widthMultiplier;
            this.app.ctx.lineCap = 'round';
            this.app.ctx.lineJoin = 'round';
            this.app.ctx.shadowBlur = 15;
            this.app.ctx.shadowColor = `rgba(${color.r}, ${color.g}, ${color.b}, 0.6)`;
            this.app.ctx.stroke();

            this.app.ctx.restore();
        }
    }

    drawTouchingEffect() {
        // Draw pulsing glow between touching fingers
        for (const touch of this.app.touchingFingers) {
            const midX = (touch.left.x + touch.right.x) / 2;
            const midY = (touch.left.y + touch.right.y) / 2;

            const pulse = Math.sin(this.app.time * 0.005) * 0.3 + 0.7;
            const radius = 30 * pulse;

            const gradient = this.app.ctx.createRadialGradient(midX, midY, 0, midX, midY, radius);
            gradient.addColorStop(0, 'rgba(255, 255, 200, 0.8)');
            gradient.addColorStop(0.5, 'rgba(200, 150, 255, 0.4)');
            gradient.addColorStop(1, 'rgba(100, 200, 255, 0)');

            this.app.ctx.fillStyle = gradient;
            this.app.ctx.beginPath();
            this.app.ctx.arc(midX, midY, radius, 0, Math.PI * 2);
            this.app.ctx.fill();
        }
    }

    drawFingertipMarkers(hand) {
        for (const tip of hand.fingertips) {
            const color = this.app.getColorForFinger(tip.fingerIndex, hand.handedness, this.app.time * 0.001);
            const spread = hand.fingerSpread;
            const size = 3 + (spread / 200) * 3;

            this.app.ctx.save();

            // Inner glow
            this.app.ctx.shadowBlur = 20;
            this.app.ctx.shadowColor = `rgba(${color.r}, ${color.g}, ${color.b}, 0.8)`;

            this.app.ctx.fillStyle = `rgba(${color.r}, ${color.g}, ${color.b}, 0.9)`;
            this.app.ctx.beginPath();
            this.app.ctx.arc(tip.x, tip.y, size, 0, Math.PI * 2);
            this.app.ctx.fill();

            // Outer ring
            this.app.ctx.strokeStyle = `rgba(${color.r}, ${color.g}, ${color.b}, 0.4)`;
            this.app.ctx.lineWidth = 1.5;
            this.app.ctx.beginPath();
            this.app.ctx.arc(tip.x, tip.y, size + 4, 0, Math.PI * 2);
            this.app.ctx.stroke();

            this.app.ctx.restore();
        }
    }

    drawDebugSkeleton() {
        for (const landmarks of this.app.handResults.multiHandLandmarks) {
            const connections = [
                [0, 1], [1, 2], [2, 3], [3, 4],
                [0, 5], [5, 6], [6, 7], [7, 8],
                [0, 9], [9, 10], [10, 11], [11, 12],
                [0, 13], [13, 14], [14, 15], [15, 16],
                [0, 17], [17, 18], [18, 19], [19, 20],
                [5, 9], [9, 13], [13, 17]
            ];

            this.app.ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
            this.app.ctx.lineWidth = 1.5;

            for (const [start, end] of connections) {
                const startPoint = landmarks[start];
                const endPoint = landmarks[end];

                this.app.ctx.beginPath();
                this.app.ctx.moveTo((1 - startPoint.x) * this.app.canvas.width, startPoint.y * this.app.canvas.height);
                this.app.ctx.lineTo((1 - endPoint.x) * this.app.canvas.width, endPoint.y * this.app.canvas.height);
                this.app.ctx.stroke();
            }
        }
    }
}
