/**
 * API Client
 *
 * Handles all communication with the server, including:
 * - Firebase authentication
 * - Workspace CRUD
 * - Fit Coach operations
 */

import type {
  ResumeWorkspace,
  JobDescription,
  FitSession,
  FitCoachMessage,
  ParsedJobDescription,
  Resume,
  ResumeVariant,
} from './types';

// ============================================================================
// CONFIGURATION
// ============================================================================

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:3001';

interface AuthConfig {
  apiKey: string | null;
  projectId: string | null;
  authDomain: string | null;
  configured: boolean;
  devMode: boolean;
}

interface AuthUser {
  id: string;
  email: string;
  displayName: string;
  photoURL?: string;
}

interface AuthState {
  user: AuthUser | null;
  token: string | null;
  loading: boolean;
  error: string | null;
}

// ============================================================================
// AUTH STATE
// ============================================================================

let authState: AuthState = {
  user: null,
  token: null,
  loading: true,
  error: null,
};

let authConfig: AuthConfig | null = null;
const authListeners: Set<(state: AuthState) => void> = new Set();

function notifyAuthListeners() {
  authListeners.forEach(listener => listener(authState));
}

export function subscribeToAuth(listener: (state: AuthState) => void): () => void {
  authListeners.add(listener);
  listener(authState); // Immediate callback with current state
  return () => authListeners.delete(listener);
}

export function getAuthState(): AuthState {
  return authState;
}

// ============================================================================
// AUTH METHODS
// ============================================================================

/**
 * Initialize auth - fetch config and restore session
 */
export async function initAuth(): Promise<void> {
  try {
    // Fetch auth config from server
    const response = await fetch(`${API_BASE_URL}/auth/config`);
    authConfig = await response.json();

    // Check for stored token
    const storedToken = localStorage.getItem('auth_token');
    const storedUser = localStorage.getItem('auth_user');

    if (storedToken && storedUser) {
      authState = {
        user: JSON.parse(storedUser),
        token: storedToken,
        loading: false,
        error: null,
      };
      notifyAuthListeners();

      // Verify token is still valid
      try {
        await apiRequest('GET', '/auth/me');
      } catch {
        // Token invalid, clear it
        await signOut();
      }
    } else if (authConfig?.devMode) {
      // In dev mode, auto-login with dev user
      await devLogin();
    } else {
      authState = { ...authState, loading: false };
      notifyAuthListeners();
    }
  } catch (error) {
    console.error('Failed to initialize auth:', error);
    authState = {
      user: null,
      token: null,
      loading: false,
      error: 'Failed to connect to server',
    };
    notifyAuthListeners();
  }
}

/**
 * Sign in with Google (Firebase Auth)
 */
export async function signInWithGoogle(): Promise<void> {
  if (!authConfig?.configured) {
    throw new Error('Firebase not configured');
  }

  authState = { ...authState, loading: true, error: null };
  notifyAuthListeners();

  try {
    // Note: Full OAuth flow requires Firebase SDK or custom implementation
    // For now, we show an error directing users to the setup guide

    // Create a popup for Google sign-in (placeholder)
    const popup = window.open(
      `https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key=${authConfig.apiKey}`,
      'Google Sign In',
      'width=500,height=600'
    );

    if (!popup) {
      throw new Error('Popup blocked. Please allow popups for this site.');
    }

    // This is a simplified flow - in production, use Firebase SDK
    throw new Error('Please install Firebase SDK for Google sign-in. See FIREBASE_SETUP.md');
  } catch (error) {
    authState = {
      ...authState,
      loading: false,
      error: error instanceof Error ? error.message : 'Sign in failed',
    };
    notifyAuthListeners();
    throw error;
  }
}

/**
 * Dev mode login (bypasses Firebase)
 */
export async function devLogin(): Promise<void> {
  authState = { ...authState, loading: true, error: null };
  notifyAuthListeners();

  try {
    const response = await fetch(`${API_BASE_URL}/auth/dev-login`, {
      method: 'POST',
    });

    if (!response.ok) {
      throw new Error('Dev login not available');
    }

    const data = await response.json() as { user: AuthUser; token: string };

    authState = {
      user: data.user,
      token: data.token,
      loading: false,
      error: null,
    };

    localStorage.setItem('auth_token', data.token);
    localStorage.setItem('auth_user', JSON.stringify(data.user));

    notifyAuthListeners();
  } catch (error) {
    authState = {
      ...authState,
      loading: false,
      error: error instanceof Error ? error.message : 'Login failed',
    };
    notifyAuthListeners();
    throw error;
  }
}

/**
 * Sign out
 */
export async function signOut(): Promise<void> {
  localStorage.removeItem('auth_token');
  localStorage.removeItem('auth_user');

  authState = {
    user: null,
    token: null,
    loading: false,
    error: null,
  };

  notifyAuthListeners();
}

/**
 * Set auth from Firebase SDK (call this after Firebase signInWithPopup)
 */
export async function setAuthFromFirebase(idToken: string, user: AuthUser): Promise<void> {
  authState = {
    user,
    token: idToken,
    loading: false,
    error: null,
  };

  localStorage.setItem('auth_token', idToken);
  localStorage.setItem('auth_user', JSON.stringify(user));

  notifyAuthListeners();
}

