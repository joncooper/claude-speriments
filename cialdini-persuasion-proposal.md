# Cialdini Persuasion Techniques for AI Agent Instruction

## Executive Summary

This proposal explores how Dr. Robert Cialdini's 7 principles of persuasion can be systematically applied to improve AI agent instruction adherence. Based on the observation that these techniques help agents better follow instructions, we propose implementing a set of slash commands in Claude Code that enable users to easily apply these principles to their prompts.

**Key Benefits:**
- Improved agent instruction adherence
- More consistent agent behavior
- Better task completion rates
- Reduced need for prompt iteration
- Systematic approach to effective prompting

---

## The 7 Cialdini Principles

### 1. Reciprocity
**Principle:** People feel obligated to return favors and gestures of goodwill.

**Application to AI Agents:**
When you provide comprehensive context, helpful resources, or do preparatory work for the agent, frame your request as building on that foundation.

**Examples:**
- "I've prepared this comprehensive test suite with 50+ test cases for you. Now please ensure your implementation passes all of them."
- "I've read through the entire codebase and documented the architecture for you. Using this documentation, please implement the new feature."
- "I've given you full access to all relevant files and dependencies. Please use them to complete this refactoring."

### 2. Commitment and Consistency
**Principle:** People want to be consistent with their prior commitments and stated positions.

**Application to AI Agents:**
Get the agent to commit to an approach, plan, or standard early, then reference that commitment throughout the task.

**Examples:**
- "First, outline your complete plan for this refactoring, including all files you'll modify." → Then: "Now execute the plan you outlined above."
- "You agreed to follow PEP 8 style guidelines. Please ensure this code adheres to them."
- "You committed to making this function O(log n). Make sure your implementation meets that commitment."
- Using TodoWrite to create explicit commitments that the agent then fulfills

### 3. Social Proof (Consensus)
**Principle:** People look to what others are doing to guide their own behavior.

**Application to AI Agents:**
Reference industry best practices, common patterns, or how experienced developers typically handle similar situations.

**Examples:**
- "Industry best practices suggest using dependency injection here rather than global state."
- "Most experienced Go developers handle this error case by wrapping it with context."
- "This pattern is widely adopted in production React applications because it prevents memory leaks."
- "The top 1000 Python projects on GitHub typically use this approach for async operations."

### 4. Authority
**Principle:** People defer to credible experts and authoritative sources.

**Application to AI Agents:**
Cite official documentation, specifications, expert opinions, or established requirements.

**Examples:**
- "According to the official React documentation, hooks must be called in the same order on every render."
- "As specified in RFC 7231, HTTP PUT requests must be idempotent."
- "The tech lead reviewed this and confirmed we should use PostgreSQL for this feature."
- "The system requirements document mandates that all user data must be encrypted at rest."

### 5. Liking
**Principle:** People prefer to say yes to those they like and have rapport with.

**Application to AI Agents:**
Express appreciation, build collaborative rapport, and maintain a positive tone.

**Examples:**
- "Great work on that last implementation! Now let's tackle this next challenge together."
- "I really appreciate how thorough you are with edge cases. Please apply that same care here."
- "I've enjoyed working with you on this project. Let's finish strong with this final feature."
- "Your attention to detail is exactly what we need for this security-critical code."

### 6. Scarcity
**Principle:** People want more of what is less available or time-limited.

**Application to AI Agents:**
Emphasize constraints, limited resources, or unique opportunities.

**Examples:**
- "We only have 5000 tokens left in this session, so please be concise and focused."
- "This is a critical production bug affecting customers right now - we need the fix completed in this session."
- "You have one chance to get this right before the deployment window closes in 30 minutes."
- "This is the only opportunity to refactor this code before the API freeze."

### 7. Unity
**Principle:** People are influenced by shared identity and common goals.

**Application to AI Agents:**
Establish shared purpose, common identity, or collective goals.

**Examples:**
- "We're both committed to code quality and user safety. Let's ensure this implementation reflects those values."
- "As fellow engineers, we both know how important comprehensive testing is."
- "Let's achieve this milestone together and deliver something we can both be proud of."
- "Our shared goal is creating software that's maintainable for the next developer."

---

## Proposed Implementation

### Approach: Slash Commands with Prefix Naming

We recommend implementing **slash commands using a `/cialdini-*` prefix** for the following reasons:

1. **Ease of Use:** Simple to invoke and learn
2. **Full Autocomplete:** Tab completion works for all commands
3. **Clear Grouping:** Commands sort together alphabetically, showing they're related
4. **Clean Namespace:** Prefix indicates these are Cialdini techniques without subcommand complexity
5. **Discoverability:** Users can type `/cialdini-` and see all available techniques
6. **Composability:** Can be combined with regular prompts
7. **Transparency:** Users understand exactly what's being applied
8. **Flexibility:** Users control when and how to apply each technique

