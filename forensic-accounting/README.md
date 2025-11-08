# Forensic Accounting Agent for Claude

A comprehensive forensic accounting analysis system that examines publicly-traded companies for aggressive accounting practices and potential earnings manipulation. This tool provides the same level of analysis that senior forensic accountants deliver to equity research analysts and investment committees.

## What It Does

This agent performs deep forensic accounting analysis on any publicly-traded U.S. company by:

1. **Gathering Historical Financial Data** from SEC EDGAR filings (10-K reports)
2. **Calculating Beneish M-Scores** to detect likelihood of earnings manipulation
3. **Identifying Accounting Red Flags** across revenue quality, earnings quality, working capital, assets, and leverage
4. **Analyzing Trends Over Time** to determine if accounting is becoming more or less aggressive
5. **Generating Professional Reports** suitable for presentation to equity research analysts

## Key Features

### Beneish M-Score Analysis

The system implements the complete Beneish M-Score model, which uses 8 financial ratio indices to detect earnings manipulation with ~76% accuracy:

- **DSRI**: Days Sales in Receivables Index (revenue quality)
- **GMI**: Gross Margin Index (profitability pressure)
- **AQI**: Asset Quality Index (soft asset growth)
- **SGI**: Sales Growth Index (growth pressure)
- **DEPI**: Depreciation Index (depreciation manipulation)
- **SGAI**: SG&A Expenses Index (cost control)
- **TATA**: Total Accruals to Total Assets (earnings quality)
- **LVGI**: Leverage Index (debt pressure)

**Threshold**: M-Score > -2.22 indicates high likelihood of manipulation

### Comprehensive Red Flag Detection

The system analyzes dozens of forensic accounting red flags including:

- **Revenue Quality**: DSO trends, revenue/AR divergence, channel stuffing indicators
- **Earnings Quality**: Cash flow/earnings gaps, accrual patterns, smoothing detection
- **Working Capital**: Inventory buildup, liquidity deterioration, unusual movements
- **Asset Quality**: Soft asset growth, capitalization aggressiveness, impairment risk
- **Leverage**: Debt covenant pressure, refinancing risk, leverage increases
- **Profitability**: Margin deterioration, cost structure issues

### Trend Analysis

Multi-year trend analysis shows whether accounting policies are becoming:
- **More Aggressive** (worsening M-Scores, deteriorating metrics)
- **Less Aggressive** (improving M-Scores, strengthening metrics)

### Professional Reporting

Generates comprehensive forensic accounting reports including:
- Executive summary with clear risk assessment
- Detailed findings with specific metrics
- Implications of each red flag
- Specific recommendations for further investigation
- Professional methodology and limitations sections

## Installation

### 1. Install SEC EDGAR MCP Server (Required)

This tool uses the Model Context Protocol (MCP) to fetch financial data from SEC EDGAR. You must install an SEC EDGAR MCP server first.

**Recommended: stefanoamorelli/sec-edgar-mcp**

```bash
# Install the MCP server
pip install sec-edgar-mcp

# Or using uv (faster)
uv pip install sec-edgar-mcp
```

Then add to your Claude Code MCP configuration (`~/.config/claude/mcp.json`):

```json
{
  "mcpServers": {
    "sec-edgar": {
      "command": "python",
      "args": ["-m", "sec_edgar_mcp"]
    }
  }
}
```

**Alternative SEC EDGAR MCP servers:**
- `leopoldodonnell/edgar-mcp` (.NET-based)
- `LuisRincon23/SEC-MCP` (Python with streaming)

After installation, **restart Claude Code** for the MCP server to become available.

### 2. Install the Slash Command

```bash
# From the repository root
cp forensic-accounting/commands/forensic-analyze.md ~/.claude/commands/
```

### 3. Verify Installation

```bash
# Check that the command is available
ls ~/.claude/commands/forensic-analyze.md
```

After restarting Claude Code, MCP tools should be available with names like:
- `mcp__sec_edgar__get_company_facts`
- `mcp__sec_edgar__get_submissions`
- etc.

## Usage

### Basic Usage

In Claude Code, use the `/forensic-analyze` command with a stock ticker:

