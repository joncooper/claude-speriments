(* Approach 2: Fibonacci Ratio
   The ratio F(n+1)/F(n) converges to φ as n grows.
   Uses 64-bit integers for exact Fibonacci values. *)

let () =
  let rec fib_pair n a b =
    if n = 0 then (a, b)
    else fib_pair (n - 1) b (a + b)
  in
  let n = 50 in
  let (fn, fn1) = fib_pair n 0 1 in
  let phi = float_of_int fn1 /. float_of_int fn in
  Printf.printf "Approach: Fibonacci ratio F(%d)/F(%d)\n" (n + 1) n;
  Printf.printf "F(%d) = %d\n" n fn;
  Printf.printf "F(%d) = %d\n" (n + 1) fn1;
  Printf.printf "φ ≈ %.10f\n" phi
