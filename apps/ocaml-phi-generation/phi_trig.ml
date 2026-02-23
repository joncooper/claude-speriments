(* Approach 8: Trigonometric Identity
   φ = 2 · cos(π/5)
   This connects the golden ratio to the regular pentagon,
   where the diagonal-to-side ratio equals φ. *)

let () =
  let pi = 4.0 *. atan 1.0 in
  let phi = 2.0 *. cos (pi /. 5.0) in
  Printf.printf "Approach: Trigonometric identity φ = 2·cos(π/5)\n";
  Printf.printf "π = %.15f\n" pi;
  Printf.printf "π/5 = %.15f\n" (pi /. 5.0);
  Printf.printf "cos(π/5) = %.15f\n" (cos (pi /. 5.0));
  Printf.printf "φ ≈ %.10f\n" phi
