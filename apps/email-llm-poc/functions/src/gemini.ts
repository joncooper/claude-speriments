/**
 * Google Gemini API integration
 */

import {GoogleGenerativeAI} from "@google/generative-ai";
import {Message, GeminiResponse} from "./types";

let genAI: GoogleGenerativeAI;

/**
 * Initialize Gemini API
 */
export function initGemini(apiKey: string): void {
  genAI = new GoogleGenerativeAI(apiKey);
}

/**
 * Convert conversation history to Gemini format
 */
function formatMessagesForGemini(messages: Message[]): Array<{
  role: "user" | "model";
  parts: Array<{text: string}>;
}> {
  return messages.map((msg) => ({
    role: msg.role === "user" ? "user" : "model",
    parts: [{text: msg.content}],
  }));
}

/**
 * Call Gemini API with retry logic
 */
export async function callGemini(
  conversationHistory: Message[],
  newUserMessage: string,
  maxRetries: number = 3
): Promise<GeminiResponse> {
  const model = genAI.getGenerativeModel({
    model: "gemini-1.5-flash",
  });

  // Build conversation history
  const history = formatMessagesForGemini(conversationHistory);

  // Add system instruction via the first message if history is empty
  const chat = model.startChat({
    history,
    generationConfig: {
      temperature: 0.7,
      maxOutputTokens: 1024,
      topP: 0.95,
      topK: 40,
    },
  });

  // Try calling the API with retries
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const startTime = Date.now();

      const result = await chat.sendMessage(newUserMessage);
      const response = result.response;
      const text = response.text();

      const latencyMs = Date.now() - startTime;

      // Extract token usage from response
      const usageMetadata = response.usageMetadata;
      const promptTokens = usageMetadata?.promptTokenCount || 0;
      const completionTokens = usageMetadata?.candidatesTokenCount || 0;
      const totalTokens = usageMetadata?.totalTokenCount || 0;

      return {
        content: text,
        metadata: {
          model: "gemini-1.5-flash",
          promptTokens,
          completionTokens,
          totalTokens,
          finishReason: response.candidates?.[0]?.finishReason || "STOP",
          latencyMs,
        },
      };
    } catch (error) {
      const isLastAttempt = attempt === maxRetries;
      const isRetryable = isRetryableError(error);

      if (isLastAttempt || !isRetryable) {
        throw error;
      }

      // Exponential backoff
      const delayMs = Math.pow(2, attempt) * 1000;
      await sleep(delayMs);
    }
  }

  throw new Error("Failed to call Gemini API after retries");
}

/**
 * Check if an error is retryable
 */
function isRetryableError(error: unknown): boolean {
  if (typeof error === "object" && error !== null) {
    const errorObj = error as {code?: string; status?: number};

    // Retry on rate limits, timeouts, and service unavailable
    if (
      errorObj.code === "RATE_LIMIT_EXCEEDED" ||
      errorObj.status === 429 ||
      errorObj.status === 503 ||
      errorObj.code === "SERVICE_UNAVAILABLE" ||
      errorObj.code === "TIMEOUT"
    ) {
      return true;
    }
  }

  return false;
}

/**
 * Sleep for a given number of milliseconds
 */
function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/**
 * Generate a system prompt for the assistant
 */
export function getSystemPrompt(): string {
  return `You are a helpful AI assistant that communicates via email.

Key guidelines:
- Be concise and clear in your responses
- Use proper email etiquette
- Remember the conversation context from previous messages
- If you're unsure about something, ask for clarification
- Be friendly and professional
- Keep responses under 500 words unless more detail is explicitly requested`;
}

/**
 * Call Gemini with system prompt
 */
export async function callGeminiWithSystemPrompt(
  conversationHistory: Message[],
  newUserMessage: string
): Promise<GeminiResponse> {
  // If this is the first message, prepend system prompt
  if (conversationHistory.length === 0) {
    const systemMessage: Message = {
      id: "system",
      role: "user",
      content: getSystemPrompt(),
      timestamp: null as any, // Won't be used
    };
    const systemResponse: Message = {
      id: "system-response",
      role: "assistant",
      content: "I understand. I'll be a helpful assistant communicating via email.",
      timestamp: null as any, // Won't be used
    };
    conversationHistory = [systemMessage, systemResponse];
  }

  return callGemini(conversationHistory, newUserMessage);
}
