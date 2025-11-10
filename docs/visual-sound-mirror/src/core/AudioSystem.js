// AudioSystem.js - Handles all audio synthesis and effects

import { SCALES } from '../utils/Constants.js';

export class AudioSystem {
    constructor() {
        this.audioContext = null;
        this.masterGain = null;
        this.filterNode = null;
        this.delayNode = null;
        this.delayGain = null;
        this.delayFeedback = null;
        this.reverb = null;
        this.audioEnabled = false;
        this.isMuted = false;

        // Theremin mode audio
        this.thereminOsc = null;
        this.thereminGain = null;
        this.thereminFilter = null;
        this.thereminActive = false;

        // Scale system for theremin mode
        this.scales = SCALES;
        this.currentScale = 'pentatonic';
        this.rootNote = 60; // Middle C (MIDI note number)
    }

    async init() {
        this.audioContext = new (window.AudioContext || window.webkitAudioContext)();

        const resumeAudio = async () => {
            if (this.audioContext.state === 'suspended') {
                await this.audioContext.resume();
                console.log('Audio context resumed!');
            }
        };

        document.body.addEventListener('click', resumeAudio, { once: true });
        document.body.addEventListener('touchstart', resumeAudio, { once: true });
        document.body.addEventListener('keydown', resumeAudio, { once: true });

        // Master gain
        this.masterGain = this.audioContext.createGain();
        this.masterGain.gain.value = 0.25;

        // Global filter (controlled by left hand finger spread)
        this.filterNode = this.audioContext.createBiquadFilter();
        this.filterNode.type = 'lowpass';
        this.filterNode.frequency.value = 2000;
        this.filterNode.Q.value = 1;

        // Delay effect (controlled by right hand finger spread)
        this.delayNode = this.audioContext.createDelay(1.0);
        this.delayNode.delayTime.value = 0.3;

        this.delayGain = this.audioContext.createGain();
        this.delayGain.gain.value = 0;

        this.delayFeedback = this.audioContext.createGain();
        this.delayFeedback.gain.value = 0.4;

        // Connect delay feedback loop
        this.delayNode.connect(this.delayFeedback);
        this.delayFeedback.connect(this.delayNode);
        this.delayNode.connect(this.delayGain);

        // Create reverb
        this.reverb = this.createReverb();

        // Audio chain: filter -> delay -> reverb -> master
        this.filterNode.connect(this.reverb);
        this.delayGain.connect(this.reverb);
        this.reverb.connect(this.masterGain);
        this.masterGain.connect(this.audioContext.destination);

        this.audioEnabled = true;
        console.log('Audio initialized with advanced routing');
    }

    createReverb() {
        const convolver = this.audioContext.createConvolver();
        const rate = this.audioContext.sampleRate;
        const length = rate * 3;
        const impulse = this.audioContext.createBuffer(2, length, rate);

        for (let channel = 0; channel < 2; channel++) {
            const channelData = impulse.getChannelData(channel);
            for (let i = 0; i < length; i++) {
                channelData[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / length, 2.5);
            }
        }

        convolver.buffer = impulse;
        return convolver;
    }

    toggleMute() {
        this.isMuted = !this.isMuted;
        if (this.masterGain && this.audioContext) {
            const now = this.audioContext.currentTime;
            this.masterGain.gain.linearRampToValueAtTime(
                this.isMuted ? 0 : 0.25,
                now + 0.1
            );
        }
        return this.isMuted;
    }

    // ===== THEREMIN MODE =====

    startTheremin() {
        if (!this.audioEnabled || this.isMuted || !this.audioContext || this.thereminActive) {
            return;
        }

        const now = this.audioContext.currentTime;

        // Create continuous oscillator
        this.thereminOsc = this.audioContext.createOscillator();
        this.thereminOsc.type = 'triangle';
        this.thereminOsc.frequency.value = 440;

        // Theremin-specific filter
        this.thereminFilter = this.audioContext.createBiquadFilter();
        this.thereminFilter.type = 'lowpass';
        this.thereminFilter.frequency.value = 2000;
        this.thereminFilter.Q.value = 5;

        // Theremin gain with smooth attack
        this.thereminGain = this.audioContext.createGain();
        this.thereminGain.gain.setValueAtTime(0, now);
        this.thereminGain.gain.linearRampToValueAtTime(0.3, now + 0.05);

        // Connect: osc -> filter -> gain -> reverb -> master
        this.thereminOsc.connect(this.thereminFilter);
        this.thereminFilter.connect(this.thereminGain);
        this.thereminGain.connect(this.reverb);

        this.thereminOsc.start(now);
        this.thereminActive = true;
        console.log('Theremin started');
    }

