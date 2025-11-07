# DBT Daily Logger - Future Enhancements

## Phase 2: Cloud Sync & Data Export (To be implemented later)

### iCloud Sync
- [ ] Add `icloud_storage` package to pubspec.yaml
- [ ] Implement iCloud Drive sync for Hive database
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
- Store Hive database file in iCloud container
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

### Web View / Sharing
- [ ] Create read-only web view of entries
- [ ] Add shareable link generation (optional)
- [ ] Implement data export to JSON/CSV
- [ ] Add import from backup

**Considerations:**
- Privacy: ensure data is not uploaded to external servers
- Could use Firebase Hosting for optional cloud backup
- Local-first approach preferred

## Phase 3: Additional Features (Nice to have)

### Analytics & Insights
- [ ] Trend graphs for emotions over time
- [ ] Skills usage heatmap
- [ ] Behavior patterns recognition
- [ ] Weekly/monthly summaries

### Customization
- [ ] Custom behaviors (beyond the standard list)
- [ ] Adjustable rating scales
- [ ] Theme customization
- [ ] Reminder notifications

### Accessibility
- [ ] VoiceOver/TalkBack support
- [ ] High contrast mode
- [ ] Font size adjustment
- [ ] Haptic feedback options

## Technical Debt
- [ ] Add comprehensive unit tests
- [ ] Add integration tests for data sync
- [ ] Implement error handling and logging
- [ ] Add crashlytics (optional)
- [ ] Performance optimization for large datasets

## Documentation
- [ ] User guide for parents/therapists
- [ ] Video tutorials
- [ ] Privacy policy
- [ ] Terms of use

---

## Current Implementation Status

### ✅ Completed (Phase 1)
- Data model matching physical diary card
- Daily entry tracking with all behaviors/emotions
- Weekly skills tracking structure
- Fun, tween-friendly UI with swipe navigation
- Emoji-based rating scales
- Local data persistence (switched to JSON from Hive for simplicity)
- Entry history view
- Edit/delete functionality

**Recent Session Completions:**
- ✅ All 7 behaviors with exact abbreviations from card (SI, NSSI, Family conflict, Isolate, Avoid/Procrast, Withhold, Subst. Use)
- ✅ All 6 emotions from card (Anger, Fear/Anxiety, Joy, Sadness, Guilt, Shame)
- ✅ Randomized order for behaviors and emotions to prevent sequencing bias
- ✅ Fixed cramped 0-7 "Used DBT skills" scale - replaced with dedicated skills page
- ✅ Added detailed DBT skills checkboxes organized by category
- ✅ Fixed async save operation to ensure data persists before screen closes
- ✅ Added debug logging for troubleshooting save/load flow
- ✅ Improved emoji rating scale widget to handle scales with more values (Wrap instead of Row)

### 🚧 In Progress / High Priority Next Steps

#### UI Polish & Bug Fixes
- [ ] Remove medication pill icon (💊) from home screen entry cards - it looks weird
- [ ] Verify home screen updates properly after saving entry (added debug logging)
- [ ] Test entry save/load flow end-to-end

#### Sleep & Self-Care Page Enhancements
- [ ] Add hours of sleep input (number picker or slider)
- [ ] Add sleep quality rating (0-5 scale)
- [ ] Add exercise toggle or rating
- [ ] Consider adding other self-care items from physical card

#### DBT Skills Reference Section
- [ ] Add "Skills Reference" button/section on home screen
- [ ] Create full-screen skill explainer views for each DBT skill
- [ ] Implement expandable detail view (triangle at bottom to expand beyond screen)
- [ ] Make it scrollable when expanded for longer skill descriptions
- [ ] Organize by category (Mindfulness, Emotion Regulation, etc.)

#### Weekly Skills Visualization
- [ ] Create weekly grid view showing which skills were used each day (Mon-Sun)
- [ ] Heatmap or checkbox visualization
- [ ] Match the layout from physical diary card
- [ ] Add to home screen or separate view

### 📋 Not Started
- iCloud sync (Phase 2)
- PDF export (Phase 2)
- Web sharing (Phase 2)
- Analytics (Phase 3)
