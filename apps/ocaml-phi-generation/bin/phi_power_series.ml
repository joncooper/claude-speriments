(** Approach 8: Binomial power series for sqrt(5)
    sqrt(5) = 2 * sqrt(1 + 1/4)
    Using the generalized binomial series: sqrt(1+x) = sum_{n=0}^{inf} C(1/2, n) * x^n
    where x = 1/4 (|x| < 1 guarantees convergence).
    Generalized binomial coefficient: C(1/2, n) = (1/2)(1/2-1)...(1/2-n+1) / n!
    phi = (1 + sqrt(5)) / 2 *)

let () =
  let x = 0.25 in
  let eps = 1e-15 in
  (* Accumulate series sum, updating the term incrementally:
     term_n = term_{n-1} * (1/2 - (n-1)) / n * x *)
  let sqrt1px =
    let sum  = ref 1.0 in
    let term = ref 1.0 in
    let n    = ref 1 in
    while Float.abs !term > eps do
      term := !term *. (0.5 -. Float.of_int (!n - 1)) /. Float.of_int !n *. x;
      sum  := !sum +. !term;
      incr n
    done;
    !sum
  in
  let phi = (1.0 +. 2.0 *. sqrt1px) /. 2.0 in
  Printf.printf "phi = %.10f\n" phi
