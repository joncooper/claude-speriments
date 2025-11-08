# Management Integrity Agent for Claude

An AI-powered equity research tool that analyzes whether public company management follows through on their commitments. This agent answers the critical investor question: **"Does management do what they say they're going to do?"**

## What It Does

This agent performs comprehensive management credibility analysis on any publicly-traded U.S. company by:

1. **Extracting Forward-Looking Commitments** from SEC filings (10-K, 10-Q reports) using AI
2. **Verifying Outcomes** by analyzing subsequent filings to check if promises were kept
3. **Scoring Management Credibility** with quantitative 0-100 scores and letter grades
4. **Identifying Red Flags** including declining specificity, systematic misses, and abandoned initiatives
5. **Analyzing Trends** to determine if management credibility is improving or declining
6. **Generating Professional Reports** suitable for equity research analysts

## Why This Matters

Management credibility is a critical but often overlooked factor in equity analysis:

- **🎯 Track Record Matters**: Past fulfillment predicts future performance
- **🚩 Red Flags**: Patterns of overpromising indicate deeper issues
- **📈 Trends**: Improving credibility suggests learning; declining suggests problems
- **💰 Investment Impact**: Unreliable management destroys shareholder value
- **🔍 Differentiation**: Most investors don't systematically track this

This tool provides the same level of analysis that experienced equity analysts perform manually, but automated and systematic.

## Key Features

### AI-Powered Commitment Extraction

The system uses Claude to identify specific, verifiable management commitments:

- **Forward-looking statements** about future actions and targets
- **Specific and measurable** (not vague aspirations like "focus on innovation")
- **Verifiable** against future filings
- **Categorized** into types:
  - Financial targets (revenue, margins, EPS)
  - Capital allocation (buybacks, dividends, CapEx)
  - Strategic initiatives (M&A, expansions)
  - Operational improvements (cost savings, efficiency)
  - Product launches (new products, services)

Only high-quality commitments (specificity ≥ 4/10) are included.

### AI-Powered Outcome Verification

For each commitment, Claude analyzes subsequent filings to determine:

- **✅ Fulfilled**: Target met or exceeded
- **⚠️ Partially Fulfilled**: Progress made but target missed
- **❌ Not Fulfilled**: Little to no progress
- **🚫 Abandoned**: Initiative explicitly discontinued
- **⏳ Pending**: Timeline not yet reached

Includes exact evidence quotes and variance calculations.

### Quantitative Credibility Scoring

Rigorous scoring methodology:

```
Score = (Fulfilled + 0.5 × Partially Fulfilled) / Total Verifiable × 100
```

**Letter Grades:**
- **A+/A (90-100)**: Excellent - Management consistently delivers
- **B+/B/B- (75-89)**: Good - Generally reliable
- **C+/C/C- (60-74)**: Fair - Mixed track record
- **D+/D/D- (40-59)**: Poor - Significant credibility issues
- **F (0-39)**: Failing - Pattern of broken promises

**Category Breakdowns:**
- Performance by commitment type
- Identifies strengths and weaknesses

### Red Flag Detection

Automatically identifies concerning patterns:

- **High Category Miss Rate**: >50% failures in specific area (e.g., financial targets)
- **Declining Specificity**: Management becoming more vague over time (>2 point drop)
- **Multiple Abandoned Initiatives**: Pattern of discontinuing promised projects (≥2)
- **Consistent Underperformance**: Average variance below target (< -5%)

### Time Trend Analysis

Shows whether credibility is:
- **📈 Improving**: Management learning from past misses
- **📉 Declining**: Growing pattern of unfulfilled commitments (⚠️ major red flag)
- **➡️ Stable**: Consistent performance level

### Professional Reporting

Generates comprehensive markdown reports including:
- Executive summary with clear assessment
- Credibility score details
- Category performance breakdown
- Time trends
- Red flags (if any)
- Notable successes and failures
- Detailed findings with evidence
- Methodology and limitations

## Installation

### 1. Install SEC EDGAR MCP Server (Required)

This tool uses the Model Context Protocol (MCP) to fetch SEC data.

**Recommended: stefanoamorelli/sec-edgar-mcp**

```bash
# Install the MCP server
pip install sec-edgar-mcp

# Or using uv (faster)
uv pip install sec-edgar-mcp
```

Add to your Claude Code MCP configuration (`~/.config/claude/mcp.json`):

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

**After installation, restart Claude Code** for the MCP server to become available.

### 2. Set Anthropic API Key (Required)

The agent uses Claude for AI-powered commitment extraction and verification.

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

Or add to your shell profile (~/.bashrc, ~/.zshrc):

```bash
echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### 3. Install the Slash Command

```bash
# From the repository root
cp agents/equity-mgmt-integrity/commands/mgmt-integrity.md ~/.claude/commands/
```

### 4. Verify Installation

```bash
# Check command is installed
ls ~/.claude/commands/mgmt-integrity.md

