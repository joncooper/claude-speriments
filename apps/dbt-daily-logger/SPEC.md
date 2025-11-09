# DBT Daily Logger - Technical Specification

**Version**: 1.0
**Date**: 2025-11-08
**Branch**: `dbt-daily-logger-wip-2025-11-08`

---

## Overview

Rebuild of DBT Daily Logger app with Firebase backend for multi-platform support (iOS, web) and automatic cloud sync.

### Goals
- Clean, maintainable codebase
- Firebase-first architecture (works offline, syncs when online)
- Combine best features from both prototype branches
- Foundation for web UI (shared data layer)
- User authentication and data privacy

---

## Architecture

### Technology Stack

**Frontend (Flutter)**
- Flutter SDK 3.0+
- Material Design 3
- Provider for state management

**Backend (Firebase)**
- Firebase Authentication (anonymous or email)
- Cloud Firestore (NoSQL database)
- Firebase Storage (future: for attachments/exports)
- Firebase Hosting (future: web UI)

**Key Packages**
```yaml
dependencies:
  flutter:
    sdk: flutter

  # Firebase
  firebase_core: ^2.24.0
  firebase_auth: ^4.15.0
  cloud_firestore: ^4.13.0

  # UI
  cupertino_icons: ^1.0.6
  provider: ^6.1.1
  intl: ^0.18.1

  # Future phases
  # fl_chart: ^0.65.0           # Charts
  # table_calendar: ^3.0.9      # Calendar
  # confetti: ^0.7.0            # Celebrations
```

### Data Architecture

**Firestore Structure**
```
users/
  {userId}/
    profile/
      - createdAt
      - settings (theme, notifications)

    entries/
      {entryId}/
        - date (timestamp)
        - emotions (map)
        - urges (map)
        - behaviors (map)
        - skillsUsed (array)
        - sleepHours (number)
        - sleepQuality (number)
        - exercised (boolean)
        - tookMedication (boolean)
        - notes (string)
        - createdAt
        - updatedAt
```

**Offline Support**
- Firestore automatically caches data locally
- Write operations queue when offline
- Sync when connection restored
- No additional offline logic needed

---

## Feature Prioritization

### Phase 1: Foundation (Week 1)
- [x] Project setup with Firebase
- [ ] Authentication (anonymous initially, email later)
- [ ] Data models and Firestore integration
- [ ] Basic navigation structure

### Phase 2: Core Features (Week 1-2)
- [ ] Daily entry form
  - Emotions (6 types, 0-10 scale)
  - Urges (with intensity)
  - Target behaviors (7 types)
  - DBT skills selector (4 modules, all skills)
  - Sleep tracking (hours, quality 0-5, exercise)
  - Medication checkbox
  - Notes field
- [ ] Randomized question order
- [ ] Entry list/history view
- [ ] View/edit/delete entries
- [ ] Date-based organization

### Phase 3: Enhanced Features (Week 2-3)
- [ ] Dark mode + theme service
- [ ] Weekly skills grid (Mon-Sun visualization)
- [ ] Skills reference screen (simple list initially)
- [ ] User settings screen

### Phase 4: Polish (Week 3-4)
- [ ] Animations and transitions
- [ ] Error handling and validation
- [ ] Loading states
- [ ] Empty states
- [ ] Search/filter entries

### Phase 5: Advanced (Future)
- [ ] Charts and insights
- [ ] Calendar view with streaks
- [ ] Swipeable skills cards
- [ ] PDF export
- [ ] Web UI (separate project, same Firestore)
- [ ] Email authentication
- [ ] Data export

---

## Data Models

### DiaryEntry

