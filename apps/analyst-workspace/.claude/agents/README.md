# Agents

This directory contains autonomous agent definitions for equity research workflows.

## What Are Agents?

Agents are autonomous workflows that:
- Execute complex, multi-step tasks
- Make decisions based on intermediate results
- Run for extended periods (5 minutes to hours)
- Include human checkpoints at key decisions
- Write outputs to git for transparency

## Agent Structure

Each agent has its own directory:

```
agents/
└── research-initiation/
    ├── prompt.md         # Agent behavior and process
    ├── config.yaml       # Configuration (costs, timeouts)
    ├── README.md         # Documentation
    └── examples/         # Example runs (optional)
```

## Agent Types

### Research Agents (Exploratory)
Open-ended research on companies or themes:
- `research-initiation-agent` - First pass on new company
- `pattern-finder-agent` - Find historical analogs
- `industry-mapper-agent` - Map industry structure
- `thesis-builder-agent` - Construct investment thesis

**Characteristics:**
- Time: 30-120 minutes
- Checkpoints: Multiple (plan, gather, synthesize)
- Output: Comprehensive markdown documents
- Cost: $5-50 depending on depth

### Analysis Agents (Focused)
Structured analysis of specific events or data:
- `earnings-analysis-agent` - Analyze earnings releases
- `filing-delta-agent` - Compare filings over time
- `transcript-analyzer-agent` - Extract key points from calls
- `model-builder-agent` - Build financial models

**Characteristics:**
- Time: 5-30 minutes
- Checkpoints: Few or none (straightforward task)
- Output: Structured analysis in standard format
- Cost: $1-10

### Monitoring Agents (Continuous)
Track ongoing developments:
- `thesis-monitor-agent` - Watch for thesis breaks
- `signal-detector-agent` - Multi-source monitoring
- `risk-monitor-agent` - Risk indicator tracking

**Characteristics:**
- Time: Always running (check periodically)
- Checkpoints: Alert when action needed
- Output: Notifications + log of observations
- Cost: $1-5 per day

## Creating a New Agent

### 1. Define the Agent's Purpose

Answer these questions:
- What problem does this solve?
- How long should it take?
- What are the inputs?
- What are the outputs?
- Where do checkpoints make sense?

### 2. Create Agent Directory

```bash
mkdir -p .claude/agents/my-agent
cd .claude/agents/my-agent
```

### 3. Write Agent Prompt (prompt.md)

```markdown
# Agent Name

Brief description of what this agent does.

## Purpose
[Why this agent exists]

## Process

### Phase 1: Planning (CHECKPOINT)
[What the agent does first]
[Present plan to analyst]
[Get approval before proceeding]

### Phase 2: Execution
[Main work happens here]
[Use MCP servers for data]
[Write intermediate results]

### Phase 3: Synthesis (CHECKPOINT if complex)
[Combine findings]
[Show to analyst]
[Get direction on next steps]

### Phase 4: Output
[Write final outputs to git]
[Specific file locations]

## Inputs
- param1: Description
- param2: Description

## Outputs
- file1: Description (location)
- file2: Description (location)

## Guidelines
- Be explicit about uncertainty
- Provide provenance for claims
- Ask for guidance at checkpoints
- Write everything to git
- Stay within cost budget
```

### 4. Create Configuration (config.yaml)

```yaml
name: my-agent
version: 1.0.0
description: Brief description

# Cost and time limits
limits:
  cost_usd_warn: 10
  cost_usd_max: 50
  time_minutes_estimate: 30
  time_minutes_max: 120

# Model to use
model: sonnet  # or opus for complex reasoning

# Checkpoints
checkpoints:
  - plan_phase
  - synthesis_phase

# Output locations
outputs:
  primary: "coverage/{ticker}/analysis.md"
  supporting:
    - "coverage/{ticker}/open-questions.md"
    - "coverage/{ticker}/.agent-runs/{date}/"

# MCP servers this agent uses
mcp_servers:
  - sec-edgar
  - market-data
```

### 5. Document the Agent (README.md)

```markdown
# Agent Name

Brief description.

## What It Does
[Detailed explanation]

## When to Use
[Scenarios where this agent is helpful]

## Usage
Via slash command:
/command-that-launches-this-agent [params]

## Process Overview
1. Step 1
2. Step 2
3. Step 3

## Outputs
- File 1: Description
- File 2: Description

## Time & Cost
- Estimated time: 30-60 minutes
- Estimated cost: $5-15

## Examples
[Link to example runs or outputs]
```

### 6. Test the Agent

```bash
# Launch via slash command
/launch-my-agent [test-params]

# Check outputs
cat coverage/TEST/analysis.md

# Review logs
cat .infrastructure/logs/agent-runs.jsonl | grep my-agent
```

### 7. Iterate

Based on testing:
- Refine prompts
- Adjust checkpoints
- Improve error handling
- Add examples

## Agent Development Best Practices

### Checkpoints
**Always checkpoint when:**
- About to do expensive operations
- Need analyst input to proceed
- Multiple valid paths forward
- Found unexpected results

**Example checkpoint:**
```markdown
[Agent] Planning phase complete. I propose to research:
1. Topic A (high priority, $5, 15 min)
2. Topic B (medium priority, $10, 30 min)
3. Topic C (low priority, $8, 20 min)

Given your $20 budget, I recommend #1 and #2.

Proceed? [y/n]
Modify? [m]
```

