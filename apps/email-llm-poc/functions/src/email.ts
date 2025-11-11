/**
 * Email parsing and sending utilities
 */

import * as sgMail from "@sendgrid/mail";
import {ParsedEmail} from "./types";

/**
 * Initialize SendGrid with API key
 */
export function initSendGrid(apiKey: string): void {
  sgMail.setApiKey(apiKey);
}

/**
 * Parse inbound email from SendGrid webhook
 */
export function parseInboundEmail(body: Record<string, unknown>): ParsedEmail {
  const from = (body.from as string) || "";
  const to = (body.to as string) || "";
  const subject = (body.subject as string) || "No subject";
  const text = (body.text as string) || "";
  const headers = (body.headers as string) || "";

  // Extract sender name and email
  const fromMatch = from.match(/(.*?)\s*<(.+?)>/) || [, from, from];
  const fromName = fromMatch[1]?.trim() || "";
  const fromEmail = fromMatch[2]?.trim() || from;

  // Extract Message-ID
  const messageIdMatch = headers.match(/Message-ID:\s*<(.+?)>/i);
  const messageId = messageIdMatch ? messageIdMatch[1] : "";

  // Extract References for threading
  const referencesMatch = headers.match(/References:\s*(.+)/i);
  const referencesStr = referencesMatch ? referencesMatch[1] : "";
  const references = referencesStr
    .split(/\s+/)
    .map((ref) => ref.replace(/[<>]/g, ""))
    .filter((ref) => ref.length > 0);

  // Thread ID is the first reference, or the message ID if it's the first email
  const threadId = references.length > 0 ? references[0] : messageId;

  // Clean the email body
  const cleanBody = extractCleanBody(text);

  return {
    from: fromEmail,
    fromName,
    to,
    subject,
    body: text,
    cleanBody,
    messageId,
    threadId,
    references,
    timestamp: new Date(),
  };
}

/**
 * Extract clean body from email (remove quotes and signatures)
 */
export function extractCleanBody(rawBody: string): string {
  let clean = rawBody;

  // Common quote markers
  const quoteMarkers = [
    "\n\nOn ", // Gmail, Outlook
    "\n\n>", // Plain text quotes
    "\n\n--", // Signature delimiter
    "\n\n___", // Some clients use underscores
  ];

  for (const marker of quoteMarkers) {
    const index = clean.indexOf(marker);
    if (index !== -1) {
      clean = clean.substring(0, index);
    }
  }

  // Remove leading/trailing whitespace
  clean = clean.trim();

  // Limit length
  const maxLength = 10000;
  if (clean.length > maxLength) {
    clean = clean.substring(0, maxLength) + "\n\n[Message truncated]";
  }

  return clean;
}

/**
 * Send an email reply via SendGrid
 */
export async function sendEmailReply(
  to: string,
  subject: string,
  content: string,
  inReplyTo: string,
  references: string[],
  fromEmail: string,
  fromName: string = "AI Assistant"
): Promise<void> {
  // Build References header
  const allReferences = [...references, inReplyTo]
    .filter((ref) => ref)
    .map((ref) => `<${ref}>`)
    .join(" ");

  const msg = {
    to,
    from: {
      email: fromEmail,
      name: fromName,
    },
    subject: subject.startsWith("Re: ") ? subject : `Re: ${subject}`,
    text: content,
    headers: {
      "In-Reply-To": `<${inReplyTo}>`,
      References: allReferences,
    },
  };

  await sgMail.send(msg);
}

/**
 * Send a rate limit notification email
 */
export async function sendRateLimitEmail(
  to: string,
  fromEmail: string,
  resetHours: number
): Promise<void> {
  const content = `Hi there,

You've reached the daily message limit. Your limit will reset in approximately ${resetHours} hours.

If you have urgent needs or would like to discuss higher limits, please reply to this email.

Best,
Your AI Assistant`;

  const msg = {
    to,
    from: {
      email: fromEmail,
      name: "AI Assistant",
    },
    subject: "Daily message limit reached",
    text: content,
  };

  await sgMail.send(msg);
}

/**
 * Send an error notification email
 */
export async function sendErrorEmail(
  to: string,
  fromEmail: string,
  errorId: string
): Promise<void> {
  const content = `Hi there,

I encountered an error while processing your message. The issue has been logged and we're looking into it.

Please try resending your message in a few minutes. If the problem persists, please mention this error ID in your reply: ${errorId}

Best,
Your AI Assistant`;

  const msg = {
    to,
    from: {
      email: fromEmail,
      name: "AI Assistant",
    },
    subject: "Error processing your message",
    text: content,
  };

  await sgMail.send(msg);
}
