# Twitter Data Analyzer

A command-line utility to download, store, and analyze your Twitter/X data using DuckDB and Google Gemini AI.

## Features

- **Download Your Twitter Data**: Fetch all your tweets, likes, and bookmarks via Twitter API v2
- **Local Storage**: Store everything in a fast, queryable DuckDB database
- **AI-Powered Analysis**: Use Google Gemini to gain insights into your Twitter activity
- **SQL Queries**: Run custom SQL queries on your data
- **Privacy-First**: All data stays local on your machine

## What You Can Analyze

- **Tweets**: Your posting patterns, topics, sentiment, and engagement
- **Likes**: What content you engage with and your interests
- **Bookmarks**: What you save for later and why
- **Summary**: Comprehensive overview of your Twitter presence

## Installation

### Prerequisites

- Python 3.9 or higher
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- Twitter API credentials ([get them here](https://developer.twitter.com/en/portal/dashboard))
- Google Gemini API key ([get it here](https://makersuite.google.com/app/apikey))

### Setup

1. **Install uv** (if you don't have it):
   ```bash
   # macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

   # Or with pip
   pip install uv
   ```

2. **Clone or navigate to this directory**:
   ```bash
   cd twitter-data-analyzer
   ```

3. **Install dependencies with uv** (recommended):
   ```bash
   # Create virtual environment and install dependencies
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e .
   ```

   Or use pip (alternative):
   ```bash
   pip install -r requirements.txt
   # Or: pip install -e .
   ```

4. **Initialize configuration**:
   ```bash
   python -m twitter_analyzer.cli init
   ```

5. **Configure API keys**: Edit the `.env` file with your credentials:
   ```bash
   # Twitter API Credentials
   TWITTER_BEARER_TOKEN=your_bearer_token_here
   # OR use OAuth 1.0a:
   TWITTER_API_KEY=your_api_key_here
   TWITTER_API_SECRET=your_api_secret_here
   TWITTER_ACCESS_TOKEN=your_access_token_here
   TWITTER_ACCESS_SECRET=your_access_token_secret_here

   # Google Gemini API Key
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Getting Twitter API Credentials

1. Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. Create a new project and app
3. Enable OAuth 2.0 or get your bearer token
4. For OAuth 1.0a, you'll need: API Key, API Secret, Access Token, and Access Token Secret
5. Copy these values to your `.env` file

## Getting Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the key to your `.env` file

## Usage

### Check Configuration Status

```bash
python -m twitter_analyzer.cli status
```

Shows your configuration status and database statistics.

### Fetch Your Twitter Data

```bash
# Fetch everything
python -m twitter_analyzer.cli fetch

# Fetch only tweets
python -m twitter_analyzer.cli fetch --no-likes --no-bookmarks

# Fetch with a limit
python -m twitter_analyzer.cli fetch --limit 100
```

This will:
1. Authenticate with Twitter
2. Download your tweets, likes, and bookmarks
3. Store everything in `twitter_data.duckdb`

### Analyze Your Data

```bash
# General analysis of tweets
python -m twitter_analyzer.cli analyze tweets

# Sentiment analysis
python -m twitter_analyzer.cli analyze tweets --analysis-type sentiment

# Topic analysis
python -m twitter_analyzer.cli analyze tweets --analysis-type topics

# Pattern analysis
python -m twitter_analyzer.cli analyze tweets --analysis-type patterns

# Analyze likes
python -m twitter_analyzer.cli analyze likes

# Analyze bookmarks
python -m twitter_analyzer.cli analyze bookmarks

# Get a comprehensive summary
python -m twitter_analyzer.cli analyze summary
```

### Ask Custom Questions

```bash
python -m twitter_analyzer.cli ask "What are my main interests based on my likes?"
python -m twitter_analyzer.cli ask "How has my tweeting style changed over time?"
python -m twitter_analyzer.cli ask "What topics do I tweet about most?"
```

### Run SQL Queries

```bash
# Most liked tweets
python -m twitter_analyzer.cli query "SELECT text, like_count FROM tweets ORDER BY like_count DESC LIMIT 10"

# Tweets per month
python -m twitter_analyzer.cli query "SELECT DATE_TRUNC('month', created_at) as month, COUNT(*) FROM tweets GROUP BY month"

# Most common hashtags
python -m twitter_analyzer.cli query "SELECT text FROM tweets WHERE text LIKE '%#%' LIMIT 20"
```

## Database Schema

The DuckDB database contains the following tables:

### `user_profile`
- User profile information
- Follower/following counts
- Account metadata

### `tweets`
- All your tweets
- Engagement metrics (likes, retweets, replies)
- Tweet metadata (lang, created_at, etc.)

### `likes`
- Tweets you've liked
- Author information
- Like timestamps

### `bookmarks`
- Bookmarked tweets
- Author information
- Bookmark timestamps

### `following` / `followers`
- Users you follow
- Users who follow you
- (Note: These tables exist but require additional API calls to populate)

## Examples

### Analyze Your Writing Style

```bash
python -m twitter_analyzer.cli analyze tweets --analysis-type general
```

### Find Your Most Engaging Topics

```bash
python -m twitter_analyzer.cli query "SELECT text, like_count + retweet_count as engagement FROM tweets ORDER BY engagement DESC LIMIT 20"
```

### Understand What Content You Save

```bash
python -m twitter_analyzer.cli analyze bookmarks
```

### Ask About Your Twitter Habits

```bash
python -m twitter_analyzer.cli ask "What time of day do I tweet most?"
python -m twitter_analyzer.cli ask "Do I engage more with technical or personal content?"
```

## Architecture

```
twitter-data-analyzer/
├── src/twitter_analyzer/
│   ├── cli.py              # Command-line interface
│   ├── config.py           # Configuration management
│   ├── database.py         # DuckDB operations
│   ├── twitter_fetcher.py  # Twitter API integration
│   └── gemini_analyzer.py  # Gemini AI integration
├── pyproject.toml          # Package configuration (uv/pip)
├── requirements.txt        # Python dependencies (legacy)
├── setup.py               # Package setup (legacy)
├── .env.example           # Example configuration
└── README.md              # This file
```

## Troubleshooting

### Twitter API Rate Limits

Twitter API has rate limits. If you hit them:
- The tool will automatically stop and save what it has
- Wait 15 minutes and run fetch again
- Use `--limit` to fetch smaller batches

### Bookmarks Not Working

Bookmarks require OAuth 2.0 with specific scopes:
- Make sure you have a bearer token with bookmark.read scope
- Or use the OAuth 2.0 flow with proper permissions

### Gemini API Errors

- Check your API key is correct
- Ensure you have quota remaining
- Try using a smaller dataset (first 100 tweets/likes)

## Privacy & Data

- All data is stored locally in `twitter_data.duckdb`
- No data is sent anywhere except to Twitter (to fetch) and Gemini (to analyze)
- You control your data completely
- Delete `twitter_data.duckdb` to remove all stored data

## Advanced Usage

### Custom SQL Analysis

```bash
# Export tweets to JSON
python -c "import duckdb; duckdb.connect('twitter_data.duckdb').execute('COPY tweets TO \"tweets.json\"')"

# Connect with Python
python
>>> import duckdb
>>> conn = duckdb.connect('twitter_data.duckdb')
>>> conn.execute("SELECT * FROM tweets LIMIT 5").fetchdf()
```

### Integration with Other Tools

The DuckDB database can be opened with:
- DuckDB CLI
- Python (duckdb, pandas, polars)
- R (duckdb package)
- Any tool that supports DuckDB

## Contributing

This is part of the [claude-speriments](https://github.com/joncooper/claude-speriments) repository. Feel free to open issues or contribute improvements!

## License

MIT License - see repository for details

## Acknowledgments

- Built with [Tweepy](https://www.tweepy.org/) for Twitter API access
- Powered by [DuckDB](https://duckdb.org/) for fast local analytics
- Analysis by [Google Gemini](https://ai.google.dev/)
- CLI built with [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/)
- Package management with [uv](https://docs.astral.sh/uv/) - An extremely fast Python package installer

---

**Have fun exploring your Twitter data!** 🐦📊✨
