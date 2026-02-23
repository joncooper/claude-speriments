# Implementation Notes

## Precision

OCaml's `float` type is IEEE 754 double precision, giving ~15–16 significant decimal digits. All programs easily exceed the 10-digit target; we display exactly 10 with `%.10f`.

## Why these 10 approaches?

The goal was maximum variety across different mathematical domains:

- **Algebraic/direct** (`phi_direct`, `phi_trigonometric`): One call to a transcendental function; relies entirely on the quality of the FP implementation.
- **Sequence limits** (`phi_fibonacci`, `phi_continued_fraction`): Both converge at the same rate (φ^-n per step) because the continued fraction truncations *are* Fibonacci ratios. The code style differs: one uses float recursion, the other builds up a tower of fractions.
- **Root-finding** (`phi_newton`, `phi_bisection`, `phi_fixed_point`): Three distinct strategies. Newton is superlinear (quadratic), bisection is linear with a convergence guarantee, fixed-point is linear but requires no derivative.
- **Linear algebra** (`phi_matrix`): Uses fast matrix exponentiation (O(log n) multiplications). The same Fibonacci ratio emerges from the matrix structure—a fundamentally different computation path.
- **Analysis/series** (`phi_power_series`): Applies the generalized binomial theorem to express √5 as an infinite sum. Geometric convergence (ratio = 1/4) is faster than Fibonacci-based linear convergence.
- **Exact arithmetic** (`phi_zarith`): Eliminates floating-point accumulation during the Fibonacci recurrence. All rounding is deferred to a single `Q.to_float` at the end.

## phi_continued_fraction vs phi_fixed_point

Both iterate x ← 1 + 1/x. The distinction:

- `phi_fixed_point`: runs until `|x' - x| < eps` (convergence criterion).
- `phi_continued_fraction`: runs a fixed 200 iterations regardless (truncated CF evaluation).

They are mathematically equivalent but illustrate different programming idioms.

## Zarith fraction output

After 100 Fibonacci steps the exact rational is F(101)/F(100):

```
573147844013817084101 / 354224848179261915075
```

These are 21-digit integers — well beyond the 64-bit integer range, which is why Zarith is needed.

## OCaml-specific notes

- `Float.pi` and `Float.abs` require OCaml ≥ 4.03.
- `Float.of_int` requires OCaml ≥ 4.07.
- All programs are purely functional except `phi_power_series.ml`, which uses a `while` loop with mutable refs for clarity.
- The `mat_pow` function in `phi_matrix.ml` uses structural recursion; OCaml will optimise the even-branch tail calls.
