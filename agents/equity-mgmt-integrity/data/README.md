# Data Directory

This directory stores all data files generated during management integrity analysis.

## Generated Files

When you run `/mgmt-integrity TICKER:AAPL`, the following files are created:

### 1. `{TICKER}_sec_data.json`

Raw SEC filing data fetched via MCP tools.

**Structure:**
```json
{
  "company_info": {
    "name": "Apple Inc",
    "ticker": "AAPL",
    "cik": "0000320193"
  },
  "filings": [
    {
      "filing_type": "10-K",
      "filing_date": "2023-11-01",
      "period_date": "2023-09-30",
      "md_a_text": "Management's Discussion and Analysis text...",
      "business_text": "Business description text...",
      "accession_number": "0000320193-23-000106"
    }
  ]
}
```

**Purpose:** Source data for analysis. Contains MD&A and Business sections from SEC filings.

**Size:** ~1-5 MB depending on company and number of filings

### 2. `{TICKER}_commitments.json`

Extracted forward-looking commitments from management.

**Structure:**
```json
[
  {
    "commitment_id": "COMM_a3f5e8c1b2d4f6a9",
    "commitment_text": "We expect to achieve operating margins of 30% by fiscal 2025",
    "category": "financial_target",
    "metric": "operating margin",
    "target": 30.0,
    "target_unit": "percent",
    "timeline": "fiscal 2025",
    "specificity": 8,
    "verifiable": true,
    "confidence": 0.95,
    "source_filing": {
      "ticker": "AAPL",
      "company": "Apple Inc",
      "filing_type": "10-K",
      "filing_date": "2023-11-01",
      "period_date": "2023-09-30"
    }
  }
]
```

**Purpose:** All specific, verifiable commitments identified by AI.

**Key fields:**
- `commitment_id`: Unique identifier
- `commitment_text`: Exact quote from filing
- `category`: Type of commitment (financial_target, capital_allocation, strategic_initiative, operational_improvement, product_launch)
- `metric`: What's being committed to
- `target`: Quantitative value (if applicable)
- `timeline`: When it should be fulfilled
- `specificity`: Quality score (1-10, only ≥4 included)
- `verifiable`: Must be true
- `confidence`: AI confidence (0.0-1.0)

**Size:** ~10-100 KB depending on number of commitments

### 3. `{TICKER}_outcomes.json`

Verification results for each commitment.

**Structure:**
```json
[
  {
    "commitment_id": "COMM_a3f5e8c1b2d4f6a9",
    "status": "fulfilled",
    "explanation": "Operating margins reached 31.2% in fiscal 2025, exceeding the 30% target",
    "actual_value": 31.2,
    "actual_unit": "percent",
    "variance": 4.0,
    "evidence": "Our operating margin expanded to 31.2% for the fiscal year...",
    "confidence": 0.92,
    "verification_filing": {
      "filing_type": "10-K",
      "filing_date": "2025-11-01",
      "period_date": "2025-09-30"
    }
  }
]
```

**Purpose:** Results of commitment verification against subsequent filings.

**Status values:**
- `fulfilled`: Target met or exceeded
- `partially_fulfilled`: Progress made but target missed
- `not_fulfilled`: Little to no progress
- `abandoned`: Initiative discontinued
- `pending`: Timeline not yet reached
- `unverifiable`: Insufficient information

**Key fields:**
- `commitment_id`: Links to commitment
- `status`: Outcome classification
- `explanation`: Why this status was assigned
- `actual_value`: Result achieved (if quantifiable)
- `variance`: % difference from target
- `evidence`: Quote from verification filing
- `verification_filing`: Which filing was used to verify

**Size:** ~10-100 KB depending on number of commitments

### 4. `{TICKER}_score.json`

Credibility scores and analysis.

**Structure:**
```json
{
  "overall_score": 83.3,
  "grade": "B+",
  "total_commitments": 20,
  "verifiable_commitments": 18,
  "fulfilled_count": 13,
  "partially_fulfilled_count": 4,
  "not_fulfilled_count": 1,
  "abandoned_count": 0,
  "pending_count": 2,
  "fulfillment_rate": 72.2,
  "partial_rate": 22.2,
  "miss_rate": 5.6,
  "category_scores": {
    "financial_target": {
      "score": 80.0,
      "count": 5,
      "fulfilled": 3,
      "partial": 2,
      "missed": 0
    },
    "capital_allocation": {
      "score": 90.0,
      "count": 4,
      "fulfilled": 3,
      "partial": 1,
      "missed": 0
    }
  },
  "specificity_index": 7.2,
  "red_flags": [],
  "time_trends": {
    "trend": "stable",
    "early_score": 82.0,
    "late_score": 84.5,
    "change": 2.5,
    "description": "Credibility stable (around 83.0)"
  }
}
```

