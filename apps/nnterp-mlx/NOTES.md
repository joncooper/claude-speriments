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
