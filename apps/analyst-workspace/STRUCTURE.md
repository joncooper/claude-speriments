# Repository Structure

This document explains the organization of the analyst-workspace repository.

## Directory Layout

```
analyst-workspace/
├── .claude/                    # Claude Code configuration
├── .infrastructure/            # Infrastructure & tooling
├── coverage/                   # Per-company research
├── patterns/                   # Cross-company insights
├── meta/                       # Learning & calibration
├── shared/                     # Firm-wide knowledge
├── demo/                       # Demo materials
└── notes/                      # Design documentation
```

## `.claude/` - Claude Code Configuration

Claude Code-specific files for commands, agents, and data access.

```
.claude/
├── commands/
│   ├── instant/           # Quick commands (<1 min)
│   │   ├── thesis-snapshot.md
│   │   ├── init-coverage.md
│   │   └── costs.md
│   ├── analysis/          # Analysis commands (5-30 min)
│   │   └── earnings-analysis.md
│   └── research/          # Research commands (30+ min)
│       └── deep-dive.md
│
├── agents/
│   ├── research-initiation/
│   │   ├── prompt.md      # Agent behavior definition
│   │   ├── config.yaml    # Agent configuration
│   │   └── README.md      # Agent documentation
│   └── earnings-analysis/
│       └── ...
│
└── mcp-servers/
    ├── sec-edgar/
    │   ├── server.py      # MCP server implementation
    │   ├── requirements.txt
    │   └── README.md
    ├── market-data/
    │   └── ...
    └── config.json        # MCP server configuration
```

### Commands