**Purpose:** Final credibility assessment with quantitative scores.

**Key metrics:**
- `overall_score`: 0-100 credibility score
- `grade`: Letter grade (A+ to F)
- Outcome counts and rates
- `category_scores`: Performance by commitment type
- `specificity_index`: Average commitment quality
- `red_flags`: Concerning patterns identified
- `time_trends`: Improving, declining, or stable

**Size:** ~5-20 KB

### 5. `{TICKER}_report.md`

Professional markdown report suitable for equity analysts.

**Structure:**
```markdown
# Management Integrity Analysis
## Apple Inc (AAPL)

## Executive Summary

**Overall Credibility Score:** 83.3/100 (B+)

...

## Category Performance Breakdown

...

## Red Flags

...

## Notable Successes

...

## Detailed Findings

...
```

**Purpose:** Comprehensive professional report with all findings.

**Sections:**
1. Executive Summary
2. Company Overview
3. Credibility Score Details
4. Category Performance
5. Time Trends
6. Red Flags (if any)
7. Notable Successes
8. Notable Misses
9. Detailed Findings
10. Methodology
11. Limitations

**Size:** ~20-100 KB depending on analysis depth

## Data Flow

```
1. MCP Tools → {TICKER}_sec_data.json
   ↓
2. Commitment Extraction → {TICKER}_commitments.json
   ↓
3. Outcome Verification → {TICKER}_outcomes.json
   ↓
4. Credibility Scoring → {TICKER}_score.json
   ↓
5. Report Generation → {TICKER}_report.md
```

## File Management

### Viewing Files

**JSON files:**
```bash
# Pretty print
python -m json.tool AAPL_commitments.json

# View in Claude Code
# Just ask: "Show me the commitments for AAPL"
```

**Markdown report:**
```bash
# View in terminal
cat AAPL_report.md

# View in browser
open AAPL_report.md
```

### Cleaning Up

```bash
# Remove all files for a specific company
rm AAPL_*

# Remove all analysis files
rm *.json *.md

# Keep only reports
rm *_sec_data.json *_commitments.json *_outcomes.json *_score.json
```

### Archiving

```bash
# Create archive of all AAPL analysis
tar -czf AAPL_analysis_$(date +%Y%m%d).tar.gz AAPL_*

# Extract archive
tar -xzf AAPL_analysis_20251108.tar.gz
```

## Data Retention

**Recommendation:** Keep analysis files for:
- **SEC data:** Can be re-fetched, safe to delete after analysis
- **Commitments:** Keep for reference and trend analysis
- **Outcomes:** Keep for tracking over time
- **Scores:** Keep for historical comparison
- **Reports:** Keep for research and audit trail

## Privacy and Security

**Data sensitivity:**
- All data is from public SEC filings (not confidential)
- No personal information
- No proprietary data
- Safe to share reports with team

**Best practices:**
- Don't commit large SEC data files to git
- Keep analysis files local or in secure storage
- Share reports via secure channels
- Be mindful of material non-public information in discussions

## Rerunning Analysis

You can rerun analysis on the same company:

```bash
# Remove old files
rm AAPL_*

# Run fresh analysis
/mgmt-integrity TICKER:AAPL
```

Or keep old files and rename:

```bash
# Archive previous run
mkdir archive_20251108
mv AAPL_* archive_20251108/

# Run new analysis
/mgmt-integrity TICKER:AAPL
```

## Troubleshooting

**Missing files:**
- Check that analysis completed without errors
- Verify ANTHROPIC_API_KEY is set
- Ensure MCP tools are working

**Corrupted files:**
- Delete and rerun analysis
- Check for partial writes (file size 0)

**Large file sizes:**
- SEC data files can be 1-5 MB (normal)
- If > 10 MB, may have excessive text extraction

## Data Schema Versions

**Current version:** 1.0.0

If schema changes in future versions, migration scripts will be provided.

---

**Last Updated:** November 2025
