/**
 * Fit Coach Routes
 *
 * LLM-powered resume coaching endpoints.
 */

import { Hono } from 'hono';
import {
  parseJobDescription,
  generateCoachingMessage,
  cleanJobDescription,
  analyzeCoverage,
  calculateFitScore,
} from '../services/claude';
import { getFitSessions, saveFitSession } from '../services/firebase';
import type {
  JobDescription,
  FitSession,
  FitCoachMessage,
  Resume,
  ResumeVariant,
  ParsedJobDescription,
  JDRequirement,
} from '../../src/types';
import { v4 as uuid } from 'uuid';

export const fitCoachRoutes = new Hono();

/**
 * POST /api/fit-coach/parse-jd - Parse a job description into requirements
 */
fitCoachRoutes.post('/parse-jd', async (c) => {
  const body = await c.req.json() as { jobDescription: JobDescription };

  if (!body.jobDescription) {
    return c.json({ error: 'Missing jobDescription' }, 400);
  }

  const parsed = await parseJobDescription(body.jobDescription);

  return c.json({ parsed });
});

/**
 * POST /api/fit-coach/clean-jd - Clean messy job description text
 */
fitCoachRoutes.post('/clean-jd', async (c) => {
  const body = await c.req.json() as { rawText: string };

  if (!body.rawText) {
    return c.json({ error: 'Missing rawText' }, 400);
  }

  const cleaned = await cleanJobDescription(body.rawText);

  return c.json({ cleaned });
});

/**
 * POST /api/fit-coach/analyze - Analyze coverage against resume
 */
fitCoachRoutes.post('/analyze', async (c) => {
  const body = await c.req.json() as {
    parsedJD: ParsedJobDescription;
    resume: Resume;
    variant: ResumeVariant;
  };

  if (!body.parsedJD || !body.resume || !body.variant) {
    return c.json({ error: 'Missing required fields' }, 400);
  }

  const analyzed = analyzeCoverage(body.parsedJD, body.resume, body.variant);
  const { score, breakdown } = calculateFitScore(analyzed.requirements);

  return c.json({
    analyzed,
    score,
    breakdown,
  });
});

/**
 * POST /api/fit-coach/start-session - Start a new fit coaching session
 */
fitCoachRoutes.post('/start-session', async (c) => {
  const user = c.get('user');
  const body = await c.req.json() as {
    jobDescription: JobDescription;
    resume: Resume;
    variant: ResumeVariant;
  };

  if (!body.jobDescription || !body.resume || !body.variant) {
    return c.json({ error: 'Missing required fields' }, 400);
  }

  // Parse job description
  const parsed = await parseJobDescription(body.jobDescription);

  // Analyze coverage
  const analyzed = analyzeCoverage(parsed, body.resume, body.variant);
  const { score, breakdown } = calculateFitScore(analyzed.requirements);

  // Create session
  const session: FitSession = {
    id: uuid(),
    jobDescriptionId: body.jobDescription.id,
    variantId: body.variant.id,
    requirements: analyzed.requirements,
    conversationHistory: [],
    overallFitScore: score,
    coverageBreakdown: breakdown,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
    isActive: true,
  };

  // Generate initial coaching message
  const firstGap = session.requirements.find(
    r => r.coverageStatus === 'missing' || r.coverageStatus === 'partial'
  );

  // Welcome message
  session.conversationHistory.push({
    id: uuid(),
    role: 'coach',
    content: `Welcome to Fit Coach! Let's work together to improve your resume's fit for this ${body.jobDescription.title} role at ${body.jobDescription.company}.\n\nYour current score is ${score}% with ${breakdown.strong} strong matches, ${breakdown.partial} partial matches, and ${breakdown.missing} gaps to address.${breakdown.notMe > 0 ? ` (${breakdown.notMe} marked as not applicable)` : ''}`,
    timestamp: new Date().toISOString(),
  });

  // First coaching message about a gap
  if (firstGap) {
    const coachMessage = await generateCoachingMessage(
      firstGap,
      body.resume,
      body.variant,
      session.conversationHistory
    );
    session.conversationHistory.push(coachMessage);
  } else {
    session.conversationHistory.push({
      id: uuid(),
      role: 'coach',
      content: `Great news! Your resume has excellent coverage for this role. You can still review each requirement and refine your wording to make an even stronger impression.`,
      timestamp: new Date().toISOString(),
    });
  }

  // Save session
  await saveFitSession(user.id, session);

  return c.json({ session });
});

/**
 * POST /api/fit-coach/chat - Send message and get coaching response
 */
