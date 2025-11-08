# Infrastructure Stack Decisions

## Infrastructure Philosophy

**Principle 1: Git-First, Database-When-Needed**
- Git is perfect for: documents, code, structured data, version history, human-readable
- Database is for: high-volume queries, relationships, search at scale
- Start git-first, add DB incrementally

**Principle 2: Compose Standard Tools**
- Don't build what exists
- Use MCP servers to wrap external services
- Keep infrastructure swappable

**Principle 3: Local-First, Cloud-When-Necessary**
- Analyst's machine is the truth
- Cloud for: collaboration, compute-heavy tasks, always-on monitoring
- Avoid "your research is trapped in our system"

## The Minimal Viable Infrastructure Stack

### TIER 0: Core (Must Have Week 1)

```
┌─────────────────────────────────────────────────┐
│  Analyst's Machine                               │
│                                                  │
│  analyst-workspace/                              │
│  ├── .claude/                                    │
│  ├── coverage/                                   │
│  ├── patterns/                                   │
│  └── .infrastructure/                            │
│      ├── logs/              # Agent execution    │
│      ├── cache/             # HTTP/API cache     │
│      └── costs.db           # SQLite for costs   │
│                                                  │
│  Git → Remote (GitHub/GitLab)                   │
│  └── Backup, collaboration, audit trail         │
└─────────────────────────────────────────────────┘
```

**What you need:**
- ✅ Git repo
- ✅ SQLite for lightweight queries (costs, time series)
- ✅ Local file cache for API responses
- ✅ That's it!

### TIER 1: Data Access Layer (Week 2-3)

#### 1.1 SEC Filing Access ⭐ ESSENTIAL

**Don't build it yourself. Use MCP server wrapper around SEC EDGAR API.**

```python
# .claude/mcp-servers/sec-edgar/server.py

class SECEdgarServer:
    def get_filing(self, ticker: str, form_type: str, date: str):
        """Fetch specific filing"""
        # Check local cache first
        # Fetch from SEC EDGAR (free API)
        # Rate limit: 10 requests/second max
        # Cache response locally
        # Return structured data

    def get_latest_filings(self, ticker: str, limit: int = 10):
        """Get recent filings for ticker"""

    def search_filings(self, ticker: str, keywords: list):
        """Search within filings"""
```

**Why this approach:**
- SEC EDGAR API is free, comprehensive, official
- Rate limits are generous (10 req/sec)
- Cache locally so re-reading is instant
- MCP server = swappable later if needed

**Storage:**
```
.infrastructure/cache/sec-filings/
├── AAPL/
│   ├── 10-K-2024-01-27.json       # Raw filing data
│   ├── 10-K-2024-01-27.txt        # Text extract
│   └── 10-K-2024-01-27.meta.json  # Metadata
```

**Cost:** $0

#### 1.2 Document Extraction ⭐ ESSENTIAL

**Start simple, upgrade if needed.**

```python
# Phase 1: Use what you have (Week 2)
- Claude can read PDFs directly (built into Read tool)
- For HTML filings: Use BeautifulSoup
- For tables: Use pandas.read_html()

# Phase 2: Add if needed (Month 2+)
- doclify: If Claude struggles with complex tables
- Unstructured.io: If you need batch processing
- Docling: If you need advanced layout analysis

# DON'T start with heavy tooling
```

**Practical approach:**
```markdown
# Agent workflow for filing analysis

1. Fetch filing via SEC MCP server → HTML
2. Parse HTML → structured sections
3. Pass relevant sections to Claude
4. Claude extracts what matters
5. Save structured output to git

# Only add doclify if Claude consistently fails on tables
```

#### 1.3 Stock Price Data ⭐ ESSENTIAL

**Use free APIs initially, upgrade only if needed.**

