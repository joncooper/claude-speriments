"""Main CLI application for audio transcription."""

import typer
from pathlib import Path
from typing import Optional
from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeRemainingColumn,
)
from rich.panel import Panel
from rich.table import Table
from rich import box
import sys

app = typer.Typer(
    name="transcribe",
    help="Transcribe audio files using local AI models with speaker diarization",
    add_completion=False,
)
console = Console()


def show_model_info():
    """Display available models in a nice table."""
    table = Table(
        title="Available Models",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan",
    )

    table.add_column("Model", style="cyan", no_wrap=True)
    table.add_column("Size", style="yellow")
    table.add_column("Speed", style="green")
    table.add_column("Memory", style="magenta")
    table.add_column("Best For", style="white")

    table.add_row(
        "whisper-turbo",
        "809M",
        "8x faster",
        "~6GB",
        "Quick transcriptions",
    )
    table.add_row(
        "granite",
        "8B",
        "Moderate",
        "~16GB",
        "Highest accuracy, multilingual",
    )
    table.add_row(
        "canary",
        "2.5B",
        "418 RTFx",
        "~10GB",
        "Fast English ASR",
    )

    console.print(table)


@app.command()
def main(
    audio_file: Optional[Path] = typer.Argument(
        None,
        exists=True,
        help="Path to the audio file to transcribe (m4a, mp3, wav, etc.)",
    ),
    model: str = typer.Option(
        "whisper-turbo",
        "--model",
        "-m",
        help="Model to use: whisper-turbo, granite, or canary",
    ),
    diarize: bool = typer.Option(
        False,
        "--diarize",
        "-d",
        help="Enable speaker diarization (requires HF_TOKEN)",
    ),
    output: Optional[Path] = typer.Option(
        None,
        "--output",
        "-o",
        help="Output file path (default: prints to stdout)",
    ),
    language: Optional[str] = typer.Option(
        None,
        "--language",
        "-l",
        help="Language code (e.g., en, es, fr). Auto-detect if not specified.",
    ),
    device: Optional[str] = typer.Option(
        None,
        "--device",
        help="Device to use: cuda or cpu (auto-detect if not specified)",
    ),
    show_models: bool = typer.Option(
        False,
        "--show-models",
        help="Show available models and exit",
    ),
):
    """Transcribe an audio file using local AI models.

    Examples:
        \b
        # Basic transcription with default model
        transcribe audio.m4a

        \b
        # Use specific model
        transcribe audio.m4a --model granite

        \b
        # Enable speaker diarization
        transcribe audio.m4a --diarize

        \b
        # Save to file
        transcribe audio.m4a --output transcript.md
    """
    if show_models:
        show_model_info()
        return

    # Check that audio file is provided
    if audio_file is None:
        console.print("[red]Error:[/red] AUDIO_FILE argument is required")
        console.print("\nUse --show-models to see available models")
        raise typer.Exit(1)

    # Validate model name
    valid_models = ["whisper-turbo", "granite", "canary"]
    if model not in valid_models:
        console.print(f"[red]Error:[/red] Invalid model '{model}'")
        show_model_info()
        raise typer.Exit(1)

    # Show welcome banner
    console.print(
        Panel.fit(
            f"[bold cyan]Audio Transcription CLI[/bold cyan]\n"
            f"Transcribing: [yellow]{audio_file.name}[/yellow]",
            border_style="cyan",
        )
    )

    # Import heavy libraries only when needed
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Loading libraries...", total=None)

        from src.models import get_model
        from src.formatting import (
            format_transcript_markdown,
            get_audio_duration,
        )

        progress.update(task, completed=1)

    # Initialize model
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task(
            f"[cyan]Loading {model} model...",
            total=None,
        )

        try:
            transcription_model = get_model(model, device=device)
            transcription_model.load()
            progress.update(task, completed=1)

            # Show model info
            console.print(
                f"[green]✓[/green] Model loaded: [cyan]{transcription_model.name}[/cyan]"
            )
            console.print(
                f"  Memory usage: [yellow]{transcription_model.memory_usage}[/yellow]"
            )
            console.print(f"  Device: [yellow]{transcription_model.device}[/yellow]\n")

        except Exception as e:
            console.print(f"[red]Error loading model:[/red] {e}")
            raise typer.Exit(1)

    # Get audio duration
    try:
        audio_duration = get_audio_duration(audio_file)
        console.print(
            f"[cyan]Audio duration:[/cyan] {audio_duration:.1f} seconds\n"
        )
    except Exception as e:
        console.print(f"[yellow]Warning:[/yellow] Could not get audio duration: {e}")
        audio_duration = 0

    # Transcribe
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeRemainingColumn(),
        console=console,
    ) as progress:
        task = progress.add_task(
            "[cyan]Transcribing audio...",
            total=100,
        )

        try:
            segments = transcription_model.transcribe(
                audio_file,
                language=language,
            )
            progress.update(task, completed=100)

            console.print(
                f"[green]✓[/green] Transcription complete: "
                f"[cyan]{len(segments)}[/cyan] segments\n"
            )

        except Exception as e:
            console.print(f"[red]Error during transcription:[/red] {e}")
            raise typer.Exit(1)

    # Speaker diarization (optional)
    if diarize:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task(
                "[cyan]Running speaker diarization...",
                total=None,
            )

            try:
                from src.diarization import (
                    SpeakerDiarizer,
                    merge_consecutive_same_speaker,
                )

                diarizer = SpeakerDiarizer(device=device)
                diarizer.load()

                speaker_segments = diarizer.diarize(audio_file)
                segments = diarizer.assign_speakers_to_segments(
                    segments,
                    speaker_segments,
                )

                # Merge consecutive segments from same speaker
                segments = merge_consecutive_same_speaker(segments)

                progress.update(task, completed=1)

                # Count unique speakers
                speakers = set(seg.speaker for seg in segments if seg.speaker)
                console.print(
                    f"[green]✓[/green] Diarization complete: "
                    f"[cyan]{len(speakers)}[/cyan] speakers detected\n"
                )

            except Exception as e:
                console.print(
                    f"[yellow]Warning:[/yellow] Diarization failed: {e}\n"
                    f"Continuing with transcription only..."
                )

    # Format output
    lang_display = language or "auto-detected"
    transcript = format_transcript_markdown(
        segments,
        model_name=transcription_model.name,
        audio_duration=audio_duration if audio_duration > 0 else segments[-1].end if segments else 0,
        language=lang_display,
    )

    # Output
    if output:
        output.write_text(transcript)
        console.print(
            f"[green]✓[/green] Transcript saved to: [cyan]{output}[/cyan]"
        )
    else:
        # Print to stdout
        console.print("\n" + "─" * 80 + "\n")
        console.print(transcript)

    # Show summary
    console.print(
        Panel.fit(
            f"[green]Transcription Complete![/green]\n"
            f"Segments: [cyan]{len(segments)}[/cyan] | "
            f"Model: [cyan]{model}[/cyan]",
            border_style="green",
        )
    )


if __name__ == "__main__":
    app()
