/**
 * Authentication Middleware
 *
 * Verifies Firebase ID tokens and attaches user info to context.
 * Also provides auth routes for the OAuth flow.
 */

import { Hono } from 'hono';
import type { Context, Next } from 'hono';
import { getOrCreateUser } from '../services/firebase';

// User type attached to context
export interface AuthUser {
  id: string;
  email: string;
  displayName: string;
  photoURL?: string;
}

// Extend Hono context with user
declare module 'hono' {
  interface ContextVariableMap {
    user: AuthUser;
  }
}

// Environment config
const FIREBASE_PROJECT_ID = process.env.FIREBASE_PROJECT_ID;
const FIREBASE_API_KEY = process.env.FIREBASE_API_KEY;

// Development mode flag - allows bypass of auth for local testing
const DEV_MODE = process.env.NODE_ENV !== 'production';
const DEV_USER: AuthUser = {
  id: 'dev-user-123',
  email: 'dev@localhost',
  displayName: 'Dev User',
};

/**
 * Verify Firebase ID token
 */
async function verifyIdToken(idToken: string): Promise<AuthUser | null> {
  if (!FIREBASE_PROJECT_ID) {
    console.warn('Firebase not configured, using dev user');
    return DEV_USER;
  }

  try {
    // Use Firebase Auth REST API to verify token
    const response = await fetch(
      `https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=${FIREBASE_API_KEY}`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ idToken }),
      }
    );

    if (!response.ok) {
      console.error('Token verification failed:', await response.text());
      return null;
    }

    const data = await response.json() as {
      users?: Array<{
        localId: string;
        email: string;
        displayName?: string;
        photoUrl?: string;
      }>;
    };

    const user = data.users?.[0];
    if (!user) {
      return null;
    }

    // Get or create user in Firestore
    await getOrCreateUser(
      user.localId,
      user.email,
      user.displayName || user.email.split('@')[0],
      user.photoUrl
    );

    return {
      id: user.localId,
      email: user.email,
      displayName: user.displayName || user.email.split('@')[0],
      photoURL: user.photoUrl,
    };
  } catch (error) {
    console.error('Token verification error:', error);
    return null;
  }
}

/**
 * Auth middleware - verifies token and attaches user to context
 */
export async function authMiddleware(c: Context, next: Next) {
  // In dev mode, allow bypass with special header
  if (DEV_MODE && c.req.header('X-Dev-Auth') === 'true') {
    c.set('user', DEV_USER);
    return next();
  }

  const authHeader = c.req.header('Authorization');
  if (!authHeader?.startsWith('Bearer ')) {
    return c.json({ error: 'Missing or invalid Authorization header' }, 401);
  }

  const idToken = authHeader.slice(7);
  const user = await verifyIdToken(idToken);

  if (!user) {
    return c.json({ error: 'Invalid or expired token' }, 401);
  }

  c.set('user', user);
  return next();
}

// ============================================================================
// AUTH ROUTES
// ============================================================================

export const authRoutes = new Hono();

/**
 * GET /auth/config - Returns Firebase config for client
 */
authRoutes.get('/config', (c) => {
  return c.json({
    apiKey: FIREBASE_API_KEY || null,
    projectId: FIREBASE_PROJECT_ID || null,
    authDomain: FIREBASE_PROJECT_ID ? `${FIREBASE_PROJECT_ID}.firebaseapp.com` : null,
    configured: !!(FIREBASE_API_KEY && FIREBASE_PROJECT_ID),
    devMode: DEV_MODE,
  });
});

/**
 * GET /auth/me - Returns current user (requires auth)
 */
authRoutes.get('/me', authMiddleware, (c) => {
  const user = c.get('user');
  return c.json({ user });
});

/**
 * POST /auth/dev-login - Dev mode login (only in development)
 */
authRoutes.post('/dev-login', (c) => {
  if (!DEV_MODE) {
    return c.json({ error: 'Dev login not available in production' }, 403);
  }

  // Return a fake token for dev mode
  return c.json({
    user: DEV_USER,
    token: 'dev-token-not-real',
    devMode: true,
  });
});
