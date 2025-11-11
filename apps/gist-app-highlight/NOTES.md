# Implementation Notes

## Project Overview

**Sideshow** is a web app for creating annotated markdown documents that can be shared via short links. Think GitHub Gists meets Genius.com's annotation system.

## Architecture Decisions

### Why Firebase?

- **Firestore**: Document database, perfect for storing gists + highlights
- **Auth**: Built-in Google sign-in, no server needed
- **Free tier**: 1GB storage, 50K reads/day, 20K writes/day (plenty for personal use)
- **Client-side only**: No backend runtime required
- **Security rules**: Only creator can edit, everyone can view

### Why bun?

- **Speed**: 10-100x faster than npm (similar to Python's uv)
- **All-in-one**: Package manager + runtime + bundler + test runner
- **Modern**: Written in Zig, native TypeScript support
- **Compatible**: Drop-in replacement for npm/yarn/pnpm
- See: https://bun.sh

### Why Vite?

- Fast development server with HMR
- Optimized production builds
- Native TypeScript support
- Simple configuration
- Works great with bun

### Tech Stack

| Component | Choice | Why |
|-----------|--------|-----|
| Framework | Vanilla TS | Lightweight, no overhead for this use case |
| Build Tool | Vite | Fast, modern, great DX |
| Package Manager | bun | 10-100x faster than npm |
| Database | Firestore | Serverless, easy auth, free tier |
| Auth | Firebase Auth | Google sign-in, no backend needed |
| Markdown | marked.js | Fast, widely used, 30KB minified |
| Sanitization | DOMPurify | XSS protection for user content |
| Routing | Custom | Simple hash-based routing for SPA |

## Data Model

### Firestore Collection: `gists`

```typescript
interface Gist {
  id: string;              // Short ID (8 chars, e.g., "aB3xK9mQ")
  markdown: string;         // Raw markdown content
  createdBy: string;        // Firebase user ID
  createdAt: Timestamp;     // Creation timestamp
  updatedAt: Timestamp;     // Last update timestamp
  highlights: Highlight[];  // Array of highlights
}

interface Highlight {
  id: string;               // Unique highlight ID
  startOffset: number;      // Character offset in rendered HTML
  endOffset: number;        // End character offset
  selectedText: string;     // The highlighted text
  annotation: string;       // The sidenote content (markdown)
  color?: string;           // Optional highlight color
}
```

### Short Link Generation

- Use `nanoid` or similar to generate short IDs (8 chars)
- Check for collisions in Firestore
- URL format: `/docs/sideshow/{shortId}`

## Highlight Implementation

### Challenge: Persisting Text Selections

When a user selects text in the rendered markdown:
1. Use `window.getSelection()` to get the selection
2. Calculate character offsets in the rendered HTML
3. Store offsets + selected text in Firestore
4. On page load, recreate highlights using stored offsets

### Approach: Text Offset Method

```typescript
// When user selects text:
const selection = window.getSelection();
const range = selection.getRangeAt(0);
const startOffset = getTextOffset(container, range.startContainer, range.startOffset);
const endOffset = getTextOffset(container, range.endContainer, range.endOffset);

// Store: { startOffset, endOffset, selectedText }

// On page load:
// 1. Render markdown to HTML
// 2. For each highlight, find text at offsets
// 3. Wrap in <mark> elements with unique IDs
```

### Alternative Considered: DOM Path Method

Store the DOM path to the selection (e.g., `["div", "p:2", "span:1"]`).
**Rejected**: Fragile if markdown structure changes.

## Routing

Simple hash-based SPA routing:

- `/` or `/docs/sideshow/` → Homepage (list user's gists)
- `/#/create` → Create new gist
- `/#/edit/{id}` → Edit existing gist (auth required)
- `/#/{shortId}` → View gist (public)

## Security

### Firestore Rules

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /gists/{gistId} {
      // Anyone can read
      allow read: if true;

      // Only creator can write
      allow create: if request.auth != null;
      allow update, delete: if request.auth.uid == resource.data.createdBy;
    }
  }
}
```

### XSS Protection

- Use **DOMPurify** to sanitize all markdown output
- Sanitize user-provided annotations
- Configure marked.js to escape HTML by default

## UI/UX Decisions

### Edit vs Preview Mode

- **Edit mode**: Textarea for raw markdown (like GitHub)
- **Preview mode**: Rendered HTML with highlight functionality
- Toggle button at the top

### Highlight Workflow

1. User enters preview mode
2. User selects text with mouse
3. Popup appears: "Add annotation"
4. Modal/sidebar opens for annotation text
5. Highlight appears with color
6. Annotation shown in side pane

### Side Pane Layout

```
┌─────────────────────────────────────────────┐
│ [Edit] [Preview] [Save] [Share] [@user]     │
├──────────────────────────┬──────────────────┤
│                          │                  │
│  Markdown Content        │  Annotations     │
│  (70% width)             │  (30% width)     │
│                          │                  │
│  This is some text with  │  ┌────────────┐ │
│  a highlight here.       │  │ Highlight 1│ │
│                          │  │ This is... │ │
│  More content...         │  └────────────┘ │
│                          │  ┌────────────┐ │
│                          │  │ Highlight 2│ │
│                          │  │ Another...│ │
│                          │  └────────────┘ │
└──────────────────────────┴──────────────────┘
```

## Performance Considerations

### Markdown Rendering

- Cache rendered HTML in memory
- Only re-render on content change
- Use marked.js options for performance

### Firestore Queries

- Index on `createdBy` for user's gist list
- Use `.limit()` for pagination (future)
- Consider caching in localStorage

### Bundle Size

- Vite tree-shaking for unused code
- Lazy load Firebase modules
- marked.js is ~30KB, DOMPurify ~45KB
- Total bundle should be <200KB

## Development Workflow

```bash
# Start dev server
bun run dev

