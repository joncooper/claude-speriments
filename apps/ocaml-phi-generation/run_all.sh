#!/bin/bash
# Run all 10 phi computation programs
# Usage: ./run_all.sh
#
# Tries compiled binaries first, falls back to ocaml interpreter.

set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

echo "=== Computing φ (golden ratio) to 10 digits of precision ==="
echo "=== Expected value: 1.6180339887 ==="
echo ""

programs=(
  phi_direct
  phi_fibonacci
  phi_continued_fraction
  phi_newton
  phi_fixedpoint
  phi_matrix
  phi_nested_radicals
  phi_trig
  phi_bisection
  phi_power_iteration
)

for prog in "${programs[@]}"; do
  echo "────────────────────────────────────────"
  if [ -x "./$prog" ]; then
    "./$prog"
  else
    ocaml "$prog.ml"
  fi
  echo ""
done

echo "=== All 10 approaches complete ==="