    stopTheremin() {
        if (!this.thereminActive || !this.thereminOsc) {
            return;
        }

        const now = this.audioContext.currentTime;

        // Smooth release
        this.thereminGain.gain.linearRampToValueAtTime(0, now + 0.2);

        setTimeout(() => {
            if (this.thereminOsc) {
                this.thereminOsc.stop();
                this.thereminOsc = null;
                this.thereminGain = null;
                this.thereminFilter = null;
            }
            this.thereminActive = false;
        }, 250);

        console.log('Theremin stopped');
    }

    updateTheremin(hand, canvas) {
        if (!this.thereminActive || !this.thereminOsc || !hand) {
            return;
        }

        const now = this.audioContext.currentTime;

        // X-axis controls pitch (quantized to scale)
        const normalizedX = hand.palm.x / canvas.width;
        const frequency = this.quantizeToScale(normalizedX);
        this.thereminOsc.frequency.exponentialRampToValueAtTime(frequency, now + 0.05);

        // Y-axis controls filter cutoff
        const normalizedY = hand.palm.y / canvas.height;
        const filterFreq = 200 + (1 - normalizedY) * 3800; // Inverted: top = bright
        this.thereminFilter.frequency.exponentialRampToValueAtTime(Math.max(200, filterFreq), now + 0.05);

        // Finger spread controls vibrato/resonance
        const spread = Math.max(50, Math.min(250, hand.fingerSpread));
        const resonance = 1 + ((spread - 50) / 200) * 15; // Q: 1-16
        this.thereminFilter.Q.linearRampToValueAtTime(resonance, now + 0.05);
    }

    // ===== DRUM SYNTHESIS =====

    playDrumSample(type) {
        if (!this.audioEnabled || this.isMuted || !this.audioContext) {
            return;
        }

        const now = this.audioContext.currentTime;

        try {
            switch (type) {
                // Thumb - Bass sounds
                case 'kick':
                    this.playKick(now);
                    break;
                case 'bass1':
                    this.playBass(now, 55);
                    break;
                case 'bass2':
                    this.playBass(now, 65);
                    break;
                case 'bass3':
                    this.playBass(now, 82);
                    break;
                case 'subkick':
                    this.playKick(now, 100, 30);
                    break;

                // Index - Snares
                case 'snare':
                    this.playSnare(now);
                    break;
                case 'rimshot':
                    this.playRim(now, 600);
                    break;
                case 'clap':
                    this.playClap(now);
                    break;
                case 'snap':
                    this.playSnap(now);
                    break;
                case 'sidestick':
                    this.playRim(now, 800);
                    break;

                // Middle - Hi-hats/Cymbals
                case 'hihat':
                    this.playHihat(now, 0.1);
                    break;
                case 'hihat_open':
                    this.playHihat(now, 0.3);
                    break;
                case 'crash':
                    this.playCrash(now);
                    break;
                case 'ride':
                    this.playRide(now);
                    break;
                case 'splash':
                    this.playCrash(now, 0.8);
                    break;

                // Ring - Toms
                case 'tom1':
                    this.playTom(now, 120);
                    break;
                case 'tom2':
                    this.playTom(now, 90);
                    break;
                case 'tom3':
                    this.playTom(now, 70);
                    break;
                case 'conga':
                    this.playTom(now, 200);
                    break;
                case 'bongo':
                    this.playTom(now, 250);
                    break;

                // Pinky - Synths
                case 'chord1':
                    this.playChordPad(now, [261.63, 329.63, 392.00]); // C major
                    break;
                case 'chord2':
                    this.playChordPad(now, [293.66, 349.23, 440.00]); // D minor
                    break;
                case 'lead':
                    this.playLead(now);
                    break;
                case 'fx1':
                    this.playFX(now, 800, 2000);
                    break;
                case 'fx2':
                    this.playFX(now, 400, 1200);
                    break;
            }
        } catch (error) {
            console.error('Error playing drum sample:', error);
        }
    }