**Design Decision:** We chose prefix naming (`/cialdini-reciprocity`) over subcommands (`/cialdini reciprocity`) because Claude Code's tab completion is based on command filenames, not subcommand parsing. This gives users the best of both worlds: namespace organization AND full autocomplete support.

### Command Design

#### Individual Technique Commands

Each principle gets its own command that wraps the user's prompt:

**`/cialdini-reciprocity <your prompt>`**
- Prepends context about providing resources/context
- Frames the request as building on foundation you've provided

**`/cialdini-commitment <your prompt>`**
- First asks agent to state their plan/approach
- Then instructs them to follow through on it
- Can optionally use TodoWrite for tracking

**`/cialdini-social-proof <your prompt>`**
- Adds context about industry best practices
- References common patterns and widespread adoption
- Cites "experienced developers" doing similar work

**`/cialdini-authority <your prompt>`**
- Prompts user to optionally specify authoritative sources
- Frames request in terms of official requirements/specs
- Adds weight of documentation and standards

**`/cialdini-liking <your prompt>`**
- Adds appreciative, collaborative framing
- Builds rapport before the request
- Uses positive, team-oriented language

**`/cialdini-scarcity <your prompt>`**
- Emphasizes time/resource constraints
- Frames as important/urgent opportunity
- Adds focus through limitation

**`/cialdini-unity <your prompt>`**
- Establishes shared goals and values
- Uses "we" language and collective identity
- Frames as collaborative achievement

#### Meta Commands

**`/cialdini-persuade <your prompt>`**
- Analyzes the prompt and suggests which 2-3 techniques would be most effective
- Explains why those techniques are recommended
- Offers to apply them

**`/cialdini-all <your prompt>`**
- Applies all 7 techniques in a carefully balanced way
- Uses sophisticated prompt engineering to combine them naturally
- Best for critical, complex tasks requiring maximum adherence

#### Analysis Command

**`/cialdini-analyze <your prompt>`**
- Analyzes an existing prompt
- Identifies which Cialdini principles are already present
- Suggests which additional principles could improve it
- Shows before/after comparison

---

## Implementation Details

### File Structure

```
.claude/
  commands/
    cialdini-reciprocity.md
    cialdini-commitment.md
    cialdini-social-proof.md
    cialdini-authority.md
    cialdini-liking.md
    cialdini-scarcity.md
    cialdini-unity.md
    cialdini-persuade.md
    cialdini-all.md
    cialdini-analyze.md
```

All commands will autocomplete when typing `/cialdini-` followed by tab.

### Example Command Implementation

**File: `.claude/commands/cialdini-reciprocity.md`**

```markdown
---
description: Apply Cialdini's Reciprocity principle to your prompt
---

I want to apply the Reciprocity principle to the following request.

Before making the request, I'll establish what I'm providing to you:

CONTEXT I'M PROVIDING:
- Full access to the codebase and all relevant files
- Any research, documentation, or preparatory work I've done
- Clear requirements and test cases
- Tools and resources you need to succeed

Now, building on this foundation I've provided, here's what I need:

{{prompt}}

Please recognize the comprehensive context and resources I've given you, and provide an equally thorough and complete response.
```

### Example Meta Command Implementation

**File: `.claude/commands/cialdini-persuade.md`**

```markdown
---
description: Analyze prompt and suggest which Cialdini techniques to apply
---

I have a task I want to give you, but first I need your help optimizing how I phrase it.

Here's my initial request:
{{prompt}}

Please analyze this request and:

1. Identify which of Cialdini's 7 persuasion principles would be most effective here:
   - Reciprocity (emphasizing resources I'm providing)
   - Commitment & Consistency (getting you to commit to an approach)
   - Social Proof (citing best practices and common patterns)
   - Authority (referencing official docs and requirements)
   - Liking (building rapport and appreciation)
   - Scarcity (emphasizing constraints or urgency)
   - Unity (establishing shared goals)

2. Recommend the top 2-3 principles that would most improve instruction adherence for this specific task

3. Explain WHY those principles are most relevant

4. Show me what the enhanced prompt would look like with those principles applied

5. Ask if I'd like you to proceed with the enhanced version

Be thoughtful and selective - not every principle fits every situation.
```

---

## Usage Examples

### Example 1: Critical Bug Fix

**Before:**
```
Fix the authentication bug in user_service.py
```

**After (using /cialdini-scarcity):**
```
/cialdini-scarcity According to the incident report and tech lead guidance,
fix the authentication bug in user_service.py. This is affecting
production users right now and needs to be resolved in this session.
```

