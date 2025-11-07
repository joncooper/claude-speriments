"""Command-line interface for Twitter Data Analyzer."""

import typer
from typing import Optional
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.panel import Panel

from .config import get_settings
from .database import TwitterDatabase
from .twitter_fetcher import TwitterFetcher
from .gemini_analyzer import GeminiAnalyzer
from .tui import run_tui


app = typer.Typer(
    name="twitter-analyzer",
    help="Download and analyze your Twitter data with DuckDB and Gemini",
    add_completion=False,
)
console = Console()


@app.command()
def init():
    """Initialize the configuration file."""
    env_example = Path(".env.example")
    env_file = Path(".env")

    if env_file.exists():
        console.print("[yellow]⚠ .env file already exists[/yellow]")
        overwrite = typer.confirm("Overwrite it?")
        if not overwrite:
            return

    # Copy .env.example to .env
    if env_example.exists():
        env_file.write_text(env_example.read_text())
        console.print("[green]✓ Created .env file[/green]")
        console.print("\n[cyan]Next steps:[/cyan]")
        console.print("1. Edit .env file with your API credentials")
        console.print("2. Get Twitter API keys from: https://developer.twitter.com/")
        console.print("3. Get Gemini API key from: https://makersuite.google.com/app/apikey")
        console.print("4. Run: twitter-analyzer fetch")
    else:
        console.print("[red]✗ .env.example not found[/red]")


@app.command()
def status():
    """Show configuration and database status."""
    settings = get_settings()

    # Check configuration
    console.print("\n[bold cyan]Configuration Status[/bold cyan]")

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Setting", style="cyan")
    table.add_column("Status", style="green")

    twitter_ok = settings.validate_twitter_credentials()
    gemini_ok = settings.validate_gemini_key()

    table.add_row(
        "Twitter API",
        "✓ Configured" if twitter_ok else "✗ Not configured"
    )
    table.add_row(
        "Gemini API",
        "✓ Configured" if gemini_ok else "✗ Not configured"
    )
    table.add_row("Database Path", settings.db_path)

    console.print(table)

    # Check database stats
    db_path = Path(settings.db_path)
    if db_path.exists():
        console.print("\n[bold cyan]Database Statistics[/bold cyan]")

        with TwitterDatabase(settings.db_path) as db:
            stats = db.get_stats()

            stats_table = Table(show_header=True, header_style="bold magenta")
            stats_table.add_column("Metric", style="cyan")
            stats_table.add_column("Count", style="green", justify="right")

            stats_table.add_row("Tweets", str(stats['total_tweets']))
            stats_table.add_row("Likes", str(stats['total_likes']))
            stats_table.add_row("Bookmarks", str(stats['total_bookmarks']))
            stats_table.add_row("Following", str(stats['total_following']))
            stats_table.add_row("Followers", str(stats['total_followers']))

            console.print(stats_table)
    else:
        console.print("\n[yellow]⚠ Database not found. Run 'twitter-analyzer fetch' first.[/yellow]")


@app.command()
def fetch(
    tweets: bool = typer.Option(True, help="Fetch your tweets"),
    likes: bool = typer.Option(True, help="Fetch your likes"),
    bookmarks: bool = typer.Option(True, help="Fetch your bookmarks"),
    limit: Optional[int] = typer.Option(None, help="Limit number of items to fetch"),
):
    """Fetch your Twitter data and save to database."""
    settings = get_settings()

    if not settings.validate_twitter_credentials():
        console.print("[red]✗ Twitter API credentials not configured[/red]")
        console.print("Run: twitter-analyzer init")
        raise typer.Exit(1)

    console.print("[bold cyan]Fetching Twitter Data[/bold cyan]\n")

    # Initialize Twitter client
    fetcher = TwitterFetcher(
        bearer_token=settings.twitter_bearer_token,
        api_key=settings.twitter_api_key,
        api_secret=settings.twitter_api_secret,
        access_token=settings.twitter_access_token,
        access_secret=settings.twitter_access_secret,
    )

    # Get authenticated user
    console.print("[cyan]Authenticating...[/cyan]")
    user = fetcher.get_authenticated_user()
    console.print(f"[green]✓ Authenticated as @{user['username']}[/green]\n")

    # Initialize database
    with TwitterDatabase(settings.db_path) as db:
        # Save user profile
        db.upsert_user_profile(user)

        user_id = user['id']

        # Fetch tweets
        if tweets:
            tweet_list = fetcher.fetch_user_tweets(user_id, limit=limit)
            if tweet_list:
                db.insert_tweets(tweet_list)

        # Fetch likes
        if likes:
            like_list = fetcher.fetch_liked_tweets(user_id, limit=limit)
            if like_list:
                db.insert_likes(user_id, like_list)

        # Fetch bookmarks
        if bookmarks:
            bookmark_list = fetcher.fetch_bookmarks(limit=limit)
            if bookmark_list:
                db.insert_bookmarks(user_id, bookmark_list)

        # Show final stats
        console.print("\n[bold green]Fetch Complete![/bold green]\n")
        stats = db.get_stats()

        table = Table(show_header=False)
        table.add_column("Metric", style="cyan")
        table.add_column("Count", style="green", justify="right")

        table.add_row("Total Tweets", str(stats['total_tweets']))
        table.add_row("Total Likes", str(stats['total_likes']))
        table.add_row("Total Bookmarks", str(stats['total_bookmarks']))

        console.print(table)