### Error Handling
**Handle gracefully:**
- Missing data (note what's missing, continue)
- API failures (retry with exponential backoff)
- Unexpected format (note issue, best effort)
- Exceeded limits (stop, report progress so far)

**Don't:**
- Silently fail
- Guess or make up data
- Continue if critically blocked
- Exceed cost/time budgets

### Provenance
**Always cite sources:**
- "Revenue grew 15% (10-K, page 42)"
- "Management mentioned pricing pressure (Q3 2024 earnings call)"
- "PE ratio of 25x (calculated from latest financials)"

### Transparency
**Make process visible:**
- Log what you're doing
- Write intermediate results
- Explain reasoning
- Note uncertainties

### Output Structure
**Consistent formats:**
```markdown
# Analysis Title

## Summary
[3-5 bullet points]

## Key Findings
[Numbered list of main insights]

## Details
[Sections with headers]

## Open Questions
[What still needs research]

## Sources
[List of data sources used]

## Agent Metadata
- Run date: 2024-11-07
- Duration: 45 minutes
- Cost: $8.23
- Model: Claude Sonnet 4.5
```

## Agent Workflows

### Research Workflow (Long)
```
1. PLAN → Present to analyst → Get approval
2. GATHER → Fetch data from MCP servers → Cache locally
3. ANALYZE → Process data → Write intermediate files
4. SYNTHESIZE → Show findings → Get direction
5. DEEP DIVE → Based on direction → Additional research
6. OUTPUT → Write final documents → Log completion
```

### Analysis Workflow (Short)
```
1. FETCH → Get data from MCP server or cache
2. ANALYZE → Process according to template
3. OUTPUT → Write structured result
```

### Monitoring Workflow (Ongoing)
```
1. CHECK → Periodic scan of signals
2. EVALUATE → Against thesis/thresholds
3. ALERT → If action needed
4. LOG → Record observations
```

## Agent Communication Patterns

### With Analyst (Human)
- **At checkpoints:** Present findings, ask for direction
- **On errors:** Explain what went wrong, suggest alternatives
- **On completion:** Summary of what was done, where outputs are

### With Other Agents (Future)
- Agents can invoke other agents
- Pass context via git files
- Share MCP server cache
- Coordinate via orchestrator agent

### With MCP Servers (Data)
- Request data with clear parameters
- Cache responses
- Handle rate limits
- Retry on failures

### With Git (State)
- Write all outputs to git
- Use .agent-runs/ for artifacts
- Create readable markdown
- Log metadata

## Testing Agents

### Unit Testing
Test individual components:
- Data fetching
- Parsing logic
- Output formatting

### Integration Testing
Test full agent run:
- With real data
- Check all outputs created
- Verify costs within budget
- Confirm time estimates

### Validation Testing
Check output quality:
- Accuracy of facts
- Completeness of analysis
- Usefulness to analyst
- Format consistency

## Cost Management

### Before Run
- Estimate cost based on operations
- Get approval if over threshold
- Use cached data when possible

### During Run
- Track tokens used
- Warn if approaching limit
- Stop if limit exceeded

### After Run
- Log actual cost
- Compare to estimate
- Learn for future runs

## Performance Optimization

### Speed
- Parallel data fetching
- Cache aggressively
- Skip unnecessary steps
- Use Sonnet for routine tasks, Opus only when needed

### Cost
- Reuse cached data
- Batch API calls
- Smart context management
- Avoid redundant analysis

### Quality
- Good prompts
- Clear structure
- Validation steps
- Checkpoints for course correction

## Debugging Agents

### Agent Not Producing Good Output
1. Check prompt clarity
2. Add more examples
3. Improve structure
4. Adjust model (Sonnet ↔ Opus)

### Agent Taking Too Long
1. Reduce scope
2. Parallelize operations
3. Use cached data more
4. Split into smaller agents

### Agent Costs Too Much
1. Reduce context size
2. Use Sonnet instead of Opus
3. Cache more aggressively
4. Reduce iterations

### Agent Errors Frequently
1. Add error handling
2. Validate inputs
3. Handle edge cases
4. Improve retry logic

## v1.0 Agents (Target)

Minimal viable set:
- ✅ `research-initiation-agent` - Deep dive research
- ✅ `earnings-analysis-agent` - Earnings review

Additional agents will be added based on demonstrated value.

## Future Agents (Post v1.0)

High-value candidates:
- `pattern-finder-agent` - Find similar historical situations
- `thesis-builder-agent` - Construct investment thesis from analysis
- `model-auditor-agent` - Review model assumptions
- `transcript-analyzer-agent` - Extract insights from earnings calls
- `filing-delta-agent` - Compare filings over time

Build based on:
- Analyst requests
- Time savings demonstrated
- Quality of outputs
- Cost efficiency

## Questions?

See:
- [../commands/README.md](../commands/README.md) - How commands launch agents
- [../../notes/02-architecture-decisions.md](../../notes/02-architecture-decisions.md) - Architecture rationale
- [../../notes/04-v1-sprint-plan.md](../../notes/04-v1-sprint-plan.md) - Build plan
