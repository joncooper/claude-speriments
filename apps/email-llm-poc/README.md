# Email-to-LLM Conversation System

A proof-of-concept system that enables turn-by-turn conversations with an LLM via email. Built with Firebase, SendGrid, and Google Gemini.

## Overview

This system allows users to have conversations with an AI assistant through email:

1. User sends an email to the bot's address
2. System processes the email and maintains conversation context
3. Gemini API generates a contextually-aware response
4. Bot replies via email with proper threading
5. Conversation continues with full history preserved

**Key Features:**
- Turn-by-turn email conversations with context preservation
- Proper email threading (conversations stay together)
- Rate limiting (50 messages/day per user)
- Automatic conversation archiving
- Error handling and user notifications
- Free tier friendly (Firebase + SendGrid + Gemini)

## Architecture

```
User Email → SendGrid Inbound → Cloud Function → Gemini API
                                       ↓
                                   Firestore
                                       ↓
                                 SendGrid Send → User Email
```

**Tech Stack:**
- **Compute:** Cloud Functions for Firebase (Node.js/TypeScript)
- **Database:** Firestore (conversation storage)
- **LLM:** Google Gemini API (gemini-1.5-flash)
- **Email:** SendGrid (inbound + outbound)
- **Hosting:** Firebase (free tier)

## Project Status

**Current:** Technical specification complete, minimal prototype in development

**Completed:**
- [x] System design
- [x] Technical specification
- [ ] Minimal prototype (in progress)
- [ ] Full implementation
- [ ] Testing and deployment

## Quick Start

### Prerequisites

- Node.js 18+ and npm
- Firebase account
- SendGrid account (free tier)
- Gemini API key (free tier)

### Setup

```bash
# 1. Clone the repository
cd apps/email-llm-poc

# 2. Install Firebase CLI
npm install -g firebase-tools

# 3. Install dependencies
cd functions
npm install

# 4. Set up Firebase project
firebase login
firebase init

# 5. Configure environment variables
firebase functions:secrets:set SENDGRID_API_KEY
firebase functions:secrets:set GEMINI_API_KEY
firebase functions:config:set app.bot_email="your-bot@yourdomain.sendgrid.net"

# 6. Run locally with emulators
firebase emulators:start

# 7. Deploy to Firebase
firebase deploy --only functions
```

See [docs/SETUP.md](docs/SETUP.md) for detailed setup instructions.

## Usage

### Sending Your First Email

1. Send an email to your bot's address: `chatbot@yourdomain.sendgrid.net`
2. Wait a few seconds for processing
3. Receive a reply in your inbox
4. Reply to continue the conversation

### Example Conversation

```
From: user@example.com
To: chatbot@yourdomain.sendgrid.net
Subject: Hello!

Can you explain what quantum computing is?

---

From: chatbot@yourdomain.sendgrid.net
To: user@example.com
Subject: Re: Hello!

Quantum computing is a type of computation that harnesses...
[response continues]

---

From: user@example.com
To: chatbot@yourdomain.sendgrid.net
Subject: Re: Hello!

Thanks! Can you give me an example of how it's used?

[Conversation continues with full context...]
```

## Features

### Current Features

- **Conversation Threading:** Proper email thread management
- **Context Preservation:** Up to 20 messages of history
- **Rate Limiting:** 50 messages per day per user
- **Error Handling:** Graceful errors with user notifications
- **Auto-cleanup:** Archives old conversations after 30 days

### Planned Features (Phase 2)

- Web dashboard to view conversations
- Conversation export (PDF, JSON)
- Custom system prompts per user
- Image attachment support (Gemini multimodal)
- Command syntax (`/reset`, `/help`, etc.)

## Documentation

- [Technical Specification](docs/TECHNICAL_SPEC.md) - Detailed system design
- [Setup Guide](docs/SETUP.md) - Step-by-step setup instructions
- [Development Notes](NOTES.md) - Implementation decisions and learnings
- [System Prompts](prompts/) - LLM prompts and templates

## Development

### Project Structure

```
email-llm-poc/
├── README.md                 # This file
├── NOTES.md                  # Development notes
├── ICEBOX.md                 # Future ideas
├── docs/
│   ├── TECHNICAL_SPEC.md     # System design
│   └── SETUP.md              # Setup guide
├── functions/
│   ├── src/
│   │   ├── index.ts          # Main Cloud Function
│   │   ├── email.ts          # Email processing
│   │   ├── gemini.ts         # Gemini API integration
│   │   ├── firestore.ts      # Database operations
│   │   └── utils.ts          # Utilities
│   ├── package.json
│   └── tsconfig.json
├── prompts/
│   └── system_prompt.md      # Default system prompt
└── firebase.json             # Firebase configuration
```

### Local Development

```bash
# Start Firebase emulators
firebase emulators:start

# Function URL will be at:
# http://localhost:5001/your-project-id/us-central1/processInboundEmail

# Use ngrok for SendGrid webhook testing
ngrok http 5001

# Point SendGrid Inbound Parse to ngrok URL
```

### Testing

```bash
# Run unit tests
cd functions
npm test

# Test webhook locally
curl -X POST http://localhost:5001/.../processInboundEmail \
  -H "Content-Type: multipart/form-data" \
  -F "from=test@example.com" \
  -F "to=chatbot@yourdomain.sendgrid.net" \
  -F "subject=Test" \
  -F "text=Hello bot!"
```

## Costs

**Free Tier Limits:**
- Firebase: 50K Firestore reads, 20K writes per day
- SendGrid: 100 emails per day
- Gemini: 60 requests per minute
- **Total: $0/month** for light usage

**Estimated Costs (1000 users):**
- Firebase: ~$5-10/month
- SendGrid: ~$15/month (400 emails/day)
- Gemini: Free (well within limits)
- **Total: ~$20-25/month**

## Security & Privacy

- Rate limiting prevents abuse
- Webhook signature verification
- No conversation data used for AI training
- Conversations archived after 30 days
- GDPR/CCPA compliant data handling
- API keys stored securely in Firebase secrets

## Troubleshooting

**Email not received by bot:**
- Check SendGrid Inbound Parse configuration
- Verify webhook URL is correct
- Check Cloud Function logs

**No reply from bot:**
- Check Cloud Function logs for errors
- Verify Gemini API key is valid
- Check rate limits haven't been exceeded

**Conversation context lost:**
- Verify email threading headers are preserved
- Check Firestore for conversation data
- Ensure Messages-ID headers are unique

See [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) for more help.

## Contributing

This is a proof-of-concept project. Contributions, ideas, and feedback are welcome!

## License

MIT License - See LICENSE file for details

## Acknowledgments

- Built with [Claude Code](https://claude.ai/code)
- Powered by [Google Gemini](https://ai.google.dev)
- Email infrastructure by [SendGrid](https://sendgrid.com)
- Hosted on [Firebase](https://firebase.google.com)

## Contact

For questions or feedback, please open an issue on GitHub.
