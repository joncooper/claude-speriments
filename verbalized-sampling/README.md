# Verbalized Sampling: Claude Slash Commands

A collection of Claude Code slash commands implementing **Verbalized Sampling**, a research-backed prompting technique that dramatically improves LLM output diversity without sacrificing quality.

Based on the paper: [Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity](https://arxiv.org/abs/2510.01171) (arXiv:2510.01171v3)

## What is Verbalized Sampling?

**Verbalized Sampling (VS)** is a simple yet powerful prompt engineering technique that addresses "mode collapse" in aligned language models. After RLHF and instruction tuning, LLMs tend to become repetitive and overly conservative. VS counteracts this by explicitly asking the model to generate a probability distribution over multiple responses.

### Key Benefits

- **1.6-2.1x diversity improvement** over standard prompting
- **25.7% quality improvement** in human evaluations
- **Training-free**: Works with any LLM via prompting alone
- **Model-agnostic**: Compatible with GPT, Claude, Gemini, Llama, etc.
- **Safety-preserving**: Maintains alignment properties
- **Orthogonal to temperature**: Can combine with other sampling methods

### How It Works

**Traditional Prompt:**
```
Tell me a joke about coffee.
```
Result: Single, often repetitive response

**Verbalized Sampling:**
```xml
<instructions>
Generate 5 responses to the user query, each within a separate <response> tag.
Each <response> must include a <text> and a numeric <probability>.
Randomly sample responses from the full distribution.
</instructions>
Tell me a joke about coffee.
```
Result: 5 diverse responses with probabilities

## Quick Start

### Installation

1. **Clone or copy this repository** to your local machine

2. **Copy the commands to your Claude Code directory**:
   ```bash
   # From the repository root
   cp -r verbalized-sampling/commands/* ~/.claude/commands/
   ```

3. **Verify installation**:
   ```bash
   ls ~/.claude/commands/
   ```
   You should see the 12 command files listed.

4. **Restart Claude Code** (if currently running)

### Basic Usage

In Claude Code, simply type any slash command followed by your query:

```
/vs Tell me a creative story opening
```

```
/brainstorm How can we reduce urban traffic congestion?
```

```
/creative-diverse Write a haiku about mountains
```

The model will generate 5 diverse responses with probability values for each.

## Available Commands

### Core Commands

#### `/verbalized-sample` (or `/vs`)
**General-purpose verbalized sampling**

Use this for any task where you want diverse responses. This is the most faithful implementation of the paper's core technique.

**Example:**
```
/vs What are the implications of quantum computing?
```

**Best for:** General queries, exploration, when you want maximum diversity

---

#### `/vs-sample`
**Weighted sampling from distribution**

Generates a distribution of responses, then probabilistically samples one to return. Good when you want diversity but need a single answer.

**Example:**
```
/vs-sample What should I name my new app?
```

**Best for:** Decision-making, when you want probabilistic selection

---

### Creative & Writing

#### `/creative-diverse`
**Diverse creative content generation**

Optimized for creative writing tasks. Emphasizes originality and variety. Achieves the paper's reported 1.6-2.1x diversity improvement for creative tasks.

**Example:**
```
/creative-diverse Write a short poem about time
```

**Best for:** Stories, poems, jokes, creative writing

---

#### `/story-diverse`
**Diverse story variations and plot directions**

Specialized for narrative writing. Explores different genres, tones, and plot directions.

**Example:**
```
/story-diverse Continue this story: "The door creaked open..."
```

**Best for:** Fiction writing, plot development, exploring narrative possibilities

---

### Analysis & Thinking

#### `/multi-perspective`
**Multiple perspectives on a topic**

Generates intellectually diverse viewpoints. Considers different stakeholders, frameworks, and analytical approaches.

**Example:**
```
/multi-perspective Should cities ban cars from downtown areas?
```

**Best for:** Complex issues, debate prep, understanding different angles

---

#### `/brainstorm`
**High-diversity idea generation**

Optimized for ideation. Mixes conventional and unconventional ideas, different scales and approaches.

**Example:**
```
/brainstorm How can we make online learning more engaging?
```

**Best for:** Problem-solving, innovation, ideation sessions

---

#### `/compare-options`
**Diverse evaluation perspectives**

Evaluates options from multiple angles using different criteria, values, and stakeholder perspectives.

**Example:**
```
/compare-options Python vs JavaScript for backend development
```

**Best for:** Decision-making, trade-off analysis, comparing alternatives

---

### Communication & Dialogue

#### `/dialogue-sim`
**Realistic dialogue with behavioral variance**

Simulates how a character/person might respond differently in different moments. Captures authentic human variability.

**Example:**
```
/dialogue-sim How might a shy teenager respond when asked to give a presentation?
```

**Best for:** Writing dialogue, character development, social simulation

---

#### `/explain-diverse`
**Multiple diverse explanations**

Generates different ways to explain a concept, varying style, technicality, and approach.

**Example:**
```
/explain-diverse Explain blockchain technology
```

**Best for:** Teaching, documentation, making concepts accessible

---

#### `/diverse-answers`
**Open-ended questions with multiple valid answers**

For questions where multiple perspectives are valid. Represents the natural diversity of expert opinion.

**Example:**
```
/diverse-answers What makes a good leader?
```

**Best for:** Open-ended questions, philosophical queries, subjective topics

---

### Code & Technical

#### `/code-diverse`
**Diverse code solutions**

Explores different implementation approaches, algorithms, and design patterns for programming tasks.

**Example:**
```
/code-diverse Implement a function to find duplicates in an array
```

**Best for:** Algorithm exploration, learning different approaches, code review

---

## Command Reference Table

| Command | Use Case | Diversity Focus |
|---------|----------|----------------|
| `/verbalized-sample` or `/vs` | General purpose | Maximum diversity |
| `/vs-sample` | Single response from distribution | Weighted selection |
| `/creative-diverse` | Creative writing | Styles, tones, genres |
| `/story-diverse` | Fiction & narratives | Plot directions, genres |
| `/multi-perspective` | Analysis & debate | Viewpoints, frameworks |
| `/brainstorm` | Ideation | Different approaches & scales |
| `/compare-options` | Decision support | Evaluation criteria |
| `/dialogue-sim` | Character responses | Behavioral variance |
| `/explain-diverse` | Teaching & docs | Pedagogical approaches |
| `/diverse-answers` | Open-ended QA | Valid perspectives |
| `/code-diverse` | Programming | Algorithms, patterns |

## Understanding the Output

All commands generate responses in this format:

```xml
<response>
  <text>
  The actual response content goes here...
  </text>
  <probability>0.25</probability>
</response>
```

### What do the probabilities mean?

The probabilities represent the model's estimate of how likely each response is in the full distribution of valid responses. They typically sum to approximately 1.0.

**Key points:**
- Higher probability = more typical/common response
- Lower probability = less common but still valid response
- Probabilities help you understand the response landscape
- Don't just pick the highest probability - explore the diversity!

### How to use the responses

1. **Explore all responses** - Read through all 5 to get different perspectives
2. **Compare and contrast** - Look at how approaches differ
3. **Combine ideas** - Mix elements from different responses
4. **Choose what fits** - Pick the response that best fits your needs
5. **Iterate** - Use a response as a starting point and refine

## Examples

### Example 1: Creative Writing

**Command:**
```
/creative-diverse Write the opening line of a mystery novel
```

**Why Verbalized Sampling helps:**
- Gets beyond cliché opening lines
- Explores different mystery subgenres
- Different tones (noir, cozy, thriller)
- More original and unexpected options

---

### Example 2: Problem Solving

**Command:**
```
/brainstorm How can we reduce food waste in restaurants?
```

**Why Verbalized Sampling helps:**
- Mix of conventional and innovative ideas
- Different scales (individual to systemic)
- Different approaches (tech, policy, behavioral)
- More comprehensive solution space

---

### Example 3: Technical Analysis

**Command:**
```
/multi-perspective Is microservices architecture right for our project?
```

**Why Verbalized Sampling helps:**
- Different stakeholder views (devs, ops, business)
- Different time horizons (short vs long term)
- Different scales (startup vs enterprise)
- More nuanced decision-making

---

### Example 4: Code Exploration

**Command:**
```
/code-diverse Sort an array in JavaScript
```

**Why Verbalized Sampling helps:**
- Different algorithms (bubble, quick, merge, etc.)
- Different trade-offs (time vs space)
- Different paradigms (functional, imperative)
- Learning multiple approaches

## Customization

All commands are stored as markdown files in the `commands/` directory of this project. After installation, they'll be in your `~/.claude/commands/` directory. You can customize them:

### Changing the number of responses

Edit any command file in your `~/.claude/commands/` directory and change the number in the instructions:

```markdown
Generate 5 responses...  →  Generate 10 responses...
```

### Creating custom commands

1. Create a new `.md` file in `~/.claude/commands/`
2. Add YAML frontmatter with a description:
   ```markdown
   ---
   description: Your command description
   ---
   ```
3. Write your verbalized sampling prompt
4. Save and restart Claude Code

### Example custom command

Create `~/.claude/commands/haiku-diverse.md`:

```markdown
---
description: Generate diverse haiku variations
---

You are using Verbalized Sampling for haiku generation.

<instructions>
Generate 5 different haiku about the user's topic.
Each haiku should explore a different mood, imagery, or perspective.
Provide each within a <response> tag with <text> and <probability>.
Ensure diversity in tone and imagery.
</instructions>

Haiku topic:
```

## Tips for Best Results

### 1. Be specific about what you want diversity in
- ❌ "Tell me about dogs"
- ✅ "What are different reasons people choose to get dogs?"

### 2. Use the right command for your task
- Creative tasks → `/creative-diverse` or `/story-diverse`
- Analysis → `/multi-perspective` or `/brainstorm`
- Dialogue → `/dialogue-sim`

### 3. Explore all responses, not just the first
The highest probability response isn't always the best for your needs!

### 4. Combine with iteration
Use VS to explore the space, then pick a direction and refine.

### 5. Adjust expectations for the task
Some tasks have naturally less diversity (factual questions) vs more (creative writing).

## Research Background

This implementation is based on rigorous academic research:

### Paper Details
- **Title:** Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity
- **arXiv ID:** 2510.01171v3
- **Website:** https://www.verbalized-sampling.com/
- **GitHub:** https://github.com/CHATS-lab/verbalized-sampling

### Key Findings

**Diversity Improvements:**
- Creative writing: **1.6-2.1x more diverse** than baseline
- Recovers **66.8% of base model's diversity** lost to alignment

**Quality Improvements:**
- **25.7% better** in human quality evaluations
- Maintains factual accuracy and safety
- Improves realism in dialogue simulation
- Better downstream performance for synthetic data

**How It Works:**
The technique counteracts "typicality bias" in RLHF training data by explicitly requesting a probability distribution, forcing the model to consider the full range of possibilities rather than just the most typical response.

### Applications Validated in Paper

1. **Creative Writing** - Stories, poems, creative content
2. **Social Simulation** - Realistic dialogue and character behavior
3. **Open-Ended QA** - Questions with multiple valid answers
4. **Synthetic Data Generation** - Training data with better diversity

## Project Files

```
verbalized-sampling/
├── README.md                  # This file
├── PAPER_SUMMARY.md          # Detailed summary of the research paper
├── NOTES.md                  # Extensive research and implementation notes
└── commands/
    ├── verbalized-sample.md      # Core VS implementation
    ├── vs.md                     # Shorthand version
    ├── creative-diverse.md       # Creative writing
    ├── story-diverse.md          # Story generation
    ├── multi-perspective.md      # Multi-perspective analysis
    ├── brainstorm.md             # Ideation
    ├── dialogue-sim.md           # Dialogue simulation
    ├── explain-diverse.md        # Multiple explanations
    ├── diverse-answers.md        # Open-ended QA
    ├── vs-sample.md              # Weighted sampling
    ├── code-diverse.md           # Code generation
    └── compare-options.md        # Option comparison
```

### File Descriptions

- **README.md** - Usage guide and quick reference (you are here)
- **PAPER_SUMMARY.md** - Comprehensive summary of the research paper, findings, and techniques
- **NOTES.md** - Detailed research notes and implementation documentation
- **Command files** - Individual slash command implementations

## Troubleshooting

### Commands not showing up

1. Verify files are in `~/.claude/commands/` (or your Claude Code commands directory)
2. Restart Claude Code
3. Check file permissions: `chmod 644 ~/.claude/commands/*.md`

### Responses not diverse enough

1. Try a different command optimized for your task
2. Make your query more specific about the dimension of diversity you want
3. Remember some tasks naturally have less diversity than others

### Output format issues

The commands expect Claude to return XML-formatted responses. If you're getting plain text:
- The model may have decided a different format is more appropriate
- Try rephrasing your query
- The diversity is still there even if format varies

### Want to modify commands

All commands are just text files! Edit them freely:
```bash
nano ~/.claude/commands/brainstorm.md
```

Change the number of responses, adjust instructions, or create entirely new variants.

## Contributing

Found a great use case? Created a custom command? Have suggestions?

This is an experimental implementation of cutting-edge research. Contributions, feedback, and new command variants are welcome!

## FAQ

**Q: Do I need to use the XML output format?**
A: No, the model may adapt the format. The key is getting diverse responses with probabilities.

**Q: Should I always pick the highest probability response?**
A: No! The whole point is exploring diversity. Lower probability responses can be more creative/unexpected.

**Q: Can I use multiple commands in sequence?**
A: Yes! Try `/brainstorm` then `/compare-options` to ideate and evaluate.

**Q: Does this work with other Claude interfaces?**
A: These are Claude Code slash commands, but you can copy the prompts and use them anywhere.

**Q: How is this different from just asking for multiple responses?**
A: Asking for probabilities changes how the model reasons about the task, leading to more systematic exploration of the response space.

**Q: Can I change the number of responses?**
A: Yes! Edit the command files and change "Generate 5" to any number you like.

**Q: Does this make responses slower?**
A: Slightly, since you're getting 5 responses instead of 1. But it's much more efficient than 5 separate queries.

**Q: Will this work with future Claude models?**
A: Yes! The technique is training-free and model-agnostic. It works through prompting alone.

## Learn More

- **Paper:** https://arxiv.org/abs/2510.01171
- **Project website:** https://www.verbalized-sampling.com/
- **Research code:** https://github.com/CHATS-lab/verbalized-sampling
- **PAPER_SUMMARY.md** in this repository for detailed research breakdown

## License

These slash commands are provided as-is for educational and research purposes. The prompting technique is based on published academic research.

## Citation

If you use these commands in research or writing, please cite the original paper:

```bibtex
@article{verbalizedsampling2024,
  title={Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity},
  author={[Authors from paper]},
  journal={arXiv preprint arXiv:2510.01171},
  year={2024}
}
```

---

**Built with:** Research-backed prompt engineering
**Powered by:** Claude and the Verbalized Sampling technique
**Version:** 1.0
**Date:** October 2025
