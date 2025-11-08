# Interactive Browser Guide (TUI)

The Twitter Data Analyzer includes a beautiful, interactive terminal user interface (TUI) for exploring your Twitter data with just your keyboard!

## What is the TUI?

The TUI (Text User Interface) is a full-screen terminal application that lets you browse, search, and explore your Twitter data interactively. It's built with [Textual](https://textual.textualize.io/), a modern Python framework for building rich terminal UIs.

## Launching the Browser

```bash
python -m twitter_analyzer.cli browse
```

## Interface Layout

```
┌─────────────────────────────────────────┬──────────────────┐
│ Search: [type to search...]             │ 📊 Statistics    │
├─────────────────────────────────────────┤                  │
│ Tweets | Likes | Bookmarks              │ Tweets: 1,234    │
├─────────────────────────────────────────┤ Likes: 5,678     │
│ Date       | Text           | ❤️ | 🔄 | 💬│ Bookmarks: 90    │
│ 2024-01-15 | Hello world... | 5  | 2  | 1│                  │
│ 2024-01-14 | Great post ... | 12 | 3  | 2│──────────────────│
│ 2024-01-13 | Check this ... | 3  | 1  | 0│ 📄 Tweet Details │
│ ...                                     │                  │
│                                         │ Text:            │
│                                         │ Hello world...   │
│                                         │                  │
│                                         │ Created: ...     │
│                                         │ Likes: 5         │
└─────────────────────────────────────────┴──────────────────┘
```

## Layout Components

### Left Panel (70% width)
1. **Search Bar** - Type to filter tweets/likes/bookmarks
2. **Tabs** - Switch between Tweets, Likes, and Bookmarks
3. **Data Table** - Scrollable list with arrow key navigation

### Right Panel (30% width)
1. **Statistics** - Overview of your data counts
2. **Details** - Shows full information for selected tweet

## Keyboard Navigation

### Essential Keys

| Key | Action |
|-----|--------|
| `↑` / `↓` | Navigate up/down in table |
| `PgUp` / `PgDn` | Scroll page up/down |
| `Home` / `End` | Jump to first/last row |
| `Enter` | Select current row |
| `Tab` | Next tab or widget |
| `Shift+Tab` | Previous tab or widget |
| `q` | Quit the application |

### Quick Navigation

| Key | Action |
|-----|--------|
| `t` | Jump to Tweets tab |
| `l` | Jump to Likes tab |
| `b` | Jump to Bookmarks tab |
| `/` | Focus search box |
| `Esc` | Clear selection / unfocus |

## Features

### 1. Browse Your Tweets

The Tweets tab shows:
- Date posted
- Tweet text (truncated)
- Like count (❤️)
- Retweet count (🔄)
- Reply count (💬)

Navigate with arrow keys, select a tweet to see full details.

### 2. Explore Your Likes

The Likes tab displays:
- Date of the liked tweet
- Tweet text
- Author ID

See what content you engage with most!

### 3. Review Bookmarks

The Bookmarks tab shows:
- Saved tweets
- When they were created
- Their authors

Perfect for reviewing content you saved for later.

### 4. Search and Filter

Press `/` to focus the search box, then type to filter:
- Searches through tweet text
- Real-time filtering
- Works across all tabs
- Press `Esc` to clear and return to navigation

**Examples:**
- Type `python` to find tweets about Python
- Type `AI` to find AI-related content
- Type `#hashtag` to find specific hashtags

### 5. View Details

Click (or press Enter) on any row to see:
- Full tweet text (not truncated)
- Exact timestamp
- All engagement metrics
- Language
- Additional metadata

The details panel updates instantly as you navigate.

### 6. Live Statistics

The stats panel always shows current counts:
- Total tweets in database
- Total likes
- Total bookmarks
- Following/followers count

## Tips & Tricks

### Efficient Browsing

1. **Use keyboard shortcuts** - Much faster than tabbing
   - `t`, `l`, `b` to switch tabs instantly
   - `/` to search without tabbing

2. **Search smart** - Search is case-insensitive and partial match
   - `machine learn` finds "Machine Learning"
   - `#ai` finds all AI hashtags

3. **Quick scan** - Use arrow keys to quickly browse
   - Hold `↓` to scroll through tweets
   - Watch the detail panel update in real-time

4. **Clear view** - Press `Esc` to clear selection and see more tweets

### Finding Interesting Content

**Most engaging tweets:**
1. Go to Tweets tab
2. Look at the engagement columns (❤️, 🔄, 💬)
3. High numbers = popular tweets

**Topics you care about:**
1. Go to Likes tab
2. Browse what you've liked
3. Use search to find patterns

**Saved for later:**
1. Go to Bookmarks tab
2. Review what you saved
3. Remember why you bookmarked it!

## Performance

The TUI is designed to be fast:
- Loads up to 1,000 most recent items per tab
- Instant search filtering
- Smooth scrolling
- Low memory usage

## Troubleshooting

### "Database not found"
Run `python -m twitter_analyzer.cli fetch` first to download your data.

### Weird characters or broken UI
Make sure your terminal supports UTF-8 and has a modern font installed.

### Search not working
Press `/` to focus the search box first, then type.

### Can't see full tweet
Select the row (click or press Enter) to see full details in the right panel.

### TUI crashes or freezes
- Try resizing your terminal window
- Make sure you have Textual installed: `uv pip install textual`
- Check your terminal supports full-screen apps

## Comparison: TUI vs CLI Commands

| Task | CLI Command | TUI Method |
|------|-------------|------------|
| View tweets | `query "SELECT ..."` | Press `t`, scroll with arrows |
| Search tweets | `query "... WHERE text LIKE ..."` | Press `/`, type search |
| View details | Not available | Select row |
| Browse likes | `query "SELECT * FROM likes"` | Press `l` |
| Switch views | Run new command | Press `t`, `l`, or `b` |
| See stats | `status` command | Always visible |

**TUI advantages:**
- Interactive exploration
- Real-time filtering
- Visual at a glance
- Fun to use! 🎉

**CLI advantages:**
- Scriptable
- Complex SQL queries
- Export data
- Batch operations

## Advanced: Mouse Support

The TUI also supports mouse!
- Click on tabs to switch
- Click on rows to select
- Scroll with mouse wheel
- Click in search box to focus

(But keyboard is faster! 😉)

## Exiting

Press `q` to quit anytime, or `Ctrl+C` for emergency exit.

Your database is never modified by the browser - it's read-only!

## Built With

- **[Textual](https://textual.textualize.io/)** - Modern Python TUI framework
- **[Rich](https://rich.readthedocs.io/)** - Beautiful terminal formatting
- **DataTables** - Scrollable, selectable tables
- **Reactive components** - Instant updates

## What's Next?

After browsing your data in the TUI, you might want to:

1. **Run analysis:**
   ```bash
   python -m twitter_analyzer.cli analyze tweets
   ```

2. **Ask questions:**
   ```bash
   python -m twitter_analyzer.cli ask "What patterns do I see?"
   ```

3. **Run custom queries:**
   ```bash
   python -m twitter_analyzer.cli query "SELECT text, like_count FROM tweets ORDER BY like_count DESC LIMIT 10"
   ```

4. **Export data:**
   Use SQL queries to export specific data to JSON/CSV

---

**Have fun exploring your Twitter data!** 📊✨

For more info:
- [README.md](README.md) - Full documentation
- [QUICKSTART.md](QUICKSTART.md) - 5-minute setup
- [Textual Docs](https://textual.textualize.io/) - Learn about TUI framework
