"""Interactive Text User Interface for browsing Twitter data."""

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical, VerticalScroll
from textual.widgets import (
    Header,
    Footer,
    DataTable,
    Static,
    TabbedContent,
    TabPane,
    Input,
    Label,
    Button,
)
from textual.binding import Binding
from textual.reactive import reactive
from datetime import datetime
from typing import List, Dict, Any, Optional

from .database import TwitterDatabase
from .config import get_settings


class StatsPanel(Static):
    """Display statistics about the Twitter data."""

    def __init__(self, db: TwitterDatabase):
        super().__init__()
        self.db = db

    def compose(self) -> ComposeResult:
        stats = self.db.get_stats()
        yield Static(
            f"""[bold cyan]📊 Database Statistics[/bold cyan]

[yellow]Tweets:[/yellow] {stats['total_tweets']:,}
[yellow]Likes:[/yellow] {stats['total_likes']:,}
[yellow]Bookmarks:[/yellow] {stats['total_bookmarks']:,}
[yellow]Following:[/yellow] {stats['total_following']:,}
[yellow]Followers:[/yellow] {stats['total_followers']:,}
""",
            id="stats-content",
        )


class TweetDetail(Static):
    """Display detailed information about a selected tweet."""

    tweet_data = reactive(None)

    def watch_tweet_data(self, tweet_data: Optional[Dict[str, Any]]) -> None:
        """Update display when tweet changes."""
        if tweet_data:
            created_at = tweet_data.get("created_at", "")
            if isinstance(created_at, str):
                try:
                    created_at = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
                    created_at = created_at.strftime("%Y-%m-%d %H:%M:%S")
                except:
                    pass

            content = f"""[bold cyan]📄 Tweet Details[/bold cyan]

[yellow]Text:[/yellow]
{tweet_data.get('text', 'N/A')}

[yellow]Created:[/yellow] {created_at}
[yellow]Likes:[/yellow] {tweet_data.get('like_count', 0):,}
[yellow]Retweets:[/yellow] {tweet_data.get('retweet_count', 0):,}
[yellow]Replies:[/yellow] {tweet_data.get('reply_count', 0):,}
[yellow]Language:[/yellow] {tweet_data.get('lang', 'N/A')}

[dim]Press [b]ESC[/b] to clear selection[/dim]
"""
        else:
            content = """[bold cyan]📄 Tweet Details[/bold cyan]

[dim]Select a tweet to view details[/dim]
"""
        self.update(content)


