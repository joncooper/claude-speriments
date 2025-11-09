# DBT Daily Logger - Roadmap

This document tracks the development roadmap for the DBT Daily Logger app, including completed work, planned features, experimental ideas, and long-term possibilities.

---

## ✅ Completed (Nov 7, 2025)

These features were implemented during the initial development session across two parallel branches.

### Core Functionality
- [x] Data model matching physical DBT diary card
- [x] Daily entry tracking with all behaviors/emotions
- [x] Weekly skills tracking structure
- [x] Fun, tween-friendly UI with swipe navigation
- [x] Emoji-based rating scales
- [x] Local data persistence (JSON in dbt-logger branch, Hive in flutter branch)
- [x] Entry history view with date organization
- [x] Edit/delete functionality for past entries
- [x] All 7 target behaviors with exact abbreviations from card
- [x] All 6 emotions from card with 0-10 intensity scales
- [x] Randomized order for behaviors and emotions (prevent sequencing bias)
- [x] Fixed cramped "Used DBT skills" scale - replaced with dedicated skills page
- [x] Detailed DBT skills checkboxes organized by category (all 4 modules)
- [x] Fixed async save operation to ensure data persists before screen closes
- [x] Debug logging for troubleshooting save/load flow
- [x] Improved emoji rating scale widget (handles scales with more values using Wrap)

### Advanced Features (flutter-daily-logging-app branch)
- [x] **Dark Mode**: Automatic theme switching with system preferences
- [x] **Material Design 3**: Modern, polished interface with animations
- [x] **Emotion Trends Charts**: Line graphs showing emotion intensity over time
- [x] **Urge Tracking Visualization**: Interactive charts for urge patterns
- [x] **Skills Usage Analytics**: Bar charts for most-used skills
- [x] **Time Range Selection**: 7/30/90 day views
- [x] **Interactive Calendar**: Heat map showing logging consistency
- [x] **Streak Tracking**: Current and longest streak display
- [x] **Confetti Celebrations**: Animations at milestones (every 7 days)
- [x] **Monthly Completion**: Progress ring for current month
- [x] **Interactive Emotion Wheel**: Circular, color-coded emotion picker
- [x] **Swipeable Skills Reference Cards**: Beautiful gradient cards with detailed explanations
- [x] **iCloud Sync Service**: Infrastructure for automatic backup (implemented but needs testing)
- [x] **PDF Export Service**: Generate professional reports (implemented but needs testing)
- [x] **Theme Service**: Persistent theme preferences

### Enhanced Tracking (dbt-daily-logger branch)
- [x] **Sleep Tracking**: Hours of sleep input with slider (0-12 hours)
- [x] **Sleep Quality Rating**: Emoji scale (0-5)
- [x] **Exercise Toggle**: Track physical activity
- [x] **Enhanced Sleep Page**: Better organization and UI
- [x] **Weekly Skills Grid**: Mon-Sun view of skills used each day
- [x] **Week Navigation**: Browse previous/next/current week
- [x] **Skills Reference Screen**: Detailed explanations of all DBT skills
- [x] **Color-Coded Categories**: Visual organization by module

---

## 📋 TODO - Planned Features

These are features we're definitely implementing, prioritized by importance.

### Critical: Branch Consolidation
- [ ] **Merge documentation** from both branches
  - Consolidate README (what we have)
  - Consolidate ROADMAP (this file)
  - Preserve all context about what was built
- [ ] **Decide on code strategy**: Merge branches OR rewrite from spec
- [ ] **Create final branch**: `dbt-daily-logger-wip-2025-11-08`
- [ ] **Unified feature set**: Combine best features from both branches
  - Sleep tracking + quality from dbt-logger
  - Charts/calendar/dark mode from flutter branch
  - Weekly skills grid from dbt-logger
  - iCloud/PDF from flutter branch

### High Priority: Complete Existing Features
- [ ] **Test iCloud Sync** end-to-end
  - Verify backup to iCloud
  - Test cross-device sync
  - Handle sync conflicts
  - Add sync status UI indicator
- [ ] **Test PDF Export** end-to-end
  - Verify PDF generation
  - Test share sheet integration
  - Ensure print functionality works
  - Match physical diary card layout
- [ ] **Verify All Data Persistence**
  - Test save/load for all field types
  - Ensure no data loss on app restart
  - Handle edge cases (empty entries, etc.)

### Medium Priority: Polish & UX
- [ ] **Remove medication pill icon** (💊) from home screen cards - looks weird
- [ ] **Unified Skills Reference**: Merge swipeable cards + weekly grid
  - Keep swipeable card UX from flutter branch
  - Add weekly grid view as separate tab
  - Integrate with main navigation
