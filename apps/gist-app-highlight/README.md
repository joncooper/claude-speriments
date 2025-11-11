# Sideshow - Annotated Markdown Viewer

A client-side web application for creating, annotating, and sharing markdown documents with highlights and sidenotes, inspired by GitHub Gists and Genius.com's annotation system.

## Features

- 📝 **Markdown Editor** - Paste and edit markdown content
- 👁️ **Live Preview** - Toggle between edit and rendered views
- ✨ **Highlights** - Select text to create highlights in preview mode
- 📌 **Sidenotes** - Add contextual annotations to highlighted sections
- 🔗 **Shareable Links** - Generate short links for read-only viewing
- 🔐 **Simple Auth** - Google sign-in for creators (viewers don't need auth)
- ☁️ **Cloud Storage** - Firebase Firestore for persistent storage

## Use Case

**For Creators:**
1. Copy markdown from anywhere
2. Paste into Sideshow
3. Toggle to preview mode
4. Select text → add highlights → write sidenotes
5. Save and get a shareable short link

**For Viewers:**
1. Open shared link
2. See beautifully rendered markdown with highlights and annotations
3. No sign-in required

## Tech Stack

- **TypeScript** - Type-safe development
- **Vite** - Lightning-fast build tool
- **bun** - Fast package manager (10-100x faster than npm)
- **Firebase** - Auth + Firestore database
- **marked.js** - Markdown rendering
- **DOMPurify** - XSS protection

## Setup

### Prerequisites

- **bun** (recommended) or **npm**
- Firebase project (see setup below)

### Install bun

```bash
# macOS/Linux/WSL
curl -fsSL https://bun.sh/install | bash

# Or via npm
npm install -g bun
```

### Firebase Setup

1. Create a Firebase project at https://console.firebase.google.com
2. Enable Firestore Database
3. Enable Google Authentication
4. Copy your Firebase config
5. Create `src/firebase-config.ts`:

```typescript
export const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
};
```

6. Set up Firestore security rules (see `firestore.rules`)

### Development

```bash
# Install dependencies
bun install

# Run dev server
bun run dev

# Build for production
bun run build

# Preview production build
bun run preview
```

### Deployment

The app is configured to build to `/docs/sideshow/` for GitHub Pages:

```bash
bun run build
git add docs/sideshow
git commit -m "Deploy Sideshow"
git push
```

Access at: `https://yourusername.github.io/yourrepo/docs/sideshow/`

## Project Structure

```
apps/gist-app-highlight/
├── src/
│   ├── main.ts              # Entry point
│   ├── firebase.ts          # Firebase initialization
│   ├── firebase-config.ts   # Firebase config (gitignored)
│   ├── auth.ts              # Authentication logic
│   ├── db.ts                # Firestore operations
│   ├── models.ts            # TypeScript interfaces
│   ├── markdown.ts          # Markdown rendering
│   ├── highlights.ts        # Highlight selection logic
│   ├── router.ts            # Client-side routing
│   ├── ui.ts                # UI components
│   └── utils.ts             # Utility functions
├── docs/sideshow/           # Build output (GitHub Pages)
├── public/                  # Static assets
├── index.html               # HTML template
├── vite.config.ts           # Vite configuration
├── tsconfig.json            # TypeScript config
├── package.json             # Dependencies
├── bun.lock                 # Lock file
├── README.md                # This file
├── NOTES.md                 # Implementation notes
└── ICEBOX.md                # Future enhancements
```

## Usage

### Creating a Gist

1. Sign in with Google
2. Paste your markdown
3. Click "Save" to create a draft
4. Toggle to "Preview" mode
5. Select text to highlight
6. Add annotations in the side pane
7. Click "Save" to update
8. Click "Share" to get the short link

### Viewing a Gist

1. Open link like: `/docs/sideshow/aB3xK9mQ`
2. See rendered markdown with highlights
3. Click highlights to focus their annotations
4. No sign-in required

## License

MIT

## Contributing

This is a personal experiment. Feel free to fork and adapt!
