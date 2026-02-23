"""
Activation capture and intervention for MLX transformer models.

MLX doesn't have PyTorch-style forward hooks or NNsight's proxy system.
Instead, we implement a custom forward pass that manually steps through
the model's layers, capturing activations and applying interventions
at each step. This avoids monkey-patching and works generically with
any mlx-lm model architecture.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

import mlx.core as mx

if TYPE_CHECKING:
    from .model import MLXTransformer


@dataclass
class TraceResult:
    """
    Result of a traced forward pass, containing captured activations and logits.

    Attributes:
        logits: Model output logits, shape (batch, seq_len, vocab_size).
        layers_output: Dict mapping layer index -> output tensor (batch, seq_len, hidden).
        layers_input: Dict mapping layer index -> input tensor (batch, seq_len, hidden).
        attn_output: Dict mapping layer index -> attention output tensor.
        mlp_output: Dict mapping layer index -> MLP output tensor.
        input_ids: The input token IDs used for this trace.
        token_embeddings: The token embeddings (output of embed_tokens).
    """

    logits: mx.array
    layers_output: dict[int, mx.array] = field(default_factory=dict)
    layers_input: dict[int, mx.array] = field(default_factory=dict)
    attn_output: dict[int, mx.array] = field(default_factory=dict)
    mlp_output: dict[int, mx.array] = field(default_factory=dict)
    input_ids: mx.array | None = None
    token_embeddings: mx.array | None = None

    @property
    def next_token_probs(self) -> mx.array:
        """Probabilities for the next token (last position)."""
        return mx.softmax(self.logits[:, -1, :], axis=-1)


def _create_mask(h: mx.array, cache=None, window_size: int | None = None):
    """Create an attention mask suitable for the given inputs."""
    from mlx_lm.models.base import create_attention_mask

    return create_attention_mask(h, cache, window_size=window_size)


def _run_block_with_capture(
    block,
    x: mx.array,
    mask,
    cache,
    capture_attn: bool = False,
    capture_mlp: bool = False,
) -> tuple[mx.array, mx.array | None, mx.array | None]:
    """
    Run a TransformerBlock manually to capture sub-module outputs.

    Most mlx-lm TransformerBlocks follow this pattern:
        r = self.self_attn(self.input_layernorm(x), mask, cache)
        h = x + r
        r = self.mlp(self.post_attention_layernorm(h))
        out = h + r

    Args:
        block: A TransformerBlock instance.
        x: Input hidden states.
        mask: Attention mask.
        cache: KV cache for this layer.
        capture_attn: Whether to return the attention output.
        capture_mlp: Whether to return the MLP output.

    Returns:
        (output, attn_out_or_none, mlp_out_or_none)
    """
    if not (capture_attn or capture_mlp):
        # Fast path: just call normally
        return block(x, mask, cache=cache), None, None

    # Manual forward to capture sub-outputs
    attn_out = None
    mlp_out = None

    # Attention
    normed = block.input_layernorm(x)
    r = block.self_attn(normed, mask, cache)
    if capture_attn:
        attn_out = r
    h = x + r

    # MLP
    normed = block.post_attention_layernorm(h)
    r = block.mlp(normed)
    if capture_mlp:
        mlp_out = r
    out = h + r

    return out, attn_out, mlp_out


def traced_forward(
    wrapper: MLXTransformer,
    input_ids: mx.array,
    capture_layers: set[int] | None = None,
    capture_input: bool = False,
    capture_attn: bool = False,
    capture_mlp: bool = False,
    interventions: dict[str, Any] | None = None,
) -> TraceResult:
    """
    Run a forward pass through the model, capturing activations and
    applying interventions layer by layer.

    This implements the standard transformer forward pass:
        h = embed_tokens(input_ids)
        for each layer:
            h = layer(h, mask, cache)
        h = norm(h)
        logits = lm_head(h)

    But with hooks at each layer for capturing and modifying activations.

    Args:
        wrapper: The MLXTransformer instance.
        input_ids: Token IDs, shape (batch, seq_len).
        capture_layers: Set of layer indices to capture. None = all layers.
        capture_input: Also capture layer inputs.
        capture_attn: Capture attention sub-module outputs.
        capture_mlp: Capture MLP sub-module outputs.
        interventions: Dict of intervention specs:
            - "layers_output": {layer_idx: replacement_tensor}
            - "layers_input": {layer_idx: replacement_tensor}
            - "steer": {layer_idx: (steering_vector, positions_or_none)}
            - "skip": {"start": int, "end": int, "value": tensor_or_none}

    Returns:
        TraceResult with captured activations and logits.
    """
    if capture_layers is None:
        capture_layers = set(range(wrapper.num_layers))
    elif not isinstance(capture_layers, set):
        capture_layers = set(capture_layers)

    if interventions is None:
        interventions = {}

    output_replacements = interventions.get("layers_output", {})
    input_replacements = interventions.get("layers_input", {})
    steer_config = interventions.get("steer", {})
    skip_config = interventions.get("skip", None)

    # Step 1: Embed tokens
    h = wrapper.embed_tokens(input_ids)
    token_embeddings = h

    # Step 2: Create attention mask
    mask = _create_mask(h)

    # Prepare result accumulators
    layers_output = {}
    layers_input = {}
    attn_output = {}
    mlp_output = {}

    # Determine skip range
    skip_start = skip_end = -1
    skip_value = None
    if skip_config is not None:
        skip_start = skip_config["start"]
        skip_end = skip_config["end"]
        skip_value = skip_config.get("value", None)

    # Step 3: Layer-by-layer forward
    layers = wrapper.layers
    for layer_idx, layer in enumerate(layers):
        # Capture input
        if capture_input and layer_idx in capture_layers:
            layers_input[layer_idx] = h

        # Apply input replacement
        if layer_idx in input_replacements:
            h = input_replacements[layer_idx]

        # Handle layer skipping
        if skip_start <= layer_idx <= skip_end:
            if layer_idx == skip_start and skip_value is not None:
                h = skip_value
            # Skip computation, just capture and continue
            if layer_idx in capture_layers:
                layers_output[layer_idx] = h
            continue

        # Handle per-layer mask (e.g. sliding window)
        layer_mask = mask
        if hasattr(layer, "use_sliding") and layer.use_sliding:
            sliding_window = getattr(wrapper.inner_model, "sliding_window", None)
            if sliding_window is not None:
                layer_mask = _create_mask(h, window_size=sliding_window)

        # Run the layer
        h, attn_out, mlp_out = _run_block_with_capture(
            layer,
            h,
            layer_mask,
            cache=None,
            capture_attn=capture_attn and layer_idx in capture_layers,
            capture_mlp=capture_mlp and layer_idx in capture_layers,
        )

        if attn_out is not None:
            attn_output[layer_idx] = attn_out
        if mlp_out is not None:
            mlp_output[layer_idx] = mlp_out

        # Apply output replacement
        if layer_idx in output_replacements:
            h = output_replacements[layer_idx]

        # Apply steering
        if layer_idx in steer_config:
            steer_vec, positions = steer_config[layer_idx]
            if positions is None:
                h = h + steer_vec
            else:
                if isinstance(positions, int):
                    positions = [positions]
                for pos in positions:
                    # Slice update: h[:, pos, :] += steer_vec
                    update = mx.zeros_like(h)
                    # Broadcast steer_vec to match batch dimension
                    sv = mx.broadcast_to(steer_vec, h[:, pos:pos+1, :].shape)
                    h = mx.concatenate([
                        h[:, :pos, :],
                        h[:, pos:pos+1, :] + sv,
                        h[:, pos+1:, :],
                    ], axis=1)

        # Capture output
        if layer_idx in capture_layers:
            layers_output[layer_idx] = h

    # Step 4: Final layer norm
    h = wrapper.ln_final(h)

    # Step 5: LM head
    if wrapper.lm_head is not None:
        logits = wrapper.lm_head(h)
    else:
        logits = wrapper.embed_tokens.as_linear(h)

    return TraceResult(
        logits=logits,
        layers_output=layers_output,
        layers_input=layers_input,
        attn_output=attn_output,
        mlp_output=mlp_output,
        input_ids=input_ids,
        token_embeddings=token_embeddings,
    )


