(* Approach 3: Continued Fraction
   φ = 1 + 1/(1 + 1/(1 + 1/(1 + ...)))
   The simplest possible continued fraction: all coefficients are 1.
   We evaluate bottom-up from depth k. *)

let () =
  let depth = 100 in
  let rec cf n acc =
    if n = 0 then acc
    else cf (n - 1) (1.0 +. 1.0 /. acc)
  in
  let phi = cf depth 1.0 in
  Printf.printf "Approach: Continued fraction [1; 1, 1, 1, ...]\n";
  Printf.printf "Depth: %d iterations\n" depth;
  Printf.printf "φ ≈ %.10f\n" phi
