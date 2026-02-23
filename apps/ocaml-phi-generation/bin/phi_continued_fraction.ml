(** Approach 3: Truncated continued fraction
    phi = [1; 1, 1, 1, ...] = 1 + 1/(1 + 1/(1 + ...))
    phi has the "most irrational" continued fraction: all partial quotients are 1.
    We evaluate a finite truncation from the bottom up. *)

let () =
  let depth = 200 in
  (* Build from innermost value outward using tail recursion *)
  let rec eval acc remaining =
    if remaining = 0 then acc
    else eval (1.0 +. 1.0 /. acc) (remaining - 1)
  in
  let phi = eval 1.0 depth in
  Printf.printf "phi = %.10f\n" phi
