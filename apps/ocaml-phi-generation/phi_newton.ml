(* Approach 4: Newton's Method
   Find the positive root of f(x) = x² - x - 1 = 0.
   f'(x) = 2x - 1
   x_{n+1} = x_n - f(x_n)/f'(x_n) *)

let () =
  let f x = x *. x -. x -. 1.0 in
  let f' x = 2.0 *. x -. 1.0 in
  let eps = 1e-15 in
  let rec newton x iter =
    let x_next = x -. f x /. f' x in
    if abs_float (x_next -. x) < eps || iter > 100 then (x_next, iter)
    else newton x_next (iter + 1)
  in
  let x0 = 2.0 in
  let (phi, iters) = newton x0 1 in
  Printf.printf "Approach: Newton's method on x² - x - 1 = 0\n";
  Printf.printf "Starting guess: %.1f\n" x0;
  Printf.printf "Converged in %d iterations\n" iters;
  Printf.printf "φ ≈ %.10f\n" phi
