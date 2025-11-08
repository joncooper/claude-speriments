"""
Management Integrity Analysis Library

A comprehensive toolkit for analyzing whether public company management
follows through on their commitments.
"""

from .commitment_extractor import CommitmentExtractor
from .outcome_tracker import OutcomeTracker
from .credibility_scorer import CredibilityScorer
from .report_generator import ManagementIntegrityReport
from .sec_data import load_sec_data, extract_filing_sections, format_currency

__all__ = [
    "CommitmentExtractor",
    "OutcomeTracker",
    "CredibilityScorer",
    "ManagementIntegrityReport",
    "load_sec_data",
    "extract_filing_sections",
    "format_currency",
]

__version__ = "1.0.0"
