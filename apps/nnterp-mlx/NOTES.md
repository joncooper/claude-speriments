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

Research conducted March 2026 comparing nnterp-mlx against libraries across three ecosystems: MLX (mlux, mlx-lm-lens, mlxterp), PyTorch (TransformerLens, pyvene, baukit), and JAX (Penzai).

### Approaches to interpretability hooks

| Library | Framework | Approach | Trade-off |
|---|---|---|---|
| TransformerLens | PyTorch | Rewrite model from scratch with HookPoint modules | Full hook granularity (inside attention: Q, K, V, scores, pattern, Z). But requires reimplementing every architecture. |
| pyvene | PyTorch | Declarative intervention configs + PyTorch hooks | Composable, serializable, supports learned interventions (DAS). But requires per-architecture config mapping. |
| baukit | PyTorch | Minimal context manager wrapping (`TraceDict`) | Radically simple — works on any PyTorch model, 3-line usage. But no semantic awareness. |
| Penzai | JAX | Immutable pytree surgery — select nodes, apply transforms, get new model | No mutation, no cleanup bugs, composable. But JAX-only and the functional paradigm is unfamiliar. |
| mlux | MLX | Wrap existing modules in-place with HookWrapper | Works with any mlx-lm model, no rewrite. But can only hook at module boundaries, not inside attention. |
| mlxterp | MLX | Rewrite forward with HookPoints (TransformerLens-style) + monkey-patched `__call__` during trace | Fine-grained hooks (Q, K, V, scores, pattern), SAE support, tuned lens. Most feature-complete MLX library. |
| **nnterp-mlx** | MLX | Custom layer-by-layer forward pass | Explicit, safe, debuggable, works with any mlx-lm model. Less flexible than arbitrary hooks but covers the common cases. |

Our approach is closest to mlux's philosophy (work with existing models, no rewrite) but with a different mechanism (explicit forward vs. module wrapping). Both avoid TransformerLens's maintenance burden of reimplementing architectures.

### Key ideas worth adopting

**From TransformerLens:**
- **Semantic ActivationCache** — Methods like `decompose_resid()`, `accumulated_resid()`, `direct_logit_attribution()` that encode knowledge of transformer architecture into the cache itself. This is what makes TransformerLens productive — the cache *understands* what it contains.
- **FactoredMatrix** — Represents `W_O @ W_V` (OV circuits) and `W_Q^T @ W_K` (QK circuits) without materializing the full product. Efficient SVD on the smaller factor. Especially valuable on memory-constrained Apple Silicon.
- **Stacked weight properties** — `model.W_Q` returning all layers stacked. Enables vectorized analysis across all layers/heads without loops.
- **`test_prompt()`** — One-liner for "does the model predict X?" Essential for interactive exploration.
- **Weight processing at load time** — `fold_ln`, `center_unembed` etc. that simplify the math researchers need to reason about.

**From pyvene (Stanford NLP):**
- **Declarative intervention configs** — `RepresentationConfig(layer=5, component="block_output", intervention_type=VanillaIntervention)` instead of writing hook functions. Composable, serializable, reproducible. Could be an alternative to our dict-based intervention system.
- **Learned interventions (DAS/Boundless DAS)** — Train a rotation matrix to find the causal subspace for a concept. MLX has `mx.grad` so this is feasible. Major differentiator if implemented.
- **Semantic component names** — `"block_output"`, `"mlp_output"`, `"attention_weight"` instead of full module paths. Architecture-portable.
- **Multi-source interventions** — Intervene from multiple sources simultaneously. Our current system is single-source.
- **Parallel vs serial mode** — Control whether interventions see original base or results of prior interventions.

**From baukit (David Bau):**
- **Radical simplicity** — The entire API is `TraceDict(model, layers)` as a context manager + `td['layer'].output`. Demonstrates that the simplest API wins for research use.
- **`edit_output` parameter** — Unifies capture and intervention in a single context manager. No separate "cache then hook" workflow.
- **`runningstats` module** — Streaming mean, covariance, and quantile computation for activations across datasets. Essential for production interpretability (not just single-prompt analysis).
- **`get_module()` / `replace_module()`** — Simple standalone utilities (~10 lines each) for navigating/modifying model trees by string path. Useful independent of any hook system.
- **`stop=True` for early exit** — Stop forward pass after capturing a specific layer. Maps naturally to our custom forward (just stop the loop early).

