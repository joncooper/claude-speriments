# Testing Guide - Management Integrity Agent

This guide explains how to test the Management Integrity Agent to ensure it's working correctly.

## Prerequisites

Before testing, ensure you have:

1. ✅ SEC EDGAR MCP server installed and configured
2. ✅ ANTHROPIC_API_KEY environment variable set
3. ✅ Slash command installed (`~/.claude/commands/mgmt-integrity.md`)
4. ✅ Claude Code restarted after MCP installation

## Quick Test

### Test with Apple (AAPL)

Apple is an excellent test case because:
- Large, mature company with consistent commitments
- Extensive SEC filing history
- Generally good management credibility
- Expected score: 75-90 (B to A range)

```
/mgmt-integrity TICKER:AAPL
```

**Expected results:**
- ~15-25 commitments extracted
- ~70-85% fulfillment rate
- Few or no red flags
- Score in 75-90 range (B+ to A-)
- Stable or improving trend

**Runtime:** 5-10 minutes

### Test with Tesla (TSLA)

Tesla provides an interesting contrast:
- Aggressive growth company
- Ambitious commitments (product launches, production targets)
- Mixed track record
- Expected score: 60-75 (C to B range)

```
/mgmt-integrity TICKER:TSLA
```

**Expected results:**
- ~10-20 commitments extracted
- ~50-70% fulfillment rate
- Possible red flags (ambitious timelines)
- Score in 60-75 range (C+ to B)
- Variable trend

## Component Testing

### Test 1: Data Fetching via MCP

**Objective:** Verify SEC EDGAR MCP integration works

```python
# In Claude Code, run this test
import sys
sys.path.insert(0, 'agents/equity-mgmt-integrity/lib')
from sec_data import load_sec_data

# After running /mgmt-integrity TICKER:AAPL once
data = load_sec_data('AAPL')

print(f"Company: {data['company_info']['name']}")
print(f"Filings: {len(data['filings'])}")
print(f"First filing: {data['filings'][0]['filing_type']} - {data['filings'][0]['filing_date']}")
```

**Expected output:**
```
Company: Apple Inc
Filings: 12
First filing: 10-K - 2021-10-29
```

**What to verify:**
- Company info loaded correctly
- At least 10-12 filings present
- Filings have md_a_text and business_text fields
- Dates are in expected range (last 3 years)

### Test 2: Commitment Extraction

**Objective:** Verify AI commitment extraction works

```python
import sys
sys.path.insert(0, 'agents/equity-mgmt-integrity/lib')
from commitment_extractor import CommitmentExtractor
from sec_data import load_json

commitments = load_json('agents/equity-mgmt-integrity/data/AAPL_commitments.json')

print(f"Total commitments: {len(commitments)}")
print(f"\nFirst commitment:")
print(f"  Text: {commitments[0]['commitment_text'][:100]}...")
print(f"  Category: {commitments[0]['category']}")
print(f"  Specificity: {commitments[0]['specificity']}/10")
print(f"  Verifiable: {commitments[0]['verifiable']}")
print(f"  Timeline: {commitments[0]['timeline']}")
```

**What to verify:**
- All commitments have specificity >= 4
- All commitments are verifiable=True
- commitment_text contains actual quotes
- Categories are one of: financial_target, capital_allocation, strategic_initiative, operational_improvement, product_launch
- Timelines are specific (not vague like "future")
- Each has unique commitment_id

### Test 3: Outcome Verification

**Objective:** Verify AI outcome verification works

```python
import sys
sys.path.insert(0, 'agents/equity-mgmt-integrity/lib')
from sec_data import load_json

outcomes = load_json('agents/equity-mgmt-integrity/data/AAPL_outcomes.json')

print(f"Total outcomes: {len(outcomes)}")

# Count by status
from collections import Counter
statuses = Counter(o['status'] for o in outcomes)

for status, count in statuses.items():
    print(f"  {status}: {count}")

print(f"\nFirst fulfilled commitment:")
fulfilled = [o for o in outcomes if o['status'] == 'fulfilled']
if fulfilled:
    print(f"  Commitment: {fulfilled[0]['commitment_id']}")
    print(f"  Explanation: {fulfilled[0]['explanation'][:100]}...")
    print(f"  Confidence: {fulfilled[0]['confidence']}")
```

