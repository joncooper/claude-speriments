# /curate-context

Launch an interactive browser-based UI to curate context from multiple source files.

## Usage

```
/curate-context <file1> <file2> ... [fileN]
```

**Supported input formats:**

```bash
# Individual files
/curate-context notes.md requirements.pdf spec.docx

# Glob patterns
/curate-context docs/*.md research/*.pdf

# Directories (all readable files)
/curate-context @docs @research

# Mixed
/curate-context README.md @specs docs/*.pdf
```

## What This Command Does

When invoked, this command:

1. Reads all specified files (markdown, PDF, DOCX, text - any format Claude Code can read)
2. Expands directories and glob patterns to file lists
3. Launches a local web server with an interactive curation UI
4. Opens your browser to the curation interface
5. **Step 1 - File Picker**: Select which of the loaded files to curate (skip if only 1 file)
6. **Step 2 - Curation**: Highlight and select relevant portions from each file
7. Returns the curated context as markdown, ready to use

## Implementation Instructions

When the user invokes this command, follow these steps:

### Step 1: Expand Inputs to File List

Handle different input types:

**For `@directory` references:**
- List files in the directory
- Filter to readable formats (md, txt, pdf, docx, etc.)
- Read each file

**For glob patterns (`*.md`, `docs/**/*.txt`):**
- Expand the pattern using the Glob tool
- Read each matched file

**For individual files:**
- Read the file directly

### Step 2: Read All Source Files

For each file path:
- Use the Read tool to read the file content
- Claude Code natively handles PDF, DOCX, markdown, and text files
- Store each file's content with its filename (use relative path or just filename for display)

### Step 3: Generate the Curation HTML

Create a JSON object mapping filenames to their content:

```json
{
  "file1.md": "contents of file 1...",
  "document.pdf": "extracted text from PDF...",
  "notes.txt": "text file contents..."
}
```

Then generate the HTML by piping this JSON to the generator script:

```bash
cat <<'JSONEOF' | python3 /home/user/claude-speriments/skills/context-curation/server/generate_html.py \
  --output /tmp/context-curation-$$.html \
  placeholder
<JSON_CONTENT_HERE>
JSONEOF
```

Note: The `placeholder` argument is required but the actual files come from stdin JSON.

### Step 4: Start the Server

Start the curation server in the background:

```bash
python3 /home/user/claude-speriments/skills/context-curation/server/curation_server.py \
  --port 8765 \
  --html /tmp/context-curation-$$.html \
  --output /tmp/curated-output-$$.md &
```

Save the PID to kill it later.

### Step 5: Open the Browser

```bash
# macOS
open http://localhost:8765

# Linux
xdg-open http://localhost:8765 2>/dev/null || sensible-browser http://localhost:8765
```

### Step 6: Poll for Completion

Poll the /status endpoint every 2 seconds until done:

```bash
while true; do
  status=$(curl -s http://localhost:8765/status)
  if echo "$status" | grep -q '"done": true'; then
    break
  fi
  sleep 2
done
```

### Step 7: Read and Return the Curated Content

Once complete:
1. Read the output file: `/tmp/curated-output-$$.md`
2. Kill the server process
3. Clean up temp files
4. Return the curated markdown content to the conversation

## The UI Flow

### File Picker (if multiple files)

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

### Curation View

```
┌─────────────────────────────────┬─────────────────────────┐
│ [← Back] Source Files           │ Curated Context         │
│                                 │                         │
│ [notes.md] [spec.pdf]           │ 2 selections            │
│                                 │                         │
│ Lorem ipsum dolor sit amet...   │ ┌─────────────────────┐ │
│ ████████████████████████████    │ │ From: notes.md      │ │
│ █ Selected text appears here █  │ │ Selected text...    │ │
│ ████████████████████████████    │ │              [✕]    │ │
│                                 │ └─────────────────────┘ │
│                                 │                         │
│                                 │ [Clear All] [Done →]    │
└─────────────────────────────────┴─────────────────────────┘
```

## Example Output

The curated content will be formatted as:

```markdown
## From: meeting-notes.md

The key decision was to use React for the frontend...

## From: requirements.pdf

Users must be able to export data in CSV format.
The system should support up to 1000 concurrent users.

## From: architecture.md

The API layer uses GraphQL with Apollo Server...
```

This content is then ready to be passed to a sub-agent or used directly in prompts.
