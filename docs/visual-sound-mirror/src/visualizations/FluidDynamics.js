// FluidDynamics.js - Flowing smoke/fluid effect around fingertips

export class FluidDynamics {
    constructor(canvas, ctx) {
        this.canvas = canvas;
        this.ctx = ctx;

        this.settings = {
            tendrilCount: 8,           // Tendrils per fingertip (3-15)
            tendrilRadius: 25,         // Distance from center (10-60)
            flowSpeed: 0.002,          // Rotation speed (0.0005-0.01)
            pulseAmount: 10,           // Radius pulsing (0-30)
            gradientSize: 40,          // Gradient radius (20-80)
            opacity: 0.5,              // Base opacity (0.2-0.8)
            trailPersistence: 0.92,    // How long trails last (0.8-0.98)
            velocityInfluence: 2.0     // How much movement affects flow (0-5)
        };
    }

    render(leftHand, rightHand, prevLeftHand, prevRightHand, baseHue, time) {
        if (!leftHand && !rightHand) return;

        const s = this.settings;
        const hands = [];
        if (leftHand) hands.push({ hand: leftHand, prev: prevLeftHand });
        if (rightHand) hands.push({ hand: rightHand, prev: prevRightHand });

        // Apply trail persistence for smokey effect
        this.ctx.fillStyle = `rgba(0, 0, 0, ${1 - s.trailPersistence})`;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        this.ctx.shadowBlur = 25;

        for (const { hand, prev } of hands) {
            if (!hand.fingertips) continue;

            for (const fingertip of hand.fingertips) {
                // Calculate velocity
                let velocity = { x: 0, y: 0 };
                let velocityMag = 0;
                if (prev && prev.fingertips[fingertip.fingerIndex]) {
                    const prevFinger = prev.fingertips[fingertip.fingerIndex];
                    velocity.x = (fingertip.x - prevFinger.x) * s.velocityInfluence;
                    velocity.y = (fingertip.y - prevFinger.y) * s.velocityInfluence;
                    velocityMag = Math.sqrt(velocity.x * velocity.x + velocity.y * velocity.y);
                }

                // Draw flowing smoke tendrils
                const hue = (baseHue + fingertip.fingerIndex * 30) % 360;

                for (let i = 0; i < s.tendrilCount; i++) {
                    // Rotating flow with velocity influence
                    const baseAngle = (i / s.tendrilCount) * Math.PI * 2;
                    const flowAngle = baseAngle + time * s.flowSpeed + fingertip.fingerIndex * 0.5;

                    // Pulsing radius
                    const pulse = Math.sin(time * 0.003 + i) * s.pulseAmount;
                    const radius = s.tendrilRadius + pulse;

                    // Add velocity offset for flow field effect
                    const x = fingertip.x + Math.cos(flowAngle) * radius + velocity.x * 0.5;
                    const y = fingertip.y + Math.sin(flowAngle) * radius + velocity.y * 0.5;

                    // Draw gradient circle with dynamic opacity
                    const dynamicOpacity = s.opacity * (1 + velocityMag * 0.02);
                    const gradient = this.ctx.createRadialGradient(x, y, 0, x, y, s.gradientSize);
                    gradient.addColorStop(0, `hsla(${hue}, 70%, 60%, ${dynamicOpacity})`);
                    gradient.addColorStop(1, `hsla(${hue}, 70%, 60%, 0)`);

                    this.ctx.fillStyle = gradient;
                    this.ctx.fillRect(x - s.gradientSize, y - s.gradientSize, s.gradientSize * 2, s.gradientSize * 2);
                }

                // Draw connecting wisps between tendrils for more fluid feel
                this.ctx.strokeStyle = `hsla(${hue}, 70%, 60%, ${s.opacity * 0.3})`;
                this.ctx.lineWidth = 2;
                this.ctx.beginPath();
                for (let i = 0; i < s.tendrilCount; i++) {
                    const angle1 = (i / s.tendrilCount) * Math.PI * 2 + time * s.flowSpeed;
                    const angle2 = ((i + 1) / s.tendrilCount) * Math.PI * 2 + time * s.flowSpeed;
                    const x1 = fingertip.x + Math.cos(angle1) * s.tendrilRadius;
                    const y1 = fingertip.y + Math.sin(angle1) * s.tendrilRadius;
                    const x2 = fingertip.x + Math.cos(angle2) * s.tendrilRadius;
                    const y2 = fingertip.y + Math.sin(angle2) * s.tendrilRadius;

                    if (i === 0) this.ctx.moveTo(x1, y1);
                    this.ctx.lineTo(x2, y2);
                }
                this.ctx.stroke();
            }
        }

        this.ctx.shadowBlur = 0;
    }

    updateSettings(newSettings) {
        Object.assign(this.settings, newSettings);
    }
}
