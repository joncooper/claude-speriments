# Implementation Notes

## Design Decisions

- **Standard library only.** All 10 programs use OCaml's built-in `float` type and standard math functions (`sqrt`, `cos`, `atan`). No opam packages required, keeping the barrier to entry minimal.
- **Each program is self-contained.** Every `.ml` file can be run independently with `ocaml filename.ml`. No shared modules or dependencies between programs.
- **IEEE 754 double precision.** OCaml's `float` is a 64-bit double, which provides ~15-17 significant digits — more than enough for 10-digit precision.

## Convergence Characteristics

| Approach | Convergence Rate | Iterations Needed |
|----------|-----------------|-------------------|
| Direct formula | Exact (1 step) | 1 |
| Trigonometric | Exact (1 step) | 1 |
| Newton's method | Quadratic | ~5 |
| Bisection | Linear (halving) | ~50 |
| Fibonacci ratio | Linear | ~40 for 10 digits |
| Fixed-point iteration | Linear | ~80 |
| Continued fraction | Linear | ~40 |
| Nested radicals | Linear | ~40 |
| Matrix exponentiation | Depends on n | Single computation |
| Power iteration | Linear | ~80 |

## Interesting Observations

- The continued fraction for φ is `[1; 1, 1, 1, ...]` — all 1s. This makes φ the "most irrational" number in the sense that its rational approximations converge the slowest.
- Newton's method converges quadratically (digits double each step), reaching full double precision in about 5 iterations from x₀ = 2.
- The Fibonacci approach uses 64-bit OCaml integers, which overflow around F(93). We use n=50 which is safe and already gives full double-precision accuracy.
- The power iteration and matrix exponentiation approaches are conceptually related: both exploit the fact that φ is the dominant eigenvalue of the Fibonacci matrix.
