// PadsMode.js - Sample pad system with calibration and tap detection

export class PadsMode {
    constructor(canvas) {
        this.canvas = canvas;
        this.pads = [];
        
        // Pad calibration state
        this.padCalibration = {
            calibrated: false,
            fingertipPositions: [],
            fingertipDistances: [],
            handCenter: null,
            scale: 1.0
        };

        // Pad tuning parameters
        this.padSettings = {
            basePadSize: 70,
            spacingMultiplier: 0.8,
            tapAlgorithm: 'z-velocity',
            zThreshold: 0.02,
            dwellTime: 200,
            wiggleThreshold: 10,
            retreatThreshold: 0.02,
            retriggerDelay: 100
        };
    }

    init() {
        const padsPerFinger = 5;

        // Define sounds for each finger's arc
        const fingerSounds = [
            ['kick', 'bass1', 'bass2', 'bass3', 'subkick'],           // Thumb
            ['snare', 'rimshot', 'clap', 'snap', 'sidestick'],        // Index
            ['hihat', 'hihat_open', 'crash', 'ride', 'splash'],       // Middle
            ['tom1', 'tom2', 'tom3', 'conga', 'bongo'],               // Ring
            ['chord1', 'chord2', 'lead', 'fx1', 'fx2']                // Pinky
        ];

        this.pads = [];

        if (this.padCalibration.calibrated && this.padCalibration.fingertipPositions.length === 5) {
            // Use calibrated hand geometry
            console.log('Using calibrated pad layout');
            const scale = this.padCalibration.scale;
            const padSize = Math.max(40, Math.min(120, this.padSettings.basePadSize * scale));
            const padSpacing = padSize * this.padSettings.spacingMultiplier;

            for (let finger = 0; finger < 5; finger++) {
                const fingertip = this.padCalibration.fingertipPositions[finger];
                const handCenter = this.padCalibration.handCenter;

                const dx = fingertip.x - handCenter.x;
                const dy = fingertip.y - handCenter.y;
                const angle = Math.atan2(dy, dx);

                for (let padIdx = 0; padIdx < padsPerFinger; padIdx++) {
                    const distance = padSpacing * (padIdx + 1);
                    const x = fingertip.x + Math.cos(angle) * distance;
                    const y = fingertip.y + Math.sin(angle) * distance;

                    const clampedX = Math.max(padSize / 2, Math.min(this.canvas.width - padSize / 2, x));
                    const clampedY = Math.max(padSize / 2, Math.min(this.canvas.height - padSize / 2, y));

                    this.pads.push({
                        x: clampedX - padSize / 2,
                        y: clampedY - padSize / 2,
                        size: padSize,
                        centerX: clampedX,
                        centerY: clampedY,
                        type: fingerSounds[finger][padIdx],
                        fingerIndex: finger,
                        triggered: false,
                        triggerTime: 0,
                        lastZ: null,
                        dwellStartTime: null,
                        lastXY: null,
                        color: this.getPadColor(fingerSounds[finger][padIdx])
                    });
                }
            }
        } else {
            // Use default static layout
            console.log('Using default pad layout (not calibrated)');
            const centerX = this.canvas.width / 2;
            const centerY = this.canvas.height * 0.7;
            const arcRadius = 200;
            const padSize = 50;

            for (let finger = 0; finger < 5; finger++) {
                const baseAngle = -Math.PI / 2;
                const angleSpread = Math.PI * 0.6;
                const startAngle = baseAngle - angleSpread / 2 + (finger * angleSpread / 4);

                for (let padIdx = 0; padIdx < padsPerFinger; padIdx++) {
                    const angle = startAngle + (padIdx / (padsPerFinger - 1)) * (angleSpread / 5);
                    const radius = arcRadius + (finger * 35);
                    const distance = radius - (padIdx * 30);

                    const x = centerX + Math.cos(angle) * distance;
                    const y = centerY + Math.sin(angle) * distance;

                    this.pads.push({
                        x: x - padSize / 2,
                        y: y - padSize / 2,
                        size: padSize,
                        centerX: x,
                        centerY: y,
                        type: fingerSounds[finger][padIdx],
                        fingerIndex: finger,
                        triggered: false,
                        triggerTime: 0,
                        lastZ: null,
                        color: this.getPadColor(fingerSounds[finger][padIdx])
                    });
                }
            }
        }
    }