- [ ] **Consistent Navigation**: Ensure all features accessible from main menu
- [ ] **Error Handling**: Comprehensive error messages and recovery
- [ ] **Loading States**: Progress indicators for all async operations

### Data Integrity
- [ ] **Migration Path**: If consolidating to Hive, migrate JSON data
- [ ] **Backup/Restore**: Manual export/import for safety
- [ ] **Data Validation**: Ensure all inputs are validated
- [ ] **Storage Optimization**: Handle large datasets efficiently

---

## 🔬 SPIKE - Experiments & Unknowns

Features we need to prototype, test, or research before committing.

### SPIKE: Enhanced Input Methods
**Goal**: Make emotion/behavior rating more engaging and intuitive

**Options to Explore:**
1. **Vertical Swipe Cards** (from BACKLOG ideas)
   - Full-screen card stack
   - Swipe up/down to adjust intensity
   - Visual feedback (emoji grows/shrinks, colors change)
   - Haptic feedback at each level
   - Auto-advance after selection
   - **Question**: Does this feel better than sliders?
   - **Test**: Build prototype with 2-3 emotions

2. **Circular Dial/Wheel**
   - Rotary dial interface
   - Swipe around circle
   - Emoji faces on edge
   - **Question**: Intuitive or gimmicky?
   - **Test**: Quick mockup with one emotion

3. **Keep Current + Add Option**
   - Default to sliders (proven, works)
   - Add "Swipe Mode" toggle in settings
   - Users choose preference
   - **Question**: Worth the complexity?

**Decision Point**: After prototyping, pick ONE approach or add toggle

### SPIKE: Gamification & Motivation
**Goal**: Increase engagement without being cheesy

**Ideas to Test:**
- [ ] **Streak System** (detailed in BACKLOG)
  - Test: Does it actually motivate or just add pressure?
  - Prototype: Add simple streak counter, observe usage patterns
  - Consider: Grace periods, freeze system, different streak types

- [ ] **Achievements/Badges**
  - Test: Do they feel meaningful or annoying?
  - Prototype: 3-5 simple achievements
  - Examples: "7 day streak", "Used all 4 modules this week", "30 entries"

- [ ] **Streak Recovery System**
  - Test: Does forgiveness reduce pressure?
  - Options: 1-day freeze, makeup entries, grace periods

**Decision Point**: Validate with target users (teens/young adults in DBT)

### SPIKE: Smart Features & AI
**Goal**: Provide helpful suggestions without being intrusive

**Experiments:**
- [ ] **Skill Recommendations**
  - Based on current emotions: "Feeling angry? Try: STOP, TIPP"
  - Based on history: "TIPP helped you last time"
  - Based on gaps: "Haven't used Mindfulness this week"
  - **Question**: Helpful or annoying?
  - **Test**: Prototype with 3-5 simple rules

- [ ] **Pattern Recognition**
  - "Anxiety higher on Mondays"
  - "You sleep better when you exercise"
  - **Question**: Privacy concerns? Data requirements?
  - **Test**: Offline analysis only, start simple

- [ ] **Daily Skill Suggestion**
  - Rotate through skills
  - Quick-log from home screen
  - **Question**: Encourages practice or feels nagging?

**Decision Point**: Start conservative, add features based on feedback

### SPIKE: Notifications & Reminders
**Goal**: Encourage logging without being pushy

**To Explore:**
- [ ] Daily check-in reminder
  - User-configurable time (default 8 PM)
  - Gentle vs. persistent modes
  - Snooze functionality
- [ ] Adaptive timing
  - Learn when user typically logs
  - Adjust reminder time automatically
- [ ] Smart reminders
  - Only remind if haven't logged yet
  - Don't nag on weekends (optional)
  - Motivational messages vs. plain reminders

**Question**: What's the right balance between helpful and annoying?
**Test**: Start with simple daily reminder, gather feedback

---

## 🧊 ICEBOX - Future Possibilities

Long-term ideas we might implement someday, but not planned yet. Organized by theme.

### Insights & Analytics
- [ ] **Advanced Trend Graphs**
  - Correlation analysis: emotions vs. skills used
  - Behavior patterns by day of week
  - Compare time periods (this month vs. last month)
  - Predictive insights (using ML, future)

- [ ] **Weekly/Monthly Summaries**
  - Auto-generated progress reports
  - "This week vs. last week" comparisons
  - Most-used skill highlights
  - Goal achievement tracking

- [ ] **Skills Effectiveness Tracking**
  - Track which skills correlate with lower distress
  - Personal effectiveness ratings
  - Suggest skills based on past success

### Customization & Personalization
- [ ] **Custom Behaviors**
  - Beyond standard DBT list
  - User-defined target behaviors
  - Custom tracking for personal goals

