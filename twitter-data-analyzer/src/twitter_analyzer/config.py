"""Configuration management for Twitter Data Analyzer."""

from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Twitter API Credentials
    twitter_bearer_token: Optional[str] = None
    twitter_api_key: Optional[str] = None
    twitter_api_secret: Optional[str] = None
    twitter_access_token: Optional[str] = None
    twitter_access_secret: Optional[str] = None

    # Google Gemini API Key
    gemini_api_key: Optional[str] = None

    # Database Settings
    db_path: str = "./twitter_data.duckdb"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    def validate_twitter_credentials(self) -> bool:
        """Check if Twitter credentials are configured."""
        return bool(
            self.twitter_bearer_token or
            (self.twitter_api_key and self.twitter_api_secret and
             self.twitter_access_token and self.twitter_access_secret)
        )

    def validate_gemini_key(self) -> bool:
        """Check if Gemini API key is configured."""
        return bool(self.gemini_api_key)


def get_settings() -> Settings:
    """Get application settings."""
    return Settings()
