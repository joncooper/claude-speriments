(** Approach 6: Bisection method
    phi is the positive root of f(x) = x^2 - x - 1 = 0 in the interval [1, 2].
    At each step the interval is halved by checking the sign of f at the midpoint.
    Guaranteed linear convergence: 1 bit of precision per iteration. *)

let f x = x *. x -. x -. 1.0

let () =
  let eps = 1e-14 in
  let rec bisect a b =
    let m = (a +. b) /. 2.0 in
    if b -. a < eps then m
    else if f a *. f m <= 0.0 then bisect a m
    else bisect m b
  in
  let phi = bisect 1.0 2.0 in
  Printf.printf "phi = %.10f\n" phi