# Verify environment variable
echo $ANTHROPIC_API_KEY
```

After restarting Claude Code, MCP tools should be available with names like:
- `mcp__sec_edgar__get_company_facts`
- `mcp__sec_edgar__get_submissions`

## Usage

### Basic Usage

In Claude Code, use the `/mgmt-integrity` command with a stock ticker:

```
/mgmt-integrity TICKER:AAPL
```

Replace `AAPL` with any publicly-traded U.S. company ticker symbol.

### What Happens

When you run the command, Claude will:

1. Act as an expert equity research analyst
2. Use MCP tools to fetch 3 years of SEC filings (10-K, 10-Q)
3. Extract MD&A and Business Strategy sections
4. Use AI to identify ~10-30 specific commitments from earlier filings
5. Verify each commitment against subsequent filings using AI
6. Calculate credibility scores and identify red flags
7. Generate a professional report
8. Display summary in terminal

**Runtime:** 5-15 minutes depending on company size and number of commitments.

### Example Session

```
User: /mgmt-integrity TICKER:AAPL

Claude: I'll analyze whether Apple management follows through on commitments.

[Fetching SEC data via MCP...]
Found 12 filings (6 10-Ks, 6 10-Qs) from 2021-2024.

[Extracting commitments...]
Extracted 18 specific commitments from 7 filings.

[Verifying outcomes...]
Verified 18 commitments against subsequent filings.

[Calculating credibility score...]

================================================================================
MANAGEMENT INTEGRITY ANALYSIS: AAPL
================================================================================

Company: Apple Inc
Analysis Date: November 8, 2025
Commitments Analyzed: 18

OVERALL CREDIBILITY SCORE: 83.3/100 (B+)
RISK ASSESSMENT: LOW

KEY METRICS:
- Fulfilled: 13 (72.2%)
- Partially Fulfilled: 4 (22.2%)
- Not Fulfilled: 1 (5.6%)

TIME TREND: Credibility stable (around 82.0)

RED FLAGS: 0 identified

================================================================================

Detailed report: agents/equity-mgmt-integrity/data/AAPL_report.md
```

### Output Files

The analysis generates several files in `agents/equity-mgmt-integrity/data/`:

- `{TICKER}_sec_data.json` - Raw SEC filing data
- `{TICKER}_commitments.json` - Extracted commitments
- `{TICKER}_outcomes.json` - Verification results
- `{TICKER}_score.json` - Credibility scores
- `{TICKER}_report.md` - Full professional report

## Understanding the Results

### Risk Levels

- **LOW (Score 75-100)**: Management generally reliable, suitable for investment
- **MODERATE (Score 60-74)**: Mixed track record, requires monitoring
- **HIGH (Score 40-59)**: Significant credibility issues, detailed review needed
- **VERY HIGH (Score 0-39)**: Pattern of broken promises, serious concern

### What to Look For

**🟢 Positive Signals:**
- Score above 75
- High fulfillment rate (>70%)
- Improving trend
- No red flags
- Strong performance in financial targets

**🔴 Warning Signs:**
- Score below 60
- High miss rate (>30%)
- Declining trend
- Multiple red flags
- Abandoned initiatives
- Vague commitments (declining specificity)

### Common Patterns

**Reliable Management (A/B grades):**
- Makes specific, achievable commitments
- Consistently delivers or exceeds
- Transparent about challenges
- Learns from past misses

**Unreliable Management (C/D/F grades):**
- Overpromises and underdelivers
- Makes vague, unverifiable statements
- Frequently abandons initiatives
- Consistently misses targets
- Declining specificity over time

## Use Cases

### For Equity Research Analysts

- **Initial Screening**: Quickly identify management credibility issues
- **Deep Dives**: Comprehensive analysis for research reports
- **Monitoring**: Track whether credibility is improving or declining
- **Comparative Analysis**: Compare management across competitors

### For Portfolio Managers

- **Due Diligence**: Screen potential investments for management quality
- **Risk Management**: Identify portfolio holdings with credibility issues
- **Short Ideas**: Find companies with declining credibility
- **Exit Decisions**: Use deteriorating credibility as sell signal

### For Individual Investors

- **Investment Research**: Understand if management can be trusted
- **Risk Assessment**: Identify red flags before investing
- **Monitoring**: Track management of current holdings
- **Learning**: Understand what separates good from bad management

## Technical Details

### Data Source

All data comes from **SEC EDGAR database**:
- 10-K annual reports
- 10-Q quarterly reports
- MD&A (Management Discussion & Analysis) sections
- Business strategy sections

### AI Models

Uses **Claude Sonnet 4.5** (claude-sonnet-4-5-20250929) for:
- Commitment extraction with structured output
- Outcome verification with evidence
- Confidence scoring

### Analysis Methodology

Based on principles from:
- Equity research best practices
- Academic research on management forecasting
- Behavioral finance (overpromising patterns)
- Professional investment analysis frameworks

### Limitations

**Important**: This analysis:
- Is based only on publicly-available data
- Cannot capture private communications
- May miss some commitments or include non-commitments (AI limitations)
- Requires sufficient time for verification (recent commitments may be pending)
- Cannot always control for external factors (market conditions, competition)
- Should be used as one input among many

**This tool does NOT:**
- Replace professional equity research
- Constitute investment advice
- Guarantee accuracy of predictions
- Account for all external factors

## Project Structure

```
equity-mgmt-integrity/
├── README.md                      # This file
├── TESTING.md                     # Testing guide
├── commands/
│   └── mgmt-integrity.md          # Main slash command
├── lib/                           # Python analysis library
│   ├── __init__.py
│   ├── sec_data.py                # Data manipulation helpers
│   ├── commitment_extractor.py    # AI-powered commitment extraction
│   ├── outcome_tracker.py         # AI-powered outcome verification
│   ├── credibility_scorer.py      # Scoring and red flag detection
│   └── report_generator.py        # Report generation
├── data/                          # Generated data files
│   └── README.md
└── example_analysis.py            # Simple usage example
```

## Advanced Usage

### Programmatic Access

You can use the Python library directly:

```python
import sys
sys.path.insert(0, 'agents/equity-mgmt-integrity/lib')

