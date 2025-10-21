# Cialdini Persuasion Techniques for AI Agents - Notes

## Session: 2025-10-21

### Research Phase

**Objective:** Investigate how Robert Cialdini's persuasion techniques could be applied to instructing AI agents.

**Inspiration:** LinkedIn quote suggesting that using Cialdini's persuasion techniques helps AI agents adhere to instructions better.

**Research Findings:**

Dr. Robert Cialdini identified 7 principles of persuasion (originally 6, with Unity added later):

1. **Reciprocity** - People feel obligated to return favors
2. **Commitment and Consistency** - People align with their prior commitments and want to be consistent
3. **Social Proof (Consensus)** - People look to what others are doing
4. **Authority** - People defer to credible experts
5. **Liking** - People prefer to say yes to those they like
6. **Scarcity** - People want more of what is less available
7. **Unity** - People are influenced by shared identity

### Next Steps
- Create examples of each technique applied to AI agent instruction
- Brainstorm implementation approaches
- Write proposal document

### Examples Development Phase

Working on concrete examples of each principle applied to AI agent instruction:

**1. Reciprocity Examples:**
- Providing detailed context, code samples, and helpful resources upfront
- "I've prepared this comprehensive test suite for you - now please ensure the implementation passes all tests"
- Starting with "I'll give you full access to the codebase and documentation..."

**2. Commitment and Consistency Examples:**
- "First, outline your complete plan for this refactoring" (get commitment), then "Now follow the plan you outlined"
- "You agreed to follow PEP 8 style guidelines - please ensure this code adheres to them"
- Using todo lists to track commitments

**3. Social Proof (Consensus) Examples:**
- "Industry best practices suggest using dependency injection here..."
- "Most experienced developers handle this edge case by..."
- "This pattern is widely adopted in production systems because..."

**4. Authority Examples:**
- Citing official documentation: "According to the React docs..."
- "As specified in the system requirements document..."
- "The tech lead reviewed this and confirmed we should..."

**5. Liking Examples:**
- Expressing appreciation: "Great work on that last implementation!"
- Building rapport: "I really appreciate how thorough you are"
- Collaborative tone: "Let's work together on this"

**6. Scarcity Examples:**
- "We only have 5000 tokens left, so be concise"
- "This is a critical production bug - we need the fix within this session"
- "You have one chance to get this right before the deployment window closes"

**7. Unity Examples:**
- "We're both committed to code quality"
- "As fellow engineers, we know how important testing is"
- "Let's achieve this goal together as a team"


### Implementation Brainstorming Phase

Considering different approaches to help users apply these techniques:

**Option 1: Slash Commands**
- Pros: Simple, quick to invoke, user-friendly
- Cons: Static, less context-aware, limited interactivity
- Best for: Quick application of single techniques

**Option 2: Skills**
- Pros: Can be context-aware, interactive, sophisticated logic
- Cons: More complex to implement, potentially overwhelming
- Best for: Complex workflows that need to analyze context

**Option 3: Prompt Templates/Wrappers**
- Pros: Transparent, easy to understand and modify
- Cons: User needs to remember syntax
- Best for: Reusable patterns

**Option 4: Hybrid Approach**
- Slash commands for individual techniques
- A skill for analyzing user prompts and suggesting which techniques to apply
- Templates for common combinations

**Key Insights:**
- Different techniques suit different implementation methods
- Some techniques (like reciprocity, authority) are about how users phrase prompts
- Others (like commitment/consistency) are about workflow/process
- Some could be automated (Unity tone, social proof citations)
- Others require user judgment (when to apply scarcity)

**Recommended Approach:**
1. Slash commands for each individual technique (7 commands)
2. A meta-command to analyze and suggest techniques
3. A comprehensive command that applies multiple techniques
4. Optional: A skill for advanced analysis and application


### Proposal Writing Phase

Creating comprehensive proposal document with:
- Executive summary
- Technique descriptions with AI agent examples
- Implementation plan
- Specific slash command designs
- Future enhancement possibilities

Target file: cialdini-persuasion-proposal.md


### Completion

**Proposal Document Created:** cialdini-persuasion-proposal.md

**Summary of Recommendations:**

1. **Primary Implementation:** Slash commands for each of the 7 principles
   - Individual commands: /reciprocity, /commitment, /social-proof, /authority, /liking, /scarcity, /unity
   - Meta commands: /persuade (analyze and suggest), /persuade-all (apply all techniques)
   - Analysis command: /analyze-prompt (evaluate existing prompts)

2. **Key Advantages of Slash Command Approach:**
   - Simple and user-friendly
   - Discoverable and transparent
   - Composable with regular prompts
   - User maintains control

3. **Future Enhancement Paths:**
   - Skills for automatic analysis and suggestion
   - Hook integration for automatic application
   - Template library for common scenarios
   - Metrics tracking for validation

**Rationale:**
- Slash commands provide immediate value with low complexity
- Each technique can be used independently or in combination
- Users learn effective prompting principles through use
- Foundation for more sophisticated automation later

**Files Created:**
- cialdini-persuasion-proposal.md (comprehensive proposal with examples and implementation details)
- NOTES.md (this file, documenting the research and development process)

