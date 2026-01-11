# resumeyay

A multi-dimensional resume editor that reimagines resume editing through a "foldable matrix" paradigm.

## Overview

resumeyay treats your resume data as a flexible matrix where dimensions can be selectively collapsed, expanded, or dimmed. This enables focused editing on specific aspects of your resume while maintaining awareness of the whole document.

### Key Features

- **Columnar Focus Interface**: A matrix-based editor with 4 columns (Employer, Role, Metadata, Content) that can be independently collapsed or expanded
- **Focus Modes**: Four preset view configurations optimized for different tasks
- **Ghost Preview**: Live PDF-style preview that always shows the complete document
- **Style Studio**: Visual design controls completely separated from content editing
- **Keyboard-First Design**: Full keyboard navigation support for power users
- **Local Persistence**: Data saved automatically to browser localStorage

## Quick Start

```bash
# Install dependencies
bun install

# Start development server
bun run dev

# Build for production
bun run build

# Preview production build
bun run preview
```

## Focus Modes

| Mode | Shortcut | Use Case |
|------|----------|----------|
| **Full Matrix** | Cmd/Ctrl + 1 | Initial data entry, comprehensive review |
| **Narrative Focus** | Cmd/Ctrl + 2 | Writing accomplishment bullets, wordsmithing |
| **Timeline Focus** | Cmd/Ctrl + 3 | Reviewing career progression, checking dates |
| **Compact Review** | Cmd/Ctrl + 4 | High-level overview, space estimation |

## Keyboard Shortcuts

### Navigation
| Key | Action |
|-----|--------|
| Tab / Shift+Tab | Next/previous cell |
| Enter | Edit cell / New bullet |
| Escape | Exit edit mode |

### Bullet Editing
| Key | Action |
|-----|--------|
| Tab | Indent bullet |
| Shift+Tab | Outdent bullet |
| Cmd/Ctrl + Up/Down | Move bullet up/down |
| Backspace (empty) | Delete bullet |

### Application
| Key | Action |
|-----|--------|
| Cmd/Ctrl + 1-4 | Switch focus mode |
| Cmd/Ctrl + \ | Toggle preview |
| Cmd/Ctrl + Shift + S | Open Style Studio |
| Cmd/Ctrl + Z | Undo |
| Cmd/Ctrl + Shift + Z | Redo |

## Architecture

```
src/
  types.ts    - TypeScript type definitions for resume data, focus modes, and styles
  store.ts    - State management with undo/redo and localStorage persistence
  main.ts     - UI rendering and event handling
  style.css   - Complete styling with CSS custom properties
```

### Data Model

The resume is structured as:
- **Header**: Name, email, phone, location, links
- **Sections**: Experience, Education, Projects, etc.
- **Entries**: Organization, role, dates, location, content bullets
- **Content**: Hierarchical bullet points with unlimited nesting

### Focus Mode Mechanics

Each column has three possible states:
- **Expanded**: Full width, fully interactive
- **Collapsed**: Minimal width (24px), shows abbreviated content
- **Hidden**: Not rendered (unused in current implementation)

## Styling

The app uses CSS custom properties for easy theming:

```css
:root {
  --color-accent: #2563EB;
  --color-bg-primary: #FFFFFF;
  --color-text-primary: #1A1A1A;
  /* ... */
}
```

### Style Presets

Four built-in presets available in Style Studio:
- **Classic**: Serif fonts, traditional margins
- **Modern**: Clean sans-serif, tighter spacing
- **Minimal**: No dividers, compact layout
- **Dense**: Small fonts, maximum content density

## Browser Support

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## Tech Stack

- **Vite** - Build tool and dev server
- **TypeScript** - Type safety
- **Bun** - Package manager and runtime
- **html2pdf.js** - PDF export functionality

## Development

The application uses a simple reactive architecture:
1. Store holds all state
2. UI subscribes to store changes
3. User actions dispatch to store
4. Store updates and notifies subscribers
5. UI re-renders with new state

No external UI framework is used - just vanilla TypeScript with template literals for rendering.