# Type checking
bun run build  # includes tsc

# Format code (future)
bun run format

# Deploy
bun run build
git add docs/sideshow
git commit -m "Deploy updates"
git push
```

## Testing Strategy

### Manual Testing Checklist

- [ ] Create gist with markdown
- [ ] Toggle edit/preview modes
- [ ] Select text and add highlight
- [ ] Add annotation to highlight
- [ ] Save gist
- [ ] Generate share link
- [ ] Open share link in incognito (no auth)
- [ ] Verify highlights and annotations visible
- [ ] Edit gist and verify updates
- [ ] Test on mobile viewport

### Future: Automated Tests

Could add:
- Unit tests for highlight offset calculations
- Integration tests with Firebase emulator
- E2E tests with Playwright

## Deployment

### GitHub Pages Setup

1. Vite configured to build to `/docs/sideshow/`
2. Set `base: '/docs/sideshow/'` in vite.config.ts
3. GitHub Pages serves from `/docs` directory
4. Access at: `https://username.github.io/repo/docs/sideshow/`

### Firebase Setup

1. Create project at console.firebase.google.com
2. Enable Firestore + Google Auth
3. Add web app, copy config
4. Create `src/firebase-config.ts` (gitignored)
5. Deploy security rules

## Known Issues / Limitations

1. **Highlight persistence**: If markdown is edited, offsets may break
   - **Solution**: Store highlights relative to markdown, not HTML
   - **Future**: Use more robust text anchoring

2. **Mobile support**: Text selection on mobile is tricky
   - **Solution**: Test extensively on iOS/Android
   - May need touch event handling

3. **Collaborative editing**: Not supported (by design)
   - Single creator per gist
   - No real-time updates

4. **Large documents**: May have performance issues with >10K highlights
   - **Solution**: Implement pagination or virtualization

## Future Considerations

See ICEBOX.md for full list of future enhancements.

## References

- [Vite Documentation](https://vite.dev)
- [Firebase Documentation](https://firebase.google.com/docs)
- [marked.js](https://marked.js.org)
- [bun Documentation](https://bun.sh/docs)
- [Window.getSelection() API](https://developer.mozilla.org/en-US/docs/Web/API/Window/getSelection)

## Session Context

- Created: November 2025
- Session ID: 011CV2WD7MdGvNPVrW9eRGoQ
- Branch: claude/gist-app-highlight-011CV2WD7MdGvNPVrW9eRGoQ
- Repository: claude-speriments
