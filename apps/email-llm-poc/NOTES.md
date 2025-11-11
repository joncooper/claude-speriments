# Development Notes

## Design Decisions

### Why Firebase over AWS?

**Considered Options:**
1. **Firebase (GCP)** - Selected ✓
2. AWS (SES + Lambda + DynamoDB)
3. Azure (Functions + CosmosDB)

**Rationale for Firebase:**
- **Simpler setup:** Firebase CLI handles most configuration
- **Better DX:** Firestore SDK is more intuitive than DynamoDB
- **Local development:** Firebase emulators provide full local testing
- **Unified ecosystem:** Functions, Firestore, and Logging are tightly integrated
- **Natural fit:** Both Firebase and Gemini are Google services
- **Generous free tier:** 50K Firestore reads/day, 20K writes/day
- **Quick iteration:** Deploy functions in seconds

**AWS Alternative:**
- More mature, more examples in the wild
- SES has native email receiving (no SendGrid needed)
- Slightly cheaper at very high scale
- BUT: More complex setup, steeper learning curve, less pleasant DX

### Why SendGrid for Email?

**Alternatives considered:**
- Amazon SES (requires S3 + Lambda rules)
- Mailgun (similar to SendGrid)
- Postmark (more expensive)
- Cloud Email API (GCP, limited features)

**SendGrid advantages:**
- Webhook-based inbound parsing (no S3 needed)
- Handles email parsing automatically
- Same service for sending and receiving
- Clean API for maintaining email threads
- 100 emails/day free tier

### Why Gemini over other LLMs?

**Alternatives:**
- OpenAI GPT-4 (more expensive, $10+ for 1M tokens)
- Anthropic Claude (more expensive, excellent but pricey)
- Local LLMs (complex deployment, resource intensive)

**Gemini advantages:**
- Generous free tier (60 requests/minute)
- Good performance (gemini-1.5-flash is fast)
- Multimodal support (images)
- Natural fit with GCP ecosystem
- Simple API

### Conversation Context Strategy

**Decision:** Store last 20 messages in Firestore, send to Gemini on each request

**Alternatives considered:**
1. Store only message IDs, fetch full text on demand (adds latency)
2. Store unlimited history (increases Firestore costs and Gemini token usage)
3. Summarize old messages (adds complexity, loses detail)

**Rationale:**
- 20 messages = ~5-10 back-and-forth turns
- Sufficient for most conversations
- Keeps token usage manageable
- Simple to implement
- Can be configured per deployment

### Email Threading Approach

**Decision:** Use `In-Reply-To` and `References` headers to maintain threads

**Key Implementation Details:**
- Extract `Message-ID` from inbound email
- Include as `In-Reply-To` in reply
- Build `References` chain from all previous message IDs
- Use thread ID as Firestore conversation ID

**Why this works:**
- All modern email clients respect these headers
- Keeps conversations together in inbox
- Standard email practice

### Rate Limiting Strategy

**Decision:** 50 messages/day per email address, reset at midnight UTC

**Alternatives considered:**
1. Token-based rate limiting (complex)
2. Sliding window (more fair, but complex)
3. Per-hour limits (too restrictive for bursty usage)

**Rationale:**
- Simple to implement
- Easy to explain to users
- Prevents abuse without hurting normal users
- Aligns with free tier limits

**Why reset at midnight UTC:**
- Predictable for users
- Simple implementation
- Matches common rate limit patterns

## Implementation Challenges

### Challenge 1: Email Parsing

**Problem:** Email bodies contain quoted text, signatures, and HTML

**Solution:**
```javascript
// Strip everything after common quote markers
const quoteMarkers = [
  '\n\nOn ', // Gmail, Outlook
  '\n\n>',   // Plain text quotes
  '\n\n--'   // Signature delimiter
];

function extractCleanBody(rawBody) {
  let clean = rawBody;
  for (const marker of quoteMarkers) {
    const index = clean.indexOf(marker);
    if (index !== -1) {
      clean = clean.substring(0, index);
    }
  }
  return clean.trim();
}
```

