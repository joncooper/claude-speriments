#!/usr/bin/env python3
"""
Example Forensic Accounting Analysis Script

This script demonstrates how to use the forensic accounting library
to analyze a publicly-traded company.

Usage:
    python example_analysis.py TICKER [num_years]

Example:
    python example_analysis.py AAPL 5
"""

import sys
import os
from datetime import datetime

# Add the lib directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

from forensic_analysis import ForensicAccountingAnalyzer
from report_generator import ForensicAccountingReport


def main():
    """Run forensic accounting analysis on a company."""

    # Parse command line arguments
    if len(sys.argv) < 2:
        print("Usage: python example_analysis.py TICKER [num_years]")
        print("Example: python example_analysis.py AAPL 5")
        sys.exit(1)

    ticker = sys.argv[1].upper()
    num_years = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    print("\n" + "="*80)
    print(f"FORENSIC ACCOUNTING ANALYSIS")
    print("="*80 + "\n")

    try:
        # Initialize analyzer
        analyzer = ForensicAccountingAnalyzer()

        # Run analysis
        print(f"Analyzing {ticker}...\n")
        results = analyzer.analyze_company(ticker, num_years)

        # Display summary
        print("\n" + "="*80)
        print("ANALYSIS COMPLETE")
        print("="*80 + "\n")

        metadata = results['metadata']
        assessment = results['assessment']
        beneish_scores = results['beneish_scores']

        print(f"Company: {metadata['company_name']}")
        print(f"Ticker: {metadata['ticker']}")
        print(f"Industry: {metadata['industry']}")
        print(f"Years Analyzed: {metadata['years_analyzed']}\n")

        print(f"OVERALL RISK ASSESSMENT: {assessment['risk_level']}")
        print(f"Risk Score: {assessment['risk_score']}/100\n")

        if beneish_scores:
            latest = beneish_scores[0]
            print(f"Latest Beneish M-Score: {latest['m_score']:.3f}")
            print(f"Threshold: {latest['interpretation']['threshold']}")
            print(f"Likely Manipulator: {'YES' if latest['interpretation']['is_likely_manipulator'] else 'NO'}\n")

        print(f"Red Flags Identified:")
        print(f"  - Critical: {assessment['critical_red_flags']}")
        print(f"  - High: {assessment['high_red_flags']}")
        print(f"  - Medium: {assessment['medium_red_flags']}")
        print(f"  - Total: {assessment['total_red_flags']}\n")

        print(f"Recommendation: {assessment['recommendation']}\n")

        # Generate and save report
        report_dir = os.path.join(os.path.dirname(__file__), 'reports')
        os.makedirs(report_dir, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_path = os.path.join(report_dir, f"{ticker}_{timestamp}.md")

        print(f"Generating detailed report...")
        report = ForensicAccountingReport(results)
        report.save_report(report_path)

        print(f"\n✓ Report saved to: {report_path}")

        # Save JSON data
        import json
        json_path = os.path.join(report_dir, f"{ticker}_{timestamp}.json")
        with open(json_path, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"✓ Data saved to: {json_path}\n")

        print("="*80)
        print("Analysis complete. Review the detailed report for full findings.")
        print("="*80 + "\n")

    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
