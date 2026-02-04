# Future Ideas

## UI Enhancements

- [ ] **Keyboard shortcuts** - Cmd+Enter to add selection, Cmd+Shift+Enter for done
- [ ] **Drag to reorder** selections in the curated pane
- [ ] **Edit selections** - Allow trimming or expanding after adding
- [ ] **Search within files** - Cmd+F to find text across all loaded files
- [ ] **Syntax highlighting** - For code files, show proper highlighting
- [ ] **Markdown preview** - Render markdown files as formatted HTML
- [ ] **Dark/light theme toggle** - Some users prefer light mode
- [ ] **Selection persistence** - Save state to localStorage in case of accidental close

## Workflow Enhancements

- [ ] **Templates** - Pre-defined curation patterns (e.g., "resume context", "code review context")
- [ ] **History** - Remember recent curation sessions for reuse
- [ ] **AI suggestions** - Highlight potentially relevant sections based on a query
- [ ] **Diff view** - Show what's selected vs what's not in each file
- [ ] **Export formats** - XML, JSON, or custom formats beyond markdown

## Technical Improvements

- [ ] **Auto port selection** - Find available port instead of hardcoding 8765
- [ ] **WebSocket** - Replace polling with WebSocket for instant completion detection
- [ ] **Progress indicator** - Show character/word count in curated pane
- [ ] **Large file handling** - Virtualized scrolling for very large files
- [ ] **Binary file preview** - Image thumbnails, PDF page previews

## Integration Ideas

- [ ] **MCP server** - Package as an MCP tool for broader use
- [ ] **VS Code extension** - Integrate directly into editor
- [ ] **Obsidian plugin** - Use with Obsidian vaults
- [ ] **CLI mode** - Non-interactive mode that accepts line ranges

## Content Processing

- [ ] **Smart chunking** - Suggest logical chunk boundaries (paragraphs, sections)
- [ ] **Deduplication** - Warn if selecting duplicate content
- [ ] **Token counting** - Show estimated token count for context window planning
- [ ] **Compression** - Optional summarization of selected content
