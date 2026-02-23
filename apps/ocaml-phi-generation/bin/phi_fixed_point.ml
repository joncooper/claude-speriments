(** Approach 5: Fixed-point iteration
    phi satisfies phi = 1 + 1/phi (rearrangement of phi^2 = phi + 1).
    The map g(x) = 1 + 1/x is a contraction near phi, so iteration converges.
    Convergence is linear (unlike Newton's quadratic), requiring more steps. *)

let () =
  let eps = 1e-14 in
  let rec iterate x =
    let x' = 1.0 +. 1.0 /. x in
    if Float.abs (x' -. x) < eps then x'
    else iterate x'
  in
  let phi = iterate 2.0 in
  Printf.printf "phi = %.10f\n" phi
