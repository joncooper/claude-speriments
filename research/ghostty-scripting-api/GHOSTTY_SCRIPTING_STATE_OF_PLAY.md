# Ghostty Scripting API: State of Play

**Last Updated:** December 2024
**Primary Discussion:** [#2353 - Scripting API for Ghostty](https://github.com/ghostty-org/ghostty/discussions/2353)
**Status:** Open feature request, labeled "feature-design" and "feedback-requested"
**Community Interest:** 148 reactions (133 upvotes), 91+ comments

---

## Executive Summary

Ghostty currently has **no scripting or automation API**. This is a significant gap compared to other terminal emulators like WezTerm, iTerm2, and Kitty. The community has been actively discussing this since October 2023, with various protocol proposals and one abandoned implementation attempt.

The maintainer (Mitchell Hashimoto) prefers a **simple text-based protocol** similar to Redis/memcached, but has not committed to a timeline. A partial implementation (PR #1701) was closed in December 2024 without merging due to unresolved design questions.

---

## Why This Matters

Users want to:
- **Open windows/tabs/splits programmatically** from scripts
- **Send commands to specific panes** (like running SSH in a particular tab)
- **Query terminal state** (get scrollback buffer, current command, etc.)
- **Integrate with editors** (Helix, Neovim) for live-grep and similar workflows
- **Automate environment setup** (scripts that create multi-pane layouts)
- **Build AI/MCP integrations** that can control terminal sessions
- **Set colors/themes dynamically** based on context (e.g., SSH to production = red background)

Without this, users are stuck with:
- GUI scripting hacks (AppleScript `keystroke`, `xdotool`)
- No scripting at all
- Staying on iTerm2/WezTerm/Kitty

---

## Competing Approaches Discussed

### 1. Simple Text Protocol (Maintainer's Preference)

Mitchell Hashimoto's stated preference (Nov 2023):

> I'm leaning towards a single-line text protocol in the format of memcached/redis/etc.

**Benefits:**
- Easy to debug via `telnet`
- Easy to build API clients for
- Fast to parse
- Can run over TCP or Unix sockets
- Can be secured with TLS or passwords

**Example usage:**
```bash
echo "ping" | nc localhost 9090
# Returns: PONG v=1.0.0
```

### 2. HTTP + JSON over Unix Sockets

Proposed by @jcollie:

```bash
curl --unix-socket $GHOSTTY_API_SOCKET http://localhost/v0/keybinds | jq
```

**Arguments for:**
- Every language has HTTP + JSON support
- No bikeshedding a new protocol
- curl/wget work from shell scripts

**Arguments against:**
- HTTP wasn't designed for Unix sockets
- Overhead may be unnecessary
- Opens door to overly complex API bodies

### 3. Escape Sequences (OSC)

Proposed by @RGBCube for SSH compatibility:

```bash
echo -e "\033]ghostty;background=#800000\a"
```

**Benefits:**
- Works over SSH
- No socket needed
- Could be standardized across terminal emulators

**Limitations:**
- One-way communication
- Limited to what escape sequences can express

### 4. Platform-Native APIs

Explored by @CosmicToast (Dec 2024):
- **macOS:** AppleScript / Shortcuts (Intents)
- **Linux:** D-Bus

**Findings:**
- AppleScript requires significant restructuring of window/tab management
- Shortcuts (Intents) are easier but more limited
- D-Bus rejected as primary option (not cross-platform)

### 5. Dynamically Linked Plugins (#1358)

Proposed by @LordMZTE:

```c
// Plugin loaded via dlopen
void ghostty_plugin_open(GhosttyAPI* api) {
    api->register_keybind("ctrl+shift+p", my_callback);
}
```

**Mitchell's response:**
> I'm a big fan of `dlopen`-ed plugins... I don't think these are mutually exclusive [with a network API].

This was **closed and consolidated into #2353**, but remains a potential future direction.

---

## PR #1701: The Abandoned Implementation

**Author:** @tale
**Status:** Closed December 22, 2024 (not merged)
**Lines of Code:** 566 additions across 10 files

### What It Did

Implemented a basic TCP server framework:

1. **Configuration options:**
   - `remote-tcp-socket = tcp://127.0.0.1:9090` or `unix:///tmp/ghostty.sock`
   - `remote-max-connections = 10`

2. **Architecture:**
   - Separate thread running a `libxev` event loop
   - Memory pools for completions, sockets, and buffers
   - Text-based command protocol

3. **Working functionality:**
   - TCP and Unix socket binding
   - Accept/reject client connections
   - Basic `ping` command returning `PONG v=<version>`

### Why It Stalled

The PR revealed several **unresolved design questions**:

#### 1. Authentication Model

@tale proposed:
```
remote-control-token = <token>:<command1>,<command2>,...
```

Questions raised:
- Per-command tokens vs. global token?
- TLS encryption vs. custom AES encryption?
- How to make it simple for shell scripts (telnet/netcat)?

#### 2. Socket Management

@gagbo asked:
- Should each Ghostty instance get its own socket?
- How is the socket path communicated to clients? (Environment variable?)
- Current design only supports one listening instance

#### 3. Command-to-Action Mapping

The PR only implemented `ping`. The bigger question:
- Should the API mirror the keybind `Action` enum exactly?
- How to handle actions that need arguments? (`resize_split:up,10`)
- Stateless commands vs. tracking surface/pane IDs?

#### 4. Thread Lifecycle

Code comment from the PR:
```zig
// TODO(tale): Stop flag? Only necessary if we support signaling the server
// from the main thread on an event, ie. configuration reloading.
```

Questions:
- What happens when config reloads and `remote-tcp-socket` changes?
- How to cleanly shutdown the TCP thread?

#### 5. Error Handling

Reviewer @matu3ba noted:
- TCP timeout handling for missing FIN from peer
- Unrecoverable errors should crash vs. thread teardown
- Current error handling is "pretty brittle"

### Technical Details of the Implementation

**Files added:**

| File | Purpose |
|------|---------|
| `src/tcp.zig` | Module root, exports Thread |
| `src/tcp/Thread.zig` | Thread initialization and main loop |
| `src/tcp/Server.zig` | TCP server wrapper, address parsing |
| `src/tcp/Command.zig` | Command parsing and dispatch |
| `src/tcp/commands/ping.zig` | The only implemented command |
| `src/tcp/handlers/connections.zig` | Accept/close handlers |
| `src/tcp/handlers/reader.zig` | Read/write handlers |
| `src/tcp/handlers/reject.zig` | Max-connections rejection |

**Key code patterns:**

```zig
// Address parsing (supports tcp:// and unix://)
pub fn parseAddress(raw_addr: ?[:0]const u8) BindError!std.net.Address {
    const uri = std.Uri.parse(addr) catch return BindError.InvalidAddress;
    if (std.mem.eql(u8, uri.scheme, "tcp")) {
        // Parse IP:port
    }
    if (std.mem.eql(u8, uri.scheme, "unix")) {
        // Parse socket path
    }
}

// Command dispatch
pub fn handle(self: Command, server: *Server) ![]const u8 {
    switch (self) {
        .ping => return ping(),
        // Future: .new_window, .new_tab, .send_text, etc.
    }
}
```

**The mailbox connection:**

The server held a reference to `App.Mailbox.Queue`, which would allow commands to dispatch actions to the main application. This was the intended bridge between the TCP protocol and Ghostty's internal action system, but was never utilized beyond initialization.

---

## Issue #1358: Plugin System Proposal

**Author:** @LordMZTE
**Status:** Closed, consolidated into #2353

### The Proposal

Load dynamic libraries (`.so`, `.dll`) from a config directory:

1. `dlopen` each library at startup
2. Call `ghostty_plugin_open` entry point
3. Plugins call into Ghostty's C-compatible API

### Mitchell's Response

> I'm a big fan of `dlopen`-ed plugins. They have their downsides (bugs in them can crash the hosting program) but they also have a ton of upsides like having very little performance penalty and as such being able to do a lot more that isn't quite possible with other plugin paradigms.

Key points:
- **Not mutually exclusive** with network API
- Network API is "lower bar, more familiar"
- In-process plugins can do things network APIs can't
- Needs **concrete use cases** to design properly

---

## How Other Terminals Solved These Design Problems

This section examines how Kitty, WezTerm, and iTerm2 actually implemented their scripting APIs, providing concrete answers to the design questions blocking Ghostty.

---

### Kitty: The Gold Standard for Terminal Remote Control

**Source:** [kitty/docs/rc_protocol.rst](https://github.com/kovidgoyal/kitty/blob/master/docs/rc_protocol.rst)

#### Protocol Format: JSON over Escape Sequences

Kitty uses **JSON wrapped in escape sequences**:

```
<ESC>P@kitty-cmd{"cmd":"ls","version":[0,14,2]}<ESC>\
```

**JSON structure:**
```json
{
    "cmd": "command name",
    "version": "[0, 14, 2]",
    "no_response": "Optional Boolean",
    "kitty_window_id": "Optional env var value",
    "payload": "Optional JSON object"
}
```

**Why this works:**
- JSON is universally parseable
- Escape sequence wrapper allows commands via TTY (works over SSH)
- Version field enables graceful degradation between client/server versions
- Can be tested with simple shell tools:
  ```bash
  echo -en '\eP@kitty-cmd{"cmd":"ls","version":[0,14,2]}\e\\' | socat - unix:/tmp/test
  ```

#### Authentication: Multi-Tiered Permission System

Kitty offers **four authentication levels**:

1. **Unrestricted** (`allow_remote_control=yes`): Any program can control kitty
2. **Socket-only** (`allow_remote_control=socket-only`): Only via explicit socket connection
3. **Password-based** (`remote_control_password`): Per-command token restrictions
   ```
   remote_control_password "mypass" *-colors get-*
   ```
   This password only allows color-related and get-* commands.
4. **Custom authorization**: Python script with `is_cmd_allowed()` function

**Encryption (v0.26.0+):**
- ECDH key exchange (X25519 curve)
- AES-256-GCM symmetric encryption
- Time-based nonce (±5 minute validity window)
- Public key exposed via `KITTY_PUBLIC_KEY` environment variable

#### Socket Management

- **Socket path:** Specified at launch with `--listen-on unix:/tmp/mykitty`
- **Discovery:** `KITTY_LISTEN_ON` environment variable in child processes
- **Per-instance:** Each kitty instance can have its own socket
- **Default:** Commands work via TTY when run inside a kitty window (no socket needed)

#### Window/Tab/Pane IDs

Kitty uses a **hierarchical model**:
- OS Window → Tabs → Windows (panes)
- Each has a numeric ID
- `KITTY_WINDOW_ID` environment variable available in shells
- Rich matching syntax: `--match title:"My Window"`, `--match id:43`, `--match cmdline:vim`
- Negative IDs count backwards (`-1` = most recent)

**Key insight:** The `kitten @` CLI wraps the protocol, so users don't need to construct JSON manually.

---

### WezTerm: Binary Protocol with TLS PKI

**Source:** [wez/wezterm codec/src/lib.rs](https://github.com/wez/wezterm/blob/main/codec/src/lib.rs), [wezterm-mux-server-impl/src/pki.rs](https://github.com/wez/wezterm/blob/main/wezterm-mux-server-impl/src/pki.rs)

#### Protocol Format: Binary PDUs with LEB128 Encoding

WezTerm uses a **custom binary protocol**, not text or JSON:

```rust
// Frame format:
// tagged_len: leb128  (u64 msb is set if data is compressed)
// serial: leb128
// ident: leb128
// data bytes (serde-serialized Rust structs)
```

**Why binary:**
- Optimized for high-frequency updates (terminal rendering)
- Compression support built-in
- Version-tagged enum variants for forward/backward compatibility
- Metrics collection (`pdu.encode.size`, `rpc.count`)

**Trade-off:** Harder to debug with telnet, but the CLI (`wezterm cli`) provides the human interface.

#### Authentication: Full TLS PKI

WezTerm implements **proper TLS with certificate authority**:

```rust
pub struct Pki {
    ca_cert: Certificate,
    pki_dir: PathBuf,  // ~/.config/wezterm/pki/
}
```

**On server start:**
1. Generate new CA certificate
2. Generate server certificate signed by CA
3. Store in `~/.config/wezterm/pki/`

**Client connection:**
1. Connect via "secure channel" (SSH or Unix socket) to request credentials
2. Server generates client certificate signed by CA
3. Client uses cert for TLS connection to mux server

**Key insight:** WezTerm separates the "get credentials" step (local/SSH) from the "use API" step (TLS). This is more complex than Kitty but supports true remote multiplexing.

#### Socket Management

WezTerm has **multiple connection modes**:

```rust
enum ClientDomainConfig {
    Unix(UnixDomain),      // Local Unix socket
    Tls(TlsDomainClient),  // Remote TLS connection
    Ssh(SshDomain),        // SSH tunnel
}
```

**Discovery:**
- CLI auto-discovers running GUI instance
- `--prefer-mux` flag to connect to background mux server
- `--class` flag to find specific GUI instance

#### Pane/Window IDs

- Numeric IDs for panes, tabs, windows
- `wezterm cli list` outputs JSON with all IDs
- Commands accept `--pane-id` arguments
- Output format selectable: `--format table` or `--format json`

---

### iTerm2: WebSocket + Protobuf with AppleScript Bootstrap

**Source:** [gnachman/iTerm2 api/library/python/iterm2/](https://github.com/gnachman/iTerm2/tree/master/api/library/python/iterm2/iterm2)

#### Protocol Format: Protobuf over WebSocket

iTerm2 uses **Protocol Buffers** over a **WebSocket** connection:

```python
# Connection endpoint
ws://localhost:1912
# Subprotocol
api.iterm2.com
```

**Why WebSocket + Protobuf:**
- Bidirectional streaming for notifications
- Strongly typed messages (protobuf schema)
- Python library handles all serialization

#### Authentication: AppleScript-Mediated Cookie Exchange

This is **unique and clever**:

1. **Initial auth via AppleScript:**
   ```applescript
   tell application "iTerm2" to request cookie and key for app named "MyScript"
   ```
2. iTerm2 prompts user: "Allow MyScript to control iTerm2?"
3. On approval, returns `cookie` and `key`
4. Script stores in environment: `ITERM2_COOKIE`, `ITERM2_KEY`
5. WebSocket connection includes these in headers:
   ```python
   headers = {
       "x-iterm2-cookie": cookie,
       "x-iterm2-key": key,
       "x-iterm2-advisory-name": script_name
   }
   ```

**Why this works:**
- User explicitly approves each script (security)
- Cookie persists across reconnections
- Script name shown in iTerm2 console for auditing
- Fallback: special file `~/Library/Application Support/iTerm2/disable-automation-auth` can disable prompts

#### Socket Management

**Fixed local WebSocket:**
- Always `ws://localhost:1912`
- No per-instance sockets
- Connection blocks until iTerm2 is available
- `it2run` helper script handles iTerm2 launch if needed

#### Session/Window/Tab IDs

```python
# Hierarchy
app.windows[0].tabs[0].sessions[0]

# ID types
window.id        # Numeric, for screencapture commands
session.id       # Numeric
session.unique_id # String, stable across restarts
tab.index        # Position in window (0-indexed)
```

---

### Summary: Design Decision Comparison

| Decision | Kitty | WezTerm | iTerm2 |
|----------|-------|---------|--------|
| **Protocol** | JSON in escape sequences | Binary (LEB128 + serde) | Protobuf over WebSocket |
| **Transport** | Unix socket or TTY | Unix socket, TLS, SSH | WebSocket (localhost:1912) |
| **Authentication** | Passwords + per-command ACL | TLS client certificates | AppleScript cookie exchange |
| **Socket discovery** | `KITTY_LISTEN_ON` env var | Auto-detect GUI/mux | Fixed port 1912 |
| **ID scheme** | Numeric + rich matching | Numeric IDs | Numeric + unique strings |
| **CLI wrapper** | `kitten @` | `wezterm cli` | Python library only |
| **Debug-friendly** | Yes (JSON + socat) | No (binary) | No (protobuf) |
| **SSH-friendly** | Yes (escape sequences) | Yes (SSH domain) | No (localhost only) |

---

### Transport Trade-offs: Socket-Only vs Escape Sequences

Kitty supports both socket-based control AND escape-sequence-based control. A socket-only approach (which aligns with Mitchell's stated preference for a text protocol over a socket) makes a deliberate trade-off.

**What socket-only provides:**

| Capability | Supported |
|------------|-----------|
| Local scripting and automation | ✓ |
| Editor/IDE integration | ✓ |
| GUI application control | ✓ |
| AI/MCP integrations | ✓ |
| External process control | ✓ |

**What socket-only excludes:**

| Capability | Excluded | Alternative |
|------------|----------|-------------|
| SSH → local terminal control | ✓ | Tunnel the socket, or use tmux |
| Zero-config in-terminal use | ✓ | Environment variable discovery |
| Container/sandbox without socket mount | ✓ | Mount the socket |
| Any stdout can control terminal | ✓ | **This is a security feature** |

**Why socket-only may be the right choice:**

1. **Clear boundaries** — Control plane is separate from the terminal byte stream
2. **Security by default** — Escape sequence control means any program writing to stdout can manipulate the terminal. Socket requires explicit access.
3. **Simpler implementation** — No parsing commands from the terminal stream

**The "SSH to production = red background" use case:**

This specific use case (echoing an escape sequence on SSH login to change local terminal color) cannot work with socket-only. Alternatives:
- Use tmux control mode (which Mitchell is actively building in #1935)
- SSH config with `LocalCommand` to run a socket command before connecting
- Accept this as out of scope

**Note:** Mitchell has not stated a position on escape sequence transport. The above is analysis of trade-offs, not his stated preference.

---

### Mitchell's Stated Positions

From the discussion, here's what Mitchell has **directly said**:

1. **Protocol preference:**
   > "I'm leaning towards a single-line text protocol in the format of memcached/redis/etc."

   Benefits he cited: telnet debugging, easy API clients, fast parsing, multiple transports, TLS/password security.

2. **Cross-platform requirement:**
   > "This needs to be cross platform. Additionally, I've found dbus pretty complicated to use compared to a simple text proto."

3. **Plugins not excluded:**
   > "I don't think these are mutually exclusive [network API and dlopen plugins]"

4. **No timeline commitment:**
   > "I'm not ready to commit to working on these yet."

### What We Can Infer from Other Terminals

1. **Authentication:** Kitty's tiered model is worth considering:
   - Default: socket-only (local security)
   - Optional: password with per-command restrictions
   - Encryption for password mode

2. **Socket management:**
   - Per-instance sockets with `GHOSTTY_SOCKET` environment variable
   - Unix sockets primary, TCP optional

3. **CLI wrapper:** Essential for adoption:
   - `ghostty ctl <command>` wrapping the socket protocol
   - Machine output (`--format json`) and human output (`--format table`)

---

## Community Use Cases

From the discussion, users want to:

1. **Environment Setup Scripts**
   > "I have elaborate AppleScripts for iTerm that set up my working environment with a lot of tabs for different remote hosts, and each tab has a horizontal split and a different command run in each of the panes." — @pjv

2. **Editor Integration**
   > "I find myself wanting to port stuff like this wezterm/helix integration to Ghostty" — @cryptocode

3. **Status Bar Integration**
   > "I have been using a similar interface to get the content of the active pane, read the last line of it, and display it in my status bar" — @bjesus

4. **AI/MCP Integration**
   > "Fair to assume this would be the answer to giving an AI agent terminal access via an MCP server for Ghostty?" — @binaryben

5. **Dynamic Theming**
   > "I often manually run `echo -e "\033]1337;SetColors=preset=Grass\a"` to make a particular window stand out" — @hartzell

6. **External App Integration**
   > "I use Fork as my main Git client, which has an 'Open Repo in Terminal' feature but doesn't recognise Ghostty" — @LukaHedtSV

---

## Current Workarounds

### macOS GUI Scripting

```applescript
tell application "System Events"
    keystroke "n" using command down  -- New window
    delay 0.1
    keystroke "echo hello"
    keystroke return
end tell
```

Problems:
- Fragile (breaks when UI changes)
- Slow (requires delays)
- No way to query state

### Protocol Handler (Limited)

Ghostty supports `ghostty://` URLs but functionality is limited.

---

## What Needs to Happen

Based on the discussion and analysis of other terminals, here are the decisions needed:

### 1. Protocol Format

**Options:**
- Text-based (Redis-like) — Mitchell's stated preference
- JSON — More structured, enables rich payloads
- JSON in escape sequences — Kitty's approach, works over SSH

**Recommendation:** Simple text protocol for requests, JSON for structured responses.

Mitchell's instinct is correct: Redis's RESP protocol handles everything Ghostty needs:
- Simple commands: `PING` → `+PONG`
- Arguments: `NEW_WINDOW cwd=/tmp command=bash`
- Arbitrary text: Length-prefixed bulk strings (`$12\r\nHello World!\r\n`)
- Structured responses: JSON only where needed (`LS` → `{"windows":[...]}`)

**Why NOT full JSON for everything:**
- Overkill for simple commands
- Harder to type in telnet
- More parsing overhead
- Kitty uses JSON because escape-sequence transport needs self-describing format; socket transport doesn't

**Example protocol:**
```
# Request (text)
NEW_WINDOW cwd=/tmp command=bash

# Response (simple)
+OK id=5

# Request for structured data
LS

# Response (JSON when needed)
{"windows":[{"id":1,"title":"dev"},{"id":2,"title":"ssh"}]}
```

### 2. Transport

**Options:**
- Unix socket only (secure, local)
- TCP optional (remote control)
- TTY escape sequences (in-terminal, SSH-friendly)

**Recommendation:** All three, following Kitty:
- Default: Unix socket with `GHOSTTY_SOCKET` environment variable
- Optional: TCP binding for remote control
- Bonus: Escape sequences work when running inside Ghostty (no socket config needed)

### 3. Authentication

**Options:**
- None (Unix socket permissions suffice)
- Single global token
- Per-command tokens with glob patterns
- TLS client certificates (WezTerm approach)

**Recommendation:** Tiered like Kitty:
- Level 1: `allow_remote_control=socket-only` (default, secure)
- Level 2: `remote_control_password "token" cmd1 cmd2` (restrict by command)
- Level 3: Encrypted mode for TCP (AES-GCM + time-based nonce)

### 4. Initial Command Set

Based on community use cases, minimum viable commands:

| Command | Purpose | Example |
|---------|---------|---------|
| `ls` | List windows/tabs/panes | Query current state |
| `new-window` | Create window | `--working-dir=/tmp --command=bash` |
| `new-tab` | Create tab | Same options as window |
| `send-text` | Send keystrokes | `--match id:5 "echo hello"` |
| `get-text` | Read scrollback | `--match id:5 --extent=screen` |
| `focus-window` | Switch focus | `--match title:"dev"` |
| `set-colors` | Change theme | `--match self background=#000` |

### 5. CLI Wrapper

**Essential for adoption.** Users shouldn't need to construct JSON manually.

```bash
# Example commands
ghostty ctl ls --format=json
ghostty ctl new-window --working-dir=/projects/foo
ghostty ctl send-text --match cmdline:vim ":w\n"
ghostty ctl get-text --match recent:0 | grep ERROR
```

### 6. Matching Syntax

Follow Kitty's proven approach:
- `--match id:123` — by window ID
- `--match title:"My Window"` — by title (regex)
- `--match cmdline:vim` — by running command
- `--match cwd:/home/user` — by working directory
- `--match recent:0` — most recent window
- `--match self` — current window (from `GHOSTTY_WINDOW_ID`)

---

## Proposed Implementation Path

Based on the analysis above, here's a concrete implementation path:

### Phase 1: Foundation (from PR #1701)
- Revive `libxev`-based socket server from PR #1701
- Add `GHOSTTY_SOCKET` environment variable
- Implement `ping` and `ls` commands
- Add `ghostty ctl` CLI wrapper

### Phase 2: Core Commands
- `new-window`, `new-tab`, `new-split`
- `send-text`, `get-text`
- `focus-window`, `focus-tab`
- `close-window`, `close-tab`

### Phase 3: Authentication
- `allow_remote_control` config option
- `remote_control_password` with glob patterns
- AES-GCM encryption for TCP mode

### Phase 4: Advanced Features
- Escape sequence transport (for SSH)
- Notifications (window created, closed, focused)
- Custom command registration (for plugins)

---

## Timeline

| Date | Event |
|------|-------|
| Oct 2023 | Discussion #2353 opened |
| Nov 2023 | Mitchell suggests text protocol |
| Jan 2024 | Plugin proposal #1358 consolidated |
| Apr 2024 | PR #1701 opened with TCP implementation |
| Aug 2024 | @tale steps back from PR due to time constraints |
| Dec 2024 | PR #1701 closed without merging |
| Dec 2024 | @CosmicToast explores AppleScript/Shortcuts |

**No timeline** has been provided for when this feature will be implemented.

---

## Conclusion

The Ghostty scripting API is a highly-requested feature with significant community interest but no clear path to implementation. The main blocker is not technical capability but **design decisions** that need to be made by the maintainer.

The abandoned PR #1701 provides a solid foundation if/when work resumes, but several architectural questions need answers first. Contributors interested in this feature should focus on:

1. Documenting concrete use cases
2. Proposing solutions to the authentication and socket management questions
3. Waiting for maintainer guidance on protocol format

---

## References

- [Discussion #2353](https://github.com/ghostty-org/ghostty/discussions/2353) - Main scripting API discussion
- [PR #1701](https://github.com/ghostty-org/ghostty/pull/1701) - Abandoned TCP implementation
- [Issue #1358](https://github.com/ghostty-org/ghostty/issues/1358) - Plugin system proposal
- [WezTerm CLI docs](https://wezfurlong.org/wezterm/cli/cli/index.html)
- [Kitty remote control](https://sw.kovidgoyal.net/kitty/remote-control/)
- [iTerm2 scripting](https://iterm2.com/documentation-scripting.html)
