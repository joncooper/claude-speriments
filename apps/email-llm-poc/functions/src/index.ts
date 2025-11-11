/**
 * Email-to-LLM Conversation System
 * Cloud Functions for Firebase
 */

import * as functions from "firebase-functions";
import * as admin from "firebase-admin";
import {
  initSendGrid,
  parseInboundEmail,
  sendEmailReply,
  sendRateLimitEmail,
  sendErrorEmail,
} from "./email";
import {
  initGemini,
  callGeminiWithSystemPrompt,
} from "./gemini";
import {
  getOrCreateConversation,
  addMessage,
  getConversationHistory,
  checkRateLimit,
  archiveOldConversations,
  logEvent,
  logError,
} from "./firestore";

// Initialize Firebase Admin
admin.initializeApp();

// Configuration
const SENDGRID_API_KEY = process.env.SENDGRID_API_KEY || "";
const GEMINI_API_KEY = process.env.GEMINI_API_KEY || "";
const BOT_EMAIL_ADDRESS = process.env.BOT_EMAIL_ADDRESS || "";
const MAX_MESSAGES_PER_DAY = parseInt(
  process.env.MAX_MESSAGES_PER_DAY_PER_USER || "50"
);
const MAX_CONVERSATION_HISTORY = parseInt(
  process.env.MAX_CONVERSATION_HISTORY || "20"
);

// Initialize APIs
if (SENDGRID_API_KEY) {
  initSendGrid(SENDGRID_API_KEY);
}
if (GEMINI_API_KEY) {
  initGemini(GEMINI_API_KEY);
}

/**
 * HTTP Cloud Function to process inbound emails from SendGrid
 */
export const processInboundEmail = functions.https.onRequest(
  async (req, res) => {
    // Only accept POST requests
    if (req.method !== "POST") {
      res.status(405).send("Method not allowed");
      return;
    }

    // Validate environment variables
    if (!SENDGRID_API_KEY || !GEMINI_API_KEY || !BOT_EMAIL_ADDRESS) {
      console.error("Missing required environment variables");
      res.status(500).send("Server configuration error");
      return;
    }

    try {
      // Parse the inbound email
      const emailData = parseInboundEmail(req.body);

      console.log("Received email from:", emailData.from);
      console.log("Subject:", emailData.subject);
      console.log("Thread ID:", emailData.threadId);

      // Log event
      await logEvent("email_received", {
        from: emailData.from,
        subject: emailData.subject,
        threadId: emailData.threadId,
        messageLength: emailData.cleanBody.length,
      }, emailData.from);

      // Check rate limit
      const rateLimitResult = await checkRateLimit(
        emailData.from,
        MAX_MESSAGES_PER_DAY
      );

      if (!rateLimitResult.allowed) {
        console.log("Rate limit exceeded for:", emailData.from);

        // Calculate hours until reset
        const now = new Date();
        const resetDate = rateLimitResult.resetAt?.toDate() || new Date();
        const hoursUntilReset = Math.ceil(
          (resetDate.getTime() - now.getTime()) / (1000 * 60 * 60)
        );

        await sendRateLimitEmail(
          emailData.from,
          BOT_EMAIL_ADDRESS,
          hoursUntilReset
        );

        await logEvent("rate_limit_exceeded", {
          remaining: rateLimitResult.remaining,
          resetAt: rateLimitResult.resetAt,
        }, emailData.from);

        res.status(200).send("Rate limit email sent");
        return;
      }

      console.log(`Rate limit OK. Remaining: ${rateLimitResult.remaining}`);

      // Get or create conversation
      const conversation = await getOrCreateConversation(
        emailData.threadId,
        emailData.from,
        emailData.subject
      );

      console.log("Conversation ID:", conversation.id);

      // Add user message to conversation
      await addMessage(conversation.id, {
        role: "user",
        content: emailData.cleanBody,
        timestamp: admin.firestore.Timestamp.now(),
        emailMessageId: emailData.messageId,
      });

      // Get conversation history
      const history = await getConversationHistory(
        conversation.id,
        MAX_CONVERSATION_HISTORY
      );

      console.log(`Loaded ${history.length} previous messages`);

      // Call Gemini API
      const startTime = Date.now();
      const geminiResponse = await callGeminiWithSystemPrompt(
        history.slice(0, -1), // Exclude the message we just added
        emailData.cleanBody
      );
      const geminiLatency = Date.now() - startTime;

      console.log("Gemini response received:", {
        latency: geminiLatency,
        tokens: geminiResponse.metadata.totalTokens,
      });

      // Store assistant response
      await addMessage(conversation.id, {
        role: "assistant",
        content: geminiResponse.content,
        timestamp: admin.firestore.Timestamp.now(),
        geminiMetadata: geminiResponse.metadata,
      });

      // Send email reply
      await sendEmailReply(
        emailData.from,
        emailData.subject,
        geminiResponse.content,
        emailData.messageId,
        emailData.references,
        BOT_EMAIL_ADDRESS
      );

      console.log("Email reply sent");

      // Log success
      await logEvent("email_sent", {
        conversationId: conversation.id,
        tokensUsed: geminiResponse.metadata.totalTokens,
        latencyMs: geminiLatency,
        remaining: rateLimitResult.remaining,
      }, emailData.from, conversation.id);

      res.status(200).send("Email processed successfully");
    } catch (error) {
      console.error("Error processing email:", error);

      // Generate error ID for tracking
      const errorId = `ERR-${Date.now()}`;

      // Log error
      await logError(
        error as Error,
        {
          errorId,
          body: req.body,
        },
        req.body?.from
      );

      // Try to send error notification to user
      if (req.body?.from && BOT_EMAIL_ADDRESS) {
        try {
          await sendErrorEmail(
            req.body.from,
            BOT_EMAIL_ADDRESS,
            errorId
          );
        } catch (emailError) {
          console.error("Failed to send error email:", emailError);
        }
      }

      // Return 200 to prevent SendGrid retries
      // (we handle errors internally)
      res.status(200).send("Error processed");
    }
  }
);

/**
 * Scheduled function to clean up old conversations
 * Runs daily at 2:00 AM UTC
 */
export const cleanupOldConversations = functions.pubsub
  .schedule("0 2 * * *")
  .timeZone("UTC")
  .onRun(async () => {
    console.log("Starting conversation cleanup...");

    try {
      const archivedCount = await archiveOldConversations(30);
      console.log(`Archived ${archivedCount} conversations`);

      await logEvent("cleanup_completed", {
        archivedCount,
      });
    } catch (error) {
      console.error("Error during cleanup:", error);
      await logError(error as Error, {
        task: "cleanup",
      });
    }
  });

/**
 * HTTP function for health checks
 */
export const healthCheck = functions.https.onRequest(async (req, res) => {
  const health = {
    status: "ok",
    timestamp: new Date().toISOString(),
    environment: {
      hasSendGridKey: !!SENDGRID_API_KEY,
      hasGeminiKey: !!GEMINI_API_KEY,
      hasBotEmail: !!BOT_EMAIL_ADDRESS,
    },
  };

  res.status(200).json(health);
});
