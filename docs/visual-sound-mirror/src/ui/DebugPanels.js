// DebugPanels.js - Debug UI controls for visualization tuning

export class DebugPanels {
    constructor(app) {
        this.app = app;
    }

    populate() {
        const container = document.querySelector('.viz-debug-content');
        if (!container) return;

        const vizMode = this.app.visualizationMode;
        let html = `
            <h3>Visualization Tuning (Press 'V' to toggle)</h3>
            <p class="viz-mode-indicator">Mode <span id="currentVizMode">${vizMode}</span>: ${this.getVisualizationModeName(vizMode)} | Press 1-6 to switch modes</p>
        `;

        // Mode-specific controls
        if (vizMode === 1) {
            html += this.getParticleControls();
        } else if (vizMode === 2) {
            html += this.getBloomControls();
        } else if (vizMode === 3) {
            html += this.getFluidControls();
        } else if (vizMode === 4) {
            html += this.getOrbitControls();
        } else if (vizMode === 5) {
            html += this.getKaleidoscopeControls();
        } else if (vizMode === 6) {
            html += this.getEchoControls();
        }

        container.innerHTML = html;
        this.attachListeners();
    }

    getParticleControls() {
        const s = this.app.particleSettings;
        return `
            <div class="control-group">
                <label>Emission Rate: <span id="emissionRateValue">${s.emissionRate}</span>/sec</label>
                <input type="range" id="emissionRate" min="10" max="500" value="${s.emissionRate}" step="10">
            </div>
            <div class="control-group">
                <label>Lifetime: <span id="lifetimeValue">${s.lifetime}</span>ms</label>
                <input type="range" id="lifetime" min="500" max="8000" value="${s.lifetime}" step="100">
            </div>
            <div class="control-group">
                <label>Initial Velocity: <span id="initialVelocityValue">${s.initialVelocity}</span>x</label>
                <input type="range" id="initialVelocity" min="0.01" max="2.0" value="${s.initialVelocity}" step="0.01">
            </div>
            <div class="control-group">
                <label>Gravity: <span id="gravityValue">${s.gravity}</span></label>
                <input type="range" id="gravity" min="0" max="0.5" value="${s.gravity}" step="0.01">
            </div>
            <div class="control-group">
                <label>Drag: <span id="dragValue">${s.drag}</span></label>
                <input type="range" id="drag" min="0.9" max="0.999" value="${s.drag}" step="0.001">
            </div>
            <div class="control-group">
                <label>Attraction: <span id="attractionValue">${s.attraction}</span></label>
                <input type="range" id="attraction" min="-0.5" max="0.5" value="${s.attraction}" step="0.05">
            </div>
            <div class="control-group">
                <label>Repulsion: <span id="repulsionValue">${s.repulsion}</span></label>
                <input type="range" id="repulsion" min="0" max="2" value="${s.repulsion}" step="0.1">
            </div>
            <div class="control-group">
                <label>Turbulence: <span id="turbulenceValue">${s.turbulence}</span></label>
                <input type="range" id="turbulence" min="0" max="2" value="${s.turbulence}" step="0.1">
            </div>
            <div class="control-group">
                <label>Size Min: <span id="particleSizeMinValue">${s.particleSizeMin}</span>px</label>
                <input type="range" id="particleSizeMin" min="0.5" max="5" value="${s.particleSizeMin}" step="0.1">
            </div>
            <div class="control-group">
                <label>Size Max: <span id="particleSizeMaxValue">${s.particleSizeMax}</span>px</label>
                <input type="range" id="particleSizeMax" min="1" max="10" value="${s.particleSizeMax}" step="0.1">
            </div>
            <div class="control-group">
                <label>Color Mode:</label>
                <select id="colorMode">
                    <option value="velocity" ${s.colorMode === 'velocity' ? 'selected' : ''}>Velocity</option>
                    <option value="lifetime" ${s.colorMode === 'lifetime' ? 'selected' : ''}>Lifetime</option>
                    <option value="audio" ${s.colorMode === 'audio' ? 'selected' : ''}>Audio Reactive</option>
                    <option value="rainbow" ${s.colorMode === 'rainbow' ? 'selected' : ''}>Rainbow</option>
                </select>
            </div>
            <div class="control-group checkbox-group">
                <label><input type="checkbox" id="glow" ${s.glow ? 'checked' : ''}> Glow Effect</label>
                <label><input type="checkbox" id="trails" ${s.trails ? 'checked' : ''}> Particle Trails</label>
                <label><input type="checkbox" id="audioReactive" ${s.audioReactive ? 'checked' : ''}> Audio Reactive</label>
            </div>
            <div class="control-group">
                <p>Particles: <span id="particleCount">${this.app.particles.length}</span> / ${this.app.maxParticles}</p>
            </div>
            <button id="clearParticles">Clear All Particles</button>
            <button id="resetViz">Reset to Defaults</button>
        `;
    }

