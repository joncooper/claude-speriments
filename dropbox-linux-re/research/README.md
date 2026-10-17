# Research trail

Raw analysis artifacts behind the spec and de-obfuscation, preserved for
reproducibility. This is a research record, not a clean library.

## Included
- `EVIDENCE.md` — consolidated static-analysis evidence (provenance, inventory,
  architecture map, FFI contracts, server table, headers, obfuscation posture).
- `spec-sections/` — the per-dimension spec sections authored by the analysis
  fan-out, plus `verification.md` (the adversarial-verification report with the
  corrections that were folded into the final spec).
- `corpus/` — extracted string/evidence corpus:
  `str_libdropbox_core.so.txt`, `str_libdropbox_tprt.so.txt` (native string
  tables), `pyc_strings.txt` (raw, pre-decrypt), `py_layer_strings.txt`
  (post-decrypt Python-layer constants), `modules.txt`, `api_*.txt` (FFI
  identifiers), `dec_marshal_entry.json`.
- `oracle/` — full de-obfuscation tooling trail: all harness C sources
  (`harness*.c`), every driver (`driver*.py`, `mini*.py`, `probe.py`), the
  opcode-map corpus compiler (`driver5.py`, `rare*.py`, `corpus_list.txt`),
  `opcode_map.json`, `transcode.py`, `decompile_all.sh`, host/their reference
  JSONs, and small outputs (`code_trees.pkl` for the sampled modules,
  `their_corpus_codes.json`, `stock_abc.pyc`, `stockdis_abc.txt`).
- `scripts/` — ad-hoc analysis scripts (entropy/marshal-walk/xor tests, Rust
  architecture extractor).
- `client/dropbox-lnx.x86_64-274.4.4905.tar.gz` — the exact official installer
  everything derives from (sha256 `c450ec3e659a4ab556b73304e075d2a5655faf891e085ad178e4282c727ec96a`).

## Excluded (regenerable; omitted for size)
- `libpython.text.asm` (~87 MB) — `objdump -d libpython3.11.so.1.0`.
- `all_trees.pkl` (~47 MB) — all decrypted code objects; rebuild via
  `oracle/driver4.py`.
- full `stockpyc/` incl. stdlib (~57 MB) — the `dropbox.*`/`apex.*` subset is in
  `../transcoded-pyc/`.
- extracted `.dropbox-dist/` tree and `python-pypkg.zip` contents — untar/unzip
  the installer in `client/`.
- third-party checkouts/builds (pycdc, the REA agent repo).

## Regenerate
Untar `client/…tar.gz`; follow `../deobfuscation/README.md` to build the oracle
harness, export+transcode, then decompile with pycdc.
