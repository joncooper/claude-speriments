# /curate-context

Launch an interactive browser-based UI to curate context from multiple source files.

## Usage

```
/curate-context <file1> <file2> ... [fileN]
```

You can also use glob patterns:
```
/curate-context docs/*.md research/*.pdf
```

## What This Command Does

When invoked, this command:

1. Reads all specified files (markdown, PDF, DOCX, text - any format Claude Code can read)
2. Launches a local web server with an interactive curation UI
3. Opens your browser to the curation interface
4. Waits for you to select the relevant portions of each file
5. Returns the curated context as markdown, ready to use

## Implementation Instructions

When the user invokes this command, follow these steps:

### Step 1: Read All Source Files

For each file path provided:
- Use the Read tool to read the file content
- Claude Code natively handles PDF, DOCX, markdown, and text files
- Store each file's content with its filename

### Step 2: Generate the Curation HTML

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
echo '<JSON_CONTENT>' | python3 /home/user/claude-speriments/skills/context-curation/server/generate_html.py \
  --output /tmp/context-curation-$$.html \
  placeholder
```

Note: The `placeholder` argument is required but the actual files come from stdin JSON.

### Step 3: Start the Server

Start the curation server in the background:

```bash
python3 /home/user/claude-speriments/skills/context-curation/server/curation_server.py \
  --port 8765 \
  --html /tmp/context-curation-$$.html \
  --output /tmp/curated-output-$$.md &
```

Save the PID to kill it later.

### Step 4: Open the Browser

```bash
# macOS
open http://localhost:8765

# Linux
xdg-open http://localhost:8765 2>/dev/null || sensible-browser http://localhost:8765
```

### Step 5: Poll for Completion

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

### Step 6: Read and Return the Curated Content

Once complete:
1. Read the output file: `/tmp/curated-output-$$.md`
2. Kill the server process
3. Clean up temp files
4. Return the curated markdown content to the conversation

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
