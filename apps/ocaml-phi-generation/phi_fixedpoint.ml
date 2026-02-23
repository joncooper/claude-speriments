(* Approach 5: Fixed-Point Iteration
   φ is the unique positive fixed point of g(x) = 1 + 1/x.
   Starting from any positive value, iterating x ← 1 + 1/x converges to φ. *)

let () =
  let eps = 1e-15 in
  let rec iterate x iter =
    let x_next = 1.0 +. 1.0 /. x in
    if abs_float (x_next -. x) < eps || iter > 1000 then (x_next, iter)
    else iterate x_next (iter + 1)
  in
  let x0 = 1.0 in
  let (phi, iters) = iterate x0 1 in
  Printf.printf "Approach: Fixed-point iteration x = 1 + 1/x\n";
  Printf.printf "Starting value: %.1f\n" x0;
  Printf.printf "Converged in %d iterations\n" iters;
  Printf.printf "φ ≈ %.10f\n" phi
