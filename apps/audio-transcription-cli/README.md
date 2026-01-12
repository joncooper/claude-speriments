# Audio Transcription CLI

A powerful command-line tool for transcribing audio files using local AI models with speaker diarization and voice activity detection.

## Features

- **Multiple Model Support**: Choose from state-of-the-art local transcription models:
  - IBM Granite Speech 3.3 8B (highest accuracy)
  - NVIDIA Canary-Qwen 2.5B (fast and accurate)
  - OpenAI Whisper Large v3 Turbo (8x faster than Whisper Large)

- **Speaker Diarization**: Automatically detect and label different speakers in the audio
- **Voice Activity Detection (VAD)**: Skip silent portions for faster processing
- **Beautiful CLI**: Rich progress bars and visual feedback
- **Markdown Output**: Get formatted transcripts with timestamps and speaker labels

## Installation

### Prerequisites

- Python 3.10 or higher
- FFmpeg (for audio processing)

**Install FFmpeg:**
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Windows (via chocolatey)
choco install ffmpeg
```

### Install the Tool

Using uv (recommended):
```bash
cd apps/audio-transcription-cli
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

## Quick Start

Transcribe an audio file:
```bash
uv run python -m transcribe audio.m4a
```

Choose a specific model:
```bash
uv run python -m transcribe audio.m4a --model whisper-turbo
```

Enable speaker diarization:
```bash
uv run python -m transcribe audio.m4a --diarize
```

Save output to a file:
```bash
uv run python -m transcribe audio.m4a --output transcript.md
```

## Usage

```
Usage: transcribe [OPTIONS] AUDIO_FILE

Arguments:
  AUDIO_FILE  Path to the audio file to transcribe (m4a, mp3, wav, etc.)

Options:
  --model TEXT           Model to use: granite, canary, whisper-turbo [default: whisper-turbo]
  --diarize             Enable speaker diarization
  --vad                 Enable voice activity detection [default: True]
  --output PATH         Output file path (default: prints to stdout)
  --language TEXT       Language code (e.g., en, es, fr) [default: auto-detect]
  --help                Show this message and exit
```

## Available Models

### Whisper Large v3 Turbo (Default)
- **Size**: 809M parameters
- **Speed**: 8x faster than Whisper Large
- **Best for**: Quick transcriptions, general use
- **Memory**: ~6GB VRAM

### IBM Granite Speech 3.3 8B
- **Size**: 8B parameters
- **Speed**: Moderate
- **Best for**: Highest accuracy, multilingual (EN, FR, DE, ES, PT)
- **Memory**: ~16GB VRAM

### NVIDIA Canary-Qwen 2.5B
- **Size**: 2.5B parameters
- **Speed**: 418 RTFx
- **Best for**: Fast and accurate English transcription
- **Memory**: ~10GB VRAM

## Output Format

The tool generates Markdown-formatted transcripts:

```markdown
# Transcript

**Duration**: 5:32
**Model**: whisper-turbo
**Language**: English

---

## [00:00:00] Speaker 1

This is the first speaker talking about something interesting.

## [00:01:23] Speaker 2

And here's the second speaker responding to that point.

## [00:02:45] Speaker 1

The first speaker continues the conversation...
```

## Advanced Usage

### Custom Configuration

First-time model downloads require Hugging Face authentication for some models:
```bash
# Set your Hugging Face token
export HF_TOKEN=your_token_here
```

### Batch Processing

Process multiple files:
```bash
for file in *.m4a; do
  uv run python -m transcribe "$file" --output "${file%.m4a}.md"
done
```

## Performance Tips

- Use `--no-vad` to disable VAD if your audio has no silence
- Use `--model whisper-turbo` for fastest results
- Enable GPU acceleration (automatic if CUDA available)
- Process shorter clips for faster iteration

## Troubleshooting

**Out of Memory Error:**
- Try using `whisper-turbo` instead of larger models
- Close other GPU-intensive applications
- Consider using CPU mode (slower but no VRAM limits)

**FFmpeg Not Found:**
- Install FFmpeg following the instructions above
- Ensure it's in your system PATH

**Model Download Issues:**
- Check your internet connection
- For pyannote models, accept the terms on Hugging Face
- Set `HF_TOKEN` environment variable if needed

## Development

### Project Structure

```
audio-transcription-cli/
├── src/
│   ├── transcribe.py      # Main CLI entry point
│   ├── models.py          # Model wrappers
│   ├── diarization.py     # Speaker diarization
│   ├── vad.py             # Voice activity detection
│   └── formatting.py      # Markdown output formatting
├── tests/                 # Unit tests
├── examples/              # Example audio files
└── README.md              # This file
```

### Contributing

This is an experimental project in the `claude-speriments` repository. Feel free to:
- Open issues for bugs or feature requests
- Submit pull requests with improvements
- Share your transcription results

## License

MIT License - See repository root for details

## Acknowledgments

- OpenAI for Whisper models
- IBM for Granite Speech models
- NVIDIA for Canary models
- pyannote.audio team for diarization tools
- The open-source ML community
