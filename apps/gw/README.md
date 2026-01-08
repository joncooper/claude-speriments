# gw - Gmail & Google Calendar CLI

A fast, single-binary CLI for accessing Gmail and Google Calendar from the terminal. Designed for developers, automation, and seamless integration with Claude Code.

## Features

**Gmail:**
- List, search, and read emails
- Send new emails and replies
- Download attachments
- Thread support
- Full Gmail search syntax

**Google Calendar:**
- List events across all calendars
- Quick views: today, tomorrow, week
- Create events with natural language
- Search and manage events
- Multi-calendar support

## Quick Start

### 1. Build

```bash
cd apps/gw
go build -o gw .
```

### 2. Set Up OAuth Credentials

You need to create OAuth2 credentials in Google Cloud Console:

1. Go to [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
2. Create a new project (or select existing)
3. Enable the **Gmail API** and **Google Calendar API**
4. Configure OAuth consent screen:
   - Choose "External" user type
   - Add your email as a test user
5. Create OAuth 2.0 Client ID:
   - Application type: **Desktop application**
   - Download the JSON file
6. Run `gw auth setup` and paste the JSON contents

### 3. Authenticate

```bash
gw auth login
```

This opens your browser for Google authentication. Token is cached at `~/.gw/token.json`.

### 4. Use

```bash
# Gmail
gw mail list              # Recent emails
gw mail list --unread     # Unread only
gw mail read <id>         # Read email
gw mail send --to user@example.com --subject "Hi" --body "Hello!"

# Calendar
gw cal today              # Today's events
gw cal week               # This week
gw cal create --quick "Lunch tomorrow at noon"
```

## Gmail Commands

### List Emails

```bash
gw mail list                    # List 10 recent emails
gw mail list -n 25              # List 25 emails
gw mail list --unread           # Only unread
gw mail list -q "from:boss"     # With search query
```

### Read Email

```bash
gw mail read <message-id>       # Read message
gw mail read <id> --raw         # Raw format
gw mail read <id> --mark-read   # Mark as read
gw mail thread <thread-id>      # Read full thread
```

### Search

```bash
gw mail search "from:alice@example.com"
gw mail search "subject:urgent is:unread"
gw mail search "has:attachment larger:5M"
gw mail search "after:2024/01/01 before:2024/02/01"
```

### Send Email

```bash
gw mail send --to user@example.com --subject "Hello" --body "Message"
gw mail send --to user@example.com --subject "Hello" --body-file msg.txt
echo "Message" | gw mail send --to user@example.com --subject "Hello" --body-stdin
gw mail send --to user@example.com --subject "Hello" --body "Hi" --cc other@example.com
gw mail send --to user@example.com --subject "Hello" --body "Hi" --draft  # Create draft only
```

### Reply

```bash
gw mail reply <message-id> --body "Thanks for your message"
gw mail reply <message-id> --body-file reply.txt
```

### Attachments

```bash
gw mail attachment <message-id>                  # List attachments
gw mail attachment <message-id> <attachment-id>  # Download one
gw mail attachment <message-id> --all            # Download all
gw mail attachment <message-id> --all -o ./downloads
```

### Labels

```bash
gw mail labels  # List all labels
```

## Calendar Commands

### View Events

```bash
gw cal list                 # Next 10 events
gw cal list -n 20           # Next 20 events
gw cal list --days 30       # Next 30 days
gw cal list --all-calendars # From all calendars

gw cal today                # Today's events
gw cal tomorrow             # Tomorrow's events
gw cal week                 # This week's events

gw cal show <event-id>      # Event details
```

### Create Events

```bash
# Specific times
gw cal create --title "Meeting" --start "2024-01-15 14:00" --end "2024-01-15 15:00"
gw cal create --title "Meeting" --start "2024-01-15 14:00"  # 1 hour default

# All-day events
gw cal create --title "Vacation" --date "2024-01-20" --all-day

# With location and attendees
gw cal create --title "Team Sync" --start "2024-01-15 10:00" \
  --location "Conference Room A" \
  --attendees alice@company.com,bob@company.com

# Natural language (Quick Add)
gw cal create --quick "Lunch with John tomorrow at noon"
gw cal create --quick "Project deadline January 31st"
gw cal create --quick "1:1 with manager Friday 3-4pm"
```

### Search and Delete

```bash
gw cal search "team meeting"
gw cal search "John" --days 90

gw cal delete <event-id>
```

### Calendars

```bash
gw cal calendars                          # List all calendars
gw cal list --calendar <calendar-id>      # Events from specific calendar
```

## Authentication Commands

```bash
gw auth setup    # Configure OAuth credentials
gw auth login    # Authenticate with Google
gw auth logout   # Clear cached token
gw auth status   # Check auth status
```

## Configuration

All configuration is stored in `~/.gw/`:

```
~/.gw/
├── credentials.json   # OAuth client credentials
└── token.json         # Cached access token
```

## Integration with Claude Code

This tool is designed to work with Claude Code through the `gw` skill:

```bash
# In Claude Code
/gw-mail     # Gmail operations
/gw-cal      # Calendar operations
/gw-inbox    # Quick inbox check
/gw-today    # Today's schedule
```

See `skills/gw/` for the Claude Code skill files.

## Gmail Search Syntax

The `gw` tool supports Gmail's full search syntax:

| Query | Description |
|-------|-------------|
| `from:user@example.com` | From specific sender |
| `to:user@example.com` | To specific recipient |
| `subject:keyword` | Subject contains keyword |
| `is:unread` | Unread messages |
| `is:starred` | Starred messages |
| `has:attachment` | Has attachments |
| `filename:pdf` | Has PDF attachments |
| `larger:5M` | Larger than 5MB |
| `smaller:1M` | Smaller than 1MB |
| `after:2024/01/01` | After date |
| `before:2024/02/01` | Before date |
| `older_than:7d` | Older than 7 days |
| `newer_than:1d` | From last day |
| `label:important` | Has label |
| `in:inbox` | In inbox |
| `in:sent` | In sent |

Combine with `AND`, `OR`, `NOT`, and parentheses:
```bash
gw mail search "(from:alice OR from:bob) AND is:unread"
```

## Building from Source

Requirements:
- Go 1.21 or later

```bash
git clone https://github.com/joncooper/claude-speriments
cd claude-speriments/apps/gw
go build -o gw .

# Install to PATH
sudo mv gw /usr/local/bin/
```

## License

MIT
