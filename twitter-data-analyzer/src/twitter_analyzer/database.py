"""Database management with DuckDB."""

import duckdb
from pathlib import Path
from typing import Optional, List, Dict, Any
from datetime import datetime
import json


class TwitterDatabase:
    """Manage Twitter data in DuckDB."""

    def __init__(self, db_path: str):
        """Initialize database connection."""
        self.db_path = db_path
        self.conn: Optional[duckdb.DuckDBPyConnection] = None

    def connect(self):
        """Connect to the database."""
        self.conn = duckdb.connect(self.db_path)
        self._create_tables()

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None

    def _create_tables(self):
        """Create database schema."""
        if not self.conn:
            raise RuntimeError("Database not connected")

        # User profile table
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS user_profile (
                id BIGINT PRIMARY KEY,
                username VARCHAR,
                name VARCHAR,
                description TEXT,
                followers_count INTEGER,
                following_count INTEGER,
                tweet_count INTEGER,
                created_at TIMESTAMP,
                verified BOOLEAN,
                profile_image_url VARCHAR,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Tweets table
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS tweets (
                id BIGINT PRIMARY KEY,
                text TEXT,
                created_at TIMESTAMP,
                author_id BIGINT,
                conversation_id BIGINT,
                in_reply_to_user_id BIGINT,
                retweet_count INTEGER,
                reply_count INTEGER,
                like_count INTEGER,
                quote_count INTEGER,
                bookmark_count INTEGER,
                impression_count INTEGER,
                lang VARCHAR,
                possibly_sensitive BOOLEAN,
                source VARCHAR,
                entities JSON,
                referenced_tweets JSON,
                fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Likes table
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS likes (
                user_id BIGINT,
                tweet_id BIGINT,
                tweet_text TEXT,
                tweet_author_id BIGINT,
                tweet_created_at TIMESTAMP,
                liked_at TIMESTAMP,
                fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (user_id, tweet_id)
            )
        """)

        # Bookmarks table
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS bookmarks (
                user_id BIGINT,
                tweet_id BIGINT,
                tweet_text TEXT,
                tweet_author_id BIGINT,
                tweet_created_at TIMESTAMP,
                bookmarked_at TIMESTAMP,
                fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (user_id, tweet_id)
            )
        """)

        # Following table
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS following (
                user_id BIGINT,
                following_user_id BIGINT,
                following_username VARCHAR,
                following_name VARCHAR,
                followed_at TIMESTAMP,
                fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (user_id, following_user_id)
            )
        """)

        # Followers table
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS followers (
                user_id BIGINT,
                follower_user_id BIGINT,
                follower_username VARCHAR,
                follower_name VARCHAR,
                followed_at TIMESTAMP,
                fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (user_id, follower_user_id)
            )
        """)

        # Audit logs table
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS audit_logs (
                id INTEGER PRIMARY KEY,
                run_id VARCHAR,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                item_type VARCHAR,
                item_id BIGINT,
                flagged BOOLEAN,
                severity VARCHAR,
                categories JSON,
                reason TEXT,
                prompt_version VARCHAR,
                model_name VARCHAR,
                tokens_used INTEGER,
                api_latency_ms INTEGER
            )
        """)

        # Create indexes for common queries
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_tweets_author ON tweets(author_id)")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_tweets_created ON tweets(created_at)")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_likes_user ON likes(user_id)")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_bookmarks_user ON bookmarks(user_id)")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_audit_logs_run ON audit_logs(run_id)")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_audit_logs_item ON audit_logs(item_type, item_id)")

    def upsert_user_profile(self, user_data: Dict[str, Any]):
        """Insert or update user profile."""
        if not self.conn:
            raise RuntimeError("Database not connected")

        self.conn.execute("""
            INSERT OR REPLACE INTO user_profile (
                id, username, name, description, followers_count,
                following_count, tweet_count, created_at, verified,
                profile_image_url, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        """, [
            user_data.get('id'),
            user_data.get('username'),
            user_data.get('name'),
            user_data.get('description'),
            user_data.get('public_metrics', {}).get('followers_count'),
            user_data.get('public_metrics', {}).get('following_count'),
            user_data.get('public_metrics', {}).get('tweet_count'),
            user_data.get('created_at'),
            user_data.get('verified', False),
            user_data.get('profile_image_url'),
        ])

    def insert_tweets(self, tweets: List[Dict[str, Any]]):
        """Insert tweets into database."""
        if not self.conn:
            raise RuntimeError("Database not connected")

        for tweet in tweets:
            metrics = tweet.get('public_metrics', {})
            self.conn.execute("""
                INSERT OR REPLACE INTO tweets (
                    id, text, created_at, author_id, conversation_id,
                    in_reply_to_user_id, retweet_count, reply_count,
                    like_count, quote_count, bookmark_count, impression_count,
                    lang, possibly_sensitive, source, entities, referenced_tweets
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, [
                tweet.get('id'),
                tweet.get('text'),
                tweet.get('created_at'),
                tweet.get('author_id'),
                tweet.get('conversation_id'),
                tweet.get('in_reply_to_user_id'),
                metrics.get('retweet_count', 0),
                metrics.get('reply_count', 0),
                metrics.get('like_count', 0),
                metrics.get('quote_count', 0),
                metrics.get('bookmark_count', 0),
                metrics.get('impression_count', 0),
                tweet.get('lang'),
                tweet.get('possibly_sensitive', False),
                tweet.get('source'),
                json.dumps(tweet.get('entities')) if tweet.get('entities') else None,
                json.dumps(tweet.get('referenced_tweets')) if tweet.get('referenced_tweets') else None,
            ])

    def insert_likes(self, user_id: int, likes: List[Dict[str, Any]]):
        """Insert liked tweets into database."""
        if not self.conn:
            raise RuntimeError("Database not connected")

        for tweet in likes:
            self.conn.execute("""
                INSERT OR REPLACE INTO likes (
                    user_id, tweet_id, tweet_text, tweet_author_id,
                    tweet_created_at, liked_at
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, [
                user_id,
                tweet.get('id'),
                tweet.get('text'),
                tweet.get('author_id'),
                tweet.get('created_at'),
                tweet.get('created_at'),  # We don't have actual like timestamp from API
            ])

    def insert_bookmarks(self, user_id: int, bookmarks: List[Dict[str, Any]]):
        """Insert bookmarked tweets into database."""
        if not self.conn:
            raise RuntimeError("Database not connected")

        for tweet in bookmarks:
            self.conn.execute("""
                INSERT OR REPLACE INTO bookmarks (
                    user_id, tweet_id, tweet_text, tweet_author_id,
                    tweet_created_at, bookmarked_at
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, [
                user_id,
                tweet.get('id'),
                tweet.get('text'),
                tweet.get('author_id'),
                tweet.get('created_at'),
                tweet.get('created_at'),  # We don't have actual bookmark timestamp
            ])

    def query(self, sql: str) -> List[Dict[str, Any]]:
        """Execute a SQL query and return results as list of dicts."""
        if not self.conn:
            raise RuntimeError("Database not connected")

        result = self.conn.execute(sql).fetchall()
        columns = [desc[0] for desc in self.conn.description]
        return [dict(zip(columns, row)) for row in result]

    def get_stats(self) -> Dict[str, int]:
        """Get database statistics."""
        if not self.conn:
            raise RuntimeError("Database not connected")

        return {
            'total_tweets': self.conn.execute("SELECT COUNT(*) FROM tweets").fetchone()[0],
            'total_likes': self.conn.execute("SELECT COUNT(*) FROM likes").fetchone()[0],
            'total_bookmarks': self.conn.execute("SELECT COUNT(*) FROM bookmarks").fetchone()[0],
            'total_following': self.conn.execute("SELECT COUNT(*) FROM following").fetchone()[0],
            'total_followers': self.conn.execute("SELECT COUNT(*) FROM followers").fetchone()[0],
        }

    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
