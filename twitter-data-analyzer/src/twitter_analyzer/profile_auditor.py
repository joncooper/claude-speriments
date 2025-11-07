"""Profile auditor for identifying potentially problematic content."""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
import json
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

import google.generativeai as genai


console = Console()


class Severity(Enum):
    """Severity levels for flagged content."""
    HIGH = "high"       # Definitely should remove
    MEDIUM = "medium"   # Probably should review
    LOW = "low"         # Minor concern
    CLEAN = "clean"     # No issues


class Category(Enum):
    """Categories of potentially problematic content."""
    POLITICAL = "political"                 # Political opinions/affiliations
    CONTROVERSIAL = "controversial"         # Religion, social issues, debates
    NSFW = "nsfw"                          # Adult content, sexual references
    PROFANITY = "profanity"                # Vulgar language
    PERSONAL = "personal"                  # Oversharing personal info
    UNPROFESSIONAL = "unprofessional"      # Unprofessional tone/content
    OFFENSIVE = "offensive"                # Potentially offensive jokes/content


@dataclass
class FlaggedItem:
    """An item that was flagged during audit."""
    item_type: str  # "tweet", "like", "bookmark"
    item_id: int
    text: str
    severity: Severity
    categories: List[Category]
    reason: str
    created_at: Optional[str] = None