fitCoachRoutes.post('/chat', async (c) => {
  const user = c.get('user');
  const body = await c.req.json() as {
    sessionId: string;
    message: string;
    session: FitSession;
    resume: Resume;
    variant: ResumeVariant;
    focusedRequirementId?: string;
  };

  if (!body.message || !body.session || !body.resume || !body.variant) {
    return c.json({ error: 'Missing required fields' }, 400);
  }

  const session = body.session;

  // Add user message
  const userMessage: FitCoachMessage = {
    id: uuid(),
    role: 'user',
    content: body.message,
    timestamp: new Date().toISOString(),
    relatedRequirementId: body.focusedRequirementId,
  };
  session.conversationHistory.push(userMessage);

  // Find requirement to coach about
  const focusedReq = body.focusedRequirementId
    ? session.requirements.find(r => r.id === body.focusedRequirementId)
    : session.requirements.find(
        r => r.coverageStatus === 'missing' || r.coverageStatus === 'partial'
      );

  let coachMessage: FitCoachMessage;
  if (focusedReq) {
    coachMessage = await generateCoachingMessage(
      focusedReq,
      body.resume,
      body.variant,
      session.conversationHistory
    );
  } else {
    coachMessage = {
      id: uuid(),
      role: 'coach',
      content: `You've addressed all the key requirements! Is there anything specific you'd like to refine or any other aspects of the job description you'd like to discuss?`,
      timestamp: new Date().toISOString(),
    };
  }

  session.conversationHistory.push(coachMessage);
  session.updatedAt = new Date().toISOString();

  // Save updated session
  await saveFitSession(user.id, session);

  return c.json({
    userMessage,
    coachMessage,
    session,
  });
});

/**
 * POST /api/fit-coach/update-requirement - Update requirement status
 */
fitCoachRoutes.post('/update-requirement', async (c) => {
  const user = c.get('user');
  const body = await c.req.json() as {
    session: FitSession;
    requirementId: string;
    status: 'strong' | 'partial' | 'missing' | 'not-me';
    notMeReason?: string;
  };

  if (!body.session || !body.requirementId || !body.status) {
    return c.json({ error: 'Missing required fields' }, 400);
  }

  const session = body.session;
  const req = session.requirements.find(r => r.id === body.requirementId);

  if (!req) {
    return c.json({ error: 'Requirement not found' }, 404);
  }

  req.coverageStatus = body.status;
  if (body.status === 'not-me' && body.notMeReason) {
    req.notMeReason = body.notMeReason;
  }

  // Recalculate score
  const { score, breakdown } = calculateFitScore(session.requirements);
  session.overallFitScore = score;
  session.coverageBreakdown = breakdown;
  session.updatedAt = new Date().toISOString();

  // Save updated session
  await saveFitSession(user.id, session);

  return c.json({ session });
});

/**
 * POST /api/fit-coach/refresh - Refresh coverage analysis
 */
fitCoachRoutes.post('/refresh', async (c) => {
  const user = c.get('user');
  const body = await c.req.json() as {
    session: FitSession;
    resume: Resume;
    variant: ResumeVariant;
  };

  if (!body.session || !body.resume || !body.variant) {
    return c.json({ error: 'Missing required fields' }, 400);
  }

  const session = body.session;

  // Create a ParsedJobDescription from session requirements
  const parsedJD: ParsedJobDescription = {
    id: uuid(),
    originalJobDescriptionId: session.jobDescriptionId,
    title: '',
    company: '',
    requirements: session.requirements,
    parsedAt: new Date().toISOString(),
    rawText: '',
  };

  // Re-analyze coverage (preserving not-me status)
  const analyzed = analyzeCoverage(parsedJD, body.resume, body.variant);

  // Preserve not-me statuses
  for (const req of analyzed.requirements) {
    const existing = session.requirements.find(r => r.id === req.id);
    if (existing?.coverageStatus === 'not-me') {
      req.coverageStatus = 'not-me';
      req.notMeReason = existing.notMeReason;
    }
  }

  session.requirements = analyzed.requirements;
  const { score, breakdown } = calculateFitScore(session.requirements);
  session.overallFitScore = score;
  session.coverageBreakdown = breakdown;
  session.updatedAt = new Date().toISOString();

  // Save updated session
  await saveFitSession(user.id, session);

  return c.json({ session });
});

/**
 * GET /api/fit-coach/sessions - Get all fit sessions
 */
fitCoachRoutes.get('/sessions', async (c) => {
  const user = c.get('user');
  const sessions = await getFitSessions(user.id);

  return c.json({ sessions });
});

/**
 * DELETE /api/fit-coach/sessions/:id - End/delete a session
 */
fitCoachRoutes.delete('/sessions/:id', async (c) => {
  const user = c.get('user');
  const sessionId = c.req.param('id');

  // For now, we'll just mark it as inactive
  const sessions = await getFitSessions(user.id);
  const session = sessions.find(s => s.id === sessionId);

  if (session) {
    session.isActive = false;
    session.updatedAt = new Date().toISOString();
    await saveFitSession(user.id, session);
  }

  return c.json({ success: true });
});