```dart
class DiaryEntry {
  final String id;
  final String userId;
  final DateTime date;

  // Emotions (0-10 scale)
  final Map<String, int> emotions; // anger, fear, joy, sadness, guilt, shame

  // Urges (0-10 scale)
  final Map<String, int> urges;

  // Behaviors (occurrence count)
  final Map<String, int> behaviors; // SI, NSSI, conflict, isolate, avoid, withhold, substance

  // Skills
  final List<String> skillsUsed; // IDs from DBT skills constants

  // Daily basics
  final double? sleepHours;
  final int? sleepQuality; // 0-5
  final bool? exercised;
  final bool? tookMedication;

  // Notes
  final String? notes;

  // Metadata
  final DateTime createdAt;
  final DateTime updatedAt;

  // Firestore conversion
  Map<String, dynamic> toFirestore();
  factory DiaryEntry.fromFirestore(DocumentSnapshot doc);
}
```

### UserProfile

```dart
class UserProfile {
  final String userId;
  final DateTime createdAt;
  final ThemeMode themeMode;
  final bool notificationsEnabled;

  Map<String, dynamic> toFirestore();
  factory UserProfile.fromFirestore(DocumentSnapshot doc);
}
```

### DBT Skills Constants

```dart
// Organized by module, same as physical diary card
class DBTSkills {
  static const Map<String, List<String>> skillsByModule = {
    'Mindfulness': [
      'Observe',
      'Describe',
      'Participate',
      'One-mindfully',
      'Non-judgmentally',
      'Effectively',
      'Wise Mind',
    ],
    'Distress Tolerance': [
      'STOP',
      'Pros and Cons',
      'TIP',
      'ACCEPTS',
      'Self-Soothe',
      'IMPROVE',
      'Radical Acceptance',
      'Willingness',
      'Half-smile',
    ],
    'Emotion Regulation': [
      'Check the Facts',
      'Opposite Action',
      'Problem Solving',
      'ABC PLEASE',
      'Accumulate Positive Emotions',
      'Build Mastery',
      'Cope Ahead',
      'Mindfulness of Current Emotions',
    ],
    'Interpersonal Effectiveness': [
      'DEAR MAN',
      'GIVE',
      'FAST',
      'Validation',
      'Building/Ending Relationships',
    ],
  };
}
```

---

## Screen Architecture

### Main Navigation

```
App (MaterialApp)
├── AuthWrapper (checks authentication)
│   ├── LoginScreen (if not authenticated)
│   └── MainScreen (if authenticated)
│       ├── HomeScreen (entry list)
│       ├── NewEntryScreen
│       ├── EntryDetailScreen
│       ├── WeeklySkillsScreen
│       ├── SkillsReferenceScreen
│       └── SettingsScreen
```

### Screen Details

**HomeScreen**
- List of diary entries (most recent first)
- Date headers
- Summary cards (emotions, behaviors used)
- FAB to create new entry
- Bottom nav: Home, Weekly Grid, Skills, Settings

**NewEntryScreen / EditEntryScreen**
- Multi-page form or scrollable single page
- Sections:
  1. Emotions (randomized order)
  2. Urges
  3. Behaviors (randomized order)
  4. DBT Skills (organized by module)
  5. Sleep & Self-care
  6. Notes
- Save/Cancel buttons
- Auto-save drafts (Firestore handles this)

**EntryDetailScreen**
- Read-only view of entry
- Edit and Delete actions
- Formatted display of all data

**WeeklySkillsScreen**
- Mon-Sun grid
- Shows which skills used each day
- Color-coded by module
- Week navigation

**SkillsReferenceScreen**
- List organized by module
- Expandable tiles for each skill
- Brief explanation of each

**SettingsScreen**
- Theme toggle (light/dark/system)
- Notification preferences (future)
- Account management
- Data export (future)
- Sign out

---

## Firebase Setup

### Initial Configuration

1. Create Firebase project
2. Add iOS app (bundle ID: `com.example.dbtDailyLogger` or custom)
3. Download `GoogleService-Info.plist` → `ios/Runner/`
4. Add web app (for future web UI)
5. Enable Firestore
6. Enable Authentication (Anonymous + Email)

