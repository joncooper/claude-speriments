(* Approach 6: Matrix Exponentiation
   The matrix M = [[1,1],[1,0]] has the property that M^n = [[F(n+1),F(n)],[F(n),F(n-1)]].
   We compute M^n using repeated squaring, then extract φ ≈ M[0][0] / M[0][1]. *)

type mat2 = { a: float; b: float; c: float; d: float }

let mat_mul m1 m2 = {
  a = m1.a *. m2.a +. m1.b *. m2.c;
  b = m1.a *. m2.b +. m1.b *. m2.d;
  c = m1.c *. m2.a +. m1.d *. m2.c;
  d = m1.c *. m2.b +. m1.d *. m2.d;
}

let mat_id = { a = 1.0; b = 0.0; c = 0.0; d = 1.0 }

let rec mat_pow m n =
  if n = 0 then mat_id
  else if n mod 2 = 0 then
    let half = mat_pow m (n / 2) in
    mat_mul half half
  else
    mat_mul m (mat_pow m (n - 1))

let () =
  let fib_mat = { a = 1.0; b = 1.0; c = 1.0; d = 0.0 } in
  let n = 80 in
  let result = mat_pow fib_mat n in
  let phi = result.a /. result.b in
  Printf.printf "Approach: Matrix exponentiation [[1,1],[1,0]]^%d\n" n;
  Printf.printf "M^%d = [[%.0f, %.0f], [%.0f, %.0f]]\n" n result.a result.b result.c result.d;
  Printf.printf "φ ≈ M[0][0] / M[0][1] = %.10f\n" phi
