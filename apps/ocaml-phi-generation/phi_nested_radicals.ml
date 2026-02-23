(* Approach 7: Nested Radicals
   φ = √(1 + √(1 + √(1 + √(1 + ...))))
   This follows from φ² = φ + 1, hence φ = √(1 + φ).
   We evaluate from the inside out, starting with an initial guess. *)

let () =
  let depth = 100 in
  let rec nested n acc =
    if n = 0 then acc
    else nested (n - 1) (sqrt (1.0 +. acc))
  in
  let phi = nested depth 1.0 in
  Printf.printf "Approach: Nested radicals √(1 + √(1 + √(1 + ...)))\n";
  Printf.printf "Nesting depth: %d\n" depth;
  Printf.printf "φ ≈ %.10f\n" phi
