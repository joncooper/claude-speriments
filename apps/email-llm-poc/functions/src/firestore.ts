/**
 * Firestore operations for conversations and messages
 */

import * as admin from "firebase-admin";
import {Conversation, Message, User, RateLimitResult} from "./types";

const db = admin.firestore();

/**
 * Get or create a conversation
 */
export async function getOrCreateConversation(
  threadId: string,
  userEmail: string,
  subject: string
): Promise<Conversation> {
  // Check if conversation already exists
  const conversationQuery = await db
    .collection("conversations")
    .where("threadId", "==", threadId)
    .limit(1)
    .get();

  if (!conversationQuery.empty) {
    const doc = conversationQuery.docs[0];
    return {
      id: doc.id,
      ...doc.data(),
    } as Conversation;
  }

  // Create new conversation
  const now = admin.firestore.Timestamp.now();
  const conversationData: Omit<Conversation, "id"> = {
    threadId,
    userEmail,
    createdAt: now,
    updatedAt: now,
    messageCount: 0,
    status: "active",
    metadata: {
      firstSubject: subject,
      lastMessageAt: now,
      totalTokensUsed: 0,
    },
  };

  const docRef = await db.collection("conversations").add(conversationData);

  return {
    id: docRef.id,
    ...conversationData,
  };
}

/**
 * Add a message to a conversation
 */
export async function addMessage(
  conversationId: string,
  message: Omit<Message, "id">
): Promise<string> {
  const messageRef = await db
    .collection("conversations")
    .doc(conversationId)
    .collection("messages")
    .add(message);

  // Update conversation metadata
  const updateData: Record<string, unknown> = {
    updatedAt: admin.firestore.Timestamp.now(),
    messageCount: admin.firestore.FieldValue.increment(1),
    "metadata.lastMessageAt": admin.firestore.Timestamp.now(),
  };

  if (message.geminiMetadata) {
    updateData["metadata.totalTokensUsed"] =
      admin.firestore.FieldValue.increment(message.geminiMetadata.totalTokens);
  }

  await db.collection("conversations").doc(conversationId).update(updateData);

  return messageRef.id;
}

/**
 * Get conversation history (last N messages)
 */
export async function getConversationHistory(
  conversationId: string,
  limit: number = 20
): Promise<Message[]> {
  const messagesSnapshot = await db
    .collection("conversations")
    .doc(conversationId)
    .collection("messages")
    .orderBy("timestamp", "desc")
    .limit(limit)
    .get();

  const messages: Message[] = messagesSnapshot.docs
    .reverse()
    .map((doc) => ({
      id: doc.id,
      ...doc.data(),
    } as Message));

  return messages;
}

/**
 * Check rate limit for a user
 */
export async function checkRateLimit(
  userEmail: string,
  maxMessagesPerDay: number = 50
): Promise<RateLimitResult> {
  const userRef = db.collection("users").doc(userEmail);
  const userDoc = await userRef.get();
  const userData = userDoc.exists ? (userDoc.data() as User) : null;

  const now = admin.firestore.Timestamp.now();
  const todayStart = new Date();
  todayStart.setHours(0, 0, 0, 0);
  const tomorrowStart = new Date(todayStart);
  tomorrowStart.setDate(tomorrowStart.getDate() + 1);

  // Check if we need to reset daily counter
  if (!userData || userData.dailyResetAt.toDate() < todayStart) {
    const newUserData: Partial<User> = {
      email: userEmail,
      dailyMessageCount: 0,
      dailyResetAt: admin.firestore.Timestamp.fromDate(tomorrowStart),
      lastMessageAt: now,
    };

    if (!userData) {
      newUserData.createdAt = now;
      newUserData.stats = {
        totalConversations: 0,
        totalMessages: 0,
        totalTokensUsed: 0,
      };
      newUserData.blocked = false;
    }

    await userRef.set(newUserData, {merge: true});

    return {
      allowed: true,
      remaining: maxMessagesPerDay,
    };
  }

  // Check if user is blocked
  if (userData.blocked) {
    return {
      allowed: false,
      remaining: 0,
      resetAt: userData.dailyResetAt,
    };
  }

  // Check if user has exceeded limit
  if (userData.dailyMessageCount >= maxMessagesPerDay) {
    return {
      allowed: false,
      remaining: 0,
      resetAt: userData.dailyResetAt,
    };
  }

  // Increment counter
  await userRef.update({
    dailyMessageCount: admin.firestore.FieldValue.increment(1),
    lastMessageAt: now,
    "stats.totalMessages": admin.firestore.FieldValue.increment(1),
  });

  return {
    allowed: true,
    remaining: maxMessagesPerDay - userData.dailyMessageCount - 1,
  };
}

/**
 * Archive old conversations
 */
export async function archiveOldConversations(
  daysOld: number = 30
): Promise<number> {
  const cutoffDate = new Date();
  cutoffDate.setDate(cutoffDate.getDate() - daysOld);
  const cutoffTimestamp = admin.firestore.Timestamp.fromDate(cutoffDate);

  const oldConversations = await db
    .collection("conversations")
    .where("status", "==", "active")
    .where("updatedAt", "<", cutoffTimestamp)
    .get();

  const batch = db.batch();
  oldConversations.docs.forEach((doc) => {
    batch.update(doc.ref, {status: "archived"});
  });

  await batch.commit();

  return oldConversations.size;
}

/**
 * Log an event to audit logs
 */
export async function logEvent(
  eventType: string,
  data: Record<string, unknown>,
  userEmail?: string,
  conversationId?: string
): Promise<void> {
  await db.collection("audit_logs").add({
    timestamp: admin.firestore.Timestamp.now(),
    eventType,
    userEmail,
    conversationId,
    data,
  });
}

/**
 * Log an error to audit logs
 */
export async function logError(
  error: Error,
  data: Record<string, unknown>,
  userEmail?: string,
  conversationId?: string
): Promise<void> {
  await db.collection("audit_logs").add({
    timestamp: admin.firestore.Timestamp.now(),
    eventType: "error",
    userEmail,
    conversationId,
    data,
    error: {
      message: error.message,
      stack: error.stack || "",
      code: (error as {code?: string}).code || "UNKNOWN",
    },
  });
}
