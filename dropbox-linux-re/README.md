# Dropbox Linux client — reverse-engineering study

Static reverse-engineering and Python de-obfuscation of the official Dropbox
Linux desktop client **274.4.4905** (CPython branch `dbx-desktop-v3.11.14`), for
**interoperability / architecture understanding**. The client was analyzed
statically; its own interpreter was used only as a decryption oracle to
deserialize (not execute) the bundled Python.

## Contents

- `spec/DROPBOX_LINUX_CLIENT_SPEC.md` — the rebuild spec: architecture, process
  model, transport (gRPC/HTTP-2), session/auth, server topology, Nucleus sync
  protocol, block storage, Bolt notifications, persistence/crypto, and the Python
  obfuscation scheme. Every claim tagged `[OBS]`/`[INF]`/`[UNK]`; corrections
  from an adversarial verification pass are folded in.
- `deobfuscation/` — original tooling that reverses the four-layer Python
  protection (custom pyc magic, encrypted marshal payload, permuted opcode
  numbering, stubbed `marshal.dumps`): a C harness that drives the shipped
  interpreter as a decryption oracle, the opcode-map recovery drivers,
  `opcode_map.json` (full 108-opcode their→stock permutation), and `transcode.py`
  which rebuilds stock CPython-3.11 `.pyc`. See `deobfuscation/README.md`.
- `decompiled/` — Python **source** for the `dropbox.*` and `apex.*` packages,
  via `pycdc` on the transcoded pyc. Coverage: ~1360 clean, ~1250 partial
  (pycdc's 3.11 limits — `# WARNING: Decompyle incomplete`), ~240 that crash
  pycdc (use the disassembly/transcoded pyc instead).
- `transcoded-pyc/` — the de-obfuscated stock-3.11 `.pyc` for `dropbox.*`/`apex.*`
  (ground truth; readable by any stock `dis`/decompiler).

## Provenance & licensing

All code under `decompiled/` and `transcoded-pyc/` is **Dropbox, Inc.'s
copyrighted code**, recovered from the publicly distributed client installer. It
is included here for study and interoperability only and is **not** covered by
this repository's license. The `spec/` and `deobfuscation/` directories are
original work. Not affiliated with or endorsed by Dropbox.

## Reproduce

See `deobfuscation/README.md`. Summary: build `harness4` against the client's
`libpython3.11.so.1.0`, run `driver4.py` (decrypt+export), then `transcode.py`
(→ stock pyc), then `pycdc` (→ source).
