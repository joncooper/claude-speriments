---

## 9. Python layer: obfuscation scheme and de-obfuscation

The control plane is Python, shipped only as `.pyc` inside `python-pypkg.zip`
(3,628 modules) and run by a **modified CPython 3.11.14** (`libpython3.11.so.1.0`,
branch `dbx-desktop-v3.11.14`). Four independent protections, in load order:

1. **Custom pyc magic** `b7 34 0d 0a` (stock 3.11 = `a7 0d 0d 0a`). [OBS]
2. **Encrypted marshal payload.** Each `.pyc` is a PEP-552 hash-based header
   (`flags=0x01`, an 8-byte field that is a shared constant across most modules,
   not a per-file source hash) followed by an encrypted marshalled code object.
   Whole-body entropy ≈ 7.9–8.0 bits/byte including stdlib modules, so decryption
   is universal. [OBS] Decryption is wired into their patched
   **`PyMarshal_ReadObjectFromString`**: on their interpreter
   `marshal.loads(body[16:])` returns a live code object; on stock 3.11 the same
   bytes raise `ValueError: bad marshal data`. [OBS] Crypto primitives come from
   the statically-linked OpenSSL 3.5.5 (both AES and ChaCha20 present). The exact
   cipher and key are `[UNK]` — not required for de-obfuscation because the
   client's own interpreter performs the decryption (below). A same-length XOR of
   two equal-size modules does **not** cancel (5/153 zero bytes), ruling out a
   fixed-keystream XOR; the cipher is block- or per-file-keyed. [OBS]
3. **Permuted opcode numbering.** Opcode integers are renumbered by a fixed
   permutation; operand bytes and inline-cache layout are unchanged, and
   `CACHE`(0), `RESUME`(0x97), `STORE_NAME`(0x5a) are fixed points, while e.g.
   their `0x7d`→`LOAD_CONST`, `0x8e`→`LOAD_NAME`, `0x83`→`BINARY_OP`,
   `0x23`→`RETURN_VALUE`, `0x91`→`LOAD_CLASSDEREF`. [OBS] The full 108-opcode
   map was recovered (see below).
4. **Remapped marshal type codes** — not separately cracked; the oracle
   unmarshals for us.

### 9.1 De-obfuscation method (oracle + transcoder)

Build a C harness that embeds the shipped `libpython3.11.so.1.0`
(`Py_InitializeFromConfig` with `module_search_paths = [python-pypkg.zip,
python-pyext]`). Booting the interpreter at all exercises its decryptor (it loads
`encodings`/`codecs` from the encrypted zip). A controlled driver then reads each
module's raw bytes and calls `marshal.loads(body[16:])` — their patched marshal
**decrypts + deserializes without executing the module** — and exports each code
object as a plain tree.

The opcode permutation is recovered by compiling an identical ~170-file corpus on
both their interpreter and stock 3.11, aligning equal-length instruction streams,
and majority-voting `their_byte → opname` (zero conflicts; covers every opcode
used across all 3,628 modules). A host transcoder remaps each `co_code` opcode
byte (every even offset) `their → stock` and re-marshals to a standard 3.11
`.pyc`.

**Result:** all 3,628 modules transcoded to stock `.pyc` with 0 errors, readable
by any stock-3.11 `dis`/decompiler. Validated against ground truth: transcoded
`abc` disassembles correctly and its top-level API matches the genuine
`/usr/lib/python3.11/abc.py` (47/48 name overlap; the 1 diff is 3.11.14↔3.11.17
patch noise). Tooling: `oracle/` (harness + drivers + `opcode_map.json` +
`transcode.py` + README).

### 9.2 Python control plane (now readable) — key findings

With the payloads decrypted, the control-plane vocabulary that was previously
unreadable resolves (counts = occurrences in module string constants): `oauth`
464, `bolt` 828, `subscribe` 217, `host_id` 197, `host_int` 160, `nonce` 222,
`client_api` 294, `hostkey` 89, `access_token` 53, `refresh_token` 24,
`Dropbox-Host-Key` 3. [OBS] Recovered module structure, directly relevant to
session/transport:

- `apex/auth.py` → class **`OAuthClient`**, `retrieve_token_callback`,
  `_RETRIEVE_TOKEN_ID`, `_RETRIEVE_TOKEN_CONTEXTS`, `refresh_token`,
  `access_token` — the OAuth token client above the native `dbxauth` FFI. [OBS]
- `apex/http_client.py` → class **`HttpClient`**, `Response`/`ResponseHead`, and
  typed errors `ReceiverDropped`, `ClientInitiatedReconnect`, `Timeout`,
  `ProtocolError`, `InvalidHost`, plus `_error_from_response_proto`. [OBS]
- `apex/context.py` → the config tree `Config`/`ApexContext` with
  `DatabaseConfig`, `LoggingConfig`, `MetricsConfig`, `AnalyticsConfig`,
  **`StormcrowConfig`**, `AutoUpdaterConfig`, `HostInformation`, `force_http1`. [OBS]
- `apex/dbxconn.py` → class **`Connection`**. [OBS]

This confirms, at the Python level, that both the host-key and the OAuth
(`refresh_token`/`access_token`) credentials are managed here, and that the
device-link / `host_int` orchestration the native layer did not expose is in
these (now-readable) modules — recoverable as a follow-on by disassembling the
linking modules (`dropbox/client/**`, `apex/auth.py`, `dbxauth`).

---
