# Feature Backlog (ICEBOX)

Future enhancements and ideas for the Email-to-LLM conversation system.

## High Priority

### Command Syntax
**Description:** Allow users to send special commands via email

**Commands:**
- `/reset` - Clear conversation history
- `/help` - Get usage instructions
- `/export` - Email conversation transcript
- `/stats` - View usage statistics
- `/persona <name>` - Switch AI persona

**Implementation:**
- Parse message body for commands (must be first line)
- Execute command instead of calling Gemini
- Send formatted response

**Complexity:** Medium
**Value:** High

---

### Image Attachment Support
**Description:** Process images in email attachments using Gemini's multimodal capabilities

**Use Cases:**
- "What's in this image?"
- "Transcribe text from this photo"
- "Describe this diagram"

**Implementation:**
- Parse attachments from SendGrid webhook
- Convert to base64 or URL
- Include in Gemini API call
- Handle multiple images

**Complexity:** Medium
**Value:** High

---

### Web Dashboard
**Description:** Web interface to view and manage conversations

**Features:**
- View all conversations
- Search message history
- Export conversations
- Delete conversations
- View usage statistics

**Tech Stack:**
- Next.js or Remix
- Firebase Authentication
- Firestore queries
- Hosted on Firebase Hosting

**Complexity:** High
**Value:** High

---

### Better Email Parsing
**Description:** Use ML to better detect signatures, quotes, and disclaimers

**Current Issues:**
- Some signatures don't use `--` delimiter
- Corporate disclaimers confuse the bot
- Nested quotes not handled well

**Solutions:**
- Train simple classifier (signature vs content)
- Use regex patterns for common formats
- Strip common disclaimer text

**Complexity:** Medium
**Value:** Medium

---

### Conversation Export
**Description:** Export conversations in multiple formats

**Formats:**
- **PDF:** Nicely formatted conversation
- **JSON:** Machine-readable format
- **Markdown:** Plain text with formatting
- **CSV:** For data analysis

**Delivery:**
- Email with attachment
- Download from web dashboard
- Automatic periodic exports

**Complexity:** Medium
**Value:** Medium

---

## Medium Priority

### Custom System Prompts
**Description:** Allow users to customize the AI's behavior

**Implementation:**
- Store per-user system prompt in Firestore
- Command to set: `/prompt You are a helpful coding assistant...`
- Prepend to every Gemini API call

**Use Cases:**
- Coding assistant
- Writing coach
- Language tutor
- Domain expert

**Complexity:** Low
**Value:** Medium

---

### Scheduled Messages
**Description:** Bot can send proactive emails on schedule

**Use Cases:**
- Daily reminders
- Weekly summaries
- Follow-up questions
- Habit tracking

**Implementation:**
- Cloud Scheduler triggers function
- Query users with scheduled messages
- Send via SendGrid API

**Complexity:** Medium
**Value:** Low

---

### Premium Tier
**Description:** Paid tier with enhanced features

**Premium Features:**
- Higher rate limits (500 messages/day)
- Faster responses (dedicated instances)
- Priority support
- Custom branding
- API access

**Pricing:**
- $10/month per user
- $50/month for teams (10 users)

**Implementation:**
- Stripe integration
- User subscriptions in Firestore
- Feature flags based on tier

**Complexity:** High
**Value:** Medium (if scale is reached)

---

### Multi-Language Support
**Description:** Detect and respond in user's language

**Implementation:**
- Detect language from email
- Set Gemini language parameter
- Translate system prompts

**Languages:**
- Spanish
- French
- German
- Japanese
- Chinese

**Complexity:** Low
**Value:** Medium

---

### Email Templates
**Description:** Pre-built templates for common responses

**Templates:**
- Welcome email (first time users)
- Rate limit notification
- Error notification
- Weekly summary
- Conversation export

**Implementation:**
- Store templates in Firestore or files
- Use template engine (Handlebars, EJS)
- Inject dynamic data

**Complexity:** Low
**Value:** Medium

---

## Low Priority

### Voice Note Support
**Description:** Process audio attachments and respond with text

**Implementation:**
- Detect audio attachments
- Transcribe with Whisper API
- Process as text message
- Optional: Respond with audio (TTS)

**Complexity:** High
**Value:** Low

---

### Team Accounts
**Description:** Multiple users share conversations

**Features:**
- Team email address
- Shared conversation history
- @mentions for specific users
- Role-based access

**Implementation:**
- Team collection in Firestore
- Permission system
- User management UI

