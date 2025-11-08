# Analyst Workspace - Project Overview

## Vision
Build Claude Code-based tools that grant equity research analysts "superpowers" - not to do their work for them, but to enable better, deeper, more thorough research. Allow analysts to iteratively develop, test, refine, and use their own idiomatic best practices, and share those within their firm.

## Core Philosophy

**Key Principles:**
1. **Enhance, Don't Replace** - Tools amplify analyst judgment, never replace it
2. **Analyst-Owned** - Analysts build and refine their own tools, not IT-imposed
3. **Iterative Refinement** - Start simple, evolve based on what works
4. **Knowledge Compounds** - Every piece of research makes the next piece better
5. **Shareable Best Practices** - Culture of contribution within firms
6. **Git-First** - Version control for thinking, not just code

## The Fundamental Insight

Great analysts are pattern matchers who:
- Connect disparate observations
- Learn from past situations
- Build systematic frameworks
- Compound knowledge over time

**The problem:** Most of this happens in analysts' heads and is lost when they leave.

**The solution:** Tools that externalize, capture, and compound analytical thinking.

## Architecture Approach

### Hybrid Layered System

```
Tier 1: Instant Commands (<1 min)
  → Direct execution, simple transformations

Tier 2: Data Retrieval (1-5 min)
  → MCP servers for external data sources

Tier 3: Structured Analysis (5-30 min)
  → Single-purpose agents with clear outputs

Tier 4: Deep Research (30 min - hours)
  → Multi-stage agents with human checkpoints
```

### Storage Philosophy

- **Git = Source of Truth** for documents, analysis, thinking
- **SQLite = Query Layer** for metadata, time series, search
- **Local-First** with cloud sync for collaboration
- **Human-Readable** formats (Markdown, YAML, CSV)

## v1.0 Proof of Value

**Goal:** One workflow that saves 4+ hours of analyst time.

**The Workflow:**
1. `/deep-dive TICKER` - Launch research agent
2. Agent performs comprehensive initial research (30-60 min)
3. Outputs structured analysis to git
4. Analyst reviews, refines, builds thesis

**Success Metrics:**
- Saves 4-6 hours of manual research time
- Produces genuinely valuable output
- Foundation is solid for building more
- Demonstrates clear ROI

## Related Documents

- [01-brainstorming-ideas.md](01-brainstorming-ideas.md) - Comprehensive idea clusters
- [02-architecture-decisions.md](02-architecture-decisions.md) - Why we built it this way
- [03-infrastructure-stack.md](03-infrastructure-stack.md) - Technical infrastructure choices
- [04-v1-sprint-plan.md](04-v1-sprint-plan.md) - 7-day build plan for v1.0

## Project Status

**Current Phase:** Setup and Foundation
**Target:** v1.0 by November 15, 2024
**Focus:** Proof of value with single deep-dive workflow
