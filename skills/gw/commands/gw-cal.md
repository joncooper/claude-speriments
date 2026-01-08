# Google Calendar Operations with gw

You have access to the `gw` CLI tool for Google Calendar operations. Use it to help the user manage their calendar.

## Available Commands

```bash
# List upcoming events
gw cal list                    # List next 10 events
gw cal list -n 20              # List next 20 events
gw cal list --days 30          # Events in next 30 days
gw cal list --calendar work    # Events from specific calendar
gw cal list --all-calendars    # Events from all calendars

# Quick views
gw cal today                   # Today's events
gw cal tomorrow                # Tomorrow's events
gw cal week                    # This week's events

# Show event details
gw cal show <event-id>         # Full event details

# Create events
gw cal create --title "Meeting" --start "2024-01-15 14:00" --end "2024-01-15 15:00"
gw cal create --title "Birthday" --date "2024-01-20" --all-day
gw cal create --quick "Lunch with John tomorrow at noon"
gw cal create --title "Team Sync" --start "2024-01-15 10:00" --location "Room 101" --attendees email1@company.com,email2@company.com

# Delete events
gw cal delete <event-id>

# Search events
gw cal search "meeting"
gw cal search "John" --days 90

# List all calendars
gw cal calendars
```

## Time Formats

When creating events, use these formats for --start and --end:
- `2024-01-15 14:00`
- `2024-01-15T14:00`
- `01/15/2024 14:00`

For all-day events, use --date with:
- `2024-01-15`
- `01/15/2024`

## Quick Add

The `--quick` flag uses natural language:
```bash
gw cal create --quick "Dinner with team on Friday at 7pm"
gw cal create --quick "Project deadline January 31st"
gw cal create --quick "1:1 with manager tomorrow 3-4pm"
```

## Working with Multiple Calendars

```bash
# List available calendars
gw cal calendars

# Use specific calendar
gw cal list --calendar <calendar-id>
gw cal create --calendar <calendar-id> --title "Event"
```

## Instructions

1. First, check authentication status: `gw auth status`
2. If not authenticated, guide user to run `gw auth login`
3. For viewing events, use the list/today/tomorrow/week commands
4. For creating events, confirm details before creating
5. Show event links when available for easy access

What would you like to do with Google Calendar?
