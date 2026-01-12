# Examples

This directory contains example usage of the audio transcription CLI.

## Example Audio Files

Due to size constraints, example audio files are not included in the repository. You can:

1. Use your own audio files (m4a, mp3, wav, etc.)
2. Download sample audio from:
   - [LibriVox](https://librivox.org/) - Public domain audiobooks
   - [Common Voice](https://commonvoice.mozilla.org/) - Open source voice dataset
   - Record your own audio

## Usage Examples

### Basic Transcription

```bash
# Transcribe a file
uv run python -m src audio.m4a

# Save to file
uv run python -m src audio.m4a --output transcript.md
```

### With Different Models

```bash
# Whisper Turbo (fast, default)
uv run python -m src audio.m4a --model whisper-turbo

# Granite (highest accuracy)
uv run python -m src audio.m4a --model granite

# Canary (very fast, English only)
uv run python -m src audio.m4a --model canary
```

### With Speaker Diarization

```bash
# Set HF token first
export HF_TOKEN=your_token_here

# Transcribe with speaker detection
uv run python -m src audio.m4a --diarize --output transcript.md
```

### Specify Language

```bash
# For best results, specify the language
uv run python -m src audio.m4a --language en
uv run python -m src audio.m4a --language es
uv run python -m src audio.m4a --language fr
```

### Choose Device

```bash
# Use GPU (default if available)
uv run python -m src audio.m4a --device cuda

# Force CPU (slower but no GPU required)
uv run python -m src audio.m4a --device cpu
```

## Sample Output

Here's what a transcript with speaker diarization looks like:

```markdown
# Transcript

**Duration**: 3:24
**Model**: Whisper Large v3 Turbo
**Language**: English

---

## [00:00:00] SPEAKER_00

Welcome to today's podcast. I'm really excited to discuss artificial intelligence and its impact on society.

## [00:00:15] SPEAKER_01

Thanks for having me! It's a fascinating topic. I think we're seeing unprecedented changes in how we work and communicate.

## [00:01:23] SPEAKER_00

Absolutely. Let's start with the basics. What exactly is AI, and why is it suddenly everywhere?

## [00:01:35] SPEAKER_01

Great question. AI, or artificial intelligence, refers to machines that can perform tasks that typically require human intelligence...
```

## Testing Different Scenarios

### Short Voice Note
```bash
uv run python -m src short-note.m4a
```

### Long Interview
```bash
uv run python -m src interview.m4a --diarize --model whisper-turbo
```

### Non-English Audio
```bash
uv run python -m src spanish-audio.m4a --language es --model granite
```

### Noisy Audio
```bash
# VAD helps skip silence
uv run python -m src noisy-audio.m4a --model whisper-turbo
```

## Batch Processing

Process multiple files at once:

```bash
# Using bash loop
for file in *.m4a; do
  echo "Processing $file..."
  uv run python -m src "$file" --output "${file%.m4a}.md"
done
```

Or with parallel processing:

```bash
# Install GNU parallel
# Ubuntu: sudo apt-get install parallel
# macOS: brew install parallel

# Process in parallel
ls *.m4a | parallel uv run python -m src {} --output {.}.md
```

## Performance Comparison

Approximate processing times for a 5-minute audio file:

| Model | Device | Time | Memory |
|-------|--------|------|--------|
| whisper-turbo | CPU | ~5 min | 4GB |
| whisper-turbo | GPU | ~30 sec | 6GB VRAM |
| granite | CPU | ~15 min | 8GB |
| granite | GPU | ~2 min | 16GB VRAM |
| canary | GPU | ~20 sec | 10GB VRAM |

*Times are approximate and depend on hardware, audio quality, and content.*

## Tips

1. **Start simple**: Use default settings first
2. **Check GPU**: Use `nvidia-smi` to monitor GPU usage
3. **Test quality**: Try different models to see what works best for your use case
4. **Audio quality matters**: Better recording = better transcription
5. **Use VAD**: Helps with long files that have silence

## Troubleshooting

If you encounter issues:
- Check the main [README.md](../README.md)
- See [QUICKSTART.md](../QUICKSTART.md) for common problems
- Review [NOTES.md](../NOTES.md) for implementation details
