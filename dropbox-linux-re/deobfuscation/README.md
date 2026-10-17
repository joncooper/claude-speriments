# Dropbox Linux client — Python de-obfuscation toolchain

Reverses the four-layer protection on the client's bundled Python
(`libpython3.11.so.1.0` + `python-pypkg.zip`, Dropbox build 274.4.4905,
CPython branch `dbx-desktop-v3.11.14`). Static-analysis / interoperability study.
Produces stock CPython 3.11 `.pyc` for any standard 3.11 tool.

## The protection scheme (fully recovered)

1. **Custom pyc magic** `b7 34 0d 0a` (stock 3.11 is `a7 0d 0d 0a`).
2. **Encrypted marshal payload.** Each `.pyc` body is a marshalled code object
   whose bytes are encrypted; decryption is wired into their patched
   **`PyMarshal_ReadObjectFromString`** (proved: `marshal.loads(body[16:])` on
   *their* interpreter returns a code object; on stock 3.11 it fails
   "bad marshal data"). Crypto primitives come from the statically-linked
   OpenSSL 3.5.5; exact cipher/key not needed by this toolchain because their
   own interpreter performs the decryption.
3. **Permuted opcode numbering.** Opcode integers are renumbered by a fixed
   permutation (operand + inline-cache layout unchanged; `CACHE`=0, `RESUME`,
   `STORE_NAME` are fixed points). The full map (108 opcodes) is in
   `opcode_map.json` — recovered by compiling an identical corpus on both
   their interpreter and stock 3.11 and aligning instruction streams
   (zero conflicts; covers every opcode used across all 3628 modules).
4. **Remapped marshal type codes** — sidestepped: their interpreter unmarshals
   for us, so the tree is exported as live code objects, never parsed by hand.

## How it works (oracle + transcode)

`harness4` embeds *their* `libpython3.11.so.1.0`, boots it against the encrypted
zip (their decryptor runs to load stdlib), and runs a controlled driver. Driver
reads each `.pyc`'s raw bytes and calls `marshal.loads` (their patched version →
decrypts + unmarshals) to obtain a live code object **without executing any
module** (`marshal.loads` deserializes; it does not run code). Each code object
is exported as a plain tree (`all_trees.pkl`). The host transcoder remaps the
opcode bytes their→stock and re-marshals to a stock `.pyc`.

## Files
- `harness4.c` / `harness4` — embeds their libpython, runs a driver file.
- `driver4.py` — decrypt + export all modules to `out/all_trees.pkl`.
- `driver5.py` + `rare2.py` + `rare3.py` — opcode-map corpus compiler (their side).
- `opcode_map.json` — recovered their→stock opcode permutation.
- `transcode.py` — host-side: `out/all_trees.pkl` → `out/stockpyc/**.pyc`.
- `out/stockpyc/` — 3628 stock-3.11 `.pyc` (readable by `dis`, decompilers).

## Reproduce
```
D=<dist>/dropbox-lnx.x86_64-274.4.4905
gcc harness4.c "$D/libpython3.11.so.1.0" -I/usr/include/python3.11 -o harness4 -Wl,-rpath,"$D"
ORACLE_OUT=out ORACLE_ZIP="$D/python-pypkg.zip" ./harness4 driver4.py   # decrypt+export
python3.11 transcode.py                                                 # -> out/stockpyc/*.pyc
python3.11 -c "import marshal,dis;dis.dis(marshal.loads(open('out/stockpyc/apex/auth.pyc','rb').read()[16:]))"
```

## Validation
Transcoded `abc.pyc` disassembles to correct 3.11 bytecode and its top-level API
matches the genuine `/usr/lib/python3.11/abc.py` (47/48 name overlap; the 1 diff
is 3.11.14↔3.11.17 patch noise). All 3628 modules transcode with 0 errors.

## Scope / ethics
Interoperability + architecture understanding only. Do not redistribute the
decrypted Dropbox bytecode (it is Dropbox's copyrighted code). This toolchain is
original analysis code.
