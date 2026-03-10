# Text-to-Speech App - Implementation Plan

## Research Summary

### TTS Engine Selection: **Chatterbox** (by Resemble AI)

After evaluating 13+ open-source TTS engines, **Chatterbox** is the clear choice:

| Criteria | Chatterbox |
|----------|-----------|
| **License** | MIT (fully commercial, code + models) |
| **Voice Cloning** | Zero-shot from 5 seconds of reference audio |
| **Quality** | 63.75% preference over ElevenLabs in blind tests |
| **Speed** | <150ms first audio with Turbo variant |
| **Variants** | Original, Multilingual (23 langs), Turbo (350M params) |
| **Maintenance** | Actively maintained by Resemble AI (11K+ GitHub stars) |
| **Safety** | Built-in PerTh watermarking |

**Why not others:**
- F5-TTS, Fish Speech/OpenAudio: CC-BY-NC model license (non-commercial only)
- XTTS v2 (Coqui): Non-commercial model license, company shut down
- Kokoro: No voice cloning support
- Piper: No voice cloning support
- Bark: Inconsistent quality, not maintained
- Tortoise: Very slow, not maintained

### Lessons from Existing Implementations

**Key patterns to adopt:**
1. **Smart text chunking at sentence boundaries** - never split mid-sentence (from open-unified-tts, Podcastfy)
2. **Crossfade audio stitching** for seamless concatenation (from open-unified-tts, Chatterbox-TTS-Extended)
3. **Academic text preprocessing** - remove citations `[1]`, `(Smith, 2020)`, URLs, page numbers, headers/footers (from Paper2Audio, Listening.com, Mozilla.ai Blueprint)
4. **Real-time progress feedback** via WebSocket/SSE (from Deepgram best practices)
5. **Streaming audio playback** before full generation completes

**Weaknesses in existing solutions to improve upon:**
1. Most are CLI-only or Gradio UIs (ugly) - we'll build a polished web UI
2. Most use cloud TTS APIs (expensive) - Chatterbox is local and free
3. Limited preprocessing - we'll build a robust pipeline for academic papers
4. No voice cloning in most open solutions - Chatterbox makes this simple
5. Poor progress tracking - we'll use SSE for real-time chunk-by-chunk updates

---

## Architecture

```
apps/text-to-speech-app/
├── README.md
├── NOTES.md
├── ICEBOX.md
├── backend/
│   ├── pyproject.toml          # Python deps (uv)
│   ├── .python-version
│   ├── .env.example
│   └── src/
│       └── tts_app/
│           ├── __init__.py
│           ├── main.py          # FastAPI app entry point
│           ├── routes.py        # API endpoints
│           ├── text_extract.py  # URL/PDF/text extraction
│           ├── preprocess.py    # Text cleaning pipeline
│           ├── chunker.py       # Smart sentence-boundary chunking
│           ├── synthesize.py    # Chatterbox TTS wrapper
│           └── audio_stitch.py  # Crossfade concatenation
├── frontend/
│   ├── package.json            # JS deps (bun)
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── index.html
│   └── src/
│       ├── main.ts             # App entry point
│       ├── style.css           # Styles
│       ├── api.ts              # Backend API client
│       ├── components/
│       │   ├── InputForm.ts    # Text/URL/file input + reference audio upload
│       │   ├── ProgressBar.ts  # Chunk-by-chunk progress display
│       │   └── AudioPlayer.ts  # Playback + download
│       └── utils/
│           └── sse.ts          # Server-Sent Events client
```

### Backend (Python + FastAPI)

**Text Input Pipeline:**
1. Accept text directly, URL (fetch & extract), or PDF upload
2. For URLs: use `trafilatura` for article extraction (handles most blog/news sites cleanly)
3. For PDFs: use `pymupdf` (fast, reliable text extraction)