    playKick(now, startFreq = 150, endFreq = 40) {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();

        osc.frequency.setValueAtTime(startFreq, now);
        osc.frequency.exponentialRampToValueAtTime(endFreq, now + 0.1);

        gain.gain.setValueAtTime(1, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.5);

        osc.connect(gain);
        gain.connect(this.masterGain);

        osc.start(now);
        osc.stop(now + 0.5);
    }

    playSnare(now) {
        // Tone component
        const osc = this.audioContext.createOscillator();
        const oscGain = this.audioContext.createGain();
        osc.frequency.value = 200;
        oscGain.gain.setValueAtTime(0.3, now);
        oscGain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
        osc.connect(oscGain);

        // Noise component
        const bufferSize = this.audioContext.sampleRate * 0.2;
        const buffer = this.audioContext.createBuffer(1, bufferSize, this.audioContext.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
            data[i] = Math.random() * 2 - 1;
        }

        const noise = this.audioContext.createBufferSource();
        noise.buffer = buffer;
        const noiseGain = this.audioContext.createGain();
        noiseGain.gain.setValueAtTime(0.5, now);
        noiseGain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
        noise.connect(noiseGain);

        oscGain.connect(this.masterGain);
        noiseGain.connect(this.masterGain);

        osc.start(now);
        osc.stop(now + 0.2);
        noise.start(now);
    }

    playHihat(now, decay = 0.1) {
        const bufferSize = this.audioContext.sampleRate * decay;
        const buffer = this.audioContext.createBuffer(1, bufferSize, this.audioContext.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
            data[i] = Math.random() * 2 - 1;
        }

        const noise = this.audioContext.createBufferSource();
        noise.buffer = buffer;

        const filter = this.audioContext.createBiquadFilter();
        filter.type = 'highpass';
        filter.frequency.value = 7000;

        const gain = this.audioContext.createGain();
        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + decay);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(this.masterGain);

