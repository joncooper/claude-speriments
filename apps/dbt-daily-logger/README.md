# DBT Daily Logger 🌟

A Flutter mobile application for iOS that helps users track their DBT (Dialectical Behavior Therapy) journey with comprehensive daily logging, insights, and skill development tools.

## Overview

This app provides a digital version of the DBT diary card with enhanced features for tracking emotions, behaviors, skills usage, and self-care activities. It combines the structure of traditional DBT logging with modern mobile UX including data visualization, skill references, and motivational features.

---

## ✅ Implemented Features

### 📝 Core Daily Logging

**Daily Diary Cards**
- Create comprehensive daily entries with all standard DBT diary card elements
- Track emotions (Anger, Fear/Anxiety, Joy, Sadness, Guilt, Shame) with 0-10 intensity scales
- Monitor urges and their intensity levels
- Log target behaviors (SI, NSSI, Family conflict, Isolation, Avoidance/Procrastination, Withholding, Substance use)
- Record which DBT skills were used, organized by module
- Track sleep hours and quality
- Log medication adherence
- Add free-form journal notes
- **Randomized question order** to prevent sequencing bias

**DBT Skills Tracking**
- Comprehensive coverage of all 4 DBT modules:
  - **Mindfulness**: Observe, Describe, Participate, One-mindfully, Non-judgmentally, Effectively, Wise Mind
  - **Distress Tolerance**: STOP, Pros and Cons, TIP, ACCEPTS, Self-Soothe, IMPROVE, Radical Acceptance, Willingness, Half-smile
  - **Emotion Regulation**: Check the Facts, Opposite Action, Problem Solving, ABC PLEASE, Accumulate Positive Emotions, Build Mastery, Cope Ahead, Mindfulness of Current Emotions
  - **Interpersonal Effectiveness**: DEAR MAN, GIVE, FAST, Validation, Building/Ending Relationships
- Detailed skill checkboxes organized by category
- Dedicated skills page (not cramped 0-7 scale)

### 📚 Learning & Reference

**Branch: flutter-daily-logging-app**
- **Swipeable Skills Reference Cards**: Beautiful gradient cards for each DBT skill
- **Interactive Card Design**: Swipe through skills with smooth animations
- **Detailed Explanations**: What each skill is, when to use it, and how to practice it
- **Module Organization**: Skills grouped by Mindfulness, Distress Tolerance, Emotion Regulation, Interpersonal Effectiveness
- **Quick Access**: Book icon button on home screen

**Branch: dbt-daily-logger**
- **Skills Reference Screen**: Comprehensive list of all DBT skills with explanations
- **Simple Navigation**: Organized by category with expandable details
- **Weekly Skills Grid**: Visual grid showing which skills were used each day (Mon-Sun)
- **Week Navigation**: Browse previous/next/current week
- **Color-Coded Categories**: Visual organization by DBT module

### 📊 Insights & Visualization

**Branch: flutter-daily-logging-app ONLY**
- **Emotion Trends Charts**: Line graphs showing emotion intensity over time
- **Urge Tracking Visualization**: Monitor urge patterns with interactive charts
- **Skills Usage Analytics**: Bar charts showing most-used DBT skills
- **Time Range Selection**: View data for 7, 30, or 90 days
- **Insights Dashboard**: Comprehensive statistics and patterns

### 📅 Calendar & Motivation

**Branch: flutter-daily-logging-app ONLY**
- **Interactive Calendar**: Heat map showing daily logging consistency
- **Streak Tracking**: Current streak and longest streak display
- **Streak Celebrations**: Confetti animations at milestones (every 7 days)
- **Monthly Completion**: Progress ring showing percentage of days logged this month
- **Calendar Navigation**: Jump to any date to view/edit entries

### 🎨 User Experience

**Branch: flutter-daily-logging-app ONLY**
- **Dark Mode**: Automatic theme switching based on system preferences
- **Material Design 3**: Modern, polished interface with smooth animations
- **Theme Persistence**: Remember user's theme preference
- **Interactive Emotion Wheel**: Circular, color-coded emotion picker
- **Emoji Rating Scales**: Fun, intuitive sliders for all intensity ratings
- **Streamlined Navigation**: Quick access menu to all features

### 💾 Data Management

**Both Branches**
- Local data persistence using Hive database (flutter branch) or JSON files (dbt-logger branch)
- View and edit past entries
- Delete entries
- Entry history with date-based organization
- All data stored securely on device

**Branch: flutter-daily-logging-app ONLY**
- **iCloud Sync Service**: Automatic backup to iCloud (implementation present)
- **Cross-Device Sync**: Access entries across all iOS devices (infrastructure ready)
- **Sync Status Monitoring**: Check iCloud connection status
- **PDF Export Service**: Generate professional PDF reports (implementation present)
- **Bulk Export**: Export single entry or all entries
- **Share Integration**: Share PDFs with therapist or print directly

### 🏗️ Technical Implementation

**Common Base (Both Branches)**
- Flutter SDK 3.0+
- iOS-optimized with proper entitlements
- Hive for local database
- Provider for state management
- Material Design 3 UI components

**Additional Packages (flutter-daily-logging-app)**
- `fl_chart` ^0.65.0 - Charts and graphs
- `table_calendar` ^3.0.9 - Calendar views
- `confetti` ^0.7.0 - Celebration animations
- `lottie` ^2.7.0 - Advanced animations
- `pdf` ^3.10.7 - PDF generation
- `printing` ^5.11.1 - Native print dialog
- `path_provider` ^2.1.1 - File system access (for iCloud)

