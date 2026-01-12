/**
 * Firebase Service
 *
 * Handles Firestore operations for workspace data.
 *
 * SETUP INSTRUCTIONS:
 * 1. Go to https://console.firebase.google.com/
 * 2. Create a new project (or use existing)
 * 3. Enable Firestore Database (start in test mode for dev)
 * 4. Enable Authentication > Sign-in method > Google
 * 5. Go to Project Settings > Service accounts > Generate new private key
 * 6. Save the JSON file as server/firebase-service-account.json (gitignored)
 * 7. Copy the config values to .env file
 */

import type {
  ResumeWorkspace,
  JobDescription,
  FitSession,
} from '../../src/types';

// Types for Firestore documents
interface FirestoreTimestamp {
  _seconds: number;
  _nanoseconds: number;
}

interface UserDocument {
  id: string;
  email: string;
  displayName: string;
  photoURL?: string;
  createdAt: string;
  lastLoginAt: string;
}

interface WorkspaceDocument extends ResumeWorkspace {
  userId: string;
}

// Environment config
const FIREBASE_PROJECT_ID = process.env.FIREBASE_PROJECT_ID;
const FIREBASE_CLIENT_EMAIL = process.env.FIREBASE_CLIENT_EMAIL;
const FIREBASE_PRIVATE_KEY = process.env.FIREBASE_PRIVATE_KEY?.replace(/\\n/g, '\n');

// Check if Firebase is configured
export function isFirebaseConfigured(): boolean {
  return !!(FIREBASE_PROJECT_ID && FIREBASE_CLIENT_EMAIL && FIREBASE_PRIVATE_KEY);
}

// In-memory store for development (when Firebase isn't configured)
const memoryStore: Map<string, Map<string, unknown>> = new Map();

function getMemoryCollection(collection: string): Map<string, unknown> {
  if (!memoryStore.has(collection)) {
    memoryStore.set(collection, new Map());
  }
  return memoryStore.get(collection)!;
}

