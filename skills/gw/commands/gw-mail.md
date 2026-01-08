# Gmail Operations with gw

You have access to the `gw` CLI tool for Gmail operations. Use it to help the user manage their email.

## Available Commands

```bash
# List recent emails
gw mail list              # List 10 recent emails
gw mail list -n 25        # List 25 recent emails
gw mail list --unread     # List only unread emails
gw mail list -q "query"   # Filter with Gmail search query

# Read an email
gw mail read <message-id>           # Read message by ID
gw mail read <message-id> --raw     # Show raw output
gw mail read <message-id> --mark-read  # Mark as read after viewing

# Read an email thread
gw mail thread <thread-id>          # Read all messages in thread

# Search emails
gw mail search "from:boss@company.com"
gw mail search "subject:urgent is:unread"
gw mail search "has:attachment larger:5M"

# Send an email
gw mail send --to user@example.com --subject "Hello" --body "Message text"
gw mail send --to user@example.com --subject "Hello" --body-file message.txt
echo "Message" | gw mail send --to user@example.com --subject "Hello" --body-stdin

# Reply to an email
gw mail reply <message-id> --body "Reply text"

# Download attachments
gw mail attachment <message-id>           # List attachments
gw mail attachment <message-id> --all     # Download all
gw mail attachment <message-id> <att-id>  # Download specific

# List labels
gw mail labels
```

## Gmail Search Syntax

The `gw mail search` and `gw mail list -q` commands support Gmail's search syntax:
- `from:sender@email.com` - From specific sender
- `to:recipient@email.com` - To specific recipient
- `subject:keyword` - Subject contains keyword
- `is:unread` / `is:read` - Read status
- `has:attachment` - Has attachments
- `larger:5M` / `smaller:1M` - Size filters
- `after:2024/01/01` / `before:2024/02/01` - Date filters
- `label:important` - By label

## Instructions

1. First, check authentication status: `gw auth status`
2. If not authenticated, guide user to run `gw auth login`
3. Use the commands above to help with the user's email task
4. When reading emails, show relevant details (from, subject, date, body)
5. When sending emails, confirm details before sending
6. Be helpful but respect user privacy - don't read more than necessary

What would you like to do with Gmail?
