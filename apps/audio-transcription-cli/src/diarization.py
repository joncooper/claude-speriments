"""Speaker diarization using pyannote.audio."""

from pathlib import Path
from typing import List, Tuple, Optional
import warnings

# Suppress some pyannote warnings
warnings.filterwarnings("ignore", category=UserWarning)


class SpeakerDiarizer:
    """Speaker diarization using pyannote.audio."""

    def __init__(self, device: Optional[str] = None):
        """Initialize the diarizer.

        Args:
            device: Device to run on ('cuda', 'cpu', or None for auto-detect)
        """
        import torch
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device

        self.pipeline = None

    def load(self, hf_token: Optional[str] = None):
        """Load the diarization pipeline.

        Args:
            hf_token: Hugging Face token for accessing pyannote models.
                     Can also be set via HF_TOKEN environment variable.

        Note:
            You need to accept the terms at:
            https://huggingface.co/pyannote/speaker-diarization-3.1
        """
        from pyannote.audio import Pipeline
        import os

        # Get token from parameter or environment
        token = hf_token or os.getenv("HF_TOKEN")

        if not token:
            raise ValueError(
                "Hugging Face token required for speaker diarization.\n"
                "Set HF_TOKEN environment variable or pass hf_token parameter.\n"
                "Accept terms at: https://huggingface.co/pyannote/speaker-diarization-3.1"
            )

        self.pipeline = Pipeline.from_pretrained(
            "pyannote/speaker-diarization-3.1",
            use_auth_token=token,
        )

        # Move to device
        if self.device == "cuda":
            import torch
            self.pipeline.to(torch.device("cuda"))

    def diarize(self, audio_path: Path) -> List[Tuple[float, float, str]]:
        """Perform speaker diarization on an audio file.

        Args:
            audio_path: Path to the audio file

        Returns:
            List of (start_time, end_time, speaker_label) tuples
        """
        if self.pipeline is None:
            self.load()

        # Run diarization
        diarization = self.pipeline(str(audio_path))

        # Extract speaker segments
        segments = []
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            segments.append((
                turn.start,
                turn.end,
                speaker,
            ))

        return segments

    def assign_speakers_to_segments(
        self,
        transcription_segments: List,
        speaker_segments: List[Tuple[float, float, str]],
    ) -> List:
        """Assign speaker labels to transcription segments.

        Args:
            transcription_segments: List of TranscriptionSegment objects
            speaker_segments: List of (start, end, speaker) tuples from diarization

        Returns:
            Updated transcription segments with speaker labels
        """
        from src.models import TranscriptionSegment

        updated_segments = []

        for seg in transcription_segments:
            # Find the speaker segment with most overlap
            max_overlap = 0
            best_speaker = None

            for sp_start, sp_end, speaker in speaker_segments:
                # Calculate overlap
                overlap_start = max(seg.start, sp_start)
                overlap_end = min(seg.end, sp_end)
                overlap = max(0, overlap_end - overlap_start)

                if overlap > max_overlap:
                    max_overlap = overlap
                    best_speaker = speaker

            # Create updated segment with speaker label
            updated_segments.append(TranscriptionSegment(
                start=seg.start,
                end=seg.end,
                text=seg.text,
                speaker=best_speaker,
            ))

        return updated_segments


def merge_consecutive_same_speaker(
    segments: List,
) -> List:
    """Merge consecutive segments from the same speaker.

    Args:
        segments: List of TranscriptionSegment objects

    Returns:
        Merged segments
    """
    if not segments:
        return segments

    from src.models import TranscriptionSegment

    merged = []
    current = segments[0]

    for seg in segments[1:]:
        # If same speaker and close in time (< 2 seconds gap), merge
        if (seg.speaker == current.speaker and
            seg.start - current.end < 2.0):
            # Merge text
            current = TranscriptionSegment(
                start=current.start,
                end=seg.end,
                text=f"{current.text} {seg.text}",
                speaker=current.speaker,
            )
        else:
            # Different speaker or large gap, start new segment
            merged.append(current)
            current = seg

    merged.append(current)
    return merged
