# Quick Start Guide

Get up and running with the Audio Transcription CLI in 5 minutes!

## Prerequisites

1. **Python 3.10+**
   ```bash
   python3 --version
   ```

2. **FFmpeg** (for audio file support)
   ```bash
   # Ubuntu/Debian
   sudo apt-get install ffmpeg

   # macOS
   brew install ffmpeg

   # Windows (chocolatey)
   choco install ffmpeg
   ```

3. **uv** (recommended) or pip
   ```bash
   # Install uv
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

## Installation

### Option 1: Using uv (Recommended)

```bash
# Navigate to the project directory
cd apps/audio-transcription-cli

# Install dependencies (takes ~2-3 minutes)
uv sync

# Verify installation
uv run python -m src --help
```

### Option 2: Using pip

```bash
cd apps/audio-transcription-cli

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -m src --help
```

## Your First Transcription

### 1. Basic Transcription

Transcribe an audio file (the model will be downloaded automatically on first run):

```bash
uv run python -m src your-audio.m4a
```

Output will be displayed in your terminal as nicely formatted Markdown.

### 2. Save to File

```bash
uv run python -m src your-audio.m4a --output transcript.md
```

### 3. Choose a Model

Show available models:
```bash
uv run python -m src --show-models
```

Use a specific model:
```bash
# Fast and accurate (default)
uv run python -m src audio.m4a --model whisper-turbo

# Highest accuracy, multilingual
uv run python -m src audio.m4a --model granite

# Very fast English transcription (requires NeMo)
uv run python -m src audio.m4a --model canary
```

### 4. Enable Speaker Diarization

First, get a Hugging Face token:
1. Create account at https://huggingface.co
2. Go to https://huggingface.co/settings/tokens
3. Create a new token
4. Accept terms at https://huggingface.co/pyannote/speaker-diarization-3.1

Then transcribe with speakers:
```bash
export HF_TOKEN=your_token_here
uv run python -m src audio.m4a --diarize --output transcript.md
```

## Common Use Cases

### Meeting Transcription
```bash
uv run python -m src meeting.m4a \
  --model whisper-turbo \
  --diarize \
  --output meeting-notes.md
```

### Podcast Transcription
```bash
uv run python -m src podcast-episode.mp3 \
  --model granite \
  --language en \
  --output episode-transcript.md
```

### Quick Voice Note
```bash
uv run python -m src voice-note.m4a
```

## Troubleshooting

### Out of Memory

Try using CPU or a smaller model:
```bash
uv run python -m src audio.m4a --device cpu --model whisper-turbo
```

### FFmpeg Not Found

Install FFmpeg (see Prerequisites above) and make sure it's in your PATH:
```bash
ffmpeg -version
```

### HF Token Issues

Make sure you've:
1. Set the `HF_TOKEN` environment variable
2. Accepted terms at https://huggingface.co/pyannote/speaker-diarization-3.1

### Model Download Slow

First-time model downloads can be large (1-8GB depending on model). Subsequent runs will use cached models.

## Next Steps

- Read the full [README.md](README.md) for detailed usage
- Check [NOTES.md](NOTES.md) for implementation details
- Explore [ICEBOX.md](ICEBOX.md) for planned features

## Performance Tips

1. **GPU vs CPU**: CUDA GPU is 10-50x faster than CPU
   ```bash
   # Check if CUDA is available
   uv run python -c "import torch; print(torch.cuda.is_available())"
   ```

2. **Model Selection**:
   - `whisper-turbo`: Best balance (default)
   - `granite`: Highest accuracy, needs 16GB VRAM
   - `canary`: Fastest, English-only

3. **Audio Quality**: Better audio quality = better transcription
   - Use lossless formats when possible
   - Minimize background noise
   - Use good microphones for recordings

## Getting Help

```bash
# Show help
uv run python -m src --help

# Show available models
uv run python -m src --show-models
```

For issues or questions, see the main repository at https://github.com/joncooper/claude-speriments

---

**Happy Transcribing!** 🎙️
