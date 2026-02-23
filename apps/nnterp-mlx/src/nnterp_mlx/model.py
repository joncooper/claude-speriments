"""
MLXTransformer: A standardized interface for mechanistic interpretability
of transformer models loaded via mlx-lm.

This is a port of nnterp (https://github.com/Butanium/nnterp) to Apple's MLX
framework. Instead of NNsight's proxy-based tracing, we use modified forward
passes to capture and optionally intervene on intermediate activations.
"""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass

import mlx.core as mx
import mlx.nn as nn
import mlx_lm

from .hooks import TraceResult, traced_forward


@dataclass
class ModelInfo:
    """Metadata about a loaded model."""

    num_layers: int
    hidden_size: int
    num_heads: int
    vocab_size: int
    num_kv_heads: int
    tie_word_embeddings: bool


class LayerAccessor:
    """Provides indexed access to layer modules."""

    def __init__(self, model: MLXTransformer, attr_name: str | None = None):
        self._model = model
        self._attr_name = attr_name

    def __getitem__(self, layer: int) -> nn.Module:
        module = self._model.layers[layer]
        if self._attr_name is not None:
            module = getattr(module, self._attr_name)
        return module

    def __len__(self) -> int:
        return self._model.info.num_layers


class MLXTransformer:
    """
    Wraps an mlx-lm model with a standardized interface for mechanistic
    interpretability, inspired by nnterp's StandardizedTransformer.

    Model structure (standardized names mapping to mlx-lm internals)::

        MLXTransformer
        ├── embed_tokens      -> model.model.embed_tokens
        ├── layers[i]         -> model.model.layers[i]  (TransformerBlock)
        │   ├── self_attn     -> layers[i].self_attn
        │   └── mlp           -> layers[i].mlp
        ├── ln_final          -> model.model.norm
        └── lm_head           -> model.lm_head (or tied embeddings)

    Example::

        model = MLXTransformer("mlx-community/Llama-3.2-1B-Instruct-4bit")

        # Capture activations
        with model.trace("The capital of France is") as result:
            pass
        layer_5_output = result.layers_output[5]
        logits = result.logits

        # Interventions
        with model.trace(
            "The capital of France is",
            interventions={"layers_output": {5: replacement_tensor}},
        ) as result:
            pass
        modified_logits = result.logits

    Args:
        model_path: HuggingFace repo ID or local path for mlx-lm model.
        tokenizer_config: Optional tokenizer configuration overrides.
        model_config: Optional model configuration overrides.
        lazy: If True, don't evaluate model parameters immediately.
    """

    def __init__(
        self,
        model_path: str,
        tokenizer_config: dict | None = None,
        model_config: dict | None = None,
        lazy: bool = False,
    ):
        self._model_path = model_path
        self._model, self._tokenizer = mlx_lm.load(
            model_path,
            tokenizer_config=tokenizer_config or {},
            model_config=model_config or {},
            lazy=lazy,
        )

        # Extract model info from config
        self.info = self._extract_model_info()

        # Set up standardized accessors
        self.attentions = LayerAccessor(self, "self_attn")
        self.mlps = LayerAccessor(self, "mlp")

    def _extract_model_info(self) -> ModelInfo:
        """Extract model metadata from the loaded model's args/config."""
        args = self._model.args

        num_layers = getattr(args, "num_hidden_layers", None)
        if num_layers is None:
            num_layers = len(self.layers)

        hidden_size = getattr(args, "hidden_size", None)
        if hidden_size is None:
            hidden_size = getattr(args, "d_model", None)

        num_heads = getattr(args, "num_attention_heads", None)
        if num_heads is None:
            num_heads = getattr(args, "n_heads", None)

        num_kv_heads = getattr(args, "num_key_value_heads", num_heads)

        vocab_size = getattr(args, "vocab_size", None)

        tie_word_embeddings = getattr(args, "tie_word_embeddings", True)

        return ModelInfo(
            num_layers=num_layers,
            hidden_size=hidden_size,
            num_heads=num_heads,
            vocab_size=vocab_size,
            num_kv_heads=num_kv_heads,
            tie_word_embeddings=tie_word_embeddings,
        )

    # -- Standardized module accessors --

    @property
    def model(self) -> nn.Module:
        """The raw mlx-lm model."""
        return self._model

    @property
    def inner_model(self) -> nn.Module:
        """The inner model (e.g., LlamaModel, Qwen2Model)."""
        return self._model.model

    @property
    def embed_tokens(self) -> nn.Embedding:
        """Token embedding layer."""
        return self._model.model.embed_tokens

    @property
    def layers(self) -> list:
        """List of TransformerBlock layers."""
        if hasattr(self._model, "layers"):
            return self._model.layers
        return self._model.model.layers

    @property
    def ln_final(self) -> nn.Module:
        """Final layer normalization."""
        return self._model.model.norm

    @property
    def lm_head(self) -> nn.Module | None:
        """Language model head (None if tied embeddings)."""
        if hasattr(self._model, "lm_head"):
            return self._model.lm_head
        return None

    @property
    def tokenizer(self):
        """The tokenizer."""
        return self._tokenizer

    @property
    def num_layers(self) -> int:
        return self.info.num_layers

    @property
    def hidden_size(self) -> int:
        return self.info.hidden_size

    @property
    def vocab_size(self) -> int:
        return self.info.vocab_size

    # -- Tokenization --

    def tokenize(
        self,
        prompts: str | list[str],
        return_mx: bool = True,
    ) -> dict:
        """
        Tokenize prompts, returning input_ids (and optionally as mx.array).

        Args:
            prompts: Single prompt or list of prompts.
            return_mx: If True, return mx.array; otherwise return list[list[int]].
        """
        if isinstance(prompts, str):
            prompts = [prompts]

        encoded = self._tokenizer(
            prompts,
            return_tensors=None,
            padding=True if len(prompts) > 1 else False,
        )
        input_ids = encoded["input_ids"]

        if return_mx:
            if isinstance(input_ids[0], list):
                input_ids = mx.array(input_ids)
            else:
                input_ids = mx.array([input_ids])

        return {"input_ids": input_ids}

    # -- Forward pass --

    def forward(
        self,
        input_ids: mx.array,
        cache: list | None = None,
    ) -> mx.array:
        """
        Run a forward pass, returning logits.

        Args:
            input_ids: Token IDs of shape (batch_size, seq_len).
            cache: Optional KV cache.

        Returns:
            Logits of shape (batch_size, seq_len, vocab_size).
        """
        return self._model(input_ids, cache=cache)

    # -- Projection utilities --

    def project_on_vocab(self, hidden_states: mx.array) -> mx.array:
        """
        Project hidden states through ln_final + lm_head to get logits.

        Args:
            hidden_states: Shape (..., hidden_size).

        Returns:
            Logits of shape (..., vocab_size).
        """
        normed = self.ln_final(hidden_states)
        if self.lm_head is not None:
            return self.lm_head(normed)
        else:
            # Tied embeddings
            return self.embed_tokens.as_linear(normed)

    def get_topk_closest_tokens(
        self,
        hidden_state: mx.array,
        k: int = 5,
    ) -> list[dict[str, float]]:
        """
        Get the top-k closest tokens to a hidden state via the logit lens.

        Args:
            hidden_state: Shape (hidden_size,) or (batch_size, hidden_size).
            k: Number of top tokens.

        Returns:
            List of dicts mapping token strings to probabilities.
        """
        if hidden_state.ndim == 1:
            hidden_state = hidden_state[None, :]

        logits = self.project_on_vocab(hidden_state)
        probs = mx.softmax(logits, axis=-1)

        # Get top-k indices and values
        top_indices = mx.argpartition(-probs, kth=k - 1, axis=-1)[..., :k]

        results = []
        for batch_idx in range(hidden_state.shape[0]):
            batch_probs = probs[batch_idx]
            batch_indices = top_indices[batch_idx]
            # Sort by probability (descending)
            idx_probs = [(int(idx), float(batch_probs[idx])) for idx in batch_indices.tolist()]
            idx_probs.sort(key=lambda x: -x[1])

            token_ids = [ip[0] for ip in idx_probs]
            tokens = self._tokenizer.convert_ids_to_tokens(token_ids)
            result = {tok: prob for tok, (_, prob) in zip(tokens, idx_probs)}
            results.append(result)

        if hidden_state.shape[0] == 1:
            return results[0]
        return results

    # -- Tracing / activation capture --

    @contextmanager
    def trace(
        self,
        prompts: str | list[str],
        interventions: dict[str, dict[int, mx.array]] | None = None,
        capture_layers: list[int] | None = None,
        capture_input: bool = False,
        capture_attn: bool = False,
        capture_mlp: bool = False,
    ):
        """
        Context manager that runs a forward pass while capturing activations
        and optionally applying interventions.

        This implements a custom layer-by-layer forward pass (bypassing the
        model's own inner forward) to intercept activations at each step.

        Args:
            prompts: Input prompt(s).
            interventions: Dict mapping intervention type to layer->tensor mappings.
                Supported types:
                - "layers_output": {layer_idx: replacement_tensor}
                - "layers_input": {layer_idx: replacement_tensor}
                - "steer": {layer_idx: (steering_vector, positions_or_none)}
                - "skip": {"start": int, "end": int, "value": tensor_or_none}
            capture_layers: Which layers to capture outputs for.
                If None, captures all layers.
            capture_input: If True, also capture layer inputs.
            capture_attn: If True, capture attention outputs.
            capture_mlp: If True, capture MLP outputs.

        Yields:
            TraceResult with captured activations and logits.

        Example::

            with model.trace("Hello world", capture_layers=[0, 5, 10]) as result:
                pass
            print(result.layers_output[5].shape)
            print(result.logits.shape)
        """
        if isinstance(prompts, str):
            prompts = [prompts]

        encoded = self.tokenize(prompts)
        input_ids = encoded["input_ids"]

        result = traced_forward(
            wrapper=self,
            input_ids=input_ids,
            capture_layers=set(capture_layers) if capture_layers else None,
            capture_input=capture_input,
            capture_attn=capture_attn,
            capture_mlp=capture_mlp,
            interventions=interventions,
        )

        # Evaluate everything
        arrays_to_eval = [result.logits]
        for d in [result.layers_output, result.layers_input,
                   result.attn_output, result.mlp_output]:
            arrays_to_eval.extend(d.values())
        if result.token_embeddings is not None:
            arrays_to_eval.append(result.token_embeddings)
        mx.eval(*arrays_to_eval)

        yield result

    # -- Convenience methods --

    def steer(
        self,
        prompts: str | list[str],
        layers: int | list[int],
        steering_vector: mx.array,
        factor: float = 1.0,
        positions: int | list[int] | None = None,
    ) -> mx.array:
        """
        Run a forward pass with activation steering applied at specified layers.

        Adds factor * steering_vector to the layer output(s).

        Args:
            prompts: Input prompt(s).
            layers: Layer(s) to steer.
            steering_vector: The steering vector to add.
            factor: Multiplicative factor.
            positions: Token positions to steer. None means all positions.

        Returns:
            Modified logits.
        """
        if isinstance(layers, int):
            layers = [layers]

        steer_interventions = {
            "steer": {
                layer: (factor * steering_vector, positions)
                for layer in layers
            }
        }

        if isinstance(prompts, str):
            prompts = [prompts]

        encoded = self.tokenize(prompts)
        input_ids = encoded["input_ids"]

        result = traced_forward(
            wrapper=self,
            input_ids=input_ids,
            capture_layers=set(),
            interventions=steer_interventions,
        )
        mx.eval(result.logits)
        return result.logits

    def skip_layers(
        self,
        prompts: str | list[str],
        start_layer: int,
        end_layer: int,
        skip_with: mx.array | None = None,
    ) -> mx.array:
        """
        Run a forward pass while skipping layers [start_layer, end_layer].

        Args:
            prompts: Input prompt(s).
            start_layer: First layer to skip.
            end_layer: Last layer to skip (inclusive).
            skip_with: Tensor to use as input for skipped layers.
                If None, uses the input to start_layer.

        Returns:
            Logits from the modified forward pass.
        """
        skip_interventions = {
            "skip": {
                "start": start_layer,
                "end": end_layer,
                "value": skip_with,
            }
        }

        if isinstance(prompts, str):
            prompts = [prompts]

        encoded = self.tokenize(prompts)
        input_ids = encoded["input_ids"]

        result = traced_forward(
            wrapper=self,
            input_ids=input_ids,
            capture_layers=set(),
            interventions=skip_interventions,
        )
        mx.eval(result.logits)
        return result.logits

    @property
    def name_or_path(self) -> str:
        return self._model_path

    def __repr__(self) -> str:
        return (
            f"MLXTransformer('{self._model_path}', "
            f"layers={self.num_layers}, "
            f"hidden_size={self.hidden_size}, "
            f"vocab_size={self.vocab_size})"
        )