    getBloomControls() {
        const s = this.app.bloomSettings;
        return `
            <div class="control-group">
                <label>Velocity Threshold: <span id="velocityThresholdValue">${s.velocityThreshold}</span></label>
                <input type="range" id="velocityThreshold" min="1" max="20" value="${s.velocityThreshold}" step="0.5">
            </div>
            <div class="control-group">
                <label>Bloom Interval: <span id="bloomIntervalValue">${s.bloomInterval}</span>ms</label>
                <input type="range" id="bloomInterval" min="50" max="500" value="${s.bloomInterval}" step="10">
            </div>
            <div class="control-group">
                <label>Lifetime: <span id="bloomLifetimeValue">${s.lifetime}</span>ms</label>
                <input type="range" id="bloomLifetime" min="500" max="5000" value="${s.lifetime}" step="100">
            </div>
            <div class="control-group">
                <label>Max Radius: <span id="maxRadiusValue">${s.maxRadius}</span>px</label>
                <input type="range" id="maxRadius" min="100" max="500" value="${s.maxRadius}" step="10">
            </div>
            <div class="control-group">
                <label>Ring Count: <span id="ringCountValue">${s.ringCount}</span></label>
                <input type="range" id="ringCount" min="1" max="8" value="${s.ringCount}" step="1">
            </div>
            <div class="control-group">
                <label>Ring Spacing: <span id="ringSpacingValue">${s.ringSpacing}</span>px</label>
                <input type="range" id="ringSpacing" min="10" max="60" value="${s.ringSpacing}" step="5">
            </div>
            <div class="control-group">
                <label>Pulse Speed: <span id="pulseSpeedValue">${s.pulseSpeed}</span>x</label>
                <input type="range" id="pulseSpeed" min="0.5" max="3.0" value="${s.pulseSpeed}" step="0.1">
            </div>
            <div class="control-group">
                <label>Glow Intensity: <span id="bloomGlowValue">${s.glowIntensity}</span></label>
                <input type="range" id="bloomGlow" min="0" max="40" value="${s.glowIntensity}" step="2">
            </div>
            <div class="control-group checkbox-group">
                <label><input type="checkbox" id="colorShift" ${s.colorShift ? 'checked' : ''}> Color Shift Over Time</label>
            </div>
            <button id="resetViz">Reset to Defaults</button>
        `;
    }