**Considerations:**
- Different email clients use different quote formats
- Some signatures don't use `--` delimiter
- HTML emails need to be converted to plain text
- May need ML-based quote detection in the future

### Challenge 2: Webhook Security

**Problem:** Need to verify requests are actually from SendGrid

**Solution:**
SendGrid doesn't provide signature verification by default, but we can:
1. Use HTTPS (TLS ensures origin)
2. Check webhook verification key in request (if SendGrid adds it)
3. Rate limit by IP (Cloud Functions handles this)
4. Monitor logs for suspicious activity

**Better solution for production:**
- Use SendGrid's Event Webhook with signature verification
- Implement custom verification token in URL

### Challenge 3: Error Handling

**Problem:** SendGrid retries failed webhooks, could cause duplicate processing

**Solution:**
- Always return 200 to SendGrid (even on errors)
- Handle errors internally
- Use Firestore transactions to prevent duplicate messages
- Idempotency key from email Message-ID

### Challenge 4: Conversation Threading

**Problem:** How to link email threads to Firestore conversations?

**Solution:**
Use email `References` header as conversation ID:
- First email: Use Message-ID as conversation ID
- Reply emails: Use first Message-ID in References chain
- Fallback: Create hash of (from + subject) if headers missing

### Challenge 5: Token Usage

**Problem:** Long conversations consume many tokens

**Solutions implemented:**
1. Limit to last 20 messages (configurable)
2. Use gemini-1.5-flash (cheaper than Pro)
3. Monitor token usage in Firestore
4. Alert if approaching limits

**Future optimization:**
- Summarize old messages
- Intelligent context selection (keep only relevant messages)
- Switch to cheaper model for simple queries

## Performance Considerations

### Cold Starts

Cloud Functions for Firebase can have cold starts (1-3 seconds):
- **Mitigation:** Use minimum instances (costs $, not for POC)
- **Acceptable:** Users expect email replies to take a few seconds anyway
- **Future:** Could use Cloud Run for faster cold starts

### Latency Breakdown

Expected latency for email processing:
- SendGrid webhook → Cloud Function: ~100-200ms
- Load conversation from Firestore: ~50-100ms
- Call Gemini API: ~2-5s (varies by response length)
- Save to Firestore: ~50-100ms
- Send via SendGrid: ~100-200ms
- **Total: ~3-6 seconds** (acceptable for email)

### Scalability

**Current architecture scales to:**
- ~1,000 users (Firestore free tier)
- ~100 emails/day (SendGrid free tier)
- ~5,000 emails/day (Gemini free tier at 1 request/user/day)

**Bottlenecks:**
1. SendGrid free tier (100 emails/day)
2. Firestore free tier (50K reads/day)
3. Cloud Functions free tier (2M invocations/month)

**Scaling strategy:**
- Upgrade SendGrid first ($15/mo for 400 emails/day)
- Firestore scales automatically (pay as you go)
- Cloud Functions scale automatically

## Security Considerations

### API Key Management

**Decision:** Use Firebase Environment Config for secrets

```bash
# Set secrets
firebase functions:secrets:set SENDGRID_API_KEY
firebase functions:secrets:set GEMINI_API_KEY

# Access in code
const sendgridKey = process.env.SENDGRID_API_KEY;
```

**Why not .env files:**
- Security risk if committed to git
- Manual deployment needed
- Firebase secrets are encrypted at rest

### Input Validation

**Implemented:**
- Email format validation
- Message length limits (10,000 chars)
- HTML sanitization

**Not yet implemented:**
- Spam detection
- Content filtering
- Email domain blocklist

### Data Privacy

**Considerations:**
- Store only necessary data (email address, messages)
- No tracking or analytics beyond basic metrics
- Archive old conversations
- Provide data export/deletion on request

