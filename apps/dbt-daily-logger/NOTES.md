# DBT Daily Logger - Development Notes

## Project Status

**Current Branch**: `claude/dbt-daily-logger-rebuild-011CV4oEjM6dkW5m2vhdeSmn`
**Status**: ALL PHASES COMPLETE ✅ - Production Ready
**Last Updated**: 2025-11-12

---

## Quick Start for New Session

### Context
This is a **complete rebuild** of the DBT Daily Logger app. Two prototype branches were consolidated:
- `origin/claude/flutter-daily-logging-app-011CUtTzsT7fGYSFYvSaDR8b` - UX features (dark mode, charts, calendar)
- `origin/claude/dbt-daily-logger-011CUu7pwHC8TurHgPToBdVz` - DBT features (sleep quality, weekly grid)

**Decision**: Rebuild from scratch with Firebase backend (not merging code)

### Why Firebase?
- Multi-platform support (iOS + web UI planned)
- Automatic cloud sync across devices
- Offline-first with automatic sync
- Free tier sufficient for personal use
- Simplifies future web UI development

### What to Read First
1. **README.md** - Feature overview from both prototype branches
2. **SPEC.md** - Complete technical specification
3. **ROADMAP.md** - What's built, what's planned (✅ Completed / 📋 TODO / 🔬 SPIKE / 🧊 ICEBOX)

---

## Build Progress

### Phase 1: Foundation ✅ COMPLETE
- [x] Initialize Flutter project with Firebase
- [x] Set up Firebase project structure (requires user to complete in Console)
- [x] Configure iOS app scaffolding (GoogleService-Info.plist needed from user)
- [ ] Configure web app (future)
- [x] Implement authentication (anonymous initially)
- [x] Create data models (DiaryEntry, UserProfile, DBTSkills)
- [x] Set up Firestore service layer
- [x] Implement basic navigation structure
- [x] Create documentation (QUICKSTART.md, FIREBASE_SETUP.md)

### Phase 2: Core Features ✅ COMPLETE
- [x] Daily entry form
  - [x] Emotions slider (6 types, 0-10 scale, randomized order)
  - [x] Urges tracker
  - [x] Target behaviors (7 types, randomized order)
  - [x] DBT skills selector (all 4 modules, organized checkboxes)
  - [x] Sleep tracking (hours, quality 0-5, exercise checkbox)
  - [x] Medication checkbox
  - [x] Notes field
- [x] Save entry to Firestore
- [x] Entry list view (home screen)
- [x] Entry detail view
- [x] Edit existing entry
- [x] Delete entry

### Phase 3: Enhanced Features ✅ COMPLETE
- [x] Dark mode + theme persistence
- [x] Weekly skills grid (Mon-Sun visualization)
- [x] Skills reference screen with search
- [x] Settings screen with account management

### Phase 4: Polish ✅ COMPLETE
- [x] Loading states
- [x] Error handling
- [x] Empty states
- [x] Animations

---

## Reference Branches

These branches remain available for reference during rebuild:

### flutter-daily-logging-app (remote only)
```bash
# View files from this branch
git show origin/claude/flutter-daily-logging-app-011CUtTzsT7fGYSFYvSaDR8b:dbt_daily_logger/lib/screens/calendar_screen.dart

# Reference for:
# - Dark mode implementation
# - Charts/insights screens
# - Calendar with streaks
# - Emotion wheel widget
# - iCloud sync service
# - PDF export service
# - Theme service
```

### dbt-daily-logger (remote only)
```bash
# View files from this branch
git show origin/claude/dbt-daily-logger-011CUu7pwHC8TurHgPToBdVz:dbt_daily_logger/lib/screens/weekly_skills_screen.dart

# Reference for:
# - Sleep quality tracking
# - Weekly skills grid
# - Simple skills reference screen
# - JSON storage approach
```

**Do NOT merge these branches** - use as reference for patterns/UX only.

---

## Architecture Decisions

### Storage: Firebase Firestore
- **Chosen over**: Hive (local-only), JSON files (manual sync)
- **Rationale**: Multi-platform, automatic sync, offline support built-in
- **Structure**: Users collection → entries subcollection
- **Security**: Firestore rules enforce user isolation

### Authentication: Firebase Auth
- **Start with**: Anonymous authentication (low friction)
- **Future**: Email authentication with account linking
- **Privacy**: Each user's data isolated by userId

### State Management: Provider
- **Simple, proven pattern**
- **AuthProvider**: Manages auth state
- **EntriesProvider**: Manages diary entries from Firestore

### UI Framework: Material Design 3
- **Native Flutter widgets**
- **Dark mode support built-in**
- **Consistent with prototype UX**

---

## Key Design Patterns

