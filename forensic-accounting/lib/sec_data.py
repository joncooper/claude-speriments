"""
SEC EDGAR Data Access Module

This module provides utilities to fetch and parse financial data from SEC EDGAR filings.
It accesses the official SEC API at data.sec.gov to retrieve 10-K and 10-Q filings
and extracts key financial metrics for forensic accounting analysis.
"""

import requests
import json
import time
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import re


class SECDataFetcher:
    """
    Fetches financial data from SEC EDGAR database.

    The SEC requires proper user-agent headers to prevent blocking.
    Data is fetched from the official SEC.gov API endpoints.
    """

    BASE_URL = "https://data.sec.gov"

    def __init__(self, user_agent: str = "ForensicAccountingTool/1.0 (claude-code-analysis; research@example.com)"):
        """
        Initialize the SEC data fetcher.

        Args:
            user_agent: User agent string for API requests (must include contact info in production)
        """
        self.headers = {
            "User-Agent": user_agent,
            "Accept-Encoding": "gzip, deflate"
        }
        self.request_delay = 0.11  # SEC rate limit: 10 requests per second, be conservative

    def _make_request(self, url: str) -> Optional[Dict]:
        """
        Make a request to SEC API with rate limiting.

        Args:
            url: Full URL to request

        Returns:
            JSON response as dictionary, or None if request fails
        """
        time.sleep(self.request_delay)

        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")
            return None

    def get_cik_from_ticker(self, ticker: str) -> Optional[str]:
        """
        Convert stock ticker to CIK (Central Index Key).

        Args:
            ticker: Stock ticker symbol (e.g., 'AAPL', 'TSLA')

        Returns:
            10-digit CIK string, or None if not found
        """
        # First try to get the company tickers mapping file
        # This contains all tickers mapped to CIKs
        ticker_url = "https://www.sec.gov/files/company_tickers.json"
        ticker_data = self._make_request(ticker_url)

        if ticker_data:
            for entry in ticker_data.values():
                if entry.get("ticker", "").upper() == ticker.upper():
                    cik = str(entry.get("cik_str")).zfill(10)
                    return cik

        print(f"Warning: Could not find CIK for ticker {ticker}")
        print("Note: In sandboxed environments, SEC API access may be restricted.")
        print("This tool requires internet access to https://www.sec.gov/")
        return None

    def get_company_facts(self, ticker: str) -> Optional[Dict]:
        """
        Get all company facts (XBRL data) for a given ticker.

        Args:
            ticker: Stock ticker symbol

        Returns:
            Dictionary containing all XBRL facts for the company
        """
        cik = self.get_cik_from_ticker(ticker)
        if not cik:
            print(f"Could not find CIK for ticker {ticker}")
            return None

        url = f"{self.BASE_URL}/api/xbrl/companyfacts/CIK{cik}.json"
        return self._make_request(url)

    def get_submission_history(self, ticker: str) -> Optional[Dict]:
        """
        Get filing submission history for a company.

        Args:
            ticker: Stock ticker symbol

        Returns:
            Dictionary containing submission history and recent filings
        """
        cik = self.get_cik_from_ticker(ticker)
        if not cik:
            return None

        url = f"{self.BASE_URL}/submissions/CIK{cik}.json"
        return self._make_request(url)

    def extract_financial_metrics(self, company_facts: Dict, num_years: int = 5) -> Dict[str, List[Dict]]:
        """
        Extract key financial metrics from company facts data.

        Args:
            company_facts: Company facts dictionary from get_company_facts()
            num_years: Number of years of historical data to extract

        Returns:
            Dictionary mapping metric names to lists of annual values
        """
        if not company_facts or "facts" not in company_facts:
            return {}

        # Define the XBRL tags we need for forensic accounting
        key_metrics = {
            # Income Statement
            "Revenues": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
                        "SalesRevenueNet", "RevenueFromContractWithCustomer"],
            "CostOfRevenue": ["CostOfRevenue", "CostOfGoodsAndServicesSold", "CostOfGoodsSold"],
            "GrossProfit": ["GrossProfit"],
            "OperatingIncome": ["OperatingIncomeLoss"],
            "NetIncome": ["NetIncomeLoss", "ProfitLoss"],
            "DepreciationAndAmortization": ["DepreciationDepletionAndAmortization",
                                           "DepreciationAndAmortization"],

            # Balance Sheet
            "Assets": ["Assets"],
            "CurrentAssets": ["AssetsCurrent"],
            "Cash": ["CashAndCashEquivalentsAtCarryingValue", "Cash"],
            "AccountsReceivable": ["AccountsReceivableNetCurrent", "AccountsReceivableNet"],
            "Inventory": ["InventoryNet"],
            "PropertyPlantEquipment": ["PropertyPlantAndEquipmentNet"],
            "Liabilities": ["Liabilities"],
            "CurrentLiabilities": ["LiabilitiesCurrent"],
            "AccountsPayable": ["AccountsPayableCurrent"],
            "LongTermDebt": ["LongTermDebt", "LongTermDebtNoncurrent"],
            "StockholdersEquity": ["StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],

            # Cash Flow Statement
            "OperatingCashFlow": ["NetCashProvidedByUsedInOperatingActivities"],
            "InvestingCashFlow": ["NetCashProvidedByUsedInInvestingActivities"],
            "FinancingCashFlow": ["NetCashProvidedByUsedInFinancingActivities"],
        }

        extracted = {}
        us_gaap_facts = company_facts.get("facts", {}).get("us-gaap", {})

        for metric_name, xbrl_tags in key_metrics.items():
            values = []

            # Try each possible XBRL tag
            for tag in xbrl_tags:
                if tag in us_gaap_facts:
                    # Get USD values only (10-K annual filings)
                    units = us_gaap_facts[tag].get("units", {})
                    usd_values = units.get("USD", [])

                    # Filter for 10-K filings (annual) and sort by date
                    annual_values = [
                        v for v in usd_values
                        if v.get("form") in ["10-K", "10-K/A"]
                    ]
                    annual_values.sort(key=lambda x: x.get("end", ""), reverse=True)

                    # Take most recent num_years
                    values = annual_values[:num_years]
                    if values:
                        break  # Found data for this metric

            if values:
                extracted[metric_name] = values

        return extracted

    def get_financial_data(self, ticker: str, num_years: int = 5) -> Tuple[Optional[Dict], Optional[Dict]]:
        """
        Get complete financial data for forensic analysis.

        Args:
            ticker: Stock ticker symbol
            num_years: Number of years of historical data

        Returns:
            Tuple of (company_info, financial_metrics)
        """
        print(f"Fetching data for {ticker}...")

        # Get company facts (XBRL data)
        company_facts = self.get_company_facts(ticker)
        if not company_facts:
            return None, None

        # Get submission history for company info
        submissions = self.get_submission_history(ticker)

        # Extract company information
        company_info = {
            "name": company_facts.get("entityName", "Unknown"),
            "cik": company_facts.get("cik", "Unknown"),
            "ticker": ticker.upper(),
            "sic": submissions.get("sic", "Unknown") if submissions else "Unknown",
            "sicDescription": submissions.get("sicDescription", "Unknown") if submissions else "Unknown",
        }

        # Extract financial metrics
        financial_metrics = self.extract_financial_metrics(company_facts, num_years)

        return company_info, financial_metrics


def format_currency(value: float) -> str:
    """Format a number as currency in millions."""
    if abs(value) >= 1e9:
        return f"${value/1e9:,.1f}B"
    elif abs(value) >= 1e6:
        return f"${value/1e6:,.1f}M"
    else:
        return f"${value:,.0f}"


def calculate_percentage_change(current: float, previous: float) -> float:
    """Calculate percentage change between two values."""
    if previous == 0:
        return 0.0
    return ((current - previous) / abs(previous)) * 100
