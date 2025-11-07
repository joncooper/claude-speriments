# DBT Daily Logger - Feature Backlog

This document contains all planned features, enhancements, and ideas for the DBT Daily Logger app, organized by priority and category.

---

## 🔥 High Priority - From Previous TODO

### iCloud Sync
- [ ] Add `icloud_storage` package to pubspec.yaml
- [ ] Implement iCloud Drive sync for JSON data files
- [ ] Add background sync service
- [ ] Handle sync conflicts (last-write-wins or manual merge)
- [ ] Add sync status indicator in UI
- [ ] Test across multiple devices

**Packages needed:**
```yaml
dependencies:
  icloud_storage: ^2.1.0  # For iCloud Drive sync
```

**Implementation notes:**
- Store JSON data files in iCloud container
- Use file watching to detect changes
- Implement conflict resolution strategy
- Add offline-first functionality

### PDF Export
- [ ] Add `pdf` package for PDF generation
- [ ] Create PDF layout matching physical diary card exactly
- [ ] Support date range selection for export
- [ ] Add weekly skills grid to PDF
- [ ] Implement sharing via iOS share sheet
- [ ] Add email/print options

**Packages needed:**
```yaml
dependencies:
  pdf: ^3.10.0
  printing: ^5.11.0  # For native print dialog
  share_plus: ^7.2.0  # For sharing PDFs
```

**PDF Layout:**
- Header: Name, date range
- Daily entries table with all behaviors, emotions, sleep, meds
- Weekly skills grid at bottom
- Match physical card formatting exactly

### Analytics & Insights
- [ ] Trend graphs for emotions over time
- [ ] Skills usage heatmap
- [ ] Behavior patterns recognition
- [ ] Weekly/monthly summaries

---

## ⭐ New High-Impact Features

### 🔥 Streak System
**Goal:** Motivate consistent logging with visual streak tracking

- [ ] **Entry Streak**: Track consecutive days logging entries
  - Display fire emoji 🔥 with number on home screen
  - Prominent placement (top of home screen or badge)
  - Persist across app restarts

- [ ] **Skill Streak**: Days in a row using at least 1 DBT skill
  - Secondary streak indicator
  - Different color/icon (e.g., ⚡)

- [ ] **Sleep Streak**: Days meeting sleep goal (7+ hours)
  - Optional, can enable in settings

- [ ] **Self-Care Streak**: Days exercising or completing self-care activities
  - Customizable definition of "self-care"

- [ ] **Streak Milestones & Celebrations**
  - Celebrate at 7, 14, 30, 60, 100 days
  - Confetti animation or special badge
  - Encouraging messages ("You're on fire! 🔥")
  - Push notification for milestone achievements

- [ ] **Streak Recovery**
  - "Don't break the chain" warnings when streak at risk
  - Grace period (1 missed day = streak frozen, 2+ = broken)
  - Option to "freeze" streak once per month

**Data Model:**
```dart
class StreakData {
  int currentEntryStreak;
  int longestEntryStreak;
  DateTime? lastEntryDate;
  int currentSkillStreak;
  int freezesRemaining;
}
```

### 🎴 Swipeable Card Interface
**Goal:** Make emotion/behavior rating feel modern, fun, and intuitive

**Option A: Vertical Swipe Cards (Recommended)**
- [ ] Convert behaviors/emotions pages to full-screen card stack
- [ ] Swipe up/down to adjust intensity (0-5)
- [ ] Visual feedback: emoji grows/shrinks, color intensity changes
- [ ] Haptic feedback at each rating level
- [ ] Card "flies away" with animation when rating confirmed
- [ ] Progress dots at bottom (•••○○○ - 3 of 6 complete)
- [ ] Can tap emoji at bottom for quick selection (keeps current UX)
- [ ] Smooth page transitions with spring animations

**Implementation Details:**
- Use `PageView.builder` with vertical scroll
- `GestureDetector` for swipe detection
- Threshold-based rating (0-20% of swipe = 1, 21-40% = 2, etc.)
- Release gesture to lock in rating
- Auto-advance to next card after 300ms
- Can swipe left/right to go back to previous card

**Option B: Circular Dial/Wheel**
- [ ] Alternative: Rotary dial interface
- [ ] Swipe around circle to select intensity
- [ ] Emoji faces positioned around edge
- [ ] Stronger haptics than Option A

**Option C: Hybrid Approach**
- [ ] Keep current interface as default
- [ ] Add "Swipe Mode" toggle in settings
- [ ] Users can choose preferred input method

### 📊 Emotion Trends & Insights
**Goal:** Help users visualize patterns and progress over time