---

## 📱 Project Structure

```
dbt_daily_logger/
├── lib/
│   ├── main.dart                       # App entry point with theme support
│   ├── models/
│   │   ├── diary_entry.dart            # Main data model
│   │   ├── diary_entry.g.dart          # Hive adapter
│   │   ├── diary_entry_new.dart        # Alternative model (if exists)
│   │   └── dbt_constants.dart          # DBT skills and constants
│   ├── screens/
│   │   ├── home_screen.dart            # Main list view (flutter branch: enhanced)
│   │   ├── simple_home_screen.dart     # Alternative home (dbt-logger branch)
│   │   ├── new_daily_entry_screen.dart # Create/edit entries (dbt-logger)
│   │   ├── entry_form_screen.dart      # Alternative entry form
│   │   ├── entry_detail_screen.dart    # View entry details
│   │   ├── insights_screen.dart        # Charts and analytics (flutter only)
│   │   ├── calendar_screen.dart        # Calendar and streaks (flutter only)
│   │   ├── skills_reference_screen.dart # Skill learning (both, different UX)
│   │   └── weekly_skills_screen.dart   # Weekly grid (dbt-logger only)
│   ├── widgets/
│   │   ├── emotion_tracker.dart        # Emotion tracking widget
│   │   ├── urge_tracker.dart           # Urge tracking widget
│   │   ├── skills_selector.dart        # Skills selection widget
│   │   ├── behavior_selector.dart      # Behavior selection widget
│   │   ├── emoji_rating_scale.dart     # Rating scale component
│   │   └── emotion_wheel.dart          # Circular emotion picker (flutter only)
│   └── services/
│       ├── diary_service.dart          # Data persistence service
│       ├── simple_storage.dart         # JSON storage (dbt-logger)
│       ├── theme_service.dart          # Theme management (flutter only)
│       ├── icloud_sync_service.dart    # iCloud sync (flutter only)
│       └── pdf_export_service.dart     # PDF generation (flutter only)
├── ios/
│   └── Runner/
│       ├── Info.plist                  # iOS configuration
│       └── Runner.entitlements         # iCloud entitlements (flutter only)
├── pubspec.yaml                        # Dependencies
├── README.md                           # This file
└── ROADMAP.md                          # Future planning and backlog
```

---

## 🚀 Setup Instructions

### Prerequisites
- Flutter SDK (>=3.0.0)
- Xcode (for iOS development)
- iOS Simulator or physical iOS device
- macOS (for iOS development)

### Installation

1. **Clone or download the project**

2. **Navigate to project directory**
   ```bash
   cd dbt_daily_logger
   ```

3. **Install dependencies**
   ```bash
   flutter pub get
   ```

4. **Generate Hive adapters** (required for database)
   ```bash
   flutter pub run build_runner build
   ```

5. **Run the app**
   ```bash
   # List available devices
   flutter devices

   # Run on iOS simulator
   flutter run

   # Run on specific device
   flutter run -d <device-id>
   ```

### Development Commands

```bash
# Clean build artifacts
flutter clean

# Rebuild Hive adapters after model changes
flutter pub run build_runner build --delete-conflicting-outputs

# Run with specific flavor/mode
flutter run --debug
flutter run --release
```

---

## 🗂️ Data Model

### DiaryEntry Structure

```dart
class DiaryEntry {
  final String id;
  final DateTime date;

  // Emotions (0-10 scale)
  final Map<String, int> emotions;  // anger, fear, joy, sadness, guilt, shame

  // Urges (0-10 scale)
  final Map<String, int> urges;

  // Target Behaviors (occurrences)
  final Map<String, int> behaviors;  // SI, NSSI, conflict, isolate, avoid, withhold, substance

  // DBT Skills Used
  final List<String> skillsUsed;

  // Daily Basics
  final double? hoursOfSleep;     // dbt-logger branch
  final int? sleepQuality;        // 0-5 scale, dbt-logger branch
  final bool? tookMedication;
  final bool? exercised;          // dbt-logger branch

  // Notes
  final String? notes;

  // Metadata
  final DateTime createdAt;
  final DateTime? updatedAt;
}
```

---

## 🌟 Key Differences Between Branches

| Feature | flutter-daily-logging-app | dbt-daily-logger |
|---------|--------------------------|------------------|
| **Storage** | Hive database | JSON files |
| **Dark Mode** | ✅ Full implementation | ❌ Not implemented |
| **Charts/Insights** | ✅ Full dashboard | ❌ Not implemented |
| **Calendar View** | ✅ With heat map & streaks | ❌ Not implemented |
| **Emotion Wheel** | ✅ Interactive circular picker | ❌ Standard sliders |
| **Skills Reference** | ✅ Swipeable cards | ✅ Simple list |
| **Weekly Skills Grid** | ❌ Not implemented | ✅ Mon-Sun grid |
| **Sleep Tracking** | ❌ Basic hours only | ✅ Hours + quality + exercise |
| **iCloud Sync** | ✅ Service implemented | ❌ Not implemented |
| **PDF Export** | ✅ Service implemented | ❌ Not implemented |
| **Confetti Celebrations** | ✅ On streak milestones | ❌ Not implemented |

---

## 📄 License

This project is for personal/educational use.

---

## 🙏 Acknowledgments

Built with Flutter and inspired by the DBT (Dialectical Behavior Therapy) framework developed by Dr. Marsha Linehan.

---

**Note**: This README documents features from TWO parallel development branches. See ROADMAP.md for consolidation plans and future development direction.