- [ ] **Custom Emotions**
  - Add emotions beyond standard 6
  - Custom intensity scales
  - Emotion aliases (e.g., "stressed" = anxiety + pressure)

- [ ] **Theme Customization**
  - Custom color schemes
  - Accent color selection
  - Light/dark/auto modes with schedules

- [ ] **Adjustable Rating Scales**
  - 0-5 vs. 0-10 options
  - Simplified mode for younger users
  - Expert mode with more granularity

### Data & Sharing
- [ ] **Web Export / Sharing**
  - Read-only web view of entries
  - Shareable link generation (encrypted)
  - Therapist access portal (permission-based)

- [ ] **Advanced Export Formats**
  - CSV for data analysis
  - Excel with charts
  - Google Sheets integration
  - JSON backup/restore

- [ ] **Multi-Platform**
  - Android version
  - Web app for desktop
  - Apple Watch complications (quick logging)

### Social & Community (Careful!)
- [ ] **Anonymous Community Features**
  - Skill success stories (optional sharing)
  - Tips from other users
  - NO comparison or competition
  - Heavy moderation required

- [ ] **Therapist Integration**
  - Secure sharing with therapist
  - Collaborative goal setting
  - Therapist can add notes (with permission)
  - HIPAA compliance required

### Clinical Tools
- [ ] **Crisis Plan Quick Access**
  - Pre-loaded crisis plan
  - One-tap access during crisis
  - Emergency contacts
  - Grounding exercises

- [ ] **DBT Diary Card Wizard**
  - Guided setup matching therapist's card
  - Customizable sections
  - Print physical cards from app

- [ ] **Mindfulness Timer**
  - Guided meditations
  - Breathing exercises
  - Timer for practices

- [ ] **Voice Notes**
  - Audio journal entries
  - Voice-to-text for notes
  - Emotion detection from voice (research needed)

### Technical Infrastructure
- [ ] **Comprehensive Testing**
  - Unit tests for all models/services
  - Integration tests for data sync
  - UI/Widget tests
  - End-to-end testing

- [ ] **Performance Optimization**
  - Large dataset handling (years of entries)
  - Lazy loading for history
  - Database indexing
  - Memory optimization

- [ ] **Crashlytics & Analytics**
  - Error tracking (privacy-preserving)
  - Usage analytics (opt-in only)
  - Performance monitoring

- [ ] **Accessibility**
  - Full VoiceOver/TalkBack support
  - High contrast mode
  - Adjustable font sizes
  - Haptic feedback customization
  - Color blind friendly palettes

### Documentation & Support
- [ ] **User Guide**
  - In-app tutorial
  - Video walkthroughs
  - DBT basics explainer

- [ ] **Therapist/Parent Guide**
  - How to interpret data
  - What to look for in trends
  - Privacy settings guide

- [ ] **Legal**
  - Privacy policy
  - Terms of use
  - COPPA compliance (if targeting under-13)

---

## 🎯 Current Focus (Nov 2025)

**Immediate Next Steps:**
1. Consolidate documentation (this file + README)
2. Decide: Merge code or rebuild from spec?
3. Create unified branch with best features from both
4. Test iCloud sync and PDF export
5. Ensure all data persistence works correctly

**Short-term Goals (Next 2-4 weeks):**
- Stable, unified codebase on single branch
- All implemented features tested and working
- Clean gitignore (no build artifacts)
- Ready for daily use and user testing

**Medium-term Goals (1-3 months):**
- User testing with target audience (teens/young adults in DBT)
- Complete 2-3 SPIKE experiments
- Implement top-priority SPIKE results
- Polish UX based on feedback

---

## 📝 Notes on Development Approach

### Why Two Branches?
The initial development session (Nov 7, 2025) was conducted across multiple Claude Code environments (web + local), resulting in parallel development:

- **flutter-daily-logging-app**: Focus on polished UX (dark mode, charts, calendar)
- **dbt-daily-logger**: Focus on DBT fidelity (sleep quality, weekly skills grid)

Both branches share the same base app and core functionality but diverged on features. The consolidation effort aims to combine the best of both.

### Design Philosophy
- **DBT-first**: Stay true to the therapy framework
- **Privacy-focused**: All data local by default, cloud sync is optional
- **Teen-friendly**: Engaging UX without being childish
- **Therapist-approved**: Features that support clinical goals
- **Evidence-based**: Track what matters for DBT progress

### Target Users
- Teenagers and young adults (13-25) in DBT therapy
- Parents/guardians supporting DBT practice
- Therapists who recommend diary card tracking
- Anyone practicing DBT skills independently

---

**Last Updated**: 2025-11-08
**Status**: Branch consolidation in progress
**Next Review**: After code consolidation decision
