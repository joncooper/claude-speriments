# Cialdini Persuasion Techniques for AI Agent Instruction

An experimental implementation of Dr. Robert Cialdini's 7 principles of persuasion as Claude Code slash commands to improve AI agent instruction adherence.

## Motivation

Based on the observation: *"I'm hearing you have to more or less use Robert Cialdini's persuasion techniques to get these AI agents to adhere to instructions."*

This experiment explores whether applying systematic persuasion principles to prompts can measurably improve:
- Instruction adherence rates
- Task completion quality
- Consistency in following requirements
- Reduction in premature completion (TODOs/stubs)

## What Are Cialdini's Persuasion Principles?

Dr. Robert Cialdini identified 7 universal principles of influence:

1. **Reciprocity** - People feel obligated to return favors
2. **Commitment & Consistency** - People align with their prior commitments
3. **Social Proof** - People look to what others are doing
4. **Authority** - People defer to credible experts
5. **Liking** - People prefer to say yes to those they like
6. **Scarcity** - People want more of what is less available
7. **Unity** - People are influenced by shared identity

## The Commands

### Individual Technique Commands

Each principle has its own slash command that wraps your prompt:

| Command | Principle | When to Use |
|---------|-----------|-------------|
| `/cialdini-reciprocity` | Reciprocity | You've provided extensive context/resources |
| `/cialdini-commitment` | Commitment | Complex multi-step tasks requiring planning |
| `/cialdini-social-proof` | Social Proof | Industry standards and best practices apply |
| `/cialdini-authority` | Authority | Official requirements or specs exist |
| `/cialdini-liking` | Liking | Building ongoing relationship with agent |
| `/cialdini-scarcity` | Scarcity | Time/resource constraints are critical |
| `/cialdini-unity` | Unity | Collaborative goals and shared values |

### Meta Commands

| Command | Purpose |
|---------|---------|
| `/cialdini-persuade` | Analyzes your prompt and suggests which 2-3 techniques would be most effective |
| `/cialdini-all` | Applies all 7 principles for maximum adherence on critical tasks |
| `/cialdini-analyze` | Evaluates an existing prompt to identify techniques present and suggest improvements |

## Installation

### Copy Commands to Your Claude Code Config

```bash
# From the repository root
cp -r cialdini-persuasion/commands/* ~/.claude/commands/
```

Or manually copy the files from `cialdini-persuasion/commands/` to your `~/.claude/commands/` directory.

### Verify Installation

```bash
# In Claude Code, type this and press Tab
/cialdini-
```

You should see all 10 commands autocomplete!

## Usage Examples

### Example 1: Multi-Step Implementation

**Standard prompt:**
```
Write a function to parse JSON with error handling and validation
```

**With commitment technique:**
```
/cialdini-commitment Write a function to parse JSON with error handling and validation
```

The agent will first outline its complete plan, then execute it systematically.

### Example 2: Critical Bug Fix

**Standard prompt:**
```
Fix the memory leak in request_handler.py
```

**With scarcity technique:**
```
/cialdini-scarcity Fix the memory leak in request_handler.py - this is affecting production right now
```

Emphasizes urgency and the need for complete implementation (no TODOs).

### Example 3: Getting Help Choosing

**When unsure which technique to use:**
```
/cialdini-persuade Refactor the authentication module to use OAuth 2.0
```

The agent will analyze the task and recommend which techniques would be most effective.

### Example 4: Critical Task

**For your most important work:**
```
/cialdini-all Implement the payment processing system with Stripe integration
```

Applies all 7 principles for maximum instruction adherence.

## How It Works

Each slash command is a markdown file in `commands/` that:
1. Explains which Cialdini principle is being applied
2. Wraps your prompt with persuasion-technique framing
3. Uses `{{prompt}}` placeholder to inject your actual task

For example, `/cialdini-commitment` asks the agent to outline its plan first (commitment), then execute it (consistency).

## Validation & Testing

**Status:** Commands implemented, validation planned

We've designed a comprehensive test plan with:
- 10 benchmark tasks across 5 categories
- Automated validation (code parsing, linting, test execution)
- A/B testing methodology
- Statistical analysis (t-tests, effect sizes)
- Controls for verbosity (testing if it's just longer prompts)

See [cialdini-test-plan.md](./cialdini-test-plan.md) for full methodology.

**Success criteria:**
- Statistical significance (p < 0.05)
- ≥15% improvement in instruction adherence
- Cohen's d ≥ 0.5 (medium-to-large effect)
- NOT explained by prompt length alone

**Question:** Do these techniques actually work, or is it "prompting theater"?
**Answer:** To be determined through rigorous testing.

## Documentation

- **[cialdini-persuasion-proposal.md](./cialdini-persuasion-proposal.md)** - Complete proposal with technique descriptions, examples, and implementation rationale
- **[cialdini-test-plan.md](./cialdini-test-plan.md)** - Comprehensive testing methodology for validation
- **[NOTES.md](./NOTES.md)** - Development process and design decisions

## Research Background

Based on Dr. Robert Cialdini's work:
- *Influence: The Psychology of Persuasion* (1984)
- 35+ years of evidence-based research
- Principles validated across human persuasion contexts

**Novel application:** Applying these principles to AI agent instruction is experimental and unvalidated (hence the test plan).

## Current Status

✅ **Implemented:** All 10 slash commands
⏸️ **On Hold:** Rigorous A/B testing and validation
🎯 **Goal:** Determine if these techniques measurably improve agent instruction adherence

## Command Quick Reference

Type `/cialdini-` and press Tab to see all commands. Here's what each does:

**Individual Techniques:**
- `reciprocity` - Emphasize resources you're providing
- `commitment` - Get agent to commit to plan first
- `social-proof` - Reference industry best practices
- `authority` - Cite official documentation
- `liking` - Build collaborative rapport
- `scarcity` - Emphasize constraints/urgency
- `unity` - Establish shared goals

**Meta Commands:**
- `persuade` - Get suggestions for which techniques to use
- `all` - Apply all 7 principles at once
- `analyze` - Evaluate an existing prompt

## Contributing

This is an experimental implementation. If you:
- Try these commands and observe measurable improvements
- Have ideas for better technique application
- Want to help run validation tests
- Find issues or edge cases

Please share feedback or open an issue!

## License

Educational and research purposes. See repository root for details.

## Citation

If you use these techniques in research or writing, please cite:

```
Cialdini, R. B. (2021). Influence: The Psychology of Persuasion (Revised Edition).
Harper Business.
```

And note that the application to AI agent instruction is experimental work from this repository.

---

**Last updated:** October 2025
**Status:** Experimental - Validation pending
