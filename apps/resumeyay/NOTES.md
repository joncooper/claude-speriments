# resumeyay - Implementation Notes

## Design Decisions

### No UI Framework

The app uses vanilla TypeScript with template literals for rendering. This keeps the bundle small and the code simple. The reactive pattern is:

1. Single store with all application state
2. Subscription-based re-rendering
3. Event delegation for handlers

For an app of this complexity, this approach works well. A framework would add complexity without proportional benefit.

### String-based Templates

HTML is generated as strings and assigned to innerHTML. While this isn't the most performant approach (full re-render on every change), it's simple and fast enough for this use case. The app never has more than a few hundred DOM elements.

### Local Storage Only

Data persistence uses localStorage for simplicity. There's no backend, authentication, or cloud sync. This keeps the app completely client-side and privacy-friendly.

### Focus Mode Implementation

Rather than having separate views, focus modes manipulate column widths and visibility using CSS flexbox. This enables smooth transitions between modes and maintains spatial consistency (elements don't jump around).

### Bullet Nesting

Content uses a recursive tree structure (ContentNode) that can nest arbitrarily deep. The PRD specifies three levels of bullet styling (bullet, circle, square), which we cycle through for deeper nests.

## Known Limitations

1. **No drag-and-drop for entries** - Would be nice for reordering
2. **Basic text editing** - No rich text (bold, italic, links) in bullets yet
3. **PDF export quality** - html2pdf.js has limitations; a server-side PDF generator would be better
4. **No import** - Can't import existing resumes from PDF/DOCX
5. **Single resume** - No way to have multiple resumes yet

## Performance Considerations

- Full DOM re-render on every change (acceptable for this app size)
- CSS transitions use transform/opacity where possible
- html2pdf.js loaded dynamically on first export

## State Management

The store uses a simple pub/sub pattern:
- `getState()` returns current state
- `subscribe(listener)` adds a listener
- Methods mutate state and call `notify()` to trigger re-renders

Undo/redo maintains a stack of resume snapshots (limited to 50 entries).

## CSS Architecture

Uses CSS custom properties extensively for:
- Colors
- Spacing
- Typography
- Column widths
- Transitions

This makes theming and adjustment easy. The Style Studio modifies these properties at runtime.

## Future Considerations

- Consider using a virtual DOM library if performance becomes an issue
- Could add IndexedDB for larger storage / multiple resumes
- WebRTC could enable real-time collaboration
- Server-side PDF generation would improve export quality