**What to verify:**
- All outcomes have valid status (fulfilled, partially_fulfilled, not_fulfilled, abandoned, pending, unverifiable)
- Outcomes have explanations
- Confidence scores are 0.0-1.0
- Evidence quotes are present for non-pending statuses
- Variances calculated for quantitative commitments

### Test 4: Credibility Scoring

**Objective:** Verify scoring calculations are correct

```python
import sys
sys.path.insert(0, 'agents/equity-mgmt-integrity/lib')
from sec_data import load_json

score = load_json('agents/equity-mgmt-integrity/data/AAPL_score.json')

print(f"Overall Score: {score['overall_score']}/100 ({score['grade']})")
print(f"\nBreakdown:")
print(f"  Fulfilled: {score['fulfilled_count']} ({score['fulfillment_rate']:.1f}%)")
print(f"  Partial: {score['partially_fulfilled_count']} ({score['partial_rate']:.1f}%)")
print(f"  Missed: {score['not_fulfilled_count'] + score['abandoned_count']} ({score['miss_rate']:.1f}%)")

# Verify calculation
total = score['fulfilled_count'] + score['partially_fulfilled_count'] + score['not_fulfilled_count'] + score['abandoned_count']
expected_score = (score['fulfilled_count'] + 0.5 * score['partially_fulfilled_count']) / total * 100

print(f"\nManual calculation: {expected_score:.1f}")
print(f"Matches score: {abs(expected_score - score['overall_score']) < 0.1}")

print(f"\nCategory scores:")
for category, stats in score['category_scores'].items():
    print(f"  {category}: {stats['score']:.1f} ({stats['count']} commitments)")

print(f"\nRed flags: {len(score['red_flags'])}")
for flag in score['red_flags']:
    print(f"  - {flag['description']}")

print(f"\nTrend: {score['time_trends']['trend']}")
```

**What to verify:**
- Score calculation matches manual calculation
- Grade is correct for score (A+ for 95+, A for 90+, etc.)
- Fulfillment/partial/miss rates sum to ~100%
- Category scores are calculated for each category present
- Red flags have descriptions and severity levels
- Time trend is one of: improving, declining, stable, insufficient_data

### Test 5: Report Generation

**Objective:** Verify report generation works

```python
import sys
sys.path.insert(0, 'agents/equity-mgmt-integrity/lib')
from sec_data import load_json
from report_generator import ManagementIntegrityReport

# Load all data
data = load_json('agents/equity-mgmt-integrity/data/AAPL_sec_data.json')
commitments = load_json('agents/equity-mgmt-integrity/data/AAPL_commitments.json')
outcomes = load_json('agents/equity-mgmt-integrity/data/AAPL_outcomes.json')
score = load_json('agents/equity-mgmt-integrity/data/AAPL_score.json')

report_data = {
    'company_info': data['company_info'],
    'commitments': commitments,
    'outcomes': outcomes,
    'score': score
}

report = ManagementIntegrityReport(report_data)

# Generate summary
summary = report.generate_summary()
print(summary)

# Check report file exists
import os
report_path = 'agents/equity-mgmt-integrity/data/AAPL_report.md'
print(f"\nReport exists: {os.path.exists(report_path)}")

if os.path.exists(report_path):
    with open(report_path) as f:
        content = f.read()
    print(f"Report length: {len(content)} characters")
    print(f"Contains score: {'Overall Credibility Score' in content}")
```

**What to verify:**
- Summary displays correctly
- Report file is created
- Report contains all required sections
- Markdown formatting is correct
- No missing data placeholders

## Manual Verification

### Spot Check Commitments

Manually verify a few extracted commitments:

1. Open the report: `agents/equity-mgmt-integrity/data/AAPL_report.md`
2. Find the "Notable Successes" or "Detailed Findings" section
3. Pick a commitment and check:
   - Is it actually a forward-looking commitment?
   - Is it specific and verifiable?
   - Does the timeline make sense?
   - Is the category classification correct?

### Spot Check Outcomes

Manually verify a few outcomes:

