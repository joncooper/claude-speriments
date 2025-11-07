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
from .profile_auditor import ProfileAuditor, Severity


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


@app.command()
def audit(
    tweets: bool = typer.Option(True, help="Audit tweets"),
    likes: bool = typer.Option(True, help="Audit likes"),
    bookmarks: bool = typer.Option(True, help="Audit bookmarks"),
    export: Optional[str] = typer.Option(None, help="Export flagged items to CSV file"),
    show_clean: bool = typer.Option(False, help="Show items that passed audit"),
):
    """
    Audit your Twitter profile for potentially problematic content.

    Identifies political, controversial, NSFW, or unprofessional content
    that you might want to remove before making your profile public.
    """
    settings = get_settings()

    # Check for Gemini API key
    if not settings.validate_gemini_key():
        console.print("[red]✗ Gemini API key not configured[/red]")
        console.print("The audit feature requires Gemini API for analysis")
        console.print("Run: twitter-analyzer init")
        raise typer.Exit(1)

    # Check for database
    db_path = Path(settings.db_path)
    if not db_path.exists():
        console.print("[red]✗ Database not found[/red]")
        console.print("Run: twitter-analyzer fetch first")
        raise typer.Exit(1)

    console.print("\n[bold cyan]🔍 Starting Profile Audit[/bold cyan]\n")
    console.print("[dim]This will analyze your content for political, controversial,")
    console.print("NSFW, profanity, and unprofessional content...[/dim]\n")

    all_flagged = []

    with TwitterDatabase(settings.db_path) as db:
        # Initialize auditor with db connection for logging
        auditor = ProfileAuditor(settings.gemini_api_key, db_conn=db.conn)
        # Audit tweets
        if tweets:
            tweet_list = db.query(
                "SELECT * FROM tweets ORDER BY created_at DESC LIMIT 1000"
            )
            if tweet_list:
                console.print(f"[cyan]Analyzing {len(tweet_list)} tweets...[/cyan]")
                flagged_tweets = auditor.audit_tweets(tweet_list)
                all_flagged.extend(flagged_tweets)
                console.print(f"[yellow]⚠ Found {len(flagged_tweets)} potentially problematic tweets[/yellow]\n")
            else:
                console.print("[dim]No tweets to audit[/dim]\n")

        # Audit likes
        if likes:
            like_list = db.query(
                "SELECT * FROM likes ORDER BY liked_at DESC LIMIT 1000"
            )
            if like_list:
                console.print(f"[cyan]Analyzing {len(like_list)} likes...[/cyan]")
                flagged_likes = auditor.audit_likes(like_list)
                all_flagged.extend(flagged_likes)
                console.print(f"[yellow]⚠ Found {len(flagged_likes)} potentially problematic likes[/yellow]\n")
            else:
                console.print("[dim]No likes to audit[/dim]\n")

        # Audit bookmarks
        if bookmarks:
            bookmark_list = db.query(
                "SELECT * FROM bookmarks ORDER BY bookmarked_at DESC LIMIT 1000"
            )
            if bookmark_list:
                console.print(f"[cyan]Analyzing {len(bookmark_list)} bookmarks...[/cyan]")
                flagged_bookmarks = auditor.audit_bookmarks(bookmark_list)
                all_flagged.extend(flagged_bookmarks)
                console.print(f"[yellow]⚠ Found {len(flagged_bookmarks)} potentially problematic bookmarks[/yellow]\n")
            else:
                console.print("[dim]No bookmarks to audit[/dim]\n")

    # Generate report
    if all_flagged:
        console.print("\n[bold green]✓ Audit Complete[/bold green]\n")

        # Show summary
        high = [f for f in all_flagged if f.severity == Severity.HIGH]
        medium = [f for f in all_flagged if f.severity == Severity.MEDIUM]
        low = [f for f in all_flagged if f.severity == Severity.LOW]

        summary_table = Table(title="Audit Summary", show_header=True)
        summary_table.add_column("Severity", style="bold")
        summary_table.add_column("Count", justify="right")
        summary_table.add_column("Recommendation")

        summary_table.add_row(
            "🔴 HIGH",
            str(len(high)),
            "[red]Review and likely delete[/red]"
        )
        summary_table.add_row(
            "🟡 MEDIUM",
            str(len(medium)),
            "[yellow]Review and assess[/yellow]"
        )
        summary_table.add_row(
            "🟢 LOW",
            str(len(low)),
            "[green]Minor concerns[/green]"
        )

        console.print(summary_table)

        # Generate full report
        report = auditor.generate_report(all_flagged)

        # Save report to file
        report_file = Path("audit_report.md")
        report_file.write_text(report)
        console.print(f"\n[green]✓ Full report saved to: {report_file}[/green]")

        # Export to CSV if requested
        if export:
            import csv
            export_path = Path(export)

            with open(export_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'Type', 'ID', 'Severity', 'Categories', 'Reason', 'Text', 'Created At'
                ])

                for item in all_flagged:
                    categories = ', '.join([c.value for c in item.categories])
                    text = item.text.replace('\n', ' ')[:500]  # Truncate for CSV
                    writer.writerow([
                        item.item_type,
                        item.item_id,
                        item.severity.value,
                        categories,
                        item.reason,
                        text,
                        item.created_at or ''
                    ])

            console.print(f"[green]✓ Exported to CSV: {export_path}[/green]")

        # Show next steps
        console.print("\n[bold cyan]Next Steps:[/bold cyan]")
        console.print("1. Review the full report: [bold]audit_report.md[/bold]")
        console.print("2. Browse flagged content: [bold]twitter-analyzer browse[/bold]")
        console.print("3. Delete problematic tweets manually on Twitter")
        console.print("4. Unlike/unbookmark concerning content")
        console.print("\n[dim]Tip: Use the TUI browser to search for specific topics and review them interactively[/dim]")

    else:
        console.print("[bold green]✓ Great news! No problematic content found.[/bold green]")
        console.print("[dim]Your profile looks professional and appropriate for public viewing.[/dim]")


