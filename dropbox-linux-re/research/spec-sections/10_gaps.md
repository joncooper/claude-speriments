---

## 10. Consolidated open questions (what a rebuild still needs to pin)

**Transport / wire**
- Exact HTTP/2 SETTINGS values Dropbox sends (initial window, max frame, max
  concurrent streams) — only the h2 parameter names are observed.
- DFC in-process frame header byte layout (length/flag/correlation-id) beyond
  "gRPC-over-framed-channel"; UDS handshake version and framing.
- gRPC max message size; whether gRPC-level message compression is ever
  negotiated (only identity/flag-0 evidenced); TLS cert-pinning policy
  (`disable-static-cert-pinning` flag exists; no pin literals found).
- Full `.proto` field numbers/layouts for `nsf.Nsf`, `fs_api.FsApi`,
  `dropbox_meta_engine.SyncEngineApi`, Bolt `SubscribeToBolt` — not in strings.

**Session / auth**
- `host_int` minting/derivation and the full device-registration/link handshake
  (now in the decrypted Python, not yet lifted).
- Per-request rule selecting `Dropbox-Host-Key` vs OAuth `Bearer`.
- OAuth client-authentication method at `/oauth2/token` (no client_id/secret
  literals at the token call).
- Exact value bound to `X-Dropbox-UID` (instance uid vs account_id); whether
  `machine_id` derives from `/etc/machine-id` vs `/var/lib/dbus/machine-id`.

**Endpoints**
- Resolved hostnames for `nsfserver` / `apiv2blockserver` (runtime-resolved);
  production block-server host (only `blockexcserver=dl-debug.dropbox.com`
  exception host observed). No literal port (443 inferred); no scheme field.

**Sync / blocks**
- Protobuf field numbers for `CommitRequest`, `ConsistentCutListPage`,
  `HlcLinearizedPage`, `SignedConsistentCutCursor`; HLC bit layout and the
  signature scheme over the cursor.
- Content block size (4 MiB is `[INF]`; a 1 MiB literal exists, 64 KiB rsync
  threshold observed); `block_hash` digest length (32 `[INF]`); exact rsync
  weak+strong hash algorithms; block-source try-order.

**Notifications**
- Bolt request Content-Type / GrpcV2 framing bytes; which header carries the
  Bolt bearer token; long-poll timeout and port; 3- vs 5-field
  `BoltChannelToken`; single multiplexed connection vs `use_separate_bolt`.

**Persistence / crypto**
- `.dbx` page-codec algorithm (cipher mode, reserve bytes, IV, per-page MAC) —
  compiled C, no SQLCipher pragmas; `database_key`/`user_key` derivation and the
  posix keystore file path/format/KDF/digest.
- Encrypted-folder/Vault: HPKE info/AAD, AES-256-GCM nonce derivation, how
  per-revision keys bind to block indices; where the client key pair / team-key
  fingerprint are persisted.
- The `.pyc` body **cipher and key** inside `libpython3.11.so.1.0` (a Ghidra
  pass on the patched marshal timed out; the oracle made it unnecessary for
  de-obfuscation but the primitive identity remains `[UNK]`).

## 11. Minimal rebuild checklist (interoperable client, own account/data)

1. TLS (OpenSSL/BoringSSL-class) + HTTP/2 client; gRPC framing
   `application/grpc+proto`, `grpc-status`/`grpc-message` trailers.
2. Account auth: obtain OAuth tokens and/or a host key; send `Dropbox-Host-Key`
   + `X-Dropbox-UID` (sync gRPC) or `Authorization: Bearer` (apiv2) with the
   `X-Dropbox-*` request headers (§5).
3. Server map (§6): dial `client.dropbox.com` (metaserver) for the sync gRPC
   services; `bolt.dropbox.com` for notifications; block servers via the routing
   tier; `api.dropbox.com` for apiv2.
4. Per-namespace sync loop (§9 of the sync section): subscribe (Bolt) → list
   (cursor delta) → commit/commit_ack, maintaining the Canopy tree + mount table.
5. Block layer (§block): content-hash files into blocks, `nsf.Nsf`
   `GetBlock/PutBlock` (+rsync `GetBlockSignature`/`*RsyncBlock`), blocklists,
   batched commit, local block cache.
6. Local state: SQLite (`nucleus.sqlite3`, `config.dbx`, …); the `.dbx` codec is
   the main unknown to replace or reimplement.

*End of specification. Sections 1–8 were authored by a parallel analysis fan-out
and independently verified; §9–11 and the corrections in the header were added
from the Python de-obfuscation and the verification pass.*
