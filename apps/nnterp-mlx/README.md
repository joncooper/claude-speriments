# nnterp-mlx

A port of [nnterp](https://github.com/Butanium/nnterp) (mechanistic interpretability for transformers) to Apple's [MLX](https://github.com/ml-explore/mlx) framework using [mlx-lm](https://github.com/ml-explore/mlx-lm) for model loading.

**Status:** Initial Spike

## What is this?

nnterp provides a standardized interface for mechanistic interpretability of transformer models. The original library is built on [NNsight](https://nnsight.net/) + PyTorch/HuggingFace. This port brings the same capabilities to MLX, enabling interpretability research on Apple Silicon with fast inference.

### Key features

- **Model wrapper** (`MLXTransformer`) with standardized access to model internals
- **Activation capture** via custom layer-by-layer forward pass (no monkey-patching)
- **Logit lens** — project intermediate hidden states through the unembedding
- **Patchscope lens** — patch activations from one context into another
- **Activation steering** — add steering vectors at specified layers
- **Layer skipping** — skip computation of specified layers
- **Prompt utilities** — track target token probabilities across layers

## Requirements

- macOS with Apple Silicon (M1/M2/M3/M4)
- Python 3.10+
- MLX and mlx-lm

## Installation

```bash
cd apps/nnterp-mlx
pip install -e .

# With visualization support
pip install -e ".[display]"
```

## Quick start

```python
from nnterp_mlx import MLXTransformer, logit_lens, Prompt

# Load any mlx-lm compatible model
model = MLXTransformer("mlx-community/Llama-3.2-1B-Instruct-4bit")

# Logit lens: see what each layer predicts
probs = logit_lens(model, "The capital of France is")
# Shape: (1, num_layers, vocab_size)

# Track specific target probabilities
prompt = Prompt.from_strings(
    "The capital of France is",
    {"correct": "Paris", "incorrect": ["London", "Berlin"]},
    model.tokenizer,
)
target_probs = prompt.get_target_probs(probs)
# {"correct": mx.array(...), "incorrect": mx.array(...)}
```

## API overview

### MLXTransformer

The main wrapper class. Loads an mlx-lm model and provides standardized access:

```python
model = MLXTransformer("mlx-community/Llama-3.2-1B-Instruct-4bit")

# Standardized module access
model.embed_tokens    # Token embedding layer
model.layers          # List of TransformerBlock layers
model.layers[i].self_attn  # Attention module at layer i
model.layers[i].mlp        # MLP module at layer i
model.ln_final        # Final layer norm
model.lm_head         # Output projection (or None if tied)

# Model info
model.num_layers      # Number of transformer layers
model.hidden_size     # Hidden dimension size
model.vocab_size      # Vocabulary size
model.tokenizer       # The tokenizer
```

### Tracing activations

Use the `trace()` context manager to capture intermediate activations:

```python
with model.trace("Hello world", capture_layers=[0, 5, 10]) as result:
    pass

result.logits            # (batch, seq_len, vocab)
result.layers_output[5]  # (batch, seq_len, hidden)
result.token_embeddings  # (batch, seq_len, hidden)
result.next_token_probs  # (batch, vocab) - probabilities for last position
```

Capture sub-module outputs:

```python
with model.trace("Hello", capture_attn=True, capture_mlp=True) as result:
    pass

result.attn_output[5]  # Attention output at layer 5
result.mlp_output[5]   # MLP output at layer 5
```

### Interventions

Apply interventions during the forward pass:

```python
# Replace a layer's output
with model.trace(
    "Hello",
    interventions={"layers_output": {5: replacement_tensor}},
) as result:
    pass

# Activation steering
logits = model.steer(
    "Tell me about cats",
    layers=[10, 15],
    steering_vector=vector,
    factor=1.5,
)

# Layer skipping
logits = model.skip_layers("Hello", start_layer=4, end_layer=12)
```

### Logit lens

```python
from nnterp_mlx import logit_lens

# Get next-token probabilities at each layer
probs = logit_lens(model, "The capital of France is")
# Shape: (num_prompts, num_layers, vocab_size)

# Get raw logits instead
logits = logit_lens(model, "The capital of France is", return_logits=True)
```

### Patchscope lens

```python
from nnterp_mlx import patchscope_lens, repeat_prompt

probs = patchscope_lens(
    model,
    source_prompts=["The capital of France is"],
    target_patch_prompt=repeat_prompt(),
    layers=[0, 5, 10, 15],
)
# Shape: (num_sources, num_layers, vocab_size)
```

### Collecting activations

```python
from nnterp_mlx import collect_activations

acts = collect_activations(
    model,
    ["prompt 1", "prompt 2", "prompt 3"],
    layers=[0, 10, 20],
    idx=-1,  # Last token
)
# Shape: (num_layers, num_prompts, hidden_size)
```

### Prompt utilities

```python
from nnterp_mlx import Prompt, run_prompts

# Create prompts with target tokens
prompts = [
    Prompt.from_strings(
        "The capital of France is",
        {"correct": "Paris", "incorrect": "London"},
        model.tokenizer,
    ),
    Prompt.from_strings(
        "The capital of Germany is",
        {"correct": "Berlin", "incorrect": "London"},
        model.tokenizer,
    ),
]

# Run and get aggregated target probabilities
results = run_prompts(model, prompts, batch_size=32)
# {"correct": mx.array(...), "incorrect": mx.array(...)}
```

## How it works

### Architecture differences from nnterp

The original nnterp uses NNsight's proxy-based tracing system, which allows deferred execution — you set up operations on proxy objects, and they execute lazily during the forward pass. MLX doesn't have an equivalent mechanism.

Instead, nnterp-mlx implements a **custom forward pass** (`traced_forward`) that manually steps through the model's layers:

1. Embed tokens via `embed_tokens`
2. For each transformer layer:
   - Optionally capture the layer's input
   - Optionally replace the input (intervention)
   - Run the layer (or skip it)
   - Optionally capture attention/MLP sub-module outputs
   - Optionally replace/steer the output
   - Optionally capture the layer's output
3. Apply final layer norm
4. Project through lm_head

This approach:
- **No monkey-patching**: Doesn't modify any model class methods
- **Architecture-generic**: Works with any mlx-lm model that follows the standard structure (embed_tokens → layers → norm → lm_head)
- **Safe**: Original model is never modified; each trace is a clean forward pass

### Naming conventions

mlx-lm models already follow the LLaMA naming convention that nnterp standardizes to:

| nnterp name | mlx-lm name |
|---|---|
| `embed_tokens` | `model.model.embed_tokens` |
| `layers[i]` | `model.model.layers[i]` |
| `layers[i].self_attn` | `model.model.layers[i].self_attn` |
| `layers[i].mlp` | `model.model.layers[i].mlp` |
| `ln_final` | `model.model.norm` |
| `lm_head` | `model.lm_head` |

## Supported models

Any model supported by mlx-lm should work, including:
- Llama (1/2/3/3.1/3.2/3.3)
- Qwen (2/2.5/3)
- Gemma (1/2/3)
- Mistral / Mixtral
- Phi (3/4)
- DeepSeek
- And many more (100+ architectures)

## Credits

- [nnterp](https://github.com/Butanium/nnterp) by Clément Dumas — the original library this is ported from
- [MLX](https://github.com/ml-explore/mlx) by Apple — the ML framework
- [mlx-lm](https://github.com/ml-explore/mlx-lm) by Apple — language model support for MLX
