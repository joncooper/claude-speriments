"""
Forensic Accounting Analysis Orchestrator

This module coordinates the complete forensic accounting analysis,
including data gathering, Beneish M-Score calculation, red flag detection,
and trend analysis.
"""

from typing import Dict, List, Optional, Tuple
import json
from datetime import datetime

try:
    from .sec_data import SECDataFetcher, format_currency, calculate_percentage_change
    from .beneish_score import BeneishMScore
    from .red_flags import ForensicRedFlagAnalyzer, RedFlagFinding
except ImportError:
    from sec_data import SECDataFetcher, format_currency, calculate_percentage_change
    from beneish_score import BeneishMScore
    from red_flags import ForensicRedFlagAnalyzer, RedFlagFinding


class ForensicAccountingAnalyzer:
    """
    Complete forensic accounting analysis for a publicly-traded company.

    This class orchestrates all components of the forensic analysis:
    1. Data gathering from SEC EDGAR
    2. Financial metric extraction and preparation
    3. Beneish M-Score calculation
    4. Red flag detection
    5. Trend analysis
    6. Multi-year comparison
    """

    def __init__(self):
        """Initialize the forensic analyzer."""
        self.sec_fetcher = SECDataFetcher()
        self.beneish_calculator = BeneishMScore()
        self.red_flag_analyzer = ForensicRedFlagAnalyzer()

        self.company_info = None
        self.financial_metrics = None
        self.analysis_results = None

    def analyze_company(self, ticker: str, num_years: int = 5) -> Dict:
        """
        Perform complete forensic accounting analysis on a company.

        Args:
            ticker: Stock ticker symbol
            num_years: Number of years of historical data to analyze

        Returns:
            Dictionary containing complete analysis results
        """
        print(f"\n{'='*70}")
        print(f"FORENSIC ACCOUNTING ANALYSIS: {ticker.upper()}")
        print(f"{'='*70}\n")

        # Step 1: Gather data
        print("Step 1: Gathering financial data from SEC EDGAR...")
        company_info, financial_metrics = self.sec_fetcher.get_financial_data(ticker, num_years)

        if not company_info or not financial_metrics:
            raise ValueError(f"Could not retrieve financial data for ticker {ticker}")

        self.company_info = company_info
        self.financial_metrics = financial_metrics

        print(f"✓ Retrieved {len(financial_metrics.get('Revenues', []))} years of data for {company_info['name']}\n")

        # Step 2: Prepare standardized data
        print("Step 2: Preparing financial data for analysis...")
        annual_data = self._prepare_annual_data(financial_metrics)
        print(f"✓ Prepared {len(annual_data)} years of standardized data\n")

        # Step 3: Calculate Beneish M-Score for each year (need 2 years)
        print("Step 3: Calculating Beneish M-Scores...")
        beneish_results = self._calculate_beneish_scores(annual_data)
        print(f"✓ Calculated M-Scores for {len(beneish_results)} periods\n")

        # Step 4: Detect red flags
        print("Step 4: Analyzing for accounting red flags...")
        red_flags = self.red_flag_analyzer.analyze_all(annual_data)
        severity_counts = self.red_flag_analyzer.get_severity_counts()
        print(f"✓ Identified {len(red_flags)} red flags:")
        for severity in ["Critical", "High", "Medium", "Low"]:
            count = severity_counts.get(severity, 0)
            if count > 0:
                print(f"  - {severity}: {count}")
        print()

        # Step 5: Trend analysis
        print("Step 5: Performing trend analysis...")
        trends = self._analyze_trends(annual_data, beneish_results)
        print(f"✓ Analyzed {len(trends)} trend indicators\n")

        # Step 6: Overall assessment
        print("Step 6: Generating overall assessment...")
        assessment = self._generate_assessment(beneish_results, red_flags, trends)
        print(f"✓ Overall Risk Level: {assessment['risk_level']}\n")

        # Compile results
        self.analysis_results = {
            "metadata": {
                "ticker": ticker.upper(),
                "company_name": company_info["name"],
                "cik": company_info["cik"],
                "industry": company_info["sicDescription"],
                "analysis_date": datetime.now().isoformat(),
                "years_analyzed": len(annual_data)
            },
            "company_info": company_info,
            "annual_data": annual_data,
            "beneish_scores": beneish_results,
            "red_flags": [self._serialize_red_flag(rf) for rf in red_flags],
            "trends": trends,
            "assessment": assessment
        }

        return self.analysis_results

    def _prepare_annual_data(self, financial_metrics: Dict[str, List[Dict]]) -> List[Dict]:
        """
        Prepare annual financial data in standardized format.

        Args:
            financial_metrics: Raw financial metrics from SEC data

        Returns:
            List of dictionaries with standardized annual data
        """
        # Determine how many years we have (use Revenues as reference)
        revenues = financial_metrics.get("Revenues", [])
        num_years = len(revenues)

        annual_data = []

        for i in range(num_years):
            year_data = {}

            # Extract fiscal year from revenues
            if i < len(revenues):
                year_data["fiscal_year_end"] = revenues[i].get("end", "Unknown")
                year_data["form"] = revenues[i].get("form", "Unknown")

            # Extract all metrics for this year
            for metric_name, metric_values in financial_metrics.items():
                if i < len(metric_values):
                    year_data[metric_name] = metric_values[i].get("val", 0)
                else:
                    year_data[metric_name] = 0

            annual_data.append(year_data)

        return annual_data

    def _calculate_beneish_scores(self, annual_data: List[Dict]) -> List[Dict]:
        """
        Calculate Beneish M-Scores for each consecutive year pair.

        Args:
            annual_data: List of annual financial data dictionaries

        Returns:
            List of Beneish score results
        """
        results = []

        # Need at least 2 years to calculate M-Score
        for i in range(len(annual_data) - 1):
            current_year = annual_data[i]
            prior_year = annual_data[i + 1]

            try:
                # Prepare data in format expected by Beneish calculator
                beneish_data = {
                    "ar_current": current_year.get("AccountsReceivable", 0),
                    "ar_prior": prior_year.get("AccountsReceivable", 0),
                    "sales_current": current_year.get("Revenues", 0),
                    "sales_prior": prior_year.get("Revenues", 0),
                    "cogs_current": current_year.get("CostOfRevenue", 0),
                    "cogs_prior": prior_year.get("CostOfRevenue", 0),
                    "total_assets_current": current_year.get("Assets", 0),
                    "total_assets_prior": prior_year.get("Assets", 0),
                    "ppe_current": current_year.get("PropertyPlantEquipment", 0),
                    "ppe_prior": prior_year.get("PropertyPlantEquipment", 0),
                    "current_assets_current": current_year.get("CurrentAssets", 0),
                    "current_assets_prior": prior_year.get("CurrentAssets", 0),
                    "depreciation_current": current_year.get("DepreciationAndAmortization", 1),
                    "depreciation_prior": prior_year.get("DepreciationAndAmortization", 1),
                    "sga_current": self._estimate_sga(current_year),
                    "sga_prior": self._estimate_sga(prior_year),
                    "total_debt_current": current_year.get("Liabilities", 0),
                    "total_debt_prior": prior_year.get("Liabilities", 0),
                    "net_income_current": current_year.get("NetIncome", 0),
                    "operating_cf_current": current_year.get("OperatingCashFlow", 0)
                }

                # Calculate M-Score
                m_score, variables = self.beneish_calculator.calculate_m_score(beneish_data)
                interpretation = self.beneish_calculator.interpret_score(m_score)
                variable_analysis = self.beneish_calculator.analyze_variables(variables)

                results.append({
                    "period": f"{current_year.get('fiscal_year_end', 'Unknown')}",
                    "comparison_to": f"{prior_year.get('fiscal_year_end', 'Unknown')}",
                    "m_score": m_score,
                    "variables": variables,
                    "interpretation": interpretation,
                    "variable_flags": variable_analysis
                })

            except Exception as e:
                print(f"Warning: Could not calculate Beneish score for period {i}: {e}")

        return results

    def _estimate_sga(self, year_data: Dict) -> float:
        """
        Estimate SG&A expenses from available data.

        If not directly available, estimate as Operating Income minus Gross Profit.
        """
        # Try to calculate from income statement components
        revenues = year_data.get("Revenues", 0)
        cogs = year_data.get("CostOfRevenue", 0)
        operating_income = year_data.get("OperatingIncome", 0)

        if revenues > 0 and cogs >= 0:
            gross_profit = revenues - cogs
            # SGA = Gross Profit - Operating Income
            sga = gross_profit - operating_income
            return max(sga, 0)  # Can't be negative

        # Fallback: use a percentage of revenue (typical SG&A is 10-30%)
        return revenues * 0.20

    def _analyze_trends(self, annual_data: List[Dict], beneish_results: List[Dict]) -> Dict:
        """
        Analyze trends over time in key metrics and scores.

        Args:
            annual_data: Annual financial data
            beneish_results: Beneish M-Score results

        Returns:
            Dictionary of trend analyses
        """
        trends = {}

        # M-Score trend
        if len(beneish_results) >= 2:
            m_scores = [r["m_score"] for r in beneish_results]
            trends["m_score_trend"] = {
                "direction": "Worsening" if m_scores[0] > m_scores[-1] else "Improving",
                "latest": m_scores[0],
                "oldest": m_scores[-1],
                "change": m_scores[0] - m_scores[-1],
                "is_deteriorating": m_scores[0] > m_scores[-1]
            }

        # Revenue growth trend
        if len(annual_data) >= 3:
            revenues = [year.get("Revenues", 0) for year in annual_data[:3]]
            if all(r > 0 for r in revenues):
                growth_rates = []
                for i in range(len(revenues) - 1):
                    if revenues[i + 1] > 0:
                        growth = ((revenues[i] - revenues[i + 1]) / revenues[i + 1]) * 100
                        growth_rates.append(growth)

                trends["revenue_growth"] = {
                    "latest_rate_%": growth_rates[0] if growth_rates else 0,
                    "average_rate_%": sum(growth_rates) / len(growth_rates) if growth_rates else 0,
                    "is_accelerating": growth_rates[0] > growth_rates[-1] if len(growth_rates) >= 2 else False
                }

        # Profitability trend
        if len(annual_data) >= 3:
            margins = []
            for year in annual_data[:3]:
                revenue = year.get("Revenues", 0)
                net_income = year.get("NetIncome", 0)
                if revenue > 0:
                    margin = (net_income / revenue) * 100
                    margins.append(margin)

            if margins:
                trends["profit_margin"] = {
                    "latest_%": margins[0],
                    "average_%": sum(margins) / len(margins),
                    "is_improving": margins[0] > margins[-1] if len(margins) >= 2 else False
                }

        # Cash flow trend
        if len(annual_data) >= 2:
            latest = annual_data[0]
            ni = latest.get("NetIncome", 0)
            ocf = latest.get("OperatingCashFlow", 0)

            if ni > 0:
                trends["cash_flow_quality"] = {
                    "cf_to_ni_ratio": ocf / ni,
                    "is_healthy": (ocf / ni) > 0.8
                }

        return trends

    def _generate_assessment(self, beneish_results: List[Dict],
                            red_flags: List[RedFlagFinding],
                            trends: Dict) -> Dict:
        """
        Generate overall assessment of accounting aggressiveness.

        Args:
            beneish_results: Beneish M-Score results
            red_flags: List of detected red flags
            trends: Trend analysis results

        Returns:
            Dictionary with overall assessment
        """
        risk_score = 0
        factors = []

        # Factor 1: Latest Beneish M-Score
        if beneish_results:
            latest_score = beneish_results[0]["m_score"]
            if latest_score > -1.78:
                risk_score += 40
                factors.append("Very high Beneish M-Score indicating likely manipulation")
            elif latest_score > -2.22:
                risk_score += 25
                factors.append("Elevated Beneish M-Score above manipulation threshold")
            elif latest_score > -2.50:
                risk_score += 10
                factors.append("Moderately elevated Beneish M-Score")

        # Factor 2: M-Score trend
        if trends.get("m_score_trend", {}).get("is_deteriorating"):
            risk_score += 15
            factors.append("Beneish M-Score deteriorating over time")

        # Factor 3: Red flags by severity
        severity_counts = {}
        for rf in red_flags:
            severity_counts[rf.severity] = severity_counts.get(rf.severity, 0) + 1

        critical_count = severity_counts.get("Critical", 0)
        high_count = severity_counts.get("High", 0)
        medium_count = severity_counts.get("Medium", 0)

        if critical_count > 0:
            risk_score += critical_count * 15
            factors.append(f"{critical_count} critical red flag(s) detected")

        if high_count > 0:
            risk_score += high_count * 8
            factors.append(f"{high_count} high severity red flag(s) detected")

        if medium_count > 2:
            risk_score += 10
            factors.append(f"Multiple ({medium_count}) medium severity red flags")

        # Factor 4: Cash flow quality
        cf_quality = trends.get("cash_flow_quality", {})
        if not cf_quality.get("is_healthy", True):
            risk_score += 15
            factors.append("Poor cash flow quality (CF significantly below earnings)")

        # Factor 5: Margin trends
        margin_trend = trends.get("profit_margin", {})
        if not margin_trend.get("is_improving", True) and margin_trend.get("latest_%", 0) < 5:
            risk_score += 10
            factors.append("Deteriorating or low profit margins")

        # Determine overall risk level
        if risk_score >= 60:
            risk_level = "VERY HIGH"
            recommendation = "Immediate forensic investigation recommended. Multiple severe indicators of potential manipulation."
        elif risk_score >= 40:
            risk_level = "HIGH"
            recommendation = "Detailed forensic review strongly recommended. Significant red flags present."
        elif risk_score >= 20:
            risk_level = "MODERATE"
            recommendation = "Enhanced monitoring and targeted investigation of specific areas recommended."
        else:
            risk_level = "LOW"
            recommendation = "Financial reporting appears within normal parameters. Standard due diligence appropriate."

        return {
            "risk_level": risk_level,
            "risk_score": risk_score,
            "risk_factors": factors,
            "recommendation": recommendation,
            "total_red_flags": len(red_flags),
            "critical_red_flags": critical_count,
            "high_red_flags": high_count,
            "medium_red_flags": medium_count
        }

    def _serialize_red_flag(self, red_flag: RedFlagFinding) -> Dict:
        """Convert RedFlagFinding to dictionary for JSON serialization."""
        return {
            "category": red_flag.category,
            "severity": red_flag.severity,
            "title": red_flag.title,
            "description": red_flag.description,
            "metrics": red_flag.metrics,
            "implications": red_flag.implications,
            "recommendations": red_flag.recommendations
        }

    def save_results(self, filepath: str) -> None:
        """Save analysis results to JSON file."""
        if not self.analysis_results:
            raise ValueError("No analysis results to save. Run analyze_company() first.")

        with open(filepath, 'w') as f:
            json.dump(self.analysis_results, f, indent=2, default=str)

        print(f"Results saved to {filepath}")


def run_forensic_analysis(ticker: str, num_years: int = 5) -> Dict:
    """
    Convenience function to run complete forensic analysis.

    Args:
        ticker: Stock ticker symbol
        num_years: Number of years to analyze

    Returns:
        Complete analysis results dictionary
    """
    analyzer = ForensicAccountingAnalyzer()
    return analyzer.analyze_company(ticker, num_years)
