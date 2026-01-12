# Firebase Setup Guide

This guide will walk you through setting up Firebase for the DBT Daily Logger app.

## Prerequisites

- Flutter SDK installed (3.0+)
- Xcode installed (for iOS development)
- A Google account (for Firebase Console)
- Node.js installed (for Firebase CLI tools)

## Step 1: Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click **Add project**
3. Enter project name: `dbt-daily-logger` (or your preferred name)
4. Disable Google Analytics (optional for personal use)
5. Click **Create project**

## Step 2: Enable Firestore Database

1. In the Firebase Console, go to **Build** → **Firestore Database**
2. Click **Create database**
3. Select **Start in test mode** (we'll add security rules later)
4. Choose your region (pick one closest to you)
5. Click **Enable**

### Add Security Rules

After Firestore is created, go to the **Rules** tab and replace with:

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

Click **Publish** to save the rules.

### Create Indexes

Go to the **Indexes** tab and create a composite index:

- Collection ID: `users/{userId}/entries`
- Fields:
  - `date` - Descending
  - `createdAt` - Descending
- Query scope: Collection

## Step 3: Enable Authentication

1. In the Firebase Console, go to **Build** → **Authentication**
2. Click **Get started**
3. Go to the **Sign-in method** tab
4. Enable **Anonymous** authentication
   - Click on **Anonymous**
   - Toggle **Enable**
   - Click **Save**
5. (Optional for future) Enable **Email/Password** authentication

## Step 4: Add iOS App to Firebase

1. In the Firebase Console, click the iOS icon to add an iOS app
2. Enter iOS bundle ID: `com.example.dbtDailyLogger`
   - (Or use your custom bundle ID if you changed it)
3. Enter app nickname: `DBT Daily Logger iOS` (optional)
4. Click **Register app**
5. Download `GoogleService-Info.plist`
6. **Important:** Place this file in `ios/Runner/` directory

## Step 5: Install Firebase CLI Tools

If you haven't already, install the FlutterFire CLI:

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Install FlutterFire CLI
dart pub global activate flutterfire_cli
```

## Step 6: Configure Firebase in Flutter

Run the FlutterFire configuration tool:

```bash
cd apps/dbt-daily-logger

# Login to Firebase (if not already logged in)
firebase login

# Configure FlutterFire
flutterfire configure
```

This will:
- Detect your Firebase projects
- Let you select the project you created
- Generate `lib/firebase_options.dart` with your configuration
- Configure iOS and web platforms

## Step 7: Install Dependencies

```bash
flutter pub get
```

## Step 8: Configure iOS Project

### Update Info.plist

Open `ios/Runner/Info.plist` and add the following before the closing `</dict>` tag:

```xml
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleTypeRole</key>
        <string>Editor</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>com.googleusercontent.apps.YOUR-IOS-CLIENT-ID</string>
        </array>
    </dict>
</array>
```

Replace `YOUR-IOS-CLIENT-ID` with the value from your `GoogleService-Info.plist`.

### Update Podfile

Open `ios/Podfile` and ensure the platform version is at least 13.0:

```ruby
platform :ios, '13.0'
```

### Install Pods

```bash
cd ios
pod install
cd ..
```

## Step 9: Run the App

```bash
# Open iOS Simulator
open -a Simulator

# Run the app
flutter run
```

## Step 10: Verify Firebase Connection

When you first run the app:

1. You should see the login screen
2. Tap **Get Started** to sign in anonymously
3. Check the Firebase Console → **Authentication** → **Users** tab
4. You should see a new anonymous user created
5. Create a test entry (once that feature is built)
6. Check **Firestore Database** to see your data

## Troubleshooting

### Build Fails on iOS

```bash
cd ios
pod repo update
pod install --repo-update
cd ..
flutter clean
flutter pub get
flutter run
```

### Firebase Connection Errors

1. Verify `GoogleService-Info.plist` is in `ios/Runner/`
2. Check that bundle ID matches in:
   - Firebase Console
   - `GoogleService-Info.plist`
   - Xcode project settings
3. Run `flutterfire configure` again

### Firestore Permission Denied

1. Check that security rules are published
2. Verify user is authenticated before accessing Firestore
3. Check that the userId in the path matches the authenticated user

### Anonymous Auth Not Working

1. Verify Anonymous auth is enabled in Firebase Console
2. Check for error messages in the console/logs
3. Ensure you're connected to the internet

## Testing Offline Support

Firestore automatically handles offline caching:

1. Run the app and create an entry while online
2. Enable airplane mode on the simulator
3. Create another entry
4. The entry will queue for upload
5. Disable airplane mode
6. The entry should sync automatically

You can verify this in **Firestore Database** in the Firebase Console.

## Next Steps

Once Firebase is configured:

1. ✅ Authentication working
2. ✅ Firestore reading/writing
3. ✅ Offline support enabled
4. 🔜 Build the entry form (Phase 2)
5. 🔜 Implement weekly skills grid
6. 🔜 Add settings screen

## Security Best Practices

1. **Never commit Firebase credentials** to public repositories
   - `.gitignore` is configured to exclude sensitive files
   - Be cautious with `GoogleService-Info.plist`

2. **Use security rules** to protect user data
   - The rules we added ensure users can only access their own data
   - Review rules in Firebase Console regularly

3. **Monitor usage** in Firebase Console
   - Check for unexpected activity
   - Set up budget alerts if needed
   - Free tier should be sufficient for personal use

4. **Backup your data**
   - Firebase handles backups, but export feature is planned
   - Consider manual exports for important data

## Firebase Free Tier Limits

For personal use, you should stay well within free tier:

- **Firestore:** 50K reads, 20K writes, 20K deletes per day
- **Authentication:** Unlimited
- **Hosting:** 10 GB storage, 360 MB/day bandwidth

Typical usage for one user:
- ~100 reads per day (loading entries)
- ~10 writes per day (daily entries)
- Well within free tier limits

---

**Questions or Issues?**

Check the [NOTES.md](NOTES.md) file for additional troubleshooting tips and reference the [Firebase Documentation](https://firebase.google.com/docs).
