/**
 * API Client
 *
 * Handles all communication with the server.
 * Uses Firebase Auth for authentication.
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
import { getIdToken } from './firebase';

// ============================================================================
// CONFIGURATION
// ============================================================================

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:3001';

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

  // Get auth token
  const token = await getIdToken();
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  } else {
    // Dev mode fallback
    headers['X-Dev-Auth'] = 'true';
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
