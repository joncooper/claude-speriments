# v1.0 Sprint Plan - 7 Days to Proof of Value

**Goal:** Working end-to-end system that ONE analyst can use for real research by November 15th.

## Success Criteria

- ✅ Analyst can research a company they don't cover yet
- ✅ System captures their thinking in structured way
- ✅ Agent does deep research autonomously
- ✅ Everything persists in git
- ✅ Demonstrates clear time savings (4+ hours)
- ✅ Foundation for everything else

## What We're Building: The One Workflow That Matters

**Company Deep Dive**

```
Analyst workflow:
1. /deep-dive SNOW --depth=standard
2. Agent runs for 30-60 min, does comprehensive research
3. Outputs structured analysis to git
4. Analyst reviews, refines, builds thesis
5. /thesis-snapshot SNOW → formatted for PM
```

**This proves:**
- Agents can do real research
- Git storage works
- Data access works
- Output is valuable
- System is usable

## 7-Day Build Plan

### Day 1 (Nov 8): Foundation & Structure

**Morning: Set up repository** (2 hours)
```bash
# Create repo structure
mkdir analyst-workspace && cd analyst-workspace
git init

# Directory structure
mkdir -p .claude/{commands,agents}
mkdir -p .infrastructure/{cache,logs}
mkdir -p coverage patterns

# Create basic docs
touch README.md
touch .claude/commands/README.md
```

**Afternoon: Build 3 essential slash commands** (4 hours)

1. **`/init-coverage [ticker]`** - Create folder structure for new company
2. **`/thesis-snapshot [ticker]`** - Display current thesis
3. **`/costs`** - Show spending

These are SIMPLE, no agents, just prove slash commands work.

**Evening: Test with one company manually** (2 hours)
- `/init-coverage AAPL`
- Manually create `coverage/AAPL/thesis.md`
- `/thesis-snapshot AAPL` displays it
- ✅ Proves git storage + commands work

**Deliverable:** Basic repo structure, 3 working commands

---

### Day 2 (Nov 9): Data Access Layer

**Morning: SEC EDGAR MCP Server** (4 hours)

```python
# .claude/mcp-servers/sec-edgar/server.py
# Simple wrapper around SEC EDGAR API
# Functions:
# - get_latest_filing(ticker, form_type)
# - download_filing(url)
# - extract_text(html)

# Key: Add aggressive caching
# .infrastructure/cache/sec/{ticker}/{form}-{date}.json
```

**Afternoon: Market Data MCP Server** (3 hours)

```python
# .claude/mcp-servers/market-data/server.py
# Use yfinance (simple, free, good enough)
# Functions:
# - get_price_history(ticker, period)
# - get_key_stats(ticker)
# - get_peers(ticker)

# Cache everything
```

**Evening: Test data access** (1 hour)
- Fetch AAPL 10-K
- Fetch AAPL price history
- Verify caching works
- ✅ Can access external data

**Deliverable:** 2 working MCP servers with caching

---

### Day 3 (Nov 10): First Agent - The Core

**All day: Build `research-initiation-agent`** (8 hours)

This is the heart of v1.0. Make it good.

```markdown
# .claude/agents/research-initiation-agent/prompt.md

You are a research analyst doing first-pass research on a company.

## Process

### Step 1: Plan (show to user)
Review what's already known about {ticker}.
Create research plan covering:
- Business model & operations
- Financial performance
- Competitive position
- Key risks
- Investment highlights

Wait for user approval.

### Step 2: Gather Data
Use MCP servers to fetch:
- Latest 10-K, 10-Q
- Recent earnings transcript
- Stock performance (3 years)
- Peer group financials

Save all to coverage/{ticker}/.agent-data/

### Step 3: Analyze
Go section by section:
1. Business Model
2. Financials (last 3 years)
3. Competition
4. Risks

Write detailed analysis to coverage/{ticker}/initial-analysis.md

### Step 4: Synthesize (show to user)
Create:
- Executive summary (3-5 bullets)
- Key questions needing more research
- Preliminary view (if confident enough)

### Step 5: Output
Write structured files to coverage/{ticker}/
```

**Test it:**
```bash
# Run agent on a company you know well (to validate quality)
/deep-dive AAPL --depth=standard

# Check outputs:
- Is analysis comprehensive?
- Are facts accurate?
- Is structure clear?
- Would this save analyst time?
```

**Deliverable:** Working research-initiation-agent that produces valuable output

---

### Day 4 (Nov 11): Polish Agent + Add Observability

**Morning: Improve agent based on Day 3 test** (4 hours)
- Better prompting
- Better structure
- Handle edge cases (missing data, etc.)
- Add cost estimates before expensive operations

