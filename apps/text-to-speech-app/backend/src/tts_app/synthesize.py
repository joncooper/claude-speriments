"""TTS synthesis using Chatterbox."""

import os
import torch
import numpy as np
from pathlib import Path

_model = None
_device = None
SAMPLE_RATE = 24000


def _get_device() -> str:
    """Determine the device to use."""
    global _device
    if _device is None:
        configured = os.environ.get("DEVICE", "").lower()
        if configured in ("cuda", "cpu"):
            _device = configured
        else:
            _device = "cuda" if torch.cuda.is_available() else "cpu"
    return _device


def _get_model():
    """Lazy-load the Chatterbox model."""
    global _model
    if _model is None:
        from chatterbox.tts import ChatterboxTTS

        device = _get_device()
        _model = ChatterboxTTS.from_pretrained(device=device)
    return _model


def synthesize_chunk(
    text: str,
    reference_audio_path: str | None = None,
    exaggeration: float = 0.5,
    cfg_weight: float = 0.5,
) -> np.ndarray:
    """Synthesize a single chunk of text to audio.

    Args:
        text: The text to synthesize.
        reference_audio_path: Optional path to reference audio for voice cloning.
        exaggeration: Emotion exaggeration factor (0.0 = neutral, 1.0 = very expressive).
        cfg_weight: Classifier-free guidance weight (higher = more adherence to reference).

    Returns:
        Audio as numpy array (float32, mono).
    """
    model = _get_model()

    wav = model.generate(
        text,
        audio_prompt_path=reference_audio_path,
        exaggeration=exaggeration,
        cfg_weight=cfg_weight,
    )

    # Convert to numpy - Chatterbox returns a tensor
    if isinstance(wav, torch.Tensor):
        audio = wav.squeeze().cpu().numpy()
    else:
        audio = np.array(wav, dtype=np.float32)

    # Normalize to [-1, 1]
    peak = np.max(np.abs(audio))
    if peak > 0:
        audio = audio / peak

    return audio


def get_sample_rate() -> int:
    return SAMPLE_RATE
