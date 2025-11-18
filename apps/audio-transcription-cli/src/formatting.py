"""Transcript formatting utilities."""

from typing import List
from datetime import timedelta


def format_timestamp(seconds: float) -> str:
    """Format seconds as HH:MM:SS timestamp.

    Args:
        seconds: Time in seconds

    Returns:
        Formatted timestamp string
    """
    td = timedelta(seconds=seconds)
    hours = td.seconds // 3600
    minutes = (td.seconds % 3600) // 60
    secs = td.seconds % 60

    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def format_duration(seconds: float) -> str:
    """Format duration in a human-readable way.

    Args:
        seconds: Duration in seconds

    Returns:
        Formatted duration string (e.g., "5:32" or "1:23:45")
    """
    td = timedelta(seconds=int(seconds))
    hours = td.seconds // 3600
    minutes = (td.seconds % 3600) // 60
    secs = td.seconds % 60

    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes}:{secs:02d}"


def format_transcript_markdown(
    segments: List,
    model_name: str,
    audio_duration: float,
    language: str = "auto-detected",
) -> str:
    """Format transcription segments as Markdown.

    Args:
        segments: List of TranscriptionSegment objects
        model_name: Name of the model used
        audio_duration: Total duration of audio in seconds
        language: Language of the transcription

    Returns:
        Formatted Markdown string
    """
    from src.models import TranscriptionSegment

    # Build header
    md = "# Transcript\n\n"
    md += f"**Duration**: {format_duration(audio_duration)}\n"
    md += f"**Model**: {model_name}\n"
    md += f"**Language**: {language}\n\n"
    md += "---\n\n"

    # Add segments
    current_speaker = None

    for seg in segments:
        # Add speaker header if speaker changed
        if seg.speaker != current_speaker:
            current_speaker = seg.speaker
            speaker_label = seg.speaker if seg.speaker else "Speaker"
            md += f"## [{format_timestamp(seg.start)}] {speaker_label}\n\n"

        # Add text (if no speaker labels, show timestamp for each segment)
        if seg.speaker is None:
            md += f"**[{format_timestamp(seg.start)}]** {seg.text}\n\n"
        else:
            md += f"{seg.text}\n\n"

    return md


def format_plain_text(segments: List) -> str:
    """Format transcription segments as plain text.

    Args:
        segments: List of TranscriptionSegment objects

    Returns:
        Plain text transcription
    """
    lines = []

    for seg in segments:
        if seg.speaker:
            lines.append(f"[{format_timestamp(seg.start)}] {seg.speaker}: {seg.text}")
        else:
            lines.append(f"[{format_timestamp(seg.start)}] {seg.text}")

    return "\n".join(lines)


def get_audio_duration(audio_path) -> float:
    """Get the duration of an audio file.

    Args:
        audio_path: Path to audio file

    Returns:
        Duration in seconds
    """
    import torchaudio
    from pathlib import Path

    waveform, sample_rate = torchaudio.load(str(audio_path))
    duration = waveform.shape[1] / sample_rate

    return duration
