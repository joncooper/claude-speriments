(** Approach 4: Newton-Raphson root finding
    phi is the positive root of f(x) = x^2 - x - 1 = 0
    Iteration: x_{n+1} = x_n - f(x_n) / f'(x_n)
              = x_n - (x^2 - x - 1) / (2x - 1)
    Newton's method has quadratic convergence: digits roughly double each step. *)

let f x  = x *. x -. x -. 1.0
let df x = 2.0 *. x -. 1.0

let () =
  let eps = 1e-14 in
  let rec newton x =
    let step = f x /. df x in
    if Float.abs step < eps then x -. step
    else newton (x -. step)
  in
  let phi = newton 1.5 in
  Printf.printf "phi = %.10f\n" phi
