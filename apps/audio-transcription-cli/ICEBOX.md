# Future Enhancement Backlog

This file tracks potential improvements and features for the audio transcription CLI.

## High Priority

### Batch Processing
- **Description**: Process multiple audio files in one command
- **Usage**: `transcribe *.m4a --batch --output-dir transcripts/`
- **Benefits**: More efficient for large datasets
- **Complexity**: Medium
- **Dependencies**: None

### Forced Alignment for Non-Whisper Models
- **Description**: Add word-level timestamps to Granite/Canary output
- **Implementation**: Use forced alignment tools (wav2vec2, Montreal Forced Aligner)
- **Benefits**: Better timestamps for all models
- **Complexity**: High
- **Dependencies**: alignment toolkit

### Progress Bar for Long Audio
- **Description**: Show progress during transcription of long files
- **Implementation**: Hook into model's internal progress or chunk processing
- **Benefits**: Better UX for long files
- **Complexity**: Medium
- **Dependencies**: Model-specific callbacks

## Medium Priority

### Additional Output Formats
- **Description**: Support more output formats
- **Formats**:
  - SRT/VTT for subtitles
  - JSON with detailed metadata
  - Plain text
  - WebVTT with styling
- **Complexity**: Low
- **Dependencies**: None

### Model Caching/Download Management
- **Description**: Better handling of model downloads
- **Features**:
  - Show download progress
  - Cache models in user directory
  - List cached models
  - Remove old models
- **Complexity**: Medium
- **Dependencies**: huggingface_hub utilities

### Configuration File
- **Description**: Support config file for default settings
- **Format**: YAML or TOML
- **Settings**: Default model, device, language, etc.
- **Location**: `~/.config/audio-transcribe/config.yaml`
- **Complexity**: Low
- **Dependencies**: pyyaml or tomli

### Real-time Transcription
- **Description**: Transcribe audio from microphone in real-time
- **Use Cases**: Live captioning, meeting transcription
- **Complexity**: High
- **Dependencies**: pyaudio or sounddevice

### GPU Memory Optimization
- **Description**: Better GPU memory management
- **Features**:
  - Automatic batch size adjustment
  - Model offloading to CPU
  - Quantization options (4-bit, 8-bit)
- **Complexity**: Medium
- **Dependencies**: bitsandbytes, accelerate

## Low Priority

### Web UI
- **Description**: Optional web interface for the CLI
- **Tech**: FastAPI + HTMX or Streamlit
- **Benefits**: Easier for non-technical users
- **Complexity**: High
- **Dependencies**: fastapi, streamlit

### Language Auto-Detection
- **Description**: Automatically detect language before transcription
- **Implementation**: Use lightweight model (langdetect, fasttext)
- **Benefits**: Better accuracy for multilingual content
- **Complexity**: Low
- **Dependencies**: langdetect or fasttext

### Custom Vocabulary
- **Description**: Support custom vocabulary/terms
- **Use Cases**: Technical jargon, names, domain-specific terms
- **Implementation**: Model-specific (Whisper supports, others might not)
- **Complexity**: Medium
- **Dependencies**: Model-specific

### Emotion Detection
- **Description**: Detect speaker emotion/sentiment
- **Implementation**: Use emotion recognition models
- **Output**: Add emotion tags to speaker segments
- **Complexity**: High
- **Dependencies**: emotion recognition model

### Audio Preprocessing
- **Description**: Automatic audio enhancement
- **Features**:
  - Noise reduction
  - Volume normalization
  - Sample rate conversion
- **Complexity**: Medium
- **Dependencies**: noisereduce, pydub

### Speaker Identification
- **Description**: Identify known speakers by voice
- **Implementation**: Speaker embedding + matching
- **Use Cases**: Meeting transcripts with known participants
- **Complexity**: High
- **Dependencies**: speaker verification model

## Research / Experimental

### Whisper Fine-tuning
- **Description**: Fine-tune Whisper on specific domains
- **Use Cases**: Medical, legal, technical terminology
- **Complexity**: Very High
- **Dependencies**: Training infrastructure

### Multi-speaker Transcription
- **Description**: Better handling of overlapping speech
- **Challenge**: Current models struggle with overlaps
- **Research**: Explore separation + transcription
- **Complexity**: Very High
- **Dependencies**: speech separation models

### Punctuation and Formatting
- **Description**: Better punctuation restoration
- **Implementation**: Post-processing with punctuation models
- **Benefits**: More readable transcripts
- **Complexity**: Medium
- **Dependencies**: punctuation restoration model

### Translation
- **Description**: Translate transcripts to other languages
- **Implementation**: Use translation models (NLLB, M2M100)
- **Use Cases**: Multilingual content
- **Complexity**: Medium
- **Dependencies**: translation models

## Performance Improvements

### ONNX Runtime
- **Description**: Convert models to ONNX for faster inference
- **Models**: Whisper already uses CTranslate2 (similar)
- **Benefits**: Potentially faster CPU inference
- **Complexity**: High
- **Dependencies**: onnxruntime

### Streaming Inference
- **Description**: Process audio in chunks as it arrives
- **Benefits**: Lower latency, less memory
- **Complexity**: High
- **Dependencies**: Model-specific streaming support

### Distributed Processing
- **Description**: Process multiple files across machines
- **Use Cases**: Large-scale transcription jobs
- **Implementation**: Ray, Dask, or custom
- **Complexity**: Very High
- **Dependencies**: distributed computing framework

## Documentation Improvements

### Video Tutorials
- **Description**: Create video guides for common use cases
- **Platform**: YouTube, Loom
- **Topics**: Installation, basic usage, advanced features

### Example Gallery
- **Description**: Showcase transcription examples
- **Content**: Different accents, languages, use cases
- **Format**: GitHub Pages or similar

### Comparison Benchmarks
- **Description**: Performance and accuracy benchmarks
- **Comparisons**: Different models, settings, hardware
- **Metrics**: WER, RTF, memory usage

## Integration Ideas

### GitHub Action
- **Description**: Transcribe audio in CI/CD pipelines
- **Use Cases**: Podcast show notes, video content
- **Complexity**: Medium

### Discord/Slack Bot
- **Description**: Transcribe voice messages automatically
- **Use Cases**: Accessibility, search
- **Complexity**: High

### Obsidian Plugin
- **Description**: Transcribe voice notes in Obsidian
- **Use Cases**: Note-taking, journaling
- **Complexity**: Medium

### VS Code Extension
- **Description**: Transcribe audio from within VS Code
- **Use Cases**: Developer docs, code comments
- **Complexity**: Medium

## Notes

- Items are roughly ordered by priority within each section
- Complexity estimates: Low (< 1 day), Medium (1-3 days), High (> 3 days)
- Some items may depend on external model availability
- Community feedback welcome!

---

**Last Updated**: November 2025