        noise.start(now);
    }

    playClap(now) {
        for (let i = 0; i < 3; i++) {
            const delay = i * 0.02;
            const bufferSize = this.audioContext.sampleRate * 0.1;
            const buffer = this.audioContext.createBuffer(1, bufferSize, this.audioContext.sampleRate);
            const data = buffer.getChannelData(0);
            for (let j = 0; j < bufferSize; j++) {
                data[j] = Math.random() * 2 - 1;
            }

            const noise = this.audioContext.createBufferSource();
            noise.buffer = buffer;
            const gain = this.audioContext.createGain();
            gain.gain.setValueAtTime(0.4, now + delay);
            gain.gain.exponentialRampToValueAtTime(0.01, now + delay + 0.15);

            noise.connect(gain);
            gain.connect(this.masterGain);
            noise.start(now + delay);
        }
    }

    playTom(now, freq) {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();

        osc.frequency.setValueAtTime(freq, now);
        osc.frequency.exponentialRampToValueAtTime(freq * 0.5, now + 0.3);

        gain.gain.setValueAtTime(0.7, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);

        osc.connect(gain);
        gain.connect(this.masterGain);

        osc.start(now);
        osc.stop(now + 0.3);
    }

    playRim(now, freq = 400) {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();
        osc.frequency.value = freq;
        osc.type = 'square';

        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.05);

        osc.connect(gain);
        gain.connect(this.masterGain);

        osc.start(now);
        osc.stop(now + 0.05);
    }

    playSnap(now) {
        // Short, sharp noise burst
        const bufferSize = this.audioContext.sampleRate * 0.05;
        const buffer = this.audioContext.createBuffer(1, bufferSize, this.audioContext.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
            data[i] = Math.random() * 2 - 1;
        }

        const noise = this.audioContext.createBufferSource();
        noise.buffer = buffer;

        const filter = this.audioContext.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.value = 2000;
        filter.Q.value = 10;

        const gain = this.audioContext.createGain();
        gain.gain.setValueAtTime(0.5, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.05);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(this.masterGain);

        noise.start(now);
    }

    playCowbell(now) {
        const osc1 = this.audioContext.createOscillator();
        const osc2 = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();

        osc1.frequency.value = 540;
        osc2.frequency.value = 800;
        osc1.type = 'square';
        osc2.type = 'square';

        gain.gain.setValueAtTime(0.4, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);

        osc1.connect(gain);
        osc2.connect(gain);
        gain.connect(this.masterGain);

        osc1.start(now);
        osc2.start(now);
        osc1.stop(now + 0.2);
        osc2.stop(now + 0.2);
    }

    playCrash(now, decay = 1.5) {
        const bufferSize = this.audioContext.sampleRate * decay;
        const buffer = this.audioContext.createBuffer(1, bufferSize, this.audioContext.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
            data[i] = Math.random() * 2 - 1;
        }

        const noise = this.audioContext.createBufferSource();
        noise.buffer = buffer;

        const filter = this.audioContext.createBiquadFilter();
        filter.type = 'highpass';
        filter.frequency.value = 5000;

        const gain = this.audioContext.createGain();
        gain.gain.setValueAtTime(0.5, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + decay);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(this.masterGain);

        noise.start(now);
    }

    playRide(now) {
        const osc1 = this.audioContext.createOscillator();
        const osc2 = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();

        osc1.frequency.value = 3000;
        osc2.frequency.value = 4500;
        osc1.type = 'square';
        osc2.type = 'square';

        gain.gain.setValueAtTime(0.15, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.5);

        osc1.connect(gain);
        osc2.connect(gain);
        gain.connect(this.masterGain);

        osc1.start(now);
        osc2.start(now);
        osc1.stop(now + 0.5);
        osc2.stop(now + 0.5);
    }

    playPerc(now, freq) {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();
        osc.frequency.value = freq;
        osc.type = 'sine';

        gain.gain.setValueAtTime(0.4, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.15);

        osc.connect(gain);
        gain.connect(this.masterGain);

        osc.start(now);
        osc.stop(now + 0.15);
    }

    playBass(now, freq = 55) {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();
        osc.frequency.value = freq;
        osc.type = 'sawtooth';

        const filter = this.audioContext.createBiquadFilter();
        filter.type = 'lowpass';
        filter.frequency.value = 300;

        gain.gain.setValueAtTime(0.6, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.4);

        osc.connect(filter);
        filter.connect(gain);
        gain.connect(this.masterGain);

        osc.start(now);
        osc.stop(now + 0.4);
    }

    playFX(now, startFreq, endFreq) {
        // Sweep effect sound
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();
        osc.type = 'sawtooth';

        osc.frequency.setValueAtTime(startFreq, now);
        osc.frequency.exponentialRampToValueAtTime(endFreq, now + 0.4);

        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.4);

        osc.connect(gain);
        gain.connect(this.filterNode);

        osc.start(now);
        osc.stop(now + 0.4);
    }

    playChordPad(now, frequencies) {
        for (let i = 0; i < frequencies.length; i++) {
            const osc = this.audioContext.createOscillator();
            const gain = this.audioContext.createGain();
            osc.frequency.value = frequencies[i];
            osc.type = 'sawtooth';

            gain.gain.setValueAtTime(0.2, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 1.5);

            osc.connect(gain);
            gain.connect(this.filterNode);

            osc.start(now);
            osc.stop(now + 1.5);
        }
    }

    playLead(now) {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();
        osc.frequency.value = 523.25; // C5
        osc.type = 'square';

        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);

        osc.connect(gain);
        gain.connect(this.filterNode);

        osc.start(now);
        osc.stop(now + 0.3);
    }

    // ===== HELPER METHODS =====

    midiToFreq(midiNote) {
        return 440 * Math.pow(2, (midiNote - 69) / 12);
    }

    quantizeToScale(normalizedX) {
        const scale = this.scales[this.currentScale];
        const octaveRange = 3; // 3 octaves
        const totalNotes = octaveRange * 12;

        // Map X position to MIDI note range
        const rawMidiNote = this.rootNote - 12 + (normalizedX * totalNotes);

        // Find nearest note in scale
        const octave = Math.floor((rawMidiNote - this.rootNote) / 12);
        const semitone = Math.round(rawMidiNote - this.rootNote - (octave * 12));

        // Find closest scale degree
        let closestDegree = scale[0];
        let minDist = Math.abs(semitone - scale[0]);

        for (const degree of scale) {
            const dist = Math.abs(semitone - degree);
            if (dist < minDist) {
                minDist = dist;
                closestDegree = degree;
            }
        }

        const quantizedMidi = this.rootNote + (octave * 12) + closestDegree;
        return this.midiToFreq(quantizedMidi);
    }

    cycleScale() {
        const scaleNames = Object.keys(this.scales);
        const currentIndex = scaleNames.indexOf(this.currentScale);
        const nextIndex = (currentIndex + 1) % scaleNames.length;
        this.currentScale = scaleNames[nextIndex];
        console.log('Scale changed to:', this.currentScale);
        return this.currentScale;
    }
}
