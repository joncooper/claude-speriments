"""
Commitment Extractor

AI-powered extraction of forward-looking commitments from SEC filings.
Uses Anthropic's Claude to identify specific, verifiable management commitments.
"""

import os
import json
import hashlib
from typing import Dict, List, Optional
from anthropic import Anthropic


class CommitmentExtractor:
    """
    Extracts forward-looking management commitments from SEC filing text.

    Uses Claude to identify specific, verifiable statements about future
    actions, targets, or initiatives that management has committed to.
    """

    COMMITMENT_CATEGORIES = [
        "financial_target",      # Revenue, margins, EPS goals
        "capital_allocation",    # CapEx, buybacks, dividends
        "strategic_initiative",  # M&A, market expansion, partnerships
        "operational_improvement",  # Efficiency, cost reduction
        "product_launch",        # New products, services, features
    ]

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the commitment extractor.

        Args:
            api_key: Anthropic API key (defaults to ANTHROPIC_API_KEY env var)

        Raises:
            ValueError: If API key is not provided or found in environment
        """
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Anthropic API key required. Set ANTHROPIC_API_KEY environment variable "
                "or pass api_key parameter."
            )

        self.client = Anthropic(api_key=self.api_key)
        self.model = "claude-sonnet-4-5-20250929"

    def extract_from_text(
        self,
        text: str,
        filing_metadata: Dict
    ) -> List[Dict]:
        """
        Extract commitments from filing text using AI.

        Args:
            text: Text content from SEC filing (MD&A, Business sections)
            filing_metadata: Metadata about the filing including:
                - ticker: Stock ticker
                - company: Company name
                - filing_type: '10-K' or '10-Q'
                - filing_date: Date of filing
                - period_date: Period end date

        Returns:
            List of commitment dictionaries with structure:
            {
                'commitment_id': str,
                'commitment_text': str,  # Exact quote
                'category': str,  # One of COMMITMENT_CATEGORIES
                'metric': str,  # What's being committed to
                'target': Optional[float],  # Quantitative value if specified
                'target_unit': Optional[str],  # Unit (percent, billion_usd, etc.)
                'timeline': str,  # When should it be fulfilled
                'specificity': int,  # 1-10 scale
                'verifiable': bool,  # Can it be objectively verified
                'confidence': float,  # AI confidence (0.0-1.0)
                'source_filing': dict,  # Filing metadata
            }
        """
        # Truncate text if too long (keep first 50k chars)
        truncated_text = text[:50000] if len(text) > 50000 else text

        system_prompt = self._build_extraction_prompt()
        user_message = self._build_user_message(truncated_text, filing_metadata)

        # Call Claude API
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )

            # Parse response
            response_text = response.content[0].text

            # Extract JSON from response
            commitments = self._parse_commitments(response_text, filing_metadata)

            # Filter by quality
            filtered_commitments = [
                c for c in commitments
                if c['verifiable'] and c['specificity'] >= 4
            ]

            return filtered_commitments

        except Exception as e:
            print(f"Error extracting commitments: {e}")
            return []

    def _build_extraction_prompt(self) -> str:
        """Build the system prompt for commitment extraction."""
        return """You are an expert equity research analyst specializing in analyzing management credibility.

Your task is to extract SPECIFIC, VERIFIABLE forward-looking commitments from SEC filing text.

# What Qualifies as a Commitment

A commitment must be:
1. **Forward-looking**: About future actions, not past achievements
2. **Specific**: Clear and concrete, not vague aspirations
3. **Verifiable**: Can be objectively checked in future filings
4. **Management-driven**: Within management's control to deliver

# Good Examples

✅ "We expect to achieve operating margins of 30% by fiscal 2025"
✅ "Plan to return $90 billion to shareholders via buybacks in FY24"
✅ "Will open 50 new stores in Asia by end of 2024"
✅ "Targeting cost savings of $500M from restructuring by Q4"
✅ "Launch of Model Y in Europe scheduled for March 2024"

# Bad Examples (Do NOT Extract)

