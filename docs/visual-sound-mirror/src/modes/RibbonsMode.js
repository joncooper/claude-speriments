// RibbonsMode.js - Flowing finger ribbons visualization

export class RibbonsMode {
    constructor(canvas, ctx) {
        this.canvas = canvas;
        this.ctx = ctx;
    }

    render(leftHand, rightHand, fingerTrails, touchingFingers, settings, getColorCallback) {
        const hands = [leftHand, rightHand].filter(h => h);

        for (const hand of hands) {
            for (const tip of hand.fingertips) {
                const trail = fingerTrails[tip.fingerId];
                if (!trail || trail.length < 2) continue;

                // Draw multiple parallel ribbons for each finger
                for (let offset = -settings.ribbonOffsets; offset <= settings.ribbonOffsets; offset++) {
                    this.ctx.beginPath();
                    this.ctx.lineWidth = settings.ribbonWidth;
                    this.ctx.lineCap = 'round';
                    this.ctx.lineJoin = 'round';

                    const color = getColorCallback(tip.fingerIndex, hand.handedness, trail[0].time * 0.001);
                    const alpha = 0.3 + (Math.abs(offset) / settings.ribbonOffsets) * 0.3;
                    this.ctx.strokeStyle = `rgba(${color.r}, ${color.g}, ${color.b}, ${alpha})`;

                    for (let i = 0; i < trail.length; i++) {
                        const point = trail[i];
                        const offsetDist = offset * settings.ribbonSpacing;

                        let perpX = 0, perpY = 0;
                        if (i < trail.length - 1) {
                            const next = trail[i + 1];
                            const dx = next.x - point.x;
                            const dy = next.y - point.y;
                            const len = Math.sqrt(dx * dx + dy * dy) || 1;
                            perpX = -dy / len * offsetDist;
                            perpY = dx / len * offsetDist;
                        }

                        const x = point.x + perpX;
                        const y = point.y + perpY;

                        if (i === 0) {
                            this.ctx.moveTo(x, y);
                        } else {
                            this.ctx.lineTo(x, y);
                        }
                    }

                    this.ctx.stroke();
                }

                // Draw fingertip glow
                const color = getColorCallback(tip.fingerIndex, hand.handedness, 0);
                const gradient = this.ctx.createRadialGradient(tip.x, tip.y, 0, tip.x, tip.y, 15);
                gradient.addColorStop(0, `rgba(${color.r}, ${color.g}, ${color.b}, 0.8)`);
                gradient.addColorStop(1, `rgba(${color.r}, ${color.g}, ${color.b}, 0)`);
                this.ctx.fillStyle = gradient;
                this.ctx.fillRect(tip.x - 15, tip.y - 15, 30, 30);
            }
        }

        // Draw connections between touching fingers
        if (touchingFingers && touchingFingers.length > 0) {
            for (const touch of touchingFingers) {
                this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.6)';
                this.ctx.lineWidth = 2;
                this.ctx.beginPath();
                this.ctx.moveTo(touch.left.x, touch.left.y);
                this.ctx.lineTo(touch.right.x, touch.right.y);
                this.ctx.stroke();

                const midX = (touch.left.x + touch.right.x) / 2;
                const midY = (touch.left.y + touch.right.y) / 2;
                const gradient = this.ctx.createRadialGradient(midX, midY, 0, midX, midY, 20);
                gradient.addColorStop(0, 'rgba(255, 255, 255, 0.8)');
                gradient.addColorStop(1, 'rgba(255, 200, 100, 0)');
                this.ctx.fillStyle = gradient;
                this.ctx.beginPath();
                this.ctx.arc(midX, midY, 20, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }
    }
}
