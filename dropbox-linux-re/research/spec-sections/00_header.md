# Dropbox Linux Client — Reverse-Engineering & Rebuild Specification

**Target:** official Dropbox Linux desktop client **274.4.4905** (x86_64),
interpreter branch `dbx-desktop-v3.11.14`.
**Acquired:** `https://www.dropbox.com/download?plat=lnx.x86_64` →
`dropbox-lnx.x86_64-274.4.4905.tar.gz` (sha256 `c450ec3e…c727ec96a`).
**Method:** static analysis of the shipped binaries (native libs via strings +
embedded Rust source paths/panic messages + targeted disassembly) and
**de-obfuscation of the Python layer via the client's own interpreter used as a
decryption oracle** (§9). The client was never run as a product; no Dropbox
application module was executed (code objects were deserialized, not run).
**Purpose:** interoperability / architecture understanding.

**Evidence tags:** `[OBS]` observed string/symbol in a binary · `[INF]` inferred
from observed evidence + known behavior of a named vendored crate · `[UNK]` not
determined statically.

## Confidence & corrections (from an adversarial verification pass)

Each section below was authored from the evidence corpus and then independently
re-checked against that corpus. Net corrections applied to the first-pass text:

- **Session/auth:** `RegisterClient` is **EKMS encrypted-folder key enrollment,
  not device registration** — the host-key/`host_int` minting and the full device
  link handshake are **not** present in the native strings (they live in the
  now-decrypted Python layer, §9/§10). The posix keystore is a **file-based store
  (base64 + JSON + digest)**, not libsecret/gnome-keyring (no keyring backend
  strings exist). `Dropbox-Host-Key` vs OAuth `Bearer` per-request selection is
  `[INF]`. `ping_sfe` is `[INF]`; `bolt_subscribe`/`upload_block`/
  `commit_at_head`/`download_block` are `[OBS]`.
- **Transport:** `throttling_factor ∈ [MIN, 1.0]` is `[OBS]`; "server-driven" is
  `[INF]`. Exact HTTP/2 SETTINGS values and any TLS pin policy are `[UNK]`.
- **Endpoints:** the server map being **persisted** into the Apex config DB is
  `[INF]` (the DB and a "recreated the Apex database" log are `[OBS]`).
- **Sync:** real mount invariants are `mounted_nses ⊆ fileid_nses`,
  `mounted_nses ⊆ mountable_nses`, `fileid_nses ⊆ known_nses`. PNM forms are
  `EncryptedFileFilePNM`/`EncryptedFileDirectoryPNM` (no `EncryptedFilePNM`,
  no `DeviceInfoPNM`). `NeedBlocks{blocks:[…]}` is `[OBS]`; "hashes for upload"
  is `[INF]`.
- **Blocks:** the **4 MiB block size is `[INF]`** (no size literal found; a
  `1048576`/1 MiB literal and a 64 KiB rsync-delta threshold are observed);
  `block_hash` length 32 is `[INF]` from SHA-256.
- **Bolt:** `boltserver → bolt.dropbox.com` is an `[INF]` mapping (both tokens
  observed; it is the only bolt-named host).

Consolidated unknowns are in §10.

---
