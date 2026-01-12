/**
 * Workspace Routes
 *
 * CRUD operations for resume workspace data.
 */

import { Hono } from 'hono';
import {
  getWorkspace,
  saveWorkspace,
  getJobDescriptions,
  saveJobDescription,
  deleteJobDescription,
} from '../services/firebase';
import type { ResumeWorkspace, JobDescription } from '../../src/types';

export const workspaceRoutes = new Hono();

/**
 * GET /api/workspace - Get user's workspace
 */
workspaceRoutes.get('/', async (c) => {
  const user = c.get('user');
  const workspace = await getWorkspace(user.id);

  if (!workspace) {
    return c.json({ workspace: null });
  }

  return c.json({ workspace });
});

/**
 * PUT /api/workspace - Save user's workspace
 */
workspaceRoutes.put('/', async (c) => {
  const user = c.get('user');
  const body = await c.req.json() as { workspace: ResumeWorkspace };

  if (!body.workspace) {
    return c.json({ error: 'Missing workspace data' }, 400);
  }

  await saveWorkspace(user.id, body.workspace);

  return c.json({ success: true });
});

/**
 * GET /api/workspace/jobs - Get all job descriptions
 */
workspaceRoutes.get('/jobs', async (c) => {
  const user = c.get('user');
  const jobs = await getJobDescriptions(user.id);

  return c.json({ jobs });
});

/**
 * POST /api/workspace/jobs - Create/update job description
 */
workspaceRoutes.post('/jobs', async (c) => {
  const user = c.get('user');
  const body = await c.req.json() as { job: JobDescription };

  if (!body.job) {
    return c.json({ error: 'Missing job data' }, 400);
  }

  await saveJobDescription(user.id, body.job);

  return c.json({ success: true, job: body.job });
});

/**
 * DELETE /api/workspace/jobs/:id - Delete job description
 */
workspaceRoutes.delete('/jobs/:id', async (c) => {
  const user = c.get('user');
  const jobId = c.req.param('id');

  await deleteJobDescription(user.id, jobId);

  return c.json({ success: true });
});