```python
# .claude/mcp-servers/market-data/server.py

class MarketDataServer:
    """
    Tier 1: Free APIs
    - Yahoo Finance (yfinance) - good enough for most use cases
    - Alpha Vantage (free tier) - 500 calls/day
    - FRED (Federal Reserve) - macro data

    Tier 2: Paid (only if analysts need real-time)
    - Polygon.io - $200/month
    - IEX Cloud - usage-based
    """

    def get_price_history(self, ticker: str, start: str, end: str):
        """OHLCV data"""

    def get_fundamentals(self, ticker: str):
        """Key metrics"""

    def get_peers(self, ticker: str):
        """Peer group"""
```

**Storage:**
```
.infrastructure/cache/market-data/
├── AAPL/
│   ├── prices-daily.csv         # Price history
│   ├── fundamentals.json        # Key metrics
│   └── updated-2024-11-07.txt   # Cache timestamp
```

**Cost:** $0 to start, $200/month if you need real-time

### TIER 2: Intelligence Layer (Month 2-3)

#### 2.1 Vector DB / RAG ⚠️ ADD WHEN NEEDED

**Don't start with this. Add when you hit specific pain points.**

**When you DON'T need it (initially):**
- Coverage universe is 20-50 stocks per analyst
- Git grep is fast enough for keyword search
- Agents can read relevant files directly
- Context windows are 200K tokens

**When you DO need it (later):**
- Firm has 10+ years of research (thousands of reports)
- Need semantic search ("find similar situations")
- Need cross-analyst knowledge discovery
- Context window limitations hit

**If/when you add it:**
```python
# Use: pgvector (Postgres extension)
# Why:
# - Runs locally or cloud
# - Standard SQL + vectors
# - No vendor lock-in
# - Can query: "Find research similar to [current situation]"

# Alternative: Qdrant (if you want dedicated vector DB)
```

**Practical timeline:**
```markdown
# Month 1-3: No vector DB
- Store everything in git
- Use grep/ripgrep for search
- Agents read relevant files

# Month 4+: Evaluate need
- Are analysts saying "I can't find X"?
- Are agents hitting context limits?
- Do we need semantic search?

# If yes: Add pgvector
```

#### 2.2 Context Management ⚠️ PROBABLY NOT NEEDED

**Context7 solves a problem you might not have.**

**Claude Code + Git already gives you:**
- Read tool: Load specific files into context
- Grep tool: Find relevant content
- Task tool: Agents can manage their own context
- Git structure: Logical organization

**You need context management if:**
- Agents repeatedly load same 10MB file
- Constantly hitting context limits
- Spending too much on input tokens

**Better approach:**
```markdown
# Smart file organization (free)
coverage/AAPL/
├── summary.md          # 1 page, always load this
├── thesis.md           # 2-3 pages, load when needed
├── detailed-analysis/  # Only load specific sections
│   ├── business-model.md
│   ├── financials.md
│   └── competition.md
└── archive/           # Old stuff, rarely loaded

# Agent loads: summary.md first
# Then: Only load specific detailed sections needed
# Result: No context management needed
```

**If you do need it:**
- Use prompt caching (Claude feature, built-in)
- Cache stable content (company background)
- Regenerate dynamic content (recent events)

### TIER 3: Operations Layer (Month 2-4)

#### 3.1 Observability & Eval ⭐ ESSENTIAL (but keep simple)

**Don't build a fancy platform. Use files + SQLite.**

```python
# .infrastructure/logs/

# Agent execution logs (JSON Lines)
agent-runs.jsonl:
{"timestamp": "2024-11-07T10:30:00Z", "agent": "research-initiation",
 "ticker": "AAPL", "duration_sec": 1834, "cost_usd": 4.23,
 "input_tokens": 50000, "output_tokens": 15000, "status": "success"}

# Cost tracking (SQLite)
costs.db:
  table: agent_costs
    - id, timestamp, agent_type, ticker, cost, tokens_in, tokens_out

# Eval results (JSON)
evals/
├── 2024-11-07-earnings-analysis-eval.json
└── 2024-11-08-pattern-finder-eval.json
```

