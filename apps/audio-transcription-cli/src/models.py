"""Model wrappers for different transcription engines."""

import torch
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class TranscriptionSegment:
    """A segment of transcribed audio."""
    start: float
    end: float
    text: str
    speaker: Optional[str] = None


class TranscriptionModel(ABC):
    """Abstract base class for transcription models."""

    def __init__(self, device: Optional[str] = None):
        """Initialize the model.

        Args:
            device: Device to run on ('cuda', 'cpu', or None for auto-detect)
        """
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device
        self.model = None

    @abstractmethod
    def load(self):
        """Load the model into memory."""
        pass

    @abstractmethod
    def transcribe(
        self,
        audio_path: Path,
        language: Optional[str] = None,
    ) -> List[TranscriptionSegment]:
        """Transcribe an audio file.

        Args:
            audio_path: Path to the audio file
            language: Language code (e.g., 'en', 'es', 'fr') or None for auto-detect

        Returns:
            List of transcription segments with timestamps
        """
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the model name."""
        pass

    @property
    @abstractmethod
    def memory_usage(self) -> str:
        """Return estimated memory usage."""
        pass


class WhisperTurboModel(TranscriptionModel):
    """OpenAI Whisper Large v3 Turbo model using faster-whisper."""

    def __init__(self, device: Optional[str] = None):
        super().__init__(device)
        self.model_size = "deepdml/faster-whisper-large-v3-turbo-ct2"

    def load(self):
        """Load the Whisper Turbo model."""
        from faster_whisper import WhisperModel

        # Use int8 quantization for lower memory usage
        compute_type = "int8" if self.device == "cpu" else "float16"

        self.model = WhisperModel(
            self.model_size,
            device=self.device,
            compute_type=compute_type,
        )

    def transcribe(
        self,
        audio_path: Path,
        language: Optional[str] = None,
    ) -> List[TranscriptionSegment]:
        """Transcribe using Whisper Turbo."""
        if self.model is None:
            self.load()

        segments, info = self.model.transcribe(
            str(audio_path),
            language=language,
            beam_size=5,
            vad_filter=True,  # Built-in VAD
            vad_parameters=dict(min_silence_duration_ms=500),
        )

        results = []
        for segment in segments:
            results.append(TranscriptionSegment(
                start=segment.start,
                end=segment.end,
                text=segment.text.strip(),
            ))

        return results

    @property
    def name(self) -> str:
        return "Whisper Large v3 Turbo"

    @property
    def memory_usage(self) -> str:
        return "~6GB VRAM"


class GraniteModel(TranscriptionModel):
    """IBM Granite Speech 3.3 8B model."""

    def __init__(self, device: Optional[str] = None):
        super().__init__(device)
        self.model_name = "ibm-granite/granite-speech-3.3-8b"
        self.processor = None

    def load(self):
        """Load the Granite model."""
        from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq

        self.processor = AutoProcessor.from_pretrained(self.model_name)

        self.model = AutoModelForSpeechSeq2Seq.from_pretrained(
            self.model_name,
            device_map=self.device,
            torch_dtype=torch.bfloat16,
        )

    def transcribe(
        self,
        audio_path: Path,
        language: Optional[str] = None,
    ) -> List[TranscriptionSegment]:
        """Transcribe using Granite."""
        if self.model is None:
            self.load()

        import torchaudio

        # Load audio
        waveform, sample_rate = torchaudio.load(str(audio_path))

        # Resample to 16kHz if needed
        if sample_rate != 16000:
            resampler = torchaudio.transforms.Resample(sample_rate, 16000)
            waveform = resampler(waveform)
            sample_rate = 16000

        # Convert stereo to mono if needed
        if waveform.shape[0] > 1:
            waveform = torch.mean(waveform, dim=0, keepdim=True)

        # Process audio
        inputs = self.processor(
            waveform.squeeze().numpy(),
            sampling_rate=sample_rate,
            return_tensors="pt"
        ).to(self.device)

        # Generate transcription
        with torch.no_grad():
            generated_ids = self.model.generate(**inputs, max_new_tokens=512)

        # Decode
        transcription = self.processor.batch_decode(
            generated_ids,
            skip_special_tokens=True
        )[0]

        # Granite returns full transcription without timestamps
        # We'll return it as a single segment
        duration = waveform.shape[1] / sample_rate

        return [TranscriptionSegment(
            start=0.0,
            end=duration,
            text=transcription.strip(),
        )]

    @property
    def name(self) -> str:
        return "IBM Granite Speech 3.3 8B"

    @property
    def memory_usage(self) -> str:
        return "~16GB VRAM"


class CanaryModel(TranscriptionModel):
    """NVIDIA Canary-Qwen 2.5B model."""

    def __init__(self, device: Optional[str] = None):
        super().__init__(device)
        self.model_name = "nvidia/canary-qwen-2.5b"

    def load(self):
        """Load the Canary model."""
        try:
            from nemo.collections.speechlm2.models import SALM
            self.model = SALM.from_pretrained(self.model_name)
        except ImportError:
            raise ImportError(
                "NVIDIA NeMo is required for Canary model. Install with:\n"
                "  pip install nemo_toolkit[asr]"
            )

    def transcribe(
        self,
        audio_path: Path,
        language: Optional[str] = None,
    ) -> List[TranscriptionSegment]:
        """Transcribe using Canary."""
        if self.model is None:
            self.load()

        # Generate transcription
        answer_ids = self.model.generate(
            prompts=[
                [{
                    "role": "user",
                    "content": f"Transcribe the following: {self.model.audio_locator_tag}",
                    "audio": [str(audio_path)]
                }]
            ],
            max_new_tokens=512,
        )

        transcription = self.model.tokenizer.ids_to_text(answer_ids[0].cpu())

        # Canary returns full transcription without detailed timestamps
        # We'll return it as a single segment
        import torchaudio
        waveform, sample_rate = torchaudio.load(str(audio_path))
        duration = waveform.shape[1] / sample_rate

        return [TranscriptionSegment(
            start=0.0,
            end=duration,
            text=transcription.strip(),
        )]

    @property
    def name(self) -> str:
        return "NVIDIA Canary-Qwen 2.5B"

    @property
    def memory_usage(self) -> str:
        return "~10GB VRAM"


def get_model(model_name: str, device: Optional[str] = None) -> TranscriptionModel:
    """Get a transcription model by name.

    Args:
        model_name: One of 'whisper-turbo', 'granite', 'canary'
        device: Device to run on or None for auto-detect

    Returns:
        Initialized transcription model

    Raises:
        ValueError: If model_name is not recognized
    """
    models = {
        "whisper-turbo": WhisperTurboModel,
        "granite": GraniteModel,
        "canary": CanaryModel,
    }

    if model_name not in models:
        available = ", ".join(models.keys())
        raise ValueError(
            f"Unknown model: {model_name}. Available models: {available}"
        )

    return models[model_name](device=device)