    getFluidControls() {
        const s = this.app.fluidSettings;
        return `
            <div class="control-group">
                <label>Tendril Count: <span id="tendrilCountValue">${s.tendrilCount}</span></label>
                <input type="range" id="tendrilCount" min="3" max="15" value="${s.tendrilCount}" step="1">
            </div>
            <div class="control-group">
                <label>Tendril Radius: <span id="tendrilRadiusValue">${s.tendrilRadius}</span>px</label>
                <input type="range" id="tendrilRadius" min="10" max="60" value="${s.tendrilRadius}" step="5">
            </div>
            <div class="control-group">
                <label>Flow Speed: <span id="flowSpeedValue">${s.flowSpeed}</span></label>
                <input type="range" id="flowSpeed" min="0.0005" max="0.01" value="${s.flowSpeed}" step="0.0005">
            </div>
            <div class="control-group">
                <label>Pulse Amount: <span id="pulseAmountValue">${s.pulseAmount}</span>px</label>
                <input type="range" id="pulseAmount" min="0" max="30" value="${s.pulseAmount}" step="2">
            </div>
            <div class="control-group">
                <label>Gradient Size: <span id="gradientSizeValue">${s.gradientSize}</span>px</label>
                <input type="range" id="gradientSize" min="20" max="80" value="${s.gradientSize}" step="5">
            </div>
            <div class="control-group">
                <label>Opacity: <span id="fluidOpacityValue">${s.opacity}</span></label>
                <input type="range" id="fluidOpacity" min="0.2" max="0.8" value="${s.opacity}" step="0.05">
            </div>
            <div class="control-group">
                <label>Trail Persistence: <span id="trailPersistenceValue">${s.trailPersistence}</span></label>
                <input type="range" id="trailPersistence" min="0.8" max="0.98" value="${s.trailPersistence}" step="0.01">
            </div>
            <div class="control-group">
                <label>Velocity Influence: <span id="velocityInfluenceValue">${s.velocityInfluence}</span></label>
                <input type="range" id="velocityInfluence" min="0" max="5" value="${s.velocityInfluence}" step="0.1">
            </div>
            <button id="resetViz">Reset to Defaults</button>
        `;
    }

    getOrbitControls() {
        const s = this.app.orbitSettings;
        return `
            <div class="control-group">
                <label>Orbiter Count: <span id="orbiterCountValue">${s.orbiterCount}</span></label>
                <input type="range" id="orbiterCount" min="4" max="20" value="${s.orbiterCount}" step="1">
            </div>
            <div class="control-group">
                <label>Orbit Radius: <span id="orbitRadiusValue">${s.orbitRadius}</span>px</label>
                <input type="range" id="orbitRadius" min="20" max="100" value="${s.orbitRadius}" step="5">
            </div>
            <div class="control-group">
                <label>Orbit Speed: <span id="orbitSpeedValue">${s.orbitSpeed}</span></label>
                <input type="range" id="orbitSpeed" min="0.001" max="0.01" value="${s.orbitSpeed}" step="0.001">
            </div>
            <div class="control-group">
                <label>Orbiter Size: <span id="orbiterSizeValue">${s.orbiterSize}</span>px</label>
                <input type="range" id="orbiterSize" min="2" max="12" value="${s.orbiterSize}" step="1">
            </div>
            <div class="control-group">
                <label>Sun Size: <span id="sunSizeValue">${s.sunSize}</span>px</label>
                <input type="range" id="sunSize" min="8" max="30" value="${s.sunSize}" step="1">
            </div>
            <div class="control-group">
                <label>Trail Length: <span id="trailLengthValue">${s.trailLength}</span></label>
                <input type="range" id="trailLength" min="0" max="0.5" value="${s.trailLength}" step="0.05">
            </div>
            <div class="control-group">
                <label>Wobble: <span id="wobbleValue">${s.wobble}</span>px</label>
                <input type="range" id="wobble" min="0" max="20" value="${s.wobble}" step="1">
            </div>
            <div class="control-group">
                <label>Glow Intensity: <span id="orbitGlowValue">${s.glowIntensity}</span></label>
                <input type="range" id="orbitGlow" min="0" max="40" value="${s.glowIntensity}" step="2">
            </div>
            <button id="resetViz">Reset to Defaults</button>
        `;
    }