@app.command()
def analyze(
    target: str = typer.Argument("tweets", help="What to analyze: tweets, likes, bookmarks, summary"),
    analysis_type: str = typer.Option("general", help="Analysis type: general, sentiment, topics, patterns"),
):
    """Analyze your Twitter data using Gemini."""
    settings = get_settings()

    if not settings.validate_gemini_key():
        console.print("[red]✗ Gemini API key not configured[/red]")
        console.print("Run: twitter-analyzer init")
        raise typer.Exit(1)

    db_path = Path(settings.db_path)
    if not db_path.exists():
        console.print("[red]✗ Database not found[/red]")
        console.print("Run: twitter-analyzer fetch first")
        raise typer.Exit(1)

    # Initialize Gemini
    analyzer = GeminiAnalyzer(settings.gemini_api_key)

    with TwitterDatabase(settings.db_path) as db:
        if target == "tweets":
            tweets = db.query("SELECT * FROM tweets ORDER BY created_at DESC LIMIT 100")
            if not tweets:
                console.print("[yellow]No tweets found in database[/yellow]")
                return

            result = analyzer.analyze_tweets(tweets, analysis_type)

        elif target == "likes":
            likes = db.query("SELECT * FROM likes ORDER BY liked_at DESC LIMIT 100")
            if not likes:
                console.print("[yellow]No likes found in database[/yellow]")
                return

            result = analyzer.analyze_likes(likes)

        elif target == "bookmarks":
            bookmarks = db.query("SELECT * FROM bookmarks ORDER BY bookmarked_at DESC LIMIT 100")
            if not bookmarks:
                console.print("[yellow]No bookmarks found in database[/yellow]")
                return

            result = analyzer.analyze_bookmarks(bookmarks)

        elif target == "summary":
            stats = db.get_stats()
            tweets = db.query("SELECT * FROM tweets ORDER BY created_at DESC LIMIT 20")
            likes = db.query("SELECT * FROM likes ORDER BY liked_at DESC LIMIT 20")

            result = analyzer.generate_summary(stats, tweets, likes)

        else:
            console.print(f"[red]Unknown target: {target}[/red]")
            console.print("Valid targets: tweets, likes, bookmarks, summary")
            raise typer.Exit(1)

    # Display results
    console.print("\n")
    console.print(Panel(Markdown(result), title=f"Analysis: {target}", border_style="cyan"))


@app.command()
def query(sql: str = typer.Argument(..., help="SQL query to run")):
    """Run a custom SQL query on the database."""
    settings = get_settings()

    db_path = Path(settings.db_path)
    if not db_path.exists():
        console.print("[red]✗ Database not found[/red]")
        console.print("Run: twitter-analyzer fetch first")
        raise typer.Exit(1)

    with TwitterDatabase(settings.db_path) as db:
        try:
            results = db.query(sql)

            if not results:
                console.print("[yellow]No results found[/yellow]")
                return

            # Display as table
            if results:
                table = Table(show_header=True, header_style="bold magenta")

                # Add columns
                for key in results[0].keys():
                    table.add_column(key, style="cyan")

                # Add rows (limit to 50)
                for row in results[:50]:
                    table.add_row(*[str(v) for v in row.values()])

                console.print(table)

                if len(results) > 50:
                    console.print(f"\n[yellow]Showing first 50 of {len(results)} results[/yellow]")

        except Exception as e:
            console.print(f"[red]Query error: {e}[/red]")
            raise typer.Exit(1)


@app.command()
def ask(question: str = typer.Argument(..., help="Question to ask about your Twitter data")):
    """Ask a custom question about your Twitter data."""
    settings = get_settings()

    if not settings.validate_gemini_key():
        console.print("[red]✗ Gemini API key not configured[/red]")
        raise typer.Exit(1)

    db_path = Path(settings.db_path)
    if not db_path.exists():
        console.print("[red]✗ Database not found[/red]")
        raise typer.Exit(1)

    with TwitterDatabase(settings.db_path) as db:
        # Get recent data for context
        tweets = db.query("SELECT text, created_at FROM tweets ORDER BY created_at DESC LIMIT 50")
        likes = db.query("SELECT tweet_text FROM likes LIMIT 50")
        stats = db.get_stats()

        # Prepare context
        context = f"""Statistics:
- Tweets: {stats['total_tweets']}
- Likes: {stats['total_likes']}
- Bookmarks: {stats['total_bookmarks']}

Recent tweets:
{chr(10).join([f"- {t['text']}" for t in tweets[:20]])}

Recent likes:
{chr(10).join([f"- {l['tweet_text']}" for l in likes[:20]])}
"""

    # Ask Gemini
    analyzer = GeminiAnalyzer(settings.gemini_api_key)
    result = analyzer.custom_analysis(context, question)

    console.print("\n")
    console.print(Panel(Markdown(result), title="Answer", border_style="cyan"))


@app.command()
def browse():
    """Launch interactive browser to explore your Twitter data with keyboard navigation."""
    settings = get_settings()

    db_path = Path(settings.db_path)
    if not db_path.exists():
        console.print("[red]✗ Database not found[/red]")
        console.print("Run: twitter-analyzer fetch first")
        raise typer.Exit(1)

    console.print("[cyan]Launching interactive browser...[/cyan]")
    console.print("[dim]Use arrow keys to navigate, Tab to switch tabs, / to search, q to quit[/dim]\n")

    try:
        run_tui(settings.db_path)
    except KeyboardInterrupt:
        console.print("\n[yellow]Browser closed[/yellow]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
