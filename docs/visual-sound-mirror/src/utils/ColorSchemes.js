// ColorSchemes.js - Color palette management based on color theory

export class ColorSchemes {
    constructor() {
        this.colorSchemes = {
            aurora: { base: 220, type: 'analogous' },    // Blues to greens
            sunset: { base: 30, type: 'analogous' },     // Oranges to purples
            ocean: { base: 200, type: 'monochromatic' }, // Deep blues
            forest: { base: 140, type: 'analogous' },    // Greens
            cosmic: { base: 280, type: 'triadic' }       // Purples, oranges, greens
        };
        this.currentScheme = 'aurora';
        this.baseHue = 220;
        this.colorPhase = 0;
    }

    setScheme(schemeName) {
        if (this.colorSchemes[schemeName]) {
            this.currentScheme = schemeName;
            this.baseHue = this.colorSchemes[schemeName].base;
        }
    }

    getScheme() {
        return this.colorSchemes[this.currentScheme];
    }

    updatePhase(deltaTime) {
        this.colorPhase += deltaTime * 0.0001;
    }

    getFingerColor(fingerIndex, velocity = 0, alpha = 1) {
        const scheme = this.getScheme();
        let hue;

        switch (scheme.type) {
            case 'analogous':
                hue = (this.baseHue + (fingerIndex * 20) + this.colorPhase * 10) % 360;
                break;
            case 'triadic':
                hue = (this.baseHue + (fingerIndex * 120)) % 360;
                break;
            case 'monochromatic':
                hue = this.baseHue;
                break;
            default:
                hue = (this.baseHue + (fingerIndex * 30)) % 360;
        }

        const saturation = 70 + Math.min(velocity * 2, 30);
        const lightness = 50 + Math.sin(this.colorPhase + fingerIndex) * 10;

        return `hsla(${hue}, ${saturation}%, ${lightness}%, ${alpha})`;
    }

    getParticleColor(particle, settings) {
        const { colorMode, alpha } = settings;
        let hue, saturation, lightness;

        switch (colorMode) {
            case 'velocity':
                const speed = Math.sqrt(particle.vx * particle.vx + particle.vy * particle.vy);
                hue = (this.baseHue + speed * 5) % 360;
                saturation = 70;
                lightness = 50 + Math.min(speed, 20);
                break;

            case 'lifetime':
                const lifeRatio = particle.age / particle.lifetime;
                hue = (this.baseHue + lifeRatio * 120) % 360;
                saturation = 60 + lifeRatio * 20;
                lightness = 60 - lifeRatio * 20;
                break;

            case 'audio':
                hue = (this.baseHue + this.colorPhase * 20) % 360;
                saturation = 70;
                lightness = 50;
                break;

            case 'rainbow':
                hue = (particle.hue || 0) % 360;
                saturation = 80;
                lightness = 50;
                break;

            default:
                hue = this.baseHue;
                saturation = 70;
                lightness = 50;
        }

        return `hsla(${hue}, ${saturation}%, ${lightness}%, ${alpha})`;
    }

    getBloomColor(bloom) {
        const lifeRatio = bloom.age / bloom.lifetime;
        const hue = (this.baseHue + lifeRatio * 60) % 360;
        const alpha = Math.max(0, 1 - lifeRatio);
        return `hsla(${hue}, 70%, 60%, ${alpha})`;
    }

    getRainbowHue(index, total) {
        return (360 / total) * index;
    }

    getHueShift(amount) {
        return (this.baseHue + amount) % 360;
    }
}