@app.command()
def logs(
    run_id: Optional[str] = typer.Option(None, help="Show logs for specific run ID"),
    recent: int = typer.Option(1, help="Show N most recent runs"),
    stats: bool = typer.Option(False, help="Show statistics summary"),
):
    """View audit logs and statistics."""
    settings = get_settings()

    db_path = Path(settings.db_path)
    if not db_path.exists():
        console.print("[red]✗ Database not found[/red]")
        raise typer.Exit(1)

    with TwitterDatabase(settings.db_path) as db:
        if stats:
            # Show statistics
            console.print("\n[bold cyan]📊 Audit Statistics[/bold cyan]\n")

            # Total runs
            total_runs = db.query("SELECT COUNT(DISTINCT run_id) as count FROM audit_logs")[0]['count']
            console.print(f"Total audit runs: {total_runs}")

            # Total items analyzed
            total_items = db.query("SELECT COUNT(*) as count FROM audit_logs")[0]['count']
            console.print(f"Total items analyzed: {total_items}")

            # Flagged vs clean
            flagged_count = db.query("SELECT COUNT(*) as count FROM audit_logs WHERE flagged = TRUE")[0]['count']
            clean_count = total_items - flagged_count
            console.print(f"Flagged: {flagged_count} ({flagged_count/total_items*100:.1f}%)")
            console.print(f"Clean: {clean_count} ({clean_count/total_items*100:.1f}%)")

            # By severity
            console.print("\n[bold]By Severity:[/bold]")
            severity_stats = db.query("""
                SELECT severity, COUNT(*) as count
                FROM audit_logs
                WHERE flagged = TRUE
                GROUP BY severity
                ORDER BY count DESC
            """)
            for row in severity_stats:
                console.print(f"  {row['severity']}: {row['count']}")

            # By category
            console.print("\n[bold]Top Categories:[/bold]")
            # This is tricky with JSON, simplified version
            console.print("  (Categories are stored as JSON, use query for details)")

            # API usage
            console.print("\n[bold]API Usage:[/bold]")
            total_tokens = db.query("SELECT SUM(tokens_used) as total FROM audit_logs")[0]['total'] or 0
            avg_latency = db.query("SELECT AVG(api_latency_ms) as avg FROM audit_logs")[0]['avg'] or 0
            console.print(f"Total tokens used: {total_tokens:,}")
            console.print(f"Average latency: {avg_latency:.0f}ms")

        elif run_id:
            # Show specific run
            console.print(f"\n[bold cyan]Audit Run: {run_id}[/bold cyan]\n")

            logs = db.query(f"""
                SELECT item_type, item_id, flagged, severity, reason
                FROM audit_logs
                WHERE run_id = '{run_id}'
                ORDER BY timestamp
            """)

            if not logs:
                console.print("[yellow]No logs found for that run ID[/yellow]")
                return

            flagged_logs = [l for l in logs if l['flagged']]

            console.print(f"Total items: {len(logs)}")
            console.print(f"Flagged: {len(flagged_logs)}")

            if flagged_logs:
                console.print("\n[bold]Flagged Items:[/bold]\n")
                for log in flagged_logs[:20]:
                    console.print(f"[yellow]{log['item_type']} {log['item_id']}[/yellow]")
                    console.print(f"  Severity: {log['severity']}")
                    console.print(f"  Reason: {log['reason']}\n")

        else:
            # Show recent runs
            console.print(f"\n[bold cyan]Recent Audit Runs[/bold cyan]\n")

            runs = db.query(f"""
                SELECT
                    run_id,
                    MIN(timestamp) as started,
                    COUNT(*) as items,
                    SUM(CASE WHEN flagged THEN 1 ELSE 0 END) as flagged,
                    SUM(tokens_used) as tokens,
                    model_name
                FROM audit_logs
                GROUP BY run_id
                ORDER BY started DESC
                LIMIT {recent}
            """)

            if not runs:
                console.print("[yellow]No audit logs found yet[/yellow]")
                console.print("[dim]Run an audit first: twitter-analyzer audit[/dim]")
                return

            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Run ID")
            table.add_column("Started")
            table.add_column("Items")
            table.add_column("Flagged")
            table.add_column("Tokens")
            table.add_column("Model")

            for run in runs:
                started = str(run['started'])[:19] if run['started'] else "Unknown"
                table.add_row(
                    run['run_id'],
                    started,
                    str(run['items']),
                    str(run['flagged']),
                    f"{run['tokens']:,}" if run['tokens'] else "0",
                    run['model_name'] or "unknown"
                )

            console.print(table)
            console.print(f"\n[dim]Use --run-id <ID> to see details of a specific run[/dim]")
            console.print(f"[dim]Use --stats to see overall statistics[/dim]")


if __name__ == "__main__":
    app()
