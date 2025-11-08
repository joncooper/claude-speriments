# Architecture Decisions

## Why Agentic Architecture is Essential

Many equity research workflows are fundamentally agentic because they:
- **Take significant time** (hours, not seconds)
- **Require exploration** (don't know all steps upfront)
- **Need iteration** (gather data → analyze → need more data)
- **Involve judgment calls** (which path to pursue?)
- **Compound across multiple Claude passes**

## The Hybrid Layered Approach

```
┌─────────────────────────────────────────────────────────┐
│              ANALYST INTERFACE LAYER                     │
│        (Slash Commands in Claude Code)                   │
└───────────────┬─────────────────────────────────────────┘
                │
                ├─→ [TIER 1] Instant Commands (< 1 min)
                │   • /thesis-snapshot [ticker]
                │   • /format-for-pm [content]
                │   • /jargon-check [text]
                │   → Direct execution, no agent needed
                │
                ├─→ [TIER 2] Data Retrieval (1-5 min)
                │   • /pull-financials [ticker]
                │   • /search-research [query]
                │   • /alt-data-check [ticker]
                │   → MCP servers, simple processing
                │
                ├─→ [TIER 3] Structured Analysis (5-30 min)
                │   • /earnings-analysis [ticker]
                │   • /pre-mortem [ticker]
                │   • /comp-analysis [peers]
                │   → Single-purpose agents
                │
                └─→ [TIER 4] Deep Research (30 min - hours)
                    • /deep-dive [ticker]
                    • /pattern-search [theme]
                    • /full-initiation [ticker]
                    → Multi-stage agents with checkpoints
```

## Core Architecture Principles

### 1. Progressive Escalation
Don't use an agent when a slash command will do.

**Decision Tree:**
```
Can this be done in 1 Claude call?
  → YES: Slash command
  → NO: Is it purely data retrieval?
      → YES: MCP server
      → NO: Will it take > 5 minutes?
          → YES: Agent
          → NO: Slash command that does multi-step
```

### 2. Git as State Layer
Everything persists in git:

```
analyst-workspace/
├── .claude/
│   ├── commands/              # Slash commands
│   ├── agents/                # Agent definitions
│   └── mcp-servers/           # Data sources
│
├── .infrastructure/
│   ├── cache/                 # API response cache
│   ├── logs/                  # Agent execution logs
│   └── costs.db               # SQLite cost tracking
│
├── coverage/                  # Per-company research
│   └── AAPL/
│       ├── thesis.md          # Living document
│       ├── assumptions.yaml   # Model inputs
│       ├── conviction.csv     # Time series
│       └── .agent-runs/       # Agent execution history
│
├── patterns/                  # Cross-company insights
├── meta/                      # Learning/calibration
└── shared/                    # Firm-wide knowledge
```

**Why git?**
- ✅ Version control on thinking
- ✅ Transparent agent state
- ✅ Audit trail
- ✅ Collaboration-ready
- ✅ Can diff between states
- ✅ Analyst can edit agent outputs

### 3. Agent Design Philosophy

**Agents should feel like delegating to a brilliant junior analyst.**

Good agent design includes:
- Clear inputs and outputs
- Human-in-the-loop checkpoints
- Cost and time estimates
- Transparent process
- Resumable state

**Example:**
```markdown
## research-initiation-agent

**What it does:**
Structured first-pass analysis of a new company

**Inputs:**
- ticker: AAPL
- depth: quick | standard | comprehensive
- focus: (optional) specific areas to emphasize
- time_budget: hours you're willing to wait
- cost_budget: max $ to spend

**Process:**
1. PLAN (checkpoint) → shows research plan, get approval
2. GATHER → pulls data in parallel (MCP servers)
3. ANALYZE → systematic analysis
4. SYNTHESIZE (checkpoint) → show findings, identify gaps
5. OUTPUT → structured markdown in coverage/[ticker]/

**Outputs:**
- coverage/[ticker]/initial-analysis.md
- coverage/[ticker]/open-questions.md
- coverage/[ticker]/preliminary-thesis.md

**Cost estimate:** $5-50 depending on depth
**Time estimate:** 15min - 2 hours
```

### 4. Human-in-the-Loop Checkpoints

Long-running agents MUST have checkpoints where they pause for human input:

```markdown
# Example Checkpoint Flow

[Agent] Planning phase complete. I propose to research:
1. Services business momentum (high priority)
2. iPhone cycle dynamics (high priority)
3. China exposure/risks (medium priority)
4. Wearables competitive position (medium priority)
5. Capital allocation strategy (low priority)

Given 2-hour time budget, I recommend focusing on #1-3.

Continue? [y/n]
Modify priorities? [m]

> y

[Agent] Starting data gathering phase (10 min)...
```

## Specific Agent Types for Equity Research

### Research Agents (Exploratory)
- `research-initiation-agent` - First pass on new company
- `pattern-finder-agent` - Find historical analogs
- `industry-mapper-agent` - Map industry structure
- `thesis-builder-agent` - Construct investment thesis
- `competitor-analysis-agent` - Deep dive on competition

### Analysis Agents (Deep-dive)
- `transcript-analyzer-agent` - Earnings call analysis
- `filing-delta-agent` - Compare filings over time
- `model-builder-agent` - Build financial model
- `scenario-generator-agent` - Create scenario trees
- `assumption-auditor-agent` - Audit model assumptions

### Monitoring Agents (Continuous)
- `thesis-monitor-agent` - Watch for thesis breaks
- `signal-detector-agent` - Multi-source monitoring
- `risk-monitor-agent` - Risk indicator tracking

### Learning Agents (Retrospective)
- `post-mortem-agent` - What went wrong/right?
- `calibration-agent` - Am I getting better?
- `pattern-extraction-agent` - Learn from history

### Orchestrator Agents (Coordinate multiple agents)
- `full-initiation-agent` - Runs multiple research agents
- `portfolio-review-agent` - Runs agent per position
- `firm-wide-theme-agent` - Coordinate across analysts

## Why Claude Code Agents?

**Advantages:**
- ✅ Natural integration with analyst workflow
- ✅ Git-native (perfect for research version control)
- ✅ Slash commands are intuitive
- ✅ MCP servers for data access
- ✅ Task tool for agent orchestration
- ✅ Can compose agents + commands + MCP seamlessly

## Key Technical Decisions

### ✅ Build as Claude Code Agents

**Different tasks need different architectures:**

| Task Type | Duration | Architecture | Example |
|-----------|----------|--------------|---------|
| Lookup | < 1 min | Slash command | `/thesis-snapshot AAPL` |
| Data fetch | 1-5 min | MCP server | `/pull-financials AAPL` |
| Analysis | 5-30 min | Single agent | `/earnings-analysis AAPL` |
| Research | 30-120 min | Multi-stage agent | `/deep-dive AAPL` |
| Monitoring | Continuous | Background agent + triggers | `/monitor-thesis AAPL` |

### Challenges to Handle

**1. Cost Management**
```yaml
# In agent config
cost_limits:
  warn_threshold: $10
  hard_limit: $50
  require_approval_above: $25
```

**2. Time Management**
```yaml
# In agent config
time_limits:
  estimated_duration: "30-60 min"
  checkpoint_interval: "15 min"
  max_duration: "2 hours"
```

**3. Observability**
```markdown
# Agent logs to git as it works
coverage/AAPL/.agent-runs/2024-11-07-deep-dive/
├── plan.md           # What agent plans to do
├── progress.md       # Live updates
├── data/             # Raw data gathered
├── analysis.md       # Intermediate analysis
└── output.md         # Final output
```

**4. Error Recovery**
```yaml
# Agent state checkpointing
checkpoint_after:
  - plan_phase
  - gather_phase
  - each_analysis_section
  - synthesis_phase

resume_from: last_checkpoint
```

## Slash Command → Agent Integration

**Example flow:**

1. Analyst runs: `/deep-dive AAPL --depth=standard`
2. Slash command expands
3. Claude sees the instruction
4. Claude uses Task tool to launch agent:
   ```
   Task tool:
     subagent_type: "research-initiation-agent"
     prompt: "Research AAPL with standard depth..."
     model: "sonnet" (for cost efficiency)
   ```
5. Agent runs autonomously with checkpoints
6. Agent writes outputs to git
7. Agent returns summary to Claude
8. Claude presents results to analyst

## The Right Architecture Summary

**Recommendation:**

1. **Tier 1-2**: Slash commands + MCP servers (simple, fast)
2. **Tier 3**: Single-purpose agents (structured workflows)
3. **Tier 4**: Multi-stage agents with checkpoints (deep research)
4. **Tier 5**: Orchestrator agents (coordinate multiple agents)

**This architecture gives you:**
- 🎯 Right tool for each job
- 💰 Cost efficiency (don't use agents when commands work)
- 👁️ Transparency (everything in git)
- 🔄 Resumability (agents can pause/resume)
- 🤝 Human-in-loop (checkpoints at key decisions)
- 📈 Compound learning (agents improve knowledge base)

## Example: Deep-Dive Agent Implementation

### Slash Command Definition
```markdown
# File: .claude/commands/research/deep-dive.md

# /deep-dive - Launch Research Initiation Agent

## Usage
/deep-dive [ticker] [--depth=quick|standard|comprehensive] [--focus=area]

## What it does
Launches research-initiation-agent to do structured first-pass research.

## Example
/deep-dive SNOW --depth=standard --focus="competitive position"
```

### Agent Prompt
```markdown
# File: .claude/agents/research-initiation-agent/agent.md

You are a research initiation agent for equity research analysts.

## Process

### Phase 1: PLAN (always checkpoint here)
1. Assess what analyst knows already
2. Identify key questions to answer
3. Prioritize based on time/cost budget
4. Present research plan
5. Get analyst approval before proceeding

### Phase 2: GATHER (parallel data collection)
Use MCP servers to gather:
- Financial statements (10-K, 10-Q, transcripts)
- Stock price/performance data
- News and recent events
- Analyst consensus
- Peer group data

Write all raw data to coverage/[ticker]/.agent-runs/[date]-deep-dive/data/

### Phase 3: ANALYZE (systematic analysis)
1. Business model
2. Financial performance
3. Competitive position
4. Management quality
5. Risks

### Phase 4: SYNTHESIZE (checkpoint here)
1. Integrate findings
2. Identify what's most important
3. Identify gaps
4. Show to analyst, get direction

### Phase 5: OUTPUT
Write structured outputs:
- coverage/[ticker]/initial-analysis.md
- coverage/[ticker]/open-questions.md
- coverage/[ticker]/preliminary-thesis.md

## Guidelines
- Ask for guidance at checkpoints
- Be explicit about uncertainty
- Flag contradictions in data
- Provide provenance for all claims
- Write everything to git for transparency
```

## State Management

**Git handles state at multiple levels:**

1. **Document state** - Markdown files with research
2. **Agent state** - Progress logs in .agent-runs/
3. **Metadata state** - SQLite for queryable data
4. **Code state** - Slash commands and agent definitions

**This means:**
- Everything is version controlled
- Everything is auditable
- Everything is human-readable
- Everything can be diffed
- Everything is portable

## Scalability Considerations

**Single Analyst (v1.0):**
- Local git repo
- SQLite for metadata
- All processing on laptop
- Works great for 20-50 stocks

**Small Team (5-10 analysts):**
- Shared git remote
- Still local processing
- Occasional merge conflicts (good forcing function)
- Shared pattern library

**Firm-Wide (50+ analysts):**
- Centralized git server
- Shared search index
- May need cloud compute for heavy agents
- Dedicated infra team

**Key:** Start simple, add complexity only when needed.