    calibrateFromHand(hand) {
        if (!hand || !hand.fingertips) return;

        console.log('Calibrating pads from hand geometry');
        
        this.padCalibration.fingertipPositions = hand.fingertips.map(tip => ({
            x: tip.x,
            y: tip.y
        }));

        this.padCalibration.handCenter = {
            x: hand.palm.x,
            y: hand.palm.y
        };

        const distances = [];
        for (let i = 0; i < hand.fingertips.length - 1; i++) {
            const tip1 = hand.fingertips[i];
            const tip2 = hand.fingertips[i + 1];
            const dist = Math.sqrt(
                Math.pow(tip2.x - tip1.x, 2) +
                Math.pow(tip2.y - tip1.y, 2)
            );
            distances.push(dist);
        }
        
        const avgDist = distances.reduce((a, b) => a + b, 0) / distances.length;
        const referenceDistance = 80;
        this.padCalibration.scale = avgDist / referenceDistance;
        
        this.padCalibration.fingertipDistances = distances;
        this.padCalibration.calibrated = true;
        
        console.log('Calibration complete:', {
            scale: this.padCalibration.scale.toFixed(2),
            avgFingerSpacing: avgDist.toFixed(0)
        });
    }

    detect(leftHand, audioCallback) {
        if (!leftHand || !leftHand.fingertips) return;

        const now = Date.now();

        for (const fingertip of leftHand.fingertips) {
            for (const pad of this.pads) {
                if (pad.fingerIndex !== fingertip.fingerIndex) continue;

                const dist = Math.sqrt(
                    Math.pow(fingertip.x - pad.centerX, 2) +
                    Math.pow(fingertip.y - pad.centerY, 2)
                );

                if (dist < pad.size * 1.5) {
                    let shouldTrigger = false;

                    switch (this.padSettings.tapAlgorithm) {
                        case 'z-velocity':
                            shouldTrigger = this.detectTap_ZVelocity(pad, fingertip, now);
                            break;
                        case 'dwell-retreat':
                            shouldTrigger = this.detectTap_DwellRetreat(pad, fingertip, now);
                            break;
                        case 'wiggle':
                            shouldTrigger = this.detectTap_Wiggle(pad, fingertip, now);
                            break;
                        case 'hybrid':
                            shouldTrigger = this.detectTap_Hybrid(pad, fingertip, now);
                            break;
                    }

                    if (shouldTrigger) {
                        const cooldownElapsed = now - pad.triggerTime;
                        if (cooldownElapsed >= this.padSettings.retriggerDelay) {
                            if (audioCallback) audioCallback(pad.type);
                            pad.triggered = true;
                            pad.triggerTime = now;
                        }
                    }
                }

                if (pad.triggered && now - pad.triggerTime > 200) {
                    pad.triggered = false;
                }
            }
        }
    }

    detectTap_ZVelocity(pad, fingertip, now) {
        if (pad.lastZ !== null) {
            const zVelocity = fingertip.z - pad.lastZ;
            if (zVelocity > this.padSettings.zThreshold) {
                pad.lastZ = fingertip.z;
                return true;
            }
        }
        pad.lastZ = fingertip.z;
        return false;
    }

    detectTap_DwellRetreat(pad, fingertip, now) {
        if (pad.dwellStartTime === null) {
            pad.dwellStartTime = now;
            pad.lastZ = fingertip.z;
            return false;
        }

        const dwellDuration = now - pad.dwellStartTime;
        if (dwellDuration >= this.padSettings.dwellTime) {
            const zVelocity = fingertip.z - pad.lastZ;
            if (zVelocity < -this.padSettings.retreatThreshold) {
                pad.dwellStartTime = null;
                pad.lastZ = fingertip.z;
                return true;
            }
        }
        
        pad.lastZ = fingertip.z;
        return false;
    }

