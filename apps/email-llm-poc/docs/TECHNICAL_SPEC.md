# Technical Specification: Email-to-LLM Conversation System

**Version:** 1.0
**Last Updated:** November 2025
**Status:** Design Phase

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Component Specifications](#component-specifications)
3. [Data Models](#data-models)
4. [API Contracts](#api-contracts)
5. [Error Handling](#error-handling)
6. [Security](#security)
7. [Rate Limiting](#rate-limiting)
8. [Deployment](#deployment)
9. [Testing Strategy](#testing-strategy)
10. [Monitoring & Observability](#monitoring--observability)

---

## Architecture Overview

### System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                          Email-to-LLM System                         │
└─────────────────────────────────────────────────────────────────────┘

External Services:
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│  SendGrid   │         │   Gemini    │         │  Firebase   │
│  Inbound    │         │     API     │         │   Platform  │
└──────┬──────┘         └──────▲──────┘         └──────▲──────┘
       │                       │                        │
       │                       │                        │
       ▼                       │                        │
┌─────────────────────────────┴────────────────────────┴──────┐
│              Cloud Functions for Firebase                    │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  processInboundEmail (HTTP Trigger)                  │   │
│  │  - Validates webhook signature                       │   │
│  │  - Parses email content                              │   │
│  │  - Manages conversation state                        │   │
│  │  - Calls Gemini API                                  │   │
│  │  - Sends email response                              │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  cleanupOldConversations (Scheduled, daily)          │   │
│  │  - Archives conversations older than 30 days         │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │    Firestore     │
                    │                  │
                    │  conversations/  │
                    │  users/          │
                    │  audit_logs/     │
                    └──────────────────┘
```

### Technology Stack

| Component | Technology | Justification |
|-----------|------------|---------------|
| Email Receiving | SendGrid Inbound Parse | Webhook-based, reliable, handles parsing |
| Email Sending | SendGrid API | Same service, maintains threading |
| Compute | Cloud Functions for Firebase | Serverless, auto-scaling, simple deployment |
| Database | Firestore | Document-based, real-time, generous free tier |
| LLM | Google Gemini API | Free tier, multimodal, good performance |
| Logging | Cloud Logging | Native Firebase integration |
| Secrets | Firebase Environment Config | Built-in secrets management |

### Data Flow

**Inbound Email Processing:**

1. User sends email to `chatbot@yourdomain.sendgrid.net`
2. SendGrid Inbound Parse webhook triggers `processInboundEmail` function
3. Function validates SendGrid signature
4. Function extracts email metadata and content
5. Function loads conversation history from Firestore (or creates new)
6. Function builds message context for Gemini
7. Function calls Gemini API
8. Function stores response in Firestore
9. Function sends reply via SendGrid API with proper threading headers
10. Function logs metrics to Firestore and Cloud Logging

---

## Component Specifications

### 1. Cloud Function: processInboundEmail

**Trigger:** HTTP POST from SendGrid Inbound Parse

**Environment Variables:**
```bash
SENDGRID_API_KEY=SG.xxxxx
SENDGRID_WEBHOOK_VERIFICATION_KEY=xxxxx
GEMINI_API_KEY=xxxxx
BOT_EMAIL_ADDRESS=chatbot@yourdomain.sendgrid.net
MAX_MESSAGES_PER_DAY_PER_USER=50
MAX_CONVERSATION_HISTORY=20
```

**Request Flow:**

```javascript
async function processInboundEmail(req, res) {
  try {
    // 1. Validate webhook signature
    if (!validateSendGridWebhook(req)) {
      return res.status(401).send('Unauthorized');
    }

    // 2. Parse email
    const emailData = parseInboundEmail(req.body);

    // 3. Rate limiting check
    const rateLimitResult = await checkRateLimit(emailData.fromEmail);
    if (!rateLimitResult.allowed) {
      await sendRateLimitEmail(emailData.fromEmail);
      return res.status(200).send('Rate limit email sent');
    }

    // 4. Load or create conversation
    const conversation = await getOrCreateConversation(
      emailData.threadId,
      emailData.fromEmail
    );

    // 5. Add user message to conversation
    await addMessage(conversation.id, {
      role: 'user',
      content: emailData.cleanBody,
      timestamp: new Date(),
      emailMessageId: emailData.messageId
    });

    // 6. Call Gemini API
    const geminiResponse = await callGemini(
      conversation.id,
      emailData.cleanBody
    );

    // 7. Store assistant response
    await addMessage(conversation.id, {
      role: 'assistant',
      content: geminiResponse.content,
      timestamp: new Date(),
      metadata: geminiResponse.metadata
    });

    // 8. Send email reply
    await sendEmailReply(
      emailData.fromEmail,
      emailData.subject,
      geminiResponse.content,
      emailData.messageId,
      emailData.references
    );

    // 9. Log metrics
    await logMetrics(conversation.id, geminiResponse.metadata);

    return res.status(200).send('Email processed');

  } catch (error) {
    console.error('Error processing email:', error);
    await logError(error, req.body);

    // Send error notification to user if possible
    if (req.body?.from) {
      await sendErrorEmail(req.body.from);
    }

    return res.status(500).send('Error processing email');
  }
}
```

### 2. Cloud Function: cleanupOldConversations

**Trigger:** Cloud Scheduler (daily at 2 AM UTC)

**Purpose:** Archive conversations older than 30 days to manage Firestore costs

```javascript
async function cleanupOldConversations() {
  const thirtyDaysAgo = new Date();
  thirtyDaysAgo.setDate(thirtyDaysAgo.getDate() - 30);

  const oldConversations = await firestore
    .collection('conversations')
    .where('updatedAt', '<', thirtyDaysAgo)
    .get();

  for (const doc of oldConversations.docs) {
    await archiveConversation(doc.id);
  }

  console.log(`Archived ${oldConversations.size} conversations`);
}
```

---

## Data Models

### Firestore Schema

#### Collection: `conversations`

```typescript
interface Conversation {
  id: string;                    // Auto-generated document ID
  threadId: string;              // Email thread ID (from References header)
  userEmail: string;             // User's email address
  createdAt: Timestamp;          // First message timestamp
  updatedAt: Timestamp;          // Last message timestamp
  messageCount: number;          // Total messages in conversation
  status: 'active' | 'archived'; // Conversation status

  // Metadata
  metadata: {
    firstSubject: string;        // Original email subject
    lastMessageAt: Timestamp;    // Last activity
    totalTokensUsed: number;     // Total Gemini tokens across conversation
  };
}

// Subcollection: conversations/{conversationId}/messages
interface Message {
  id: string;                    // Auto-generated
  role: 'user' | 'assistant';    // Message sender
  content: string;               // Message text
  timestamp: Timestamp;          // When message was created
  emailMessageId?: string;       // Original email message ID

  // Gemini-specific metadata (for assistant messages)
  geminiMetadata?: {
    model: string;               // e.g., "gemini-1.5-flash"
    promptTokens: number;
    completionTokens: number;
    totalTokens: number;
    finishReason: string;
    latencyMs: number;           // API call duration
  };
}
```

#### Collection: `users`

```typescript
interface User {
  email: string;                 // Document ID
  createdAt: Timestamp;          // First interaction
  lastMessageAt: Timestamp;      // Last message timestamp

  // Rate limiting
  dailyMessageCount: number;     // Messages today
  dailyResetAt: Timestamp;       // When to reset counter

  // Statistics
  stats: {
    totalConversations: number;
    totalMessages: number;
    totalTokensUsed: number;
  };

  // Flags
  blocked: boolean;              // Whether user is blocked
  blockedReason?: string;        // Why user was blocked
}
```

#### Collection: `audit_logs`

```typescript
interface AuditLog {
  id: string;                    // Auto-generated
  timestamp: Timestamp;
  eventType: string;             // 'email_received', 'email_sent', 'error', etc.
  userEmail?: string;
  conversationId?: string;

  // Event-specific data
  data: {
    [key: string]: any;
  };

  // Error tracking
  error?: {
    message: string;
    stack: string;
    code: string;
  };
}
```

---

## API Contracts

### SendGrid Inbound Parse Webhook

**Endpoint:** `POST /processInboundEmail`

**Headers:**
```
Content-Type: multipart/form-data
```

**Request Body (Form Data):**
```javascript
{
  "headers": "Received: from mail.example.com...",  // Full email headers
  "dkim": "{@example.com : pass}",                   // DKIM verification
  "from": "User Name <user@example.com>",            // Sender
  "to": "chatbot@yourdomain.sendgrid.net",           // Recipient
  "subject": "Re: Previous conversation",            // Subject line
  "text": "This is the email body...",               // Plain text body
  "html": "<html>This is the email body...</html>",  // HTML body (if present)
  "envelope": "{\"to\":[\"chatbot@...\"],\"from\":\"user@...\"}",
  "charsets": "{\"to\":\"UTF-8\",\"subject\":\"UTF-8\"}",
  "SPF": "pass",

  // Attachment fields (if present)
  "attachment-info": "{\"attachment1\":{\"filename\":\"image.jpg\",...}}",
  "attachment1": <binary data>
}
```

**Response:**
- `200 OK`: Email processed successfully
- `401 Unauthorized`: Invalid webhook signature
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Processing error

### Gemini API

**Endpoint:** `POST https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent`

**Request:**
```json
{
  "contents": [
    {
      "role": "user",
      "parts": [{"text": "Hello!"}]
    },
    {
      "role": "model",
      "parts": [{"text": "Hi there! How can I help?"}]
    },
    {
      "role": "user",
      "parts": [{"text": "What's the weather like?"}]
    }
  ],
  "generationConfig": {
    "temperature": 0.7,
    "maxOutputTokens": 1024,
    "topP": 0.95,
    "topK": 40
  }
}
```

**Response:**
```json
{
  "candidates": [
    {
      "content": {
        "parts": [{"text": "I don't have access to real-time weather..."}],
        "role": "model"
      },
      "finishReason": "STOP",
      "safetyRatings": [...]
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 45,
    "candidatesTokenCount": 23,
    "totalTokenCount": 68
  }
}
```

### SendGrid Send Email API

**Endpoint:** `POST https://api.sendgrid.com/v3/mail/send`

**Headers:**
```
Authorization: Bearer SG.xxxxx
Content-Type: application/json
```

**Request:**
```json
{
  "personalizations": [
    {
      "to": [{"email": "user@example.com"}]
    }
  ],
  "from": {
    "email": "chatbot@yourdomain.sendgrid.net",
    "name": "AI Assistant"
  },
  "subject": "Re: Previous conversation",
  "content": [
    {
      "type": "text/plain",
      "value": "This is the reply message..."
    }
  ],
  "headers": {
    "In-Reply-To": "<original-message-id@example.com>",
    "References": "<thread-id@example.com> <original-message-id@example.com>"
  }
}
```

**Response:**
- `202 Accepted`: Email queued for delivery

---

## Error Handling

### Error Categories

| Error Type | HTTP Code | User Action | System Action |
|------------|-----------|-------------|---------------|
| Invalid webhook signature | 401 | None | Log and alert |
| Rate limit exceeded | 200* | Receive rate limit email | Update user record |
| Gemini API error | 200* | Receive error email | Retry 3x with backoff |
| Firestore error | 200* | Receive error email | Log and alert |
| SendGrid send error | 200* | None (can't notify) | Log and alert |
| Parsing error | 200* | Receive error email | Log |

*Note: Return 200 to SendGrid to prevent retries (we handle errors internally)

### Error Handling Strategy

```javascript
// Retry logic for Gemini API
async function callGeminiWithRetry(messages, maxRetries = 3) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await callGemini(messages);
    } catch (error) {
      if (attempt === maxRetries || !isRetryableError(error)) {
        throw error;
      }

      const delayMs = Math.pow(2, attempt) * 1000; // Exponential backoff
      await sleep(delayMs);
    }
  }
}

// Retryable errors
function isRetryableError(error) {
  return [
    'RATE_LIMIT_EXCEEDED',
    'SERVICE_UNAVAILABLE',
    'TIMEOUT'
  ].includes(error.code);
}
```

### User-Facing Error Messages

**Rate Limit Email:**
```
Subject: Daily message limit reached

Hi there,

You've reached the daily limit of 50 messages. Your limit will reset
in [X] hours. Thanks for your understanding!

If you have urgent needs or would like to discuss higher limits,
please contact support@yourdomain.com.

Best,
Your AI Assistant
```

**Processing Error Email:**
```
Subject: Error processing your message

Hi there,

I encountered an error while processing your message. The issue has
been logged and we're looking into it.

Please try resending your message in a few minutes. If the problem
persists, contact support@yourdomain.com with reference ID: [ERROR_ID]

Best,
Your AI Assistant
```

---

## Security

### Authentication & Authorization

1. **SendGrid Webhook Verification**
   - Verify webhook signature on all inbound requests
   - Rotate webhook verification key quarterly
   - Log all failed verification attempts

2. **Email Validation**
   - Validate sender email format
   - Check SPF/DKIM status from SendGrid
   - Blocklist management for abusive senders

3. **API Key Management**
   - Store all API keys in Firebase Environment Config
   - Never log API keys
   - Rotate keys quarterly
   - Use separate keys for dev/staging/prod

### Content Security

1. **Input Sanitization**
   - Strip HTML from email bodies
   - Remove email signatures and quoted text
   - Limit message length (max 10,000 characters)
   - Filter potentially harmful content

2. **Output Validation**
   - Sanitize Gemini responses before sending
   - Check for sensitive information leakage
   - Enforce content policies

3. **Rate Limiting (see dedicated section)**

### Data Privacy

1. **Data Retention**
   - Archive conversations after 30 days
   - Permanently delete archived conversations after 90 days
   - Provide user data export on request
   - Provide user data deletion on request

2. **PII Handling**
   - Email addresses are the only PII stored
   - No conversation content used for training
   - Comply with GDPR/CCPA requirements

3. **Encryption**
   - Firestore encryption at rest (default)
   - TLS for all API communications
   - No client-side encryption needed (server-to-server)

---

## Rate Limiting

### Strategy

**Per-User Limits:**
- 50 messages per day per email address
- Resets at midnight UTC
- Enforced before Gemini API call to avoid token usage

**Global Limits:**
- Gemini API: 60 requests/minute (free tier)
- SendGrid: 100 emails/day (free tier)
- Implement queue if approaching limits

### Implementation

```javascript
async function checkRateLimit(userEmail) {
  const userDoc = await firestore.collection('users').doc(userEmail).get();
  const userData = userDoc.exists ? userDoc.data() : null;

  const now = new Date();
  const todayStart = new Date(now.getFullYear(), now.getMonth(), now.getDate());

  // Check if we need to reset daily counter
  if (!userData || userData.dailyResetAt.toDate() < todayStart) {
    await firestore.collection('users').doc(userEmail).set({
      email: userEmail,
      dailyMessageCount: 0,
      dailyResetAt: getTomorrowStart(),
      lastMessageAt: now,
      createdAt: userData?.createdAt || now
    }, { merge: true });

    return { allowed: true, remaining: 50 };
  }

  // Check if user has exceeded limit
  if (userData.dailyMessageCount >= 50) {
    return {
      allowed: false,
      remaining: 0,
      resetAt: userData.dailyResetAt
    };
  }

  // Increment counter
  await firestore.collection('users').doc(userEmail).update({
    dailyMessageCount: userData.dailyMessageCount + 1,
    lastMessageAt: now
  });

  return {
    allowed: true,
    remaining: 50 - userData.dailyMessageCount - 1
  };
}
```

### Graceful Degradation

If Gemini API rate limit is hit:
1. Queue message for processing
2. Send user an email: "High demand right now. Your message will be processed within 5 minutes."
3. Process queue with backoff
4. Send response when processed

---

## Deployment

### Prerequisites

1. **Firebase Project**
   - Create project at console.firebase.google.com
   - Enable Firestore
   - Enable Cloud Functions
   - Set up billing (required for external API calls)

2. **SendGrid Account**
   - Sign up at sendgrid.com
   - Verify domain
   - Set up Inbound Parse
   - Generate API key

3. **Gemini API Access**
   - Get API key from ai.google.dev
   - Note: Free tier limits

### Deployment Steps

```bash
# 1. Install Firebase CLI
npm install -g firebase-tools

# 2. Login to Firebase
firebase login

# 3. Initialize project
cd apps/email-llm-poc
firebase init functions
# Select TypeScript, ESLint, install dependencies

# 4. Set environment variables
firebase functions:secrets:set SENDGRID_API_KEY
firebase functions:secrets:set SENDGRID_WEBHOOK_VERIFICATION_KEY
firebase functions:secrets:set GEMINI_API_KEY

firebase functions:config:set app.bot_email="chatbot@yourdomain.sendgrid.net"
firebase functions:config:set app.max_messages_per_day="50"

# 5. Deploy
firebase deploy --only functions

# 6. Get function URL
firebase functions:list
# Example: https://us-central1-project-id.cloudfunctions.net/processInboundEmail

# 7. Configure SendGrid Inbound Parse
# Point webhook to function URL
```

### Environment Configuration

**Development (.env.local):**
```bash
SENDGRID_API_KEY=SG.dev_key
SENDGRID_WEBHOOK_VERIFICATION_KEY=dev_verification_key
GEMINI_API_KEY=dev_gemini_key
BOT_EMAIL_ADDRESS=chatbot-dev@yourdomain.sendgrid.net
FIRESTORE_EMULATOR_HOST=localhost:8080
```

**Production (Firebase Environment Config):**
```bash
# Secrets (encrypted)
SENDGRID_API_KEY=SG.prod_key
SENDGRID_WEBHOOK_VERIFICATION_KEY=prod_verification_key
GEMINI_API_KEY=prod_gemini_key

# Config (plain)
app.bot_email=chatbot@yourdomain.sendgrid.net
app.max_messages_per_day=50
app.max_conversation_history=20
```

---

## Testing Strategy

### Unit Tests

Test individual functions in isolation:

```javascript
describe('Email Parser', () => {
  test('extracts clean body from email', () => {
    const rawBody = `Hello!\n\nOn Mon, Nov 11, 2025, User wrote:\n> Previous message`;
    const clean = extractCleanBody(rawBody);
    expect(clean).toBe('Hello!');
  });

  test('handles emails without quoted text', () => {
    const rawBody = 'Just a simple message';
    const clean = extractCleanBody(rawBody);
    expect(clean).toBe('Just a simple message');
  });
});

describe('Rate Limiter', () => {
  test('allows messages under limit', async () => {
    const result = await checkRateLimit('user@example.com');
    expect(result.allowed).toBe(true);
  });

  test('blocks messages over limit', async () => {
    // Set up user with 50 messages
    await setupUserWithMessageCount('user@example.com', 50);

    const result = await checkRateLimit('user@example.com');
    expect(result.allowed).toBe(false);
  });
});
```

### Integration Tests

Test component interactions:

```javascript
describe('End-to-End Email Processing', () => {
  test('processes inbound email and sends reply', async () => {
    const mockRequest = {
      body: createMockSendGridWebhook({
        from: 'user@example.com',
        subject: 'Hello',
        text: 'Can you help me?'
      })
    };

    const mockResponse = createMockResponse();

    await processInboundEmail(mockRequest, mockResponse);

    expect(mockResponse.status).toHaveBeenCalledWith(200);
    expect(sendGridSendMock).toHaveBeenCalledWith(
      expect.objectContaining({
        to: 'user@example.com',
        content: expect.arrayContaining([
          expect.objectContaining({
            value: expect.stringContaining('help')
          })
        ])
      })
    );
  });
});
```

### Manual Testing Checklist

- [ ] Send first email to bot
- [ ] Receive response with proper threading
- [ ] Send reply to maintain conversation context
- [ ] Verify conversation history in Firestore
- [ ] Test rate limiting by sending 51 messages
- [ ] Test error handling by temporarily disabling Gemini API
- [ ] Test email signature stripping
- [ ] Test quoted text removal
- [ ] Test long messages (>10,000 chars)
- [ ] Test special characters and emojis
- [ ] Test HTML emails
- [ ] Test concurrent requests from same user

### Load Testing

Use Artillery or similar tool:

```yaml
config:
  target: 'https://us-central1-project.cloudfunctions.net'
  phases:
    - duration: 60
      arrivalRate: 5
      name: "Warm up"
    - duration: 300
      arrivalRate: 20
      name: "Sustained load"

scenarios:
  - name: "Process emails"
    flow:
      - post:
          url: "/processInboundEmail"
          headers:
            Content-Type: "multipart/form-data"
          form:
            from: "user{{ $randomNumber() }}@example.com"
            to: "chatbot@yourdomain.sendgrid.net"
            subject: "Test message"
            text: "Hello bot!"
```

---

## Monitoring & Observability

### Metrics to Track

**System Metrics:**
- Function execution count
- Function execution duration (p50, p95, p99)
- Function error rate
- Cold start frequency
- Firestore read/write operations
- Firestore query latency

**Application Metrics:**
- Emails received per hour
- Emails sent per hour
- Gemini API calls per hour
- Gemini token usage
- Average conversation length
- Rate limit hits
- Error types and frequency

**Business Metrics:**
- Unique users per day
- Active conversations
- Average response time (user email → bot reply)
- User retention (7-day, 30-day)

### Logging Strategy

**Structured Logging:**

```javascript
function logEvent(eventType, data) {
  console.log(JSON.stringify({
    severity: 'INFO',
    eventType,
    timestamp: new Date().toISOString(),
    ...data
  }));
}

// Usage
logEvent('email_received', {
  from: userEmail,
  conversationId,
  messageLength: body.length
});

logEvent('gemini_api_call', {
  conversationId,
  model: 'gemini-1.5-flash',
  promptTokens: metadata.promptTokens,
  completionTokens: metadata.completionTokens,
  latencyMs: metadata.latencyMs
});
```

### Dashboards

**Cloud Logging Queries:**

```sql
-- Error rate
resource.type="cloud_function"
severity="ERROR"
jsonPayload.eventType="email_processing_error"

-- Slow responses (>5s)
resource.type="cloud_function"
jsonPayload.eventType="email_sent"
jsonPayload.totalLatencyMs>5000

-- Rate limit hits
jsonPayload.eventType="rate_limit_exceeded"
```

**Custom Dashboard Widgets:**
1. Email processing rate (line chart)
2. Error rate (line chart)
3. Gemini token usage (stacked area)
4. Active users (gauge)
5. Average response time (line chart)
6. Rate limit hits (bar chart)

### Alerts

**Critical Alerts (page on-call):**
- Error rate >5% for 5 minutes
- Function failing to deploy
- Firestore unreachable
- SendGrid API errors >10% for 5 minutes

**Warning Alerts (email team):**
- Error rate >2% for 15 minutes
- Gemini API latency >10s (p95) for 10 minutes
- Rate limit approaching (>80% of daily quota)
- Unusual spike in traffic (>200% of baseline)

---

## Appendix

### Conversation Context Management

To keep Gemini API calls efficient and under token limits, manage conversation history:

```javascript
async function buildGeminiContext(conversationId, maxMessages = 20) {
  const messages = await firestore
    .collection('conversations')
    .doc(conversationId)
    .collection('messages')
    .orderBy('timestamp', 'desc')
    .limit(maxMessages)
    .get();

  // Reverse to chronological order
  const chronological = messages.docs.reverse();

  // Format for Gemini API
  return chronological.map(doc => {
    const msg = doc.data();
    return {
      role: msg.role === 'user' ? 'user' : 'model',
      parts: [{ text: msg.content }]
    };
  });
}
```

### Email Threading Headers

To maintain proper email threads:

```javascript
function buildEmailHeaders(inboundEmail) {
  // Extract thread information
  const references = extractHeader(inboundEmail.headers, 'References') || '';
  const inReplyTo = extractHeader(inboundEmail.headers, 'Message-ID');

  // Build References header (chain of all message IDs in thread)
  const allReferences = references
    ? `${references} <${inReplyTo}>`
    : `<${inReplyTo}>`;

  return {
    'In-Reply-To': `<${inReplyTo}>`,
    'References': allReferences
  };
}
```

### Future Enhancements

**Phase 2:**
- Web dashboard to view conversations
- Conversation export (PDF, JSON)
- Multi-language support
- Custom system prompts per user
- Attachment support (images for Gemini multimodal)

**Phase 3:**
- Voice note support (via Whisper API)
- Scheduled messages
- Conversation sharing
- Team accounts
- Premium tier with higher limits

---

## Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-11 | Initial technical specification |