### Firestore Security Rules

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // User can only access their own data
    match /users/{userId}/{document=**} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

### Firestore Indexes

```
// Composite index for querying entries by date
Collection: users/{userId}/entries
Fields: date (Descending), createdAt (Descending)
```

---

## Development Workflow

### Setup Steps

1. **Initialize Flutter project**
```bash
cd dbt_daily_logger
flutter create . --org com.example --platforms ios,web
flutter pub add firebase_core firebase_auth cloud_firestore provider intl
```

2. **Configure Firebase**
- Follow FlutterFire CLI setup
- Add GoogleService-Info.plist
- Initialize in main.dart

3. **Project Structure**
```
lib/
├── main.dart
├── models/
│   ├── diary_entry.dart
│   ├── user_profile.dart
│   └── dbt_skills.dart
├── services/
│   ├── auth_service.dart
│   ├── firestore_service.dart
│   └── theme_service.dart
├── providers/
│   ├── auth_provider.dart
│   └── entries_provider.dart
├── screens/
│   ├── auth/
│   │   └── login_screen.dart
│   ├── home_screen.dart
│   ├── new_entry_screen.dart
│   ├── entry_detail_screen.dart
│   ├── weekly_skills_screen.dart
│   ├── skills_reference_screen.dart
│   └── settings_screen.dart
└── widgets/
    ├── emotion_slider.dart
    ├── behavior_selector.dart
    ├── skills_selector.dart
    └── entry_card.dart
```

### Testing Strategy

1. **Manual Testing**
   - Test on iOS simulator
   - Verify offline mode (airplane mode)
   - Test sync across devices (create second Firebase user)

2. **Future: Automated Tests**
   - Unit tests for models
   - Widget tests for UI components
   - Integration tests for Firestore operations

---

## Migration Path (Future)

### From Prototype Branches

Users with existing data (unlikely, but possible):
1. Export from old app (if needed)
2. Import script to convert to Firestore format
3. Manual data entry for small datasets

### Web UI Development

Once mobile app is stable:
1. Create separate web project (Flutter Web or React)
2. Use same Firebase project
3. Share Firestore security rules
4. Implement responsive layout for desktop

---

## Security Considerations

### Data Privacy
- User data isolated by userId
- Firestore security rules enforce access control
- No data sharing between users
- Future: Option to export/delete all data (GDPR)

### Authentication
- Start with anonymous auth (low friction)
- Migrate to email auth when ready
- Account linking (anonymous → email) for data preservation

### Offline Security
- Firestore cache encrypted on device
- No plaintext storage of sensitive data

---

## Performance Considerations

### Firestore Optimization
- Paginate entry list (load 20 at a time)
- Index date field for fast queries
- Use snapshots for real-time updates (optional)
- Cache aggressively for offline use

### Flutter Performance
- Lazy load entry list
- Use const constructors where possible
- Optimize rebuilds with Provider selectors
- Profile in release mode

---

## Success Criteria

### MVP Complete When:
- [x] User can sign in (anonymous)
- [ ] User can create daily entry with all fields
- [ ] Entries persist to Firestore
- [ ] Entries sync across devices
- [ ] Works offline (queue writes)
- [ ] Can view/edit/delete entries
- [ ] Dark mode works
- [ ] Weekly skills grid displays
- [ ] Skills reference accessible
- [ ] No crashes on iOS simulator

### Ready for Beta When:
- [ ] All MVP criteria met
- [ ] Email authentication working
- [ ] Error handling comprehensive
- [ ] Loading states polished
- [ ] Tested on real device
- [ ] Data export implemented
- [ ] Privacy policy written

---

## Next Steps

1. Initialize Flutter project with Firebase
2. Set up authentication
3. Create data models
4. Build entry form
5. Implement Firestore CRUD
6. Test offline sync
7. Add remaining screens
8. Polish and deploy

---

**Status**: Specification complete, ready to build
**Last Updated**: 2025-11-08
