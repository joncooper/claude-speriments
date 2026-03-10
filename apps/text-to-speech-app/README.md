# Paper to Audio

A web application that converts papers, articles, and blog posts into natural-sounding audio using [Chatterbox TTS](https://github.com/resemble-ai/chatterbox) by Resemble AI. Supports zero-shot voice cloning from just 5 seconds of reference audio.

**Status:** Initial Spike

## Features

- **Multiple input methods**: Paste text, enter a URL, or upload a PDF
- **Smart text preprocessing**: Automatically removes citations, URLs, page numbers, and academic formatting artifacts
- **Sentence-boundary chunking**: Never splits text mid-sentence for natural audio flow
- **Voice cloning**: Clone any voice from a short audio clip (5+ seconds)
- **Voice controls**: Adjust expressiveness and voice similarity
- **Real-time progress**: Server-Sent Events stream chunk-by-chunk synthesis progress
- **Crossfade stitching**: Seamless audio concatenation with crossfade between chunks
- **Clean web UI**: Responsive, polished interface with drag-and-drop file uploads

## Tech Stack

| Component | Technology |
|-----------|-----------|
| TTS Engine | [Chatterbox](https://github.com/resemble-ai/chatterbox) (MIT license) |
| Backend | Python, FastAPI, uvicorn |
| Frontend | TypeScript, Vite |
| Text Extraction | trafilatura (URLs), PyMuPDF (PDFs) |
| Audio Processing | scipy, pydub |

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- [bun](https://bun.sh/) (JavaScript runtime)
- CUDA-capable GPU recommended (CPU works but is slow)

## Setup

### Backend

```bash
cd backend
cp .env.example .env
uv sync
```

### Frontend

```bash
cd frontend
bun install
```

## Running

### Development (two terminals)

**Terminal 1 - Backend:**
```bash
cd backend
uv run tts-app
```

**Terminal 2 - Frontend:**
```bash
cd frontend
bun run dev
```

The frontend dev server runs on `http://localhost:5173` and proxies API requests to the backend on port 8000.

### Production

```bash
# Build frontend
cd frontend && bun run build

# Run backend (serves frontend static files from dist/)
cd ../backend && uv run tts-app
```

Access the app at `http://localhost:8000`.

## Usage

1. **Add content**: Paste text, enter an article URL, or upload a PDF
2. **Preview** (optional): Click "Preview Extracted Text" to see the cleaned text and chunk count
3. **Configure voice**: Use the default voice or upload reference audio for voice cloning
4. **Adjust settings**: Tune expressiveness (neutral to animated) and voice similarity (creative to faithful)
5. **Generate**: Click "Generate Audio" and watch real-time progress
6. **Listen & download**: Play the audio in-browser or download the WAV file

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/extract-text` | Extract and preview text from URL/PDF/text |
| `POST` | `/api/generate` | Start TTS generation (returns job ID) |
| `GET` | `/api/progress/{job_id}` | SSE stream of progress updates |
| `GET` | `/api/audio/{job_id}` | Download generated audio file |

## Architecture

```
Input (text/URL/PDF)
    → Text Extraction (trafilatura / PyMuPDF)
    → Preprocessing (citation removal, normalization)
    → Sentence-boundary Chunking (~250 words/chunk)
    → Chatterbox TTS (per-chunk synthesis)
    → Crossfade Audio Stitching
    → WAV Output
```

The backend runs TTS synthesis in a background task and streams progress via Server-Sent Events, so the UI stays responsive during long generation jobs.