```
/forensic-analyze TICKER:AAPL
```

Replace `AAPL` with any publicly-traded U.S. company ticker symbol.

### What Happens

When you run the command, Claude will:

1. Act as a senior forensic accountant
2. Use MCP tools to fetch 5 years of historical financial data from SEC EDGAR
3. Structure and save the financial data
4. Run Python analysis scripts to:
   - Calculate Beneish M-Scores for each period
   - Identify all accounting red flags
   - Analyze trends over time
5. Generate a professional forensic accounting report
6. Provide clear guidance on risk level and next steps

### Output

You'll receive:

1. **Terminal Summary**: Key findings and overall risk assessment
2. **Detailed Report**: Professional markdown report saved to `forensic-accounting/reports/[TICKER]_[DATE].md`
3. **Data Files**: Complete analysis results in JSON format for further review

### Example Session

```
User: /forensic-analyze TICKER:TSLA

Claude: I'll perform a comprehensive forensic accounting analysis on Tesla (TSLA).

[Analysis runs...]

================================================================================
FORENSIC ACCOUNTING ANALYSIS: TSLA
================================================================================

Company: Tesla Inc
Analysis Date: November 7, 2025
Data Period: 5 years

OVERALL RISK ASSESSMENT: MODERATE

KEY FINDINGS:
1. Beneish M-Score: -2.45 - Below manipulation threshold
2. 0 Critical Red Flags Identified
3. 2 High Severity Red Flags Identified
4. Trend: Accounting policies becoming LESS aggressive

MOST CRITICAL CONCERNS:
- Days Sales Outstanding increased 18% (DSO now 52 days)
- Inventory growth (23%) exceeding sales growth (15%)

RECOMMENDATION:
Enhanced monitoring recommended. While M-Score is below threshold,
specific working capital trends warrant closer attention.

DETAILED REPORT: forensic-accounting/reports/TSLA_2025-11-07.md
```

## Understanding the Results

### Risk Levels

- **VERY HIGH**: Strong indicators of manipulation. Immediate forensic investigation recommended.
- **HIGH**: Significant red flags present. Detailed forensic review strongly recommended.
- **MODERATE**: Some concerning signals. Enhanced monitoring and targeted investigation recommended.
- **LOW**: Financial reporting within normal parameters. Standard due diligence appropriate.

### Interpreting Beneish M-Scores

| Score Range | Risk Level | Action |
|-------------|------------|--------|
| > -1.78 | Very High | Immediate investigation |
| -1.78 to -2.22 | High | Detailed forensic review |
| -2.22 to -2.50 | Moderate | Enhanced monitoring |
| < -2.50 | Low | Standard due diligence |

### Red Flag Severity

- **🔴 Critical**: Immediate attention required (e.g., negative cash flow with positive earnings)
- **🟠 High**: Significant concerns requiring detailed review (e.g., AR growing much faster than revenue)
- **🟡 Medium**: Enhanced monitoring warranted (e.g., inventory growth exceeding sales)
- **🟢 Low**: Note for standard due diligence (e.g., minor ratio changes)

## Use Cases

### For Equity Research Analysts

- **Initial Screening**: Quickly identify companies with questionable accounting
- **Deep Dives**: Support detailed company analysis with forensic perspective
- **Monitoring**: Track whether accounting quality is improving or deteriorating
- **Report Support**: Include forensic analysis in research reports

### For Portfolio Managers

- **Due Diligence**: Screen potential investments for accounting red flags
- **Risk Management**: Monitor existing positions for emerging accounting issues
- **Short Ideas**: Identify companies with aggressive accounting for potential shorts
- **Exit Decisions**: Use deteriorating accounting quality as a sell signal

### For Compliance Teams

- **Vendor Due Diligence**: Assess accounting quality of counterparties
- **Investment Review**: Evaluate accounting practices of investment targets
- **Risk Assessment**: Identify high-risk accounting situations

### For Financial Professionals in Training

- **Learning Tool**: Understand how senior forensic accountants analyze financial statements
- **Pattern Recognition**: See real examples of accounting red flags
- **Methodology**: Learn professional forensic accounting techniques

