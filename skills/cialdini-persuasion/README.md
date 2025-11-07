# Cialdini Persuasion Techniques for AI Agents

A collection of Claude Code slash commands that apply **Dr. Robert Cialdini's 7 principles of persuasion** to improve AI agent instruction adherence and task completion.

## What Are These Techniques?

Dr. Robert Cialdini's research identified 7 universal principles of persuasion that influence human behavior. This experiment applies these same principles to improve how AI agents follow instructions, complete tasks, and maintain consistency.

### Key Benefits

- **Improved instruction adherence** - Agents follow directions more reliably
- **More consistent behavior** - Reduced variability in task execution
- **Better completion rates** - Higher success rate on complex tasks
- **Less iteration needed** - Get better results on first attempt
- **Systematic approach** - Proven framework for effective prompting

## The 7 Principles

### 1. **Reciprocity**
When you provide context, resources, or preparatory work, agents feel obligated to reciprocate with thorough work.

### 2. **Commitment and Consistency**
Getting agents to commit to a plan or approach early makes them more likely to follow through consistently.

### 3. **Social Proof (Consensus)**
Referencing industry best practices and common patterns guides agent behavior toward proven solutions.

### 4. **Authority**
Citing official documentation, specs, and expert sources increases compliance with requirements.

### 5. **Liking**
Acknowledging agent capabilities and past successes creates better cooperation.

### 6. **Scarcity**
Emphasizing limited time, resources, or opportunities focuses agent attention and effort.

### 7. **Unity**
Framing tasks as shared goals creates stronger commitment to success.

## Quick Start

### Installation

1. **Clone or copy this repository** to your local machine

2. **Copy the commands to your Claude Code directory**:
   ```bash
   # From the repository root
   cp -r cialdini-persuasion/commands/* ~/.claude/commands/
   ```

3. **Verify installation**:
   ```bash
   ls ~/.claude/commands/cialdini-*
   ```
   You should see the 10 command files.

4. **Restart Claude Code** (if currently running)

### Basic Usage

In Claude Code, use any Cialdini command followed by your task:

```
/cialdini-reciprocity Implement user authentication with these API docs I've prepared
```

```
/cialdini-commitment First plan the refactoring, then execute it
```

```
/cialdini-authority According to the Python docs, implement this using context managers
```

## Available Commands

### Individual Technique Commands

#### `/cialdini-reciprocity`
**Principle:** Reciprocity - returning favors and gestures

Apply when you've provided extensive context, resources, or done preparatory work. The agent reciprocates your effort with thorough execution.

**Example:**
```
/cialdini-reciprocity I've prepared comprehensive test cases and documentation. Please implement the feature to pass all tests.
```

---

#### `/cialdini-commitment`
**Principle:** Commitment and Consistency

Get the agent to commit to an approach or plan first, then ensure consistent follow-through.

**Example:**
```
/cialdini-commitment First outline your complete testing strategy, then implement all the tests you described.
```

---

#### `/cialdini-social-proof`
**Principle:** Social Proof (Consensus)

Reference industry best practices, common patterns, and how experienced developers handle similar situations.

**Example:**
```
/cialdini-social-proof Industry best practice is to use dependency injection here. Implement it that way.
```

---

#### `/cialdini-authority`
**Principle:** Authority and credible sources

Cite official documentation, specifications, standards, or expert requirements.

**Example:**
```
/cialdini-authority According to the React documentation, hooks must be called in the same order. Ensure your code follows this requirement.
```

---

#### `/cialdini-liking`
**Principle:** Liking and rapport

Acknowledge the agent's capabilities and past successes to create better cooperation.

**Example:**
```
/cialdini-liking You've done excellent work on similar refactorings. Please apply that same expertise to optimize this module.
```

---

#### `/cialdini-scarcity`
**Principle:** Scarcity and urgency

Emphasize limited time, resources, or opportunities to focus attention and effort.

**Example:**
```
/cialdini-scarcity This is our one chance to get the migration right before the deadline. Please be extra thorough.
```

---

#### `/cialdini-unity`
**Principle:** Unity and shared identity

