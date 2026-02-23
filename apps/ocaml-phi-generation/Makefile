SOURCES = phi_direct.ml phi_fibonacci.ml phi_continued_fraction.ml \
          phi_newton.ml phi_fixedpoint.ml phi_matrix.ml \
          phi_nested_radicals.ml phi_trig.ml phi_bisection.ml \
          phi_power_iteration.ml

BINARIES = $(SOURCES:.ml=)

.PHONY: all clean run

all: $(BINARIES)

%: %.ml
	ocamlfind ocamlopt -package stdlib -linkpkg -o $@ $< 2>/dev/null || \
	ocamlopt -o $@ $< 2>/dev/null || \
	ocaml $<

run: all
	@echo "=== Computing φ (golden ratio) to 10 digits ==="
	@echo "=== Expected: 1.6180339887 ==="
	@echo ""
	@for bin in $(BINARIES); do \
		echo "────────────────────────────────────────"; \
		if [ -x ./$$bin ]; then ./$$bin; else ocaml $$bin.ml; fi; \
		echo ""; \
	done

clean:
	rm -f $(BINARIES) *.cmi *.cmx *.o