Slash commands are organized by execution time:
- **instant/** - Commands that complete in seconds
- **analysis/** - Commands that launch agents for structured analysis (5-30 min)
- **research/** - Commands that launch deep research agents (30+ min)

### Agents

Each agent gets its own directory with:
- `prompt.md` - The agent's system prompt and instructions
- `config.yaml` - Configuration (cost limits, timeouts, etc.)
- `README.md` - Documentation on what the agent does and how to use it

### MCP Servers

Each MCP server provides access to external data sources:
- `server.py` - The MCP server implementation
- `requirements.txt` - Python dependencies
- `README.md` - Documentation

## `.infrastructure/` - Infrastructure & Tooling

Supporting infrastructure for the system.

```
.infrastructure/
├── cache/                 # Cached API responses
│   ├── sec-filings/
│   │   └── AAPL/
│   │       ├── 10-K-2024-01-27.json
│   │       └── 10-K-2024-01-27.txt
│   └── market-data/
│       └── AAPL/
│           └── prices-daily.csv
│
├── logs/                  # Agent execution logs
│   ├── agent-runs.jsonl   # Structured logs (JSON Lines)
│   └── errors.log         # Error logs
│
├── costs.db               # SQLite database for cost tracking
├── index.db               # SQLite database for search index
│
└── scripts/               # Utility scripts
    ├── update-index.py    # Update search index
    ├── cost-report.py     # Generate cost reports
    └── log-agent-run.py   # Log agent execution
```

### Cache

API responses are cached locally to:
- Speed up repeated access
- Reduce API costs
- Enable offline work

Cache structure:
```
cache/
└── {data-source}/
    └── {ticker}/
        └── {resource}-{date}.{ext}
```

### Logs

**agent-runs.jsonl** - One JSON object per line:
```json
{"timestamp": "2024-11-07T10:30:00Z", "agent": "research-initiation",
 "ticker": "AAPL", "duration_sec": 1834, "cost_usd": 4.23,
 "status": "success", "output_path": "coverage/AAPL/initial-analysis.md"}
```

### Databases

**costs.db** - SQLite database tracking:
- Agent execution costs
- Token usage
- Time spent
- Success/failure rates

**index.db** - SQLite database with:
- Full-text search index
- Document metadata
- Cross-references

## `coverage/` - Per-Company Research

Research files for each company in your coverage universe.

```
coverage/
└── AAPL/
    ├── thesis.md              # Current investment thesis
    ├── initial-analysis.md    # First-pass analysis from agent
    ├── open-questions.md      # Questions needing research
    ├── assumptions.yaml       # Model assumptions
    ├── conviction.csv         # Conviction tracking over time
    │
    ├── earnings/              # Earnings analysis
    │   ├── 2024-Q1.md
    │   └── 2024-Q2.md
    │
    ├── meetings/              # Management meeting notes
    │   └── 2024-11-01-management.md
    │
    ├── history/               # Historical analysis
    │   └── 2023-initiation.md
    │
    └── .agent-runs/           # Agent execution artifacts
        └── 2024-11-07-deep-dive/
            ├── plan.md
            ├── data/
            ├── analysis.md
            └── output.md
```

### File Formats

**thesis.md** - Structured investment thesis:
```markdown
# AAPL Investment Thesis

## Summary
[3-5 bullet executive summary]

## Bull Case
[Key positive factors]

## Bear Case
[Key risks and concerns]

## Conviction: 8/10
[Rationale for conviction level]
```

**assumptions.yaml** - Model assumptions:
```yaml
ticker: AAPL
last_updated: 2024-11-07

revenue_growth:
  value: 0.15
  basis: "Historical 12%, management guide 18%, our view 15%"
  confidence: 6
  sensitivity: high
```

**conviction.csv** - Time series:
```csv
date,conviction,rationale
2024-11-01,7,"Solid quarter, but macro uncertainty"
2024-11-07,8,"Product cycle looking strong"
```

## `patterns/` - Cross-Company Insights

Reusable patterns and frameworks discovered across multiple companies.

```
patterns/
├── operating-leverage.md      # Pattern: Operating leverage dynamics
├── land-and-expand.md         # Pattern: SaaS land-and-expand
├── winner-take-most.md        # Pattern: Network effects
└── management-transitions.md  # Pattern: Management change impacts
```

Each pattern file includes:
- Description of the pattern
- How to recognize it
- Historical examples
- Key variables that determine outcomes
- Typical timeline

## `meta/` - Learning & Calibration

Tracking your own analytical performance and skill development.

```
meta/
├── calibration.csv            # Prediction accuracy tracking
├── skills-assessment.yaml     # Skills self-assessment
├── research-journal.md        # Daily/weekly learnings
├── mistakes-log.md            # Documented mistakes and lessons
└── process-improvements.md    # Research process refinements
```

## `shared/` - Firm-Wide Knowledge

Resources shared across the analyst team (when scaling beyond individual use).

```
shared/
├── templates/                 # Standardized templates
│   ├── thesis-template.md
│   └── earnings-template.md
├── best-practices/            # Firm research standards
│   └── valuation-framework.md
└── common-patterns/           # Shared pattern library
    └── ...
```

## `demo/` - Demo Materials

Materials for demonstrating the system.

```
demo/
├── demo-script.md             # Step-by-step demo flow
├── demo-video.mp4             # Recorded demo
└── example-output/            # Pre-run examples
    ├── SNOW-deep-dive/
    │   ├── initial-analysis.md
    │   └── open-questions.md
    └── DDOG-earnings/
        └── earnings-2024-Q3.md
```

## `notes/` - Design Documentation

Planning and design documents for the project.

```
notes/
├── 00-overview.md                  # High-level vision
├── 01-brainstorming-ideas.md       # Comprehensive idea catalog
├── 02-architecture-decisions.md    # Architecture rationale
├── 03-infrastructure-stack.md      # Infrastructure choices
└── 04-v1-sprint-plan.md            # v1.0 build plan
```

## File Naming Conventions

### Markdown Files
- Use lowercase with hyphens: `initial-analysis.md`
- Date prefix for versioned content: `2024-11-07-earnings.md`
- Descriptive names: `competitive-analysis.md` not `comp.md`

### Data Files
- CSV for time series: `conviction.csv`, `prices.csv`
- YAML for configuration: `assumptions.yaml`, `config.yaml`
- JSON for structured data: `metadata.json`

### Directories
- Company tickers: ALL CAPS (`AAPL/`, `MSFT/`)
- Other directories: lowercase with hyphens
- Hidden directories: prefix with `.` (`.agent-runs/`, `.infrastructure/`)

## Git Practices

### What to Commit
✅ All markdown documents
✅ Configuration files (YAML, JSON)
✅ Code (Python scripts, MCP servers)
✅ Small CSV files (conviction tracking, etc.)
✅ Agent outputs

### What NOT to Commit
❌ `.infrastructure/cache/` - API responses (too large, regenerable)
❌ `.infrastructure/logs/` - Logs (use .gitignore)
❌ Large datasets
❌ API keys or secrets

### Commit Messages
- Research updates: "Update AAPL thesis based on Q3 earnings"
- Agent runs: "Add deep-dive analysis for SNOW"
- Pattern additions: "Document SaaS unit economics pattern"
- Code changes: "Add error handling to SEC EDGAR MCP server"

## Search and Discovery

### Finding Files

**By ticker:**
```bash
ls coverage/AAPL/
```

**By content:**
```bash
/search "pricing power"
# or
grep -r "pricing power" coverage/
```

**By date:**
```bash
find coverage/ -name "2024-11-*"
```

**Recent changes:**
```bash
git log --since="1 week ago" --name-only
```

### Database Queries

**Cost by ticker:**
```sql
SELECT ticker, SUM(cost_usd) FROM agent_runs GROUP BY ticker;
```

**Recent agent runs:**
```sql
SELECT * FROM agent_runs ORDER BY timestamp DESC LIMIT 10;
```

## Scaling Considerations

### Single Analyst
- All directories relevant
- Local git repo
- Cache stays small
- Simple search with grep

### Small Team (5-10 analysts)
- Shared git remote
- `shared/` directory becomes important
- May need `.gitignore` for large cache
- Consider shared `index.db` on network drive

### Firm-Wide (50+ analysts)
- Separate repos per analyst or team
- Shared `patterns/` synced across repos
- Centralized search infrastructure
- Cloud storage for large cache

## Maintenance

### Daily
- Git commit research updates
- Agent runs logged automatically

### Weekly
- Review agent costs: `/costs`
- Update conviction logs
- Clean old cache files (optional)

### Monthly
- Update skills assessment
- Review and update patterns
- Archive old analysis to `history/`

### Quarterly
- Comprehensive git commit with thesis updates
- Calibration review
- Process improvements documentation

## Backup Strategy

### Git Remote
Primary backup. All documents version controlled.

### Local Backup
```bash
# Backup databases and cache
tar -czf backup-$(date +%Y%m%d).tar.gz .infrastructure/
```

### Critical Files
Most critical:
1. `coverage/*/thesis.md` - Investment theses
2. `patterns/*.md` - Pattern library
3. `.infrastructure/costs.db` - Historical costs
4. `meta/*` - Learning data

All are in git and small enough to backup easily.

## Questions?

See [README.md](README.md) for high-level overview or [notes/](notes/) for detailed design documents.
