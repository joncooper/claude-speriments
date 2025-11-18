# Implementation Notes

## Overview

This is a command-line tool for transcribing audio files using local AI models. It supports multiple state-of-the-art models, speaker diarization, and voice activity detection.

## Technology Stack

### Core Libraries

- **uv**: Modern Python package manager (10-100x faster than pip)
- **typer**: CLI framework with excellent developer experience
- **rich**: Beautiful terminal output with progress bars and formatting
- **torch/torchaudio**: PyTorch for audio processing and ML inference

### Model Libraries

1. **faster-whisper**: Optimized Whisper inference using CTranslate2
   - Used for OpenAI Whisper Large v3 Turbo
   - Significantly faster than original Whisper implementation
   - Supports quantization (int8, float16)

2. **transformers**: Hugging Face library for model loading
   - Used for IBM Granite Speech 3.3 8B
   - Could be used for NVIDIA Canary (but NeMo is better)

3. **pyannote.audio**: Speaker diarization and VAD
   - State-of-the-art speaker detection
   - Built-in VAD capabilities
   - Version 3.1 (latest, pure PyTorch)

## Model Details

### OpenAI Whisper Large v3 Turbo (Default)

- **Size**: 809M parameters
- **Speed**: 8x faster than Whisper Large
- **Implementation**: faster-whisper with CTranslate2
- **Pros**: Fast, good accuracy, well-supported
- **Cons**: English-focused, not as accurate as larger models
- **Memory**: ~6GB VRAM
- **Timestamps**: Native support with word-level precision

### IBM Granite Speech 3.3 8B

- **Size**: 8B parameters
- **Speed**: Moderate (slower than Whisper Turbo)
- **Implementation**: Hugging Face transformers
- **Pros**: Highest accuracy, multilingual (EN/FR/DE/ES/PT)
- **Cons**: Large memory footprint, no native timestamps
- **Memory**: ~16GB VRAM
- **Timestamps**: Not natively supported (returns full transcription)

### NVIDIA Canary-Qwen 2.5B

- **Size**: 2.5B parameters
- **Speed**: Very fast (418 RTFx)
- **Implementation**: NVIDIA NeMo (optional dependency)
- **Pros**: Excellent speed/accuracy tradeoff
- **Cons**: Requires NeMo toolkit (large dependency), English-only
- **Memory**: ~10GB VRAM
- **Timestamps**: Limited (returns full transcription)

## Design Decisions

### Why Python?

While Rust or Go would be faster, Python has:
- Much more mature audio/ML ecosystem
- Better model support (transformers, faster-whisper, pyannote)
- Easier integration with Hugging Face models
- Still performs well for this use case (ML inference is the bottleneck, not Python)

### Model Abstraction

Used an abstract base class (`TranscriptionModel`) to:
- Make it easy to add new models
- Provide consistent interface across models
- Handle device management (CUDA/CPU) uniformly
- Support different output formats

### VAD Strategy

Two approaches:
1. **Built-in VAD**: Whisper has native VAD support (faster)
2. **pyannote VAD**: More accurate, used during diarization

For best results: use Whisper's built-in VAD for transcription, then run pyannote for diarization.

### Diarization Workflow

1. Transcribe audio with timestamps
2. Run pyannote diarization separately
3. Align speaker segments with transcription segments
4. Merge consecutive segments from same speaker

This approach is more robust than trying to do everything at once.

## Challenges and Solutions

### Challenge: Different Models, Different APIs

**Problem**: Each model has a different API and output format.

**Solution**: Created `TranscriptionModel` abstraction with standard `TranscriptionSegment` output.

### Challenge: Timestamp Support

**Problem**: Granite and Canary don't provide native timestamps.

**Solution**:
- Use Whisper for best timestamp support
- For others, return full transcription as single segment
- Could be enhanced with forced alignment in future

### Challenge: Memory Usage

**Problem**: Large models require significant VRAM.

**Solution**:
- Support device selection (CUDA/CPU)
- Use quantization where available (int8 for Whisper)
- Provide memory usage estimates in CLI
- Clear documentation about requirements

### Challenge: HF Token for Diarization

**Problem**: pyannote models require accepting terms and HF token.

**Solution**:
- Clear error messages
- Support HF_TOKEN environment variable
- Link to model page in error message
- Make diarization optional

## Performance Optimizations

1. **Lazy Loading**: Only import heavy libraries when needed
2. **Quantization**: Use int8 for CPU, float16 for GPU
3. **Batching**: Could be added for multiple files (future)
4. **VAD**: Skip silent portions to speed up processing

## Future Enhancements (ICEBOX)

See ICEBOX.md for planned features.

## Testing Strategy

Currently manual testing. Could add:
- Unit tests for formatting functions
- Integration tests with sample audio
- Performance benchmarks
- Accuracy comparison between models

## Deployment

Not designed for web deployment. This is a CLI tool for:
- Local transcription
- Privacy-sensitive use cases
- Batch processing
- Offline usage

## Dependencies

Managed via uv for fast, reliable installs. Major dependencies:

- torch + torchaudio: ~3GB
- CUDA libraries: ~5GB (if using GPU)
- transformers: ~100MB
- faster-whisper: ~50MB
- pyannote.audio: ~50MB

Total: ~8GB for full install with GPU support.

## Known Limitations

1. **Granite & Canary timestamps**: Limited timestamp support
2. **m4a support**: Requires FFmpeg for audio conversion
3. **Memory requirements**: Large models need significant VRAM
4. **Diarization accuracy**: Depends on audio quality
5. **NeMo dependency**: Canary requires large NeMo toolkit (optional)

## Model Selection Guidance

**Use Whisper Turbo when:**
- You want fast results
- Timestamps are important
- Memory is limited
- English or common languages

**Use Granite when:**
- Accuracy is paramount
- Multilingual support needed
- You have 16GB+ VRAM
- Timestamps less important

**Use Canary when:**
- English-only transcription
- Want best speed/accuracy ratio
- Have NeMo installed
- Don't need detailed timestamps

## Code Organization

```
src/
├── __init__.py         # Package metadata
├── __main__.py         # Entry point for python -m src
├── transcribe.py       # Main CLI application
├── models.py           # Model wrappers and abstraction
├── diarization.py      # Speaker diarization logic
└── formatting.py       # Output formatting (Markdown, etc.)
```

Clean separation of concerns:
- CLI logic separate from model logic
- Formatting independent of transcription
- Diarization as optional add-on

## Development Workflow

1. Install: `uv sync`
2. Run: `uv run python -m src audio.m4a`
3. Add deps: `uv add package-name`
4. Update README when adding features

## Contributing

This is part of the `claude-speriments` repository. See the main CLAUDE.md for contribution guidelines.

---

**Created**: November 2025
**Last Updated**: November 2025
