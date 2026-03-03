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

## Intervention system v2 (inspired by pyvene & baukit)

- [ ] Declarative intervention configs (inspired by pyvene) — `InterventionConfig(layer=5, component="mlp_output", type=VanillaIntervention)` as a composable, serializable alternative to the current dict-based system
- [ ] Semantic component names — `"block_output"`, `"mlp_output"`, `"attention_output"` instead of raw layer indices, portable across architectures
- [ ] Multi-source interventions — patch from multiple source prompts simultaneously into different layers/positions
- [ ] Parallel vs serial intervention modes — control whether interventions see original base or results of prior interventions
- [ ] `InterventionComposer` — fluent builder for chaining interventions: `.add(scale(0.5)).add(noise(0.1)).add(clamp(-1, 1)).build()` (inspired by mlxterp)
- [ ] Built-in intervention functions — `zero_out()`, `scale(factor)`, `add_vector(vec)`, `replace_with(value, align="end")`, `noise(std)`, `clamp(min, max)` as composable callables
- [ ] `stop_at_layer` parameter in `trace()` — early exit for partial forward passes (saves compute when only intermediate activations are needed; inspired by baukit's `stop=True`)
- [ ] Unified capture + intervene — allow `trace()` to both capture activations and apply interventions in a single pass (inspired by baukit's `edit_output`)

## Learned interventions (inspired by pyvene DAS)

- [ ] `RotatedSpaceIntervention` — learn a rotation matrix to find the causal subspace for a concept (Distributed Alignment Search, Geiger et al. 2023). MLX has `mx.grad` so this is feasible.
- [ ] `BoundlessRotatedSpaceIntervention` — learn rotation + per-dimension sigmoid masks (no fixed k), automatically discovers subspace dimensionality
- [ ] Intervention serialization — save/load learned intervention parameters alongside configs for reproducibility

## SAE (Sparse Autoencoders)

- [ ] TopK SAE class — encoder, topk activation, decoder, optional tied weights (~100 lines)
- [ ] SAELens weight loader — convert pre-trained SAELens-format SAEs (PyTorch) to MLX for immediate use with cached activations
- [ ] Streaming `ActivationDataLoader` — iterate over dataset, trace model, extract layer activations, buffer and yield batches for SAE training
- [ ] SAE training loop — ghost gradients, dead neuron resurrection, LR warmup + cosine decay, checkpointing
- [ ] Feature analysis — `get_top_features_for_text()`, `get_top_texts_for_feature()`, Neuronpedia-style colored token visualization
- [ ] Tuned lens (Belrose et al. 2023) — learned per-layer affine transforms for better intermediate predictions than raw logit lens

## Dataset-level analysis (inspired by baukit runningstats)

- [ ] Streaming statistics — `RunningMean`, `RunningCovariance`, `RunningQuantile` for computing activation distributions across a dataset without holding everything in memory
- [ ] `collect_activations` integration — pipe batched activations from `collect_activations()` into streaming stats
- [ ] PCA directions from activation covariance — identify principal directions of variation at each layer

## Advanced techniques

- [ ] Gradient-based attribution methods (if MLX autograd supports this pattern)

## Testing & benchmarks

- [ ] Integration tests against known nnterp outputs (numerical agreement)
- [ ] Benchmark: MLX vs PyTorch/NNsight speed comparison on Apple Silicon
