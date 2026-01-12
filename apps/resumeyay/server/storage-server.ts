/**
 * Git-Backed Storage Server for Resumeyay
 *
 * Stores workspace data as JSON files with git version control.
 * Each save creates a git commit for full history tracking.
 */

import { serve } from 'bun';
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'fs';
import { join } from 'path';
import { execSync } from 'child_process';

const PORT = process.env.PORT || 3001;
const DATA_DIR = process.env.DATA_DIR || join(import.meta.dir, '..', 'data');
const WORKSPACE_FILE = 'workspace.json';

// Ensure data directory exists and is a git repo
function initDataDir() {
  if (!existsSync(DATA_DIR)) {
    mkdirSync(DATA_DIR, { recursive: true });
    console.log(`Created data directory: ${DATA_DIR}`);
  }

  const gitDir = join(DATA_DIR, '.git');
  if (!existsSync(gitDir)) {
    execSync('git init', { cwd: DATA_DIR });
    console.log(`Initialized git repo in: ${DATA_DIR}`);
  }
}

// Git operations
function gitCommit(message: string) {
  try {
    execSync('git add -A', { cwd: DATA_DIR });
    execSync(`git commit -m "${message.replace(/"/g, '\\"')}"`, { cwd: DATA_DIR });
    return true;
  } catch (error) {
    // Commit might fail if nothing changed
    console.log('Git commit skipped (no changes or error)');
    return false;
  }
}

function gitHistory(limit = 50): Array<{ sha: string; message: string; date: string }> {
  try {
    const output = execSync(
      `git log --pretty=format:'{"sha":"%h","message":"%s","date":"%ci"}' -n ${limit}`,
      { cwd: DATA_DIR, encoding: 'utf-8' }
    );
    return output
      .trim()
      .split('\n')
      .filter(line => line)
      .map(line => JSON.parse(line));
  } catch {
    return [];
  }
}

function gitRevert(sha: string): boolean {
  try {
    execSync(`git checkout ${sha} -- ${WORKSPACE_FILE}`, { cwd: DATA_DIR });
    gitCommit(`Revert to ${sha}`);
    return true;
  } catch (error) {
    console.error('Git revert failed:', error);
    return false;
  }
}

function gitShowVersion(sha: string): string | null {
  try {
    return execSync(`git show ${sha}:${WORKSPACE_FILE}`, { cwd: DATA_DIR, encoding: 'utf-8' });
  } catch {
    return null;
  }
}

// File operations
function loadWorkspace(): string | null {
  const filePath = join(DATA_DIR, WORKSPACE_FILE);
  if (existsSync(filePath)) {
    return readFileSync(filePath, 'utf-8');
  }
  return null;
}

function saveWorkspace(data: string, message?: string): boolean {
  const filePath = join(DATA_DIR, WORKSPACE_FILE);
  writeFileSync(filePath, data, 'utf-8');
  gitCommit(message || `Save workspace ${new Date().toISOString()}`);
  return true;
}

// CORS headers
const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

// Request handler
async function handleRequest(req: Request): Promise<Response> {
  const url = new URL(req.url);
  const path = url.pathname;
  const method = req.method;

  // Handle CORS preflight
  if (method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: corsHeaders });
  }

  // Routes
  try {
    // GET /workspace - Load workspace
    if (method === 'GET' && path === '/workspace') {
      const data = loadWorkspace();
      if (data) {
        return new Response(data, {
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        });
      }
      return new Response(JSON.stringify({ error: 'No workspace found' }), {
        status: 404,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      });
    }

    // PUT /workspace - Save workspace
    if (method === 'PUT' && path === '/workspace') {
      const body = await req.text();
      const message = url.searchParams.get('message') || undefined;

      // Validate JSON
      try {
        JSON.parse(body);
      } catch {
        return new Response(JSON.stringify({ error: 'Invalid JSON' }), {
          status: 400,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        });
      }

      saveWorkspace(body, message);
      return new Response(JSON.stringify({ success: true }), {
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      });
    }

    // GET /history - Get git history
    if (method === 'GET' && path === '/history') {
      const limit = parseInt(url.searchParams.get('limit') || '50');
      const history = gitHistory(limit);
      return new Response(JSON.stringify(history), {
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      });
    }

    // GET /version/:sha - Get specific version
    if (method === 'GET' && path.startsWith('/version/')) {
      const sha = path.split('/')[2];
      const data = gitShowVersion(sha);
      if (data) {
        return new Response(data, {
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        });
      }
      return new Response(JSON.stringify({ error: 'Version not found' }), {
        status: 404,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      });
    }

    // POST /revert/:sha - Revert to specific version
    if (method === 'POST' && path.startsWith('/revert/')) {
      const sha = path.split('/')[2];
      const success = gitRevert(sha);
      if (success) {
        const data = loadWorkspace();
        return new Response(data || JSON.stringify({ success: true }), {
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        });
      }
      return new Response(JSON.stringify({ error: 'Revert failed' }), {
        status: 500,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      });
    }

    // GET /health - Health check
    if (method === 'GET' && path === '/health') {
      return new Response(JSON.stringify({ status: 'ok', dataDir: DATA_DIR }), {
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      });
    }

    // 404 for unknown routes
    return new Response(JSON.stringify({ error: 'Not found' }), {
      status: 404,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });
  } catch (error) {
    console.error('Request error:', error);
    return new Response(JSON.stringify({ error: 'Internal server error' }), {
      status: 500,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });
  }
}

// Initialize and start server
initDataDir();

serve({
  port: PORT,
  fetch: handleRequest,
});

console.log(`🗄️  Storage server running on http://localhost:${PORT}`);
console.log(`📁 Data directory: ${DATA_DIR}`);
