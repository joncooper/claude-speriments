# DBT Daily Logger 🌟

A beautiful, innovative Flutter mobile application for iOS that helps users track their DBT (Dialectical Behavior Therapy) journey with delightful UX and powerful insights.

## ✨ Innovative Features

### 🎨 Gorgeous Visual Design
- **Dark Mode**: Eye-friendly dark theme that automatically syncs with system preferences
- **Material Design 3**: Modern, polished interface with smooth animations
- **Intuitive Navigation**: Quick access to all features through a streamlined menu

### 📊 Data Insights & Visualization
- **Emotion Trends Charts**: Beautiful line graphs showing emotion intensity over time
- **Urge Tracking Visualization**: Monitor urge patterns with interactive charts
- **Skills Usage Analytics**: Bar charts showing your most-used DBT skills
- **Time Range Selection**: View data for 7, 30, or 90 days

### 📅 Calendar & Streak Tracking
- **Interactive Calendar**: Visual heat map showing logging consistency
- **Streak Celebrations**: Confetti animations when you hit milestones!
- **Current Streak**: See your ongoing daily logging streak
- **Longest Streak**: Track your personal best
- **Monthly Completion**: Progress circle showing this month's completion rate

### 🎡 Interactive Emotion Wheel
- **Circular Emotion Picker**: Fun, visual way to select emotions
- **Color-Coded Segments**: Each emotion has its own vibrant color
- **Tap-to-Select**: Intuitive touch interface

### 📚 DBT Skills Reference Cards
- **Swipeable Cards**: Beautiful gradient cards for each skill
- **Module Organization**: Skills organized by Mindfulness, Distress Tolerance, Emotion Regulation, and Interpersonal Effectiveness
- **Detailed Explanations**: Learn what each skill is and how to use it
- **Quick Tips**: Actionable steps for practicing each skill

### ☁️ iCloud Sync
- **Automatic Backup**: Your data is automatically backed up to iCloud
- **Cross-Device Sync**: Access your entries across all your iOS devices
- **Data Safety**: Never lose your progress
- **Sync Status**: Check iCloud connection status anytime

### 📄 PDF Export
- **Professional Reports**: Export beautifully formatted PDF reports
- **Single or Bulk Export**: Export one entry or all entries
- **Share with Therapist**: Easily share your progress
- **Print Support**: Print entries directly from the app

## 🎯 Core Functionality

### Daily Diary Cards
- Create comprehensive daily entries
- Track emotions with 0-10 intensity sliders
- Monitor urges and their intensity
- Log target behaviors
- Record which DBT skills you used
- Track sleep hours and medication adherence
- Add free-form notes

### DBT Skills Coverage
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

## 📱 Project Structure

```
dbt_daily_logger/
├── lib/
│   ├── main.dart                       # App entry point with theme support
│   ├── models/
│   │   ├── diary_entry.dart            # Main data model
│   │   ├── diary_entry.g.dart          # Hive adapter
│   │   └── dbt_constants.dart          # DBT skills and constants
│   ├── screens/
│   │   ├── home_screen.dart            # Main list view
│   │   ├── entry_form_screen.dart      # Create/edit entries
│   │   ├── entry_detail_screen.dart    # View entry details
│   │   ├── insights_screen.dart        # Charts and analytics
│   │   ├── calendar_screen.dart        # Calendar and streaks
│   │   └── skills_reference_screen.dart # Skill learning cards
│   ├── widgets/
│   │   ├── emotion_tracker.dart        # Emotion tracking widget
│   │   ├── urge_tracker.dart           # Urge tracking widget
│   │   ├── skills_selector.dart        # Skills selection widget
│   │   ├── behavior_selector.dart      # Behavior selection widget
│   │   └── emotion_wheel.dart          # Interactive emotion wheel
│   └── services/
│       ├── diary_service.dart          # Data persistence service
│       ├── icloud_sync_service.dart    # iCloud sync
│       ├── theme_service.dart          # Dark mode support
│       └── pdf_export_service.dart     # PDF generation
├── ios/
│   └── Runner/
│       ├── Info.plist                  # iOS configuration
│       └── Runner.entitlements         # iCloud capabilities
├── pubspec.yaml                        # Dependencies
└── README.md                           # This file
```

## 🚀 Getting Started

### Prerequisites
- Flutter SDK (>=3.0.0)
- Xcode (for iOS development)
- iOS Simulator or physical iOS device (iOS 13+)