**Afternoon: Add observability** (3 hours)

```python
# Simple cost tracking
# .infrastructure/costs.db (SQLite)

CREATE TABLE agent_runs (
    id INTEGER PRIMARY KEY,
    timestamp TEXT,
    agent_type TEXT,
    ticker TEXT,
    duration_seconds INTEGER,
    cost_usd REAL,
    input_tokens INTEGER,
    output_tokens INTEGER,
    status TEXT,
    output_path TEXT
);
```

```bash
# Update /costs command to query database
```

**Evening: End-to-end test** (1 hour)
- Pick a company you DON'T know well
- Run `/deep-dive [ticker]`
- See if output is actually useful
- ✅ Validates the whole system

**Deliverable:** Polished agent + cost tracking working

---

### Day 5 (Nov 12): Additional Workflows

**Morning: Build `/earnings-analysis [ticker]`** (3 hours)

Simpler agent for quick earnings analysis:
1. Fetch latest earnings transcript + 10-Q
2. Compare to prior quarter
3. Extract: beats/misses, guidance changes, surprises
4. Write coverage/{ticker}/earnings-{date}.md

**Afternoon: Build useful utility commands** (3 hours)

```bash
/pattern-add [observation]
# Quickly log insights to patterns/

/question-log [ticker] [question]
# Track questions for management meetings

/conviction-log [ticker] [score] [rationale]
# Track conviction over time

/format-for-pm [content]
# Reformat for busy PM
```

**Evening: Build `/search [query]`** (2 hours)

```python
# Simple full-text search across git repo
# Use ripgrep under the hood
# Returns files + line numbers + context
```

**Deliverable:** 5-6 total working commands + 2 agents

---

### Day 6 (Nov 13): Real-World Test

**Morning: Documentation** (2 hours)
```markdown
# README.md with:
- Quick start guide
- Command reference
- Agent descriptions
- Examples

# Screencast: 5-minute demo video
```

