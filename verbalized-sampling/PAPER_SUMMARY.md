# Paper Summary: Verbalized Sampling

## Citation
**Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity**
arXiv:2510.01171v3
Website: https://www.verbalized-sampling.com/
GitHub: https://github.com/CHATS-lab/verbalized-sampling

---

## Executive Summary

This paper introduces **Verbalized Sampling (VS)**, a simple yet powerful training-free prompting technique that dramatically improves the diversity of LLM outputs without sacrificing quality, safety, or factual accuracy. The technique addresses the common problem of **mode collapse** in aligned language models, where post-training processes (RLHF, instruction tuning) make models overly conservative and repetitive.

**Key Achievement**: VS improves output diversity by **1.6-2.1x** while simultaneously improving quality by **25.7%** in human evaluations, and recovers **66.8%** of the base model's original diversity.

---

## The Problem: Mode Collapse

### What is Mode Collapse?
After alignment training, LLMs become less diverse in their outputs. They:
- Repeat similar phrases and structures
- Favor typical, "safe" responses
- Lose creative variety
- Generate less realistic distributions of responses

### Why Does It Happen?
**Typicality Bias**: Human annotators in RLHF/preference data collection systematically prefer familiar, typical text over diverse alternatives. This bias gets baked into the aligned model.

### Why Does It Matter?
Mode collapse limits LLM effectiveness for:
- Creative writing (repetitive, boring outputs)
- Social simulation (unrealistic, homogeneous behaviors)
- Open-ended QA (narrow answer distributions)
- Synthetic data generation (less useful training data)

---

## The Solution: Verbalized Sampling

### Core Idea
Instead of asking for a single response, **explicitly ask the model to generate a probability distribution** over multiple responses.

### How It Works

**Traditional Prompt:**
```
Tell me a joke about coffee.
```
Result: Single, often typical response

**Verbalized Sampling Prompt:**
```xml
<instructions>
Generate 5 responses to the user query, each within a separate <response> tag.
Each <response> must include a <text> and a numeric <probability>.
Randomly sample responses from the full distribution.
</instructions>
Tell me a joke about coffee.
```
Result: 5 diverse responses with probabilities, much richer output

### Why This Works
1. **Explicit Distribution Request**: Counteracts the model's tendency toward single mode
2. **Probability Verbalization**: Forces the model to consider full range of possibilities
3. **Sampling Instruction**: Encourages exploration, not just the "best" response
4. **Training-Free**: No fine-tuning needed, works immediately

---

## Key Properties

### ✅ Advantages
- **Training-free**: Works via prompting alone
- **Model-agnostic**: Compatible with GPT, Claude, Gemini, Llama, etc.
- **Orthogonal to temperature**: Can combine with other sampling methods
- **Quality-preserving**: Doesn't hurt (and often improves) output quality
- **Safety-preserving**: Maintains alignment properties
- **Efficient**: Single API call gets multiple diverse responses

### 📊 Performance Gains

| Task | Diversity Improvement | Quality Impact |
|------|----------------------|----------------|
| Creative Writing | **1.6-2.1x** | **+25.7%** human eval score |
| Social Dialogue | **Substantially more realistic** | Maintained |
| Open-Ended QA | **Broader distribution** | Maintained |
| Synthetic Data | **More diverse data** | **Better downstream performance** |

---

## Prompting Techniques to Implement

Based on the paper, here are the key prompting techniques we will implement as slash commands:

### 1. **Core Verbalized Sampling**
**Technique**: Distribution elicitation with explicit probabilities

**Pattern**:
```xml
<instructions>
Generate N responses to the user query, each within a separate <response> tag.
Each <response> must include a <text> and a numeric <probability>.
Randomly sample responses from the full distribution.
</instructions>
[User's query]
```

**Use Cases**: General-purpose diversity enhancement

**Slash Command**: `/verbalized-sample` or `/vs`

---

### 2. **Creative Writing Mode**
**Technique**: Verbalized sampling optimized for creative tasks

**Pattern**:
```xml
<instructions>
Generate N creative responses to the following prompt.
Each response should explore different styles, tones, or approaches.
Provide each in a <response> tag with <text> and <probability>.
Prioritize originality and variety over typicality.
</instructions>
[User's creative prompt]
```

**Use Cases**: Stories, poems, jokes, creative content

**Slash Command**: `/creative-diverse` or `/creative`

---

### 3. **Multi-Perspective Analysis**
**Technique**: Generate diverse viewpoints on a topic

**Pattern**:
```xml
<instructions>
Generate N different perspectives on the following topic.
Each perspective should represent a distinct viewpoint or approach.
Provide each in a <response> tag with <text> and <probability>.
Ensure intellectual diversity across responses.
</instructions>
[User's topic/question]
```

**Use Cases**: Analysis, debate prep, understanding different angles

