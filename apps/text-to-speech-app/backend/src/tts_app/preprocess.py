"""Clean and preprocess text for TTS synthesis."""

import re


def preprocess(text: str) -> str:
    """Run the full preprocessing pipeline on extracted text."""
    text = _remove_bracketed_citations(text)
    text = _remove_parenthetical_citations(text)
    text = _remove_urls(text)
    text = _remove_figure_table_refs(text)
    text = _remove_page_numbers(text)
    text = _expand_abbreviations(text)
    text = _normalize_characters(text)
    text = _normalize_whitespace(text)
    return text.strip()


def _remove_bracketed_citations(text: str) -> str:
    """Remove [1], [1, 2], [1-5], [1, 3-7] style citations."""
    return re.sub(r"\[[\d,;\s\-–]+\]", "", text)


def _remove_parenthetical_citations(text: str) -> str:
    """Remove (Smith, 2020), (Smith & Jones, 2020; Doe, 2019) style citations."""
    return re.sub(
        r"\((?:[A-Z][a-z]+(?:\s(?:et\s+al\.|&\s+[A-Z][a-z]+))?(?:,\s*\d{4}[a-z]?)(?:;\s*)?)+\)",
        "",
        text,
    )


def _remove_urls(text: str) -> str:
    """Remove URLs and email addresses."""
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"\S+@\S+\.\S+", "", text)
    return text


def _remove_figure_table_refs(text: str) -> str:
    """Remove standalone figure/table references like 'See Figure 3.' or '(Table 2)'."""
    text = re.sub(
        r"(?:See\s+)?(?:Fig(?:ure)?|Table|Appendix)\s*\.?\s*\d+[a-z]?(?:\s*[-–]\s*\d+)?",
        "",
        text,
        flags=re.IGNORECASE,
    )
    return text


def _remove_page_numbers(text: str) -> str:
    """Remove standalone page numbers (lines that are just a number)."""
    return re.sub(r"^\s*\d{1,4}\s*$", "", text, flags=re.MULTILINE)


def _expand_abbreviations(text: str) -> str:
    """Expand common abbreviations for better TTS pronunciation."""
    replacements = {
        r"\bet\s+al\.": "and others",
        r"\bFig\.": "Figure",
        r"\bfig\.": "figure",
        r"\bEq\.": "Equation",
        r"\beq\.": "equation",
        r"\bDr\.": "Doctor",
        r"\bvs\.": "versus",
        r"\bi\.e\.": "that is",
        r"\be\.g\.": "for example",
        r"\betc\.(?!\w)": "etcetera",
        r"\bw\.r\.t\.": "with respect to",
        r"\bapprox\.": "approximately",
    }
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text)
    return text


def _normalize_characters(text: str) -> str:
    """Normalize special characters for TTS."""
    text = text.replace("—", ", ")
    text = text.replace("–", " to ")
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2026", "...")
    text = text.replace("\xad", "")  # soft hyphen
    return text


def _normalize_whitespace(text: str) -> str:
    """Collapse multiple whitespace and blank lines."""
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text
