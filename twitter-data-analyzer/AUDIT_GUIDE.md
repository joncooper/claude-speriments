# Profile Audit Guide

The audit feature helps you identify potentially problematic content before making your Twitter profile public.

## What It Checks

The auditor analyzes your tweets, likes, and bookmarks for:

### Categories

1. **POLITICAL** - Political opinions, endorsements, partisan content
   - Party affiliations or criticisms
   - Political figure mentions
   - Policy debates

2. **CONTROVERSIAL** - Religion, divisive social issues, heated debates
   - Religious opinions
   - Hot-button social issues
   - Polarizing topics

3. **NSFW** - Adult/sexual content or references
   - Explicit content
   - Sexual references
   - Suggestive material

4. **PROFANITY** - Vulgar language, swearing
   - F-words, s-words, etc.
   - Crude language

5. **PERSONAL** - Oversharing personal information
   - Too much personal detail
   - Private information that shouldn't be public

6. **UNPROFESSIONAL** - Unprofessional tone or content
   - Rants and complaints
   - Unprofessional language
   - Overly casual tone

7. **OFFENSIVE** - Potentially offensive jokes or content
   - Jokes that could be misunderstood
   - Sarcasm without context
   - Potentially offensive humor

### Severity Levels

- **🔴 HIGH** - Should definitely review and likely delete
- **🟡 MEDIUM** - Probably should review and assess
- **🟢 LOW** - Minor concerns, use judgment

## Running the Audit

### Basic Usage

```bash
# Audit everything (recommended)
python -m twitter_analyzer.cli audit

# Audit only tweets
python -m twitter_analyzer.cli audit --no-likes --no-bookmarks

# Audit only likes
python -m twitter_analyzer.cli audit --no-tweets --no-bookmarks

# Export results to CSV
python -m twitter_analyzer.cli audit --export audit_results.csv
```

### What Happens

1. **Analysis** - Gemini analyzes your content in batches
2. **Categorization** - Each problematic item is categorized
3. **Scoring** - Assigned a severity level (HIGH/MEDIUM/LOW)
4. **Report** - Generates `audit_report.md` with details
5. **Export** - Optional CSV with all flagged items

## Understanding the Report

The audit generates `audit_report.md` with:

### Summary Section

```
Total Items Flagged: 45

By Severity:
- 🔴 HIGH: 12 items (should definitely review/remove)
- 🟡 MEDIUM: 23 items (probably should review)
- 🟢 LOW: 10 items (minor concerns)

By Type:
- Tweets: 15
- Likes: 25
- Bookmarks: 5

By Category:
- Political: 18
- Controversial: 12
- NSFW: 5
- Profanity: 8
- Unprofessional: 2
```

### Detailed Items

For each HIGH priority item:
- Tweet/Like ID
- Categories flagged
- Reason for flagging
- Full or partial text

For MEDIUM priority: First 10 shown

## CSV Export

The CSV export (`--export audit_results.csv`) includes:

| Column | Description |
|--------|-------------|
| Type | tweet, like, or bookmark |
| ID | Tweet ID number |
| Severity | high, medium, low |
| Categories | Comma-separated list |
| Reason | Why it was flagged |
| Text | Content (truncated to 500 chars) |
| Created At | When it was posted |

Use this CSV to:
- Sort by severity
- Filter by category
- Systematically review items
- Track what you've deleted

## Taking Action

### 1. Review the Report

```bash
# Read the full report
cat audit_report.md

# Or open in your editor
code audit_report.md
```

### 2. Browse Flagged Content

```bash
# Launch interactive browser
python -m twitter_analyzer.cli browse

# Search for specific topics
# Press '/' and type keywords like:
# - "politics"
# - "trump" or "biden"
# - Specific hashtags
# - Controversial terms
```

### 3. Delete Tweets

**Manual deletion:**
1. Go to twitter.com
2. Find tweet by searching or browsing
3. Click ⋯ → Delete

**Find your tweets:**
- The report shows tweet IDs
- URLs are: `https://twitter.com/username/status/TWEET_ID`

### 4. Unlike Tweets

**Manual unlike:**
1. Go to twitter.com/username/likes
2. Find the liked tweet
3. Click the heart to unlike

### 5. Remove Bookmarks

**Manual removal:**
1. Go to twitter.com/i/bookmarks
2. Find the bookmarked tweet
3. Click bookmark icon to remove

## Tips for Effective Auditing

### 1. Start with HIGH Priority

Focus on HIGH severity items first - these are most problematic.

### 2. Consider Context

Remember:
- What's the job/industry you're targeting?
- What's your company culture like?
- Regional/cultural differences matter

### 3. When in Doubt, Delete

If you're unsure whether something could be problematic, err on the side of caution.

### 4. Check Your Likes Carefully

