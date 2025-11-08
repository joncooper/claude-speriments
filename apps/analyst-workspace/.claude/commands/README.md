# Slash Commands

This directory contains slash commands for Claude Code.

## Organization

Commands are organized by execution time and complexity:

```
commands/
├── instant/      # Quick commands (<1 min)
├── analysis/     # Analysis agents (5-30 min)
└── research/     # Deep research agents (30+ min)
```

## Command Format

Each slash command is a markdown file that defines:
- Command name and usage
- What it does
- Parameters
- Examples
- Implementation (direct execution or agent launch)

## Example Command Structure

```markdown
# /command-name - Brief description

## Usage
/command-name [required-param] [--optional-flag]

## What it does
Detailed description of command functionality

## Parameters
- required-param: Description
- --optional-flag: Description (default: value)

## Examples
/command-name AAPL
/command-name MSFT --depth=comprehensive

## Implementation
[Direct execution code or agent launch specification]
```

## Command Categories

### Instant Commands (instant/)
Fast, synchronous operations:
- `/thesis-snapshot [ticker]` - Display current thesis
- `/init-coverage [ticker]` - Set up new company folder
- `/costs [period]` - Show spending report
- `/search [query]` - Full-text search

### Analysis Commands (analysis/)
Launch single-purpose agents for structured analysis:
- `/earnings-analysis [ticker]` - Analyze latest earnings
- `/comp-analysis [peers]` - Competitive comparison
- `/model-audit [ticker]` - Check model assumptions

### Research Commands (research/)
Launch deep research agents with checkpoints:
- `/deep-dive [ticker]` - Comprehensive company research
- `/pattern-search [theme]` - Find historical analogs
- `/full-initiation [ticker]` - Multi-agent research workflow

## Creating New Commands

### 1. Choose the Right Tier

**Use instant/** when:
- Executes in <1 minute
- No external API calls (or only cached data)
- Deterministic output
- Simple transformation or lookup

**Use analysis/** when:
- Needs 5-30 minutes
- Single focused task
- Structured output format
- May need external data

**Use research/** when:
- Needs 30+ minutes
- Exploratory/open-ended
- Multiple subtasks
- Requires human checkpoints

### 2. Create the Command File

```bash
# For instant command
touch .claude/commands/instant/my-command.md

# For analysis command (launches agent)
touch .claude/commands/analysis/my-analysis.md

# For research command (launches agent)
touch .claude/commands/research/my-research.md
```

### 3. Define the Command

See existing commands for templates.

### 4. Test the Command

```bash
# In Claude Code
/my-command [params]
```

## Best Practices

### Naming
- Use lowercase with hyphens: `earnings-analysis`
- Be descriptive: `thesis-snapshot` not `thesis`
- Verb-noun pattern: `init-coverage`, `update-model`

### Documentation
- Clear usage examples
- Document all parameters
- Explain what output to expect
- Note time/cost estimates for agent commands

### Parameters
- Required parameters: `[ticker]`
- Optional parameters: `[--depth=standard]`
- Provide sensible defaults
- Validate input before launching expensive agents

### Error Handling
- Check if required files exist
- Validate ticker symbols
- Handle missing data gracefully
- Provide helpful error messages

## Command Development Workflow

1. **Design** - Decide what the command should do
2. **Tier** - Choose instant/analysis/research
3. **Prototype** - Create minimal version
4. **Test** - Try on real data
5. **Refine** - Improve based on testing
6. **Document** - Add examples and help text
7. **Share** - Commit to git for team use

## Agent-Launching Commands

Commands in `analysis/` and `research/` typically launch agents:

```markdown
# /deep-dive - Launch Research Initiation Agent

## Implementation
This command launches an agent using the Task tool:

Task tool:
  subagent_type: "research-initiation-agent"
  prompt: "Research {ticker} with {depth} depth..."
  model: "sonnet"
```

See [../agents/README.md](../agents/README.md) for agent development.

## Command Composition

Commands can be composed in workflows:

```bash
# Initialize and research
/init-coverage SNOW
/deep-dive SNOW --depth=standard

# Review and format
/thesis-snapshot SNOW
/format-for-pm coverage/SNOW/thesis.md
```

## Tips

- **Start simple** - Build instant commands before complex agents
- **Test frequently** - Run commands on real data often
- **Get feedback** - Have other analysts try your commands
- **Iterate** - Refine based on actual use
- **Document learnings** - Note what works and what doesn't

## v1.0 Commands (Target)

Minimal viable set:
- ✅ `/deep-dive [ticker]`
- ✅ `/earnings-analysis [ticker]`
- ✅ `/init-coverage [ticker]`
- ✅ `/thesis-snapshot [ticker]`
- ✅ `/search [query]`
- ✅ `/costs [period]`

Additional commands will be added based on value and usage patterns.