// Generic Firestore REST API helper
async function firestoreRequest(
  method: 'GET' | 'POST' | 'PATCH' | 'DELETE',
  path: string,
  body?: unknown
): Promise<unknown> {
  if (!isFirebaseConfigured()) {
    throw new Error('Firebase not configured');
  }

  const token = await getAccessToken();
  const baseUrl = `https://firestore.googleapis.com/v1/projects/${FIREBASE_PROJECT_ID}/databases/(default)/documents`;

  const response = await fetch(`${baseUrl}${path}`, {
    method,
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
    body: body ? JSON.stringify(body) : undefined,
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Firestore error: ${response.status} ${error}`);
  }

  if (method === 'DELETE') {
    return null;
  }

  return response.json();
}

// Get OAuth2 access token for Firebase
async function getAccessToken(): Promise<string> {
  // For simplicity, we'll use a JWT for service account auth
  // In production, you'd use the google-auth-library
  const jwt = await createServiceAccountJWT();

  const response = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer',
      assertion: jwt,
    }),
  });

  const data = await response.json() as { access_token: string };
  return data.access_token;
}

// Create JWT for service account authentication
async function createServiceAccountJWT(): Promise<string> {
  const header = { alg: 'RS256', typ: 'JWT' };
  const now = Math.floor(Date.now() / 1000);
  const payload = {
    iss: FIREBASE_CLIENT_EMAIL,
    sub: FIREBASE_CLIENT_EMAIL,
    aud: 'https://oauth2.googleapis.com/token',
    iat: now,
    exp: now + 3600,
    scope: 'https://www.googleapis.com/auth/datastore',
  };

  const encodedHeader = btoa(JSON.stringify(header));
  const encodedPayload = btoa(JSON.stringify(payload));
  const signatureInput = `${encodedHeader}.${encodedPayload}`;

  // Sign with private key
  const key = await crypto.subtle.importKey(
    'pkcs8',
    pemToArrayBuffer(FIREBASE_PRIVATE_KEY!),
    { name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' },
    false,
    ['sign']
  );

  const signature = await crypto.subtle.sign(
    'RSASSA-PKCS1-v1_5',
    key,
    new TextEncoder().encode(signatureInput)
  );

  const encodedSignature = btoa(String.fromCharCode(...new Uint8Array(signature)));
  return `${signatureInput}.${encodedSignature}`;
}

function pemToArrayBuffer(pem: string): ArrayBuffer {
  const b64 = pem
    .replace(/-----BEGIN PRIVATE KEY-----/, '')
    .replace(/-----END PRIVATE KEY-----/, '')
    .replace(/\s/g, '');
  const binary = atob(b64);
  const buffer = new ArrayBuffer(binary.length);
  const view = new Uint8Array(buffer);
  for (let i = 0; i < binary.length; i++) {
    view[i] = binary.charCodeAt(i);
  }
  return buffer;
}

// ============================================================================
// USER OPERATIONS
// ============================================================================

export async function getOrCreateUser(
  userId: string,
  email: string,
  displayName: string,
  photoURL?: string
): Promise<UserDocument> {
  if (!isFirebaseConfigured()) {
    const users = getMemoryCollection('users');
    let user = users.get(userId) as UserDocument | undefined;
    if (!user) {
      user = {
        id: userId,
        email,
        displayName,
        photoURL,
        createdAt: new Date().toISOString(),
        lastLoginAt: new Date().toISOString(),
      };
      users.set(userId, user);
    } else {
      user.lastLoginAt = new Date().toISOString();
    }
    return user;
  }

  // Try to get existing user
  try {
    const doc = await firestoreRequest('GET', `/users/${userId}`) as { fields: Record<string, unknown> };
    return firestoreDocToUser(doc);
  } catch {
    // Create new user
    const user: UserDocument = {
      id: userId,
      email,
      displayName,
      photoURL,
      createdAt: new Date().toISOString(),
      lastLoginAt: new Date().toISOString(),
    };
    await firestoreRequest('PATCH', `/users/${userId}`, {
      fields: userToFirestoreFields(user),
    });
    return user;
  }
}

// ============================================================================
// WORKSPACE OPERATIONS
// ============================================================================

export async function getWorkspace(userId: string): Promise<WorkspaceDocument | null> {
  if (!isFirebaseConfigured()) {
    const workspaces = getMemoryCollection('workspaces');
    return (workspaces.get(userId) as WorkspaceDocument) || null;
  }

  try {
    const doc = await firestoreRequest('GET', `/workspaces/${userId}`) as { fields: Record<string, unknown> };
    return firestoreDocToWorkspace(doc);
  } catch {
    return null;
  }
}

export async function saveWorkspace(userId: string, workspace: ResumeWorkspace): Promise<void> {
  const doc: WorkspaceDocument = { ...workspace, userId };

  if (!isFirebaseConfigured()) {
    const workspaces = getMemoryCollection('workspaces');
    workspaces.set(userId, doc);
    return;
  }

  await firestoreRequest('PATCH', `/workspaces/${userId}`, {
    fields: workspaceToFirestoreFields(doc),
  });
}

// ============================================================================
// JOB DESCRIPTION OPERATIONS
// ============================================================================

export async function getJobDescriptions(userId: string): Promise<JobDescription[]> {
  if (!isFirebaseConfigured()) {
    const jobs = getMemoryCollection(`jobs_${userId}`);
    return Array.from(jobs.values()) as JobDescription[];
  }

  try {
    const result = await firestoreRequest('GET', `/users/${userId}/jobs`) as { documents?: Array<{ fields: Record<string, unknown> }> };
    return (result.documents || []).map(doc => firestoreDocToJob(doc));
  } catch {
    return [];
  }
}

export async function saveJobDescription(userId: string, job: JobDescription): Promise<void> {
  if (!isFirebaseConfigured()) {
    const jobs = getMemoryCollection(`jobs_${userId}`);
    jobs.set(job.id, job);
    return;
  }

  await firestoreRequest('PATCH', `/users/${userId}/jobs/${job.id}`, {
    fields: jobToFirestoreFields(job),
  });
}

export async function deleteJobDescription(userId: string, jobId: string): Promise<void> {
  if (!isFirebaseConfigured()) {
    const jobs = getMemoryCollection(`jobs_${userId}`);
    jobs.delete(jobId);
    return;
  }

  await firestoreRequest('DELETE', `/users/${userId}/jobs/${jobId}`);
}

// ============================================================================
// FIT SESSION OPERATIONS
// ============================================================================

export async function getFitSessions(userId: string): Promise<FitSession[]> {
  if (!isFirebaseConfigured()) {
    const sessions = getMemoryCollection(`fitSessions_${userId}`);
    return Array.from(sessions.values()) as FitSession[];
  }

  try {
    const result = await firestoreRequest('GET', `/users/${userId}/fitSessions`) as { documents?: Array<{ fields: Record<string, unknown> }> };
    return (result.documents || []).map(doc => firestoreDocToFitSession(doc));
  } catch {
    return [];
  }
}

export async function saveFitSession(userId: string, session: FitSession): Promise<void> {
  if (!isFirebaseConfigured()) {
    const sessions = getMemoryCollection(`fitSessions_${userId}`);
    sessions.set(session.id, session);
    return;
  }

  await firestoreRequest('PATCH', `/users/${userId}/fitSessions/${session.id}`, {
    fields: fitSessionToFirestoreFields(session),
  });
}

// ============================================================================
// FIRESTORE CONVERSION HELPERS
// ============================================================================

function firestoreDocToUser(doc: { fields: Record<string, unknown> }): UserDocument {
  const f = doc.fields as Record<string, { stringValue?: string }>;
  return {
    id: f.id?.stringValue || '',
    email: f.email?.stringValue || '',
    displayName: f.displayName?.stringValue || '',
    photoURL: f.photoURL?.stringValue,
    createdAt: f.createdAt?.stringValue || '',
    lastLoginAt: f.lastLoginAt?.stringValue || '',
  };
}

function userToFirestoreFields(user: UserDocument): Record<string, unknown> {
  return {
    id: { stringValue: user.id },
    email: { stringValue: user.email },
    displayName: { stringValue: user.displayName },
    photoURL: user.photoURL ? { stringValue: user.photoURL } : { nullValue: null },
    createdAt: { stringValue: user.createdAt },
    lastLoginAt: { stringValue: user.lastLoginAt },
  };
}

function firestoreDocToWorkspace(doc: { fields: Record<string, unknown> }): WorkspaceDocument {
  // For complex nested objects, we store as JSON string
  const f = doc.fields as Record<string, { stringValue?: string }>;
  const json = f.data?.stringValue || '{}';
  return JSON.parse(json);
}

function workspaceToFirestoreFields(workspace: WorkspaceDocument): Record<string, unknown> {
  // Store complex nested object as JSON string for simplicity
  return {
    data: { stringValue: JSON.stringify(workspace) },
    userId: { stringValue: workspace.userId },
    updatedAt: { stringValue: workspace.updatedAt },
  };
}

function firestoreDocToJob(doc: { fields: Record<string, unknown> }): JobDescription {
  const f = doc.fields as Record<string, { stringValue?: string }>;
  const json = f.data?.stringValue || '{}';
  return JSON.parse(json);
}

function jobToFirestoreFields(job: JobDescription): Record<string, unknown> {
  return {
    data: { stringValue: JSON.stringify(job) },
    id: { stringValue: job.id },
    title: { stringValue: job.title },
    company: { stringValue: job.company },
  };
}

function firestoreDocToFitSession(doc: { fields: Record<string, unknown> }): FitSession {
  const f = doc.fields as Record<string, { stringValue?: string }>;
  const json = f.data?.stringValue || '{}';
  return JSON.parse(json);
}

function fitSessionToFirestoreFields(session: FitSession): Record<string, unknown> {
  return {
    data: { stringValue: JSON.stringify(session) },
    id: { stringValue: session.id },
    jobDescriptionId: { stringValue: session.jobDescriptionId },
    variantId: { stringValue: session.variantId },
  };
}