## Technical Details

### Data Source

All financial data comes from the **SEC EDGAR database**, specifically:
- 10-K annual reports
- XBRL-tagged financial statements
- Official company submissions

The system uses the official SEC API at `data.sec.gov` (no API key required).

### Analysis Methodology

The analysis follows methodologies used by:
- Certified Fraud Examiners (CFE)
- Forensic accounting professionals
- CFA Institute financial analysis framework
- Academic research on earnings manipulation detection

### Limitations

**Important**: This analysis:
- Is based only on publicly-available data
- Cannot guarantee detection of all manipulation
- Has ~76% accuracy with ~17.5% false positive rate on Beneish M-Score
- Should be used as a screening tool, not definitive proof
- Requires interpretation by qualified professionals

**This tool does NOT:**
- Replace professional forensic accounting services
- Constitute an audit or assurance engagement
- Provide investment advice
- Guarantee detection of fraud

### Rate Limits

The SEC API has rate limits:
- 10 requests per second maximum
- The system automatically throttles requests to comply

## Project Structure

```
forensic-accounting/
├── README.md                          # This file
├── commands/
│   └── forensic-analyze.md            # Main slash command
├── lib/                               # Python analysis library
│   ├── __init__.py
│   ├── sec_data.py                    # SEC EDGAR data fetching
│   ├── beneish_score.py              # Beneish M-Score calculator
│   ├── red_flags.py                   # Red flag detection
│   ├── forensic_analysis.py           # Main orchestrator
│   └── report_generator.py            # Report generation
├── reports/                           # Generated reports saved here
└── templates/                         # Report templates
```

## Advanced Usage

### Programmatic Access

You can also use the Python library directly:

```python
import sys
sys.path.append('forensic-accounting')

from lib import ForensicAccountingAnalyzer
from lib.report_generator import generate_report

# Run analysis
analyzer = ForensicAccountingAnalyzer()
results = analyzer.analyze_company('AAPL', num_years=5)

# Generate report
generate_report(results, 'forensic-accounting/reports/AAPL_analysis.md')

# Access specific results
print(f"M-Score: {results['beneish_scores'][0]['m_score']}")
print(f"Risk Level: {results['assessment']['risk_level']}")
```

### Batch Analysis

Analyze multiple companies:

```python
from lib import run_forensic_analysis

tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']

for ticker in tickers:
    try:
        results = run_forensic_analysis(ticker, num_years=5)
        print(f"{ticker}: {results['assessment']['risk_level']}")
    except Exception as e:
        print(f"{ticker}: Error - {e}")
```

### Custom Analysis Period

Adjust the number of years analyzed:

```
/forensic-analyze TICKER:AAPL YEARS:7
```

## Examples of Red Flags Detected

### Revenue Quality Issues

- **DSO Increase**: Days Sales Outstanding growing faster than revenue (potential revenue inflation)
- **AR/Revenue Divergence**: Accounts receivable growing much faster than sales
- **Revenue Timing**: Unusual patterns in quarterly revenue recognition

### Earnings Quality Issues

- **Low CF/NI Ratio**: Operating cash flow significantly below net income
- **High Accruals**: Earnings heavily dependent on accrual adjustments
- **Earnings Smoothing**: Unusually stable earnings despite volatile cash flows

### Working Capital Red Flags

- **Inventory Buildup**: Inventory growing faster than sales (obsolescence risk)
- **Liquidity Deterioration**: Current ratio declining significantly
- **Unusual Movements**: Unexplained changes in working capital accounts

### Asset Quality Concerns

- **Soft Asset Growth**: Increasing proportion of intangibles and deferred charges
- **Capitalization Issues**: Aggressive capitalization of expenses
- **Impairment Risk**: Asset values that may require write-downs

## Real-World Application

This analysis is based on the same techniques used by forensic accountants in:

- **Major Fraud Cases**: Enron, WorldCom, HealthSouth, Luckin Coffee
- **Short-Seller Research**: Famous short reports often cite similar red flags
- **Audit Firms**: Big 4 forensic accounting practices
- **Investment Research**: Buy-side and sell-side equity research

