# Analyst Workspace

**Claude Code-powered tools for equity research analysts.**

Give analysts superpowers: not to do their work for them, but to enable better, deeper, more thorough research.

## Vision

Enable equity research analysts to:
- Develop their own idiomatic best practices
- Iteratively test and refine analytical frameworks
- Capture and compound knowledge over time
- Share best practices within their firm

## Status

**Current Phase:** Planning & Foundation
**Target v1.0:** November 15, 2024
**Focus:** Proof of value with single deep-dive research workflow

## Quick Start (Coming Soon)

```bash
# Initialize coverage for a new company
/init-coverage SNOW

# Launch comprehensive research agent
/deep-dive SNOW --depth=standard

# View analysis output
cat coverage/SNOW/initial-analysis.md

# Search all research
/search "pricing power"

# Check costs
/costs
```

## Core Workflow (v1.0)

The **Proof of Value** workflow:

1. Analyst needs to research a new company
2. `/deep-dive TICKER` launches autonomous research agent
3. Agent performs 30-60 minutes of comprehensive analysis:
   - Fetches SEC filings (10-K, 10-Q, transcripts)
   - Gathers market data and peer comparisons
   - Analyzes business model, financials, competition, risks
   - Outputs structured analysis to git
4. Analyst reviews, refines, builds investment thesis
5. Saves 4-6 hours of manual research time

## Project Structure

```
analyst-workspace/
├── .claude/
│   ├── commands/           # Slash commands (instant, analysis, research)
│   ├── agents/             # Autonomous agents (research, earnings analysis)
│   └── mcp-servers/        # Data sources (SEC, market data)
│
├── .infrastructure/
│   ├── cache/              # API response cache
│   ├── logs/               # Agent execution logs
│   └── costs.db            # Cost tracking (SQLite)
│
├── coverage/               # Per-company research
│   └── [TICKER]/
│       ├── thesis.md
│       ├── initial-analysis.md
│       ├── assumptions.yaml
│       └── .agent-runs/
│
├── patterns/               # Cross-company insights
├── meta/                   # Learning & calibration
├── shared/                 # Firm-wide knowledge
├── demo/                   # Demo materials
└── notes/                  # Design docs & planning
```

## Documentation

### Planning & Design
- [00-overview.md](notes/00-overview.md) - Project vision and philosophy
- [01-brainstorming-ideas.md](notes/01-brainstorming-ideas.md) - Comprehensive idea clusters (18 clusters, 60+ concepts)
- [02-architecture-decisions.md](notes/02-architecture-decisions.md) - Why we built it this way
- [03-infrastructure-stack.md](notes/03-infrastructure-stack.md) - Technical infrastructure choices
- [04-v1-sprint-plan.md](notes/04-v1-sprint-plan.md) - 7-day build plan for v1.0

## Key Principles

1. **Git-First** - Version control for thinking, not just code
2. **Analyst-Owned** - Tools built by analysts, not imposed by IT
3. **Local-First** - Analyst's machine is source of truth
4. **Human-Readable** - Markdown, YAML, CSV (no black boxes)
5. **Compound Learning** - Every piece of research makes the next better
6. **Progressive Enhancement** - Start simple, add complexity as needed

## Architecture

### Layered Approach

**Tier 1: Instant Commands** (<1 min)
- Simple transformations and lookups
- Direct execution, no agents

**Tier 2: Data Retrieval** (1-5 min)
- MCP servers for external data
- SEC filings, market data, fundamentals

**Tier 3: Structured Analysis** (5-30 min)
- Single-purpose agents
- Earnings analysis, competitive analysis

**Tier 4: Deep Research** (30-60 min)
- Multi-stage agents with checkpoints
- Comprehensive company research

### Technology Stack (v1.0)

**Core:**
- Claude Code (agent orchestration)
- Git (source of truth)
- SQLite (metadata & search index)
- Python (MCP servers, utilities)

**Data Sources:**
- SEC EDGAR API (free, official)
- yfinance (market data - free)
- Local caching (speed + cost optimization)

**Infrastructure:**
- Local-first (runs on analyst's laptop)
- File-based caching
- Simple observability (JSON logs + SQLite)

## Planned Features (v1.0)

### Slash Commands (6 total)
- `/deep-dive [ticker]` - Launch research agent
- `/earnings-analysis [ticker]` - Quick earnings review
- `/init-coverage [ticker]` - Set up new company
- `/thesis-snapshot [ticker]` - Display current view
- `/search [query]` - Full-text search
- `/costs` - Spending report

### Agents (2 total)
- `research-initiation-agent` - Deep dive research
- `earnings-analysis-agent` - Earnings review

### MCP Servers (2 total)
- `sec-edgar` - SEC filings access
- `market-data` - Price data & fundamentals

## Future Roadmap (Post v1.0)

**Phase 2 (Month 2):**
- Pattern recognition and matching
- Conviction tracking over time
- More specialized agents

**Phase 3 (Month 3):**
- Multi-analyst collaboration
- Firm-wide knowledge sharing
- Advanced search (semantic)

**Phase 4 (Month 4+):**
- Learning & calibration systems
- Performance attribution
- Thesis evolution tracking

See [01-brainstorming-ideas.md](notes/01-brainstorming-ideas.md) for comprehensive feature ideas.

## Design Philosophy

### What This Is
- **Thinking partner** for analysts
- **Knowledge amplifier** that compounds over time
- **Framework builder** for systematic analysis
- **Research infrastructure** that improves with use

### What This Is NOT
- Automated stock picking
- Replacement for analyst judgment
- Generic research assistant
- Black box recommendation engine

The goal is to make good analysts great by:
- Reducing time on mechanical tasks
- Capturing and reusing patterns
- Forcing systematic thinking
- Enabling knowledge sharing

## Contributing

This is currently in early development. Once v1.0 is stable, we'll open for contributions.

## License

TBD

## Contact

For questions or feedback, see main repository.

---

**Current Status:** Repository structure created, planning complete, ready to begin implementation.

**Next Steps:**
1. Build SEC EDGAR MCP server
2. Build market data MCP server
3. Build research-initiation-agent
4. Test end-to-end workflow
5. Iterate based on real usage