// ============================================================================
// API REQUEST HELPER
// ============================================================================

async function apiRequest<T>(
  method: 'GET' | 'POST' | 'PUT' | 'DELETE',
  path: string,
  body?: unknown
): Promise<T> {
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
  };

  // Add auth header
  if (authState.token) {
    if (authConfig?.devMode && authState.token === 'dev-token-not-real') {
      headers['X-Dev-Auth'] = 'true';
    } else {
      headers['Authorization'] = `Bearer ${authState.token}`;
    }
  }

  const response = await fetch(`${API_BASE_URL}${path}`, {
    method,
    headers,
    body: body ? JSON.stringify(body) : undefined,
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ error: 'Request failed' }));
    throw new Error(error.error || `Request failed: ${response.status}`);
  }

  return response.json();
}

// ============================================================================
// WORKSPACE API
// ============================================================================

export async function fetchWorkspace(): Promise<ResumeWorkspace | null> {
  const data = await apiRequest<{ workspace: ResumeWorkspace | null }>('GET', '/api/workspace');
  return data.workspace;
}

export async function saveWorkspace(workspace: ResumeWorkspace): Promise<void> {
  await apiRequest('PUT', '/api/workspace', { workspace });
}

export async function fetchJobDescriptions(): Promise<JobDescription[]> {
  const data = await apiRequest<{ jobs: JobDescription[] }>('GET', '/api/workspace/jobs');
  return data.jobs;
}

export async function saveJobDescription(job: JobDescription): Promise<void> {
  await apiRequest('POST', '/api/workspace/jobs', { job });
}

export async function deleteJobDescription(jobId: string): Promise<void> {
  await apiRequest('DELETE', `/api/workspace/jobs/${jobId}`);
}

// ============================================================================
// FIT COACH API
// ============================================================================

export async function parseJobDescriptionApi(
  jobDescription: JobDescription
): Promise<ParsedJobDescription> {
  const data = await apiRequest<{ parsed: ParsedJobDescription }>(
    'POST',
    '/api/fit-coach/parse-jd',
    { jobDescription }
  );
  return data.parsed;
}

export async function cleanJobDescriptionApi(
  rawText: string
): Promise<{ title: string; company: string; description: string; requirements: string[]; keywords: string[] }> {
  const data = await apiRequest<{ cleaned: { title: string; company: string; description: string; requirements: string[]; keywords: string[] } }>(
    'POST',
    '/api/fit-coach/clean-jd',
    { rawText }
  );
  return data.cleaned;
}

export async function analyzeCoverageApi(
  parsedJD: ParsedJobDescription,
  resume: Resume,
  variant: ResumeVariant
): Promise<{ analyzed: ParsedJobDescription; score: number; breakdown: { strong: number; partial: number; missing: number; notMe: number } }> {
  return apiRequest(
    'POST',
    '/api/fit-coach/analyze',
    { parsedJD, resume, variant }
  );
}

export async function startFitSessionApi(
  jobDescription: JobDescription,
  resume: Resume,
  variant: ResumeVariant
): Promise<FitSession> {
  const data = await apiRequest<{ session: FitSession }>(
    'POST',
    '/api/fit-coach/start-session',
    { jobDescription, resume, variant }
  );
  return data.session;
}

export async function sendCoachMessageApi(
  session: FitSession,
  message: string,
  resume: Resume,
  variant: ResumeVariant,
  focusedRequirementId?: string
): Promise<{ userMessage: FitCoachMessage; coachMessage: FitCoachMessage; session: FitSession }> {
  return apiRequest(
    'POST',
    '/api/fit-coach/chat',
    {
      sessionId: session.id,
      message,
      session,
      resume,
      variant,
      focusedRequirementId,
    }
  );
}

export async function updateRequirementStatusApi(
  session: FitSession,
  requirementId: string,
  status: 'strong' | 'partial' | 'missing' | 'not-me',
  notMeReason?: string
): Promise<FitSession> {
  const data = await apiRequest<{ session: FitSession }>(
    'POST',
    '/api/fit-coach/update-requirement',
    { session, requirementId, status, notMeReason }
  );
  return data.session;
}

export async function refreshCoverageApi(
  session: FitSession,
  resume: Resume,
  variant: ResumeVariant
): Promise<FitSession> {
  const data = await apiRequest<{ session: FitSession }>(
    'POST',
    '/api/fit-coach/refresh',
    { session, resume, variant }
  );
  return data.session;
}

export async function fetchFitSessions(): Promise<FitSession[]> {
  const data = await apiRequest<{ sessions: FitSession[] }>('GET', '/api/fit-coach/sessions');
  return data.sessions;
}

export async function endFitSessionApi(sessionId: string): Promise<void> {
  await apiRequest('DELETE', `/api/fit-coach/sessions/${sessionId}`);
}

// ============================================================================
// SERVER STATUS
// ============================================================================

export async function checkServerHealth(): Promise<boolean> {
  try {
    const response = await fetch(`${API_BASE_URL}/health`);
    return response.ok;
  } catch {
    return false;
  }
}
