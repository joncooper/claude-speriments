# Setup Guide: Email-to-LLM Conversation System

This guide walks you through setting up the email-to-LLM conversation system from scratch.

## Prerequisites

Before you begin, ensure you have:

- **Node.js 18+** installed ([download](https://nodejs.org/))
- **npm** or **yarn** package manager
- **Git** for version control
- A **Google account** (for Firebase and Gemini)
- A **SendGrid account** (free tier is fine)
- A **custom domain** (optional, but recommended for production)

## Step 1: Firebase Setup

### 1.1 Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Add project"
3. Enter project name (e.g., "email-llm-bot")
4. Disable Google Analytics (optional for POC)
5. Click "Create project"

### 1.2 Enable Firestore

1. In Firebase Console, go to "Firestore Database"
2. Click "Create database"
3. Choose "Start in production mode"
4. Select a location (choose closest to your users)
5. Click "Enable"

### 1.3 Enable Billing

⚠️ **Important:** Cloud Functions require a billing account (for external API calls).

1. Go to project settings (gear icon)
2. Click "Usage and billing"
3. Click "Details & settings"
4. Add a billing account
5. Set up budget alerts (recommended: $10/month)

**Note:** You'll stay within the free tier for low usage, but a billing account is required.

### 1.4 Install Firebase CLI

```bash
npm install -g firebase-tools
```

### 1.5 Login to Firebase

```bash
firebase login
```

This opens a browser window to authenticate.

## Step 2: Local Project Setup

### 2.1 Navigate to Project

```bash
cd apps/email-llm-poc
```

### 2.2 Initialize Firebase

```bash
firebase init
```

Choose:
- **Functions:** Configure Cloud Functions (TypeScript)
- **Firestore:** Set up Firestore security rules
- **Emulators:** Set up local emulators for development

Configuration options:
- Use existing project (select your project from Step 1)
- TypeScript for Functions: Yes
- ESLint: Yes
- Install dependencies: Yes
- Firestore rules file: firestore.rules (already exists)
- Firestore indexes: firestore.indexes.json (already exists)
- Emulators: Functions, Firestore

This creates a `.firebaserc` file with your project ID.

### 2.3 Install Dependencies

```bash
cd functions
npm install
cd ..
```

## Step 3: SendGrid Setup

### 3.1 Create SendGrid Account

1. Go to [SendGrid](https://sendgrid.com/)
2. Sign up for a free account (100 emails/day)
3. Verify your email address
4. Complete sender verification

### 3.2 Create API Key

1. Go to Settings > API Keys
2. Click "Create API Key"
3. Name: "Email LLM Bot"
4. Permissions: "Full Access" (or at minimum: Mail Send + Inbound Parse)
5. Copy the API key (you won't see it again!)

### 3.3 Set Up Inbound Parse

#### Option A: Using SendGrid Subdomain (Easiest)

1. Go to Settings > Inbound Parse
2. Click "Add Host & URL"
3. For subdomain: choose any available name (e.g., "chatbot")
4. This gives you: `[anything]@chatbot.parse.sendgrid.net`
5. For URL: Leave blank for now (we'll add it after deploying)
6. Click "Add"

#### Option B: Using Custom Domain (Production)

1. Go to Settings > Inbound Parse
2. Click "Add Host & URL"
3. Enter your domain (e.g., "yourdomain.com")
4. Add MX record to your DNS:
   ```
   Type: MX
   Host: mail.yourdomain.com
   Value: mx.sendgrid.net
   Priority: 10
   ```
5. Wait for DNS propagation (5-30 minutes)
6. Verify domain in SendGrid

**We'll come back to set the webhook URL after deployment.**

## Step 4: Gemini API Setup

### 4.1 Get API Key

1. Go to [Google AI Studio](https://ai.google.dev/)
2. Click "Get API key"
3. Create a new API key (or use existing)
4. Copy the API key

### 4.2 Test API Key (Optional)

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=YOUR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"Hello"}]}]}'
```

You should get a response with generated text.

## Step 5: Configure Environment Variables

### 5.1 Set Firebase Secrets (Production)

```bash
# Set SendGrid API key
firebase functions:secrets:set SENDGRID_API_KEY
# Paste your SendGrid API key when prompted

# Set Gemini API key
firebase functions:secrets:set GEMINI_API_KEY
# Paste your Gemini API key when prompted
```

### 5.2 Set Firebase Config (Production)

```bash
# Set bot email address
firebase functions:config:set app.bot_email="chatbot@chatbot.parse.sendgrid.net"

# Set rate limits
firebase functions:config:set app.max_messages_per_day="50"
firebase functions:config:set app.max_conversation_history="20"
```

### 5.3 Local Development (.env)

Create `functions/.env` for local testing:

```bash
cd functions
cp .env.example .env
```

Edit `functions/.env`:

```bash
SENDGRID_API_KEY=SG.your_sendgrid_api_key
GEMINI_API_KEY=your_gemini_api_key
BOT_EMAIL_ADDRESS=chatbot@chatbot.parse.sendgrid.net
MAX_MESSAGES_PER_DAY_PER_USER=50
MAX_CONVERSATION_HISTORY=20
```

⚠️ **Important:** Never commit `.env` to git!

## Step 6: Deploy to Firebase

### 6.1 Build and Deploy

```bash
# From the project root (apps/email-llm-poc)
firebase deploy --only functions
```

This will:
1. Build TypeScript to JavaScript
2. Upload functions to Firebase
3. Display function URLs

### 6.2 Note Function URLs

After deployment, you'll see URLs like:

```
✔  functions: Finished running predeploy script.
...
✔  functions[processInboundEmail(us-central1)]: Successful create operation.
Function URL (processInboundEmail): https://us-central1-your-project.cloudfunctions.net/processInboundEmail

✔  functions[healthCheck(us-central1)]: Successful create operation.
Function URL (healthCheck): https://us-central1-your-project.cloudfunctions.net/healthCheck
```

**Copy the `processInboundEmail` URL** - you'll need it for SendGrid.

### 6.3 Test Health Check

```bash
curl https://us-central1-your-project.cloudfunctions.net/healthCheck
```

You should see:
```json
{
  "status": "ok",
  "timestamp": "2025-11-11T...",
  "environment": {
    "hasSendGridKey": true,
    "hasGeminiKey": true,
    "hasBotEmail": true
  }
}
```

## Step 7: Connect SendGrid Webhook

### 7.1 Update Inbound Parse

1. Go back to SendGrid > Settings > Inbound Parse
2. Click the gear icon next to your domain
3. Enter the webhook URL:
   ```
   https://us-central1-your-project.cloudfunctions.net/processInboundEmail
   ```
4. Check "POST the raw, full MIME message"
5. Click "Update"

### 7.2 Verify Webhook

SendGrid will send a test POST to verify the URL is accessible.

If verification fails:
- Check the URL is correct
- Ensure the Cloud Function is deployed
- Check Firebase logs for errors

## Step 8: Test the System

### 8.1 Send Test Email

Send an email to your bot's address:

```
To: anything@chatbot.parse.sendgrid.net
Subject: Hello!
Body: Can you help me with something?
```

Replace `chatbot.parse.sendgrid.net` with your actual domain.

### 8.2 Check Logs

```bash
firebase functions:log
```

You should see:
- "Received email from: your@email.com"
- "Gemini response received"
- "Email reply sent"

### 8.3 Receive Reply

Check your inbox! You should receive a reply from the bot within 5-10 seconds.

### 8.4 Continue Conversation

Reply to the bot's email to continue the conversation. The bot should maintain context.

## Step 9: Local Development Setup (Optional)

For testing without deploying:

### 9.1 Start Emulators

```bash
firebase emulators:start
```

This starts:
- Functions emulator on http://localhost:5001
- Firestore emulator on http://localhost:8080
- Emulator UI on http://localhost:4000

### 9.2 Use ngrok for Webhook Testing

SendGrid can't send webhooks to localhost, so use ngrok:

```bash
# Install ngrok
npm install -g ngrok

# Start ngrok tunnel
ngrok http 5001
```

Copy the HTTPS URL (e.g., `https://abc123.ngrok.io`)

### 9.3 Update SendGrid Webhook

Temporarily update SendGrid Inbound Parse webhook to:

```
https://abc123.ngrok.io/your-project/us-central1/processInboundEmail
```

Now you can test locally with real emails!

## Troubleshooting

### Email Not Received by Bot

**Check:**
- SendGrid Inbound Parse is configured correctly
- MX records are set (if using custom domain)
- DNS has propagated (use `dig` or `nslookup`)
- Email didn't bounce (check SendGrid Activity Feed)

### No Reply from Bot

**Check:**
1. Firebase logs: `firebase functions:log`
2. Look for errors in processing
3. Verify API keys are set correctly:
   ```bash
   firebase functions:config:get
   ```
4. Check rate limits (try from different email)
5. Verify Gemini API quota (60 requests/minute)

### "Configuration Error" in Logs

**Check:**
- All environment variables are set
- API keys are valid
- Firebase secrets are deployed:
  ```bash
  firebase functions:secrets:access SENDGRID_API_KEY
  firebase functions:secrets:access GEMINI_API_KEY
  ```

### Rate Limit Errors

**Gemini API:**
- Free tier: 60 requests per minute
- Wait 1 minute and try again
- Consider upgrading if needed

**SendGrid:**
- Free tier: 100 emails per day
- Upgrade to Essentials ($15/month) for more

### Firestore Permission Denied

**Check:**
- Firestore rules allow server-side access
- Using Admin SDK (not client SDK)

### Function Timeout

**Check:**
- Gemini API latency (usually 1-3s)
- Firestore queries are indexed
- Consider increasing timeout:
  ```typescript
  export const processInboundEmail = functions
    .runWith({ timeoutSeconds: 120 })
    .https.onRequest(...)
  ```

## Next Steps

### Monitor Usage

1. **Firebase Console:** Check function invocations, errors
2. **SendGrid Activity:** See email delivery status
3. **Gemini API Quotas:** Monitor at ai.google.dev

### Set Up Monitoring

```bash
# View logs in real-time
firebase functions:log --only processInboundEmail

# Set up log-based alerts in Firebase Console
# Go to Logs > Create Metric > Create Alert
```

### Enable Additional Features

- See ICEBOX.md for future enhancements
- Customize system prompt in `prompts/system_prompt.md`
- Add custom commands (/reset, /help, etc.)

## Cost Estimates

### Free Tier

- Firebase: 2M function invocations/month
- SendGrid: 100 emails/day
- Gemini: 60 requests/minute
- **Total: $0/month** for light usage

### Paid Tiers

**Low usage (100 emails/day):**
- Firebase: ~$5/month
- SendGrid: $15/month (Essentials, 400 emails/day)
- Gemini: Free
- **Total: ~$20/month**

**Medium usage (1000 emails/day):**
- Firebase: ~$20/month
- SendGrid: $15/month (still under limit)
- Gemini: Free (may need to monitor)
- **Total: ~$35/month**

## Getting Help

### Resources

- [Firebase Functions Docs](https://firebase.google.com/docs/functions)
- [SendGrid Inbound Parse Docs](https://docs.sendgrid.com/for-developers/parsing-email/setting-up-the-inbound-parse-webhook)
- [Gemini API Docs](https://ai.google.dev/docs)

### Common Issues

- Check GitHub Issues for this project
- See NOTES.md for implementation details
- Review logs for specific error messages

---

**Setup Complete!** 🎉

You now have a working email-to-LLM conversation system. Try it out and see ICEBOX.md for ideas on what to build next.
