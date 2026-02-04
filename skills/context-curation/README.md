# Context Curation Tool

A visual tool for curating context from multiple source files into a single, targeted markdown block for prompting.

**Status:** Initial Spike

## The Problem

When working with Claude Code, you often have many potentially relevant files—research papers, meeting notes, requirements docs, code files—but including everything creates noise. You need to surgically select just the relevant portions.

## The Solution

A browser-based highlighting interface that lets you:

1. **View** all your source files in one place
2. **Select** specific passages by highlighting (like a yellow highlighter)
3. **Accumulate** selections in a right-hand pane
4. **Export** curated context back to Claude Code

## Installation

Add this skill to your Claude Code settings:

```json
{
  "skills": [
    "/home/user/claude-speriments/skills/context-curation/commands"
  ]
}
```

Or use it directly by referencing the command file.

## Usage

```
/curate-context file1.md file2.pdf notes/*.txt
```

This will:
1. Read all specified files (supports markdown, PDF, DOCX, text)
2. Open a browser-based curation UI
3. Let you highlight and select relevant portions
4. Return the curated context to your Claude session

### The UI

```
┌─────────────────────────────────┬─────────────────────────┐
│ Source Files                    │ Curated Context         │
│                                 │                         │
│ [Tab: file1.md] [file2.pdf]     │ 0 selections            │
│                                 │                         │
│ Lorem ipsum dolor sit amet,     │ ┌─────────────────────┐ │
│ consectetur adipiscing elit.    │ │ From: file1.md      │ │
│ ████████████████████████████    │ │                     │ │
│ █ Selected text appears here █  │ │ Selected text...    │ │
│ ████████████████████████████    │ │              [✕]    │ │
│                                 │ └─────────────────────┘ │
│ Sed do eiusmod tempor...        │                         │
│                                 │ [Clear All]  [Done]     │
└─────────────────────────────────┴─────────────────────────┘
```

### Workflow

1. Click a file tab to view its contents
2. Click and drag to select text you want to include
3. Click "Add to Context" button that appears
4. Repeat for all relevant passages across all files
5. Click "Done — Send to Claude" when finished
6. The curated markdown appears in your Claude session

## Output Format

```markdown
## From: meeting-notes.md

The key decision was to use React for the frontend...

## From: requirements.pdf

Users must be able to export data in CSV format.
The system should support up to 1000 concurrent users.
```

## Architecture

```
skills/context-curation/
├── README.md                 # This file
├── commands/
│   └── curate-context.md     # Slash command definition
└── server/
    ├── curation_server.py    # HTTP server (serves UI, receives results)
    ├── curation_ui.html      # Browser UI template
    └── generate_html.py      # Generates HTML with embedded content
```

### How It Works

1. **Claude reads files** using native PDF/DOCX/markdown support
2. **generate_html.py** embeds file contents into the HTML template
3. **curation_server.py** serves the UI and handles the /done POST
4. **Browser** provides the highlighting/selection interface
5. **Claude polls** /status until the user clicks Done
6. **Curated content** is read from the output file and returned

## Requirements

- Python 3.8+
- A web browser
- No external dependencies (uses Python standard library only)

## Future Ideas

See [ICEBOX.md](./ICEBOX.md) for planned enhancements.