from commitment_extractor import CommitmentExtractor
from outcome_tracker import OutcomeTracker
from credibility_scorer import CredibilityScorer

# Extract commitments
extractor = CommitmentExtractor()
commitments = extractor.extract_from_text(filing_text, metadata)

# Verify outcomes
tracker = OutcomeTracker()
outcome = tracker.verify_commitment(commitment, verification_text, metadata)

# Score credibility
scorer = CredibilityScorer()
score = scorer.score_management(commitments, outcomes)
```

### Custom Analysis

Modify the analysis by:
- Adjusting the commitment/verification filing split (default 60/40)
- Changing specificity threshold (default ≥4)
- Modifying scoring weights
- Adding custom red flag rules
- Filtering by commitment category

## Real-World Examples

### Case Study: High Credibility (Score 85+)

**Characteristics:**
- Specific, measurable commitments
- Consistent delivery or exceeding targets
- Transparent communication
- Limited abandoned initiatives
- Strong financial target performance

### Case Study: Declining Credibility (Score dropping 15+ points)

**Red Flags:**
- Increasingly vague commitments
- Rising miss rate over time
- Multiple abandoned strategic initiatives
- Systematic underperformance vs. guidance
- ⚠️ **Strong sell signal for investors**

### Case Study: Low Credibility (Score <50)

**Characteristics:**
- Pattern of overpromising
- Frequent target misses (>50%)
- Multiple abandoned initiatives
- Vague, unverifiable statements
- Poor financial target performance
- **Avoid or short opportunity**

## Troubleshooting

### "ANTHROPIC_API_KEY not found"

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

### "SEC EDGAR MCP tools not available"

- Install sec-edgar-mcp: `pip install sec-edgar-mcp`
- Add to ~/.config/claude/mcp.json
- Restart Claude Code

### "No commitments found"

- Some companies make few specific commitments (common in certain industries)
- Try a different company or longer time period
- Check that MD&A sections were properly extracted

### "Most commitments marked as pending"

- Company's commitments have long timelines
- Need more recent data to verify
- This is normal for forward-looking commitments

## Roadmap

Potential enhancements:

- [ ] Support for international companies (non-U.S. exchanges)
- [ ] Earnings call transcript analysis
- [ ] Conference presentation analysis
- [ ] Competitor comparison reports
- [ ] Historical trend charts
- [ ] Industry benchmarking
- [ ] Real-time monitoring and alerts
- [ ] Integration with financial models

## Contributing

Contributions welcome:
- Improved AI prompts for extraction/verification
- Additional red flag patterns
- Industry-specific adjustments
- Documentation improvements
- Bug reports and fixes

## Citation

If you use this tool in research, please cite:

```
Management Integrity Agent for Claude (2025)
https://github.com/joncooper/claude-speriments
```

## License

This project is for educational and research purposes.

## Disclaimer

**IMPORTANT LEGAL DISCLAIMER:**

This tool is provided for educational and research purposes only. It does not constitute:

- Investment advice or recommendations
- Professional equity research services
- Financial, legal, or tax advice

**No warranties**: This tool is provided "as is" without any warranties. The creators assume no liability for investment decisions made based on this analysis.

**Professional judgment required**: All findings must be interpreted by qualified professionals. Automated analysis cannot replace experienced human judgment.

**Not a guarantee**: The analysis cannot guarantee accuracy of management assessment. False positives and false negatives are possible.

**Seek professional advice**: For material investment decisions, consult qualified equity research analysts and investment professionals.

---

**Version:** 1.0.0
**Last Updated:** November 2025
**Status:** Production Ready

---

*"The best predictor of future management behavior is past management behavior."*
— Investment Principle
