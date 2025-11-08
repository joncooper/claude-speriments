"""
Beneish M-Score Calculator

Implements the Beneish M-Score model for detecting earnings manipulation.
Developed by Professor Messod Beneish, this model uses 8 financial ratios
to identify companies likely manipulating their earnings.

Reference:
Beneish, M. D. (1999). "The Detection of Earnings Manipulation."
Financial Analysts Journal, 55(5), 24-36.
"""

from typing import Dict, Optional, List, Tuple
import math


class BeneishMScore:
    """
    Calculate Beneish M-Score for earnings manipulation detection.

    The model uses 8 variables (indices) calculated from financial statements:
    - DSRI: Days Sales in Receivables Index
    - GMI: Gross Margin Index
    - AQI: Asset Quality Index
    - SGI: Sales Growth Index
    - DEPI: Depreciation Index
    - SGAI: Sales, General and Administrative Expenses Index
    - LVGI: Leverage Index
    - TATA: Total Accruals to Total Assets

    A score > -2.22 suggests high probability of earnings manipulation.
    """

    # Model coefficients from Beneish (1999)
    COEFFICIENTS = {
        "intercept": -4.84,
        "DSRI": 0.92,
        "GMI": 0.528,
        "AQI": 0.404,
        "SGI": 0.892,
        "DEPI": 0.115,
        "SGAI": -0.172,
        "TATA": 4.679,
        "LVGI": -0.327
    }

    # Updated threshold from Beneish, Lee, and Nichols (2013)
    THRESHOLD_8_VAR = -2.22  # 8-variable model
    THRESHOLD_5_VAR = -1.78  # 5-variable model (more conservative)

    def __init__(self):
        """Initialize the Beneish M-Score calculator."""
        self.variables = {}
        self.score = None
        self.interpretation = ""

    def calculate_dsri(self, ar_current: float, sales_current: float,
                       ar_prior: float, sales_prior: float) -> float:
        """
        Calculate Days Sales in Receivables Index (DSRI).

        DSRI = (AR_t / Sales_t) / (AR_t-1 / Sales_t-1)

        A large increase in DSR suggests revenue inflation or
        aggressive credit policies.

        Args:
            ar_current: Accounts receivable in current year
            sales_current: Sales in current year
            ar_prior: Accounts receivable in prior year
            sales_prior: Sales in prior year

        Returns:
            DSRI value
        """
        if sales_current == 0 or sales_prior == 0 or ar_prior == 0:
            return 1.0

        dsr_current = ar_current / sales_current
        dsr_prior = ar_prior / sales_prior

        if dsr_prior == 0:
            return 1.0

        return dsr_current / dsr_prior

    def calculate_gmi(self, gross_margin_prior: float, gross_margin_current: float) -> float:
        """
        Calculate Gross Margin Index (GMI).

        GMI = Gross Margin_t-1 / Gross Margin_t

        A value > 1 indicates deteriorating margins, which may
        pressure management to manipulate earnings.

        Args:
            gross_margin_prior: (Sales - COGS) / Sales in prior year
            gross_margin_current: (Sales - COGS) / Sales in current year

        Returns:
            GMI value
        """
        if gross_margin_current == 0:
            return 1.0

        return gross_margin_prior / gross_margin_current

    def calculate_aqi(self, total_assets_current: float, ppe_current: float,
                     current_assets_current: float, total_assets_prior: float,
                     ppe_prior: float, current_assets_prior: float) -> float:
        """
        Calculate Asset Quality Index (AQI).

        AQI = [1 - (CA_t + PPE_t) / TA_t] / [1 - (CA_t-1 + PPE_t-1) / TA_t-1]

        A value > 1 suggests increased proportion of "soft" assets,
        which are easier to manipulate.

        Args:
            total_assets_current: Total assets in current year
            ppe_current: Property, plant & equipment (net) in current year
            current_assets_current: Current assets in current year
            total_assets_prior: Total assets in prior year
            ppe_prior: Property, plant & equipment (net) in prior year
            current_assets_prior: Current assets in prior year

        Returns:
            AQI value
        """
        if total_assets_current == 0 or total_assets_prior == 0:
            return 1.0

        aqi_current = 1 - ((current_assets_current + ppe_current) / total_assets_current)
        aqi_prior = 1 - ((current_assets_prior + ppe_prior) / total_assets_prior)

        if aqi_prior == 0:
            return 1.0

        return aqi_current / aqi_prior

    def calculate_sgi(self, sales_current: float, sales_prior: float) -> float:
        """
        Calculate Sales Growth Index (SGI).

        SGI = Sales_t / Sales_t-1

        Growth companies are under pressure to meet targets and
        may be more likely to manipulate earnings.

        Args:
            sales_current: Sales in current year
            sales_prior: Sales in prior year

        Returns:
            SGI value
        """
        if sales_prior == 0:
            return 1.0

        return sales_current / sales_prior

    def calculate_depi(self, depreciation_rate_prior: float,
                       depreciation_rate_current: float) -> float:
        """
        Calculate Depreciation Index (DEPI).

        DEPI = Depreciation Rate_t-1 / Depreciation Rate_t
        where Depreciation Rate = Depreciation / (Depreciation + PPE)

        A value > 1 suggests slower depreciation, possibly indicating
        inflated earnings.

        Args:
            depreciation_rate_prior: Depreciation rate in prior year
            depreciation_rate_current: Depreciation rate in current year

        Returns:
            DEPI value
        """
        if depreciation_rate_current == 0:
            return 1.0

        return depreciation_rate_prior / depreciation_rate_current

    def calculate_sgai(self, sga_current: float, sales_current: float,
                       sga_prior: float, sales_prior: float) -> float:
        """
        Calculate Sales, General, and Administrative Expenses Index (SGAI).

        SGAI = (SGA_t / Sales_t) / (SGA_t-1 / Sales_t-1)

        A disproportionate increase in sales overhead may signal
        declining prospects, pressuring earnings manipulation.

        Args:
            sga_current: SGA expenses in current year
            sales_current: Sales in current year
            sga_prior: SGA expenses in prior year
            sales_prior: Sales in prior year

        Returns:
            SGAI value
        """
        if sales_current == 0 or sales_prior == 0:
            return 1.0

        sgai_current = sga_current / sales_current
        sgai_prior = sga_prior / sales_prior

        if sgai_prior == 0:
            return 1.0

        return sgai_current / sgai_prior

    def calculate_lvgi(self, total_debt_current: float, total_assets_current: float,
                       total_debt_prior: float, total_assets_prior: float) -> float:
        """
        Calculate Leverage Index (LVGI).

        LVGI = [(LTD_t + CL_t) / TA_t] / [(LTD_t-1 + CL_t-1) / TA_t-1]

        An increase in leverage may indicate pressure to manipulate
        earnings to meet debt covenants.

        Args:
            total_debt_current: Total debt in current year
            total_assets_current: Total assets in current year
            total_debt_prior: Total debt in prior year
            total_assets_prior: Total assets in prior year

        Returns:
            LVGI value
        """
        if total_assets_current == 0 or total_assets_prior == 0:
            return 1.0

        leverage_current = total_debt_current / total_assets_current
        leverage_prior = total_debt_prior / total_assets_prior

        if leverage_prior == 0:
            return 1.0

        return leverage_current / leverage_prior

    def calculate_tata(self, net_income: float, operating_cash_flow: float,
                       total_assets: float) -> float:
        """
        Calculate Total Accruals to Total Assets (TATA).

        TATA = (Income from Continuing Operations - Cash Flow from Operations) / Total Assets

        Higher accruals relative to assets may indicate earnings
        manipulation through accrual accounting.

        Args:
            net_income: Net income (or income from continuing operations)
            operating_cash_flow: Cash flow from operating activities
            total_assets: Total assets

        Returns:
            TATA value
        """
        if total_assets == 0:
            return 0.0

        return (net_income - operating_cash_flow) / total_assets

    def calculate_m_score(self, financial_data: Dict[str, float]) -> Tuple[float, Dict[str, float]]:
        """
        Calculate the Beneish M-Score from financial statement data.

        Args:
            financial_data: Dictionary containing required financial metrics

        Returns:
            Tuple of (m_score, variables_dict)
        """
        # Extract data for current and prior year
        required_fields = [
            "ar_current", "ar_prior", "sales_current", "sales_prior",
            "cogs_current", "cogs_prior", "total_assets_current", "total_assets_prior",
            "ppe_current", "ppe_prior", "current_assets_current", "current_assets_prior",
            "depreciation_current", "depreciation_prior", "sga_current", "sga_prior",
            "total_debt_current", "total_debt_prior", "net_income_current",
            "operating_cf_current"
        ]

        # Check for missing fields
        missing = [field for field in required_fields if field not in financial_data]
        if missing:
            raise ValueError(f"Missing required fields: {missing}")

        # Calculate all 8 variables
        variables = {}

        # 1. DSRI
        variables["DSRI"] = self.calculate_dsri(
            financial_data["ar_current"],
            financial_data["sales_current"],
            financial_data["ar_prior"],
            financial_data["sales_prior"]
        )

        # 2. GMI
        gross_margin_current = ((financial_data["sales_current"] - financial_data["cogs_current"]) /
                                financial_data["sales_current"]) if financial_data["sales_current"] != 0 else 0
        gross_margin_prior = ((financial_data["sales_prior"] - financial_data["cogs_prior"]) /
                              financial_data["sales_prior"]) if financial_data["sales_prior"] != 0 else 0
        variables["GMI"] = self.calculate_gmi(gross_margin_prior, gross_margin_current)

        # 3. AQI
        variables["AQI"] = self.calculate_aqi(
            financial_data["total_assets_current"],
            financial_data["ppe_current"],
            financial_data["current_assets_current"],
            financial_data["total_assets_prior"],
            financial_data["ppe_prior"],
            financial_data["current_assets_prior"]
        )

        # 4. SGI
        variables["SGI"] = self.calculate_sgi(
            financial_data["sales_current"],
            financial_data["sales_prior"]
        )

        # 5. DEPI
        depreciation_rate_current = (financial_data["depreciation_current"] /
                                     (financial_data["depreciation_current"] + financial_data["ppe_current"])
                                     if (financial_data["depreciation_current"] + financial_data["ppe_current"]) != 0 else 0)
        depreciation_rate_prior = (financial_data["depreciation_prior"] /
                                   (financial_data["depreciation_prior"] + financial_data["ppe_prior"])
                                   if (financial_data["depreciation_prior"] + financial_data["ppe_prior"]) != 0 else 0)
        variables["DEPI"] = self.calculate_depi(depreciation_rate_prior, depreciation_rate_current)

        # 6. SGAI
        variables["SGAI"] = self.calculate_sgai(
            financial_data["sga_current"],
            financial_data["sales_current"],
            financial_data["sga_prior"],
            financial_data["sales_prior"]
        )

        # 7. TATA
        variables["TATA"] = self.calculate_tata(
            financial_data["net_income_current"],
            financial_data["operating_cf_current"],
            financial_data["total_assets_current"]
        )

        # 8. LVGI
        variables["LVGI"] = self.calculate_lvgi(
            financial_data["total_debt_current"],
            financial_data["total_assets_current"],
            financial_data["total_debt_prior"],
            financial_data["total_assets_prior"]
        )

        # Calculate M-Score
        m_score = self.COEFFICIENTS["intercept"]
        for var_name, var_value in variables.items():
            m_score += self.COEFFICIENTS[var_name] * var_value

        self.variables = variables
        self.score = m_score

        return m_score, variables

    def interpret_score(self, m_score: float) -> Dict[str, any]:
        """
        Interpret the Beneish M-Score.

        Args:
            m_score: The calculated M-Score

        Returns:
            Dictionary with interpretation details
        """
        is_manipulator = m_score > self.THRESHOLD_8_VAR

        if m_score > -1.78:
            risk_level = "VERY HIGH"
            interpretation = "Strong indication of earnings manipulation. Immediate investigation recommended."
        elif m_score > -2.22:
            risk_level = "HIGH"
            interpretation = "Significant red flags present. Detailed forensic review warranted."
        elif m_score > -2.50:
            risk_level = "MODERATE"
            interpretation = "Some concerning signals. Monitor closely and investigate specific areas."
        else:
            risk_level = "LOW"
            interpretation = "Financial reporting appears within normal parameters."

        return {
            "score": m_score,
            "threshold": self.THRESHOLD_8_VAR,
            "is_likely_manipulator": is_manipulator,
            "risk_level": risk_level,
            "interpretation": interpretation
        }

    def analyze_variables(self, variables: Dict[str, float]) -> List[Dict[str, any]]:
        """
        Analyze individual Beneish variables for specific red flags.

        Args:
            variables: Dictionary of calculated Beneish variables

        Returns:
            List of findings for variables indicating potential manipulation
        """
        findings = []

        # DSRI > 1.031 is concerning
        if variables.get("DSRI", 1.0) > 1.031:
            findings.append({
                "variable": "DSRI",
                "value": variables["DSRI"],
                "threshold": 1.031,
                "concern": "Days Sales in Receivables increasing faster than sales",
                "implications": [
                    "Potential revenue inflation",
                    "Aggressive credit policies",
                    "Channel stuffing",
                    "Difficulties collecting receivables"
                ]
            })

        # GMI > 1.014 is concerning
        if variables.get("GMI", 1.0) > 1.014:
            findings.append({
                "variable": "GMI",
                "value": variables["GMI"],
                "threshold": 1.014,
                "concern": "Gross margins deteriorating",
                "implications": [
                    "Weakening competitive position",
                    "Increased pressure to manipulate earnings",
                    "Cost control issues",
                    "Pricing pressure"
                ]
            })

        # AQI > 1.039 is concerning
        if variables.get("AQI", 1.0) > 1.039:
            findings.append({
                "variable": "AQI",
                "value": variables["AQI"],
                "threshold": 1.039,
                "concern": "Increasing proportion of soft assets",
                "implications": [
                    "Greater reliance on intangible/deferred assets",
                    "Potential asset capitalization issues",
                    "Easier to manipulate asset values",
                    "Reduced asset quality"
                ]
            })

        # SGI > 1.134 is concerning
        if variables.get("SGI", 1.0) > 1.134:
            findings.append({
                "variable": "SGI",
                "value": variables["SGI"],
                "threshold": 1.134,
                "concern": "Rapid sales growth",
                "implications": [
                    "Pressure to maintain growth trajectory",
                    "Incentive to inflate revenues",
                    "Growth companies under scrutiny",
                    "May be unsustainable"
                ]
            })

        # DEPI > 1.001 is concerning
        if variables.get("DEPI", 1.0) > 1.001:
            findings.append({
                "variable": "DEPI",
                "value": variables["DEPI"],
                "threshold": 1.001,
                "concern": "Depreciation rate slowing",
                "implications": [
                    "Potential manipulation of depreciation assumptions",
                    "Extending asset useful lives",
                    "Inflating earnings by reducing expenses",
                    "Assets may be overvalued"
                ]
            })

        # SGAI > 1.001 is concerning
        if variables.get("SGAI", 1.0) > 1.001:
            findings.append({
                "variable": "SGAI",
                "value": variables["SGAI"],
                "threshold": 1.001,
                "concern": "SG&A expenses growing faster than sales",
                "implications": [
                    "Operational inefficiency",
                    "Declining prospects",
                    "Increased pressure to manipulate",
                    "Cost structure issues"
                ]
            })

        # TATA > 0.018 is concerning
        if variables.get("TATA", 0.0) > 0.018:
            findings.append({
                "variable": "TATA",
                "value": variables["TATA"],
                "threshold": 0.018,
                "concern": "High total accruals relative to assets",
                "implications": [
                    "Earnings not supported by cash flow",
                    "Aggressive accrual accounting",
                    "Potential earnings manipulation",
                    "Quality of earnings concern"
                ]
            })

        # LVGI > 1.037 is concerning
        if variables.get("LVGI", 1.0) > 1.037:
            findings.append({
                "variable": "LVGI",
                "value": variables["LVGI"],
                "threshold": 1.037,
                "concern": "Increasing financial leverage",
                "implications": [
                    "Pressure to meet debt covenants",
                    "Incentive to manipulate earnings",
                    "Reduced financial flexibility",
                    "Increased financial risk"
                ]
            })

        return findings
