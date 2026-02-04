# Context Curation Tool

A visual tool for curating context from multiple source files into a single, targeted markdown block for prompting.

**Status:** Initial Spike

## The Problem

When working with Claude Code, you often have many potentially relevant files—research papers, meeting notes, requirements docs, code files—but including everything creates noise. You need to surgically select just the relevant portions.

## The Solution

A browser-based highlighting interface that lets you:

1. **Pick** which files to include from a visual grid (when multiple files)
2. **View** selected files in a tabbed interface
3. **Select** specific passages by highlighting (like a yellow highlighter)
4. **Accumulate** selections in a right-hand pane
5. **Export** curated context back to Claude Code

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

```bash
# Individual files
/curate-context notes.md requirements.pdf spec.docx

# Glob patterns
/curate-context docs/*.md research/*.pdf

# Directories (Claude Code @-references)
/curate-context @docs @research

# Mixed
/curate-context README.md @specs docs/*.pdf
```

This will:
1. Read all specified files (supports markdown, PDF, DOCX, text)
2. Open a browser-based curation UI
3. Let you pick which files to curate (if multiple)
4. Let you highlight and select relevant portions
5. Return the curated context to your Claude session

## The UI

### Step 1: File Picker (if multiple files)

When you load multiple files, you first see a grid to select which ones to curate:

```
┌─────────────────────────────────────────────────────────────┐
│         Select Files to Curate                              │
│                                                             │
│  [Select All] [Deselect All]          3 of 8 files selected │
│                                                             │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐            │
│  │ ☑ notes.md  │ │ ☐ draft.md  │ │ ☑ spec.pdf  │            │
│  │ 42 lines    │ │ 128 lines   │ │ 15 lines    │            │
│  │ Preview...  │ │ Preview...  │ │ Preview...  │            │
│  └─────────────┘ └─────────────┘ └─────────────┘            │
│                                                             │
│              [Continue to Curation →]                       │
└─────────────────────────────────────────────────────────────┘
```

### Step 2: Curation View

After selecting files, highlight text to add to your context:

```
┌─────────────────────────────────┬─────────────────────────┐
│ [← Back] Source Files           │ Curated Context         │
│                                 │                         │
│ [notes.md] [spec.pdf]           │ 2 selections            │
│                                 │                         │
│ Lorem ipsum dolor sit amet,     │ ┌─────────────────────┐ │
│ consectetur adipiscing elit.    │ │ From: notes.md      │ │
│ ████████████████████████████    │ │                     │ │
│ █ Selected text appears here █  │ │ Selected text...    │ │
│ ████████████████████████████    │ │              [✕]    │ │
│                                 │ └─────────────────────┘ │
│ Sed do eiusmod tempor...        │                         │
│                                 │ [Clear All]  [Done]     │
└─────────────────────────────────┴─────────────────────────┘
```

### Workflow

1. Pick which files to include (or skip if only 1 file)
2. Click a file tab to view its contents
3. Click and drag to select text you want to include
4. Click "Add to Context" button that appears
5. Repeat for all relevant passages across all files
6. Click "Done — Send to Claude" when finished
7. The curated markdown appears in your Claude session

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
4. **Browser** provides the file picker and highlighting/selection interface
5. **Claude polls** /status until the user clicks Done
6. **Curated content** is read from the output file and returned

## Requirements

- Python 3.8+
- A web browser
- No external dependencies (uses Python standard library only)

## Future Ideas

See [ICEBOX.md](./ICEBOX.md) for planned enhancements.