Frame the task as a shared goal where you're working together toward success.

**Example:**
```
/cialdini-unity We're both committed to shipping high-quality code. Let's work together to make this implementation robust.
```

---

### Combination Commands

#### `/cialdini-persuade`
**Apply multiple principles at once**

Combines the most effective principles for maximum instruction adherence.

**Example:**
```
/cialdini-persuade Implement the authentication system following the security standards we discussed.
```

---

#### `/cialdini-all`
**Apply all 7 principles comprehensively**

The most thorough application - uses all principles in a structured way.

**Example:**
```
/cialdini-all Complete this complex refactoring while maintaining backward compatibility.
```

---

#### `/cialdini-analyze`
**Analyze which principles would be most effective**

Before applying techniques, analyze your task to identify which principles would work best.

**Example:**
```
/cialdini-analyze I need to get the agent to write comprehensive tests for a complex API
```

---

## Command Reference Table

| Command | Principle | Best For |
|---------|-----------|----------|
| `/cialdini-reciprocity` | Reciprocity | When you've provided extensive resources |
| `/cialdini-commitment` | Commitment | When you want a plan followed consistently |
| `/cialdini-social-proof` | Social Proof | When best practices matter |
| `/cialdini-authority` | Authority | When citing official requirements |
| `/cialdini-liking` | Liking | When building on past success |
| `/cialdini-scarcity` | Scarcity | When time/resources are limited |
| `/cialdini-unity` | Unity | When framing as shared goal |
| `/cialdini-persuade` | Multiple | General purpose, strong adherence |
| `/cialdini-all` | All 7 | Complex tasks needing max adherence |
| `/cialdini-analyze` | Analysis | Choosing the right technique |

## When to Use Each Technique

### Use **Reciprocity** when:
- You've done preparatory work (research, documentation, test cases)
- You've provided extensive context or resources
- You want the agent to match your effort level

### Use **Commitment** when:
- You need consistent execution of a multi-step plan
- You want to lock in an approach early
- Previous iterations lacked consistency

### Use **Social Proof** when:
- Industry best practices are important
- You want to avoid anti-patterns
- Common solutions exist for the problem

### Use **Authority** when:
- Official documentation or specs must be followed
- Compliance with standards is required
- Expert opinions are relevant

### Use **Liking** when:
- Building on previous successful work
- You want cooperative problem-solving
- Positive reinforcement would help

### Use **Scarcity** when:
- Deadlines are tight
- This is a critical one-time operation
- Resources are limited

### Use **Unity** when:
- Framing as collaborative effort
- Shared goals are important
- You want strong buy-in

## Examples

### Example 1: Complex Refactoring

**Without Cialdini:**
```
Refactor the authentication system to use OAuth2
```

**With Cialdini (Commitment + Authority):**
```
/cialdini-commitment First, outline your refactoring plan following the OAuth2 RFC 6749 specification. Then execute that plan consistently.
```

**Result:** Agent commits to a specific approach aligned with specs, then executes it consistently.

---

### Example 2: Comprehensive Testing

**Without Cialdini:**
```
Write tests for the API
```

**With Cialdini (Reciprocity + Social Proof):**
```
/cialdini-reciprocity I've documented all API endpoints and edge cases. Following industry testing best practices, please write comprehensive tests covering all scenarios I've documented.
```

**Result:** Agent reciprocates your documentation work with thorough tests using proven patterns.

---

### Example 3: Critical Bug Fix

**Without Cialdini:**
```
Fix the memory leak in the background worker
```

**With Cialdini (Scarcity + Authority):**
```
/cialdini-scarcity This is a production issue affecting customers right now. According to the language memory management docs, implement a fix that prevents this leak.
```

**Result:** Agent prioritizes the urgency and follows authoritative guidance for the fix.

---

## Tips for Best Results

### 1. Choose the Right Principle(s)
Not every principle applies to every task. Use `/cialdini-analyze` when unsure.

### 2. Be Specific
The principles work best when combined with clear, specific instructions.

### 3. Combine Principles
Using 2-3 complementary principles is often more effective than just one.

