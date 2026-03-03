# Icebox

## Semantic cache & analysis (inspired by TransformerLens ActivationCache)

- [ ] `TraceResult.decompose_resid(layer)` — per-component (embed, each attn head, each MLP) contributions to residual stream
- [ ] `TraceResult.accumulated_resid(layer)` — cumulative residual stream state at each layer
- [ ] `TraceResult.stack_head_results(layer)` — stack all attention head outputs for per-head analysis
- [ ] `TraceResult.direct_logit_attribution(token)` — which components push toward a specific token prediction
- [ ] `TraceResult.apply_ln_to_stack(stack, layer)` — apply cached layer norm scaling to a decomposed residual stack
- [ ] `pos_slice` parameter in `trace()` — capture only specific token positions to save memory (e.g., `pos_slice=-1` for last token only)

## Weight-level analysis (inspired by TransformerLens FactoredMatrix)

- [ ] `FactoredMatrix` class — represent weight products (OV circuits: `W_O @ W_V`, QK circuits: `W_Q^T @ W_K`) without materializing full matrices; support efficient SVD, eigendecomposition, and Frobenius norm
- [ ] Stacked weight access properties — `model.W_Q`, `model.W_K`, `model.W_V`, `model.W_O` returning all layers stacked into a single array for vectorized operations
- [ ] `model.OV` / `model.QK` — composed circuit matrices as FactoredMatrix objects
- [ ] Composition scores — measure subspace alignment between heads (`utils.composition_scores(left, right)`) for circuit discovery
- [ ] `fold_layer_norm()` utility — optionally fold LN weights into adjacent linear layers so the residual stream becomes a true linear sum of component contributions (simplifies direct logit attribution)

## Interactive utilities

- [ ] `test_prompt(model, prompt, answer)` — one-liner: "does the model predict X?" Shows rank, probability, and top-k alternatives
- [ ] CLI tool for quick interpretability analysis
- [ ] Notebook examples with visualizations

## Visualization (inspired by Penzai Treescope & CircuitsVis)

- [ ] `model.show()` — print module tree with shapes, dtypes, and quantization info
- [ ] Display module with Plotly visualization (port of nnterp's display.py)
- [ ] CircuitsVis integration — React-based attention pattern and logit lens heatmap visualization in notebooks
- [ ] Named dimension wrapper for `mx.array` — lightweight `.tag("batch", "heads", "seq", "hidden")` / `.untag("heads")` for self-documenting tensor operations (inspired by Penzai NamedArray)

## Generation & caching

- [ ] Generation with interventions (patchscope_generate equivalent)
- [ ] KV cache support in traced forward pass for faster sequential generation

## Patchscope extensions

- [ ] Instruction-tuned repeat prompt variant (it_repeat_prompt)
- [ ] Batched patchscope lens for better throughput
- [ ] Activation patching between different models (cross-model patchscope)

## Architecture-specific features

- [ ] Attention probability access (needs architecture-specific hooks into mlx-lm's SDPA)
- [ ] Support for MoE router logit access

## Advanced techniques

- [ ] Gradient-based attribution methods (if MLX autograd supports this pattern)
- [ ] SAE (Sparse Autoencoder) integration — interop with sae-for-mlx for encoding/decoding activations through trained SAEs
- [ ] Declarative intervention configs (inspired by pyvene) — `InterventionConfig(layer=5, component="mlp", type="addition")` as a more composable alternative to the current dict-based system

## Testing & benchmarks

- [ ] Integration tests against known nnterp outputs (numerical agreement)
- [ ] Benchmark: MLX vs PyTorch/NNsight speed comparison on Apple Silicon
