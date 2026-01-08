# Gmail Operations with gday

You have access to the `gday` CLI tool for Gmail operations. Use it to help the user manage their email.

## Available Commands

```bash
# List recent emails
gday mail list              # List 10 recent emails
gday mail list -n 25        # List 25 recent emails
gday mail list --unread     # List only unread emails
gday mail list -q "query"   # Filter with Gmail search query

# Read an email
gday mail read <message-id>           # Read message by ID
gday mail read <message-id> --raw     # Show raw output
gday mail read <message-id> --mark-read  # Mark as read after viewing

# Read an email thread
gday mail thread <thread-id>          # Read all messages in thread

# Search emails
gday mail search "from:boss@company.com"
gday mail search "subject:urgent is:unread"
gday mail search "has:attachment larger:5M"

# Send an email
gday mail send --to user@example.com --subject "Hello" --body "Message text"
gday mail send --to user@example.com --subject "Hello" --body-file message.txt
echo "Message" | gday mail send --to user@example.com --subject "Hello" --body-stdin

# Reply to an email
gday mail reply <message-id> --body "Reply text"

# Download attachments
gday mail attachment <message-id>           # List attachments
gday mail attachment <message-id> --all     # Download all
gday mail attachment <message-id> <att-id>  # Download specific

# List labels
gday mail labels
```

## Gmail Search Syntax

The `gday mail search` and `gday mail list -q` commands support Gmail's search syntax:
- `from:sender@email.com` - From specific sender
- `to:recipient@email.com` - To specific recipient
- `subject:keyword` - Subject contains keyword
- `is:unread` / `is:read` - Read status
- `has:attachment` - Has attachments
- `larger:5M` / `smaller:1M` - Size filters
- `after:2024/01/01` / `before:2024/02/01` - Date filters
- `label:important` - By label

## Instructions

1. First, check authentication status: `gday auth status`
2. If not authenticated, guide user to run `gday auth login`
3. Use the commands above to help with the user's email task
4. When reading emails, show relevant details (from, subject, date, body)
5. When sending emails, confirm details before sending
6. Be helpful but respect user privacy - don't read more than necessary

What would you like to do with Gmail?
