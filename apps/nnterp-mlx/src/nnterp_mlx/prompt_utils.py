"""
Prompt utilities for tracking token probabilities during interpretability experiments.

Port of nnterp's prompt_utils module, adapted to work with MLX arrays.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable

import mlx.core as mx

if TYPE_CHECKING:
    from .model import MLXTransformer

# Re-export from interventions for convenience
from .interventions import TargetPrompt, repeat_prompt


def get_first_tokens(
    words: str | list[str],
    tokenizer,
) -> list[int]:
    """
    Get the first token IDs for each word (with and without leading space).

    For example, "Paris" might tokenize to token 3681, and " Paris" to token 6342.
    Both are returned to cover different tokenization contexts.

    Args:
        words: A string or list of strings.
        tokenizer: A tokenizer with __call__ and convert_ids_to_tokens methods.

    Returns:
        List of unique token IDs.
    """
    if isinstance(words, str):
        words = [words]

    final_tokens = []
    for word in words:
        # Token without space prefix
        token = tokenizer(word, add_special_tokens=False)["input_ids"][0]
        final_tokens.append(token)

        # Token with space prefix
        space_token = tokenizer(" " + word, add_special_tokens=False)["input_ids"][0]
        if space_token != token:
            final_tokens.append(space_token)

    # Remove duplicates while preserving order
    return list(dict.fromkeys(final_tokens))


@dataclass
class Prompt:
    """
    A prompt with target tokens to track during next-token prediction.

    This allows you to measure the probability assigned to specific
    target categories during interpretability experiments.

    Example::

        prompt = Prompt.from_strings(
            "The capital of France is",
            {"correct": "Paris", "incorrect": ["London", "Berlin"]},
            tokenizer,
        )
        probs = prompt.get_target_probs(logit_lens_output)

    Args:
        prompt: The text prompt.
        target_tokens: Dict mapping category name -> list of token IDs.
        target_strings: Optional dict mapping category name -> original strings.
    """

    prompt: str
    target_tokens: dict[str, list[int]]
    target_strings: dict[str, str | list[str]] | None = None

    @classmethod
    def from_strings(
        cls,
        prompt: str,
        target_strings: dict[str, str | list[str]] | list[str] | str,
        tokenizer,
    ) -> Prompt:
        """
        Create a Prompt from string targets.

        Args:
            prompt: The text prompt.
            target_strings: Either:
                - A dict mapping category names to target words/lists
                - A list of target words (assigned to "target" category)
                - A single target word (assigned to "target" category)
            tokenizer: Tokenizer for converting words to token IDs.

        Returns:
            A Prompt instance with resolved token IDs.
        """
        if isinstance(target_strings, (str, list)):
            target_strings = {"target": target_strings}

        target_tokens = {
            target: get_first_tokens(words, tokenizer)
            for target, words in target_strings.items()
        }
        return cls(
            prompt=prompt,
            target_tokens=target_tokens,
            target_strings=target_strings,
        )

    def has_no_collisions(self, ignore_targets: str | list[str] | None = None) -> bool:
        """Check that no token ID appears in multiple target categories."""
        if isinstance(ignore_targets, str):
            ignore_targets = [ignore_targets]
        if ignore_targets is None:
            ignore_targets = []

        all_tokens = []
        for target, tokens in self.target_tokens.items():
            if target in ignore_targets:
                continue
            all_tokens.extend(tokens)
        return len(all_tokens) == len(set(all_tokens))

    def get_target_probs(
        self,
        probs: mx.array,
        layer: int | None = None,
    ) -> dict[str, mx.array]:
        """
        Extract probabilities for each target category from a probability tensor.

        Args:
            probs: Probability tensor of shape (num_prompts, num_layers, vocab_size)
                or (num_layers, vocab_size).
            layer: If specified, return probs for only this layer index.

        Returns:
            Dict mapping target name -> probability tensor.
        """
        target_probs = {}
        for target, tokens in self.target_tokens.items():
            token_indices = mx.array(tokens)
            # Sum probabilities across all tokens for this target
            target_prob = probs[..., tokens].sum(axis=-1)
            target_probs[target] = target_prob

        if layer is not None:
            if probs.ndim == 3:
                target_probs = {
                    target: p[:, layer] for target, p in target_probs.items()
                }
            elif probs.ndim == 2:
                target_probs = {
                    target: p[layer] for target, p in target_probs.items()
                }

        return target_probs


def run_prompts(
    model: MLXTransformer,
    prompts: list[Prompt],
    batch_size: int = 32,
    get_probs_func: Callable | None = None,
) -> dict[str, mx.array]:
    """
    Run a list of prompts through the model and return target probabilities.

    Args:
        model: The MLXTransformer model.
        prompts: List of Prompt objects. All must have the same target keys.
        batch_size: Batch size for processing.
        get_probs_func: Function to get probabilities. Default: next-token probs.

    Returns:
        Dict mapping target name -> probability tensor of shape (num_prompts,).
    """
    if len(prompts) == 0:
        return {}

    # Validate all prompts have same target keys
    keys = set(prompts[0].target_tokens.keys())
    for prompt in prompts:
        if set(prompt.target_tokens.keys()) != keys:
            raise ValueError(
                f"All prompts must have the same target keys. "
                f"Got {keys} and {set(prompt.target_tokens.keys())}"
            )

    str_prompts = [p.prompt for p in prompts]
    all_probs = []

    for i in range(0, len(str_prompts), batch_size):
        batch = str_prompts[i : i + batch_size]
        if get_probs_func is not None:
            probs = get_probs_func(model, batch)
        else:
            # Default: get next-token probabilities
            encoded = model.tokenize(batch)
            logits = model.forward(encoded["input_ids"])
            probs = mx.softmax(logits[:, -1, :], axis=-1)
            mx.eval(probs)
            # Add fake layer dimension: (batch, vocab) -> (batch, 1, vocab)
            probs = probs[:, None, :]
        all_probs.append(probs)

    all_probs = mx.concatenate(all_probs, axis=0)

    # Extract target probabilities per prompt
    target_probs = {target: [] for target in keys}
    for i, prompt in enumerate(prompts):
        for target, tokens in prompt.target_tokens.items():
            prob = all_probs[i, :, tokens].sum(axis=-1)
            target_probs[target].append(prob)

    return {
        target: mx.stack(probs) for target, probs in target_probs.items()
    }
