# gday - Gmail & Calendar Skill for Claude Code

A Claude Code skill that provides access to Gmail and Google Calendar through the `gday` CLI tool.

## Prerequisites

1. **Build the gday CLI tool** (if not already built):
   ```bash
   cd /path/to/claude-speriments/apps/gday
   go build -o gday .
   ```

2. **Add gday to your PATH** or install it:
   ```bash
   # Option 1: Copy to /usr/local/bin
   sudo cp gday /usr/local/bin/

   # Option 2: Add to PATH in your shell config
   export PATH="$PATH:/path/to/claude-speriments/apps/gday"
   ```

3. **Set up Google OAuth credentials**:
   ```bash
   gday auth setup
   ```
   Follow the prompts to configure your OAuth credentials.

4. **Login to Google**:
   ```bash
   gday auth login
   ```

## Available Commands

### `/gday-mail` - Gmail Operations
Read, send, search, and manage emails.

### `/gday-cal` - Calendar Operations
View, create, and manage calendar events.

### `/gday-inbox` - Quick Inbox Check
Check recent unread emails quickly.

### `/gday-today` - Today's Schedule
See today's calendar events at a glance.

## Usage Examples

```
/gday-mail             # Interactive mail operations
/gday-cal              # Interactive calendar operations
/gday-inbox            # Quick inbox summary
/gday-today            # Today's events
```

## Skill Installation

To use these commands in Claude Code, add the skill directory to your Claude Code configuration:

```json
{
  "skills": [
    "/path/to/claude-speriments/skills/gday"
  ]
}
```

Or copy the commands to your project's `.claude/commands/` directory.