    getKaleidoscopeControls() {
        const s = this.app.kaleidoscopeSettings;
        return `
            <div class="control-group">
                <label>Symmetry Count: <span id="symmetryCountValue">${s.symmetryCount}</span></label>
                <input type="range" id="symmetryCount" min="3" max="12" value="${s.symmetryCount}" step="1">
            </div>
            <div class="control-group">
                <label>Finger Size: <span id="fingerSizeValue">${s.fingerSize}</span>px</label>
                <input type="range" id="fingerSize" min="8" max="40" value="${s.fingerSize}" step="2">
            </div>
            <div class="control-group">
                <label>Line Opacity: <span id="lineOpacityValue">${s.lineOpacity}</span></label>
                <input type="range" id="lineOpacity" min="0" max="1" value="${s.lineOpacity}" step="0.1">
            </div>
            <div class="control-group">
                <label>Rotation Speed: <span id="rotationSpeedValue">${s.rotationSpeed}</span></label>
                <input type="range" id="rotationSpeed" min="0" max="0.01" value="${s.rotationSpeed}" step="0.001">
            </div>
            <div class="control-group">
                <label>Trail Persistence: <span id="kaleoPersistenceValue">${s.trailPersistence}</span></label>
                <input type="range" id="kaleoPersistence" min="0.7" max="0.95" value="${s.trailPersistence}" step="0.01">
            </div>
            <div class="control-group">
                <label>Glow Intensity: <span id="kaleoGlowValue">${s.glowIntensity}</span></label>
                <input type="range" id="kaleoGlow" min="0" max="50" value="${s.glowIntensity}" step="2">
            </div>
            <div class="control-group checkbox-group">
                <label><input type="checkbox" id="pulseWithAudio" ${s.pulseWithAudio ? 'checked' : ''}> Pulse With Audio</label>
                <label><input type="checkbox" id="showCenter" ${s.showCenter ? 'checked' : ''}> Show Center Point</label>
            </div>
            <button id="resetViz">Reset to Defaults</button>
        `;
    }

    getEchoControls() {
        const s = this.app.echoSettings;
        return `
            <div class="control-group">
                <label>Trail Length: <span id="echoTrailLengthValue">${s.trailLength}</span></label>
                <input type="range" id="echoTrailLength" min="5" max="60" value="${s.trailLength}" step="1">
            </div>
            <div class="control-group">
                <label>Fade Speed: <span id="fadeSpeedValue">${s.fadeSpeed}</span></label>
                <input type="range" id="fadeSpeed" min="0.01" max="0.1" value="${s.fadeSpeed}" step="0.01">
            </div>
            <div class="control-group">
                <label>Chromatic Aberration: <span id="chromaticAberrationValue">${s.chromaticAberration}</span>px</label>
                <input type="range" id="chromaticAberration" min="0" max="10" value="${s.chromaticAberration}" step="1">
            </div>
            <div class="control-group">
                <label>Echo Spacing: <span id="echoSpacingValue">${s.echoSpacing}</span></label>
                <input type="range" id="echoSpacing" min="1" max="5" value="${s.echoSpacing}" step="1">
            </div>
            <div class="control-group">
                <label>Glow Intensity: <span id="echoGlowValue">${s.glowIntensity}</span></label>
                <input type="range" id="echoGlow" min="0" max="30" value="${s.glowIntensity}" step="2">
            </div>
            <div class="control-group">
                <label>Finger Size: <span id="echoFingerSizeValue">${s.fingerSize}</span>px</label>
                <input type="range" id="echoFingerSize" min="6" max="24" value="${s.fingerSize}" step="1">
            </div>
            <div class="control-group">
                <label>Palm Size: <span id="echoPalmSizeValue">${s.palmSize}</span>px</label>
                <input type="range" id="echoPalmSize" min="10" max="40" value="${s.palmSize}" step="2">
            </div>
            <div class="control-group checkbox-group">
                <label><input type="checkbox" id="motionBlur" ${s.motionBlur ? 'checked' : ''}> Motion Blur</label>
                <label><input type="checkbox" id="showPalm" ${s.showPalm ? 'checked' : ''}> Show Palm</label>
                <label><input type="checkbox" id="showFingers" ${s.showFingers ? 'checked' : ''}> Show Fingers</label>
            </div>
            <button id="resetViz">Reset to Defaults</button>
        `;
    }

