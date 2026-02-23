(** Approach 10: Exact rational arithmetic via Zarith
    Computes Fibonacci numbers as arbitrary-precision integers (Z.t), then forms
    the exact rational F(n+1)/F(n) using Q (Zarith rational module).
    No floating-point rounding occurs until the final conversion to float.
    This gives the tightest rational approximation to phi achievable with n steps,
    along with the exact fraction for inspection. *)

let () =
  let n = 100 in
  let rec fib_pair a b count =
    if count = 0 then (a, b)
    else fib_pair b (Z.add a b) (count - 1)
  in
  let (fn, fn1) = fib_pair Z.one Z.one n in
  let q = Q.div (Q.of_bigint fn1) (Q.of_bigint fn) in
  Printf.printf "phi = %.10f\n" (Q.to_float q);
  Printf.printf "exact fraction: %s / %s\n"
    (Z.to_string (Q.num q))
    (Z.to_string (Q.den q))
