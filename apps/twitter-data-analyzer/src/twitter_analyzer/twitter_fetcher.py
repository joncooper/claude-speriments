"""Twitter data fetcher using Twitter API v2."""

import tweepy
from typing import List, Dict, Any, Optional
from datetime import datetime
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn


console = Console()


class TwitterFetcher:
    """Fetch Twitter data using the Twitter API v2."""

    def __init__(
        self,
        bearer_token: Optional[str] = None,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        access_token: Optional[str] = None,
        access_secret: Optional[str] = None,
    ):
        """Initialize Twitter API client."""
        self.client: Optional[tweepy.Client] = None

        # Try bearer token first (OAuth 2.0)
        if bearer_token:
            self.client = tweepy.Client(bearer_token=bearer_token)
        # Fall back to OAuth 1.0a
        elif all([api_key, api_secret, access_token, access_secret]):
            self.client = tweepy.Client(
                consumer_key=api_key,
                consumer_secret=api_secret,
                access_token=access_token,
                access_token_secret=access_secret,
            )
        else:
            raise ValueError(
                "Either bearer_token or all of (api_key, api_secret, "
                "access_token, access_secret) must be provided"
            )

    def get_authenticated_user(self) -> Dict[str, Any]:
        """Get the authenticated user's profile."""
        if not self.client:
            raise RuntimeError("Client not initialized")

        user = self.client.get_me(
            user_fields=[
                'created_at', 'description', 'public_metrics',
                'verified', 'profile_image_url'
            ]
        )

        if not user.data:
            raise RuntimeError("Could not fetch authenticated user")

        return user.data.data

    def fetch_user_tweets(
        self,
        user_id: int,
        max_results: int = 100,
        limit: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Fetch all tweets from a user.

        Args:
            user_id: The Twitter user ID
            max_results: Results per page (max 100)
            limit: Maximum total tweets to fetch (None for all)
        """
        if not self.client:
            raise RuntimeError("Client not initialized")

        tweets = []
        pagination_token = None
        fetched = 0

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Fetching tweets...", total=None)

            while True:
                try:
                    response = self.client.get_users_tweets(
                        id=user_id,
                        max_results=min(max_results, 100),
                        pagination_token=pagination_token,
                        tweet_fields=[
                            'created_at', 'public_metrics', 'conversation_id',
                            'in_reply_to_user_id', 'referenced_tweets', 'entities',
                            'lang', 'possibly_sensitive', 'source'
                        ],
                    )

                    if response.data:
                        batch = [tweet.data for tweet in response.data]
                        tweets.extend(batch)
                        fetched += len(batch)
                        progress.update(task, description=f"Fetched {fetched} tweets...")

                        if limit and fetched >= limit:
                            break

                    # Check for more pages
                    if hasattr(response, 'meta') and 'next_token' in response.meta:
                        pagination_token = response.meta['next_token']
                    else:
                        break

                except tweepy.TooManyRequests:
                    console.print("[yellow]Rate limit hit. Stopping fetch.[/yellow]")
                    break
                except Exception as e:
                    console.print(f"[red]Error fetching tweets: {e}[/red]")
                    break

        console.print(f"[green]✓ Fetched {len(tweets)} tweets[/green]")
        return tweets

    def fetch_liked_tweets(
        self,
        user_id: int,
        max_results: int = 100,
        limit: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Fetch all liked tweets for a user.

        Args:
            user_id: The Twitter user ID
            max_results: Results per page (max 100)
            limit: Maximum total likes to fetch (None for all)
        """
        if not self.client:
            raise RuntimeError("Client not initialized")

        likes = []
        pagination_token = None
        fetched = 0

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Fetching likes...", total=None)

            while True:
                try:
                    response = self.client.get_liked_tweets(
                        id=user_id,
                        max_results=min(max_results, 100),
                        pagination_token=pagination_token,
                        tweet_fields=[
                            'created_at', 'public_metrics', 'author_id', 'entities'
                        ],
                    )

                    if response.data:
                        batch = [tweet.data for tweet in response.data]
                        likes.extend(batch)
                        fetched += len(batch)
                        progress.update(task, description=f"Fetched {fetched} likes...")

                        if limit and fetched >= limit:
                            break

                    # Check for more pages
                    if hasattr(response, 'meta') and 'next_token' in response.meta:
                        pagination_token = response.meta['next_token']
                    else:
                        break

                except tweepy.TooManyRequests:
                    console.print("[yellow]Rate limit hit. Stopping fetch.[/yellow]")
                    break
                except Exception as e:
                    console.print(f"[red]Error fetching likes: {e}[/red]")
                    break

        console.print(f"[green]✓ Fetched {len(likes)} likes[/green]")
        return likes

    def fetch_bookmarks(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Fetch bookmarked tweets for the authenticated user.

        Note: Bookmarks endpoint requires OAuth 2.0 with specific scopes.
        """
        if not self.client:
            raise RuntimeError("Client not initialized")

        bookmarks = []
        pagination_token = None
        fetched = 0

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Fetching bookmarks...", total=None)

            while True:
                try:
                    response = self.client.get_bookmarks(
                        pagination_token=pagination_token,
                        max_results=100,
                        tweet_fields=[
                            'created_at', 'public_metrics', 'author_id', 'entities'
                        ],
                    )

                    if response.data:
                        batch = [tweet.data for tweet in response.data]
                        bookmarks.extend(batch)
                        fetched += len(batch)
                        progress.update(task, description=f"Fetched {fetched} bookmarks...")

                        if limit and fetched >= limit:
                            break

                    # Check for more pages
                    if hasattr(response, 'meta') and 'next_token' in response.meta:
                        pagination_token = response.meta['next_token']
                    else:
                        break

                except tweepy.TooManyRequests:
                    console.print("[yellow]Rate limit hit. Stopping fetch.[/yellow]")
                    break
                except tweepy.Forbidden as e:
                    console.print(
                        "[yellow]Bookmarks endpoint requires OAuth 2.0 with proper scopes.[/yellow]"
                    )
                    console.print(f"[yellow]Error: {e}[/yellow]")
                    break
                except Exception as e:
                    console.print(f"[red]Error fetching bookmarks: {e}[/red]")
                    break

        if bookmarks:
            console.print(f"[green]✓ Fetched {len(bookmarks)} bookmarks[/green]")
        return bookmarks
