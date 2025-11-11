// TemporalEchoes.js - Ghost images / motion blur effect showing hand movement history

export class TemporalEchoes {
    constructor(canvas, ctx) {
        this.canvas = canvas;
        this.ctx = ctx;

        this.handHistory = [];
        this.maxHistoryLength = 60; // Store up to 60 frames of history

        this.settings = {
            trailLength: 30,           // Number of echoes to show (5-60)
            fadeSpeed: 0.03,           // How fast echoes fade (0.01-0.1)
            chromaticAberration: 3,    // RGB separation in pixels (0-10)
            motionBlur: true,          // Connect echoes with lines
            glowIntensity: 15,         // Glow blur amount (0-30)
            echoSpacing: 2,            // Frames between echoes (1-5)
            showPalm: true,            // Show palm echoes
            showFingers: true,         // Show finger echoes
            fingerSize: 12,            // Echo finger size (6-24)
            palmSize: 20               // Echo palm size (10-40)
        };
    }

    update(leftHand, rightHand) {
        // Capture current hand state
        if (leftHand || rightHand) {
            const snapshot = {
                timestamp: Date.now(),
                leftHand: leftHand ? this.copyHandState(leftHand) : null,
                rightHand: rightHand ? this.copyHandState(rightHand) : null
            };

            this.handHistory.push(snapshot);

            // Limit history length
            if (this.handHistory.length > this.maxHistoryLength) {
                this.handHistory.shift();
            }
        }
    }

    copyHandState(hand) {
        return {
            palm: { x: hand.palm.x, y: hand.palm.y },
            fingertips: hand.fingertips.map(ft => ({
                x: ft.x,
                y: ft.y,
                fingerIndex: ft.fingerIndex
            }))
        };
    }

    render(baseHue) {
        if (this.handHistory.length < 2) return;

        const now = Date.now();
        const spacing = this.settings.echoSpacing;
        const trailLength = Math.min(this.settings.trailLength, this.handHistory.length);

        // Enable glow effect
        if (this.settings.glowIntensity > 0) {
            this.ctx.shadowBlur = this.settings.glowIntensity;
        }

        // Draw echoes from oldest to newest (so newest is on top)
        for (let i = 0; i < trailLength; i += spacing) {
            const historyIndex = this.handHistory.length - 1 - i;
            if (historyIndex < 0) break;

            const snapshot = this.handHistory[historyIndex];
            const age = i / trailLength; // 0 = newest, 1 = oldest
            const alpha = (1 - age) * (1 - this.settings.fadeSpeed * i);

            if (alpha <= 0) continue;

            // Draw chromatic aberration (RGB separation for dreamy effect)
            const aberration = this.settings.chromaticAberration;

            // Red channel (shifted right/down)
            if (aberration > 0) {
                this.drawHandEcho(snapshot, alpha * 0.6, aberration, 0, 'rgba(255, 100, 100, ', baseHue);
            }

            // Green channel (center)
            this.drawHandEcho(snapshot, alpha, 0, 0, null, baseHue);

            // Blue channel (shifted left/up)
            if (aberration > 0) {
                this.drawHandEcho(snapshot, alpha * 0.6, -aberration, 0, 'rgba(100, 100, 255, ', baseHue);
            }

            // Draw motion blur connections
            if (this.settings.motionBlur && i < trailLength - spacing && historyIndex > 0) {
                const prevSnapshot = this.handHistory[historyIndex - spacing];
                if (prevSnapshot) {
                    this.drawMotionBlurConnections(snapshot, prevSnapshot, alpha * 0.3, baseHue);
                }
            }
        }

        // Reset shadow
        this.ctx.shadowBlur = 0;
    }

    drawHandEcho(snapshot, alpha, offsetX, offsetY, colorOverride, baseHue) {
        // Draw left hand echo
        if (snapshot.leftHand && this.settings.showFingers) {
            this.drawHandGhost(snapshot.leftHand, alpha, offsetX, offsetY, colorOverride, 'left', baseHue);
        }

        // Draw right hand echo
        if (snapshot.rightHand && this.settings.showFingers) {
            this.drawHandGhost(snapshot.rightHand, alpha, offsetX, offsetY, colorOverride, 'right', baseHue);
        }
    }

    drawHandGhost(hand, alpha, offsetX, offsetY, colorOverride, handedness, baseHue) {
        if (alpha <= 0) return;

        const s = this.settings;

        // Draw palm if enabled
        if (s.showPalm && hand.palm) {
            const palmX = hand.palm.x + offsetX;
            const palmY = hand.palm.y + offsetY;

            const palmHue = handedness === 'left' ? baseHue - 20 : baseHue + 20;
            const color = colorOverride || `hsla(${palmHue}, 70%, 60%, `;

            this.ctx.shadowColor = color.replace('(', '(').replace(', ', ', 80%, 60%)');
            this.ctx.fillStyle = color + alpha + ')';
            this.ctx.beginPath();
            this.ctx.arc(palmX, palmY, s.palmSize, 0, Math.PI * 2);
            this.ctx.fill();
        }

        // Draw fingertips
        if (s.showFingers && hand.fingertips) {
            for (const fingertip of hand.fingertips) {
                const x = fingertip.x + offsetX;
                const y = fingertip.y + offsetY;

                const hue = (baseHue + fingertip.fingerIndex * 30) % 360;
                const color = colorOverride || `hsla(${hue}, 80%, 60%, `;

                this.ctx.shadowColor = color.replace('(', '(').replace(', ', ', 90%, 70%)');
                this.ctx.fillStyle = color + alpha + ')';
                this.ctx.beginPath();
                this.ctx.arc(x, y, s.fingerSize, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }
    }

    drawMotionBlurConnections(snapshot1, snapshot2, alpha, baseHue) {
        if (alpha <= 0) return;

        this.ctx.lineWidth = 2;
        this.ctx.lineCap = 'round';

        // Connect left hand fingertips
        if (snapshot1.leftHand && snapshot2.leftHand) {
            for (let i = 0; i < snapshot1.leftHand.fingertips.length; i++) {
                const ft1 = snapshot1.leftHand.fingertips[i];
                const ft2 = snapshot2.leftHand.fingertips[i];

                const hue = (baseHue + i * 30) % 360;
                this.ctx.strokeStyle = `hsla(${hue}, 80%, 60%, ${alpha})`;

                this.ctx.beginPath();
                this.ctx.moveTo(ft1.x, ft1.y);
                this.ctx.lineTo(ft2.x, ft2.y);
                this.ctx.stroke();
            }
        }

        // Connect right hand fingertips
        if (snapshot1.rightHand && snapshot2.rightHand) {
            for (let i = 0; i < snapshot1.rightHand.fingertips.length; i++) {
                const ft1 = snapshot1.rightHand.fingertips[i];
                const ft2 = snapshot2.rightHand.fingertips[i];

                const hue = (baseHue + i * 30) % 360;
                this.ctx.strokeStyle = `hsla(${hue}, 80%, 60%, ${alpha})`;

                this.ctx.beginPath();
                this.ctx.moveTo(ft1.x, ft1.y);
                this.ctx.lineTo(ft2.x, ft2.y);
                this.ctx.stroke();
            }
        }
    }

    updateSettings(newSettings) {
        Object.assign(this.settings, newSettings);
    }

    clearHistory() {
        this.handHistory = [];
    }
}
