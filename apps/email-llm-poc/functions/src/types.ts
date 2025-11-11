/**
 * Type definitions for the Email-to-LLM system
 */

import {Timestamp} from "firebase-admin/firestore";

/**
 * Conversation stored in Firestore
 */
export interface Conversation {
  id: string;
  threadId: string;
  userEmail: string;
  createdAt: Timestamp;
  updatedAt: Timestamp;
  messageCount: number;
  status: "active" | "archived";
  metadata: {
    firstSubject: string;
    lastMessageAt: Timestamp;
    totalTokensUsed: number;
  };
}

/**
 * Message in a conversation
 */
export interface Message {
  id: string;
  role: "user" | "assistant";
  content: string;
  timestamp: Timestamp;
  emailMessageId?: string;
  geminiMetadata?: {
    model: string;
    promptTokens: number;
    completionTokens: number;
    totalTokens: number;
    finishReason: string;
    latencyMs: number;
  };
}

/**
 * User record for rate limiting
 */
export interface User {
  email: string;
  createdAt: Timestamp;
  lastMessageAt: Timestamp;
  dailyMessageCount: number;
  dailyResetAt: Timestamp;
  stats: {
    totalConversations: number;
    totalMessages: number;
    totalTokensUsed: number;
  };
  blocked: boolean;
  blockedReason?: string;
}

/**
 * Parsed email data from SendGrid webhook
 */
export interface ParsedEmail {
  from: string;
  fromName: string;
  to: string;
  subject: string;
  body: string;
  cleanBody: string;
  messageId: string;
  threadId: string;
  references: string[];
  timestamp: Date;
}

/**
 * Gemini API response
 */
export interface GeminiResponse {
  content: string;
  metadata: {
    model: string;
    promptTokens: number;
    completionTokens: number;
    totalTokens: number;
    finishReason: string;
    latencyMs: number;
  };
}

/**
 * Rate limit check result
 */
export interface RateLimitResult {
  allowed: boolean;
  remaining: number;
  resetAt?: Timestamp;
}

/**
 * Audit log entry
 */
export interface AuditLog {
  id: string;
  timestamp: Timestamp;
  eventType: string;
  userEmail?: string;
  conversationId?: string;
  data: Record<string, unknown>;
  error?: {
    message: string;
    stack: string;
    code: string;
  };
}
