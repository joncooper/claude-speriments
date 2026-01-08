# Google Calendar Operations with gday

You have access to the `gday` CLI tool for Google Calendar operations. Use it to help the user manage their calendar.

## Available Commands

```bash
# List upcoming events
gday cal list                    # List next 10 events
gday cal list -n 20              # List next 20 events
gday cal list --days 30          # Events in next 30 days
gday cal list --calendar work    # Events from specific calendar
gday cal list --all-calendars    # Events from all calendars

# Quick views
gday cal today                   # Today's events
gday cal tomorrow                # Tomorrow's events
gday cal week                    # This week's events

# Show event details
gday cal show <event-id>         # Full event details

# Create events
gday cal create --title "Meeting" --start "2024-01-15 14:00" --end "2024-01-15 15:00"
gday cal create --title "Birthday" --date "2024-01-20" --all-day
gday cal create --quick "Lunch with John tomorrow at noon"
gday cal create --title "Team Sync" --start "2024-01-15 10:00" --location "Room 101" --attendees email1@company.com,email2@company.com

# Delete events
gday cal delete <event-id>

# Search events
gday cal search "meeting"
gday cal search "John" --days 90

# List all calendars
gday cal calendars
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
gday cal create --quick "Dinner with team on Friday at 7pm"
gday cal create --quick "Project deadline January 31st"
gday cal create --quick "1:1 with manager tomorrow 3-4pm"
```

## Working with Multiple Calendars

```bash
# List available calendars
gday cal calendars

# Use specific calendar
gday cal list --calendar <calendar-id>
gday cal create --calendar <calendar-id> --title "Event"
```

## Instructions

1. First, check authentication status: `gday auth status`
2. If not authenticated, guide user to run `gday auth login`
3. For viewing events, use the list/today/tomorrow/week commands
4. For creating events, confirm details before creating
5. Show event links when available for easy access

What would you like to do with Google Calendar?
