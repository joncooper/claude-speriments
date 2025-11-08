#!/usr/bin/env python3
"""
Example Management Integrity Analysis

This script demonstrates how to use the management integrity analysis library
programmatically. It assumes SEC data has already been fetched via MCP tools.

For real-world usage, use the /mgmt-integrity slash command which handles
data fetching, extraction, verification, scoring, and reporting automatically.

Usage:
    python example_analysis.py AAPL

Prerequisites:
    1. SEC data must already be fetched: data/AAPL_sec_data.json
    2. ANTHROPIC_API_KEY environment variable must be set
"""

import sys
import os

# Add lib directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

from commitment_extractor import CommitmentExtractor
from outcome_tracker import OutcomeTracker
from credibility_scorer import CredibilityScorer
from report_generator import ManagementIntegrityReport
from sec_data import load_json, save_json


def main():
    """Run example analysis."""
    # Get ticker from command line
    if len(sys.argv) < 2:
        print("Usage: python example_analysis.py TICKER")
        print("Example: python example_analysis.py AAPL")
        sys.exit(1)

    ticker = sys.argv[1].upper()

    print(f"Management Integrity Analysis Example: {ticker}")
    print("=" * 80)

    # Check if data file exists
    data_file = f"agents/equity-mgmt-integrity/data/{ticker}_sec_data.json"
    if not os.path.exists(data_file):
        print(f"\nError: SEC data file not found: {data_file}")
        print("\nTo fetch data, run:")
        print(f"  /mgmt-integrity TICKER:{ticker}")
        print("\nOr ensure the file exists before running this example.")
        sys.exit(1)

    # Load SEC data
    print("\n1. Loading SEC data...")
    data = load_json(data_file)
    print(f"   Company: {data['company_info']['name']}")
    print(f"   Filings: {len(data['filings'])}")

    # Extract commitments
    print("\n2. Extracting commitments...")
    print("   (This uses AI and may take a few minutes)")

    extractor = CommitmentExtractor()
    commitments = []

    # Use first 60% of filings for commitments
    cutoff = int(len(data['filings']) * 0.6)
    commitment_filings = data['filings'][:cutoff]

    for filing in commitment_filings:
        filing_text = filing.get('md_a_text', '') + "\n\n" + filing.get('business_text', '')

        comms = extractor.extract_from_text(
            filing_text,
            {
                'ticker': data['company_info']['ticker'],
                'company': data['company_info']['name'],
                'filing_type': filing['filing_type'],
                'filing_date': filing['filing_date'],
                'period_date': filing['period_date']
            }
        )
        commitments.extend(comms)
        print(f"   {filing['filing_type']} ({filing['filing_date']}): {len(comms)} commitments")

    print(f"\n   Total commitments extracted: {len(commitments)}")

    if not commitments:
        print("\n   No commitments found. Analysis cannot continue.")
        print("   This may be normal for companies that don't make specific commitments.")
        sys.exit(0)

    # Verify outcomes
    print("\n3. Verifying outcomes...")
    print("   (This uses AI and may take a few minutes)")

    tracker = OutcomeTracker()
    outcomes = []

    verification_filings = data['filings'][cutoff:]

    for commitment in commitments:
        verification_filing = tracker.find_verification_filing(
            commitment,
            verification_filings
        )

        if verification_filing:
            verification_text = (
                verification_filing.get('md_a_text', '') +
                "\n\n" +
                verification_filing.get('business_text', '')
            )

            outcome = tracker.verify_commitment(
                commitment,
                verification_text,
                {
                    'filing_type': verification_filing['filing_type'],
                    'filing_date': verification_filing['filing_date'],
                    'period_date': verification_filing['period_date']
                }
            )
        else:
            outcome = {
                'commitment_id': commitment['commitment_id'],
                'status': 'pending',
                'explanation': 'Timeline not yet reached',
                'confidence': 0.0,
                'verification_filing': {}
            }

        outcomes.append(outcome)
        status_symbol = "✅" if outcome['status'] == 'fulfilled' else "⚠️" if outcome['status'] == 'partially_fulfilled' else "❌"
        print(f"   {status_symbol} {commitment['metric'][:50]}: {outcome['status']}")

    # Calculate credibility score
    print("\n4. Calculating credibility score...")

    scorer = CredibilityScorer()
    score = scorer.score_management(commitments, outcomes)

    print(f"\n   Overall Score: {score['overall_score']}/100 ({score['grade']})")
    print(f"   Fulfilled: {score['fulfilled_count']} ({score['fulfillment_rate']:.1f}%)")
    print(f"   Partially Fulfilled: {score['partially_fulfilled_count']} ({score['partial_rate']:.1f}%)")
    print(f"   Not Fulfilled: {score['not_fulfilled_count'] + score['abandoned_count']} ({score['miss_rate']:.1f}%)")

    if score['red_flags']:
        print(f"\n   ⚠️  Red Flags: {len(score['red_flags'])}")
        for flag in score['red_flags']:
            print(f"      - {flag['description']}")

    print(f"\n   Trend: {score['time_trends']['description']}")

    # Generate report
    print("\n5. Generating report...")

    report_data = {
        'company_info': data['company_info'],
        'commitments': commitments,
        'outcomes': outcomes,
        'score': score
    }

    report = ManagementIntegrityReport(report_data)

    # Save report
    report_path = f"agents/equity-mgmt-integrity/data/{ticker}_report.md"
    report.save_report(report_path)

    print(f"   Report saved: {report_path}")

    # Display summary
    print("\n" + "=" * 80)
    print(report.generate_summary())
    print("=" * 80)

    # Save intermediate files
    print("\nSaving analysis files...")
    save_json(commitments, f"agents/equity-mgmt-integrity/data/{ticker}_commitments.json")
    save_json(outcomes, f"agents/equity-mgmt-integrity/data/{ticker}_outcomes.json")
    save_json(score, f"agents/equity-mgmt-integrity/data/{ticker}_score.json")

    print(f"\nAnalysis complete! Files saved to agents/equity-mgmt-integrity/data/{ticker}_*")

    # Risk assessment
    if score['overall_score'] >= 75:
        risk = "LOW"
    elif score['overall_score'] >= 60:
        risk = "MODERATE"
    elif score['overall_score'] >= 40:
        risk = "HIGH"
    else:
        risk = "VERY HIGH"

    print(f"\nRISK ASSESSMENT: {risk}")

    if score['overall_score'] >= 75:
        print("✅ Management appears reliable. Generally follows through on commitments.")
    elif score['overall_score'] >= 60:
        print("⚠️  Management has mixed track record. Monitor closely.")
    elif score['overall_score'] >= 40:
        print("🚨 Management credibility is concerning. Detailed review recommended.")
    else:
        print("❌ Management has poor credibility. Pattern of broken promises.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAnalysis interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nError during analysis: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
