# Design Notes & Planning Documents

This directory contains the comprehensive planning, brainstorming, and design decisions for the Analyst Workspace project.

## Reading Order

If you're new to the project, read in this order:

1. **[00-overview.md](00-overview.md)** - Start here
   - High-level vision and philosophy
   - Core principles
   - Success metrics
   - Quick links to other docs

2. **[02-architecture-decisions.md](02-architecture-decisions.md)** - Understand the approach
   - Why agentic architecture
   - Layered system design
   - Agent types and patterns
   - Git-first storage strategy

3. **[04-v1-sprint-plan.md](04-v1-sprint-plan.md)** - See the plan
   - 7-day build plan for v1.0
   - Scope decisions (what's in, what's out)
   - Daily deliverables
   - Demo flow

4. **[03-infrastructure-stack.md](03-infrastructure-stack.md)** - Technical details
   - Infrastructure philosophy
   - Data access layer
   - Storage and persistence
   - Evolution path

5. **[01-brainstorming-ideas.md](01-brainstorming-ideas.md)** - Deep dive on possibilities
   - 18 idea clusters
   - 60+ specific concepts
   - Long-term vision
   - (This is comprehensive - save for later)

## Document Summaries

### 00-overview.md
**High-level project overview**
- Vision: Give analysts superpowers
- Core philosophy and principles
- Architecture approach summary
- v1.0 proof of value concept
- Links to all other documents

**Read this first.** 10 minutes.

### 01-brainstorming-ideas.md
**Comprehensive idea catalog (18 clusters)**

The result of deep brainstorming on ways Claude Code can transform equity research:

**Cluster A:** Research Memory Palace - Capturing insights over time
**Cluster B:** Thinking Partner - AI as intellectual challenge
**Cluster C:** Pattern Recognition - Learning from history
**Cluster D:** Quantified Judgment - Tracking predictions
**Cluster E:** Research Leverage - Optimize time spent
**Cluster F:** Collaborative Intelligence - Firm-wide knowledge
**Cluster G:** Meta-Learning - Skill development
**Cluster H:** External World Interface - Data integration
**Cluster I:** Model as Living Artifact - Intelligent models
**Cluster J:** Writing as Thinking - Better communication
**Cluster K:** Idea Generation - Systematic creativity
**Cluster L:** Communication Optimization - Right message, right audience
**Cluster M:** Continuous Calibration - Performance tracking
**Cluster N:** Risk Management - Systematic risk thinking
**Cluster O:** Speed Layer - Fast reaction workflows
**Cluster P:** Long-Term Compounding - Career-long learning
**Cluster Q:** Integration & Workflow - Daily rhythms
**Cluster R:** Firm-Wide Infrastructure - Organizational scale

Each cluster contains 3-5 specific, implementable ideas.

**This is the long-term vision.** 60+ minutes to read fully. Reference as needed.

### 02-architecture-decisions.md
**Why we built it this way**

Key decisions explained:
- Why agentic architecture is essential
- Hybrid layered approach (4 tiers)
- Agent design philosophy
- Human-in-the-loop checkpoints
- Git as state layer
- Slash command → Agent integration

Also includes:
- Specific agent types for equity research
- Example agent implementation (research-initiation-agent)
- Cost and time management strategies
- Error recovery and observability

**Essential for understanding the system.** 20 minutes.

### 03-infrastructure-stack.md
**Technical infrastructure choices**

Covers the full infrastructure stack in 4 tiers:
- **Tier 0:** Core (Git + SQLite) - Week 1
- **Tier 1:** Data Access (SEC, market data) - Week 2-3
- **Tier 2:** Intelligence (search, vector DB) - Month 2-3
- **Tier 3:** Operations (observability, eval) - Month 2-4
- **Tier 4:** Collaboration - Month 4-6

