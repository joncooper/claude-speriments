(* Approach 10: Power Iteration (Dominant Eigenvalue)
   The matrix [[1,1],[1,0]] has eigenvalues φ and ψ = -1/φ.
   Power iteration: repeatedly multiply a vector by the matrix
   and normalize. The result converges to the dominant eigenvalue φ. *)

let () =
  let eps = 1e-15 in
  let rec iterate vx vy iter =
    (* Multiply by [[1,1],[1,0]] *)
    let wx = vx +. vy in
    let wy = vx in
    (* Compute the Rayleigh quotient as eigenvalue estimate:
       λ ≈ (v · Mv) / (v · v), but simpler: λ ≈ ||w|| / ||v|| *)
    let norm_v = sqrt (vx *. vx +. vy *. vy) in
    let norm_w = sqrt (wx *. wx +. wy *. wy) in
    let lambda = norm_w /. norm_v in
    (* Normalize w *)
    let wx' = wx /. norm_w in
    let wy' = wy /. norm_w in
    if abs_float (lambda -. (1.0 +. sqrt 5.0) /. 2.0) < eps || iter > 200 then
      (lambda, iter)
    else
      iterate wx' wy' (iter + 1)
  in
  let (phi, iters) = iterate 1.0 0.0 1 in
  Printf.printf "Approach: Power iteration on [[1,1],[1,0]]\n";
  Printf.printf "Starting vector: [1, 0]\n";
  Printf.printf "Converged in %d iterations\n" iters;
  Printf.printf "Dominant eigenvalue φ ≈ %.10f\n" phi
