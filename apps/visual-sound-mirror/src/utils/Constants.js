// Constants.js - Shared constants across the application

export const MODES = {
    RIBBONS: 'ribbons',
    THEREMIN: 'theremin',
    PADS: 'pads'
};

export const VISUALIZATION_MODES = {
    PARTICLE_FOUNTAIN: 1,
    AUDIO_BLOOM: 2,
    FLUID_DYNAMICS: 3,
    GRAVITATIONAL_ORBITS: 4,
    KALEIDOSCOPE: 5,
    TEMPORAL_ECHOES: 6
};

export const SCALES = {
    chromatic: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    major: [0, 2, 4, 5, 7, 9, 11],
    minor: [0, 2, 3, 5, 7, 8, 10],
    pentatonic: [0, 2, 4, 7, 9],
    blues: [0, 3, 5, 6, 7, 10],
    dorian: [0, 2, 3, 5, 7, 9, 10],
    phrygian: [0, 1, 3, 5, 7, 8, 10]
};

export const FINGERTIP_INDICES = [4, 8, 12, 16, 20]; // MediaPipe hand landmark indices

export const DEFAULT_SETTINGS = {
    trailAlpha: 0.12,
    soundInterval: 70,
    minVelocityForSound: 1,
    ribbonWidth: 2.5,
    ribbonOffsets: 3,
    ribbonSpacing: 8,
    maxTrailLength: 25
};

export const GESTURE_SETTINGS = {
    holdRequired: 2500, // ms to hold gesture for mode switch
    modeSwitchCooldown: 1000
};

export const DRUM_SAMPLES = {
    KICK: 'kick',
    SNARE: 'snare',
    HIHAT: 'hihat',
    CLAP: 'clap',
    TOM_LOW: 'tom_low',
    TOM_MID: 'tom_mid',
    TOM_HIGH: 'tom_high',
    RIM: 'rim',
    SNAP: 'snap',
    COWBELL: 'cowbell'
};
