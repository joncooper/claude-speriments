# Implementation Notes

## Design Decisions

### Why a Browser UI?

Claude Code runs in a terminal, but text selection/highlighting is fundamentally a visual, mouse-driven interaction. A browser provides:
- Native text selection with mouse
- Rich visual feedback
- No terminal UI library complexity
- Works on all platforms

### Why a Local Server?

The challenge is getting curated content back to Claude. Options considered:

1. **Clipboard** - User copies and pastes back
   - Rejected: Too much friction, error-prone

2. **File download** - Browser downloads, Claude reads
   - Rejected: Requires user to tell Claude when done

3. **Local server** - Browser POSTs to server, Claude polls
   - Selected: Seamless flow, no user intervention after clicking Done

### Single HTML File

The UI is a single HTML file with embedded CSS and JS. No build step, no dependencies. The source file content is injected as a JSON object at generation time.

### Python Standard Library Only

The server uses only Python's built-in `http.server`. This ensures it works everywhere Python is installed without `pip install`.

## Technical Notes

### Content Injection

The HTML template contains a placeholder:
```javascript
const SOURCE_FILES = __SOURCE_FILES_PLACEHOLDER__;
```

The generator replaces this with the actual JSON. This is simpler than:
- Fetching content via AJAX (would need CORS handling)
- Using a separate data endpoint (more server complexity)

### Port Selection

Currently hardcoded to 8765. Could add:
- Port detection to find available port
- Pass port back to Claude for polling

### Polling vs WebSocket

Polling /status every 2 seconds is simple and reliable. WebSocket would be more elegant but adds complexity for no real benefit (user takes at least 30+ seconds to curate).

## Lessons Learned

(To be filled in after testing and iteration)
