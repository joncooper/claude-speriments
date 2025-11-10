// HandTracker.js - MediaPipe hand tracking and gesture detection

import { FINGERTIP_INDICES } from '../utils/Constants.js';

export class HandTracker {
    constructor(video, canvas) {
        this.video = video;
        this.canvas = canvas;
        this.hands = null;
        this.camera = null;

        // Hand data
        this.handResults = null;
        this.leftHand = null;
        this.rightHand = null;
        this.prevLeftHand = null;
        this.prevRightHand = null;

        // Finger trails
        this.fingerTrails = {};
        this.maxTrailLength = 25;

        // Two-hand gestures
        this.handsDistance = 0;
        this.handsAreTouching = false;
        this.touchingFingers = [];

        // No hands timer
        this.noHandsTime = 0;
        this.fadeoutStarted = false;

        // Time for trails
        this.time = 0;
    }

    async init() {
        this.hands = new Hands({
            locateFile: (file) => {
                return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
            }
        });

        this.hands.setOptions({
            maxNumHands: 2,
            modelComplexity: 1,
            minDetectionConfidence: 0.6,
            minTrackingConfidence: 0.6
        });

        this.hands.onResults((results) => this.processResults(results));

        this.camera = new Camera(this.video, {
            onFrame: async () => {
                await this.hands.send({ image: this.video });
            },
            width: 640,
            height: 480
        });

        await this.camera.start();
    }

    processResults(results) {
        this.handResults = results;
        this.prevLeftHand = this.leftHand;
        this.prevRightHand = this.rightHand;
        this.leftHand = null;
        this.rightHand = null;

        if (results.multiHandLandmarks && results.multiHandLandmarks.length > 0) {
            this.noHandsTime = 0;
            this.fadeoutStarted = false;

            for (let handIndex = 0; handIndex < results.multiHandLandmarks.length; handIndex++) {
                const landmarks = results.multiHandLandmarks[handIndex];
                const handedness = results.multiHandedness[handIndex].label; // "Left" or "Right"

                // Get fingertips (mirror X for canvas mapping to match user perspective)
                const fingertips = FINGERTIP_INDICES.map((idx, i) => ({
                    x: (1 - landmarks[idx].x) * this.canvas.width,
                    y: landmarks[idx].y * this.canvas.height,
                    z: landmarks[idx].z,
                    fingerIndex: i,
                    fingerId: `${handedness}_finger${i}`
                }));

                // Calculate palm position (mirror X for canvas mapping)
                const palm = {
                    x: (1 - landmarks[9].x) * this.canvas.width,
                    y: landmarks[9].y * this.canvas.height,
                    z: landmarks[9].z
                };

                // Calculate finger spread (thumb to pinky distance)
                const thumb = fingertips[0];
                const pinky = fingertips[4];
                const fingerSpread = Math.sqrt(
                    Math.pow(pinky.x - thumb.x, 2) +
                    Math.pow(pinky.y - thumb.y, 2)
                );

                const handData = {
                    landmarks: landmarks,
                    fingertips: fingertips,
                    palm: palm,
                    fingerSpread: fingerSpread,
                    handedness: handedness
                };

                // Assign to left or right
                if (handedness === 'Left') {
                    this.leftHand = handData;
                } else {
                    this.rightHand = handData;
                }

                // Update trails for each finger
                for (const tip of fingertips) {
                    if (!this.fingerTrails[tip.fingerId]) {
                        this.fingerTrails[tip.fingerId] = [];
                    }

                    this.fingerTrails[tip.fingerId].push({
                        x: tip.x,
                        y: tip.y,
                        time: this.time
                    });

                    if (this.fingerTrails[tip.fingerId].length > this.maxTrailLength) {
                        this.fingerTrails[tip.fingerId].shift();
                    }
                }
            }

            // Detect two-hand gestures
            if (this.leftHand && this.rightHand) {
                this.detectTwoHandGestures();
            } else {
                this.handsAreTouching = false;
                this.touchingFingers = [];
            }

        } else {
            // No hands detected
            this.noHandsTime += 16;
            if (this.noHandsTime > 1000) {
                this.fadeoutStarted = true;
                this.fingerTrails = {};
            }
        }
    }