### Data Model
```dart
class DiaryEntry {
  final String id;
  final String userId;
  final DateTime date;
  final Map<String, int> emotions;     // 6 emotions, 0-10 scale
  final Map<String, int> urges;
  final Map<String, int> behaviors;    // 7 behaviors
  final List<String> skillsUsed;       // DBT skill IDs
  final double? sleepHours;
  final int? sleepQuality;             // 0-5 scale
  final bool? exercised;
  final bool? tookMedication;
  final String? notes;
  final DateTime createdAt;
  final DateTime updatedAt;
}
```

### Firestore Structure
```
users/
  {userId}/
    profile/
      - settings
    entries/
      {entryId}/
        - date, emotions, urges, behaviors, skillsUsed, etc.
```

### Screen Flow
```
AuthWrapper
├── LoginScreen (if not authed)
└── MainScreen (if authed)
    ├── HomeScreen (entry list) - default
    ├── NewEntryScreen
    ├── EntryDetailScreen
    ├── WeeklySkillsScreen
    ├── SkillsReferenceScreen
    └── SettingsScreen
```

---

## Firebase Setup Checklist

When starting implementation:

1. **Create Firebase Project**
   - Go to console.firebase.google.com
   - Create new project: "dbt-daily-logger"
   - Enable Google Analytics (optional)

2. **Add iOS App**
   - Bundle ID: `com.example.dbtDailyLogger` (or custom)
   - Download GoogleService-Info.plist
   - Place in `ios/Runner/`

3. **Enable Firestore**
   - Start in test mode initially
   - Apply security rules from SPEC.md
   - Create composite index for entries query

4. **Enable Authentication**
   - Enable Anonymous provider
   - Enable Email/Password (future)

5. **Flutter Setup**
   ```bash
   flutter pub add firebase_core firebase_auth cloud_firestore
   flutterfire configure
   ```

---

## Important Implementation Notes

### Randomization
- **Behaviors and emotions must be randomized** on each form load
- Prevents sequencing bias in responses
- Seed randomization per-session (not per-question)

### Offline Support
- Firestore handles offline caching automatically
- Writes queue when offline, sync when online
- No additional offline logic needed
- Test with airplane mode on simulator

### Security Rules
```javascript
// In Firebase Console
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId}/{document=**} {
      allow read, write: if request.auth != null
                         && request.auth.uid == userId;
    }
  }
}
```

### Testing Strategy
1. Test on iOS simulator first
2. Verify offline mode (airplane mode)
3. Test across two devices/users for sync
4. Test data persistence after app restart

---

## DBT Skills Reference

Complete list organized by module (from physical diary card):

**Mindfulness**
- Observe, Describe, Participate
- One-mindfully, Non-judgmentally, Effectively
- Wise Mind

**Distress Tolerance**
- STOP, Pros and Cons
- TIP (Temperature, Intense exercise, Paced breathing)
- ACCEPTS, Self-Soothe, IMPROVE
- Radical Acceptance, Willingness, Half-smile

**Emotion Regulation**
- Check the Facts, Opposite Action
- Problem Solving, ABC PLEASE
- Accumulate Positive Emotions, Build Mastery
- Cope Ahead, Mindfulness of Current Emotions

**Interpersonal Effectiveness**
- DEAR MAN, GIVE, FAST
- Validation, Building/Ending Relationships

---

## Future Web UI Notes

When ready to build web interface:

1. **Separate Project**
   - New Flutter Web or React project
   - Uses same Firebase project
   - Same Firestore database

2. **Shared Data**
   - No backend code needed
   - Same security rules apply
   - Real-time sync with mobile app

3. **Features**
   - View entries in table/calendar format
   - Create/edit entries (optional)
   - Export reports
   - Visualizations (charts)

---

## Troubleshooting

### Common Issues

**Build fails after adding Firebase**
- Run `cd ios && pod install`
- Clean build: `flutter clean && flutter pub get`

**Offline writes not syncing**
- Check Firebase console for connectivity
- Verify security rules allow write
- Check auth state (must be authenticated)

**Data not appearing across devices**
- Verify same userId on both devices
- Check Firestore console for data
- Ensure both devices online at least once

---

## Files in This Directory

- **README.md** - Feature documentation (what exists in prototypes)
- **ROADMAP.md** - Development roadmap (completed/TODO/SPIKE/ICEBOX)
- **SPEC.md** - Technical specification
- **NOTES.md** - This file (session continuity)
- **build/** - Flutter build artifacts (gitignored)
- **ios/** - iOS platform files (gitignored generated files)

---

## Next Session Checklist

1. Read SPEC.md to refresh on architecture
2. Check ROADMAP.md for current phase
3. Review this NOTES.md for build progress
4. Continue from last unchecked item in Phase progression
5. Reference original branches as needed for UX patterns
6. Commit frequently with clear messages

---

## Questions to Resolve

None currently - spec is complete and approved.

---

**Ready to build!** Start with Phase 1 (Foundation) when beginning implementation.