**GDPR Compliance:**
- Right to access: Provide conversation export
- Right to deletion: Delete user data on request
- Right to rectification: Allow editing/deleting messages
- Data minimization: Store only what's needed

## Testing Strategy

### Unit Tests

**Covered:**
- Email parsing (quote removal, signature stripping)
- Rate limiting logic
- Message formatting for Gemini
- Error handling

**Tools:**
- Jest for testing
- Supertest for HTTP testing
- Firebase emulators for Firestore testing

### Integration Tests

**Covered:**
- Full email processing flow
- SendGrid webhook handling
- Gemini API integration
- Firestore operations

**Approach:**
- Use Firebase emulators for local testing
- Mock SendGrid and Gemini APIs
- Test error scenarios

### Manual Testing

**Test Cases:**
1. Send first email to bot
2. Receive response
3. Reply to continue conversation
4. Test with 21+ messages (context limit)
5. Test rate limiting (send 51 messages)
6. Test error handling (disconnect Gemini API)
7. Test email threading in different clients (Gmail, Outlook, Apple Mail)

## Lessons Learned

### 1. Firebase Emulators are Excellent

The Firebase emulator suite provides:
- Local Firestore database
- Local Cloud Functions
- Local authentication
- Full offline development

**Recommendation:** Start every session with emulators running

### 2. Email Threading is Complex

Different email clients handle threading differently:
- Gmail uses References header
- Outlook prefers In-Reply-To
- Apple Mail uses both

**Solution:** Include both headers in every reply

### 3. SendGrid Webhook Payload is Large

The webhook includes:
- Full email headers (can be 10KB+)
- Attachments (can be MB)
- HTML and plain text versions

**Optimization:** Parse only what's needed, ignore rest

### 4. Gemini API is Fast

gemini-1.5-flash typically responds in 1-3 seconds for short responses.

**Insight:** Most latency is from email sending, not LLM processing

### 5. Firestore is Great for This Use Case

Document-based structure maps naturally to conversations:
```
conversations/{conversationId}/messages/{messageId}
```

Subcollections keep related data together, queries are fast.

## Future Improvements

### Short Term (Next Iteration)

1. **Better email parsing:** Use ML to detect signatures/quotes
2. **Command syntax:** `/reset`, `/help`, `/export`
3. **Logging dashboard:** Web UI to view conversations
4. **Retry logic:** Exponential backoff for failed Gemini calls
5. **Metrics:** Token usage, latency, error rates

### Medium Term (Phase 2)

1. **Multimodal support:** Process image attachments
2. **Custom prompts:** Per-user system prompts
3. **Conversation export:** PDF, JSON, Markdown
4. **Web interface:** View/manage conversations
5. **Premium tier:** Higher rate limits, faster responses

### Long Term (Phase 3)

1. **Voice support:** Audio attachments via Whisper API
2. **Scheduled messages:** Send reminders via email
3. **Team accounts:** Shared conversations
4. **Integrations:** Calendar, tasks, notes
5. **Mobile app:** Native iOS/Android clients

## Resources

**Documentation:**
- [Firebase Functions](https://firebase.google.com/docs/functions)
- [Firestore](https://firebase.google.com/docs/firestore)
- [SendGrid Inbound Parse](https://docs.sendgrid.com/for-developers/parsing-email/setting-up-the-inbound-parse-webhook)
- [Gemini API](https://ai.google.dev/docs)

**Tools:**
- [Firebase CLI](https://firebase.google.com/docs/cli)
- [SendGrid Node.js SDK](https://github.com/sendgrid/sendgrid-nodejs)
- [Google AI SDK](https://www.npmjs.com/package/@google/generative-ai)

**Examples:**
- [Firebase Email Templates](https://github.com/firebase/functions-samples/tree/main/email-confirmation)
- [SendGrid Inbound Parse Example](https://github.com/sendgrid/sendgrid-nodejs/tree/main/examples)

---

**Last Updated:** November 11, 2025
