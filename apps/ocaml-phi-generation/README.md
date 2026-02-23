# OCaml Phi Generation

Ten OCaml programs that compute the golden ratio φ ≈ 1.6180339887 to 10 digits of precision, each using a different mathematical approach.

**Status:** Complete

## Programs

| # | File | Approach | Category |
|---|------|----------|----------|
| 1 | `phi_direct.ml` | `(1 + √5) / 2` | Closed-form |
| 2 | `phi_fibonacci.ml` | `F(n+1) / F(n)` ratio convergence | Sequence |
| 3 | `phi_continued_fraction.ml` | `[1; 1, 1, 1, ...]` continued fraction | Iterative |
| 4 | `phi_newton.ml` | Newton's method on `x² − x − 1 = 0` | Root-finding |
| 5 | `phi_fixedpoint.ml` | Fixed-point iteration `x = 1 + 1/x` | Iterative |
| 6 | `phi_matrix.ml` | Matrix exponentiation `[[1,1],[1,0]]^n` | Linear algebra |
| 7 | `phi_nested_radicals.ml` | `√(1 + √(1 + √(1 + ...)))` | Iterative |
| 8 | `phi_trig.ml` | `2 · cos(π/5)` | Trigonometric |
| 9 | `phi_bisection.ml` | Bisection method on `x² − x − 1 = 0` | Root-finding |
| 10 | `phi_power_iteration.ml` | Dominant eigenvalue of Fibonacci matrix | Linear algebra |

## Requirements

- OCaml compiler (4.x or 5.x)
- No external libraries needed — all programs use only the standard library

## Usage

Run all programs at once:

```bash
./run_all.sh
```

Or compile and run individually:

```bash
ocaml phi_direct.ml
ocaml phi_fibonacci.ml
# etc.
```

Or compile to native code:

```bash
make        # Compile all
make run    # Compile and run all
make clean  # Remove binaries
```

## Sample Output

```
=== Computing φ (golden ratio) to 10 digits of precision ===
=== Expected value: 1.6180339887 ===

────────────────────────────────────────
Approach: Direct algebraic formula (1 + sqrt(5)) / 2
φ = 1.6180339887

────────────────────────────────────────
Approach: Fibonacci ratio F(51)/F(50)
φ ≈ 1.6180339887

────────────────────────────────────────
Approach: Continued fraction [1; 1, 1, 1, ...]
Depth: 100 iterations
φ ≈ 1.6180339887

...
```

## Mathematical Background

The golden ratio φ is defined as the positive root of `x² − x − 1 = 0`, yielding the exact value `(1 + √5) / 2`. It appears throughout mathematics, art, and nature. Its unique properties include:

- **Self-similarity:** `φ² = φ + 1`, so `φ = 1 + 1/φ`
- **Simplest continued fraction:** All partial quotients are 1
- **Fibonacci connection:** `lim F(n+1)/F(n) = φ`
- **Pentagon geometry:** Diagonal-to-side ratio of a regular pentagon is φ