    detectTap_Wiggle(pad, fingertip, now) {
        if (pad.lastXY === null) {
            pad.lastXY = { x: fingertip.x, y: fingertip.y };
            return false;
        }

        const xyDist = Math.sqrt(
            Math.pow(fingertip.x - pad.lastXY.x, 2) +
            Math.pow(fingertip.y - pad.lastXY.y, 2)
        );

        if (xyDist > this.padSettings.wiggleThreshold) {
            pad.lastXY = { x: fingertip.x, y: fingertip.y };
            return true;
        }

        pad.lastXY = { x: fingertip.x, y: fingertip.y };
        return false;
    }

    detectTap_Hybrid(pad, fingertip, now) {
        const zVelocityTriggered = this.detectTap_ZVelocity(pad, fingertip, now);
        const wiggleTriggered = this.detectTap_Wiggle(pad, fingertip, now);
        return zVelocityTriggered || wiggleTriggered;
    }

    render(ctx, leftHand) {
        for (const pad of this.pads) {
            const triggered = pad.triggered;
            const alpha = triggered ? 0.9 : 0.5;
            const scale = triggered ? 1.1 : 1.0;

            ctx.fillStyle = `rgba(${pad.color.r}, ${pad.color.g}, ${pad.color.b}, ${alpha})`;
            ctx.strokeStyle = triggered ? 'rgba(255, 255, 255, 0.9)' : 'rgba(255, 255, 255, 0.4)';
            ctx.lineWidth = triggered ? 3 : 1.5;

            const size = pad.size * scale;
            const x = pad.centerX - size / 2;
            const y = pad.centerY - size / 2;

            ctx.fillRect(x, y, size, size);
            ctx.strokeRect(x, y, size, size);
        }

        if (leftHand && leftHand.fingertips) {
            ctx.fillStyle = 'rgba(255, 255, 255, 0.6)';
            for (const tip of leftHand.fingertips) {
                ctx.beginPath();
                ctx.arc(tip.x, tip.y, 8, 0, Math.PI * 2);
                ctx.fill();
            }
        }
    }

    getPadColor(type) {
        const colors = {
            kick: { r: 255, g: 60, b: 60 },
            bass1: { r: 200, g: 40, b: 40 },
            bass2: { r: 180, g: 60, b: 40 },
            bass3: { r: 160, g: 80, b: 60 },
            subkick: { r: 120, g: 40, b: 40 },
            snare: { r: 60, g: 150, b: 255 },
            rimshot: { r: 80, g: 180, b: 255 },
            clap: { r: 100, g: 200, b: 255 },
            snap: { r: 120, g: 220, b: 255 },
            sidestick: { r: 60, g: 120, b: 200 },
            hihat: { r: 200, g: 200, b: 60 },
            hihat_open: { r: 220, g: 220, b: 100 },
            crash: { r: 240, g: 240, b: 240 },
            ride: { r: 200, g: 200, b: 200 },
            splash: { r: 255, g: 255, b: 150 },
            tom1: { r: 180, g: 80, b: 200 },
            tom2: { r: 160, g: 100, b: 220 },
            tom3: { r: 140, g: 120, b: 240 },
            conga: { r: 200, g: 100, b: 180 },
            bongo: { r: 220, g: 120, b: 200 },
            chord1: { r: 100, g: 200, b: 100 },
            chord2: { r: 80, g: 220, b: 120 },
            lead: { r: 100, g: 255, b: 150 },
            fx1: { r: 60, g: 200, b: 200 },
            fx2: { r: 80, g: 180, b: 220 }
        };
        return colors[type] || { r: 150, g: 150, b: 150 };
    }

    updateSettings(settings) {
        Object.assign(this.padSettings, settings);
    }

    getPads() {
        return this.pads;
    }

    getCalibration() {
        return this.padCalibration;
    }
}
