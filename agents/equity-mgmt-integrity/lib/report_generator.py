"""
Report Generator

Professional markdown report generation for management integrity analysis.
Creates comprehensive reports suitable for equity research analysts.
"""

from typing import Dict, List
from datetime import datetime
import os


class ManagementIntegrityReport:
    """
    Generates professional markdown reports for management integrity analysis.

    Reports include:
    - Executive summary with score and grade
    - Category performance breakdown
    - Time trends
    - Red flags (if any)
    - Notable successes and misses
    - Detailed findings with evidence
    - Methodology and limitations
    """

    def __init__(self, results: Dict):
        """
        Initialize report generator.

        Args:
            results: Complete analysis results containing:
                - company_info: Company metadata
                - commitments: List of commitments
                - outcomes: List of outcomes
                - score: Credibility score dictionary
        """
        self.results = results
        self.company_info = results['company_info']
        self.commitments = results['commitments']
        self.outcomes = results['outcomes']
        self.score = results['score']

        # Create outcome lookup
        self.outcome_lookup = {o['commitment_id']: o for o in self.outcomes}

    def generate_markdown(self) -> str:
        """
        Generate complete markdown report.

        Returns:
            Full markdown report as string
        """
        sections = [
            self._generate_header(),
            self._generate_executive_summary(),
            self._generate_company_overview(),
            self._generate_credibility_score_details(),
            self._generate_category_breakdown(),
            self._generate_time_trends(),
            self._generate_red_flags(),
            self._generate_notable_successes(),
            self._generate_notable_misses(),
            self._generate_detailed_findings(),
            self._generate_methodology(),
            self._generate_limitations(),
        ]

        return "\n\n".join(sections)

    def save_report(self, filepath: str) -> None:
        """
        Generate and save report to file.

        Args:
            filepath: Path to save the markdown report
        """
        report = self.generate_markdown()

        # Create directory if needed
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'w') as f:
            f.write(report)

    def generate_summary(self) -> str:
        """
        Generate concise terminal summary.

        Returns:
            Short summary suitable for console output
        """
        score = self.score
        company = self.company_info['name']
        ticker = self.company_info['ticker']

        # Risk assessment
        if score['overall_score'] >= 75:
            risk = "LOW"
        elif score['overall_score'] >= 60:
            risk = "MODERATE"
        elif score['overall_score'] >= 40:
            risk = "HIGH"
        else:
            risk = "VERY HIGH"

        summary = f"""
MANAGEMENT INTEGRITY ANALYSIS: {ticker}
{'=' * 80}

Company: {company}
Analysis Date: {datetime.now().strftime('%B %d, %Y')}
Commitments Analyzed: {score['verifiable_commitments']}

OVERALL CREDIBILITY SCORE: {score['overall_score']}/100 ({score['grade']})
RISK ASSESSMENT: {risk}

KEY METRICS:
- Fulfilled: {score['fulfilled_count']} ({score['fulfillment_rate']:.1f}%)
- Partially Fulfilled: {score['partially_fulfilled_count']} ({score['partial_rate']:.1f}%)
- Not Fulfilled: {score['not_fulfilled_count'] + score['abandoned_count']} ({score['miss_rate']:.1f}%)

TIME TREND: {score['time_trends']['description']}

RED FLAGS: {len(score['red_flags'])} identified
"""

        if score['red_flags']:
            summary += "\nMOST CRITICAL CONCERNS:\n"
            for flag in score['red_flags'][:3]:
                summary += f"- {flag['description']}\n"

        return summary

    def _generate_header(self) -> str:
        """Generate report header."""
        return f"""# Management Integrity Analysis
## {self.company_info['name']} ({self.company_info['ticker']})

**Analysis Date:** {datetime.now().strftime('%B %d, %Y')}
**Analyst:** Management Integrity Agent v1.0
**Report Type:** Management Credibility Assessment

---"""

    def _generate_executive_summary(self) -> str:
        """Generate executive summary section."""
        score = self.score

        # Overall assessment
        if score['overall_score'] >= 75:
            assessment = "Management demonstrates strong credibility with a high fulfillment rate."
        elif score['overall_score'] >= 60:
            assessment = "Management shows moderate credibility with some misses."
        elif score['overall_score'] >= 40:
            assessment = "Management credibility is concerning with significant unfulfilled commitments."
        else:
            assessment = "Management credibility is very poor with pattern of broken promises."

        summary = f"""## Executive Summary

**Overall Credibility Score:** {score['overall_score']}/100 ({score['grade']})

{assessment}

### Key Findings

- **Total Commitments Analyzed:** {score['verifiable_commitments']}
- **Fulfillment Rate:** {score['fulfillment_rate']:.1f}% ({score['fulfilled_count']} of {score['verifiable_commitments']})
- **Partial Fulfillment Rate:** {score['partial_rate']:.1f}% ({score['partially_fulfilled_count']} of {score['verifiable_commitments']})
- **Miss Rate:** {score['miss_rate']:.1f}% ({score['not_fulfilled_count'] + score['abandoned_count']} of {score['verifiable_commitments']})
- **Commitment Quality (Specificity Index):** {score['specificity_index']}/10

### Trend Assessment

{score['time_trends']['description']}"""

        return summary

    def _generate_company_overview(self) -> str:
        """Generate company overview section."""
        return f"""## Company Overview

**Company Name:** {self.company_info['name']}
**Ticker:** {self.company_info['ticker']}
**CIK:** {self.company_info.get('cik', 'N/A')}

### Analysis Scope

This analysis examines management commitments made in SEC filings (10-K and 10-Q reports) over the past 3 years and verifies whether management followed through on their promises."""

    def _generate_credibility_score_details(self) -> str:
        """Generate detailed credibility score explanation."""
        score = self.score

        return f"""## Credibility Score Details

### Scoring Methodology

The Management Integrity Score is calculated as:

```
Score = (Fulfilled + 0.5 × Partially Fulfilled) / Total Verifiable × 100
Score = ({score['fulfilled_count']} + 0.5 × {score['partially_fulfilled_count']}) / {score['verifiable_commitments']} × 100
Score = {score['overall_score']}/100
```

### Grade: {score['grade']}

| Score Range | Grade | Description |
|-------------|-------|-------------|
| 90-100 | A+/A | Excellent - Management consistently delivers |
| 75-89 | B+/B/B- | Good - Management generally reliable |
| 60-74 | C+/C/C- | Fair - Mixed track record |
| 40-59 | D+/D/D- | Poor - Significant credibility issues |
| 0-39 | F | Failing - Pattern of broken promises |

### Outcome Breakdown

| Status | Count | Percentage |
|--------|-------|------------|
| ✅ Fulfilled | {score['fulfilled_count']} | {score['fulfillment_rate']:.1f}% |
| ⚠️ Partially Fulfilled | {score['partially_fulfilled_count']} | {score['partial_rate']:.1f}% |
| ❌ Not Fulfilled | {score['not_fulfilled_count']} | {(score['not_fulfilled_count'] / score['verifiable_commitments'] * 100) if score['verifiable_commitments'] > 0 else 0:.1f}% |
| 🚫 Abandoned | {score['abandoned_count']} | {(score['abandoned_count'] / score['verifiable_commitments'] * 100) if score['verifiable_commitments'] > 0 else 0:.1f}% |
| ⏳ Pending | {score['pending_count']} | - |"""

    def _generate_category_breakdown(self) -> str:
        """Generate category performance breakdown."""
        if not self.score['category_scores']:
            return "## Category Performance\n\nInsufficient data for category breakdown."

        section = "## Category Performance Breakdown\n\n"
        section += "Management performance varies by commitment type:\n\n"
        section += "| Category | Score | Fulfilled | Partial | Missed | Total |\n"
        section += "|----------|-------|-----------|---------|--------|---------|\n"

        for category, stats in self.score['category_scores'].items():
            category_name = category.replace('_', ' ').title()
            section += f"| {category_name} | {stats['score']:.1f} | {stats['fulfilled']} | {stats['partial']} | {stats['missed']} | {stats['count']} |\n"

        # Identify best and worst categories
        sorted_categories = sorted(
            self.score['category_scores'].items(),
            key=lambda x: x[1]['score'],
            reverse=True
        )

        if sorted_categories:
            best_category = sorted_categories[0]
            worst_category = sorted_categories[-1]

            section += f"\n**Best Performance:** {best_category[0].replace('_', ' ').title()} ({best_category[1]['score']:.1f})\n"
            section += f"**Weakest Performance:** {worst_category[0].replace('_', ' ').title()} ({worst_category[1]['score']:.1f})\n"

        return section

    def _generate_time_trends(self) -> str:
        """Generate time trends section."""
        trends = self.score['time_trends']

        section = "## Time Trends\n\n"

        if trends['trend'] == 'insufficient_data':
            section += trends['description']
        elif trends['trend'] == 'improving':
            section += f"📈 **Management credibility is IMPROVING over time.**\n\n"
            section += f"- Early Period Score: {trends['early_score']:.1f}\n"
            section += f"- Late Period Score: {trends['late_score']:.1f}\n"
            section += f"- Change: +{trends['change']:.1f} points\n\n"
            section += "This positive trend suggests management is learning from past misses and becoming more reliable."
        elif trends['trend'] == 'declining':
            section += f"📉 **Management credibility is DECLINING over time.**\n\n"
            section += f"- Early Period Score: {trends['early_score']:.1f}\n"
            section += f"- Late Period Score: {trends['late_score']:.1f}\n"
            section += f"- Change: {trends['change']:.1f} points\n\n"
            section += "⚠️ **WARNING:** Declining credibility is a significant red flag for investors."
        else:
            section += f"➡️ **Management credibility is STABLE.**\n\n"
            section += f"- Score has remained around {trends['early_score']:.1f} consistently."

        return section

    def _generate_red_flags(self) -> str:
        """Generate red flags section."""
        red_flags = self.score['red_flags']

        if not red_flags:
            return "## Red Flags\n\n✅ **No significant red flags identified.**\n\nManagement appears to be delivering on commitments consistently."

        section = "## Red Flags\n\n"
        section += f"⚠️ **{len(red_flags)} concerning patterns identified:**\n\n"

        for i, flag in enumerate(red_flags, 1):
            severity_emoji = "🔴" if flag['severity'] == 'high' else "🟡"
            section += f"{i}. {severity_emoji} **{flag['description']}**\n"
            section += f"   - Type: {flag['type'].replace('_', ' ').title()}\n"
            section += f"   - Severity: {flag['severity'].upper()}\n\n"

        return section

    def _generate_notable_successes(self) -> str:
        """Generate notable successes section."""
        # Find top fulfilled commitments
        fulfilled = [
            (c, self.outcome_lookup[c['commitment_id']])
            for c in self.commitments
            if c['commitment_id'] in self.outcome_lookup
            and self.outcome_lookup[c['commitment_id']]['status'] == 'fulfilled'
        ]

        if not fulfilled:
            return "## Notable Successes\n\nNo fulfilled commitments to highlight."

        # Sort by specificity (highest quality commitments)
        fulfilled.sort(key=lambda x: x[0]['specificity'], reverse=True)

        section = "## Notable Successes\n\n"
        section += "Management delivered on these key commitments:\n\n"

        for i, (commitment, outcome) in enumerate(fulfilled[:5], 1):
            section += f"### {i}. {commitment['metric'].title()}\n\n"
            section += f"**Commitment:** \"{commitment['commitment_text']}\"\n\n"
            section += f"**Category:** {commitment['category'].replace('_', ' ').title()}\n"
            section += f"**Timeline:** {commitment['timeline']}\n"

            if 'variance' in outcome:
                section += f"**Result:** Target exceeded by {outcome['variance']:.1f}%\n"
            else:
                section += f"**Result:** ✅ Fulfilled\n"

            section += f"**Evidence:** {outcome.get('evidence', 'See verification filing')[:200]}...\n\n"

        return section

    def _generate_notable_misses(self) -> str:
        """Generate notable misses section."""
        # Find commitments that were not fulfilled or abandoned
        misses = [
            (c, self.outcome_lookup[c['commitment_id']])
            for c in self.commitments
            if c['commitment_id'] in self.outcome_lookup
            and self.outcome_lookup[c['commitment_id']]['status'] in ['not_fulfilled', 'abandoned']
        ]

        if not misses:
            return "## Notable Misses\n\n✅ No significant misses identified."

        section = "## Notable Misses\n\n"
        section += "⚠️ Management failed to deliver on these commitments:\n\n"

        for i, (commitment, outcome) in enumerate(misses[:5], 1):
            status_emoji = "🚫" if outcome['status'] == 'abandoned' else "❌"
            section += f"### {i}. {status_emoji} {commitment['metric'].title()}\n\n"
            section += f"**Commitment:** \"{commitment['commitment_text']}\"\n\n"
            section += f"**Category:** {commitment['category'].replace('_', ' ').title()}\n"
            section += f"**Timeline:** {commitment['timeline']}\n"
            section += f"**Status:** {outcome['status'].replace('_', ' ').title()}\n"

            if 'variance' in outcome:
                section += f"**Shortfall:** Missed by {abs(outcome['variance']):.1f}%\n"

            section += f"**Explanation:** {outcome['explanation']}\n\n"

        return section

    def _generate_detailed_findings(self) -> str:
        """Generate detailed findings section."""
        section = "## Detailed Findings\n\n"
        section += "Complete list of all commitments and their outcomes:\n\n"

        # Group by status
        by_status = {}
        for commitment in self.commitments:
            if commitment['commitment_id'] in self.outcome_lookup:
                outcome = self.outcome_lookup[commitment['commitment_id']]
                status = outcome['status']
                if status not in by_status:
                    by_status[status] = []
                by_status[status].append((commitment, outcome))

        # Output each status group
        status_order = ['fulfilled', 'partially_fulfilled', 'not_fulfilled', 'abandoned', 'pending']
        for status in status_order:
            if status in by_status:
                section += f"### {status.replace('_', ' ').title()} ({len(by_status[status])})\n\n"

                for commitment, outcome in by_status[status]:
                    section += f"- **{commitment['metric'].title()}**: {commitment['commitment_text'][:100]}...\n"
                    section += f"  - Filed: {commitment['source_filing']['filing_date']}\n"
                    section += f"  - Timeline: {commitment['timeline']}\n"
                    if 'variance' in outcome:
                        section += f"  - Variance: {outcome['variance']:.1f}%\n"
                    section += "\n"

        return section

    def _generate_methodology(self) -> str:
        """Generate methodology section."""
        return """## Methodology

This analysis uses a systematic approach to evaluate management credibility:

### 1. Commitment Extraction

Using AI-powered analysis, we scan SEC filings (10-K, 10-Q) for forward-looking commitments. Only specific, verifiable commitments are included:
- Must be concrete and measurable
- Must have a clear timeline
- Must be within management's control
- Specificity scored 1-10 (only 4+ included)

### 2. Outcome Verification

For each commitment, we analyze subsequent SEC filings to determine if the promise was fulfilled:
- **Fulfilled**: Target met or exceeded
- **Partially Fulfilled**: Progress made but target missed
- **Not Fulfilled**: Little to no progress
- **Abandoned**: Initiative discontinued
- **Pending**: Timeline not yet reached

### 3. Credibility Scoring

Overall score calculated as:
```
Score = (Fulfilled + 0.5 × Partial) / Total Verifiable × 100
```

This methodology is designed to be objective, evidence-based, and actionable for equity research analysts."""

    def _generate_limitations(self) -> str:
        """Generate limitations section."""
        return """## Limitations

**Important Considerations:**

1. **Based on Public Data Only**: Analysis uses only publicly-filed SEC documents. Private communications and non-public commitments are not captured.

2. **AI-Powered Extraction**: Commitment identification uses AI and may miss some commitments or include statements that aren't true commitments.

3. **Time Lag**: Recent commitments may not have had sufficient time to be fulfilled.

4. **External Factors**: Some failures may be due to market conditions, competition, or other factors beyond management's control.

5. **Not Investment Advice**: This analysis is a tool for equity research and does not constitute investment advice. Professional judgment required.

6. **Sample Size**: Analysis quality improves with more commitments. Fewer than 10 commitments may not be statistically significant.

7. **Context Matters**: Scores should be interpreted within industry and company context. Some industries have more predictable outcomes than others.

**This analysis should be used as one input among many in investment decision-making.**

---

**Generated by:** Management Integrity Agent v1.0
**Date:** {datetime.now().strftime('%B %d, %Y')}
**Data Source:** SEC EDGAR Database""".format(datetime=datetime)
