# Quick Start Guide

Get up and running with Twitter Data Analyzer in 5 minutes!

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

## Step 1: Install

```bash
cd twitter-data-analyzer
pip install -r requirements.txt
```

## Step 2: Get API Keys

### Twitter API (choose one method):

**Option A: Bearer Token (Easier)**
1. Go to https://developer.twitter.com/en/portal/dashboard
2. Create a project and app
3. Go to "Keys and tokens"
4. Generate/copy your "Bearer Token"

**Option B: OAuth 1.0a (More features)**
1. Go to https://developer.twitter.com/en/portal/dashboard
2. Create a project and app
3. Go to "Keys and tokens"
4. Copy: API Key, API Key Secret, Access Token, Access Token Secret

### Gemini API:
1. Go to https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key

## Step 3: Configure

```bash
# Create config file
python -m twitter_analyzer.cli init

# Edit .env file with your API keys
nano .env  # or use your preferred editor
```

Example `.env`:
```bash
# Use Bearer Token (easier)
TWITTER_BEARER_TOKEN=AAAAAAAAAAAAAAAAAAAAAFooBar...

# OR use OAuth 1.0a
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_SECRET=your_access_secret

# Gemini API
GEMINI_API_KEY=AIzaSyFooBar...
```

## Step 4: Fetch Your Data

```bash
# Fetch everything (tweets, likes, bookmarks)
python -m twitter_analyzer.cli fetch

# Or fetch just tweets
python -m twitter_analyzer.cli fetch --no-likes --no-bookmarks

# Fetch with a limit (useful for testing)
python -m twitter_analyzer.cli fetch --limit 50
```

This will:
- Authenticate with Twitter
- Download your tweets, likes, and bookmarks
- Save everything to `twitter_data.duckdb`

## Step 5: Analyze!

```bash
# Get a summary
python -m twitter_analyzer.cli analyze summary

# Analyze your tweets
python -m twitter_analyzer.cli analyze tweets

# Analyze what you like
python -m twitter_analyzer.cli analyze likes

# Ask custom questions
python -m twitter_analyzer.cli ask "What are my main interests?"
python -m twitter_analyzer.cli ask "What topics do I tweet about most?"

# Run SQL queries
python -m twitter_analyzer.cli query "SELECT text, like_count FROM tweets ORDER BY like_count DESC LIMIT 10"
```

## Common Commands

### Check Status
```bash
python -m twitter_analyzer.cli status
```

### Different Analysis Types
```bash
# Sentiment analysis
python -m twitter_analyzer.cli analyze tweets --analysis-type sentiment

# Topic analysis
python -m twitter_analyzer.cli analyze tweets --analysis-type topics

# Pattern analysis
python -m twitter_analyzer.cli analyze tweets --analysis-type patterns
```

### SQL Queries Examples
```bash
# Most liked tweets
python -m twitter_analyzer.cli query "SELECT text, like_count FROM tweets ORDER BY like_count DESC LIMIT 10"

# Tweet count by month
python -m twitter_analyzer.cli query "SELECT DATE_TRUNC('month', created_at) as month, COUNT(*) as count FROM tweets GROUP BY month ORDER BY month"

# Recent tweets
python -m twitter_analyzer.cli query "SELECT text, created_at FROM tweets ORDER BY created_at DESC LIMIT 20"
```

## Troubleshooting

### "Twitter API credentials not configured"
- Make sure you've created a `.env` file (run `python -m twitter_analyzer.cli init`)
- Check that your API keys are correct in `.env`
- Try running `python -m twitter_analyzer.cli status` to check config

### "Rate limit hit"
- Twitter has rate limits on API calls
- The tool saves what it fetched so far
- Wait 15 minutes and run fetch again

### Bookmarks not working
- Bookmarks require OAuth 2.0 with specific scopes
- Use a Bearer Token with bookmark.read scope
- Or skip bookmarks: `python -m twitter_analyzer.cli fetch --no-bookmarks`

### Import errors
- Make sure you installed dependencies: `pip install -r requirements.txt`
- Try: `pip install --upgrade -r requirements.txt`

## What's Next?

- Read the full [README.md](README.md) for more details
- Check [NOTES.md](NOTES.md) for implementation details
- Explore your data with custom SQL queries
- Ask Gemini interesting questions about your Twitter patterns!

## Example Workflow

```bash
# 1. Install and configure
pip install -r requirements.txt
python -m twitter_analyzer.cli init
# Edit .env with your API keys

# 2. Check everything is configured
python -m twitter_analyzer.cli status

# 3. Fetch your data
python -m twitter_analyzer.cli fetch --limit 100

# 4. Get insights
python -m twitter_analyzer.cli analyze summary
python -m twitter_analyzer.cli ask "What are my main interests based on likes?"

# 5. Explore with SQL
python -m twitter_analyzer.cli query "SELECT COUNT(*) FROM tweets"
python -m twitter_analyzer.cli query "SELECT text FROM tweets LIMIT 5"
```

Enjoy exploring your Twitter data! 🐦📊