Key decisions:
- **SEC Data:** Free EDGAR API + MCP wrapper + cache
- **Market Data:** yfinance (free) → Polygon if needed
- **Document Extraction:** Claude Read + BeautifulSoup (start simple)
- **Vector DB:** Defer until Month 4+ (don't need yet)
- **Persistence:** Git (source of truth) + SQLite (query layer)
- **Observability:** Files + SQLite (own your data)

Includes:
- What NOT to build (avoid over-engineering)
- Minimum viable dependencies
- Infrastructure evolution path
- Cost estimates at each phase

**Critical for implementation.** 30 minutes.

### 04-v1-sprint-plan.md
**7-day build plan for v1.0**

The practical execution plan:

**Goal:** One workflow that saves 4+ hours of analyst time

**The Workflow:**
1. `/deep-dive TICKER`
2. Agent performs 30-60 min comprehensive research
3. Outputs structured analysis to git
4. Analyst saves 4-6 hours

**Daily Plan:**
- **Day 1:** Foundation & structure (repo setup, basic commands)
- **Day 2:** Data access layer (SEC + market data MCP servers)
- **Day 3:** First agent (research-initiation-agent)
- **Day 4:** Polish agent + observability
- **Day 5:** Additional workflows (earnings analysis, utilities)
- **Day 6:** Real-world test + bug fixes
- **Day 7:** Polish & ship

Includes:
- Scope (what's IN v1.0, what's NOT)
- Demo flow (5-minute demo script)
- Technology choices
- Risk mitigation
- Success metrics
- Daily checkpoints

**Your execution guide.** 20 minutes to read, 7 days to build.

## Key Themes Across Documents

### 1. Progressive Enhancement
Start simple, add complexity only when needed:
- Week 1: Basic structure
- Month 1: Core workflow
- Month 3: Collaboration
- Month 6+: Advanced features

### 2. Git-First Philosophy
Everything in version control:
- Documents (markdown)
- Configuration (YAML)
- Data (CSV for time series)
- Agent outputs
- Thinking evolution

### 3. Analyst-Driven
Tools built BY analysts FOR analysts:
- Not IT-imposed solutions
- Iterative refinement
- Own your data
- Shareable best practices

### 4. Local-First
Analyst's machine is source of truth:
- Cloud for sync/collaboration
- Works offline
- No vendor lock-in
- Portable data

### 5. Human-in-Loop
Agents enhance, don't replace:
- Checkpoints at key decisions
- Transparent process
- Editable outputs
- Learn analyst preferences

### 6. Measure Everything
Track to improve:
- Cost per agent run
- Time saved
- Prediction calibration
- Skill development
- Research ROI

## Common Questions

### "Where should I start?"
Read [00-overview.md](00-overview.md), then [04-v1-sprint-plan.md](04-v1-sprint-plan.md).
That gives you vision + execution plan.

### "What's the long-term vision?"
Read [01-brainstorming-ideas.md](01-brainstorming-ideas.md).
But don't try to build it all at once! v1.0 is one workflow.

### "Why these technical choices?"
Read [03-infrastructure-stack.md](03-infrastructure-stack.md).
Every choice has rationale. We optimize for shipping, not perfection.

### "Why agents instead of just tools?"
Read [02-architecture-decisions.md](02-architecture-decisions.md).
Research is exploratory, iterative, time-consuming. Perfect for agents.

### "How do I know if v1.0 is successful?"
From [04-v1-sprint-plan.md](04-v1-sprint-plan.md):
- Can run `/deep-dive` on real company
- Agent completes in < 60 min
- Output is genuinely useful
- Saves 4+ hours of manual work
- Foundation is solid for building more

### "What comes after v1.0?"
- Week 2: Get feedback from real analysts
- Month 2: Add top 3 requested features
- Month 3: Scale to 5-10 analysts
- Month 4+: Firm-wide features

See [01-brainstorming-ideas.md](01-brainstorming-ideas.md) for the full long-term vision.

## Design Philosophy

These documents reflect several key principles:

**1. Depth AND Breadth**
- Brainstormed 60+ ideas (breadth)
- Chose 1 workflow for v1.0 (depth)
- Will expand systematically based on value

**2. Theory AND Practice**
- [01-brainstorming-ideas.md](01-brainstorming-ideas.md) is aspirational
- [04-v1-sprint-plan.md](04-v1-sprint-plan.md) is concrete
- Both matter

**3. Vision AND Pragmatism**
- Long-term: Comprehensive research OS
- Short-term: One workflow that works
- Ship incremental value

**4. Flexibility AND Structure**
- Flexible: Analysts build their own tools
- Structured: Clear patterns and frameworks
- Balance both

## Contributing to These Docs

As the project evolves, these documents should be:

**Updated:**
- When key decisions change
- When new ideas emerge
- After major milestones

**Versioned:**
- Use git to track evolution
- Can see how thinking changed
- Learn from past decisions

**Referenced:**
- Link from implementation code
- Explain why things are built this way
- Onboard new contributors

## Document Maintenance

### After v1.0 Launch
- Create: `05-v1-retro.md` - What worked, what didn't
- Update: `00-overview.md` - Reflect current status
- Revise: `04-v1-sprint-plan.md` → `05-v2-plan.md`

### After 6 Months
- Create: `06-six-month-learnings.md`
- Document: Patterns that emerged
- Archive: Outdated plans

### Ongoing
- Weekly: Update status in `00-overview.md`
- Monthly: Document new patterns/ideas
- Quarterly: Review and refine vision

## Related Documentation

Outside this directory:

- **[../README.md](../README.md)** - Main project README
- **[../STRUCTURE.md](../STRUCTURE.md)** - Repository organization
- **[../.claude/](../.claude/)** - Agent and command implementations

## Questions or Feedback

These documents capture the initial planning and design thinking. As we build and learn, they'll evolve.

If something is unclear or missing, that's valuable feedback!

---

**Total reading time:**
- Quick start: 30 min (overview + sprint plan)
- Full understanding: 2-3 hours (all docs)
- Deep dive: 4+ hours (all docs + pondering)

**Most important:**
Start with [00-overview.md](00-overview.md), understand the vision, then jump to [04-v1-sprint-plan.md](04-v1-sprint-plan.md) and start building.
