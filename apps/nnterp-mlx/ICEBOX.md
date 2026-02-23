# Icebox

## Future enhancements

- [ ] Attention probability access (needs architecture-specific hooks into mlx-lm's SDPA)
- [ ] Display module with Plotly visualization (port of nnterp's display.py)
- [ ] Generation with interventions (patchscope_generate equivalent)
- [ ] KV cache support in traced forward pass for faster sequential generation
- [ ] Instruction-tuned repeat prompt variant (it_repeat_prompt)
- [ ] Batched patchscope lens for better throughput
- [ ] Activation patching between different models (cross-model patchscope)
- [ ] Support for MoE router logit access
- [ ] Gradient-based attribution methods (if MLX autograd supports this pattern)
- [ ] CLI tool for quick interpretability analysis
- [ ] Notebook examples with visualizations
- [ ] Integration tests against known nnterp outputs (numerical agreement)
- [ ] Benchmark: MLX vs PyTorch/NNsight speed comparison on Apple Silicon