**Preprocessing Pipeline:**
1. Remove bracketed citations: `[1]`, `[1, 2]`, `[1-5]`
2. Remove parenthetical citations: `(Smith, 2020)`, `(Smith & Jones, 2020; Doe, 2019)`
3. Remove URLs and email addresses
4. Remove page numbers, headers, footers
5. Remove figure/table references (e.g., "See Figure 3")
6. Normalize whitespace and fix broken hyphenation
7. Convert special characters (em-dashes, smart quotes, etc.)
8. Expand common abbreviations (e.g., "Fig." → "Figure", "et al." → "and others")

**Chunking Strategy:**
1. Split text into sentences using `nltk.sent_tokenize` or regex
2. Group sentences into chunks of ~200-300 words (Chatterbox sweet spot)
3. Never break mid-sentence
4. Maintain paragraph context where possible

**TTS Generation:**
1. Load Chatterbox model (lazy-load on first request)
2. For each chunk, generate audio with consistent voice settings
3. If reference audio provided, use voice cloning mode
4. If no reference audio, use default voice
5. Stream progress updates via SSE (Server-Sent Events)

**Audio Stitching:**
1. Concatenate chunk audio with crossfade (50-100ms overlap)
2. Normalize volume across chunks
3. Output as WAV (lossless) with option to convert to MP3
4. Return audio file URL for download

### Frontend (TypeScript + Vite)

**UI Layout:**
1. **Input Section**: Tabbed interface (Paste Text | Enter URL | Upload PDF)
2. **Voice Section**: Toggle between default voice and custom voice (upload reference audio, 5+ seconds)
3. **Generate Button**: Starts the pipeline
4. **Progress Section**: Shows preprocessing status, then chunk-by-chunk TTS progress bar
5. **Audio Player**: Standard HTML5 audio player with download button
6. Clean, minimal design using vanilla CSS (no framework needed)

### API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/generate` | Start TTS generation (returns job ID) |
| `GET` | `/api/progress/{job_id}` | SSE stream of progress updates |
| `GET` | `/api/audio/{job_id}` | Download generated audio file |
| `GET` | `/api/voices` | List available default voices |
| `POST` | `/api/extract-text` | Extract and preview text from URL/PDF |

---

## Implementation Steps

### Step 1: Project scaffolding
- Create `apps/text-to-speech-app/` directory structure
- Initialize Python backend with uv (`pyproject.toml`, dependencies)
- Initialize TypeScript frontend with bun + Vite
- Create `.env.example`, `.gitignore`

### Step 2: Backend - Text extraction & preprocessing
- Implement URL text extraction with `trafilatura`
- Implement PDF text extraction with `pymupdf`
- Build preprocessing pipeline (citations, URLs, formatting cleanup)
- Build smart sentence-boundary chunker
- Add `/api/extract-text` endpoint for preview

### Step 3: Backend - TTS synthesis
- Integrate Chatterbox TTS
- Implement voice cloning from reference audio upload
- Implement chunk-by-chunk generation with progress tracking
- Build crossfade audio stitching with `pydub` or `scipy`
- Add `/api/generate` and `/api/progress/{job_id}` endpoints

### Step 4: Frontend - UI
- Build input form (tabs for text/URL/PDF)
- Build reference audio upload component
- Build SSE-connected progress display
- Build audio player with download
- Style with clean, minimal CSS

### Step 5: Integration & polish
- Wire frontend to backend API
- End-to-end testing
- Error handling and edge cases
- Create README.md, NOTES.md, ICEBOX.md
- Update root README.md with new project entry

---

## Dependencies

### Backend (Python)
- `fastapi` + `uvicorn` - Web framework
- `chatterbox-tts` - TTS engine (Resemble AI)
- `trafilatura` - Web article text extraction
- `pymupdf` - PDF text extraction
- `pydub` - Audio manipulation and stitching
- `nltk` - Sentence tokenization
- `python-multipart` - File upload handling
- `sse-starlette` - Server-Sent Events

### Frontend (TypeScript)
- `vite` - Build tool
- No UI framework (vanilla TS + DOM)
- Minimal dependencies for clean, fast app