**Simple dashboard:**
```python
# .claude/commands/infrastructure/costs-report.md

/costs-report [period]

Shows:
- Total spend by agent type
- Cost per ticker
- Token usage trends
- Slowest agents
- Failed runs

Just queries SQLite and prints table
```

**Eval approach:**
```markdown
# Start with human eval
- Analyst rates agent output: 1-5 stars
- Collects feedback: what was good/bad?
- Logs to evals/ directory

# Later add automated eval
- Does output match expected format?
- Are all required sections present?
- Are claims sourced?
- Did it complete in time/budget?
```

**Observability tools:**
- **Start:** Just files (own your data)
- **Later:** Langfuse (free tier) - if you want dashboards
- **Advanced:** Weights & Biases - if doing serious eval

#### 3.2 Persistence Strategy ⭐ CRITICAL DECISION

**The key question: What's the source of truth?**

**Option A: Git-First (recommended for starting)**
```
Source of Truth: Git repo

Advantages:
✅ Version control built-in
✅ Human-readable (markdown)
✅ Auditable (every change tracked)
✅ Portable (analyst owns their data)
✅ Collaboration-ready (branches, PRs)
✅ Works offline
✅ Free

Disadvantages:
❌ No complex queries
❌ No full-text search at scale
❌ Not ideal for high-frequency writes
❌ Can't handle 1M+ documents efficiently

Best for:
- Individual analyst (20-50 stocks)
- Team (5-10 analysts)
- Up to ~10GB data
- Research documents, models, insights
```

**Option B: Hybrid (recommended for scaling)**
```
Source of Truth: Git (documents) + Database (metadata/search)

Git stores:
- Markdown documents (thesis, analysis, notes)
- YAML configs (assumptions, models)
- Agent outputs
- Slash commands

Database stores:
- Metadata (ticker, date, analyst, tags)
- Time series (conviction scores, performance)
- Relationships (patterns, references)
- Search index

Sync: On git commit, update database
Query: Database finds files → read from git
```

**Practical Hybrid Architecture:**

```python
# .infrastructure/index.db (SQLite)

tables:
  documents:
    - path (e.g., coverage/AAPL/thesis.md)
    - ticker
    - doc_type
    - last_modified
    - analyst
    - tags
    - fts_content (full-text search index)

  conviction_history:
    - ticker, date, conviction_score, rationale

  patterns:
    - pattern_id, description, examples, tags

  agent_runs:
    - run_id, agent_type, ticker, status, cost, output_path
```

**Git hook updates database:**
```bash
# .git/hooks/post-commit
python .infrastructure/update-index.py
```

**Query interface:**
```markdown
# /search [query]

Searches across all research:
- Full-text search in SQLite FTS
- Returns matching documents
- Loads into context

Example: /search "margin expansion through automation"

Returns:
- coverage/AAPL/thesis.md (line 45)
- patterns/operating-leverage.md
- coverage/MSFT/history/2023-analysis.md
```

**Recommendation:**

```markdown
# Week 1-4: Pure Git
- Everything in git
- Use grep for search
- Keep it simple

# Month 2-3: Add SQLite Index
- Git remains source of truth
- SQLite for metadata + FTS
- Still runs on analyst's laptop

# Month 6+: Evaluate need for cloud DB
- If: Multi-office collaboration needed
- If: Firm-wide search portal wanted
- If: Advanced analytics on research patterns
- Then: Consider Postgres + pgvector

# But: Git always remains source of truth
```

### TIER 4: Collaboration Layer (Month 4-6)

**Eventually you'll need:**

#### 4.1 Shared Research Database

```
Option 1: Just use Git with remotes
- Each analyst pushes to shared repo
- Works for 5-10 analysts
- Free

Option 2: Add lightweight app
- Simple web app: search firm's research
- Reads from git repos
- No write access (git is still source)
- Could build with FastAPI + SQLite in a weekend

Option 3: Full platform (DON'T START HERE)
- Custom research platform
- Permissioning, roles, etc.
- Expensive to build and maintain
```

