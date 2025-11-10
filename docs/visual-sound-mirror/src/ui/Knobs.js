// Knobs.js - Virtual knob controls for audio parameters

export class Knobs {
    constructor(canvas) {
        this.canvas = canvas;
        this.knobs = [];
        this.activeKnob = null;
        this.init();
    }

    init() {
        // Smaller knobs positioned in top-left corner
        const knobRadius = 40;
        const padding = 20;
        const spacing = 100;

        // Position in top-left
        const startX = padding + knobRadius;
        const startY = padding + knobRadius;

        this.knobs = [
            { x: startX, y: startY, radius: knobRadius, value: 0.5, label: 'Filter', param: 'filter', angle: 0 },
            { x: startX + spacing, y: startY, radius: knobRadius, value: 0.3, label: 'Reverb', param: 'reverb', angle: 0 },
            { x: startX + spacing * 2, y: startY, radius: knobRadius, value: 0.4, label: 'Delay', param: 'delay', angle: 0 },
            { x: startX + spacing * 3, y: startY, radius: knobRadius, value: 0.7, label: 'Res', param: 'resonance', angle: 0 }
        ];
    }

    detect(leftHand, rightHand) {
        if (!leftHand && !rightHand) return;

        const hands = [];
        if (leftHand) hands.push(leftHand);
        if (rightHand) hands.push(rightHand);

        for (const hand of hands) {
            // Require BOTH thumb and index finger for pinch control
            const thumb = hand.fingertips[0];
            const index = hand.fingertips[1];

            for (const knob of this.knobs) {
                // Check if both fingers are inside knob area
                const thumbDist = Math.sqrt(
                    Math.pow(thumb.x - knob.x, 2) +
                    Math.pow(thumb.y - knob.y, 2)
                );
                const indexDist = Math.sqrt(
                    Math.pow(index.x - knob.x, 2) +
                    Math.pow(index.y - knob.y, 2)
                );

                // Both fingers must be within the knob radius
                if (thumbDist < knob.radius && indexDist < knob.radius) {
                    // Calculate pinch center (midpoint between thumb and index)
                    const pinchX = (thumb.x + index.x) / 2;
                    const pinchY = (thumb.y + index.y) / 2;

                    // Calculate angle from knob center to pinch center
                    const dx = pinchX - knob.x;
                    const dy = pinchY - knob.y;
                    const angle = Math.atan2(dy, dx);

                    // Map angle to value (0-1)
                    // Start at bottom (-π/2) and rotate clockwise
                    const startAngle = -Math.PI / 2;
                    const normalizedAngle = ((angle - startAngle + 2 * Math.PI) % (2 * Math.PI)) / (2 * Math.PI);
                    knob.value = Math.max(0, Math.min(1, normalizedAngle));

                    this.activeKnob = knob;
                    break;
                } else {
                    // Reset active knob if fingers leave
                    if (this.activeKnob === knob) {
                        this.activeKnob = null;
                    }
                }
            }
        }
    }

    apply(audioContext, filterNode, delayGain) {
        if (!audioContext) return;

        const now = audioContext.currentTime;

        for (const knob of this.knobs) {
            switch (knob.param) {
                case 'filter':
                    const filterFreq = 200 + knob.value * 3800;
                    filterNode.frequency.linearRampToValueAtTime(filterFreq, now + 0.1);
                    break;
                case 'reverb':
                    // Can't easily change reverb, but could implement dry/wet mix
                    break;
                case 'delay':
                    const delayMix = knob.value * 0.7;
                    delayGain.gain.linearRampToValueAtTime(delayMix, now + 0.1);
                    break;
                case 'resonance':
                    const resonance = 0.1 + knob.value * 19.9; // Q: 0.1-20
                    filterNode.Q.linearRampToValueAtTime(resonance, now + 0.1);
                    break;
            }
        }
    }

    render(ctx) {
        // Draw virtual knobs (global controls, always visible)
        for (const knob of this.knobs) {
            // Knob background circle
            ctx.fillStyle = 'rgba(50, 50, 60, 0.7)';
            ctx.beginPath();
            ctx.arc(knob.x, knob.y, knob.radius, 0, Math.PI * 2);
            ctx.fill();

            // Knob ring
            ctx.strokeStyle = 'rgba(100, 150, 200, 0.6)';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.arc(knob.x, knob.y, knob.radius, 0, Math.PI * 2);
            ctx.stroke();

            // Value indicator (arc from bottom)
            const startAngle = Math.PI * 0.75; // Start at 135 degrees
            const endAngle = startAngle + (knob.value * Math.PI * 1.5); // 270 degree range

            ctx.strokeStyle = 'rgba(100, 200, 255, 0.9)';
            ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.arc(knob.x, knob.y, knob.radius - 8, startAngle, endAngle);
            ctx.stroke();

            // Knob pointer
            const pointerAngle = startAngle + (knob.value * Math.PI * 1.5);
            const pointerX = knob.x + Math.cos(pointerAngle) * (knob.radius - 10);
            const pointerY = knob.y + Math.sin(pointerAngle) * (knob.radius - 10);

            ctx.strokeStyle = 'rgba(255, 255, 255, 0.9)';
            ctx.lineWidth = 3;
            ctx.lineCap = 'round';
            ctx.beginPath();
            ctx.moveTo(knob.x, knob.y);
            ctx.lineTo(pointerX, pointerY);
            ctx.stroke();

            // Knob label
            ctx.fillStyle = 'rgba(200, 200, 220, 0.9)';
            ctx.font = '12px monospace';
            ctx.textAlign = 'center';
            ctx.fillText(knob.label, knob.x, knob.y + knob.radius + 15);
        }

        // Reset text properties
        ctx.textAlign = 'left';
        ctx.textBaseline = 'alphabetic';
    }

    getKnobs() {
        return this.knobs;
    }
}
