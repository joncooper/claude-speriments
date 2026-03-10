"""Extract text from URLs, PDFs, and raw text input."""

import io
import re

import trafilatura
import fitz  # pymupdf


def extract_from_url(url: str) -> str:
    """Fetch a URL and extract the main article text."""
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        raise ValueError(f"Could not fetch URL: {url}")

    text = trafilatura.extract(
        downloaded,
        include_comments=False,
        include_tables=False,
        no_fallback=False,
        favor_recall=True,
    )
    if not text:
        raise ValueError("Could not extract text content from the page")

    return text


def extract_from_pdf(pdf_bytes: bytes) -> str:
    """Extract text from a PDF file."""
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    pages = []
    for page in doc:
        pages.append(page.get_text())
    doc.close()

    text = "\n\n".join(pages)
    if not text.strip():
        raise ValueError("Could not extract text from PDF (may be image-based)")

    return text


def extract_from_text(raw: str) -> str:
    """Pass through raw text with basic cleanup."""
    return raw.strip()