class TwitterBrowserApp(App):
    """Interactive browser for Twitter data."""

    CSS = """
    Screen {
        layout: horizontal;
    }

    #left-panel {
        width: 70%;
        height: 100%;
    }

    #right-panel {
        width: 30%;
        height: 100%;
        border-left: solid $primary;
    }

    #stats-panel {
        height: auto;
        padding: 1;
        border-bottom: solid $primary;
    }

    #detail-panel {
        height: 1fr;
        padding: 1;
    }

    #search-container {
        height: auto;
        padding: 1;
        border-bottom: solid $primary;
    }

    #table-container {
        height: 1fr;
    }

    DataTable {
        height: 100%;
    }

    Input {
        width: 100%;
    }

    TweetDetail {
        height: 100%;
    }

    StatsPanel {
        height: auto;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("t", "focus_tweets", "Tweets"),
        Binding("l", "focus_likes", "Likes"),
        Binding("b", "focus_bookmarks", "Bookmarks"),
        Binding("slash", "focus_search", "Search"),
        Binding("escape", "clear_selection", "Clear"),
    ]

    def __init__(self, db_path: str):
        super().__init__()
        self.db = TwitterDatabase(db_path)
        self.current_tab = "tweets"
        self.search_query = ""

    async def on_mount(self) -> None:
        """Initialize the app when mounted."""
        self.db.connect()
        self.title = "Twitter Data Browser"
        self.sub_title = "Press 'q' to quit, 't' for tweets, 'l' for likes, 'b' for bookmarks"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()

        with Horizontal():
            # Left panel with tabs and data tables
            with Vertical(id="left-panel"):
                with Container(id="search-container"):
                    yield Input(
                        placeholder="Type to search... (press / to focus)",
                        id="search-input",
                    )

                with TabbedContent(id="data-tabs"):
                    with TabPane("Tweets", id="tweets-tab"):
                        yield DataTable(id="tweets-table", zebra_stripes=True, cursor_type="row")

                    with TabPane("Likes", id="likes-tab"):
                        yield DataTable(id="likes-table", zebra_stripes=True, cursor_type="row")

                    with TabPane("Bookmarks", id="bookmarks-tab"):
                        yield DataTable(
                            id="bookmarks-table", zebra_stripes=True, cursor_type="row"
                        )

            # Right panel with stats and details
            with Vertical(id="right-panel"):
                with Container(id="stats-panel"):
                    yield StatsPanel(self.db)

                with VerticalScroll(id="detail-panel"):
                    yield TweetDetail(id="tweet-detail")

        yield Footer()

    async def on_ready(self) -> None:
        """Load data after app is ready."""
        await self.load_tweets()
        await self.load_likes()
        await self.load_bookmarks()

    async def load_tweets(self) -> None:
        """Load tweets into the table."""
        table = self.query_one("#tweets-table", DataTable)
        table.clear(columns=True)

        table.add_columns("Date", "Text", "❤️", "🔄", "💬")

        query = """
            SELECT id, created_at, text, like_count, retweet_count, reply_count,
                   lang, author_id, conversation_id
            FROM tweets
            ORDER BY created_at DESC
            LIMIT 1000
        """

        if self.search_query:
            query = f"""
                SELECT id, created_at, text, like_count, retweet_count, reply_count,
                       lang, author_id, conversation_id
                FROM tweets
                WHERE text LIKE '%{self.search_query}%'
                ORDER BY created_at DESC
                LIMIT 1000
            """

        tweets = self.db.query(query)

        for tweet in tweets:
            created_at = tweet.get("created_at", "")
            if isinstance(created_at, str):
                try:
                    dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
                    created_at = dt.strftime("%Y-%m-%d")
                except:
                    created_at = created_at[:10] if len(created_at) >= 10 else created_at

            # Truncate text for display
            text = tweet.get("text", "")
            if len(text) > 60:
                text = text[:57] + "..."

            table.add_row(
                created_at,
                text,
                str(tweet.get("like_count", 0)),
                str(tweet.get("retweet_count", 0)),
                str(tweet.get("reply_count", 0)),
                key=str(tweet.get("id")),
            )

    async def load_likes(self) -> None:
        """Load likes into the table."""
        table = self.query_one("#likes-table", DataTable)
        table.clear(columns=True)

        table.add_columns("Date", "Text", "Author")

        query = """
            SELECT tweet_id, tweet_created_at, tweet_text, tweet_author_id
            FROM likes
            ORDER BY liked_at DESC
            LIMIT 1000
        """

        if self.search_query:
            query = f"""
                SELECT tweet_id, tweet_created_at, tweet_text, tweet_author_id
                FROM likes
                WHERE tweet_text LIKE '%{self.search_query}%'
                ORDER BY liked_at DESC
                LIMIT 1000
            """

        likes = self.db.query(query)

        for like in likes:
            created_at = like.get("tweet_created_at", "")
            if isinstance(created_at, str):
                try:
                    dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
                    created_at = dt.strftime("%Y-%m-%d")
                except:
                    created_at = created_at[:10] if len(created_at) >= 10 else created_at

            text = like.get("tweet_text", "")
            if len(text) > 50:
                text = text[:47] + "..."

            author = str(like.get("tweet_author_id", ""))[:15]

            table.add_row(
                created_at,
                text,
                author,
                key=str(like.get("tweet_id")),
            )

    async def load_bookmarks(self) -> None:
        """Load bookmarks into the table."""
        table = self.query_one("#bookmarks-table", DataTable)
        table.clear(columns=True)

        table.add_columns("Date", "Text", "Author")

        query = """
            SELECT tweet_id, tweet_created_at, tweet_text, tweet_author_id
            FROM bookmarks
            ORDER BY bookmarked_at DESC
            LIMIT 1000
        """

        if self.search_query:
            query = f"""
                SELECT tweet_id, tweet_created_at, tweet_text, tweet_author_id
                FROM bookmarks
                WHERE tweet_text LIKE '%{self.search_query}%'
                ORDER BY bookmarked_at DESC
                LIMIT 1000
            """

        bookmarks = self.db.query(query)

        for bookmark in bookmarks:
            created_at = bookmark.get("tweet_created_at", "")
            if isinstance(created_at, str):
                try:
                    dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
                    created_at = dt.strftime("%Y-%m-%d")
                except:
                    created_at = created_at[:10] if len(created_at) >= 10 else created_at

            text = bookmark.get("tweet_text", "")
            if len(text) > 50:
                text = text[:47] + "..."

            author = str(bookmark.get("tweet_author_id", ""))[:15]

            table.add_row(
                created_at,
                text,
                author,
                key=str(bookmark.get("tweet_id")),
            )

    async def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        """Handle row selection in any table."""
        tweet_id = event.row_key

        # Determine which table was clicked
        if event.data_table.id == "tweets-table":
            query = f"""
                SELECT * FROM tweets WHERE id = {tweet_id}
            """
        elif event.data_table.id == "likes-table":
            query = f"""
                SELECT tweet_text as text, tweet_created_at as created_at,
                       tweet_id as id, 0 as like_count, 0 as retweet_count,
                       0 as reply_count, '' as lang
                FROM likes WHERE tweet_id = {tweet_id}
            """
        else:  # bookmarks-table
            query = f"""
                SELECT tweet_text as text, tweet_created_at as created_at,
                       tweet_id as id, 0 as like_count, 0 as retweet_count,
                       0 as reply_count, '' as lang
                FROM bookmarks WHERE tweet_id = {tweet_id}
            """

        result = self.db.query(query)
        if result:
            detail_widget = self.query_one("#tweet-detail", TweetDetail)
            detail_widget.tweet_data = result[0]

    async def on_input_changed(self, event: Input.Changed) -> None:
        """Handle search input changes."""
        if event.input.id == "search-input":
            self.search_query = event.value
            # Reload the current table
            await self.reload_current_table()

    async def reload_current_table(self) -> None:
        """Reload the currently active table."""
        tabs = self.query_one("#data-tabs", TabbedContent)
        active_tab = tabs.active

        if active_tab == "tweets-tab":
            await self.load_tweets()
        elif active_tab == "likes-tab":
            await self.load_likes()
        elif active_tab == "bookmarks-tab":
            await self.load_bookmarks()

    def action_focus_tweets(self) -> None:
        """Focus the tweets tab."""
        tabs = self.query_one("#data-tabs", TabbedContent)
        tabs.active = "tweets-tab"

    def action_focus_likes(self) -> None:
        """Focus the likes tab."""
        tabs = self.query_one("#data-tabs", TabbedContent)
        tabs.active = "likes-tab"

    def action_focus_bookmarks(self) -> None:
        """Focus the bookmarks tab."""
        tabs = self.query_one("#data-tabs", TabbedContent)
        tabs.active = "bookmarks-tab"

    def action_focus_search(self) -> None:
        """Focus the search input."""
        search_input = self.query_one("#search-input", Input)
        search_input.focus()

    def action_clear_selection(self) -> None:
        """Clear the current tweet selection."""
        detail_widget = self.query_one("#tweet-detail", TweetDetail)
        detail_widget.tweet_data = None

    def on_unmount(self) -> None:
        """Clean up when app closes."""
        self.db.close()


def run_tui(db_path: str) -> None:
    """Run the Text User Interface."""
    app = TwitterBrowserApp(db_path)
    app.run()