    attachListeners() {
        // Delegate to mode-specific listeners
        const vizMode = this.app.visualizationMode;
        if (vizMode === 1) this.attachParticleListeners();
        else if (vizMode === 2) this.attachBloomListeners();
        else if (vizMode === 3) this.attachFluidListeners();
        else if (vizMode === 4) this.attachOrbitListeners();
        else if (vizMode === 5) this.attachKaleidoscopeListeners();
        else if (vizMode === 6) this.attachEchoListeners();
    }

    attachParticleListeners() {
        const s = this.app.particleSettings;
        this.attachSlider('emissionRate', (val) => { s.emissionRate = parseFloat(val); });
        this.attachSlider('lifetime', (val) => { s.lifetime = parseFloat(val); });
        this.attachSlider('initialVelocity', (val) => { s.initialVelocity = parseFloat(val); });
        this.attachSlider('gravity', (val) => { s.gravity = parseFloat(val); });
        this.attachSlider('drag', (val) => { s.drag = parseFloat(val); });
        this.attachSlider('attraction', (val) => { s.attraction = parseFloat(val); });
        this.attachSlider('repulsion', (val) => { s.repulsion = parseFloat(val); });
        this.attachSlider('turbulence', (val) => { s.turbulence = parseFloat(val); });
        this.attachSlider('particleSizeMin', (val) => { s.particleSizeMin = parseFloat(val); });
        this.attachSlider('particleSizeMax', (val) => { s.particleSizeMax = parseFloat(val); });

        const colorMode = document.getElementById('colorMode');
        if (colorMode) {
            colorMode.addEventListener('change', (e) => { s.colorMode = e.target.value; });
        }

        this.attachCheckbox('glow', (checked) => { s.glow = checked; });
        this.attachCheckbox('trails', (checked) => { s.trails = checked; });
        this.attachCheckbox('audioReactive', (checked) => { s.audioReactive = checked; });

        const clearBtn = document.getElementById('clearParticles');
        if (clearBtn) {
            clearBtn.addEventListener('click', () => { this.app.particles = []; });
        }

        this.attachResetButton();
    }

    attachBloomListeners() {
        const s = this.app.bloomSettings;
        this.attachSlider('velocityThreshold', (val) => { s.velocityThreshold = parseFloat(val); });
        this.attachSlider('bloomInterval', (val) => { s.bloomInterval = parseFloat(val); });
        this.attachSlider('bloomLifetime', (val) => { s.lifetime = parseFloat(val); });
        this.attachSlider('maxRadius', (val) => { s.maxRadius = parseFloat(val); });
        this.attachSlider('ringCount', (val) => { s.ringCount = parseInt(val); });
        this.attachSlider('ringSpacing', (val) => { s.ringSpacing = parseFloat(val); });
        this.attachSlider('pulseSpeed', (val) => { s.pulseSpeed = parseFloat(val); });
        this.attachSlider('bloomGlow', (val) => { s.glowIntensity = parseFloat(val); });
        this.attachCheckbox('colorShift', (checked) => { s.colorShift = checked; });
        this.attachResetButton();
    }

    attachFluidListeners() {
        const s = this.app.fluidSettings;
        this.attachSlider('tendrilCount', (val) => { s.tendrilCount = parseInt(val); });
        this.attachSlider('tendrilRadius', (val) => { s.tendrilRadius = parseFloat(val); });
        this.attachSlider('flowSpeed', (val) => { s.flowSpeed = parseFloat(val); });
        this.attachSlider('pulseAmount', (val) => { s.pulseAmount = parseFloat(val); });
        this.attachSlider('gradientSize', (val) => { s.gradientSize = parseFloat(val); });
        this.attachSlider('fluidOpacity', (val) => { s.opacity = parseFloat(val); });
        this.attachSlider('trailPersistence', (val) => { s.trailPersistence = parseFloat(val); });
        this.attachSlider('velocityInfluence', (val) => { s.velocityInfluence = parseFloat(val); });
        this.attachResetButton();
    }

