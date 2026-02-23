(** Approach 2: Fibonacci ratio convergence
    lim_{n->inf} F(n+1) / F(n) = phi
    Consecutive Fibonacci numbers are stored as floats to avoid integer overflow.
    100 iterations gives full double-precision accuracy. *)

let () =
  let rec iterate a b n =
    if n = 0 then b /. a
    else iterate b (a +. b) (n - 1)
  in
  let phi = iterate 1.0 1.0 100 in
  Printf.printf "phi = %.10f\n" phi
