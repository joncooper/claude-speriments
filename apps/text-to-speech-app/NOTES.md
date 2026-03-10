# Notes

## TTS Engine Selection

Evaluated 13+ open-source TTS engines. Key decision factors:

1. **Chatterbox** (selected) - MIT license on both code and models, zero-shot voice cloning from 5s audio, outperformed ElevenLabs in blind evaluations (63.75% preference). Actively maintained by Resemble AI.

2. **F5-TTS** - Excellent quality but CC-BY-NC model license (non-commercial only).

3. **Fish Speech / OpenAudio S1** - #1 on TTS-Arena2 but CC-BY-NC-SA model license.

4. **XTTS v2 (Coqui)** - Most mature ecosystem but Coqui AI shut down (Dec 2023). Community fork exists. Non-commercial model license.

5. **Kokoro** - Blazing fast, tiny model (82M params), but no voice cloning support.

## Text Preprocessing

The preprocessing pipeline is specifically designed for academic papers and long-form content:

- Bracketed citations `[1]`, `[1, 2]`, `[1-5]` removed
- Parenthetical citations `(Smith, 2020)` removed
- Common abbreviations expanded for better pronunciation (e.g., "et al." → "and others")
- Special characters normalized (em-dashes, smart quotes)

## Chunking Strategy

Chunks target ~250 words based on Chatterbox's optimal input length. Splitting strictly at sentence boundaries prevents mid-word audio artifacts. Crossfade stitching (80ms overlap) with 300ms silence between chunks produces natural-sounding output.

## Architecture Decisions

- **SSE over WebSocket**: Simpler for unidirectional progress updates. No need for bidirectional communication.
- **In-memory job store**: Acceptable for single-user/development use. Would need Redis or similar for production scale.
- **Lazy model loading**: Chatterbox model loads on first request to avoid slow startup.
- **Background task synthesis**: Uses `asyncio.create_task` to avoid blocking the API server during long generations.
