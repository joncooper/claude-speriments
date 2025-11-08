"""
Forensic Accounting Report Generator

Generates professional forensic accounting reports suitable for presentation
to equity research analysts, investment committees, or compliance teams.
"""

from typing import Dict, List
from datetime import datetime


class ForensicAccountingReport:
    """
    Generate comprehensive forensic accounting reports.

    The report follows professional forensic accounting standards and
    includes executive summary, detailed findings, supporting analysis,
    and specific recommendations.
    """

    def __init__(self, analysis_results: Dict):
        """
        Initialize report generator with analysis results.

        Args:
            analysis_results: Complete analysis results from ForensicAccountingAnalyzer
        """
        self.results = analysis_results
        self.metadata = analysis_results.get("metadata", {})
        self.company_info = analysis_results.get("company_info", {})
        self.beneish_scores = analysis_results.get("beneish_scores", [])
        self.red_flags = analysis_results.get("red_flags", [])
        self.trends = analysis_results.get("trends", {})
        self.assessment = analysis_results.get("assessment", {})

    def generate_markdown_report(self) -> str:
        """
        Generate complete forensic accounting report in markdown format.

        Returns:
            Formatted markdown report string
        """
        sections = [
            self._generate_cover_page(),
            self._generate_executive_summary(),
            self._generate_company_overview(),
            self._generate_beneish_analysis(),
            self._generate_red_flags_section(),
            self._generate_trend_analysis(),
            self._generate_detailed_findings(),
            self._generate_recommendations(),
            self._generate_methodology(),
            self._generate_limitations()
        ]

        return "\n\n".join(sections)

    def _generate_cover_page(self) -> str:
        """Generate report cover page."""
        return f"""# FORENSIC ACCOUNTING REPORT

## {self.metadata.get('company_name', 'Unknown Company')}
### Ticker: {self.metadata.get('ticker', 'N/A')}

---

**Report Type:** Forensic Accounting Assessment - Accounting Policy Aggressiveness Analysis

**Report Date:** {datetime.now().strftime('%B %d, %Y')}

**Analysis Period:** {self.metadata.get('years_analyzed', 'N/A')} years of historical financial statements

**Prepared For:** Equity Research / Investment Analysis

**Confidentiality:** This report contains proprietary analysis and should be treated as confidential.

---

## OVERALL ASSESSMENT

**Risk Level:** `{self.assessment.get('risk_level', 'UNKNOWN')}`

**Risk Score:** {self.assessment.get('risk_score', 0)}/100

**Recommendation:** {self.assessment.get('recommendation', 'N/A')}

---
"""

    def _generate_executive_summary(self) -> str:
        """Generate executive summary section."""
        risk_level = self.assessment.get('risk_level', 'UNKNOWN')
        total_flags = self.assessment.get('total_red_flags', 0)
        critical_flags = self.assessment.get('critical_red_flags', 0)
        high_flags = self.assessment.get('high_red_flags', 0)

        # Get latest Beneish score
        latest_beneish = "N/A"
        if self.beneish_scores:
            latest_beneish = f"{self.beneish_scores[0]['m_score']:.3f}"

        summary = f"""## EXECUTIVE SUMMARY

This forensic accounting analysis examines the accounting policies and financial reporting quality of **{self.company_info.get('name', 'the Company')}** ({self.metadata.get('ticker', 'N/A')}) to assess the aggressiveness of their accounting practices and identify potential areas of earnings manipulation.

### Key Findings

**Overall Risk Assessment:** {risk_level}

Based on our comprehensive analysis, the company's financial reporting exhibits a **{risk_level}** risk level for aggressive accounting or earnings manipulation.

### Critical Metrics

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **Beneish M-Score (Latest)** | {latest_beneish} | {"**Above threshold** - High manipulation risk" if self.beneish_scores and self.beneish_scores[0]['m_score'] > -2.22 else "Below threshold"} |
| **Total Red Flags Identified** | {total_flags} | {self._interpret_flag_count(total_flags)} |
| **Critical Severity Flags** | {critical_flags} | {"**Immediate attention required**" if critical_flags > 0 else "None identified"} |
| **High Severity Flags** | {high_flags} | {"**Significant concerns**" if high_flags > 0 else "None identified"} |

### Primary Concerns

"""

        # Add top risk factors
        risk_factors = self.assessment.get('risk_factors', [])
        if risk_factors:
            for i, factor in enumerate(risk_factors[:5], 1):
                summary += f"{i}. {factor}\n"
        else:
            summary += "No significant concerns identified.\n"

        summary += f"""
### Recommendation

{self.assessment.get('recommendation', 'N/A')}

"""

        return summary

    def _generate_company_overview(self) -> str:
        """Generate company overview section."""
        return f"""## COMPANY OVERVIEW

**Legal Name:** {self.company_info.get('name', 'Unknown')}

**Stock Ticker:** {self.metadata.get('ticker', 'N/A')}

**CIK (SEC Identifier):** {self.company_info.get('cik', 'Unknown')}

**Industry:** {self.company_info.get('sicDescription', 'Unknown')}

**SIC Code:** {self.company_info.get('sic', 'Unknown')}

**Analysis Period:** {self.metadata.get('years_analyzed', 'N/A')} fiscal years

**Data Source:** SEC EDGAR database (10-K and 10-K/A filings)

---
"""

    def _generate_beneish_analysis(self) -> str:
        """Generate Beneish M-Score analysis section."""
        section = """## BENEISH M-SCORE ANALYSIS

The Beneish M-Score is a mathematical model that uses financial ratios to detect earnings manipulation. Developed by Professor Messod Beneish, the model has approximately 76% accuracy in identifying companies engaging in earnings manipulation.

**Interpretation Thresholds:**
- Score > -1.78: Very High Risk - Strong indication of manipulation
- Score > -2.22: High Risk - Significant red flags present
- Score < -2.22: Lower Risk - Within normal parameters

### Historical M-Scores

"""

        if not self.beneish_scores:
            section += "*Insufficient data to calculate Beneish M-Scores.*\n"
            return section

        # Create table of M-Scores
        section += "| Period | M-Score | Risk Level | Status |\n"
        section += "|--------|---------|------------|--------|\n"

        for result in self.beneish_scores:
            period = result.get('period', 'Unknown')
            score = result.get('m_score', 0)
            interp = result.get('interpretation', {})
            risk_level = interp.get('risk_level', 'Unknown')
            is_manipulator = interp.get('is_likely_manipulator', False)
            status = "🔴 **MANIPULATOR**" if is_manipulator else "✓ Non-manipulator"

            section += f"| {period} | {score:.3f} | {risk_level} | {status} |\n"

        # Add trend analysis
        if len(self.beneish_scores) > 1:
            section += "\n### M-Score Trend\n\n"
            trend = self.trends.get('m_score_trend', {})

            if trend.get('is_deteriorating', False):
                section += f"⚠️ **DETERIORATING**: The M-Score has worsened from {trend.get('oldest', 0):.3f} to {trend.get('latest', 0):.3f}, "
                section += f"increasing by {trend.get('change', 0):.3f} points. This indicates accounting policies are becoming MORE aggressive over time.\n"
            else:
                section += f"✓ **IMPROVING**: The M-Score has improved from {trend.get('oldest', 0):.3f} to {trend.get('latest', 0):.3f}. "
                section += "This suggests more conservative accounting practices.\n"

        # Add detailed variable analysis for latest period
        section += "\n### Detailed Variable Analysis (Latest Period)\n\n"

        if self.beneish_scores:
            latest = self.beneish_scores[0]
            variables = latest.get('variables', {})
            variable_flags = latest.get('variable_flags', [])

            section += "The Beneish M-Score is calculated from 8 financial ratio indices:\n\n"
            section += "| Variable | Value | Threshold | Status |\n"
            section += "|----------|-------|-----------|--------|\n"

            variable_thresholds = {
                "DSRI": 1.031,
                "GMI": 1.014,
                "AQI": 1.039,
                "SGI": 1.134,
                "DEPI": 1.001,
                "SGAI": 1.001,
                "TATA": 0.018,
                "LVGI": 1.037
            }

            for var_name, var_value in variables.items():
                threshold = variable_thresholds.get(var_name, 1.0)
                is_concerning = (var_value > threshold) if var_name != "SGAI" else (var_value > threshold)
                status = "⚠️ **Concerning**" if is_concerning else "✓ Normal"
                section += f"| {var_name} | {var_value:.3f} | {threshold} | {status} |\n"

            # Add explanations for concerning variables
            if variable_flags:
                section += "\n### Red Flags from Variable Analysis\n\n"
                for flag in variable_flags:
                    section += f"#### {flag['variable']}: {flag['concern']}\n\n"
                    section += f"**Value:** {flag['value']:.3f} (Threshold: {flag['threshold']})\n\n"
                    section += "**Implications:**\n"
                    for impl in flag['implications']:
                        section += f"- {impl}\n"
                    section += "\n"

        section += "\n---\n"
        return section

    def _generate_red_flags_section(self) -> str:
        """Generate red flags summary section."""
        section = """## RED FLAG ANALYSIS

The following red flags were identified through detailed analysis of financial statement trends, ratios, and quality metrics.

"""

        if not self.red_flags:
            section += "*No significant red flags identified.*\n\n"
            return section

        # Group by severity
        by_severity = {"Critical": [], "High": [], "Medium": [], "Low": []}
        for flag in self.red_flags:
            severity = flag.get('severity', 'Low')
            by_severity[severity].append(flag)

        # Summary table
        section += "### Red Flag Summary\n\n"
        section += "| Severity | Count | Requires Action |\n"
        section += "|----------|-------|----------------|\n"
        section += f"| 🔴 Critical | {len(by_severity['Critical'])} | Immediate investigation |\n"
        section += f"| 🟠 High | {len(by_severity['High'])} | Detailed review |\n"
        section += f"| 🟡 Medium | {len(by_severity['Medium'])} | Enhanced monitoring |\n"
        section += f"| 🟢 Low | {len(by_severity['Low'])} | Standard due diligence |\n\n"

        # Group by category for overview
        by_category = {}
        for flag in self.red_flags:
            category = flag.get('category', 'Other')
            by_category[category] = by_category.get(category, 0) + 1

        section += "### Red Flags by Category\n\n"
        for category, count in sorted(by_category.items(), key=lambda x: x[1], reverse=True):
            section += f"- **{category}**: {count} finding(s)\n"

        section += "\n---\n"
        return section

    def _generate_trend_analysis(self) -> str:
        """Generate trend analysis section."""
        section = """## TREND ANALYSIS

Analysis of key financial metrics over time to identify patterns of improvement or deterioration.

"""

        # Revenue trend
        rev_trend = self.trends.get('revenue_growth', {})
        if rev_trend:
            section += "### Revenue Growth\n\n"
            section += f"- **Latest Growth Rate:** {rev_trend.get('latest_rate_%', 0):.1f}%\n"
            section += f"- **Average Growth Rate:** {rev_trend.get('average_rate_%', 0):.1f}%\n"
            direction = "Accelerating" if rev_trend.get('is_accelerating', False) else "Decelerating"
            section += f"- **Trend:** {direction}\n\n"

        # Margin trend
        margin_trend = self.trends.get('profit_margin', {})
        if margin_trend:
            section += "### Profit Margins\n\n"
            section += f"- **Latest Margin:** {margin_trend.get('latest_%', 0):.1f}%\n"
            section += f"- **Average Margin:** {margin_trend.get('average_%', 0):.1f}%\n"
            direction = "Improving" if margin_trend.get('is_improving', False) else "Deteriorating"
            emoji = "✓" if margin_trend.get('is_improving', False) else "⚠️"
            section += f"- **Trend:** {emoji} {direction}\n\n"

        # Cash flow quality
        cf_trend = self.trends.get('cash_flow_quality', {})
        if cf_trend:
            section += "### Cash Flow Quality\n\n"
            ratio = cf_trend.get('cf_to_ni_ratio', 0)
            section += f"- **Operating CF / Net Income Ratio:** {ratio:.2f}\n"

            if ratio > 1.0:
                assessment = "✓ **Excellent** - Cash generation exceeds reported earnings"
            elif ratio > 0.8:
                assessment = "✓ **Good** - Cash closely tracks earnings"
            elif ratio > 0.5:
                assessment = "⚠️ **Moderate Concern** - Earnings not fully converting to cash"
            else:
                assessment = "🔴 **Serious Concern** - Significant gap between earnings and cash"

            section += f"- **Assessment:** {assessment}\n\n"

        section += "---\n"
        return section

    def _generate_detailed_findings(self) -> str:
        """Generate detailed findings section."""
        section = """## DETAILED FINDINGS

This section provides comprehensive details on each identified red flag, including specific metrics, implications, and recommended actions.

"""

        if not self.red_flags:
            section += "*No red flags to detail.*\n\n"
            return section

        # Group by severity and detail each
        by_severity = {"Critical": [], "High": [], "Medium": [], "Low": []}
        for flag in self.red_flags:
            severity = flag.get('severity', 'Low')
            by_severity[severity].append(flag)

        finding_num = 1

        for severity in ["Critical", "High", "Medium", "Low"]:
            flags = by_severity[severity]
            if not flags:
                continue

            severity_emoji = {
                "Critical": "🔴",
                "High": "🟠",
                "Medium": "🟡",
                "Low": "🟢"
            }

            section += f"\n### {severity_emoji[severity]} {severity} Severity Findings\n\n"

            for flag in flags:
                section += f"#### Finding #{finding_num}: {flag['title']}\n\n"
                section += f"**Category:** {flag['category']}\n\n"
                section += f"**Description:**\n{flag['description']}\n\n"

                # Metrics
                if flag.get('metrics'):
                    section += "**Key Metrics:**\n\n"
                    section += "| Metric | Value |\n"
                    section += "|--------|-------|\n"
                    for metric_name, metric_value in flag['metrics'].items():
                        formatted_value = f"{metric_value:,.2f}" if isinstance(metric_value, (int, float)) else str(metric_value)
                        section += f"| {metric_name} | {formatted_value} |\n"
                    section += "\n"

                # Implications
                if flag.get('implications'):
                    section += "**Implications:**\n\n"
                    for impl in flag['implications']:
                        section += f"- {impl}\n"
                    section += "\n"

                # Recommendations
                if flag.get('recommendations'):
                    section += "**Recommended Actions:**\n\n"
                    for rec in flag['recommendations']:
                        section += f"- {rec}\n"
                    section += "\n"

                section += "---\n\n"
                finding_num += 1

        return section

    def _generate_recommendations(self) -> str:
        """Generate recommendations section."""
        risk_level = self.assessment.get('risk_level', 'UNKNOWN')

        section = f"""## RECOMMENDATIONS

Based on the {risk_level} risk assessment, we recommend the following actions:

### Immediate Actions

"""

        # Tailor recommendations based on risk level
        if risk_level == "VERY HIGH" or risk_level == "HIGH":
            section += """1. **Initiate Detailed Forensic Investigation**
   - Engage external forensic accounting specialists
   - Conduct detailed testing of revenue recognition practices
   - Perform substantive procedures on key balance sheet accounts
   - Review management compensation structures and incentives

2. **Enhanced Due Diligence**
   - Request management discussions on accounting policy choices
   - Obtain detailed sub-ledger data for suspicious accounts
   - Interview key accounting personnel
   - Review Board Audit Committee minutes

3. **Independent Verification**
   - Confirm major transactions with counterparties
   - Physically verify existence of material assets
   - Independently contact major customers and suppliers
   - Review subsequent events and cash receipts

"""
        elif risk_level == "MODERATE":
            section += """1. **Targeted Investigation**
   - Focus detailed testing on areas with identified red flags
   - Request management explanations for concerning trends
   - Perform analytical procedures on key metrics
   - Review accounting policy disclosures in detail

2. **Enhanced Monitoring**
   - Establish quarterly monitoring of key risk indicators
   - Track trends in concerning ratios
   - Monitor cash flow patterns
   - Watch for accounting policy changes

"""
        else:  # LOW risk
            section += """1. **Standard Due Diligence**
   - Maintain normal audit and review procedures
   - Continue quarterly monitoring of key metrics
   - Review significant accounting policy changes
   - Monitor for emerging risk factors

2. **Periodic Reassessment**
   - Repeat forensic analysis annually
   - Stay alert for changes in risk profile
   - Monitor industry and peer trends

"""

        section += """### Ongoing Monitoring

Regardless of current risk level, implement continuous monitoring of:

- **Beneish M-Score**: Calculate quarterly and track trends
- **Cash Flow Quality**: Monitor operating CF to net income ratio
- **Working Capital Metrics**: Track DSO, inventory turnover, DPO
- **Accounting Policy Changes**: Review all changes and assess impact
- **Management Commentary**: Analyze MD&A for signs of stress or pressure
- **Audit Committee Communications**: Review for indications of disputes or issues

### Documentation Requirements

Maintain comprehensive documentation of:

- All analyses performed and conclusions reached
- Management representations and explanations obtained
- Independent verification procedures conducted
- Ongoing monitoring results and any changes in assessment

---
"""

        return section

    def _generate_methodology(self) -> str:
        """Generate methodology section."""
        return """## METHODOLOGY

This forensic accounting analysis employs multiple established methodologies and frameworks used by experienced forensic accountants and fraud examiners.

### Data Sources

- **Primary Source:** SEC EDGAR database
- **Filing Types Analyzed:** 10-K, 10-K/A (Annual Reports)
- **Data Format:** XBRL-tagged financial statements
- **Analysis Period:** Multi-year historical data

### Analytical Frameworks

#### 1. Beneish M-Score Model

The Beneish M-Score is a mathematical model that uses eight financial ratios to identify companies likely engaging in earnings manipulation. The model was developed by Professor Messod Beneish through analysis of known financial statement manipulators.

**Variables:**
- DSRI: Days Sales in Receivables Index
- GMI: Gross Margin Index
- AQI: Asset Quality Index
- SGI: Sales Growth Index
- DEPI: Depreciation Index
- SGAI: SG&A Expense Index
- TATA: Total Accruals to Total Assets
- LVGI: Leverage Index

**Threshold:** M-Score > -2.22 indicates high likelihood of manipulation

**Accuracy:** Approximately 76% in detecting manipulators (with 17.5% false positive rate)

#### 2. Red Flag Analysis

Comprehensive review of financial statement quality indicators including:

- **Revenue Quality:** DSO trends, revenue/AR growth divergence
- **Earnings Quality:** Cash flow to earnings ratios, accruals analysis
- **Working Capital:** Current ratio, inventory trends
- **Asset Quality:** Composition analysis, soft asset proportion
- **Debt and Leverage:** Debt trends, covenant pressure indicators
- **Margin Analysis:** Gross margin trends, profitability patterns

#### 3. Trend Analysis

Multi-year analysis of:
- M-Score progression (improving or deteriorating)
- Revenue growth patterns and sustainability
- Profit margin trends
- Cash flow generation quality
- Balance sheet composition changes

### Professional Standards

This analysis follows principles consistent with:
- ACFE (Association of Certified Fraud Examiners) standards
- AICPA forensic accounting guidelines
- CFA Institute financial analysis frameworks

---
"""

    def _generate_limitations(self) -> str:
        """Generate limitations section."""
        return """## LIMITATIONS AND DISCLAIMERS

### Scope Limitations

1. **Public Information Only**
   - Analysis based solely on publicly-filed SEC documents
   - No access to internal records, systems, or personnel
   - Limited to information management chooses to disclose

2. **Historical Data**
   - Analysis based on past financial statements
   - Does not predict future manipulation or guarantee detection
   - Current period activities not yet reported may differ

3. **Model Limitations**
   - Beneish M-Score has ~76% accuracy with ~17.5% false positive rate
   - Not all manipulation is detectable through quantitative analysis
   - Sophisticated schemes may evade statistical detection

4. **Industry and Context**
   - Industry-specific factors may affect ratios and metrics
   - Business model differences can impact normal ranges
   - Growth stage and lifecycle considerations not fully captured

### Important Disclaimers

**This report does not:**
- Constitute an audit or review under professional auditing standards
- Provide absolute certainty regarding presence or absence of manipulation
- Replace need for detailed forensic investigation if serious concerns exist
- Offer investment advice or recommendations regarding the company's securities

**This report should:**
- Be used as a screening and risk assessment tool
- Inform decisions about whether deeper investigation is warranted
- Be considered alongside other due diligence activities
- Be updated regularly as new financial information becomes available

### Professional Judgment Required

The findings and risk assessments in this report require interpretation by qualified professionals with:
- Understanding of accounting principles and practices
- Knowledge of the specific industry and business model
- Experience in forensic accounting and fraud detection
- Context regarding the company's history and circumstances

**No automated analysis can substitute for experienced professional judgment in forensic accounting matters.**

---

## APPENDICES

### Appendix A: Variable Definitions

Detailed definitions of all Beneish M-Score variables and thresholds.

### Appendix B: Red Flag Taxonomy

Complete taxonomy of accounting red flags analyzed in this assessment.

### Appendix C: Data Tables

Complete financial data tables used in the analysis.

---

**END OF REPORT**

---

*This report was generated using automated forensic accounting analysis tools. All findings should be reviewed and validated by qualified forensic accounting professionals before making material decisions.*

*Report Generation Date: {datetime.now().strftime('%B %d, %Y at %H:%M UTC')}*
"""

    def _interpret_flag_count(self, count: int) -> str:
        """Interpret the red flag count."""
        if count == 0:
            return "Clean financial reporting"
        elif count <= 3:
            return "Some areas warrant attention"
        elif count <= 6:
            return "Multiple concerning areas"
        else:
            return "Significant concerns across multiple areas"

    def save_report(self, filepath: str) -> None:
        """
        Save the generated report to a file.

        Args:
            filepath: Path to save the markdown report
        """
        report = self.generate_markdown_report()

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report)

        print(f"Report saved to {filepath}")


def generate_report(analysis_results: Dict, output_path: str) -> None:
    """
    Convenience function to generate and save a report.

    Args:
        analysis_results: Complete analysis results dictionary
        output_path: Path to save the report
    """
    report = ForensicAccountingReport(analysis_results)
    report.save_report(output_path)
