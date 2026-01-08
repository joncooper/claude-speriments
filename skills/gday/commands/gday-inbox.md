# Quick Inbox Check

Check the user's recent unread emails. Run this command:

```bash
gday mail list --unread -n 15
```

Then summarize the results:
- Total number of unread emails
- Who they're from and subjects
- Highlight any that look urgent or important

If there are no unread emails, let the user know their inbox is clear.

If authentication fails, guide them to run `gday auth login`.
