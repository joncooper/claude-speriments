(** Approach 7: 2x2 matrix exponentiation
    The matrix M = [[1,1],[1,0]] satisfies M^n = [[F(n+1), F(n)], [F(n), F(n-1)]]
    where F(n) is the nth Fibonacci number.
    phi = lim F(n+1)/F(n) = lim M^n[0][0] / M^n[0][1]
    Fast exponentiation by repeated squaring gives O(log n) matrix multiplications. *)

type mat2 = { a: float; b: float; c: float; d: float }

let mul m1 m2 = {
  a = m1.a *. m2.a +. m1.b *. m2.c;
  b = m1.a *. m2.b +. m1.b *. m2.d;
  c = m1.c *. m2.a +. m1.d *. m2.c;
  d = m1.c *. m2.b +. m1.d *. m2.d;
}

let fib_matrix = { a = 1.0; b = 1.0; c = 1.0; d = 0.0 }

let () =
  let rec mat_pow m n =
    if n = 1 then m
    else if n mod 2 = 0 then
      let half = mat_pow m (n / 2) in mul half half
    else
      mul m (mat_pow m (n - 1))
  in
  (* M^80: m.a = F(81), m.b = F(80) *)
  let m = mat_pow fib_matrix 80 in
  let phi = m.a /. m.b in
  Printf.printf "phi = %.10f\n" phi