**Afternoon: Full real-world test** (4 hours)
- Give to ONE analyst (could be you)
- Pick a real company they need to research
- Use ONLY the system (don't cheat with manual research)
- Note: What works? What breaks? What's missing?

**Evening: Bug fixes** (2 hours)
- Fix critical issues found during testing
- Improve error messages
- Add missing features if truly blocking

**Deliverable:** System that works for real analyst doing real work

---

### Day 7 (Nov 14): Polish & Ship

**Morning: Final polish** (3 hours)
- Error handling
- Help text for commands
- Examples in docs
- Clean up code

**Afternoon: Package for demo** (3 hours)
```bash
# Create demo script
demo/
├── demo-script.md           # Step-by-step demo flow
├── example-output/          # Pre-run examples
│   ├── SNOW-deep-dive/
│   └── DDOG-earnings/
└── demo-video.mp4          # Recording of demo
```

**Evening: Prep for Monday demo** (2 hours)
- Test on fresh machine (does setup work?)
- Run through demo script 2-3 times
- Have backup examples ready
- ✅ Ready to show someone!

**Deliverable:** Shippable v1.0

---

## Scope: What's IN v1.0

### Commands (6 total)
1. ✅ `/deep-dive [ticker]` - Launch research agent
2. ✅ `/earnings-analysis [ticker]` - Quick earnings review
3. ✅ `/init-coverage [ticker]` - Set up new company
4. ✅ `/thesis-snapshot [ticker]` - Display current view
5. ✅ `/search [query]` - Full-text search
6. ✅ `/costs` - Spending report

### Agents (2 total)
1. ✅ `research-initiation-agent` - Deep dive research
2. ✅ `earnings-analysis-agent` - Earnings review

### MCP Servers (2 total)
1. ✅ `sec-edgar` - SEC filings access
2. ✅ `market-data` - Price data & fundamentals

### Infrastructure
- ✅ Git-based storage
- ✅ Local file caching
- ✅ SQLite for costs/logs
- ✅ Simple observability

### Documentation
- ✅ README with quick start
- ✅ Command reference
- ✅ Example outputs
- ✅ 5-min demo video

## Scope: What's NOT in v1.0

❌ Vector database / semantic search
❌ Advanced document extraction (doclify)
❌ Multiple analyst collaboration features
❌ Web interface
❌ Real-time data feeds
❌ Complex eval framework
❌ 10+ different agents
❌ Firm-wide knowledge graph
❌ Advanced visualizations
❌ Mobile app
❌ Anything not critical for ONE analyst to get value

## The Demo Flow (5 Minutes)

### Setup (30 sec)
"This is Claude Code configured for equity research.
I have 6 slash commands and 2 autonomous agents."

[Show: ls .claude/commands]

### Use Case: Research a New Company (3 min)

"I need to research Snowflake (SNOW). I'll use /deep-dive."

[Run: /deep-dive SNOW --depth=standard]

"The agent will:
1. Plan the research approach [shows plan]
2. Fetch SEC filings and market data [shows data gathering]
3. Analyze systematically [shows analysis in progress]
4. Output structured research [shows final output]

This takes 30-45 minutes. Here's one I ran earlier..."

[Show: coverage/SNOW/initial-analysis.md]
[Show: coverage/SNOW/open-questions.md]

"Everything is in git, version controlled, human-readable."

### What This Enables (1 min)

"This would have taken me 4-6 hours manually.
Agent did it in 45 minutes for $5.
I can now spend time on the high-value analysis.

And the system learns:
- All research is searchable: /search 'pricing power'
- Patterns get captured and reused
- Thesis evolution is tracked
- Everything is auditable"

### What's Next (30 sec)

"v1.0 proves the concept.
Next: More agents, firm-wide collaboration, advanced features.
But this already makes me a better analyst."

## Critical Decisions for Speed

### Technology Choices

| Decision | Choice | Why |
|----------|--------|-----|
| Language | Python | Fast to write, great libs |
| MCP Framework | Use official SDK | Don't reinvent |
| File Format | Markdown + YAML | Human-readable, git-friendly |
| Database | SQLite | No server, good enough |
| Data Source | Free APIs | $0 cost, good enough |
| Document Parsing | Claude Read tool | Already available |
| Search | ripgrep | Fast, already have it |
| Observability | JSON logs + SQLite | Simple, works |

### What We're NOT Debating

- No cloud infrastructure debates (local first)
- No "which vector DB" (not using one)
- No "build vs buy" for complex features (not building them)
- No architecture astronaut stuff (ship working code)

## Risk Mitigation

**What could go wrong?**

1. **"Agent doesn't produce quality output"**
   - Mitigation: Test daily, iterate prompts
   - Backup: Simplify scope, make it a structured research assistant vs autonomous

2. **"MCP servers are buggy"**
   - Mitigation: Start with very simple wrappers
   - Backup: Mock data if needed for demo

3. **"Can't finish in time"**
   - Mitigation: Daily checkpoints, cut scope ruthlessly
   - Backup: Ship v0.9 that does less but works perfectly

4. **"No one to test with"**
   - Mitigation: You test it yourself on real research
   - Backup: Create realistic test scenarios

## Daily Checkpoints

End of each day, ask:
1. ✅ Can I demo what I built today?
2. ✅ Does it work end-to-end?
3. ✅ What's blocking tomorrow?
4. ✅ Am I on track for Friday?

If answer to #4 is "no" → cut scope immediately.

## Success Metrics for v1.0

By Nov 15th, can you say YES to all of these?

- ✅ I can run `/deep-dive [ticker]` on a real company
- ✅ Agent completes in < 60 minutes
- ✅ Output is actually useful (would save me hours)
- ✅ Everything persists in git
- ✅ I can find things with `/search`
- ✅ I know what it cost me (`/costs`)
- ✅ I can show this to someone and they get it
- ✅ Foundation is solid for building more

If 8/8 = Ship it! 🚢
If 6-7/8 = Almost there, polish over weekend
If <6/8 = Cut scope, focus on core workflow

## What Happens After v1.0?

**Week 2 (Nov 15-22): Get feedback + iterate**
- Show to 2-3 analysts
- What do they love? What's confusing?
- What's the next most valuable agent/command?

**Week 3-4: v1.1 with top 3 requested features**

**Month 2: Scale to 5-10 analysts**

**Month 3: Firm-wide rollout planning**

But that's later. Right now: **Ship v1.0 by Nov 15th.**

## Actual Build Recommendation

**You should focus on ONLY this:**

1. **Days 1-3:** Build the deep-dive agent + data access. Make it GREAT.
2. **Day 4:** Test it for real. Fix what breaks.
3. **Day 5:** Add 2-3 utility commands to round it out.
4. **Day 6:** Documentation + demo prep.
5. **Day 7:** Polish + buffer.

**If you do this, you'll have something genuinely impressive by Friday.**

The temptation will be to add more agents, more features, more complexity. **Resist.**

One working end-to-end workflow that saves 4 hours of analyst time is worth 10 half-built features.

## The Core Principle

**Proof of Value = Simple + Useful**

One workflow that makes an analyst say:
*"Holy shit, this just saved me 4 hours."*

That's all you need for v1.0.