1. Look at `AAPL_commitments.json` and find a commitment
2. Look at `AAPL_outcomes.json` and find the matching outcome
3. Verify:
   - Does the status make sense?
   - Is the explanation reasonable?
   - If quantitative, is the variance calculation correct?
   - Does the evidence quote support the determination?

### Verify Score Logic

Check the scoring makes sense:

```python
# Manual calculation
fulfilled = 13  # from score.json
partial = 4
total = 18

score = (fulfilled + 0.5 * partial) / total * 100
# = (13 + 2) / 18 * 100 = 83.3

print(f"Expected: 83.3")
print(f"Actual: {score}")
```

## Known Issues and Limitations

### Expected Variations

- **AI non-determinism**: Running twice may extract slightly different commitments
- **Confidence scores vary**: AI confidence depends on clarity of filing language
- **Some pending commitments**: Normal for recent commitments with long timelines
- **Category classification**: May vary slightly between runs

### Common Issues

**Issue: No commitments found**
- Some companies make few specific commitments
- Try different company (AAPL, MSFT, GOOGL are good test cases)
- Check MD&A sections were properly extracted

**Issue: Most commitments marked as unverifiable**
- Recent filings may not have had time for verification
- Need longer time period or older filings

**Issue: Low confidence scores**
- Vague filing language makes verification difficult
- This is expected for some industries/companies

**Issue: API rate limits**
- Anthropic API has rate limits
- Agent will fail gracefully with error message
- Wait and retry

## Test Cases

### Good Management (Expected A/B grades)

- **AAPL** (Apple): Consistent, reliable
- **MSFT** (Microsoft): Strong track record
- **GOOGL** (Google/Alphabet): Generally delivers

### Mixed Management (Expected C grades)

- **TSLA** (Tesla): Ambitious, mixed results
- Many growth companies fall into this category

### Poor Management (Expected D/F grades)

- Companies with history of broken promises
- Recent IPOs that overpromised
- Companies facing difficulties

## Debugging

### Enable Verbose Output

Add print statements to see what's happening:

```python
# In commitment_extractor.py, add before API call:
print(f"Extracting from {len(text)} chars of text...")

# In outcome_tracker.py, add:
print(f"Verifying commitment: {commitment['commitment_text'][:50]}...")
print(f"Against filing: {verification_metadata['filing_date']}")
```

### Check API Keys

```bash
# Verify environment variable is set
echo $ANTHROPIC_API_KEY

# Should output your API key (sk-ant-...)
```

### Check MCP Tools

In Claude Code, ask:

```
What MCP tools are available?
```

Should see tools like:
- mcp__sec_edgar__get_company_facts
- mcp__sec_edgar__get_submissions

### Inspect Data Files

All intermediate data is saved to JSON:

```bash
# Check files exist
ls -lh agents/equity-mgmt-integrity/data/AAPL_*

# Pretty print a file
python -m json.tool agents/equity-mgmt-integrity/data/AAPL_commitments.json | head -50
```

## Performance Benchmarks

**Expected runtimes (on typical hardware):**

- Data fetching via MCP: 1-3 minutes
- Commitment extraction (15 commitments): 2-4 minutes
- Outcome verification (15 commitments): 2-4 minutes
- Scoring: < 1 second
- Report generation: < 1 second

**Total:** 5-15 minutes per company

**API costs (approximate):**
- Commitment extraction: $0.20-0.50 per company
- Outcome verification: $0.20-0.50 per company
- Total: ~$0.40-1.00 per analysis

## Success Criteria

The agent is working correctly if:

- ✅ Successfully fetches SEC data via MCP
- ✅ Extracts 5-30 commitments (varies by company)
- ✅ All commitments have specificity >= 4 and verifiable=True
- ✅ Outcomes are assigned appropriate statuses
- ✅ Score calculation is mathematically correct
- ✅ Letter grade matches score threshold
- ✅ Report is comprehensive and professional
- ✅ Results make intuitive sense for the company

## Reporting Issues

If you encounter issues:

1. Check Prerequisites section above
2. Try the Quick Test with AAPL
3. Run Component Tests to isolate the problem
4. Check Known Issues section
5. Enable Debugging output
6. Report issue with:
   - Company tested
   - Error messages
   - Data files (if applicable)
   - Expected vs actual behavior

---

**Last Updated:** November 2025