❌ "We remain committed to innovation" (too vague)
❌ "Continue to focus on customer satisfaction" (not verifiable)
❌ "Hope to see improved results" (not a commitment)
❌ "Revenue was $10B last quarter" (past, not forward-looking)
❌ "Market conditions may improve" (not within management control)

# Categories

Classify each commitment:
- **financial_target**: Revenue, margins, EPS goals, profitability targets
- **capital_allocation**: CapEx plans, buybacks, dividends, M&A spending
- **strategic_initiative**: Market expansion, partnerships, acquisitions
- **operational_improvement**: Cost reduction, efficiency gains, restructuring
- **product_launch**: New products, services, features with timeline

# Specificity Scale (1-10)

- **1-3**: Vague aspirations ("improve", "focus on", "committed to")
- **4-6**: General direction with some details ("grow revenue", "expand internationally")
- **7-8**: Concrete targets ("30% margins", "$90B buybacks")
- **9-10**: Highly specific with exact numbers and dates ("50 stores by Dec 31, 2024")

Only extract commitments with specificity >= 4.

# Output Format

Return a JSON array of commitments:

```json
[
  {
    "commitment_text": "exact quote from filing",
    "category": "financial_target",
    "metric": "operating margin",
    "target": 30.0,
    "target_unit": "percent",
    "timeline": "fiscal 2025",
    "specificity": 8,
    "verifiable": true,
    "confidence": 0.95
  }
]
```

If no valid commitments found, return empty array: []

Be selective. Only extract high-quality, verifiable commitments."""

    def _build_user_message(self, text: str, filing_metadata: Dict) -> str:
        """Build the user message with filing text."""
        return f"""Extract forward-looking management commitments from this SEC filing:

**Company:** {filing_metadata.get('company', 'Unknown')} ({filing_metadata.get('ticker', 'N/A')})
**Filing:** {filing_metadata.get('filing_type', 'Unknown')} filed {filing_metadata.get('filing_date', 'Unknown')}
**Period:** {filing_metadata.get('period_date', 'Unknown')}

**Filing Text:**

{text}

---

Extract all specific, verifiable forward-looking commitments from the text above.
Return as JSON array."""

    def _parse_commitments(
        self,
        response_text: str,
        filing_metadata: Dict
    ) -> List[Dict]:
        """
        Parse commitment JSON from Claude's response.

        Args:
            response_text: Raw response from Claude
            filing_metadata: Filing metadata to add to each commitment

        Returns:
            List of commitment dictionaries
        """
        # Try to find JSON in the response
        json_match = response_text
        if "```json" in response_text:
            # Extract JSON from code block
            start = response_text.find("```json") + 7
            end = response_text.find("```", start)
            json_match = response_text[start:end].strip()
        elif "```" in response_text:
            # Extract from generic code block
            start = response_text.find("```") + 3
            end = response_text.find("```", start)
            json_match = response_text[start:end].strip()

        try:
            commitments = json.loads(json_match)
        except json.JSONDecodeError:
            print("Warning: Could not parse commitment JSON")
            return []

        # Add metadata and generate IDs
        for commitment in commitments:
            # Generate unique ID from content
            commitment_id = self._generate_commitment_id(
                commitment['commitment_text'],
                filing_metadata['filing_date']
            )
            commitment['commitment_id'] = commitment_id

            # Add source filing info
            commitment['source_filing'] = {
                'ticker': filing_metadata.get('ticker'),
                'company': filing_metadata.get('company'),
                'filing_type': filing_metadata.get('filing_type'),
                'filing_date': filing_metadata.get('filing_date'),
                'period_date': filing_metadata.get('period_date'),
            }

        return commitments

    def _generate_commitment_id(self, text: str, filing_date: str) -> str:
        """
        Generate a unique ID for a commitment.

        Args:
            text: Commitment text
            filing_date: Date of filing

        Returns:
            Unique commitment ID
        """
        # Use hash of text + date for uniqueness
        content = f"{text}_{filing_date}"
        hash_obj = hashlib.sha256(content.encode())
        return f"COMM_{hash_obj.hexdigest()[:16]}"
