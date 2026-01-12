# Firebase Setup Guide

This guide walks you through setting up Firebase for Resumeyay.

## Step 1: Create a Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Add project"
3. Name it something like "resumeyay" or "resumeyay-dev"
4. Disable Google Analytics (not needed) or enable if you want it
5. Click "Create project"

## Step 2: Enable Authentication

1. In your project, go to **Build > Authentication**
2. Click "Get started"
3. Go to **Sign-in method** tab
4. Click on **Google**
5. Toggle "Enable"
6. Set a public-facing name (e.g., "Resumeyay")
7. Select your email as the support email
8. Click "Save"

## Step 3: Create Firestore Database

1. Go to **Build > Firestore Database**
2. Click "Create database"
3. Choose "Start in **test mode**" (we'll add rules later)
4. Select a location close to you
5. Click "Enable"

## Step 4: Get Web App Config

1. Go to **Project Settings** (gear icon in sidebar)
2. Scroll down to "Your apps"
3. Click the web icon `</>`
4. Name the app "resumeyay-web"
5. Don't enable Firebase Hosting (not needed)
6. Click "Register app"
7. Copy the config values:
   - `apiKey` → `FIREBASE_API_KEY`
   - `projectId` → `FIREBASE_PROJECT_ID`

## Step 5: Get Service Account Key

1. Still in **Project Settings**
2. Go to **Service accounts** tab
3. Click "Generate new private key"
4. Click "Generate key" to download the JSON file
5. **Option A**: Save the file as `server/firebase-service-account.json`
6. **Option B**: Copy values to your `.env` file:
   - `client_email` → `FIREBASE_CLIENT_EMAIL`
   - `private_key` → `FIREBASE_PRIVATE_KEY` (keep the `\n` characters)

## Step 6: Configure Environment

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Fill in your values:
   ```env
   ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
   FIREBASE_API_KEY=AIzaSy...
   FIREBASE_PROJECT_ID=resumeyay-xxxxx
   FIREBASE_CLIENT_EMAIL=firebase-adminsdk-xxxxx@resumeyay-xxxxx.iam.gserviceaccount.com
   FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
   ```

## Step 7: Run the App

```bash
# Start the server
bun run server

# In another terminal, start the frontend
bun run dev
```

## Firestore Security Rules (Later)

Once you're ready to lock down your database, update the rules in Firebase Console > Firestore > Rules:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Users can only access their own data
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }

    match /workspaces/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }

    match /users/{userId}/jobs/{jobId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }

    match /users/{userId}/fitSessions/{sessionId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

## Troubleshooting

### "Firebase not configured" error
- Make sure your `.env` file exists and has the correct values
- Restart the server after changing `.env`

### "Invalid token" error
- The token might have expired - try logging in again
- Make sure `FIREBASE_API_KEY` is correct

### CORS errors
- Make sure the server is running on port 3001
- Check that the client is calling the correct server URL

## Development Mode

When Firebase isn't configured, the server runs in "dev mode":
- Uses in-memory storage (data lost on restart)
- Uses a fake user for authentication
- Add `X-Dev-Auth: true` header to bypass auth

This lets you develop without setting up Firebase immediately.
