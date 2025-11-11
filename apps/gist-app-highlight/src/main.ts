/**
 * Sideshow - Main Application Entry Point
 */

import './style.css';
import type { AppState, Route } from './models';
import { onAuthChange, signInWithGoogle, signOut } from './auth';
import { getGist, createGist, updateGist, getUserGists } from './db';
import { parseRoute, onRouteChange, navigateTo } from './router';
import { renderHeader, renderHome, renderEditor, setupEditorHandlers, showShareModal } from './ui';
import { extractTitle } from './markdown';

/**
 * Global application state
 */
let appState: AppState = {
  user: null,
  gist: null,
  viewMode: 'preview',
  isOwner: false,
  selectedHighlightId: null,
};

let cleanupHandlers: (() => void)[] = [];

/**
 * Initialize the application
 */
async function init() {
  // Setup auth listener
  onAuthChange((user) => {
    appState.user = user;
    render();
  });

  // Setup route listener
  onRouteChange((route) => {
    handleRouteChange(route);
  });

  // Initial render
  const initialRoute = parseRoute();
  await handleRouteChange(initialRoute);
}

/**
 * Handle route changes
 */
async function handleRouteChange(route: Route) {
  // Cleanup previous handlers
  cleanupHandlers.forEach(fn => fn());
  cleanupHandlers = [];

  switch (route.type) {
    case 'home':
      await renderHomePage();
      break;

    case 'create':
      await handleCreate();
      break;

    case 'edit':
      await handleEdit(route.gistId);
      break;

    case 'view':
      await handleView(route.gistId);
      break;
  }
}

/**
 * Render the home page
 */
async function renderHomePage() {
  appState.gist = null;
  appState.isOwner = false;

  const gists = appState.user ? await getUserGists(appState.user.uid) : [];
  render(renderHome(appState.user, gists));
}

/**
 * Handle create new gist
 */
async function handleCreate() {
  if (!appState.user) {
    alert('Please sign in to create a gist');
    navigateTo({ type: 'home' });
    return;
  }

  // Create a new empty gist
  const gist = await createGist('# New Gist\n\nStart writing...', appState.user.uid, 'New Gist');

  // Navigate to edit mode
  navigateTo({ type: 'edit', gistId: gist.id });
}

/**
 * Handle edit mode
 */
async function handleEdit(gistId: string) {
  if (!appState.user) {
    // Redirect to view mode if not signed in
    navigateTo({ type: 'view', gistId });
    return;
  }

  const gist = await getGist(gistId);

  if (!gist) {
    render('<div class="error">Gist not found</div>');
    return;
  }

  // Check ownership
  if (gist.createdBy !== appState.user.uid) {
    // Not the owner, redirect to view mode
    navigateTo({ type: 'view', gistId });
    return;
  }

  appState.gist = gist;
  appState.isOwner = true;
  appState.viewMode = 'preview';

  render();
}

/**
 * Handle view mode (public viewing)
 */
async function handleView(gistId: string) {
  const gist = await getGist(gistId);

  if (!gist) {
    render('<div class="error">Gist not found</div>');
    return;
  }

  appState.gist = gist;
  appState.isOwner = appState.user?.uid === gist.createdBy;
  appState.viewMode = 'preview';

  render();
}

/**
 * Update application state
 */
function updateState(newState: Partial<AppState>) {
  appState = { ...appState, ...newState };
  render();
}

/**
 * Render the application
 */
function render(content?: string) {
  const app = document.querySelector<HTMLDivElement>('#app')!;

  if (content) {
    // Simple content render (home page, error, etc.)
    app.innerHTML = `
      ${renderHeader(appState, handleHeaderAction)}
      <main>${content}</main>
    `;
    setupHeaderHandlers();
    return;
  }

  // Full app render with gist editor
  const editorContent = appState.gist ? renderEditor(appState) : '';

  app.innerHTML = `
    ${renderHeader(appState, handleHeaderAction)}
    <main>${editorContent}</main>
  `;

  setupHeaderHandlers();

  // Setup editor-specific handlers
  if (appState.gist) {
    const cleanup = setupEditorHandlers(appState, updateState);
    cleanupHandlers.push(cleanup);
  }
}

/**
 * Setup header event handlers
 */
function setupHeaderHandlers() {
  document.querySelectorAll('[data-action]').forEach(element => {
    element.addEventListener('click', (e) => {
      e.preventDefault();
      const action = (element as HTMLElement).dataset.action;
      if (action) {
        handleHeaderAction(action);
      }
    });
  });
}

/**
 * Handle header actions
 */
async function handleHeaderAction(action: string) {
  switch (action) {
    case 'sign-in':
      try {
        await signInWithGoogle();
      } catch (error) {
        console.error('Sign in failed:', error);
        alert('Failed to sign in. Please try again.');
      }
      break;

    case 'sign-out':
      try {
        await signOut();
        navigateTo({ type: 'home' });
      } catch (error) {
        console.error('Sign out failed:', error);
      }
      break;

    case 'home':
      navigateTo({ type: 'home' });
      break;

    case 'create':
      await handleCreate();
      break;

    case 'mode-edit':
      appState.viewMode = 'edit';
      render();
      break;

    case 'mode-preview':
      appState.viewMode = 'preview';
      render();
      break;

    case 'save':
      await handleSave();
      break;

    case 'share':
      if (appState.gist) {
        showShareModal(appState.gist.id);
      }
      break;
  }
}

/**
 * Handle save action
 */
async function handleSave() {
  if (!appState.gist || !appState.isOwner) {
    return;
  }

  try {
    // If in edit mode, get the content from the editor
    if (appState.viewMode === 'edit') {
      const editor = document.querySelector<HTMLTextAreaElement>('#markdown-editor');
      if (editor) {
        appState.gist.markdown = editor.value;
        appState.gist.title = extractTitle(editor.value);
      }
    }

    await updateGist(appState.gist);
    alert('Gist saved successfully!');

    // If we were in edit mode, switch to preview to see the changes
    if (appState.viewMode === 'edit') {
      appState.viewMode = 'preview';
      render();
    }
  } catch (error) {
    console.error('Failed to save gist:', error);
    alert('Failed to save gist. Please try again.');
  }
}

// Initialize the app when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
