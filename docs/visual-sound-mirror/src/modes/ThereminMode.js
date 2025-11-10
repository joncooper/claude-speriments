// ThereminMode.js - Theremin visualization with frequency display

export class ThereminMode {
    constructor(canvas, ctx) {
        this.canvas = canvas;
        this.ctx = ctx;
    }

    render(leftHand, audioSystem) {
        if (!leftHand || !leftHand.palm) return;

        const palm = leftHand.palm;

        // Draw palm position indicator
        this.ctx.fillStyle = 'rgba(100, 200, 255, 0.3)';
        this.ctx.beginPath();
        this.ctx.arc(palm.x, palm.y, 40, 0, Math.PI * 2);
        this.ctx.fill();

        this.ctx.strokeStyle = 'rgba(100, 200, 255, 0.8)';
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        this.ctx.arc(palm.x, palm.y, 40, 0, Math.PI * 2);
        this.ctx.stroke();

        // Draw vertical pitch line
        this.ctx.strokeStyle = 'rgba(150, 150, 150, 0.3)';
        this.ctx.lineWidth = 1;
        this.ctx.setLineDash([5, 5]);
        this.ctx.beginPath();
        this.ctx.moveTo(palm.x, 0);
        this.ctx.lineTo(palm.x, this.canvas.height);
        this.ctx.stroke();
        this.ctx.setLineDash([]);

        // Draw horizontal filter line
        this.ctx.strokeStyle = 'rgba(150, 150, 150, 0.3)';
        this.ctx.beginPath();
        this.ctx.moveTo(0, palm.y);
        this.ctx.lineTo(this.canvas.width, palm.y);
        this.ctx.stroke();

        // Draw frequency visualization
        const normalizedX = palm.x / this.canvas.width;
        const frequency = audioSystem.quantizeToScale(normalizedX);

        this.ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
        this.ctx.font = 'bold 24px monospace';
        this.ctx.textAlign = 'center';
        this.ctx.fillText(Math.round(frequency) + ' Hz', palm.x, palm.y - 60);

        // Draw filter indicator
        const normalizedY = palm.y / this.canvas.height;
        const brightness = Math.round((1 - normalizedY) * 100);
        this.ctx.font = '16px monospace';
        this.ctx.fillText('Filter: ' + brightness + '%', palm.x, palm.y + 70);

        // Draw waveform visualization
        const waveformY = this.canvas.height - 100;
        const waveformHeight = 60;
        const waveformWidth = 200;
        const waveformX = palm.x - waveformWidth / 2;

        this.ctx.strokeStyle = 'rgba(100, 200, 255, 0.6)';
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();

        for (let i = 0; i < waveformWidth; i++) {
            const t = (i / waveformWidth) * Math.PI * 4;
            const y = waveformY + Math.sin(t + Date.now() * 0.01) * (waveformHeight / 2);
            if (i === 0) {
                this.ctx.moveTo(waveformX + i, y);
            } else {
                this.ctx.lineTo(waveformX + i, y);
            }
        }
        this.ctx.stroke();

        // Draw fingertips
        if (leftHand.fingertips) {
            for (const tip of leftHand.fingertips) {
                this.ctx.fillStyle = 'rgba(255, 255, 255, 0.6)';
                this.ctx.beginPath();
                this.ctx.arc(tip.x, tip.y, 8, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }
    }
}
