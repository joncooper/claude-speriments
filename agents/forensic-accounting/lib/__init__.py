"""
Forensic Accounting Library

A comprehensive toolkit for forensic accounting analysis of publicly-traded companies.
"""

from .forensic_analysis import ForensicAccountingAnalyzer, run_forensic_analysis
from .sec_data import SECDataFetcher, format_currency, calculate_percentage_change
from .beneish_score import BeneishMScore
from .red_flags import ForensicRedFlagAnalyzer, RedFlagFinding

__all__ = [
    "ForensicAccountingAnalyzer",
    "run_forensic_analysis",
    "SECDataFetcher",
    "BeneishMScore",
    "ForensicRedFlagAnalyzer",
    "RedFlagFinding",
    "format_currency",
    "calculate_percentage_change"
]

__version__ = "1.0.0"