**Slash Command**: `/multi-perspective` or `/perspectives`

---

### 4. **Brainstorming Mode**
**Technique**: High-diversity idea generation

**Pattern**:
```xml
<instructions>
Generate N diverse ideas in response to the following challenge.
Each idea should be distinctly different from the others.
Provide each in a <response> tag with <text> and <probability>.
Think broadly and creatively - include unconventional ideas.
</instructions>
[User's challenge/problem]
```

**Use Cases**: Ideation, problem-solving, innovation

**Slash Command**: `/brainstorm` or `/ideas`

---

### 5. **Dialogue Simulation**
**Technique**: Generate diverse realistic responses for characters/personas

**Pattern**:
```xml
<instructions>
Generate N different ways [character/person] might respond to this situation.
Capture realistic behavioral variance - people don't always respond the same way.
Provide each in a <response> tag with <text> and <probability>.
Sample from the full range of realistic possibilities.
</instructions>
[User's dialogue scenario]
```

**Use Cases**: Writing dialogue, social simulation, character development

**Slash Command**: `/dialogue-sim` or `/dialogue`

---

### 6. **Weighted Sampling**
**Technique**: Sample from the verbalized distribution and return top choices

**Pattern**:
- First, generate verbalized distribution
- Parse probabilities
- Sample N responses based on weights
- Return sampled results

**Use Cases**: When you want probabilistic selection from diverse options

**Slash Command**: `/sample-weighted` or `/sample`

---

### 7. **Explanation Generation**
**Technique**: Multiple diverse explanations of a concept

**Pattern**:
```xml
<instructions>
Generate N different explanations of the following concept.
Each explanation should use a different approach (analogy, technical, simple, etc.).
Provide each in a <response> tag with <text> and <probability>.
Vary the level, style, and framing across explanations.
</instructions>
[User's concept to explain]
```

**Use Cases**: Teaching, learning, documentation

**Slash Command**: `/explain-diverse` or `/explain`

---

## Implementation Principles

Based on the paper's findings, our slash commands should follow these principles:

### 1. **Structured Output**
Use XML-style tags for parseability:
```xml
<response>
  <text>Content here</text>
  <probability>0.2</probability>
</response>
```

### 2. **Clear Instructions**
- Explicit instruction block
- State the number of responses (N)
- Request probability assignment
- Encourage "random sampling" language

### 3. **Sensible Defaults**
- Default N = 5 (good balance per paper)
- Allow user configuration
- Format output nicely for readability

### 4. **Task-Specific Variants**
Different tasks benefit from tailored prompting:
- Creative tasks: emphasize originality
- Analytical tasks: emphasize different perspectives
- Dialogue tasks: emphasize behavioral realism

### 5. **Post-Processing Options**
- Return full distribution
- Sample from distribution
- Display probabilities
- Format for different uses

---

## Technical Implementation Details

### Command Structure
Each slash command should:
1. Accept user input/query
2. Accept optional parameters (N, sampling mode, etc.)
3. Construct VS prompt with appropriate framing
4. Return formatted results

### Parameters to Support
- `--count N` or `-n N`: Number of responses (default: 5)
- `--sample`: Sample one response from distribution
- `--sample-n K`: Sample K responses from distribution
- `--raw`: Return raw model output
- `--format [json|markdown|plain]`: Output format

### Output Formats

**Markdown Format** (Default):
```markdown
## Response 1 (p=0.25)
[Text content]

## Response 2 (p=0.20)
[Text content]
...
```

**JSON Format**:
```json
{
  "responses": [
    {"text": "...", "probability": 0.25, "rank": 1},
    {"text": "...", "probability": 0.20, "rank": 2}
  ]
}
```

---

## Expected Impact

By implementing these slash commands, users will be able to:

1. **Break through mode collapse** - Get diverse outputs even from heavily aligned models
2. **Enhance creativity** - Generate more original and varied creative content
3. **Better brainstorming** - Access wider range of ideas and solutions
4. **Realistic simulation** - Create more authentic dialogue and scenarios
5. **Research & analysis** - Explore multiple perspectives systematically
6. **Data generation** - Create more diverse synthetic training data

All of this **without compromising** on:
- Factual accuracy
- Safety alignment
- Output quality
- Response coherence

---

## Conclusion

Verbalized Sampling represents a significant advance in prompt engineering. It's a simple technique with profound effects: **2-3x diversity improvement** while **maintaining or improving quality**.

The technique works because it leverages the model's understanding of probability distributions and explicitly counteracts the mode collapse induced by alignment training.

By implementing these prompting techniques as convenient slash commands, we make this powerful research immediately accessible to all Claude Code users.

---

## References

- Paper: https://arxiv.org/abs/2510.01171
- Website: https://www.verbalized-sampling.com/
- GitHub: https://github.com/CHATS-lab/verbalized-sampling
