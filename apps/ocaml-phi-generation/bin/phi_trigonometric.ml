(** Approach 9: Trigonometric identity
    phi = 2 * cos(pi/5) = 2 * cos(36 degrees)
    Derivation: the diagonal-to-side ratio of a regular pentagon equals phi,
    and that ratio can be expressed via cos(36°) through the isoceles triangle
    formed by a pentagon diagonal and two sides. *)

let () =
  let phi = 2.0 *. cos (Float.pi /. 5.0) in
  Printf.printf "phi = %.10f\n" phi
