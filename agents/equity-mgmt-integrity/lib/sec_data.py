"""
SEC Data Helper Functions

This module provides utilities for loading and manipulating SEC filing data
that has been fetched via MCP tools. It does NOT fetch data directly -
data fetching should be done through MCP servers.

These are pure data manipulation functions with no API calls.
"""

import json
import os
from typing import Dict, List, Optional
from bs4 import BeautifulSoup
import re
from datetime import datetime


def load_sec_data(ticker: str, data_dir: str = "agents/equity-mgmt-integrity/data") -> Dict:
    """
    Load MCP-fetched SEC data from the data directory.

    Args:
        ticker: Stock ticker symbol (e.g., 'AAPL')
        data_dir: Directory where data files are stored

    Returns:
        Dictionary containing company info and filings data

    Raises:
        FileNotFoundError: If the data file doesn't exist
        json.JSONDecodeError: If the file is not valid JSON
    """
    filepath = os.path.join(data_dir, f"{ticker}_sec_data.json")

    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"SEC data file not found: {filepath}\n"
            f"Run the /mgmt-integrity command first to fetch data via MCP."
        )

    with open(filepath, 'r') as f:
        data = json.load(f)

    return data


def extract_filing_sections(html_content: str, sections: List[str]) -> Dict[str, str]:
    """
    Parse sections from SEC HTML filing content.

    Common sections to extract:
    - "Item 1" - Business description
    - "Item 7" - MD&A (Management Discussion and Analysis)
    - "Item 1A" - Risk Factors

    Args:
        html_content: Raw HTML content from SEC filing
        sections: List of section names to extract (e.g., ["Item 7", "Item 1"])

    Returns:
        Dictionary mapping section names to extracted text content
    """
    if not html_content:
        return {section: "" for section in sections}

    soup = BeautifulSoup(html_content, 'html.parser')
    extracted = {}

    for section in sections:
        # Try to find the section header
        section_text = ""

        # Common patterns for section headers in SEC filings
        patterns = [
            rf"<b>\s*{re.escape(section)}\s*[.:]\s*</b>",
            rf"<b>\s*{re.escape(section)}\s*</b>",
            rf"{re.escape(section)}\s*[.:]\s*",
        ]

        # Search for section start
        for pattern in patterns:
            matches = list(re.finditer(pattern, str(soup), re.IGNORECASE))
            if matches:
                # Found the section, try to extract until next section
                start = matches[0].end()

                # Try to find the end (next major section)
                next_section_pattern = r"<b>\s*Item\s+\d+[A-Za-z]?\s*[.:]\s*</b>"
                next_matches = list(re.finditer(next_section_pattern, str(soup)[start:], re.IGNORECASE))

                if next_matches:
                    end = start + next_matches[0].start()
                    section_html = str(soup)[start:end]
                else:
                    # Take a reasonable amount of content (100KB)
                    section_html = str(soup)[start:start+100000]

                # Parse the HTML and extract text
                section_soup = BeautifulSoup(section_html, 'html.parser')
                section_text = section_soup.get_text(separator='\n', strip=True)
                break

        extracted[section] = section_text if section_text else ""

    return extracted


def format_currency(value: float) -> str:
    """
    Format a number as currency in billions, millions, or dollars.

    Args:
        value: Numeric value to format

    Returns:
        Formatted string (e.g., "$394.3B", "$1.2M", "$500")
    """
    if abs(value) >= 1e9:
        return f"${value/1e9:,.1f}B"
    elif abs(value) >= 1e6:
        return f"${value/1e6:,.1f}M"
    elif abs(value) >= 1e3:
        return f"${value/1e3:,.1f}K"
    else:
        return f"${value:,.0f}"


def calculate_percentage_change(old: float, new: float) -> float:
    """
    Calculate percentage change between two values.

    Args:
        old: Previous value
        new: Current value

    Returns:
        Percentage change (e.g., 15.5 for a 15.5% increase)
    """
    if old == 0:
        return 0.0 if new == 0 else float('inf')

    return ((new - old) / abs(old)) * 100


def parse_filing_date(date_str: str) -> datetime:
    """
    Parse various SEC filing date formats into datetime objects.

    Args:
        date_str: Date string from SEC filing (e.g., "2023-11-01", "2023-11-01T00:00:00")

    Returns:
        datetime object
    """
    # Try common formats
    formats = [
        "%Y-%m-%d",
        "%Y-%m-%dT%H:%M:%S",
        "%Y%m%d",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_str[:len(fmt.replace('%', ''))], fmt)
        except ValueError:
            continue

    raise ValueError(f"Could not parse date: {date_str}")


def filter_filings_by_date_range(
    filings: List[Dict],
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
) -> List[Dict]:
    """
    Filter filings to a specific date range.

    Args:
        filings: List of filing dictionaries with 'filing_date' or 'period_date' keys
        start_date: Start date (inclusive) in 'YYYY-MM-DD' format
        end_date: End date (inclusive) in 'YYYY-MM-DD' format

    Returns:
        Filtered list of filings
    """
    filtered = []

    start_dt = parse_filing_date(start_date) if start_date else None
    end_dt = parse_filing_date(end_date) if end_date else None

    for filing in filings:
        # Try to get date from filing
        date_str = filing.get('filing_date') or filing.get('period_date')
        if not date_str:
            continue

        filing_dt = parse_filing_date(date_str)

        # Check if within range
        if start_dt and filing_dt < start_dt:
            continue
        if end_dt and filing_dt > end_dt:
            continue

        filtered.append(filing)

    return filtered


def get_filing_text_content(filing: Dict) -> str:
    """
    Extract all relevant text content from a filing dictionary.

    Combines MD&A, business description, and other sections into a single text.

    Args:
        filing: Filing dictionary with text content fields

    Returns:
        Combined text content
    """
    sections = []

    # Common text fields in filing data
    text_fields = ['md_a_text', 'business_text', 'risk_factors_text', 'full_text']

    for field in text_fields:
        if field in filing and filing[field]:
            sections.append(filing[field])

    return "\n\n".join(sections)


def save_json(data: Dict, filepath: str) -> None:
    """
    Save data to a JSON file with proper formatting.

    Args:
        data: Data to save
        filepath: Path to save the file
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, default=str)


def load_json(filepath: str) -> Dict:
    """
    Load data from a JSON file.

    Args:
        filepath: Path to the JSON file

    Returns:
        Loaded data

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    with open(filepath, 'r') as f:
        return json.load(f)
