(** Approach 1: Direct algebraic formula
    phi = (1 + sqrt(5)) / 2
    Uses OCaml's built-in float sqrt (IEEE 754 double precision). *)

let () =
  let phi = (1.0 +. sqrt 5.0) /. 2.0 in
  Printf.printf "phi = %.10f\n" phi