### 4. Match Your Tone
The commands apply the principles, but your task description matters too.

### 5. Use for Complex Tasks
Simple tasks may not benefit much; these techniques shine on complex, multi-step work.

## Research Background

Based on Dr. Robert Cialdini's research on the psychology of persuasion, particularly:

- **"Influence: The Psychology of Persuasion"** (1984, revised 2021)
- **"Pre-Suasion: A Revolutionary Way to Influence and Persuade"** (2016)
- Decades of social psychology research on compliance and persuasion

### The Science

Cialdini's 7 principles are based on rigorous research showing they reliably influence human behavior. This implementation hypothesis: if AI agents are trained on human text data where these principles are effective, they should respond similarly when the principles are applied to instructions.

## Project Files

```
cialdini-persuasion/
├── README.md                     # This file
├── proposal.md                   # Original proposal and detailed principle explanations
├── test-plan.md                  # Comprehensive testing methodology
├── NOTES.md                      # Implementation notes
└── commands/
    ├── cialdini-reciprocity.md
    ├── cialdini-commitment.md
    ├── cialdini-social-proof.md
    ├── cialdini-authority.md
    ├── cialdini-liking.md
    ├── cialdini-scarcity.md
    ├── cialdini-unity.md
    ├── cialdini-persuade.md      # Multiple principles
    ├── cialdini-all.md           # All 7 principles
    └── cialdini-analyze.md       # Technique selection helper
```

### File Descriptions

- **README.md** - Usage guide (you are here)
- **proposal.md** - Detailed explanation of each principle with examples
- **test-plan.md** - Testing methodology and validation approach
- **NOTES.md** - Implementation notes and observations
- **commands/** - Individual slash command implementations

## Customization

All commands are markdown files in the `commands/` directory. After installation, they're in `~/.claude/commands/`. You can:

### Modify Existing Commands

Edit command files to adjust how principles are applied:

```bash
nano ~/.claude/commands/cialdini-reciprocity.md
```

### Create Custom Combinations

Create new commands that combine principles for your specific use cases:

```bash
cp ~/.claude/commands/cialdini-persuade.md ~/.claude/commands/cialdini-custom.md
# Edit to create your custom combination
```

## Troubleshooting

### Commands not showing up

1. Verify files are in `~/.claude/commands/`
2. Check files have the `cialdini-` prefix
3. Restart Claude Code
4. Check file permissions: `chmod 644 ~/.claude/commands/cialdini-*.md`

### Not seeing improved adherence

1. Make sure you're applying relevant principles (try `/cialdini-analyze`)
2. Combine principles for complex tasks
3. Be specific in your task description
4. Try `/cialdini-all` for maximum effect

### Want to test effectiveness

See `test-plan.md` for a comprehensive testing methodology comparing results with and without these techniques.

## FAQ

**Q: Do these actually work?**
A: The proposal is based on observation that these techniques improve agent behavior. The test-plan.md provides methodology for systematic validation.

**Q: Which command should I use?**
A: Use `/cialdini-analyze` to get recommendations, or start with `/cialdini-persuade` for general use.

**Q: Can I use multiple principles at once?**
A: Yes! `/cialdini-persuade` and `/cialdini-all` do this. You can also combine individual commands.

**Q: Are these manipulative?**
A: These are instructional techniques to improve task completion. They're transparent and don't involve deception.

**Q: Will this work with other LLMs?**
A: Likely yes - if the LLM is trained on human text where these principles are effective, it should respond similarly.

**Q: Can I use these outside Claude Code?**
A: Yes! The commands are just prompts - you can copy the techniques and use them in any interface.

## Learn More

- **proposal.md** - Detailed explanation of each principle with more examples
- **test-plan.md** - Methodology for testing effectiveness
- **Cialdini's books** - Original research and applications

## Citation

If you use these techniques in research or writing, please cite:

```
Cialdini, R. B. (2021). Influence: The Psychology of Persuasion (New and Expanded). Harper Business.
```

---

**Based on:** Dr. Robert Cialdini's research on persuasion
**Implementation:** Claude Code slash commands
**Version:** 1.0
**Date:** October 2025
