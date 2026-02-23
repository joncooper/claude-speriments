(* Approach 1: Direct Algebraic Formula
   φ = (1 + √5) / 2
   The simplest and most direct computation. *)

let () =
  let phi = (1.0 +. sqrt 5.0) /. 2.0 in
  Printf.printf "Approach: Direct algebraic formula (1 + sqrt(5)) / 2\n";
  Printf.printf "φ = %.10f\n" phi
