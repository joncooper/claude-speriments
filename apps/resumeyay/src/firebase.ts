/**
 * Firebase Client Initialization
 *
 * Handles Firebase Auth with Google sign-in for the browser.
 * Falls back to dev mode when Firebase SDK is not available.
 */

// Auth state types
export interface AuthUser {
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
  initialized: boolean;
  devMode: boolean;
}

// Dev mode user
const DEV_USER: AuthUser = {
  id: 'dev-user-123',
  email: 'dev@localhost',
  displayName: 'Dev User',
};

let authState: AuthState = {
  user: null,
  token: null,
  loading: true,
  error: null,
  initialized: false,
  devMode: true,
};

const authListeners: Set<(state: AuthState) => void> = new Set();

function notifyListeners() {
  authListeners.forEach(listener => listener(authState));
}

export function subscribeToAuth(listener: (state: AuthState) => void): () => void {
  authListeners.add(listener);
  listener(authState);
  return () => authListeners.delete(listener);
}

export function getAuthState(): AuthState {
  return authState;
}

/**
 * Initialize auth - uses dev mode for now
 */
export async function initializeFirebase(): Promise<void> {
  // For now, auto-login with dev user
  authState = {
    user: DEV_USER,
    token: 'dev-token',
    loading: false,
    error: null,
    initialized: true,
    devMode: true,
  };
  notifyListeners();
  console.log('🔧 Running in dev mode (Firebase SDK not installed)');
}

/**
 * Sign in - dev mode auto-succeeds
 */
export async function signInWithGoogle(): Promise<void> {
  authState = {
    user: DEV_USER,
    token: 'dev-token',
    loading: false,
    error: null,
    initialized: true,
    devMode: true,
  };
  notifyListeners();
}

/**
 * Sign out
 */
export async function signOut(): Promise<void> {
  authState = {
    user: null,
    token: null,
    loading: false,
    error: null,
    initialized: true,
    devMode: true,
  };
  notifyListeners();
}

/**
 * Get current ID token
 */
export async function getIdToken(): Promise<string | null> {
  return authState.token;
}

/**
 * Check if Firebase is configured
 */
export function isFirebaseConfigured(): boolean {
  return false; // Dev mode
}
