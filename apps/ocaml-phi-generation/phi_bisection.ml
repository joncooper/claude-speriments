(* Approach 9: Bisection Method
   Find the root of f(x) = x² - x - 1 in the interval [1, 2].
   f(1) = -1 < 0 and f(2) = 1 > 0, so there is a root between 1 and 2.
   Bisection halves the interval at each step. *)

let () =
  let f x = x *. x -. x -. 1.0 in
  let eps = 1e-15 in
  let rec bisect lo hi iter =
    let mid = (lo +. hi) /. 2.0 in
    if hi -. lo < eps || iter > 200 then (mid, iter)
    else if f mid < 0.0 then bisect mid hi (iter + 1)
    else bisect lo mid (iter + 1)
  in
  let (phi, iters) = bisect 1.0 2.0 1 in
  Printf.printf "Approach: Bisection method on x² - x - 1 = 0\n";
  Printf.printf "Initial interval: [1, 2]\n";
  Printf.printf "Converged in %d iterations\n" iters;
  Printf.printf "φ ≈ %.10f\n" phi
