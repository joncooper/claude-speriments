"""
Mechanistic interpretability interventions for MLX transformer models.

Port of nnterp's interventions module, adapted to work with MLX arrays
and the MLXTransformer wrapper instead of NNsight proxies.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

import mlx.core as mx

from .hooks import traced_forward

if TYPE_CHECKING:
    from .model import MLXTransformer


def collect_activations(
    model: MLXTransformer,
    prompts: str | list[str],
    layers: list[int] | None = None,
    idx: int = -1,
    batch_size: int | None = None,
) -> mx.array:
    """
    Collect hidden state activations at a specific token position across layers.

    Args:
        model: The MLXTransformer model.
        prompts: Single prompt or list of prompts.
        layers: Which layers to collect from. None = all layers.
        idx: Token position index. -1 = last token (default).
        batch_size: If provided, process prompts in batches to manage memory.

    Returns:
        Activations of shape (num_layers, num_prompts, hidden_size).
    """
    if isinstance(prompts, str):
        prompts = [prompts]

    if layers is None:
        layers = list(range(model.num_layers))

    capture_set = set(layers)

    if batch_size is not None and len(prompts) > batch_size:
        # Process in batches
        all_acts = []
        for i in range(0, len(prompts), batch_size):
            batch = prompts[i : i + batch_size]
            batch_acts = collect_activations(model, batch, layers, idx)
            all_acts.append(batch_acts)
        return mx.concatenate(all_acts, axis=1)

    encoded = model.tokenize(prompts)
    input_ids = encoded["input_ids"]

    result = traced_forward(
        wrapper=model,
        input_ids=input_ids,
        capture_layers=capture_set,
    )
    mx.eval(result.logits, *result.layers_output.values())

    # Stack layer outputs and extract token at idx
    acts = []
    for layer in layers:
        layer_out = result.layers_output[layer]  # (batch, seq_len, hidden)
        acts.append(layer_out[:, idx, :])  # (batch, hidden)

    return mx.stack(acts)  # (num_layers, batch, hidden)


def logit_lens(
    model: MLXTransformer,
    prompts: str | list[str],
    layers: list[int] | None = None,
    return_logits: bool = False,
) -> mx.array:
    """
    Apply the logit lens: project each layer's hidden states through the
    unembedding (ln_final + lm_head) to see intermediate predictions.

    Args:
        model: The MLXTransformer model.
        prompts: Single prompt or list of prompts.
        layers: Which layers to analyze. None = all layers.
        return_logits: If True, return raw logits instead of probabilities.

    Returns:
        If return_logits is False:
            Probabilities of shape (num_prompts, num_layers, vocab_size).
        If return_logits is True:
            Logits of shape (num_prompts, num_layers, vocab_size).
    """
    if isinstance(prompts, str):
        prompts = [prompts]

    if layers is None:
        layers = list(range(model.num_layers))

    # Collect last-token activations at each layer
    # Shape: (num_layers, num_prompts, hidden_size)
    activations = collect_activations(model, prompts, layers, idx=-1)
    mx.eval(activations)

    # Project each layer's activations through the unembedding
    probs_per_layer = []
    for layer_idx in range(len(layers)):
        hidden = activations[layer_idx]  # (num_prompts, hidden)
        logits = model.project_on_vocab(hidden)  # (num_prompts, vocab)
        if return_logits:
            probs_per_layer.append(logits)
        else:
            probs_per_layer.append(mx.softmax(logits, axis=-1))

    # Stack: (num_layers, num_prompts, vocab) -> transpose to (num_prompts, num_layers, vocab)
    result = mx.stack(probs_per_layer)
    result = mx.transpose(result, axes=[1, 0, 2])
    mx.eval(result)
    return result


@dataclass
class TargetPrompt:
    """A prompt with a specified token position for patching."""

    prompt: str
    index_to_patch: int


def repeat_prompt(
    words: list[str] | None = None,
    rel: str = " ",
    sep: str = "\n",
    placeholder: str = "?",
    index_to_patch: int = -1,
) -> TargetPrompt:
    """
    Create a repeat-prompt for patchscope, following the patchscopes paper.

    This creates a prompt like:
        king king
        1135 1135
        hello hello
        ?

    The model is expected to predict the repeated word at the placeholder position.

    Args:
        words: Words to repeat. Default: ["king", "1135", "hello"].
        rel: String between repeated words (default: " ").
        sep: Separator between lines (default: newline).
        placeholder: Placeholder string (default: "?").
        index_to_patch: Token position to patch (default: -1, last token).

    Returns:
        A TargetPrompt with the constructed prompt and patch index.
    """
    if words is None:
        words = ["king", "1135", "hello"]
    prompt = sep.join([w + rel + w for w in words]) + sep + placeholder
    return TargetPrompt(prompt, index_to_patch)


@dataclass
class TargetPromptBatch:
    """A batch of target prompts with potentially different patch indices."""

    prompts: list[str]
    index_to_patch: list[int]

    @classmethod
    def from_target_prompts(cls, prompts: list[TargetPrompt]):
        return cls(
            prompts=[p.prompt for p in prompts],
            index_to_patch=[p.index_to_patch for p in prompts],
        )

    @classmethod
    def from_target_prompt(cls, prompt: TargetPrompt, batch_size: int):
        return cls(
            prompts=[prompt.prompt] * batch_size,
            index_to_patch=[prompt.index_to_patch] * batch_size,
        )

    def __len__(self):
        return len(self.prompts)


def patchscope_lens(
    model: MLXTransformer,
    source_prompts: list[str] | str,
    target_patch_prompt: TargetPrompt | None = None,
    layers: list[int] | None = None,
    latents: mx.array | None = None,
) -> mx.array:
    """
    Apply the patchscope lens: replace hidden states in a target prompt
    with activations from source prompts at each layer, and observe
    the resulting predictions.

    For each layer, the hidden state of the source prompt's last token
    is patched into the target prompt at the specified position, and we
    measure what the model predicts.

    Args:
        model: The MLXTransformer model.
        source_prompts: Prompts to get source activations from.
        target_patch_prompt: Target prompt with patch position.
            Default: repeat_prompt().
        layers: Layers to intervene at. None = all layers.
        latents: Pre-computed activations of shape (num_layers, num_sources, hidden).
            If provided, source_prompts is ignored.

    Returns:
        Probabilities of shape (num_sources, num_layers, vocab_size).
    """
    if target_patch_prompt is None:
        target_patch_prompt = repeat_prompt()

    if isinstance(source_prompts, str):
        source_prompts = [source_prompts]

    if layers is None:
        layers = list(range(model.num_layers))

    # Get source activations if not pre-computed
    if latents is None:
        latents = collect_activations(model, source_prompts, layers, idx=-1)
        mx.eval(latents)

    num_sources = latents.shape[1]

    # Create target batch
    target_batch = TargetPromptBatch.from_target_prompt(
        target_patch_prompt, num_sources
    )

    probs_per_layer = []
    for layer_list_idx, layer in enumerate(layers):
        # Tokenize target prompts
        encoded = model.tokenize(target_batch.prompts)
        target_ids = encoded["input_ids"]

        # Build intervention: replace the hidden state at the patch position
        # in the specified layer with the source activation
        layer_latents = latents[layer_list_idx]  # (num_sources, hidden)

        # We need to create a replacement tensor for the full layer output.
        # Strategy: run traced forward, but intercept at the target layer
        # to replace the activation at the patch position.

        # First, run a clean forward to get the baseline layer output shape
        result = traced_forward(
            wrapper=model,
            input_ids=target_ids,
            capture_layers={layer},
            capture_input=True,
        )
        mx.eval(result.logits, *result.layers_output.values())

        # Now get the layer output and patch it
        layer_output = result.layers_output[layer]  # (batch, seq, hidden)
        patch_idx = target_patch_prompt.index_to_patch

        # Create patched output
        patched = layer_output
        # Replace activation at patch position with source latents
        # patched[:, patch_idx, :] = layer_latents
        if patch_idx == -1:
            seq_len = patched.shape[1]
            patched = mx.concatenate([
                patched[:, :seq_len - 1, :],
                layer_latents[:, None, :],
            ], axis=1)
        else:
            patched = mx.concatenate([
                patched[:, :patch_idx, :],
                layer_latents[:, None, :],
                patched[:, patch_idx + 1:, :],
            ], axis=1)

        # Run forward with the patched layer output
        result2 = traced_forward(
            wrapper=model,
            input_ids=target_ids,
            capture_layers=set(),
            interventions={"layers_output": {layer: patched}},
        )
        mx.eval(result2.logits)

        # Get next-token probabilities
        next_probs = mx.softmax(result2.logits[:, -1, :], axis=-1)
        probs_per_layer.append(next_probs)

    # Stack: (num_layers, num_sources, vocab) -> (num_sources, num_layers, vocab)
    result_probs = mx.stack(probs_per_layer)
    result_probs = mx.transpose(result_probs, axes=[1, 0, 2])
    mx.eval(result_probs)
    return result_probs
