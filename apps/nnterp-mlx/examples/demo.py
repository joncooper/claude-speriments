"""
Demo script for nnterp-mlx: mechanistic interpretability on Apple Silicon.

This script demonstrates the core features of nnterp-mlx:
1. Loading a model
2. Capturing activations at each layer
3. Running the logit lens
4. Patchscope lens
5. Activation steering
6. Using the Prompt class for tracking target token probabilities

Requires an Apple Silicon Mac with mlx installed.
"""

import mlx.core as mx
from nnterp_mlx import (
    MLXTransformer,
    logit_lens,
    patchscope_lens,
    collect_activations,
    repeat_prompt,
    Prompt,
)

# --- 1. Load a model ---
print("=" * 60)
print("Loading model...")
model = MLXTransformer("mlx-community/Llama-3.2-1B-Instruct-4bit")
print(f"Loaded: {model}")
print(f"  Layers: {model.num_layers}")
print(f"  Hidden size: {model.hidden_size}")
print(f"  Vocab size: {model.vocab_size}")
print()

# --- 2. Basic tracing: capture layer activations ---
print("=" * 60)
print("Tracing activations...")
with model.trace("The capital of France is", capture_layers=[0, 8, 15]) as result:
    pass

print(f"Logits shape: {result.logits.shape}")
for layer_idx, act in result.layers_output.items():
    print(f"  Layer {layer_idx} output: {act.shape}")

# Show top predictions from final logits
probs = mx.softmax(result.logits[0, -1, :], axis=-1)
top_indices = mx.argpartition(-probs, kth=5)[:5]
print("\nTop 5 predictions:")
for idx in top_indices.tolist():
    token = model.tokenizer.convert_ids_to_tokens([idx])[0]
    print(f"  {token}: {float(probs[idx]):.4f}")
print()

# --- 3. Logit lens ---
print("=" * 60)
print("Running logit lens...")
lens_probs = logit_lens(model, "The capital of France is")
print(f"Logit lens output shape: {lens_probs.shape}")
print("  (num_prompts, num_layers, vocab_size)")

# Show what each layer predicts for the next token
print("\nLayer-by-layer top prediction:")
for layer in range(0, model.num_layers, 4):
    layer_probs = lens_probs[0, layer, :]
    top_idx = int(mx.argmax(layer_probs))
    token = model.tokenizer.convert_ids_to_tokens([top_idx])[0]
    print(f"  Layer {layer:2d}: {token} ({float(layer_probs[top_idx]):.4f})")
print()

# --- 4. Collect activations ---
print("=" * 60)
print("Collecting activations across prompts...")
prompts = [
    "The capital of France is",
    "The capital of Germany is",
    "The capital of Japan is",
]
acts = collect_activations(model, prompts, layers=[0, 8, 15])
print(f"Activations shape: {acts.shape}")
print("  (num_layers, num_prompts, hidden_size)")
print()

# --- 5. Top-k closest tokens ---
print("=" * 60)
print("Top-k closest tokens for layer 15 activations...")
for i, prompt in enumerate(prompts):
    hidden = acts[2, i, :]  # Layer 15 (index 2 since we captured [0,8,15])
    topk = model.get_topk_closest_tokens(hidden, k=5)
    print(f"\n  '{prompt}'")
    for token, prob in topk.items():
        print(f"    {token}: {prob:.4f}")
print()

# --- 6. Prompt class for tracking probabilities ---
print("=" * 60)
print("Using Prompt class to track target probabilities...")
prompt = Prompt.from_strings(
    "The capital of France is",
    {"correct": "Paris", "incorrect": ["London", "Berlin", "Tokyo"]},
    model.tokenizer,
)
print(f"Tracking tokens: {prompt.target_tokens}")

lens_result = logit_lens(model, prompt.prompt)
target_probs = prompt.get_target_probs(lens_result)
print("\nProbability by layer:")
for layer in range(0, model.num_layers, 4):
    correct = float(target_probs["correct"][0, layer])
    incorrect = float(target_probs["incorrect"][0, layer])
    print(f"  Layer {layer:2d}: correct={correct:.4f}, incorrect={incorrect:.4f}")
print()

# --- 7. Patchscope lens ---
print("=" * 60)
print("Running patchscope lens...")
patch_probs = patchscope_lens(
    model,
    source_prompts=["The capital of France is"],
    layers=[0, 8, 15],
)
print(f"Patchscope output shape: {patch_probs.shape}")
print("  (num_sources, num_layers, vocab_size)")

for i, layer in enumerate([0, 8, 15]):
    layer_probs = patch_probs[0, i, :]
    top_idx = int(mx.argmax(layer_probs))
    token = model.tokenizer.convert_ids_to_tokens([top_idx])[0]
    print(f"  Layer {layer:2d} patchscope prediction: {token} ({float(layer_probs[top_idx]):.4f})")
print()

# --- 8. Layer skipping ---
print("=" * 60)
print("Layer skipping experiment...")
clean_logits = model.forward(model.tokenize("The capital of France is")["input_ids"])
mx.eval(clean_logits)
clean_top = int(mx.argmax(clean_logits[0, -1, :]))
clean_token = model.tokenizer.convert_ids_to_tokens([clean_top])[0]
print(f"  Clean prediction: {clean_token}")

# Skip middle layers
skip_logits = model.skip_layers("The capital of France is", 4, 12)
skip_top = int(mx.argmax(skip_logits[0, -1, :]))
skip_token = model.tokenizer.convert_ids_to_tokens([skip_top])[0]
print(f"  Skipping layers 4-12: {skip_token}")
print()

print("=" * 60)
print("Demo complete!")