### Installation

1. **Navigate to the project directory**
   ```bash
   cd dbt_daily_logger
   ```

2. **Install dependencies**
   ```bash
   flutter pub get
   ```

3. **Generate Hive adapters** (if needed)
   ```bash
   flutter pub run build_runner build
   ```

4. **Enable iCloud in Xcode** (for sync features)
   - Open `ios/Runner.xcworkspace` in Xcode
   - Select the Runner target
   - Go to "Signing & Capabilities"
   - Add "iCloud" capability
   - Enable "iCloud Documents"

5. **Run the app**
   ```bash
   flutter run
   ```

## 📖 User Guide

### Creating Your First Entry

1. Tap the **"New Entry"** button
2. Select a date (defaults to today)
3. Fill in your data:
   - Sleep hours and medication status
   - Emotions with intensity sliders
   - Urges with intensity ratings
   - Target behaviors that occurred
   - DBT skills you practiced
   - Any notes or reflections
4. Tap **"Save"**

### Viewing Insights

1. Tap the **Insights** icon in the app bar
2. Choose a time range (7, 30, or 90 days)
3. Explore:
   - Emotion intensity trends
   - Urge patterns
   - Most-used skills
   - Summary statistics

### Tracking Streaks

1. Tap the **Calendar** icon
2. View your:
   - Current logging streak (with confetti for milestones!)
   - Longest streak ever
   - Monthly completion percentage
3. Tap any date to view or create an entry

### Learning DBT Skills

1. Open the menu (three dots)
2. Select **"Skills Reference"**
3. Choose a module
4. Swipe through beautiful cards to learn each skill

### Exporting Data

1. Open the menu (three dots)
2. Select **"Export All to PDF"**
3. Choose where to share or save

### Enabling Dark Mode

1. Open the menu (three dots)
2. Select **"Toggle Dark Mode"**
3. Or it automatically follows your system settings

## 🛠 Technical Details

### Dependencies

**Core**
- `flutter`: Cross-platform framework
- `hive` & `hive_flutter`: Local database
- `provider`: State management
- `path_provider`: File system access

**Visualization**
- `fl_chart`: Beautiful charts
- `table_calendar`: Calendar widget
- `confetti`: Celebration animations

**Export & Sharing**
- `pdf`: PDF generation
- `printing`: Print support
- `share_plus`: System share sheet

**Other**
- `intl`: Date formatting
- `shared_preferences`: App settings
- `lottie`: Smooth animations

## 🔒 Privacy & Data

- **100% Local First**: All data stored on your device
- **iCloud Optional**: Opt-in backup to your personal iCloud
- **No Third Parties**: Zero data sent to external servers
- **HIPAA Considerations**: Suitable for healthcare use
- **Export Control**: You own your data, export anytime

## 🎨 Design Philosophy

This app is designed to be:
- **Delightful**: Beautiful animations and smooth interactions
- **Motivating**: Streaks and celebrations encourage consistency
- **Insightful**: Charts help you see patterns and progress
- **Empowering**: Learn skills while tracking your journey
- **Respectful**: Your data stays private and under your control

## 📝 Best Practices

For optimal results:
- Log daily (even if brief) to build streaks
- Review insights weekly to spot patterns
- Use the Skills Reference to deepen your DBT practice
- Export monthly reports to share with your therapist
- Enable iCloud sync for peace of mind

## 🆘 Support Resources

**Crisis Support**
- National Suicide Prevention Lifeline: **988**
- Crisis Text Line: Text **HOME** to **741741**
- Find a DBT therapist: https://behavioraltech.org/resources/find-a-therapist/

**DBT Resources**
- The Linehan Institute: https://behavioraltech.org
- DBT Skills Training Handouts and Worksheets (Marsha Linehan)

## 🤝 Contributing

This is an open-source project. Contributions, issues, and feature requests are welcome!

## 📄 License

This project is available for personal and educational use.

## 🙏 Acknowledgments

- Based on DBT principles developed by **Dr. Marsha Linehan**
- Built with ❤️ using Flutter
- Designed for the DBT community

---

**Remember**: This app is a tool for self-monitoring and skill practice. It does not replace professional therapy. If you're in crisis, please reach out to a mental health professional or crisis service immediately.

**Your mental health matters. You've got this! 💪✨**
