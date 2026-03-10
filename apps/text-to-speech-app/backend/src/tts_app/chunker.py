"""Split text into TTS-friendly chunks at sentence boundaries."""

import re

# Simple sentence boundary regex that handles common abbreviations
_SENTENCE_RE = re.compile(
    r'(?<=[.!?])\s+(?=[A-Z"])|(?<=[.!?])\n+', re.MULTILINE
)


def chunk_text(text: str, max_words: int = 250) -> list[str]:
    """Split text into chunks of roughly max_words, never breaking mid-sentence.

    Returns a list of text chunks suitable for TTS synthesis.
    """
    sentences = _split_sentences(text)
    chunks: list[str] = []
    current_chunk: list[str] = []
    current_word_count = 0

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        word_count = len(sentence.split())

        # If a single sentence exceeds max_words, it becomes its own chunk
        if word_count > max_words:
            if current_chunk:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
                current_word_count = 0
            chunks.append(sentence)
            continue

        # If adding this sentence would exceed the limit, start a new chunk
        if current_word_count + word_count > max_words and current_chunk:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_word_count = 0

        current_chunk.append(sentence)
        current_word_count += word_count

    # Don't forget the last chunk
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


def _split_sentences(text: str) -> list[str]:
    """Split text into sentences using regex-based boundary detection."""
    # First split on paragraph boundaries
    paragraphs = re.split(r"\n\s*\n", text)
    sentences = []

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        # Split paragraph into sentences
        parts = _SENTENCE_RE.split(para)
        for part in parts:
            part = part.strip()
            if part:
                sentences.append(part)

    return sentences
