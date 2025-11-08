"""
Outcome Tracker

AI-powered verification of whether management commitments were fulfilled.
Uses Anthropic's Claude to analyze subsequent filings and determine outcomes.
"""

import os
from typing import Dict, List, Optional
from anthropic import Anthropic
import json
from datetime import datetime
from dateutil import parser as date_parser
from dateutil.relativedelta import relativedelta


class OutcomeTracker:
    """
    Verifies whether management commitments were fulfilled.

    Analyzes subsequent filings to determine if promised targets were met,
    partially met, missed, abandoned, or are still pending.
    """

    OUTCOME_STATUSES = [
        "fulfilled",          # Target met or exceeded
        "partially_fulfilled", # Progress made but target missed
        "not_fulfilled",      # Little to no progress
        "abandoned",          # Explicitly discontinued
        "pending",            # Timeline not yet reached
        "unverifiable",       # Insufficient information
    ]

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the outcome tracker.

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

    def verify_commitment(
        self,
        commitment: Dict,
        verification_text: str,
        verification_metadata: Dict
    ) -> Dict:
        """
        Verify whether a commitment was fulfilled by analyzing subsequent filing text.

        Args:
            commitment: Commitment dictionary from CommitmentExtractor
            verification_text: Text from subsequent filing to verify against
            verification_metadata: Metadata about verification filing:
                - filing_type: '10-K' or '10-Q'
                - filing_date: Date of filing
                - period_date: Period end date

        Returns:
            Outcome dictionary with structure:
            {
                'commitment_id': str,
                'status': str,  # One of OUTCOME_STATUSES
                'explanation': str,  # Why this status was assigned
                'actual_value': Optional[float],  # Actual result if quantifiable
                'actual_unit': Optional[str],  # Unit of actual value
                'variance': Optional[float],  # % variance from target
                'evidence': str,  # Quote from verification filing
                'confidence': float,  # AI confidence (0.0-1.0)
                'verification_filing': dict,  # Verification filing metadata
            }
        """
        # Truncate verification text if too long
        truncated_text = verification_text[:50000] if len(verification_text) > 50000 else verification_text

        system_prompt = self._build_verification_prompt()
        user_message = self._build_verification_message(
            commitment,
            truncated_text,
            verification_metadata
        )

        # Call Claude API
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2048,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )

            # Parse response
            response_text = response.content[0].text

            # Extract JSON from response
            outcome = self._parse_outcome(response_text, commitment, verification_metadata)

            return outcome

        except Exception as e:
            print(f"Error verifying commitment {commitment['commitment_id']}: {e}")
            return {
                'commitment_id': commitment['commitment_id'],
                'status': 'unverifiable',
                'explanation': f'Error during verification: {str(e)}',
                'confidence': 0.0,
                'verification_filing': verification_metadata,
            }

    def get_verification_window(self, commitment: Dict) -> tuple[str, str]:
        """
        Determine the appropriate time window to verify a commitment.

        Args:
            commitment: Commitment dictionary with 'timeline' field

        Returns:
            Tuple of (start_date, end_date) in 'YYYY-MM-DD' format
        """
        # Parse the source filing date
        source_date = date_parser.parse(commitment['source_filing']['filing_date'])

        # Parse timeline to determine verification window
        timeline = commitment['timeline'].lower()

        # Common patterns
        if 'q1' in timeline or 'first quarter' in timeline:
            months_ahead = 3
        elif 'q2' in timeline or 'second quarter' in timeline:
            months_ahead = 6
        elif 'q3' in timeline or 'third quarter' in timeline:
            months_ahead = 9
        elif 'q4' in timeline or 'fourth quarter' in timeline or 'year end' in timeline:
            months_ahead = 12
        elif 'fy' in timeline or 'fiscal year' in timeline or 'fiscal' in timeline:
            # Extract year if present
            import re
            year_match = re.search(r'20\d{2}', timeline)
            if year_match:
                target_year = int(year_match.group())
                current_year = source_date.year
                months_ahead = (target_year - current_year) * 12
            else:
                months_ahead = 12
        else:
            # Default to 1 year ahead
            months_ahead = 12

        # Verification window: from commitment date to timeline + 3 months buffer
        start_date = source_date.strftime('%Y-%m-%d')
        end_date = (source_date + relativedelta(months=months_ahead + 3)).strftime('%Y-%m-%d')

        return start_date, end_date

    def find_verification_filing(
        self,
        commitment: Dict,
        filings: List[Dict]
    ) -> Optional[Dict]:
        """
        Find the best filing to verify a commitment.

        Looks for the first filing after the commitment's timeline target.

        Args:
            commitment: Commitment dictionary
            filings: List of subsequent filing dictionaries

        Returns:
            Best filing for verification, or None if no suitable filing found
        """
        # Get verification window
        start_date, end_date = self.get_verification_window(commitment)

        start_dt = date_parser.parse(start_date)
        end_dt = date_parser.parse(end_date)

        # Find filings within window
        candidates = []
        for filing in filings:
            filing_date = filing.get('filing_date') or filing.get('period_date')
            if not filing_date:
                continue

            filing_dt = date_parser.parse(filing_date)

            # Check if after commitment but before end of window
            if filing_dt > start_dt and filing_dt <= end_dt:
                candidates.append(filing)

        if not candidates:
            return None

        # Prefer 10-K over 10-Q (more comprehensive)
        annual_filings = [f for f in candidates if f.get('filing_type') == '10-K']
        if annual_filings:
            # Return first 10-K after target date
            return annual_filings[0]

        # Otherwise return first quarterly filing
        return candidates[0]

    def _build_verification_prompt(self) -> str:
        """Build the system prompt for outcome verification."""
        return """You are an expert equity research analyst verifying whether management followed through on commitments.

Your task is to analyze subsequent SEC filings to determine if a specific commitment was fulfilled.

# Outcome Statuses

Classify the outcome as one of:

1. **fulfilled**: Target was met or exceeded
   - Example: Promised 30% margins, achieved 31%
   - Example: Committed to $90B buybacks, returned $95B

2. **partially_fulfilled**: Progress made but target missed
   - Example: Promised 30% margins, achieved 27%
   - Example: Committed to 50 stores, opened 35

3. **not_fulfilled**: Little to no progress toward target
   - Example: Promised margin improvement, margins declined
   - Example: Committed to expansion, no stores opened

4. **abandoned**: Initiative explicitly discontinued or abandoned
   - Example: "We have decided not to pursue this initiative"
   - Example: "Project has been discontinued"

5. **pending**: Timeline not yet reached, insufficient time has passed
   - Only use if verification filing is before target date

6. **unverifiable**: Cannot determine outcome from available information
   - No mention of the commitment topic in verification filing
   - Insufficient data to assess

# Key Principles

- Be objective and evidence-based
- Look for SPECIFIC data points (numbers, dates, facts)
- Consider both explicit statements and implicit evidence (financial data)
- Distinguish between "partially fulfilled" (made progress) vs "not fulfilled" (no progress)
- Only mark as "fulfilled" if target was clearly met or exceeded
- Extract the actual value achieved if quantifiable

# Output Format

Return JSON:

```json
{
  "status": "fulfilled",
  "explanation": "Clear explanation of why this status was assigned",
  "actual_value": 31.0,
  "actual_unit": "percent",
  "variance": 3.3,
  "evidence": "Exact quote from filing supporting the determination",
  "confidence": 0.95
}
```

For non-quantifiable commitments, omit actual_value, actual_unit, and variance.

Be rigorous. Management credibility analysis requires objective assessment."""

    def _build_verification_message(
        self,
        commitment: Dict,
        verification_text: str,
        verification_metadata: Dict
    ) -> str:
        """Build the user message for verification."""
        # Format the commitment clearly
        commitment_summary = f"""
**Original Commitment:**
- Text: "{commitment['commitment_text']}"
- Category: {commitment['category']}
- Metric: {commitment['metric']}
- Target: {commitment.get('target', 'N/A')} {commitment.get('target_unit', '')}
- Timeline: {commitment['timeline']}
- Made in: {commitment['source_filing']['filing_type']} filed {commitment['source_filing']['filing_date']}
"""

        return f"""Verify whether this management commitment was fulfilled:

{commitment_summary}

**Verification Filing:**
- Type: {verification_metadata.get('filing_type', 'Unknown')}
- Date: {verification_metadata.get('filing_date', 'Unknown')}
- Period: {verification_metadata.get('period_date', 'Unknown')}

**Filing Text:**

{verification_text}

---

Analyze the filing text above and determine whether the commitment was fulfilled.
Return as JSON with status, explanation, evidence, and confidence."""

    def _parse_outcome(
        self,
        response_text: str,
        commitment: Dict,
        verification_metadata: Dict
    ) -> Dict:
        """
        Parse outcome JSON from Claude's response.

        Args:
            response_text: Raw response from Claude
            commitment: Original commitment
            verification_metadata: Verification filing metadata

        Returns:
            Outcome dictionary
        """
        # Try to find JSON in the response
        json_match = response_text
        if "```json" in response_text:
            start = response_text.find("```json") + 7
            end = response_text.find("```", start)
            json_match = response_text[start:end].strip()
        elif "```" in response_text:
            start = response_text.find("```") + 3
            end = response_text.find("```", start)
            json_match = response_text[start:end].strip()

        try:
            outcome = json.loads(json_match)
        except json.JSONDecodeError:
            print("Warning: Could not parse outcome JSON")
            outcome = {
                'status': 'unverifiable',
                'explanation': 'Failed to parse AI response',
                'confidence': 0.0
            }

        # Add commitment ID and verification metadata
        outcome['commitment_id'] = commitment['commitment_id']
        outcome['verification_filing'] = verification_metadata

        # Calculate variance if both target and actual are present
        if 'actual_value' in outcome and commitment.get('target'):
            target = commitment['target']
            actual = outcome['actual_value']
            if target > 0:
                variance = ((actual - target) / target) * 100
                outcome['variance'] = round(variance, 2)

        return outcome
