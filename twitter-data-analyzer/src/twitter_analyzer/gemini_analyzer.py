"""Gemini AI integration for analyzing Twitter data."""

import google.generativeai as genai
from typing import List, Dict, Any, Optional
from rich.console import Console
from rich.markdown import Markdown


console = Console()


class GeminiAnalyzer:
    """Analyze Twitter data using Google Gemini."""

    def __init__(self, api_key: str, model_name: str = "gemini-1.5-flash"):
        """
        Initialize Gemini client.

        Args:
            api_key: Google Gemini API key
            model_name: Model to use (default: gemini-1.5-flash)
        """
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def analyze_tweets(
        self,
        tweets: List[Dict[str, Any]],
        analysis_type: str = "general"
    ) -> str:
        """
        Analyze a collection of tweets.

        Args:
            tweets: List of tweet dictionaries
            analysis_type: Type of analysis (general, sentiment, topics, patterns)
        """
        # Prepare tweet text
        tweet_texts = [f"- {t.get('text', '')}" for t in tweets[:100]]  # Limit for token size
        tweets_str = "\n".join(tweet_texts)

        prompts = {
            "general": f"""Analyze these tweets and provide insights about:
1. Main topics and themes
2. Overall tone and sentiment
3. Key interests and patterns
4. Writing style and characteristics

Tweets:
{tweets_str}

Provide a concise analysis in markdown format.""",

            "sentiment": f"""Analyze the sentiment of these tweets:
- Overall sentiment distribution (positive, negative, neutral)
- Emotional patterns
- Topics that generate different sentiments

Tweets:
{tweets_str}

Provide a sentiment analysis in markdown format.""",

            "topics": f"""Identify and categorize the main topics in these tweets:
- List top 10 topics/themes
- Frequency of each topic
- How topics relate to each other
- Any emerging interests or trends

Tweets:
{tweets_str}

Provide a topic analysis in markdown format.""",

            "patterns": f"""Identify patterns in these tweets:
- Posting patterns and habits
- Common phrases or words
- Types of content (original, replies, quotes)
- Engagement patterns

Tweets:
{tweets_str}

Provide a pattern analysis in markdown format.""",
        }

        prompt = prompts.get(analysis_type, prompts["general"])

        console.print("[cyan]Analyzing with Gemini...[/cyan]")
        response = self.model.generate_content(prompt)
        return response.text

    def analyze_likes(self, likes: List[Dict[str, Any]]) -> str:
        """Analyze liked tweets to understand interests."""
        like_texts = [f"- {t.get('tweet_text', '')}" for t in likes[:100]]
        likes_str = "\n".join(like_texts)

        prompt = f"""Analyze these liked tweets to understand the user's interests:
1. Main topics they're interested in
2. Types of content they engage with
3. Communities or themes they follow
4. Patterns in what they find valuable

Liked tweets:
{likes_str}

Provide insights in markdown format."""

        console.print("[cyan]Analyzing likes with Gemini...[/cyan]")
        response = self.model.generate_content(prompt)
        return response.text

    def analyze_bookmarks(self, bookmarks: List[Dict[str, Any]]) -> str:
        """Analyze bookmarked tweets."""
        bookmark_texts = [f"- {t.get('tweet_text', '')}" for t in bookmarks[:100]]
        bookmarks_str = "\n".join(bookmark_texts)

        prompt = f"""Analyze these bookmarked tweets:
1. Why might these be saved/bookmarked?
2. Common themes or categories
3. Types of information being collected
4. Learning interests or goals

Bookmarked tweets:
{bookmarks_str}

Provide insights in markdown format."""

        console.print("[cyan]Analyzing bookmarks with Gemini...[/cyan]")
        response = self.model.generate_content(prompt)
        return response.text

    def custom_analysis(self, data: str, question: str) -> str:
        """
        Run a custom analysis with a user-provided question.

        Args:
            data: Context data (tweets, likes, etc.)
            question: User's question about the data
        """
        prompt = f"""Based on this Twitter data:

{data}

Question: {question}

Provide a detailed answer in markdown format."""

        console.print("[cyan]Analyzing with Gemini...[/cyan]")
        response = self.model.generate_content(prompt)
        return response.text

    def generate_summary(
        self,
        stats: Dict[str, int],
        tweet_sample: Optional[List[Dict]] = None,
        like_sample: Optional[List[Dict]] = None
    ) -> str:
        """Generate a comprehensive summary of Twitter activity."""
        prompt = f"""Generate a comprehensive summary of this Twitter account:

Statistics:
- Total tweets: {stats.get('total_tweets', 0)}
- Total likes: {stats.get('total_likes', 0)}
- Total bookmarks: {stats.get('total_bookmarks', 0)}
- Total following: {stats.get('total_following', 0)}
- Total followers: {stats.get('total_followers', 0)}
"""

        if tweet_sample:
            tweet_texts = [f"- {t.get('text', '')}" for t in tweet_sample[:20]]
            prompt += f"\n\nRecent tweets:\n" + "\n".join(tweet_texts)

        if like_sample:
            like_texts = [f"- {t.get('tweet_text', '')}" for t in like_sample[:20]]
            prompt += f"\n\nRecent likes:\n" + "\n".join(like_texts)

        prompt += """

Provide:
1. Account activity overview
2. Content themes and interests
3. Engagement patterns
4. Key characteristics

Format the response in markdown."""

        console.print("[cyan]Generating summary with Gemini...[/cyan]")
        response = self.model.generate_content(prompt)
        return response.text
