"""Stitch audio chunks together with crossfade."""

import io
import numpy as np
from scipy.io import wavfile


def crossfade_concat(
    chunks: list[np.ndarray],
    sample_rate: int,
    crossfade_ms: int = 80,
    silence_ms: int = 300,
) -> np.ndarray:
    """Concatenate audio chunks with crossfade and inter-chunk silence.

    Args:
        chunks: List of audio arrays (float32, mono).
        sample_rate: Audio sample rate.
        crossfade_ms: Crossfade duration in milliseconds.
        silence_ms: Silence to insert between chunks in milliseconds.

    Returns:
        Concatenated audio as numpy array.
    """
    if not chunks:
        return np.array([], dtype=np.float32)

    if len(chunks) == 1:
        return chunks[0]

    crossfade_samples = int(sample_rate * crossfade_ms / 1000)
    silence_samples = int(sample_rate * silence_ms / 1000)
    silence = np.zeros(silence_samples, dtype=np.float32)

    result = chunks[0].copy()

    for chunk in chunks[1:]:
        # Add silence between chunks
        result = np.concatenate([result, silence])

        # Apply crossfade if both chunks are long enough
        if len(result) >= crossfade_samples and len(chunk) >= crossfade_samples:
            fade_out = np.linspace(1.0, 0.0, crossfade_samples, dtype=np.float32)
            fade_in = np.linspace(0.0, 1.0, crossfade_samples, dtype=np.float32)

            # Apply fade out to end of result
            result[-crossfade_samples:] *= fade_out
            # Apply fade in to start of chunk
            chunk_copy = chunk.copy()
            chunk_copy[:crossfade_samples] *= fade_in
            # Overlap-add
            result[-crossfade_samples:] += chunk_copy[:crossfade_samples]
            result = np.concatenate([result, chunk_copy[crossfade_samples:]])
        else:
            result = np.concatenate([result, chunk])

    return result


def to_wav_bytes(audio: np.ndarray, sample_rate: int) -> bytes:
    """Convert audio array to WAV file bytes."""
    # Scale to int16 range
    audio_int16 = np.clip(audio * 32767, -32768, 32767).astype(np.int16)

    buf = io.BytesIO()
    wavfile.write(buf, sample_rate, audio_int16)
    return buf.getvalue()
