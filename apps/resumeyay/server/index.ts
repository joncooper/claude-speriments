/**
 * Resumeyay API Server
 *
 * Hono-based server providing:
 * - Firebase Auth verification
 * - Workspace CRUD (backed by Firestore)
 * - Fit Coach LLM endpoints (Claude API)
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';
import { logger } from 'hono/logger';
import { workspaceRoutes } from './routes/workspace';
import { fitCoachRoutes } from './routes/fit-coach';
import { authMiddleware, authRoutes } from './middleware/auth';

const app = new Hono();

// Global middleware
app.use('*', logger());
app.use('*', cors({
  origin: ['http://localhost:5173', 'http://localhost:3000'],
  credentials: true,
}));

// Health check (no auth required)
app.get('/health', (c) => c.json({ status: 'ok', timestamp: new Date().toISOString() }));

// Auth routes (login callback, etc.)
app.route('/auth', authRoutes);

// Protected API routes
const api = new Hono();
api.use('*', authMiddleware);
api.route('/workspace', workspaceRoutes);
api.route('/fit-coach', fitCoachRoutes);

app.route('/api', api);

// 404 handler
app.notFound((c) => c.json({ error: 'Not found' }, 404));

// Error handler
app.onError((err, c) => {
  console.error('Server error:', err);
  return c.json({ error: 'Internal server error' }, 500);
});

const port = process.env.PORT || 3001;

export default {
  port,
  fetch: app.fetch,
};

console.log(`🚀 Server running on http://localhost:${port}`);