### Example 2: Complex Refactoring

**Before:**
```
Refactor the payment processing module to use the new API
```

**After (using /cialdini-commitment):**
```
/cialdini-commitment Refactor the payment processing module to use the new API.
First outline your complete refactoring plan, then execute it following
industry best practices for payment system migrations.
```

### Example 3: Code Review Request

**Before:**
```
Review this pull request and suggest improvements
```

**After (using /cialdini-reciprocity):**
```
/cialdini-reciprocity I've prepared detailed context about this PR including
the business requirements, test coverage report, and performance benchmarks.
Using this comprehensive context, let's review this together and ensure
it meets our shared standards for code quality and maintainability.
```

---

## Future Enhancements

### Phase 2: Skill-Based Implementation

A more sophisticated skill could:
- Automatically detect task context and suggest appropriate techniques
- Learn which techniques work best for which types of tasks
- Provide interactive prompt optimization
- Track success rates of different technique combinations

### Phase 3: Automatic Application

Integration with Claude Code hooks:
- Pre-submit hook that analyzes prompts
- Suggests technique application before sending
- Optional auto-enhancement mode

### Phase 4: Template Library

Pre-built templates for common scenarios:
- "Critical bug fix" (scarcity + authority)
- "Complex refactoring" (commitment + social proof)
- "Code review" (reciprocity + unity)
- "New feature" (commitment + social proof + authority)

---

## Research and Validation

**See [cialdini-test-plan.md](./cialdini-test-plan.md) for comprehensive testing methodology.**

### Testing Approach Overview

To rigorously validate whether these techniques actually work (vs. "prompting theater"), we use:

1. **A/B Testing with Automated Validation**
   - Control vs. Treatment on identical tasks
   - Deterministic, reproducible results
   - Statistical significance testing

2. **Benchmark Task Suite**
   - 10 tasks across 5 categories
   - Clear pass/fail criteria (automated checks)
   - Tests for instruction adherence, completeness, consistency

3. **Verbosity Control**
   - Test if improvements come from technique content or just longer prompts
   - Critical for validating mechanism

4. **Multiple Experiments**
   - Individual technique efficacy
   - Technique-to-task matching
   - Combined technique effectiveness

### Primary Metrics

- **Instruction Adherence Rate (IAR):** % of instructions followed
- **First-Try Success Rate (FTSR):** % passing all criteria immediately
- **Completeness Score:** % fully implemented (no TODOs/stubs)
- **Constraint Violation Rate:** # of hard constraints broken

### Success Criteria

For techniques to be validated:
- Statistical significance (p < 0.05)
- ≥15% improvement in IAR
- Cohen's d ≥ 0.5 (medium-to-large effect)
- Improvement on ≥70% of tasks
- NOT explained by verbosity alone

---

## Conclusion

Cialdini's persuasion principles offer a systematic, research-backed approach to improving AI agent instruction adherence. By implementing these as slash commands in Claude Code, we provide users with:

- **Immediate value** through simple, actionable commands
- **Educational benefit** by teaching effective prompting principles
- **Flexibility** to apply techniques as needed
- **Foundation** for future AI-assisted prompt optimization

The slash command approach balances ease of use with power, making these techniques accessible to all users while leaving room for sophisticated future enhancements.

---

## Next Steps

1. **Validate concept** - Get user feedback on this proposal
2. **Prototype commands** - Implement 2-3 commands to test effectiveness
3. **Iterate** - Refine based on real-world usage
4. **Expand** - Add remaining commands and meta-commands
5. **Measure** - Track metrics to validate impact
6. **Enhance** - Consider skill-based or automated applications

---

## Appendix: Quick Reference

| Command | Principle | When to Use | Key Phrase |
|---------|-----------|-------------|------------|
| `/cialdini-reciprocity` | Reciprocity | You've provided extensive context | "I've given you..." |
| `/cialdini-commitment` | Commitment | Complex multi-step tasks | "First outline your plan..." |
| `/cialdini-social-proof` | Social Proof | Standard patterns exist | "Industry best practices..." |
| `/cialdini-authority` | Authority | Official requirements exist | "According to the docs..." |
| `/cialdini-liking` | Liking | Building ongoing relationship | "Great work on..." |
| `/cialdini-scarcity` | Scarcity | Time/resource constraints | "We only have..." |
| `/cialdini-unity` | Unity | Collaborative goals | "We're both committed to..." |
| `/cialdini-persuade` | Meta | Need help choosing techniques | Analyzes & suggests |
| `/cialdini-all` | Meta | Critical/complex tasks | Applies all 7 principles |
| `/cialdini-analyze` | Meta | Evaluate existing prompt | Shows improvements |

---

*Generated: 2025-10-21*
