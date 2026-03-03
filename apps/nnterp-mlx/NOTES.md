# Implementation Notes

## Key design decisions

### Custom forward pass vs monkey-patching

The original nnterp uses NNsight, which provides a proxy-based tracing system. Proxy objects record operations during setup, then replay them during the actual forward pass. MLX has no equivalent.

Two approaches were considered:
1. **Monkey-patching** the model's `__call__` methods to inject hooks
2. **Custom forward pass** that manually steps through the model

We chose approach 2 because:
- Monkey-patching class methods affects all instances (dangerous with multiple models)
- Instance-level patching is fragile with MLX modules
- Custom forward is explicit, safe, and debuggable
- All mlx-lm models follow the same structure, making a generic forward pass feasible

### No NNsight dependency

nnterp's power comes from NNsight's tracing system. For MLX, we provide equivalent functionality through a simpler, more explicit API. The trade-off is less flexible (no arbitrary proxy operations), but the common use cases (logit lens, patchscope, steering, activation capture) are all supported.

### MLX array operations

MLX arrays don't support in-place operations the same way as PyTorch tensors. For operations like "replace activations at position X", we use concatenation-based slice replacement rather than index assignment.

### Mask creation

Different mlx-lm model architectures handle attention masks slightly differently (e.g., sliding window attention in Llama 3.2). The traced forward pass handles this by checking for `use_sliding` on each layer and creating appropriate masks.

## Differences from nnterp

| Feature | nnterp | nnterp-mlx |
|---|---|---|
| Framework | PyTorch + NNsight | MLX + mlx-lm |
| Tracing | Proxy-based (deferred execution) | Custom forward pass |
| Context manager | `model.trace()` yields proxy accessors | `model.trace()` yields TraceResult |
| Activation access | `model.layers_output[5]` (proxy) | `result.layers_output[5]` (mx.array) |
| Module renaming | Needed (diverse HF architectures) | Not needed (mlx-lm already standardized) |
| Validation | Automatic renaming checks | Not needed |
| Remote execution | NDIF support | Not applicable |

## What's NOT ported

- `display.py` — Plotly visualization (could be added but low priority)
- `RenameConfig` — Not needed since mlx-lm already uses standardized names
- `AttentionProbabilitiesAccessor` — Would need architecture-specific hooks into mlx-lm's SDPA
- Remote execution (NDIF) — Not applicable to MLX
- Batched session-based activation collection — MLX doesn't have NNsight sessions

## Landscape & design influences

Research conducted March 2026 comparing nnterp-mlx against TransformerLens (PyTorch), Penzai (JAX), mlux (MLX), and mlx-lm-lens (MLX).

### Three approaches to interpretability hooks

| Library | Approach | Trade-off |
|---|---|---|
| TransformerLens | Rewrite model from scratch with HookPoint modules at every intermediate step | Full hook granularity (inside attention: Q, K, V, scores, pattern, Z). But requires reimplementing every architecture. |
| Penzai | Immutable pytree surgery — select nodes, apply transforms, get new model | No mutation, no cleanup bugs, composable. But JAX-only and the functional paradigm is unfamiliar. |
| mlux | Wrap existing modules in-place with HookWrapper | Works with any mlx-lm model, no rewrite. But can only hook at module boundaries, not inside attention. |
| **nnterp-mlx** | Custom layer-by-layer forward pass | Explicit, safe, debuggable, works with any mlx-lm model. Less flexible than arbitrary hooks but covers the common cases. |

Our approach is closest to mlux's philosophy (work with existing models, no rewrite) but with a different mechanism (explicit forward vs. module wrapping). Both avoid TransformerLens's maintenance burden of reimplementing architectures.

### Key ideas worth adopting

**From TransformerLens:**
- **Semantic ActivationCache** — Methods like `decompose_resid()`, `accumulated_resid()`, `direct_logit_attribution()` that encode knowledge of transformer architecture into the cache itself. This is what makes TransformerLens productive — the cache *understands* what it contains.
- **FactoredMatrix** — Represents `W_O @ W_V` (OV circuits) and `W_Q^T @ W_K` (QK circuits) without materializing the full product. Efficient SVD on the smaller factor. Especially valuable on memory-constrained Apple Silicon.
- **Stacked weight properties** — `model.W_Q` returning all layers stacked. Enables vectorized analysis across all layers/heads without loops.
- **`test_prompt()`** — One-liner for "does the model predict X?" Essential for interactive exploration.
- **Weight processing at load time** — `fold_ln`, `center_unembed` etc. that simplify the math researchers need to reason about.

**From Penzai:**
- **Named dimensions** — `activation.untag("batch", "heads", "seq")` instead of remembering index positions. Prevents a whole class of bugs.
- **Visualization as first-class** — Treescope renders models as interactive trees in notebooks. Even a simple `model.show()` would improve our DX.
- **Immutability principle** — Our context manager approach already gets most of this benefit (no leaked state after `trace()`), but worth keeping in mind.

**From mlux:**
- **Flask-based interactive explorers** — Browser UIs for logit lens, attention patterns, steering. Nice for exploration but not our priority.
- **`suggest_alpha()`** — Heuristic for steering vector intensity. Small but useful.

### What we do better than alternatives

- **Patchscope lens** — Neither TransformerLens, mlux, nor mlx-lm-lens has this built in.
- **`Prompt` class with named targets** — Systematic experiment design with target token categories.
- **No architecture-specific code** — Works with 100+ mlx-lm models via standardized structure.
- **Context manager cleanup** — No hook leak risk (TransformerLens) or manual unwrap (mlux).
- **Layer skipping** — First-class `skip_layers()` method.

### MLX interp ecosystem (as of March 2026)

Only three libraries exist:
1. **mlux** (batson/mlux) — 48 stars, module wrapping, Flask UIs, v0.2.0
2. **mlx-lm-lens** (Goekdeniz-Guelmez) — 40 stars, lightweight inspection, pip-installable, v0.0.1
3. **nnterp-mlx** (this project) — custom forward, patchscope, structured experiments, v0.1.0

The space is very young. No MLX library yet has SAE support, circuit discovery, or notebook visualization comparable to the PyTorch ecosystem.