    detectTwoHandGestures() {
        // Calculate distance between palms
        const palmDist = Math.sqrt(
            Math.pow(this.rightHand.palm.x - this.leftHand.palm.x, 2) +
            Math.pow(this.rightHand.palm.y - this.leftHand.palm.y, 2)
        );

        this.handsDistance = palmDist;
        this.handsAreTouching = palmDist < 100;

        // Detect touching fingertips
        this.touchingFingers = [];
        for (const leftFinger of this.leftHand.fingertips) {
            for (const rightFinger of this.rightHand.fingertips) {
                const dist = Math.sqrt(
                    Math.pow(rightFinger.x - leftFinger.x, 2) +
                    Math.pow(rightFinger.y - leftFinger.y, 2)
                );

                if (dist < 40) {
                    this.touchingFingers.push({
                        left: leftFinger,
                        right: rightFinger,
                        distance: dist
                    });
                }
            }
        }
    }

    countExtendedFingers(landmarks) {
        // Check each finger individually with VERY strict requirements
        const wrist = landmarks[0];

        // Thumb: check if tip is significantly further from wrist than knuckle
        const thumbTip = landmarks[4];
        const thumbKnuckle = landmarks[2];
        const thumbTipDist = Math.hypot(thumbTip.x - wrist.x, thumbTip.y - wrist.y);
        const thumbKnuckleDist = Math.hypot(thumbKnuckle.x - wrist.x, thumbKnuckle.y - wrist.y);
        const thumbExtended = thumbTipDist > thumbKnuckleDist * 1.4;

        // Index finger
        const indexTip = landmarks[8];
        const indexPip = landmarks[6];
        const indexMcp = landmarks[5];
        const indexExtended = indexTip.y < indexPip.y - 0.06 && indexTip.y < indexMcp.y - 0.08;

        // Middle finger
        const middleTip = landmarks[12];
        const middlePip = landmarks[10];
        const middleMcp = landmarks[9];
        const middleExtended = middleTip.y < middlePip.y - 0.06 && middleTip.y < middleMcp.y - 0.08;

        // Ring finger
        const ringTip = landmarks[16];
        const ringPip = landmarks[14];
        const ringMcp = landmarks[13];
        const ringExtended = ringTip.y < ringPip.y - 0.06 && ringTip.y < ringMcp.y - 0.08;
        const ringCurled = ringTip.y > ringPip.y;

        // Pinky
        const pinkyTip = landmarks[20];
        const pinkyPip = landmarks[18];
        const pinkyMcp = landmarks[17];
        const pinkyExtended = pinkyTip.y < pinkyPip.y - 0.06 && pinkyTip.y < pinkyMcp.y - 0.08;
        const pinkyCurled = pinkyTip.y > pinkyPip.y;

        // STRICT GESTURE DETECTION:
        // 1 finger = ONLY index extended, others must be actively curled
        if (indexExtended && !middleExtended && !ringExtended && !pinkyExtended &&
            !thumbExtended && ringCurled && pinkyCurled) {
            return 1;
        }

        // 2 fingers (peace sign) = ONLY index + middle extended, others actively curled
        if (indexExtended && middleExtended && !ringExtended && !pinkyExtended &&
            !thumbExtended && ringCurled && pinkyCurled) {
            return 2;
        }

        // 5 fingers = all fingers extended
        if (thumbExtended && indexExtended && middleExtended && ringExtended && pinkyExtended) {
            return 5;
        }

        // Any other combination = 0 (no recognized gesture)
        return 0;
    }

    updateTime(time) {
        this.time = time;
    }

    getHands() {
        return {
            left: this.leftHand,
            right: this.rightHand,
            prevLeft: this.prevLeftHand,
            prevRight: this.prevRightHand
        };
    }

    getFingerTrails() {
        return this.fingerTrails;
    }

    getTouchingFingers() {
        return this.touchingFingers;
    }

    isHandsAreTouching() {
        return this.handsAreTouching;
    }
}
