"""API routes for the TTS app."""

import asyncio
import os
import uuid
import tempfile
from pathlib import Path
from typing import AsyncGenerator

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from sse_starlette.sse import EventSourceResponse
import json

from . import text_extract, preprocess, chunker, synthesize, audio_stitch

router = APIRouter(prefix="/api")

# In-memory job store
_jobs: dict[str, dict] = {}

OUTPUT_DIR = Path(os.environ.get("AUDIO_OUTPUT_DIR", "./output"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

UPLOAD_DIR = Path(tempfile.mkdtemp(prefix="tts_uploads_"))


@router.post("/extract-text")
async def extract_text(
    url: str | None = Form(None),
    text: str | None = Form(None),
    file: UploadFile | None = File(None),
):
    """Extract and preview text from a URL, PDF, or raw text input."""
    try:
        raw = await _get_raw_text(url, text, file)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    cleaned = preprocess.preprocess(raw)
    chunks = chunker.chunk_text(cleaned)

    return {
        "text": cleaned,
        "chunk_count": len(chunks),
        "word_count": len(cleaned.split()),
        "chunks_preview": [c[:100] + "..." if len(c) > 100 else c for c in chunks[:5]],
    }


@router.post("/generate")
async def generate(
    url: str | None = Form(None),
    text: str | None = Form(None),
    file: UploadFile | None = File(None),
    reference_audio: UploadFile | None = File(None),
    exaggeration: float = Form(0.5),
    cfg_weight: float = Form(0.5),
):
    """Start TTS generation. Returns a job ID for progress tracking."""
    try:
        raw = await _get_raw_text(url, text, file)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Save reference audio if provided
    ref_path = None
    if reference_audio and reference_audio.filename:
        ref_bytes = await reference_audio.read()
        if len(ref_bytes) > 0:
            ref_path = str(UPLOAD_DIR / f"ref_{uuid.uuid4().hex}.wav")
            with open(ref_path, "wb") as f:
                f.write(ref_bytes)

    # Create job
    job_id = uuid.uuid4().hex[:12]
    cleaned = preprocess.preprocess(raw)
    chunks = chunker.chunk_text(cleaned)

    _jobs[job_id] = {
        "status": "processing",
        "progress": 0,
        "total_chunks": len(chunks),
        "current_chunk": 0,
        "error": None,
        "audio_file": None,
    }

    # Run synthesis in background
    asyncio.create_task(
        _run_synthesis(job_id, chunks, ref_path, exaggeration, cfg_weight)
    )

    return {"job_id": job_id, "total_chunks": len(chunks)}


@router.get("/progress/{job_id}")
async def progress(job_id: str):
    """SSE stream of progress updates for a generation job."""
    if job_id not in _jobs:
        raise HTTPException(status_code=404, detail="Job not found")

    return EventSourceResponse(_progress_stream(job_id))


@router.get("/audio/{job_id}")
async def get_audio(job_id: str):
    """Download the generated audio file."""
    job = _jobs.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    if job["status"] == "processing":
        raise HTTPException(status_code=202, detail="Still processing")
    if job["status"] == "error":
        raise HTTPException(status_code=500, detail=job["error"])

    audio_path = job["audio_file"]
    if not audio_path or not Path(audio_path).exists():
        raise HTTPException(status_code=500, detail="Audio file not found")

    return FileResponse(
        audio_path,
        media_type="audio/wav",
        filename=f"generated_{job_id}.wav",
    )


async def _get_raw_text(
    url: str | None, text: str | None, file: UploadFile | None
) -> str:
    """Extract raw text from one of the three input methods."""
    if url:
        return await asyncio.to_thread(text_extract.extract_from_url, url)
    elif file and file.filename:
        content = await file.read()
        if file.filename.lower().endswith(".pdf"):
            return text_extract.extract_from_pdf(content)
        else:
            return text_extract.extract_from_text(content.decode("utf-8", errors="replace"))
    elif text:
        return text_extract.extract_from_text(text)
    else:
        raise ValueError("Provide one of: url, text, or file")


async def _run_synthesis(
    job_id: str,
    chunks: list[str],
    ref_path: str | None,
    exaggeration: float,
    cfg_weight: float,
):
    """Run TTS synthesis for all chunks (runs in background)."""
    try:
        audio_chunks = []
        for i, chunk_text in enumerate(chunks):
            _jobs[job_id]["current_chunk"] = i + 1
            _jobs[job_id]["progress"] = int((i / len(chunks)) * 100)

            audio = await asyncio.to_thread(
                synthesize.synthesize_chunk,
                chunk_text,
                ref_path,
                exaggeration,
                cfg_weight,
            )
            audio_chunks.append(audio)

        # Stitch chunks together
        sample_rate = synthesize.get_sample_rate()
        final_audio = audio_stitch.crossfade_concat(audio_chunks, sample_rate)
        wav_bytes = audio_stitch.to_wav_bytes(final_audio, sample_rate)

        # Save to file
        output_path = str(OUTPUT_DIR / f"{job_id}.wav")
        with open(output_path, "wb") as f:
            f.write(wav_bytes)

        _jobs[job_id]["status"] = "complete"
        _jobs[job_id]["progress"] = 100
        _jobs[job_id]["audio_file"] = output_path

    except Exception as e:
        _jobs[job_id]["status"] = "error"
        _jobs[job_id]["error"] = str(e)


async def _progress_stream(job_id: str) -> AsyncGenerator[dict, None]:
    """Yield SSE events for job progress."""
    last_progress = -1
    while True:
        job = _jobs.get(job_id)
        if not job:
            yield {"event": "error", "data": json.dumps({"error": "Job not found"})}
            return

        current = job["progress"]
        if current != last_progress:
            yield {
                "event": "progress",
                "data": json.dumps({
                    "status": job["status"],
                    "progress": job["progress"],
                    "current_chunk": job["current_chunk"],
                    "total_chunks": job["total_chunks"],
                }),
            }
            last_progress = current

        if job["status"] == "complete":
            yield {
                "event": "complete",
                "data": json.dumps({"audio_url": f"/api/audio/{job_id}"}),
            }
            return

        if job["status"] == "error":
            yield {
                "event": "error",
                "data": json.dumps({"error": job["error"]}),
            }
            return

        await asyncio.sleep(0.5)
