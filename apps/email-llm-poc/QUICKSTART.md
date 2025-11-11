# Quick Start Guide

Get your email-to-LLM bot running in 15 minutes.

## Prerequisites

- Node.js 18+ installed
- Google account
- SendGrid account (free tier)

## 5-Minute Setup

### 1. Create Firebase Project

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login
firebase login

# Go to console.firebase.google.com and create a project
# Enable Firestore and Billing (required for external API calls)
```

### 2. Get API Keys

**SendGrid:**
1. Go to sendgrid.com → Sign up
2. Settings → API Keys → Create API Key (Full Access)
3. Copy the key

**Gemini:**
1. Go to ai.google.dev → Get API Key
2. Copy the key

### 3. Initialize Project

```bash
cd apps/email-llm-poc

# Initialize Firebase (select your project)
firebase init

# Choose: Functions, Firestore, Emulators
# Language: TypeScript
# Use default options

# Install dependencies
cd functions && npm install && cd ..
```

### 4. Configure Secrets

```bash
# Set API keys
firebase functions:secrets:set SENDGRID_API_KEY
# (paste SendGrid key)

firebase functions:secrets:set GEMINI_API_KEY
# (paste Gemini key)

# Set bot email (we'll get this from SendGrid in next step)
firebase functions:config:set app.bot_email="TEMPORARY"
```

### 5. Deploy

```bash
firebase deploy --only functions
```

Copy the `processInboundEmail` function URL from the output.

### 6. Configure SendGrid Inbound Parse

1. Go to SendGrid → Settings → Inbound Parse
2. Click "Add Host & URL"
3. Choose a subdomain (e.g., "chatbot")
4. You get: `anything@chatbot.parse.sendgrid.net`
5. Paste your function URL from step 5
6. Check "POST the raw, full MIME message"
7. Save

### 7. Update Bot Email

```bash
# Update with your actual SendGrid address
firebase functions:config:set app.bot_email="chatbot@chatbot.parse.sendgrid.net"

# Redeploy to pick up config
firebase deploy --only functions
```

### 8. Test!

Send an email to your bot:

```
To: test@chatbot.parse.sendgrid.net
Subject: Hello!
Body: Can you explain what you do?
```

You should receive a reply within 10 seconds!

## Next Steps

- **Read the full setup guide:** [docs/SETUP.md](docs/SETUP.md)
- **Understand the architecture:** [docs/TECHNICAL_SPEC.md](docs/TECHNICAL_SPEC.md)
- **See what's possible:** [ICEBOX.md](ICEBOX.md)
- **Customize behavior:** Edit `prompts/system_prompt.md`

## Troubleshooting

### No reply received?

```bash
# Check logs
firebase functions:log

# Look for:
# - "Received email from: ..."
# - "Email reply sent"
```

### Configuration error?

```bash
# Verify secrets are set
firebase functions:config:get

# Should show app.bot_email
```

### Still stuck?

See [docs/SETUP.md](docs/SETUP.md) for detailed troubleshooting.

## What You Built

You now have:
- ✅ A bot that responds to emails
- ✅ Conversation context (remembers previous messages)
- ✅ Rate limiting (50 messages/day per user)
- ✅ Automatic conversation archiving
- ✅ All on free tiers!

**Have fun!** Reply to the bot to continue conversations, and see what it can do.