## Research Background

### Beneish M-Score

Based on:
- Beneish, M. D. (1999). "The Detection of Earnings Manipulation." *Financial Analysts Journal*
- Beneish, M. D., Lee, C., & Nichols, D. C. (2013). "Earnings Manipulation and Expected Returns"
- Beneish, M. D., & Vorst, P. (2020). "The Cost of Fraud Prediction Errors"

### Red Flag Analysis

Based on:
- CFA Institute curriculum on financial reporting quality
- ACFE (Association of Certified Fraud Examiners) fraud detection methods
- Academic research on earnings management and manipulation
- Practitioner knowledge from forensic accounting professionals

## Troubleshooting

### "Could not find CIK for ticker"

- **Issue**: Company ticker not found in SEC database
- **Solutions**:
  - Verify the ticker symbol is correct
  - Ensure the company is U.S.-based and files with the SEC
  - Check that the company is publicly-traded
  - Try using the company's CIK number directly

### "Insufficient data to calculate"

- **Issue**: Company doesn't have enough historical data
- **Solutions**:
  - Try reducing the number of years: `YEARS:3`
  - Company may be recently public (need 2+ years for Beneish)
  - Check if company files required XBRL data

### Rate Limiting Errors

- **Issue**: SEC API rate limits exceeded
- **Solutions**:
  - Wait 60 seconds and retry
  - System should auto-throttle, but rapid repeated requests may trigger limits
  - The SEC allows 10 requests per second; system respects this

### Missing Financial Metrics

- **Issue**: Some financial statement items not available
- **Solutions**:
  - The system estimates missing values when possible
  - Some metrics may use industry-typical approximations
  - Review the Limitations section in the generated report

## Roadmap

Potential future enhancements:

- [ ] Support for international companies (non-U.S. exchanges)
- [ ] Analysis of 10-Q quarterly filings
- [ ] Additional manipulation detection models (F-Score, Altman Z)
- [ ] Industry-specific benchmarking
- [ ] Historical trend charting and visualization
- [ ] Peer comparison analysis
- [ ] Machine learning-based fraud detection
- [ ] Real-time monitoring and alerts

## Contributing

This is a research and educational tool. Contributions welcome:

- Additional red flag detections
- Improved estimation methods
- Industry-specific analysis adjustments
- Documentation improvements
- Bug reports and fixes

## License

This project is for educational and research purposes. The Beneish M-Score model is based on published academic research and is implemented here according to the original papers.

## Disclaimer

**IMPORTANT LEGAL DISCLAIMER:**

This tool is provided for educational and research purposes only. It does not constitute:

- Investment advice or recommendations
- Professional forensic accounting services
- An audit, review, or assurance engagement
- Legal, financial, or tax advice

**No warranties**: This tool is provided "as is" without any warranties. The creators assume no liability for investment decisions made based on this analysis.

**Professional judgment required**: All findings must be interpreted by qualified professionals. Automated analysis cannot replace experienced human judgment in forensic accounting.

**Not a guarantee**: The analysis cannot guarantee detection of fraud or manipulation. False positives and false negatives are possible.

**Seek professional advice**: For material investment or business decisions, consult qualified forensic accountants, auditors, and investment professionals.

## Support

For issues, questions, or suggestions:

1. Review this README and documentation
2. Check the generated report's Limitations section
3. Review the methodology section
4. Open an issue in the repository

## Acknowledgments

This tool implements methodologies developed by:

- Professor Messod Beneish (Indiana University) - Beneish M-Score model
- The forensic accounting community
- CFA Institute financial analysis framework
- Association of Certified Fraud Examiners (ACFE)

## Citation

If you use this tool in research or publications, please cite:

```
Forensic Accounting Agent for Claude (2025)
Based on: Beneish, M. D. (1999). "The Detection of Earnings Manipulation."
Financial Analysts Journal, 55(5), 24-36.
```

---

**Version:** 1.0.0
**Last Updated:** November 2025
**Status:** Production Ready

---

*"The best time to identify accounting fraud is before it becomes public."*
— Forensic Accounting Principle