**Complexity:** High
**Value:** Low (for POC)

---

### Conversation Sharing
**Description:** Share conversations with others

**Features:**
- Generate shareable link
- Optional: Password protection
- Optional: Expiration date
- View-only mode

**Implementation:**
- Public conversation endpoint
- Short URL generation
- Access control

**Complexity:** Medium
**Value:** Low

---

### Mobile App
**Description:** Native iOS/Android clients

**Features:**
- Push notifications
- Faster than email
- Richer UI
- Voice input

**Tech:**
- React Native or Flutter
- Firebase SDKs
- App Store / Play Store

**Complexity:** Very High
**Value:** Low (for POC)

---

### Integrations

#### Calendar Integration
- "Schedule a meeting for next Tuesday at 2pm"
- "What's on my calendar today?"
- Google Calendar API
- **Complexity:** High, **Value:** Medium

#### Task Management
- "Add buy milk to my todo list"
- "What tasks are due this week?"
- Todoist, Asana, or custom
- **Complexity:** Medium, **Value:** Medium

#### Note Taking
- "Save this to my notes"
- "Search my notes for X"
- Notion, Evernote, or custom
- **Complexity:** Medium, **Value:** Low

#### Email Client Integration
- Chrome/Firefox extension
- Gmail add-on
- Outlook plugin
- **Complexity:** High, **Value:** Low

---

## Technical Improvements

### Performance Optimization
- **Caching:** Cache Gemini responses for identical queries
- **Connection pooling:** Reuse HTTP connections
- **Lazy loading:** Load message history on demand
- **Compression:** Gzip Firestore data
- **CDN:** Serve static assets via CDN

**Complexity:** Medium
**Value:** Low (premature optimization)

---

### Advanced Rate Limiting
- **Token bucket algorithm:** More fair than daily limit
- **Sliding window:** Count messages over rolling 24 hours
- **Per-feature limits:** Different limits for different commands
- **Burst allowance:** Allow short bursts of messages

**Complexity:** High
**Value:** Low (current approach works)

---

### Monitoring & Analytics
- **Custom dashboard:** Real-time metrics
- **Alerting:** Slack/PagerDuty integration
- **User analytics:** Usage patterns, retention
- **A/B testing:** Test different prompts
- **Cost tracking:** Monitor spend per user

**Complexity:** High
**Value:** Medium

---

### Testing Infrastructure
- **E2E tests:** Full email flow testing
- **Load tests:** Simulate 1000s of concurrent users
- **Chaos engineering:** Test failure scenarios
- **Smoke tests:** Post-deploy verification

**Complexity:** High
**Value:** Medium

---

### Security Enhancements
- **Spam detection:** ML-based spam filter
- **Content moderation:** Filter inappropriate content
- **DDoS protection:** Rate limiting by IP
- **Anomaly detection:** Detect unusual usage patterns
- **Encryption:** End-to-end encryption for messages

**Complexity:** High
**Value:** Medium

---

## Research & Experiments

### Conversation Summarization
Automatically summarize long conversations to save tokens

**Approaches:**
- Periodic summarization (every 10 messages)
- On-demand summarization
- Hierarchical summarization

**Complexity:** Medium
**Value:** Medium

---

### Smart Context Selection
Instead of last N messages, select most relevant messages

**Approaches:**
- Embedding-based similarity
- Recency + relevance scoring
- Entity extraction and tracking

**Complexity:** High
**Value:** Low (likely premature)

---

### Multi-Modal Responses
Send images, charts, or diagrams via email

**Use Cases:**
- Generate charts from data
- Create diagrams from descriptions
- Visualize concepts

**Tools:**
- Chart.js for graphs
- Mermaid for diagrams
- DALL-E for images

**Complexity:** High
**Value:** Low

---

### Conversation Branching
Fork conversations to explore different topics

**Implementation:**
- Track conversation tree in Firestore
- Allow users to branch with command
- Navigate branches via commands

**Complexity:** High
**Value:** Low

---

## Ideas from Users

_This section will be populated as users provide feedback_

---

## Won't Do (At Least For Now)

### SMS Support
**Reason:** Adds complexity, SMS costs are high, email is the focus

### Video Attachments
**Reason:** Large files, complex processing, limited use cases

### Real-Time Chat
**Reason:** Email is intentionally async, use dedicated chat apps for real-time

### Blockchain/Web3 Integration
**Reason:** No clear benefit, adds complexity

### Social Media Integration
**Reason:** Out of scope, privacy concerns

---

**Last Updated:** November 11, 2025
