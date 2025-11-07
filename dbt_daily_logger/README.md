# DBT Daily Logger

A Flutter mobile application for iOS that helps users with their daily DBT (Dialectical Behavior Therapy) logging and diary card tracking.

## Features

### Core Functionality
- **Daily Diary Cards**: Create and manage daily entries with comprehensive tracking
- **Emotion Tracking**: Log emotions with intensity ratings (0-10 scale)
- **Urge Tracking**: Monitor urges with intensity levels
- **Target Behaviors**: Track occurrences of specific behaviors
- **DBT Skills**: Record which DBT skills were used, organized by module:
  - Mindfulness
  - Distress Tolerance
  - Emotion Regulation
  - Interpersonal Effectiveness
- **Daily Basics**: Track sleep hours and medication adherence
- **Notes**: Add free-form journal entries

### Data Management
- Local data persistence using Hive database
- View and edit past entries
- Delete entries
- All data stored securely on device

### User Interface
- Clean, Material Design 3 interface
- Intuitive sliders for intensity ratings
- Organized skill selection by DBT modules
- Quick access to recent entries
- Date-based entry organization

## Project Structure

```
dbt_daily_logger/
├── lib/
│   ├── main.dart                 # App entry point
│   ├── models/
│   │   ├── diary_entry.dart      # Main data model
│   │   ├── diary_entry.g.dart    # Hive adapter
│   │   └── dbt_constants.dart    # DBT skills and constants
│   ├── screens/
│   │   ├── home_screen.dart      # Main list view
│   │   ├── entry_form_screen.dart # Create/edit entries
│   │   └── entry_detail_screen.dart # View entry details
│   ├── widgets/
│   │   ├── emotion_tracker.dart   # Emotion tracking widget
│   │   ├── urge_tracker.dart      # Urge tracking widget
│   │   ├── skills_selector.dart   # Skills selection widget
│   │   └── behavior_selector.dart # Behavior selection widget
│   └── services/
│       └── diary_service.dart     # Data persistence service
├── ios/
│   └── Runner/
│       └── Info.plist            # iOS configuration
├── pubspec.yaml                  # Dependencies
└── README.md                     # This file
```

## Dependencies

The app uses the following Flutter packages:

- **hive** & **hive_flutter**: Local database for storing diary entries
- **intl**: Date and time formatting
- **provider**: State management
- **cupertino_icons**: iOS-style icons

## Setup Instructions

### Prerequisites
- Flutter SDK (>=3.0.0)
- Xcode (for iOS development)
- iOS Simulator or physical iOS device

### Installation

1. **Clone or download the project**

2. **Install dependencies**
   ```bash
   cd dbt_daily_logger
   flutter pub get
   ```

3. **Generate Hive adapters** (if needed)
   ```bash
   flutter pub run build_runner build
   ```

4. **Run the app**
   ```bash
   # For iOS simulator
   flutter run

   # For specific device
   flutter devices  # List available devices
   flutter run -d <device-id>
   ```

## Usage Guide

### Creating a New Entry

1. Tap the **"New Entry"** floating action button on the home screen
2. Select the date (defaults to today)
3. Fill in the sections as needed:
   - **Daily Basics**: Enter sleep hours and medication status
   - **Emotions**: Add emotions and rate their intensity
   - **Urges**: Log any urges and their intensity
   - **Target Behaviors**: Check off any behaviors that occurred
   - **DBT Skills**: Select skills used from the four modules
   - **Notes**: Add any additional context or reflections
4. Tap **"Save"** in the app bar

### Viewing Entries

- The home screen displays all entries in reverse chronological order
- Each entry card shows a summary:
  - Date
  - Number of emotions tracked
  - Number of urges tracked
  - Number of skills used
  - Number of behaviors
  - Whether notes are present
- Tap any entry card to view full details

### Editing Entries

1. Tap an entry to view its details
2. Tap the edit icon in the app bar
3. Make your changes
4. Tap **"Save"**

### Deleting Entries

1. On the home screen, tap the delete icon on an entry card
2. Confirm deletion in the dialog

## DBT Skills Included

The app includes all major DBT skills organized by module:

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
- Validation
- Building/Ending Relationships

## Customization

Users can add custom entries for:
- Emotions (beyond the pre-defined list)
- Urges (beyond the pre-defined list)
- Target behaviors (beyond the common list)

## Data Storage

All data is stored locally on the device using Hive, a fast and lightweight NoSQL database. Data includes:
- Diary entries
- Emotions with intensity ratings
- Urges with intensity ratings
- Target behaviors
- Skills used
- Notes and daily basics

**Note**: Data is not synced to the cloud and remains on the device.

## Building for Release

### iOS

1. Update version in `pubspec.yaml`
2. Build the app:
   ```bash
   flutter build ios --release
   ```
3. Open in Xcode for signing and submission:
   ```bash
   open ios/Runner.xcworkspace
   ```

## Privacy & Health Information

This app is designed to help track DBT therapy progress. Please note:
- All data is stored locally on your device
- No data is transmitted to external servers
- This app is a tool for self-monitoring and does not replace professional therapy
- In case of emergency, please contact your therapist or crisis services

## Support

For DBT resources and crisis support:
- National Suicide Prevention Lifeline: 988
- Crisis Text Line: Text HOME to 741741
- Find a DBT therapist: https://behavioraltech.org/resources/find-a-therapist/

## License

This project is open source and available for personal and educational use.

## Contributing

Contributions, issues, and feature requests are welcome!

## Acknowledgments

Based on DBT principles developed by Dr. Marsha Linehan.