- [ ] **Line Chart for Emotions**
  - Show emotion intensity over last 7/14/30 days
  - Multiple lines (one per emotion) with color coding
  - Interactive: tap point to see that day's entry
  - Pinch to zoom time range

- [ ] **Weekly Summary Card**
  - "This week vs. last week" comparison
  - "You used 12 skills this week (+3 from last week)"
  - "Your average sleep: 7.2 hours"
  - Most-used skill of the week

- [ ] **Pattern Recognition**
  - "Anxiety tends to be higher on Mondays"
  - "You sleep better when you exercise"
  - "Using Mindfulness skills correlates with lower stress"
  - Optional ML-based insights (future)

- [ ] **Charts Package**
```yaml
dependencies:
  fl_chart: ^0.65.0  # Beautiful, customizable charts
```

### 🎯 Smart Skill Recommendations
**Goal:** Suggest relevant DBT skills based on current emotional state

- [ ] Context-aware suggestions on entry screen
  - "Feeling angry? Try: STOP, TIPP, or Opposite Action"
  - "High anxiety today? Consider: Paced Breathing, Self-Soothe"

- [ ] Skill diversity prompts
  - "You haven't used Mindfulness skills this week!"
  - "Try exploring Emotion Regulation today"

- [ ] Success-based recommendations
  - "TIPP helped you last time you felt this way"
  - Track which skills help with which emotions

- [ ] Daily skill suggestion on home screen
  - "Skill to focus on today: Wise Mind"
  - Rotates through categories
  - Can mark as "practiced" from home screen

**Algorithm:**
```dart
// Pseudocode
if (anger > 3) suggest(['STOP', 'TIPP', 'Opposite Action']);
if (anxiety > 3) suggest(['Paced Breathing', 'Self-Soothe', 'ACCEPTS']);
if (sadness > 3) suggest(['Accumulating ++', 'Opposite Action']);

// Check skill diversity
if (daysWithoutCategory('Mindfulness') > 3) nudge('Try Mindfulness');
```

### 🔔 Daily Check-in Reminders
**Goal:** Encourage consistent logging with gentle, customizable reminders

- [ ] Customizable reminder time
  - Default: 8:00 PM
  - Easy time picker in settings
  - Multiple reminders per day option

- [ ] Notification Styles
  - Gentle: "Time for your daily check-in 🌙"
  - Encouraging: "You're doing great! Ready to log today?"
  - Playful: "Your DBT diary misses you! ✨"
  - Streak-focused: "Keep that 7-day streak going! 🔥"
  - Rotate styles or let user choose