Employers often look at likes as much as tweets. A like is an endorsement.

### 5. Look for Patterns

If you have many flagged items in one category (e.g., political), you might want to:
- Unlike all political content
- Search for specific politicians' names
- Remove all partisan hashtags

### 6. Update Following List

While not audited yet, consider:
- Political accounts you follow
- Controversial figures
- NSFW accounts
- "Muse" or similar accounts

You can check your following list manually at twitter.com/username/following

## Example Workflow

```bash
# 1. Run full audit with export
python -m twitter_analyzer.cli audit --export audit_results.csv

# 2. Review the report
cat audit_report.md | less

# 3. Browse interactively
python -m twitter_analyzer.cli browse
# Search for "trump", "biden", "politics", etc.

# 4. Open CSV in spreadsheet
# Sort by severity, review systematically

# 5. Delete tweets on Twitter
# Visit twitter.com and delete HIGH priority items

# 6. Re-run audit to check
python -m twitter_analyzer.cli audit

# 7. Verify your profile is clean
# Check twitter.com/username while logged out
```

## Privacy & API Usage

### Local Analysis

- All analysis happens on your machine
- Data sent to Gemini API for analysis only
- No data stored by Gemini
- Reports stay local

### Gemini API Limits

Free tier:
- 1,500 requests per day
- 15 requests per minute

With batch size of 20:
- Can analyze 300 items per minute
- 30,000 items per day

Should be plenty for most profiles!

## Limitations

### What It Can't Check

- **Following list** - Not fetched yet (coming soon)
- **Followers** - Can't control who follows you
- **Deleted tweets** - Only analyzes what's in your database
- **Media content** - Text analysis only (no image recognition)
- **Quote tweets** - Analyzes your text, not quoted content

### False Positives

The AI might flag:
- Neutral mentions of political terms
- Academic discussions
- Quoted text (if not clearly a quote)
- Sarcasm or satire

**Always review** flagged items yourself - the audit is a tool, not a final decision.

### False Negatives

The AI might miss:
- Subtle references
- Inside jokes
- Context-specific problems
- Dog whistles or coded language

**Manually review** your profile too, especially if targeting a specific industry.

## Advanced Usage

### Audit Specific Date Ranges

```bash
# Use SQL to filter
python -m twitter_analyzer.cli query "SELECT * FROM tweets WHERE created_at > '2020-01-01'"

# Then export and manually analyze
```

### Search for Specific Terms

```bash
# Find all tweets mentioning politics
python -m twitter_analyzer.cli query "SELECT text FROM tweets WHERE text LIKE '%politics%'"

# Find tweets with profanity
python -m twitter_analyzer.cli query "SELECT text FROM tweets WHERE text LIKE '%fuck%' OR text LIKE '%shit%'"
```

### Combine with TUI

```bash
# Browse and search interactively
python -m twitter_analyzer.cli browse

# Press '/' and search for:
# - Political figures' names
# - Controversial hashtags
# - Specific topics
```

## Future Enhancements

Coming soon:
- Bulk delete functionality
- Following list audit
- Automatic unlike/unbookmark
- Custom sensitivity levels
- Industry-specific audits (tech, finance, etc.)
- Local LLM support (no API needed)

## Troubleshooting

### "No problematic content found"

Either:
- ✅ Your profile is clean! (great!)
- ⚠️ False negative (review manually)
- ⚠️ Your content is subtle/coded

**Recommendation:** Still manually browse your profile.

### API Rate Limits

If you hit Gemini rate limits:
- Wait 1 minute
- Run audit in batches (--no-likes first, then --no-tweets)
- Reduce batch size (future option)

### Different Results on Re-run

AI analysis can vary slightly. If an item is borderline:
- Trust your judgment
- Err on the side of caution
- Consider the context

### High Priority Items That Seem Fine

Remember:
- Context matters
- Industry standards vary
- AI is conservative (better safe than sorry)

**You decide** what to keep or delete.

## Making Your Profile Public

After cleaning up:

1. **Final manual review**
   ```bash
   # Browse one more time
   python -m twitter_analyzer.cli browse
   ```

2. **Check while logged out**
   - Visit your profile in incognito mode
   - See what employers/others see

3. **Google yourself**
   - Search: `site:twitter.com your_username`
   - See what's indexed

4. **Update your profile**
   - Professional photo
   - Clean bio
   - No political hashtags in bio

5. **Make it public**
   - Settings → Privacy → Uncheck "Protect your posts"

## Questions?

Check the main docs:
- [README.md](README.md) - Full tool documentation
- [TUI_GUIDE.md](TUI_GUIDE.md) - Interactive browser guide
- [QUICKSTART.md](QUICKSTART.md) - Get started fast

---

**Good luck cleaning up your profile!** 🧹✨

Remember: Better safe than sorry when it comes to your professional presence online.
