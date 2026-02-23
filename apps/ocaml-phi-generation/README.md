# ocaml-phi-generation

Ten OCaml programs that each compute the golden ratio (φ ≈ 1.6180339887) to 10 digits of precision using a different algorithm or library.

**Status:** Complete

---

## What is phi?

φ = (1 + √5) / 2 ≈ 1.6180339887498948...

It is the positive root of x² − x − 1 = 0 and the limit of the ratio of consecutive Fibonacci numbers.

---

## Programs

| File | Approach | Technique |
|------|----------|-----------|
| `phi_direct.ml` | Direct formula | `(1 + sqrt 5) / 2` |
| `phi_fibonacci.ml` | Fibonacci ratio | `F(n+1) / F(n)` as n → ∞ |
| `phi_continued_fraction.ml` | Continued fraction | Truncated `[1; 1, 1, 1, …]` |
| `phi_newton.ml` | Newton-Raphson | Root of x² − x − 1 |
| `phi_fixed_point.ml` | Fixed-point iteration | x = 1 + 1/x |
| `phi_bisection.ml` | Bisection | Bracket root of x² − x − 1 |
| `phi_matrix.ml` | Matrix exponentiation | `[[1,1],[1,0]]^n` gives Fibonacci numbers |
| `phi_power_series.ml` | Binomial power series | `sqrt(5) = 2·sqrt(1 + 1/4)` via Taylor series |
| `phi_trigonometric.ml` | Trigonometric identity | φ = 2·cos(π/5) |
| `phi_zarith.ml` | Exact rational arithmetic | Zarith `Z` / `Q` modules |

---

## Setup

### Requirements

- OCaml ≥ 4.07
- [opam](https://opam.ocaml.org/) package manager
- [dune](https://dune.build/) build system
- [zarith](https://github.com/ocaml/Zarith) (only for `phi_zarith`)

```bash
opam install dune zarith
```

### Build all programs

```bash
cd apps/ocaml-phi-generation
dune build
```

### Run a single program

```bash
dune exec ./bin/phi_direct.exe
dune exec ./bin/phi_fibonacci.exe
# ... etc.
```

### Run all programs

```bash
for prog in direct fibonacci continued_fraction newton fixed_point bisection matrix power_series trigonometric zarith; do
  echo "--- phi_${prog} ---"
  dune exec ./bin/phi_${prog}.exe
done
```

Expected output for every program (first line):

```
phi = 1.6180339887
```

The `phi_zarith` program additionally prints the exact rational fraction:

```
phi = 1.6180339887
exact fraction: 573147844013817084101 / 354224848179261915075
```

---

## Convergence notes

| Program | Convergence | Iterations to 10 digits |
|---------|-------------|--------------------------|
| `phi_direct` | Single step (floating-point sqrt) | 1 |
| `phi_trigonometric` | Single step (floating-point cos) | 1 |
| `phi_fibonacci` | Linear ~0.48 bits/step | ~40 |
| `phi_continued_fraction` | Linear ~0.48 bits/step | ~40 |
| `phi_fixed_point` | Linear | ~50 |
| `phi_bisection` | Linear 1 bit/step | ~46 |
| `phi_power_series` | Geometric (ratio 1/4 per term) | ~25 |
| `phi_newton` | Quadratic (digits double per step) | ~5 |
| `phi_matrix` | Same as Fibonacci (log n matrices) | 80 |
| `phi_zarith` | Exact rational, no FP error until final conversion | 100 |