**From Penzai:**
- **Named dimensions** — `activation.untag("batch", "heads", "seq")` instead of remembering index positions. Prevents a whole class of bugs.
- **Visualization as first-class** — Treescope renders models as interactive trees in notebooks. Even a simple `model.show()` would improve our DX.
- **Immutability principle** — Our context manager approach already gets most of this benefit (no leaked state after `trace()`), but worth keeping in mind.

**From mlux:**
- **Flask-based interactive explorers** — Browser UIs for logit lens, attention patterns, steering. Nice for exploration but not our priority.
- **`suggest_alpha()`** — Heuristic for steering vector intensity. Small but useful.

**From mlxterp (coairesearch):**
- **Inside-attention hooks on MLX** — Demonstrates that fine-grained Q/K/V/scores/pattern hooks are achievable without full TransformerLens-style reimplementation. Uses temporary `__call__` monkey-patching during trace context.
- **SAE training pipeline** — TopK + BatchTopK SAEs with streaming `ActivationDataLoader`, ghost gradients, dead neuron resurrection, LR scheduling, W&B integration, Neuronpedia-style visualization. The most complete SAE implementation on MLX.
- **Tuned lens** — Learned per-layer affine transforms (Belrose et al., 2023) for better intermediate predictions than raw logit lens. Includes training and inference.
- **`InterventionComposer`** — Fluent builder for chaining: `InterventionComposer().add(scale(0.5)).add(noise(0.1)).add(clamp(-1, 1)).build()`.
- **Smart sequence alignment** — `replace_with(value, align="end")` for patching between different-length sequences. Thoughtful default for causal LMs.
- **`ModuleResolver` with fallback chains** — Tries 9 paths for embeddings, 7 for norms, 5 for lm_heads. Architecture-agnostic without configuration.

### What we do better than alternatives

- **Patchscope lens** — None of the other libraries (TransformerLens, mlux, mlxterp, mlx-lm-lens, pyvene, baukit) have this built in.
- **`Prompt` class with named targets** — Systematic experiment design with target token categories and collision checking. Unique to nnterp/nnterp-mlx.
- **No architecture-specific code** — Works with 100+ mlx-lm models via standardized structure. No per-model conversion layer (cf. mlxterp's architecture-specific code, pyvene's per-model configs).
- **Context manager cleanup** — No hook leak risk (TransformerLens) or manual unwrap (mlux). mlxterp also does this well.
- **Layer skipping** — First-class `skip_layers()` method. Trivial in our custom forward, requires custom hooks in others.
- **Explicit forward pass** — More debuggable than monkey-patching (mlxterp) or module wrapping (mlux). The full computation is visible in one function.

### MLX interp ecosystem (as of March 2026)

| Library | Stars | Approach | Unique strength |
|---|---|---|---|
| **mlux** (batson/mlux) | ~48 | Module wrapping | Flask UIs, contrastive steering |
| **mlxterp** (coairesearch/mlxterp) | ~5 | HookPoint rewrite + `__call__` patching | SAEs, tuned lens, inside-attention hooks |
| **mlx-lm-lens** (Goekdeniz-Guelmez) | ~40 | Lightweight wrapper | pip-installable, simple inspection |
| **nnterp-mlx** (this project) | — | Custom forward pass | Patchscope, Prompt class, layer skipping |

Notable PyTorch libraries with portable ideas:
- **pyvene** (stanfordnlp) — ~600 stars, NeurIPS 2024. Declarative interventions + learned interventions (DAS).
- **baukit** (davidbau) — ~120 stars. Radical simplicity + streaming statistics.
- **TransformerLens** — ~2k+ stars. Semantic cache, FactoredMatrix, weight processing.

No standalone "sae-for-mlx" library exists (elyase/sae-for-mlx appears to have been removed). SAE support on MLX comes from mlxterp's built-in module. No MLX library yet has learned interventions (DAS), circuit discovery, or visualization comparable to CircuitsVis.