class ProfileAuditor:
    """Audit Twitter profile for potentially problematic content."""

    def __init__(self, api_key: str, model_name: str = "gemini-1.5-flash"):
        """Initialize the auditor with Gemini API."""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def audit_tweets(
        self,
        tweets: List[Dict[str, Any]],
        batch_size: int = 20
    ) -> List[FlaggedItem]:
        """
        Audit tweets for problematic content.

        Args:
            tweets: List of tweet dicts from database
            batch_size: Number of tweets to analyze per API call

        Returns:
            List of flagged items
        """
        flagged = []

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task(
                f"Auditing {len(tweets)} tweets...",
                total=len(tweets)
            )

            # Process in batches to stay under rate limits
            for i in range(0, len(tweets), batch_size):
                batch = tweets[i:i + batch_size]
                batch_results = self._analyze_batch(batch, "tweet")
                flagged.extend(batch_results)
                progress.update(task, advance=len(batch))

        return flagged

    def audit_likes(
        self,
        likes: List[Dict[str, Any]],
        batch_size: int = 20
    ) -> List[FlaggedItem]:
        """
        Audit liked tweets for problematic content.

        Args:
            likes: List of like dicts from database
            batch_size: Number to analyze per API call

        Returns:
            List of flagged items
        """
        flagged = []

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task(
                f"Auditing {len(likes)} likes...",
                total=len(likes)
            )

            for i in range(0, len(likes), batch_size):
                batch = likes[i:i + batch_size]
                batch_results = self._analyze_batch(batch, "like")
                flagged.extend(batch_results)
                progress.update(task, advance=len(batch))

        return flagged

    def audit_bookmarks(
        self,
        bookmarks: List[Dict[str, Any]],
        batch_size: int = 20
    ) -> List[FlaggedItem]:
        """Audit bookmarked tweets for problematic content."""
        flagged = []

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task(
                f"Auditing {len(bookmarks)} bookmarks...",
                total=len(bookmarks)
            )

            for i in range(0, len(bookmarks), batch_size):
                batch = bookmarks[i:i + batch_size]
                batch_results = self._analyze_batch(batch, "bookmark")
                flagged.extend(batch_results)
                progress.update(task, advance=len(batch))

        return flagged

    def _analyze_batch(
        self,
        items: List[Dict[str, Any]],
        item_type: str
    ) -> List[FlaggedItem]:
        """
        Analyze a batch of items with Gemini.

        Args:
            items: List of items to analyze
            item_type: "tweet", "like", or "bookmark"

        Returns:
            List of flagged items from this batch
        """
        # Prepare batch for analysis
        if item_type == "tweet":
            texts = [(item.get('id'), item.get('text', '')) for item in items]
        else:  # like or bookmark
            texts = [(item.get('tweet_id'), item.get('tweet_text', '')) for item in items]

        # Build prompt
        prompt = self._build_audit_prompt(texts, item_type)

        try:
            # Call Gemini
            response = self.model.generate_content(prompt)

            # Parse response
            flagged = self._parse_audit_response(response.text, items, item_type)
            return flagged

        except Exception as e:
            console.print(f"[yellow]Warning: Batch analysis failed: {e}[/yellow]")
            return []

    def _build_audit_prompt(
        self,
        texts: List[tuple],
        item_type: str
    ) -> str:
        """Build the audit prompt for Gemini."""
        items_text = "\n".join([f"{id}: {text}" for id, text in texts])

        prompt = f"""You are auditing a Twitter profile to identify content that might be inappropriate for a professional/public profile (job hunting, etc.).

Analyze each {item_type} below and identify any that contain:
1. POLITICAL - Political opinions, endorsements, or partisan content
2. CONTROVERSIAL - Religion, divisive social issues, heated debates
3. NSFW - Adult/sexual content, suggestive material, or references
4. PROFANITY - Vulgar language, swearing
5. PERSONAL - Oversharing personal information
6. UNPROFESSIONAL - Unprofessional tone, rants, complaints
7. OFFENSIVE - Potentially offensive jokes, sarcasm that could be misunderstood

For each problematic {item_type}, respond with JSON in this format:
{{
  "id": <tweet_id>,
  "severity": "high|medium|low",
  "categories": ["category1", "category2"],
  "reason": "brief explanation"
}}

Only flag items that are genuinely concerning. Be practical - mild opinions are OK, but strong political statements or controversial topics should be flagged.

{item_type.capitalize()}s to analyze:
{items_text}

Respond with JSON array of flagged items only. If nothing is flagged, respond with empty array [].
"""
        return prompt

    def _parse_audit_response(
        self,
        response_text: str,
        items: List[Dict[str, Any]],
        item_type: str
    ) -> List[FlaggedItem]:
        """Parse Gemini's response into FlaggedItem objects."""
        flagged = []

        try:
            # Extract JSON from response (it might have markdown code blocks)
            json_text = response_text
            if "```json" in json_text:
                json_text = json_text.split("```json")[1].split("```")[0]
            elif "```" in json_text:
                json_text = json_text.split("```")[1].split("```")[0]

            results = json.loads(json_text.strip())

            for result in results:
                # Find the original item
                item_id = result.get('id')
                item = next((i for i in items if
                           i.get('id') == item_id or
                           i.get('tweet_id') == item_id), None)

                if not item:
                    continue

                # Get text
                if item_type == "tweet":
                    text = item.get('text', '')
                    created_at = item.get('created_at')
                else:
                    text = item.get('tweet_text', '')
                    created_at = item.get('tweet_created_at')

                # Parse severity
                severity_str = result.get('severity', 'medium').lower()
                severity = Severity[severity_str.upper()]

                # Parse categories
                categories = []
                for cat in result.get('categories', []):
                    try:
                        categories.append(Category[cat.upper()])
                    except KeyError:
                        pass

                # Create flagged item
                flagged_item = FlaggedItem(
                    item_type=item_type,
                    item_id=item_id,
                    text=text,
                    severity=severity,
                    categories=categories,
                    reason=result.get('reason', ''),
                    created_at=created_at
                )
                flagged.append(flagged_item)

        except json.JSONDecodeError as e:
            console.print(f"[yellow]Warning: Could not parse response: {e}[/yellow]")
        except Exception as e:
            console.print(f"[yellow]Warning: Error parsing results: {e}[/yellow]")

        return flagged

    def generate_report(self, flagged_items: List[FlaggedItem]) -> str:
        """Generate a human-readable audit report."""
        # Sort by severity
        high = [f for f in flagged_items if f.severity == Severity.HIGH]
        medium = [f for f in flagged_items if f.severity == Severity.MEDIUM]
        low = [f for f in flagged_items if f.severity == Severity.LOW]

        # Count by type
        tweets = [f for f in flagged_items if f.item_type == "tweet"]
        likes = [f for f in flagged_items if f.item_type == "like"]
        bookmarks = [f for f in flagged_items if f.item_type == "bookmark"]

        # Count by category
        category_counts = {}
        for item in flagged_items:
            for cat in item.categories:
                category_counts[cat.value] = category_counts.get(cat.value, 0) + 1

        report = f"""# Twitter Profile Audit Report

## Summary

**Total Items Flagged:** {len(flagged_items)}

### By Severity
- 🔴 **HIGH**: {len(high)} items (should definitely review/remove)
- 🟡 **MEDIUM**: {len(medium)} items (probably should review)
- 🟢 **LOW**: {len(low)} items (minor concerns)

### By Type
- Tweets: {len(tweets)}
- Likes: {len(likes)}
- Bookmarks: {len(bookmarks)}

### By Category
"""
        for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
            report += f"- {cat.title()}: {count}\n"

        # High priority items
        if high:
            report += f"\n## 🔴 HIGH PRIORITY ({len(high)} items)\n\n"
            for item in high[:20]:  # Show first 20
                cats = ", ".join([c.value for c in item.categories])
                report += f"### {item.item_type.title()} ID: {item.item_id}\n"
                report += f"**Categories:** {cats}\n"
                report += f"**Reason:** {item.reason}\n"
                report += f"**Text:** {item.text[:200]}{'...' if len(item.text) > 200 else ''}\n\n"

            if len(high) > 20:
                report += f"*... and {len(high) - 20} more high priority items*\n\n"

        # Medium priority items
        if medium:
            report += f"\n## 🟡 MEDIUM PRIORITY ({len(medium)} items)\n\n"
            for item in medium[:10]:  # Show first 10
                cats = ", ".join([c.value for c in item.categories])
                report += f"### {item.item_type.title()} ID: {item.item_id}\n"
                report += f"**Categories:** {cats}\n"
                report += f"**Reason:** {item.reason}\n"
                report += f"**Text:** {item.text[:150]}{'...' if len(item.text) > 150 else ''}\n\n"

            if len(medium) > 10:
                report += f"*... and {len(medium) - 10} more medium priority items*\n\n"

        # Recommendations
        report += """
## Recommendations

1. **Review all HIGH priority items** - These should likely be deleted
2. **Assess MEDIUM priority items** - Use your judgment
3. **Export the full list** - Use the CSV export for systematic review
4. **Use the TUI browser** - Search for specific topics to find more
5. **Consider bulk deletion** - You can delete tweets via Twitter API

## Next Steps

```bash
# Export to CSV for review
python -m twitter_analyzer.cli audit --export audit_results.csv

# Browse flagged content in TUI
python -m twitter_analyzer.cli browse
# Then search for specific terms

# Delete individual tweets (manual)
# Go to twitter.com and delete by ID

# Bulk delete (coming soon)
# python -m twitter_analyzer.cli delete --from-file audit_results.csv
```
"""

        return report