**Recommendation: Start with Option 1, maybe add Option 2 at Month 6.**

## The Minimal Viable Stack - Concrete Proposal

### Phase 1: Foundation (Week 1-4)

```bash
Infrastructure:
✅ Git repo (GitHub/GitLab)
✅ SQLite for costs/logs
✅ Local file cache
✅ Simple Python scripts

MCP Servers:
✅ SEC EDGAR wrapper
✅ Market data (yfinance)

Total cost: $0
```

### Phase 2: Intelligence (Month 2-3)

```bash
Add:
✅ SQLite FTS index (full-text search)
✅ Basic observability (JSON logs)
✅ Document extraction helpers (BeautifulSoup + pandas)

Still runs locally. Total cost: $0-50/month (if you upgrade market data)
```

### Phase 3: Scale (Month 4-6)

```bash
Add if needed:
⚠️ pgvector for semantic search
⚠️ Better document extraction (doclify)
⚠️ Shared database (Postgres)
⚠️ Simple web interface for firm search

Cost: $0-500/month depending on choices
```

## Technology Stack Summary

### Core Technologies

| Component | Solution | Rationale |
|-----------|----------|-----------|
| **SEC Data** | MCP + EDGAR API + cache | Free, official, cache locally for speed |
| **Document Extraction** | Claude Read + BeautifulSoup | Start simple, upgrade only if needed |
| **Market Data** | yfinance → Polygon if needed | Free to start, $200/mo if need real-time |
| **Vector DB** | Defer to Month 4+ | Don't need until you have scale problem |
| **Context Mgmt** | Git structure + smart loading | Prompt caching handles rest |
| **Observability** | Files + SQLite → Langfuse later | Own your data, upgrade when needed |
| **Persistence** | Git (source) + SQLite (index) | Best of both: version control + queryability |
| **Collaboration** | Git remotes initially | Add web interface only when needed |

### What NOT To Build

❌ Custom vector database
❌ Real-time data streaming infrastructure
❌ Complex microservices
❌ Custom document parser (use Claude)
❌ Web dashboard (CLI first)
❌ User authentication (single analyst initially)
❌ Custom ML models (Claude is the model)

### Critical Infrastructure Pieces You DO Need

✅ **Good caching** - Don't hit APIs repeatedly
✅ **Cost tracking** - Know what you're spending
✅ **Agent logging** - Debug when things break
✅ **Git structure** - Organize research logically
✅ **MCP servers** - Clean data access abstraction

## Dependencies

### Minimum Dependency List

```txt
# requirements.txt
anthropic>=0.18.0              # Claude API
yfinance>=0.2.0                # Market data
requests>=2.31.0               # HTTP requests
beautifulsoup4>=4.12.0         # HTML parsing
pandas>=2.0.0                  # Data manipulation
pyyaml>=6.0.0                  # YAML parsing
```

That's it. No fancy frameworks.

## Infrastructure Evolution Path

### Month 1: Foundation
- Git repo structure
- SEC EDGAR MCP server
- Market data MCP server
- Cost tracking (SQLite)
- Test: Can we fetch data and cache it?

### Month 2: Intelligence
- SQLite FTS index
- `/search` command
- More MCP servers as needed
- Build 2-3 more agents

### Month 3+: Scale When Needed
- Add pgvector IF semantic search needed
- Add doclify IF document extraction struggling
- Add Postgres IF collaboration needed
- But: Git remains source of truth

## Key Insight

**Start minimal, add infrastructure only when you feel the pain.**

The temptation is to build for scale from day 1. Resist.

Build for:
- 1 analyst (week 1)
- 3 analysts (month 2)
- 10 analysts (month 4)
- 50 analysts (month 8)

Each transition will tell you what infrastructure you need next.
