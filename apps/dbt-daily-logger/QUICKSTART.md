# Quick Start Guide

Get the DBT Daily Logger app running in under 10 minutes!

## Prerequisites Checklist

- [ ] Flutter SDK installed (run `flutter doctor` to verify)
- [ ] Xcode installed (for iOS development)
- [ ] Google account (for Firebase)
- [ ] iOS Simulator or physical device

## Quick Setup (5 Steps)

### 1. Install Dependencies

```bash
cd apps/dbt-daily-logger
flutter pub get
```

### 2. Create Firebase Project

1. Go to https://console.firebase.google.com/
2. Click "Add project" → name it → disable Analytics → Create
3. This takes ~30 seconds

### 3. Enable Firestore & Auth

**Firestore:**
- Build → Firestore Database → Create database
- Start in **test mode** → Pick your region → Enable

**Authentication:**
- Build → Authentication → Get started
- Sign-in method → Anonymous → Enable → Save

### 4. Configure Firebase for iOS

```bash
# Install FlutterFire CLI (one-time setup)
dart pub global activate flutterfire_cli

# Login to Firebase
firebase login

# Auto-configure Firebase
flutterfire configure
```

This will:
- Show your Firebase projects
- Select your project
- Generate `firebase_options.dart`
- Configure iOS automatically

**Important:** When prompted, download `GoogleService-Info.plist` and place it in `ios/Runner/`

### 5. Run the App

```bash
# Install iOS dependencies
cd ios && pod install && cd ..

# Run the app
flutter run
```

## What to Expect

When the app launches:

1. **Login Screen** - Tap "Get Started" to sign in anonymously
2. **Home Screen** - Empty state showing "No entries yet"
3. **Navigation** - Four tabs: Home, Weekly, Skills, Settings
4. **Create Entry** - Tap the + button (form coming in Phase 2)

## Verify Firebase Connection

1. Go to Firebase Console → Authentication
2. You should see an anonymous user created
3. Go to Firestore Database
4. You should see a `users` collection (after creating first entry)

## Current Phase: Phase 1 (Foundation) ✅

What's working now:
- ✅ Authentication (anonymous sign-in)
- ✅ Navigation structure
- ✅ Home screen with entry list
- ✅ Firebase integration
- ✅ Offline support (automatic)
- ✅ Dark mode support

What's coming next (Phase 2):
- 🔜 Daily entry form
- 🔜 Emotions slider (6 emotions, 0-10 scale)
- 🔜 Behaviors tracking
- 🔜 DBT skills selector
- 🔜 Sleep tracking
- 🔜 Save/edit/delete entries

## Troubleshooting

### "Flutter not found"
```bash
flutter doctor
# Follow instructions to complete setup
```

### "No Firebase projects found"
```bash
firebase login
# Login with the Google account that owns the project
```

### "Pod install failed"
```bash
cd ios
pod repo update
pod install --repo-update
cd ..
```

### "Build failed"
```bash
flutter clean
flutter pub get
cd ios && pod install && cd ..
flutter run
```

### "Firebase connection error"
1. Check `GoogleService-Info.plist` is in `ios/Runner/`
2. Verify bundle ID matches (`com.example.dbtDailyLogger`)
3. Run `flutterfire configure` again

## Need More Details?

- **Full Firebase setup:** See [FIREBASE_SETUP.md](FIREBASE_SETUP.md)
- **Technical spec:** See [SPEC.md](SPEC.md)
- **Roadmap:** See [ROADMAP.md](ROADMAP.md)
- **Development notes:** See [NOTES.md](NOTES.md)

## Testing the App

### Test Anonymous Authentication
1. Tap "Get Started"
2. Should navigate to home screen
3. Check Firebase Console → Authentication → Users

### Test Offline Mode
1. Enable airplane mode on simulator
2. App should still work (reading cached data)
3. Writes will queue and sync when online

### Test Dark Mode
1. Change system appearance (Settings → Developer)
2. App should automatically switch themes

## Next Steps

Once Phase 1 is verified:
1. Move to Phase 2: Core Features (entry form)
2. Implement emotions tracking
3. Add behaviors and skills
4. Build weekly skills grid
5. Polish and test

## Getting Help

If you encounter issues:
1. Check [FIREBASE_SETUP.md](FIREBASE_SETUP.md) for detailed troubleshooting
2. Review [NOTES.md](NOTES.md) for known issues
3. Run `flutter doctor -v` for environment diagnostics

---

**Ready to build?** The foundation is solid. Let's implement Phase 2! 🚀