    attachOrbitListeners() {
        const s = this.app.orbitSettings;
        this.attachSlider('orbiterCount', (val) => { s.orbiterCount = parseInt(val); });
        this.attachSlider('orbitRadius', (val) => { s.orbitRadius = parseFloat(val); });
        this.attachSlider('orbitSpeed', (val) => { s.orbitSpeed = parseFloat(val); });
        this.attachSlider('orbiterSize', (val) => { s.orbiterSize = parseFloat(val); });
        this.attachSlider('sunSize', (val) => { s.sunSize = parseFloat(val); });
        this.attachSlider('trailLength', (val) => { s.trailLength = parseFloat(val); });
        this.attachSlider('wobble', (val) => { s.wobble = parseFloat(val); });
        this.attachSlider('orbitGlow', (val) => { s.glowIntensity = parseFloat(val); });
        this.attachResetButton();
    }

    attachKaleidoscopeListeners() {
        const s = this.app.kaleidoscopeSettings;
        this.attachSlider('symmetryCount', (val) => { s.symmetryCount = parseInt(val); });
        this.attachSlider('fingerSize', (val) => { s.fingerSize = parseFloat(val); });
        this.attachSlider('lineOpacity', (val) => { s.lineOpacity = parseFloat(val); });
        this.attachSlider('rotationSpeed', (val) => { s.rotationSpeed = parseFloat(val); });
        this.attachSlider('kaleoPersistence', (val) => { s.trailPersistence = parseFloat(val); });
        this.attachSlider('kaleoGlow', (val) => { s.glowIntensity = parseFloat(val); });
        this.attachCheckbox('pulseWithAudio', (checked) => { s.pulseWithAudio = checked; });
        this.attachCheckbox('showCenter', (checked) => { s.showCenter = checked; });
        this.attachResetButton();
    }

    attachEchoListeners() {
        const s = this.app.echoSettings;
        this.attachSlider('echoTrailLength', (val) => { s.trailLength = parseInt(val); });
        this.attachSlider('fadeSpeed', (val) => { s.fadeSpeed = parseFloat(val); });
        this.attachSlider('chromaticAberration', (val) => { s.chromaticAberration = parseFloat(val); });
        this.attachSlider('echoSpacing', (val) => { s.echoSpacing = parseInt(val); });
        this.attachSlider('echoGlow', (val) => { s.glowIntensity = parseFloat(val); });
        this.attachSlider('echoFingerSize', (val) => { s.fingerSize = parseFloat(val); });
        this.attachSlider('echoPalmSize', (val) => { s.palmSize = parseFloat(val); });
        this.attachCheckbox('motionBlur', (checked) => { s.motionBlur = checked; });
        this.attachCheckbox('showPalm', (checked) => { s.showPalm = checked; });
        this.attachCheckbox('showFingers', (checked) => { s.showFingers = checked; });
        this.attachResetButton();
    }

    attachSlider(id, callback) {
        const slider = document.getElementById(id);
        const valueSpan = document.getElementById(id + 'Value');
        if (slider && valueSpan) {
            slider.addEventListener('input', (e) => {
                const val = e.target.value;
                valueSpan.textContent = val;
                callback(val);
            });
        }
    }

    attachCheckbox(id, callback) {
        const checkbox = document.getElementById(id);
        if (checkbox) {
            checkbox.addEventListener('change', (e) => {
                callback(e.target.checked);
            });
        }
    }

    attachResetButton() {
        const resetBtn = document.getElementById('resetViz');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => {
                this.app.resetCurrentModeSettings();
                this.populate();
            });
        }
    }

    getVisualizationModeName(mode) {
        const names = {
            1: 'Particle Fountain',
            2: 'Audio Bloom Pulses',
            3: 'Fluid Dynamics',
            4: 'Gravitational Orbits',
            5: 'Kaleidoscope Symmetry',
            6: 'Temporal Echoes'
        };
        return names[mode] || 'Unknown';
    }
}