- [ ] Smart Scheduling
  - Don't notify if already logged today
  - Escalating reminders (if streak at risk)
  - Quiet hours (don't disturb during sleep)

- [ ] Local Notifications Package
```yaml
dependencies:
  flutter_local_notifications: ^16.0.0
```

---

## ⚡ Medium Priority Features

### 🏆 Achievements & Badges System
**Goal:** Gamify the experience and celebrate milestones

- [ ] Achievement Types
  - **Mindfulness Master**: Used 10 different mindfulness skills
  - **Week Warrior**: 7 days in a row logging
  - **Month Master**: 30 days in a row
  - **Century Club**: 100 days in a row
  - **Skill Explorer**: Used skills from all 4 categories
  - **Early Bird**: Logged before noon 5 times
  - **Night Owl**: Logged before bed 7 days
  - **Self-Care Champion**: 14 days exercising
  - **Sleep Star**: 7 days with 7+ hours sleep
  - **Emotion Expert**: Rated all 6 emotions 10 times

- [ ] Badge Display
  - Profile/stats screen showing all badges
  - Locked/unlocked states
  - Progress bars ("4/10 mindfulness skills used")
  - Celebration animation when earned

- [ ] Badge Notifications
  - Push notification when badge earned
  - Confetti on home screen
  - Share achievements option

### 📅 Mood Calendar View
**Goal:** Provide bird's-eye view of emotional patterns

- [ ] Month calendar with colored dots/indicators
  - Color based on overall mood (avg of emotions)
  - Size based on number of entries
  - Green = good day, yellow = mixed, red = difficult

- [ ] Quick navigation
  - Tap day to see full entry
  - Swipe between months
  - Jump to "today" button

- [ ] Visual patterns
  - Easy to spot "good weeks" vs "hard weeks"
  - See skill usage density
  - Identify gaps in logging

### 💡 Daily DBT Quote/Affirmation
**Goal:** Provide inspiration and education

- [ ] Quote database (50+ quotes)
  - DBT principles and wisdom
  - Dialectical thinking examples
  - Encouraging affirmations
  - Skill reminders

- [ ] Display on home screen
  - Rotates daily
  - Small card or banner
  - Option to share

- [ ] Favorites system
  - Heart icon to favorite quotes
  - View all favorites in separate screen
  - Repeat favorites more often

### 🎤 Voice Notes Feature
**Goal:** Faster, more natural note-taking for some users

- [ ] Record voice notes instead of typing
  - Tap and hold to record
  - Visual waveform while recording
  - Max 2-3 minutes per note

- [ ] Playback interface
  - Play/pause controls
  - Speed adjustment (1x, 1.5x, 2x)
  - Delete and re-record option

- [ ] Optional transcription
  - Use device speech-to-text
  - Display alongside audio
  - Can edit transcription

- [ ] Storage consideration
  - Audio files stored locally
  - Compressed format
  - Include in iCloud sync (if enabled)

### 🎨 Progress Celebrations
**Goal:** Positive reinforcement for completing entries and milestones

- [ ] Entry Completion Animation
  - Confetti or sparkle effect
  - Encouraging message: "Great job! ✨"
  - Sound effect (optional, can disable)

- [ ] Weekly Summary Celebration
  - Sunday evening: "You logged 6/7 days this week! 🎉"
  - Highlight improvements
  - Preview next week's goals

- [ ] Milestone Celebrations
  - Streak milestones (7, 14, 30, 100 days)
  - Total entries (10, 50, 100, 365 entries)
  - Skills mastery (used 20 different skills)
  - Special animations for big milestones

### 🚨 Crisis Plan Quick Access
**Goal:** Immediate support for moments of high distress

- [ ] Red emergency button on home screen
  - Always visible
  - "Crisis Support" or "Need Help Now?"

- [ ] Crisis Plan Screen
  - Pre-configured crisis contacts (therapist, parent, crisis line)
  - Quick-access crisis skills (TIPP, STOP, etc.)
  - Grounding exercises
  - Coping statements ("This will pass", "I am safe")

- [ ] One-tap actions
  - Call crisis contact
  - Text emergency support person
  - Start guided breathing exercise
  - View safety plan

- [ ] Warning numbers
  - National Suicide Prevention: 988
  - Crisis Text Line: Text HOME to 741741
  - Teen Line: 310-855-HOPE

**Privacy Note:** All crisis contacts stored locally, never uploaded

---

## 📋 Medium-Lower Priority Features

### 🎭 Emotion Wheel
**Goal:** Help identify specific, nuanced emotions

- [ ] Interactive emotion wheel interface
  - Inner ring: Basic emotions (anger, sadness, fear, joy)
  - Middle ring: More specific (frustrated, lonely, anxious, excited)
  - Outer ring: Very specific (betrayed, isolated, panicked, ecstatic)

- [ ] Tap to drill down
  - Start broad, get more specific
  - "I feel angry → frustrated → disappointed"

- [ ] Educational tool
  - Teaches emotion vocabulary
  - Helps with emotion identification skill

- [ ] Integration with entry
  - Can use wheel instead of standard 6-emotion list
  - Records specific emotion selected

### 🌙 Dark Mode
**Goal:** Eye-friendly evening logging

- [ ] Full dark theme
  - Dark backgrounds, light text
  - Reduced blue light
  - Softer colors

- [ ] Auto-switch based on time
  - Dark after 7 PM, light before
  - Or follow system setting

- [ ] Manual toggle in settings
  - User preference override
  - Remember choice

### 📸 Photo Journal (Optional)
**Goal:** Visual memories alongside entries

- [ ] Attach 1-2 photos per entry
  - "What made you smile today?"
  - Optional, not required

- [ ] Photo grid in entry detail
  - Thumbnail previews
  - Tap to expand

- [ ] Privacy considerations
  - Photos stored locally only
  - Not included in exports (unless explicitly requested)
  - Can delete photos without deleting entry

### 🙏 Gratitude Section
**Goal:** Evidence-based mood enhancement

- [ ] "3 Good Things" prompt
  - Optional page in daily entry
  - Text fields for 3 things
  - Research shows this helps mood

- [ ] Gratitude history
  - View past gratitudes
  - Random "memory" surfaced on home screen
  - Reinforces positive experiences

- [ ] Can disable in settings
  - Not everyone finds it helpful
  - Opt-in feature

---

## 🔧 Technical & Infrastructure

### Web View / Data Sharing
- [ ] Create read-only web view of entries
- [ ] Add shareable link generation (optional)
- [ ] Implement data export to JSON/CSV
- [ ] Add import from backup
- [ ] Privacy: ensure data is not uploaded to external servers
- [ ] Could use Firebase Hosting for optional cloud backup
- [ ] Local-first approach preferred

### Share with Therapist
- [ ] Export weekly summary as formatted PDF
- [ ] Include charts and graphs
- [ ] Privacy-protected
- [ ] Professional formatting for clinical use
- [ ] Option to exclude certain entries/notes
- [ ] Email or AirDrop sharing

### Anonymous Insights (Future/Advanced)
- [ ] Opt-in aggregated data
  - "Teens your age most commonly use TIPP"
  - "Peak stress time is 3-6pm"
  - All data anonymized

- [ ] Community features (very optional)
  - See how your patterns compare
  - "You're not alone" messaging
  - Never share personal data

- [ ] Research contribution
  - Contribute to DBT effectiveness research
  - Fully anonymous, IRB-approved
  - Opt-in only

### Customization Options
- [ ] Custom behaviors (beyond the standard list)
- [ ] Adjustable rating scales
- [ ] Theme customization (colors, fonts)
- [ ] Reminder notifications customization
- [ ] Show/hide certain sections
- [ ] Reorder entry pages

### Accessibility
- [ ] VoiceOver/TalkBack support
- [ ] High contrast mode
- [ ] Font size adjustment
- [ ] Haptic feedback options
- [ ] Screen reader optimization
- [ ] Keyboard navigation (if applicable)

### Technical Debt
- [ ] Add comprehensive unit tests
- [ ] Add integration tests for data sync
- [ ] Implement error handling and logging
- [ ] Add crashlytics (optional)
- [ ] Performance optimization for large datasets
- [ ] Code documentation
- [ ] Refactor repeated code

### Documentation
- [ ] User guide for parents/therapists
- [ ] Video tutorials
- [ ] Privacy policy
- [ ] Terms of use
- [ ] In-app help/tutorial
- [ ] FAQ section

---

## 💭 Ideas to Explore

### Skill Practice Reminders
- Random skill practice prompts during day
- "Time to practice Wise Mind for 2 minutes"
- Can snooze or dismiss
- Tracks completion

### Behavior Chain Analysis Tool
- Guided tool for analyzing behavioral sequences
- "What happened before? What was I feeling? What did I do?"
- Helps identify triggers and patterns
- Export analysis to share with therapist

### Mood Prediction
- ML model to predict mood based on sleep, skills, etc.
- "Based on your patterns, today might be tough - prepare!"
- Suggest pre-emptive coping strategies
- Very advanced, lower priority

### Social/Parent Integration
- Parent dashboard (with teen permission)
- See when entries logged (not content, unless shared)
- Crisis alerts to parent
- Weekly check-in prompts for both
- Careful balance of privacy and support

### Wearable Integration
- Import sleep data from Apple Watch
- Auto-track exercise
- Heart rate variability as stress indicator
- Automatic reminder based on stress levels

### Seasonal/Holiday Considerations
- Recognize high-stress periods (exams, holidays)
- Extra support during difficult seasons
- Countdown to events ("5 days until school break")
- Prepare coping plans in advance

---

## 📊 Implementation Priority Ranking

### Must-Have (Next Sprint)
1. **Streak System** - High motivation impact
2. **Daily Reminders** - Critical for consistency
3. **Basic Emotion Trends** - Users want to see progress

### Should-Have (Following Sprint)
4. **Swipeable Cards** - Major UX improvement
5. **Skill Recommendations** - Educational value
6. **Achievements/Badges** - Gamification boost
7. **Mood Calendar** - Visual overview

### Nice-to-Have (Future)
8. PDF Export
9. iCloud Sync
10. Dark Mode
11. Crisis Plan Quick Access
12. Voice Notes
13. Everything else

---

## 🎯 Success Metrics

How we'll know these features are working:

- **Engagement**: % of days with entries (target: 5+ days/week)
- **Retention**: % of users still logging after 30 days
- **Streaks**: Average streak length (target: 7+ days)
- **Skills Usage**: % of entries with skills logged
- **Skill Diversity**: Average # of different skills per week
- **Completion Rate**: % of started entries completed
- **Time to Complete**: Average time to complete entry (target: <3 min)

---

## 🗂️ Feature Categories Summary

- **Motivation & Engagement**: Streaks, Achievements, Celebrations
- **UX/UI Improvements**: Swipeable Cards, Dark Mode, Accessibility
- **Insights & Analytics**: Trends, Calendar, Pattern Recognition
- **Smart Features**: Skill Recommendations, Reminders, Quotes
- **Clinical Tools**: Crisis Plan, Emotion Wheel, Therapist Sharing
- **Data & Sync**: iCloud, PDF Export, Backup/Restore
- **Customization**: Themes, Custom Behaviors, Settings
- **Technical**: Testing, Performance, Documentation

---

**Last Updated:** 2025-11-07
**Version:** 1.0
