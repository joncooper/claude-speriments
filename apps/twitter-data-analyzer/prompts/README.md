# Audit Prompts

This directory contains the prompts used for profile auditing.

## Files

### `audit_system.md`

The main system prompt for analyzing tweets, likes, and bookmarks.

**Variables:**
- `{item_type}` - "tweet", "like", or "bookmark"
- `{items}` - The actual content to analyze

**Customization:**

You can edit this prompt to:
- Adjust sensitivity levels
- Add/remove categories
- Change severity thresholds
- Target specific industries
- Add custom guidelines

**Example Customizations:**

For tech industry:
```markdown
Additional considerations for tech profiles:
- Technical opinions and debates are OK
- Open source advocacy is OK
- Strong opinions on programming languages are OK
```

For finance industry:
```markdown
Additional considerations for finance profiles:
- Avoid ANY political content (even mild)
- Avoid discussions of specific stocks
- Avoid financial advice or market opinions
```

## Testing Prompts

After editing prompts, test with:

```bash
# Run audit on small sample
python -m twitter_analyzer.cli audit --no-likes --no-bookmarks

# Check audit_logs to see results
python -m twitter_analyzer.cli logs
```

## Prompt Engineering Tips

1. **Be specific** - Give clear examples of what to flag
2. **Set thresholds** - Define what's "high" vs "medium" severity
3. **Consider context** - Industry, role, company culture
4. **Iterate** - Review false positives and adjust
5. **Use examples** - Include specific examples in the prompt

## Version Control

Keep prompt versions in git:
```bash
git log prompts/audit_system.md
```

To revert to a previous version:
```bash
git checkout <commit> prompts/audit_system.md
```

## A/B Testing

To test different prompts:

1. Duplicate the prompt file
2. Edit the copy
3. Modify `profile_auditor.py` to use different prompt
4. Compare results in `audit_logs` table

## Future Prompts

We could add:
- `audit_following.md` - For analyzing following list
- `audit_bio.md` - For profile bio/description
- `audit_custom.md` - User-defined criteria
- Industry-specific variants
