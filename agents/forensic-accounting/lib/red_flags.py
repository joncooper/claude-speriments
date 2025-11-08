"""
Forensic Accounting Red Flag Detection

This module implements detection of common accounting red flags that
experienced forensic accountants look for when assessing financial
statement quality and detecting potential manipulation.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class RedFlagFinding:
    """Represents a detected red flag."""
    category: str
    severity: str  # "Low", "Medium", "High", "Critical"
    title: str
    description: str
    metrics: Dict[str, float]
    implications: List[str]
    recommendations: List[str]


class ForensicRedFlagAnalyzer:
    """
    Analyze financial statements for red flags indicating
    aggressive accounting or potential manipulation.
    """

    def __init__(self):
        """Initialize the red flag analyzer."""
        self.findings: List[RedFlagFinding] = []

    def analyze_all(self, financial_data: List[Dict]) -> List[RedFlagFinding]:
        """
        Run all red flag analyses on financial data.

        Args:
            financial_data: List of annual financial data dictionaries,
                          sorted from most recent to oldest

        Returns:
            List of RedFlagFinding objects
        """
        self.findings = []

        if len(financial_data) < 2:
            return self.findings

        # Run all analyses
        self.analyze_revenue_quality(financial_data)
        self.analyze_cash_flow_quality(financial_data)
        self.analyze_working_capital(financial_data)
        self.analyze_earnings_quality(financial_data)
        self.analyze_asset_quality(financial_data)
        self.analyze_debt_trends(financial_data)
        self.analyze_margins(financial_data)

        return self.findings

    def analyze_revenue_quality(self, financial_data: List[Dict]) -> None:
        """Analyze revenue quality and recognition patterns."""
        current = financial_data[0]
        prior = financial_data[1] if len(financial_data) > 1 else None

        if not prior:
            return

        # Check DSO (Days Sales Outstanding)
        revenue_current = current.get("Revenues", 0)
        revenue_prior = prior.get("Revenues", 0)
        ar_current = current.get("AccountsReceivable", 0)
        ar_prior = prior.get("AccountsReceivable", 0)

        if revenue_current > 0 and revenue_prior > 0:
            dso_current = (ar_current / revenue_current) * 365
            dso_prior = (ar_prior / revenue_prior) * 365

            if dso_prior > 0:
                dso_change = ((dso_current - dso_prior) / dso_prior) * 100

                # Red flag if DSO increasing significantly
                if dso_change > 10:
                    severity = "High" if dso_change > 20 else "Medium"
                    self.findings.append(RedFlagFinding(
                        category="Revenue Quality",
                        severity=severity,
                        title="Increasing Days Sales Outstanding (DSO)",
                        description=f"DSO increased by {dso_change:.1f}% from {dso_prior:.0f} to {dso_current:.0f} days. "
                                  f"Revenue is growing faster than cash collection.",
                        metrics={
                            "DSO_Current": dso_current,
                            "DSO_Prior": dso_prior,
                            "DSO_Change_%": dso_change
                        },
                        implications=[
                            "Potential aggressive revenue recognition",
                            "Customer payment issues or disputes",
                            "Channel stuffing or pull-forward of sales",
                            "Deteriorating customer creditworthiness",
                            "Revenue may not be as high quality as reported"
                        ],
                        recommendations=[
                            "Investigate accounts receivable aging schedule",
                            "Review revenue recognition policies for changes",
                            "Examine large or unusual transactions near period end",
                            "Check for right of return provisions",
                            "Verify customer acceptance and satisfaction"
                        ]
                    ))

        # Check revenue vs AR growth divergence
        if revenue_prior > 0 and ar_prior > 0:
            revenue_growth = ((revenue_current - revenue_prior) / revenue_prior) * 100
            ar_growth = ((ar_current - ar_prior) / ar_prior) * 100

            if ar_growth > revenue_growth + 15:
                self.findings.append(RedFlagFinding(
                    category="Revenue Quality",
                    severity="High",
                    title="Accounts Receivable Growing Faster Than Revenue",
                    description=f"AR grew {ar_growth:.1f}% while revenue grew {revenue_growth:.1f}%. "
                                f"This divergence suggests potential revenue quality issues.",
                    metrics={
                        "Revenue_Growth_%": revenue_growth,
                        "AR_Growth_%": ar_growth,
                        "Divergence_%": ar_growth - revenue_growth
                    },
                    implications=[
                        "Revenue may be recognized before earned",
                        "Collection difficulties not reflected in revenue",
                        "Potential bill-and-hold transactions",
                        "Sales to financially weak customers",
                        "Channel stuffing or trade loading"
                    ],
                    recommendations=[
                        "Scrutinize revenue recognition methodology",
                        "Review allowance for doubtful accounts adequacy",
                        "Investigate customer concentration",
                        "Examine fourth quarter revenue patterns",
                        "Check for side letters or unusual contract terms"
                    ]
                ))

    def analyze_cash_flow_quality(self, financial_data: List[Dict]) -> None:
        """Analyze cash flow quality and earnings quality."""
        current = financial_data[0]

        net_income = current.get("NetIncome", 0)
        operating_cf = current.get("OperatingCashFlow", 0)

        # Cash Flow to Net Income ratio
        if net_income > 0:
            cf_to_ni_ratio = operating_cf / net_income

            if cf_to_ni_ratio < 0.8:
                severity = "Critical" if cf_to_ni_ratio < 0.5 else "High"
                self.findings.append(RedFlagFinding(
                    category="Earnings Quality",
                    severity=severity,
                    title="Operating Cash Flow Significantly Below Net Income",
                    description=f"Operating cash flow is only {cf_to_ni_ratio:.1%} of net income. "
                                f"Earnings are not translating to cash.",
                    metrics={
                        "Net_Income": net_income,
                        "Operating_Cash_Flow": operating_cf,
                        "CF_to_NI_Ratio": cf_to_ni_ratio
                    },
                    implications=[
                        "Earnings heavily dependent on accruals",
                        "Potential aggressive accounting policies",
                        "Revenue or earnings manipulation possible",
                        "Working capital deterioration",
                        "Lower quality of reported earnings"
                    ],
                    recommendations=[
                        "Analyze components of accruals",
                        "Review working capital changes in detail",
                        "Investigate revenue recognition practices",
                        "Examine large non-cash charges",
                        "Compare to industry peers"
                    ]
                ))

        # Negative operating cash flow
        if operating_cf < 0 and net_income > 0:
            self.findings.append(RedFlagFinding(
                category="Earnings Quality",
                severity="Critical",
                title="Negative Operating Cash Flow Despite Positive Earnings",
                description="Company reports profit but burns cash from operations. "
                          "This is a major red flag for earnings quality.",
                metrics={
                    "Net_Income": net_income,
                    "Operating_Cash_Flow": operating_cf
                },
                implications=[
                    "Severe earnings quality concern",
                    "Business model may be unsustainable",
                    "Aggressive revenue recognition",
                    "Working capital management issues",
                    "High risk of financial distress"
                ],
                recommendations=[
                    "Immediate detailed cash flow analysis required",
                    "Review all accrual accounting policies",
                    "Assess business model sustainability",
                    "Examine liquidity and going concern",
                    "Compare with direct competitors"
                ]
            ))

    def analyze_working_capital(self, financial_data: List[Dict]) -> None:
        """Analyze working capital trends and quality."""
        if len(financial_data) < 2:
            return

        current = financial_data[0]
        prior = financial_data[1]

        # Calculate working capital metrics
        current_assets = current.get("CurrentAssets", 0)
        current_liabilities = current.get("CurrentLiabilities", 0)
        inventory_current = current.get("Inventory", 0)
        revenue_current = current.get("Revenues", 0)

        current_assets_prior = prior.get("CurrentAssets", 0)
        current_liabilities_prior = prior.get("CurrentLiabilities", 0)
        inventory_prior = prior.get("Inventory", 0)
        revenue_prior = prior.get("Revenues", 0)

        # Current ratio declining significantly
        if current_liabilities > 0 and current_liabilities_prior > 0:
            current_ratio = current_assets / current_liabilities
            current_ratio_prior = current_assets_prior / current_liabilities_prior

            if current_ratio_prior > 0:
                ratio_change = ((current_ratio - current_ratio_prior) / current_ratio_prior) * 100

                if ratio_change < -15 and current_ratio < 1.5:
                    self.findings.append(RedFlagFinding(
                        category="Liquidity",
                        severity="High",
                        title="Deteriorating Current Ratio",
                        description=f"Current ratio declined {abs(ratio_change):.1f}% from {current_ratio_prior:.2f} to {current_ratio:.2f}. "
                                  f"Liquidity is weakening.",
                        metrics={
                            "Current_Ratio": current_ratio,
                            "Prior_Current_Ratio": current_ratio_prior,
                            "Change_%": ratio_change
                        },
                        implications=[
                            "Declining liquidity position",
                            "Potential difficulty meeting short-term obligations",
                            "Working capital management issues",
                            "May indicate financial stress"
                        ],
                        recommendations=[
                            "Review working capital management policies",
                            "Assess debt maturity schedule",
                            "Evaluate cash conversion cycle",
                            "Check for off-balance sheet obligations"
                        ]
                    ))

        # Inventory growth exceeding sales growth
        if revenue_prior > 0 and inventory_prior > 0:
            revenue_growth = ((revenue_current - revenue_prior) / revenue_prior) * 100
            inventory_growth = ((inventory_current - inventory_prior) / inventory_prior) * 100

            if inventory_growth > revenue_growth + 10 and inventory_growth > 15:
                self.findings.append(RedFlagFinding(
                    category="Asset Quality",
                    severity="Medium",
                    title="Inventory Growing Faster Than Sales",
                    description=f"Inventory grew {inventory_growth:.1f}% while sales grew {revenue_growth:.1f}%. "
                                f"Excess inventory may indicate obsolescence or demand issues.",
                    metrics={
                        "Inventory_Growth_%": inventory_growth,
                        "Revenue_Growth_%": revenue_growth,
                        "Divergence_%": inventory_growth - revenue_growth
                    },
                    implications=[
                        "Potential inventory obsolescence",
                        "Overproduction or demand forecasting errors",
                        "Future inventory write-downs possible",
                        "Inadequate inventory reserves",
                        "Inefficient supply chain management"
                    ],
                    recommendations=[
                        "Review inventory aging and turnover ratios",
                        "Assess inventory reserve adequacy",
                        "Investigate industry demand trends",
                        "Check for changes in product mix",
                        "Examine inventory costing methods"
                    ]
                ))

    def analyze_earnings_quality(self, financial_data: List[Dict]) -> None:
        """Analyze overall earnings quality indicators."""
        if len(financial_data) < 3:
            return

        # Check for earnings volatility or smoothing
        net_incomes = [year.get("NetIncome", 0) for year in financial_data[:5]]
        operating_cfs = [year.get("OperatingCashFlow", 0) for year in financial_data[:5]]

        if len(net_incomes) >= 3 and len(operating_cfs) >= 3:
            # Calculate variability
            ni_values = [ni for ni in net_incomes if ni != 0]
            cf_values = [cf for cf in operating_cfs if cf != 0]

            if len(ni_values) >= 3 and len(cf_values) >= 3:
                ni_avg = sum(ni_values) / len(ni_values)
                cf_avg = sum(cf_values) / len(cf_values)

                # Coefficient of variation
                ni_std = (sum((x - ni_avg) ** 2 for x in ni_values) / len(ni_values)) ** 0.5
                cf_std = (sum((x - cf_avg) ** 2 for x in cf_values) / len(cf_values)) ** 0.5

                if ni_avg != 0 and cf_avg != 0:
                    ni_cv = ni_std / abs(ni_avg)
                    cf_cv = cf_std / abs(cf_avg)

                    # If earnings much less volatile than cash flows, potential smoothing
                    if cf_cv > 0.3 and ni_cv < cf_cv * 0.5:
                        self.findings.append(RedFlagFinding(
                            category="Earnings Quality",
                            severity="Medium",
                            title="Potential Earnings Smoothing",
                            description="Net income is significantly less volatile than operating cash flow, "
                                      "suggesting possible earnings management through smoothing.",
                            metrics={
                                "NI_Coefficient_of_Variation": ni_cv,
                                "CF_Coefficient_of_Variation": cf_cv,
                                "Ratio": cf_cv / ni_cv if ni_cv > 0 else 0
                            },
                            implications=[
                                "Potential use of discretionary accruals",
                                "Cookie jar reserves being used",
                                "Earnings management to meet targets",
                                "Reduced earnings informativeness"
                            ],
                            recommendations=[
                                "Analyze discretionary accruals patterns",
                                "Review reserve account activity",
                                "Check for restructuring charges patterns",
                                "Compare volatility to industry peers"
                            ]
                        ))

    def analyze_asset_quality(self, financial_data: List[Dict]) -> None:
        """Analyze asset quality and composition."""
        if len(financial_data) < 2:
            return

        current = financial_data[0]
        prior = financial_data[1]

        total_assets_current = current.get("Assets", 0)
        total_assets_prior = prior.get("Assets", 0)
        ppe_current = current.get("PropertyPlantEquipment", 0)
        ppe_prior = prior.get("PropertyPlantEquipment", 0)
        current_assets_current = current.get("CurrentAssets", 0)
        current_assets_prior = prior.get("CurrentAssets", 0)

        if total_assets_current > 0 and total_assets_prior > 0:
            # Calculate "soft assets" (non-current, non-PPE)
            soft_assets_current = total_assets_current - current_assets_current - ppe_current
            soft_assets_prior = total_assets_prior - current_assets_prior - ppe_prior

            soft_assets_pct_current = (soft_assets_current / total_assets_current) * 100
            soft_assets_pct_prior = (soft_assets_prior / total_assets_prior) * 100

            pct_change = soft_assets_pct_current - soft_assets_pct_prior

            # Red flag if soft assets increasing as percentage
            if pct_change > 5 and soft_assets_pct_current > 20:
                self.findings.append(RedFlagFinding(
                    category="Asset Quality",
                    severity="Medium",
                    title="Increasing Proportion of Intangible/Soft Assets",
                    description=f"Soft assets (intangibles, goodwill, deferred charges) increased from "
                              f"{soft_assets_pct_prior:.1f}% to {soft_assets_pct_current:.1f}% of total assets. "
                              f"These assets are more subjective and easier to manipulate.",
                    metrics={
                        "Soft_Assets_%_Current": soft_assets_pct_current,
                        "Soft_Assets_%_Prior": soft_assets_pct_prior,
                        "Change_in_%": pct_change
                    },
                    implications=[
                        "Greater reliance on subjective valuations",
                        "Increased impairment risk",
                        "Asset values may be overstated",
                        "Lower tangible asset backing",
                        "Potential for aggressive capitalization"
                    ],
                    recommendations=[
                        "Review intangible asset composition",
                        "Assess goodwill impairment testing methodology",
                        "Examine capitalized costs (software, R&D, etc.)",
                        "Check deferred tax assets realizability",
                        "Compare asset quality to peers"
                    ]
                ))

    def analyze_debt_trends(self, financial_data: List[Dict]) -> None:
        """Analyze debt trends and leverage."""
        if len(financial_data) < 2:
            return

        current = financial_data[0]
        prior = financial_data[1]

        total_debt_current = current.get("Liabilities", 0)
        total_debt_prior = prior.get("Liabilities", 0)
        total_assets_current = current.get("Assets", 0)
        total_assets_prior = prior.get("Assets", 0)
        equity_current = current.get("StockholdersEquity", 0)
        equity_prior = prior.get("StockholdersEquity", 0)

        # Debt-to-equity ratio increasing significantly
        if equity_current > 0 and equity_prior > 0:
            de_ratio_current = total_debt_current / equity_current
            de_ratio_prior = total_debt_prior / equity_prior

            if de_ratio_prior > 0:
                de_change = ((de_ratio_current - de_ratio_prior) / de_ratio_prior) * 100

                if de_change > 20 and de_ratio_current > 1.5:
                    self.findings.append(RedFlagFinding(
                        category="Financial Risk",
                        severity="High",
                        title="Rapidly Increasing Leverage",
                        description=f"Debt-to-equity ratio increased {de_change:.1f}% from {de_ratio_prior:.2f} to {de_ratio_current:.2f}. "
                                  f"Rising leverage increases pressure to manipulate earnings.",
                        metrics={
                            "Debt_to_Equity_Current": de_ratio_current,
                            "Debt_to_Equity_Prior": de_ratio_prior,
                            "Change_%": de_change
                        },
                        implications=[
                            "Increased financial risk",
                            "Pressure to meet debt covenant requirements",
                            "Incentive to manipulate earnings or assets",
                            "Reduced financial flexibility",
                            "Higher probability of financial distress"
                        ],
                        recommendations=[
                            "Review debt covenants and compliance",
                            "Assess interest coverage ratios",
                            "Examine debt maturity schedule",
                            "Check for off-balance sheet financing",
                            "Evaluate refinancing risk"
                        ]
                    ))

    def analyze_margins(self, financial_data: List[Dict]) -> None:
        """Analyze margin trends and quality."""
        if len(financial_data) < 2:
            return

        current = financial_data[0]
        prior = financial_data[1]

        revenue_current = current.get("Revenues", 0)
        revenue_prior = prior.get("Revenues", 0)
        cogs_current = current.get("CostOfRevenue", 0)
        cogs_prior = prior.get("CostOfRevenue", 0)

        if revenue_current > 0 and revenue_prior > 0:
            gross_margin_current = ((revenue_current - cogs_current) / revenue_current) * 100
            gross_margin_prior = ((revenue_prior - cogs_prior) / revenue_prior) * 100

            margin_change = gross_margin_current - gross_margin_prior

            # Deteriorating gross margins
            if margin_change < -5:
                severity = "High" if margin_change < -10 else "Medium"
                self.findings.append(RedFlagFinding(
                    category="Profitability",
                    severity=severity,
                    title="Deteriorating Gross Margins",
                    description=f"Gross margin declined from {gross_margin_prior:.1f}% to {gross_margin_current:.1f}% "
                              f"(down {abs(margin_change):.1f} percentage points). This increases pressure to manipulate earnings.",
                    metrics={
                        "Gross_Margin_%_Current": gross_margin_current,
                        "Gross_Margin_%_Prior": gross_margin_prior,
                        "Change_in_ppts": margin_change
                    },
                    implications=[
                        "Weakening competitive position",
                        "Pricing pressure or cost increases",
                        "Increased motivation to manipulate earnings",
                        "May indicate business model stress",
                        "Future profitability concerns"
                    ],
                    recommendations=[
                        "Analyze cause of margin deterioration",
                        "Compare to industry and competitors",
                        "Review cost structure and efficiency",
                        "Assess pricing power",
                        "Examine product mix changes"
                    ]
                ))

    def get_severity_counts(self) -> Dict[str, int]:
        """Get counts of findings by severity."""
        counts = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0}
        for finding in self.findings:
            counts[finding.severity] = counts.get(finding.severity, 0) + 1
        return counts

    def get_category_counts(self) -> Dict[str, int]:
        """Get counts of findings by category."""
        counts = {}
        for finding in self.findings:
            counts[finding.category] = counts.get(finding.category, 0) + 1
        return counts
