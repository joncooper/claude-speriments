# gw - Gmail & Calendar Skill for Claude Code

A Claude Code skill that provides access to Gmail and Google Calendar through the `gw` CLI tool.

## Prerequisites

1. **Build the gw CLI tool** (if not already built):
   ```bash
   cd /path/to/claude-speriments/apps/gw
   go build -o gw .
   ```

2. **Add gw to your PATH** or install it:
   ```bash
   # Option 1: Copy to /usr/local/bin
   sudo cp gw /usr/local/bin/

   # Option 2: Add to PATH in your shell config
   export PATH="$PATH:/path/to/claude-speriments/apps/gw"
   ```

3. **Set up Google OAuth credentials**:
   ```bash
   gw auth setup
   ```
   Follow the prompts to configure your OAuth credentials.

4. **Login to Google**:
   ```bash
   gw auth login
   ```

## Available Commands

### `/gw-mail` - Gmail Operations
Read, send, search, and manage emails.

### `/gw-cal` - Calendar Operations
View, create, and manage calendar events.

### `/gw-inbox` - Quick Inbox Check
Check recent unread emails quickly.

### `/gw-today` - Today's Schedule
See today's calendar events at a glance.

## Usage Examples

```
/gw-mail             # Interactive mail operations
/gw-cal              # Interactive calendar operations
/gw-inbox            # Quick inbox summary
/gw-today            # Today's events
```

## Skill Installation

To use these commands in Claude Code, add the skill directory to your Claude Code configuration:

```json
{
  "skills": [
    "/path/to/claude-speriments/skills/gw"
  ]
}
```

Or copy the commands to your project's `.claude/commands/` directory.
