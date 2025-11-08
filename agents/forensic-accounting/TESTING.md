# Testing the Forensic Accounting Agent

## Requirements

This tool requires:
1. **Python 3.7+**
2. **Internet access** to SEC EDGAR (https://www.sec.gov/)
3. **requests library**: `pip install requests`

## Network Access

The SEC EDGAR API requires:
- Outbound HTTPS access to `https://www.sec.gov/` and `https://data.sec.gov/`
- A proper User-Agent header (automatically provided)
- Compliance with SEC rate limits (10 requests per second - automatically enforced)

**Note**: In sandboxed or restricted environments where external API access is blocked, the tool will not be able to fetch financial data. This is expected behavior and not a bug in the tool.

## Quick Test

### Using the Example Script

```bash
cd forensic-accounting
python3 example_analysis.py AAPL 5
```

This will:
1. Fetch 5 years of Apple's financial data from SEC EDGAR
2. Calculate Beneish M-Scores
3. Identify all red flags
4. Generate a comprehensive report

Expected output:
- Terminal summary showing risk level and key findings
- Detailed markdown report in `reports/AAPL_[timestamp].md`
- JSON data file in `reports/AAPL_[timestamp].json`

### Using the Slash Command

In Claude Code:

```
/forensic-analyze TICKER:AAPL
```

Claude will act as a senior forensic accountant and perform the complete analysis.

## Test Companies

Good companies to test with:

### Low Risk Examples
- **AAPL** (Apple) - Generally conservative accounting
- **MSFT** (Microsoft) - High quality financial reporting
- **JNJ** (Johnson & Johnson) - Consistent conservative practices

### Higher Risk Examples
Companies with known accounting issues or aggressive practices can be identified through:
- Short seller reports
- Accounting quality research
- Companies that have had restatements

## Expected Results

### Successful Analysis
```
================================================================================
FORENSIC ACCOUNTING ANALYSIS: AAPL
================================================================================

Company: Apple Inc
Analysis Date: November 7, 2025
Data Period: 5 years

OVERALL RISK ASSESSMENT: LOW

KEY FINDINGS:
1. Beneish M-Score: -2.65 - Below manipulation threshold
2. 0 Critical Red Flags Identified
3. 1 High Severity Red Flags Identified
4. Trend: Accounting policies stable

DETAILED REPORT: forensic-accounting/reports/AAPL_20251107_143022.md
```

### If SEC Access is Blocked

You may see:
```
Error fetching data from https://www.sec.gov/files/company_tickers.json: 403 Client Error: Forbidden
Warning: Could not find CIK for ticker AAPL
Note: In sandboxed environments, SEC API access may be restricted.
This tool requires internet access to https://www.sec.gov/
```

This indicates the environment doesn't have access to SEC APIs. The tool is working correctly but cannot reach external APIs.

## Troubleshooting

### 403 Forbidden Errors

**Cause**: SEC blocking requests or sandboxed environment

**Solutions**:
1. Ensure your environment has outbound HTTPS access
2. Check if there's a firewall or proxy blocking SEC access
3. Verify you're not in a sandboxed/offline environment
4. Try running from a different network

### Timeout Errors

**Cause**: SEC API is slow or network latency

**Solutions**:
1. Increase timeout in sec_data.py (currently 30 seconds)
2. Retry the request
3. Check your internet connection speed

### Missing Data Errors

**Cause**: Company doesn't file required XBRL data or is recently public

**Solutions**:
1. Verify the company files 10-K reports with XBRL data
2. Try reducing the number of years: `python3 example_analysis.py TICKER 3`
3. Check if the company is recently public (need at least 2 years)

### Import Errors

**Cause**: Missing dependencies

**Solutions**:
```bash
pip install requests
```

## Validation Tests

To verify the implementation is correct:

### 1. Test Beneish Calculator

```python
from lib.beneish_score import BeneishMScore

calculator = BeneishMScore()

# Test data (should produce M-Score > -2.22 indicating manipulation)
test_data = {
    "ar_current": 1000, "ar_prior": 800,
    "sales_current": 5000, "sales_prior": 4000,
    # ... (provide all required fields)
}

score, variables = calculator.calculate_m_score(test_data)
print(f"M-Score: {score}")
```

### 2. Test Red Flag Detection

```python
from lib.red_flags import ForensicRedFlagAnalyzer

analyzer = ForensicRedFlagAnalyzer()

# Create test financial data
test_data = [
    {"Revenues": 1000, "AccountsReceivable": 200, ...},
    {"Revenues": 800, "AccountsReceivable": 150, ...}
]

flags = analyzer.analyze_all(test_data)
print(f"Found {len(flags)} red flags")
```

### 3. Test Report Generation

```python
from lib.report_generator import ForensicAccountingReport

# Use results from a previous analysis
report = ForensicAccountingReport(analysis_results)
markdown = report.generate_markdown_report()
print(markdown[:500])  # Print first 500 chars
```

## Performance

Expected timing for a 5-year analysis:
- Data fetching: 5-10 seconds (depends on network)
- Analysis: < 1 second
- Report generation: < 1 second
- **Total**: ~6-12 seconds

## Known Limitations

1. **Only U.S. Public Companies**: Must file with SEC
2. **Only Annual Data**: Uses 10-K filings (not 10-Q quarterly)
3. **XBRL Required**: Company must provide XBRL-tagged financials
4. **Minimum 2 Years**: Need at least 2 years for Beneish M-Score
5. **Internet Required**: Must reach SEC EDGAR APIs
6. **Rate Limited**: SEC allows 10 requests/second

## Success Criteria

The tool is working correctly if:
- ✅ It can fetch company ticker-to-CIK mappings
- ✅ It can retrieve company facts (XBRL data)
- ✅ It calculates all 8 Beneish variables
- ✅ It detects relevant red flags
- ✅ It generates a well-formatted markdown report
- ✅ It provides clear risk assessment

## Contributing Test Cases

When adding test cases, include:
1. Company ticker
2. Expected risk level
3. Expected key red flags
4. Date of test (financial data changes over time)
5. Any special considerations

---

For questions or issues, refer to the main README.md file.
