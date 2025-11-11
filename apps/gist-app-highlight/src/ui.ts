/**
 * UI components and rendering
 */

import type { Gist, User, ViewMode } from './models';
import { renderMarkdown, applyHighlights, extractTitle } from './markdown';
import {
  getSelectionInfo,
  createHighlight,
  clearSelection,
  setupHighlightClickHandlers,
  scrollToHighlight,
  emphasizeHighlight,
} from './highlights';
import { saveHighlight, deleteHighlight } from './db';
import { getShareableUrl } from './router';

/**
 * Application state
 */
export interface AppState {
  user: User | null;
  gist: Gist | null;
  viewMode: ViewMode;
  isOwner: boolean;
  selectedHighlightId: string | null;
}

/**
 * Render the application header
 */
export function renderHeader(state: AppState, _onAction: (action: string) => void): string {
  const { user, gist, viewMode, isOwner } = state;

  const userSection = user
    ? `
      <div class="user-info">
        ${user.photoURL ? `<img src="${user.photoURL}" alt="${user.displayName}" class="user-avatar">` : ''}
        <span class="user-name">${user.displayName || user.email}</span>
        <button class="btn-secondary" data-action="sign-out">Sign Out</button>
      </div>
    `
    : `
      <button class="btn-primary" data-action="sign-in">Sign In with Google</button>
    `;

  const editorControls = isOwner && gist
    ? `
      <div class="editor-controls">
        <button class="btn-tab ${viewMode === 'edit' ? 'active' : ''}" data-action="mode-edit">Edit</button>
        <button class="btn-tab ${viewMode === 'preview' ? 'active' : ''}" data-action="mode-preview">Preview</button>
        <button class="btn-primary" data-action="save">Save</button>
        <button class="btn-secondary" data-action="share">Share</button>
      </div>
    `
    : '';

  return `
    <header class="app-header">
      <div class="header-left">
        <h1 class="app-title"><a href="#/" data-action="home">Sideshow</a></h1>
        ${editorControls}
      </div>
      <div class="header-right">
        ${userSection}
      </div>
    </header>
  `;
}

/**
 * Render the home page (list of gists)
 */
export function renderHome(user: User | null, gists: Gist[]): string {
  if (!user) {
    return `
      <div class="welcome">
        <h2>Welcome to Sideshow</h2>
        <p>Create annotated markdown documents with highlights and sidenotes.</p>
        <p>Sign in to get started.</p>
      </div>
    `;
  }

  const gistList = gists.length > 0
    ? gists.map(gist => {
        const title = gist.title || extractTitle(gist.markdown);
        const date = gist.updatedAt.toLocaleDateString();
        const highlightCount = gist.highlights.length;
        return `
          <div class="gist-item">
            <a href="#/${gist.id}" class="gist-link">
              <h3>${escapeHtml(title)}</h3>
              <div class="gist-meta">
                <span>${date}</span>
                <span>${highlightCount} highlight${highlightCount !== 1 ? 's' : ''}</span>
              </div>
            </a>
          </div>
        `;
      }).join('')
    : '<p class="empty-state">No gists yet. Create your first one!</p>';

  return `
    <div class="home">
      <div class="home-header">
        <h2>My Gists</h2>
        <button class="btn-primary" data-action="create">Create New Gist</button>
      </div>
      <div class="gist-list">
        ${gistList}
      </div>
    </div>
  `;
}

/**
 * Render the editor view
 */
export function renderEditor(state: AppState): string {
  const { gist, viewMode, isOwner } = state;

  if (!gist) {
    return '<div class="error">Gist not found</div>';
  }

  const readonly = !isOwner;

  if (viewMode === 'edit') {
    return `
      <div class="editor-container">
        <textarea
          id="markdown-editor"
          class="markdown-editor"
          placeholder="Paste your markdown here..."
          ${readonly ? 'readonly' : ''}
        >${escapeHtml(gist.markdown)}</textarea>
      </div>
    `;
  } else {
    // Preview mode
    const rendered = renderMarkdown(gist.markdown);
    const withHighlights = applyHighlights(rendered, gist.highlights);

    return `
      <div class="preview-container">
        <div class="preview-content" id="preview-content">
          ${withHighlights}
        </div>
        <div class="annotations-panel" id="annotations-panel">
          ${renderAnnotations(gist, state.selectedHighlightId)}
        </div>
      </div>
    `;
  }
}

/**
 * Render annotations panel
 */
export function renderAnnotations(gist: Gist, selectedId: string | null): string {
  if (gist.highlights.length === 0) {
    return `
      <div class="annotations-empty">
        <p>No highlights yet.</p>
        <p class="help-text">Select text to create a highlight and add annotations.</p>
      </div>
    `;
  }

  const highlights = [...gist.highlights].sort((a, b) => a.startOffset - b.startOffset);

  return `
    <div class="annotations-list">
      <h3>Annotations</h3>
      ${highlights.map(h => renderAnnotation(h, h.id === selectedId)).join('')}
    </div>
  `;
}

/**
 * Render a single annotation
 */
function renderAnnotation(highlight: Gist['highlights'][0], isSelected: boolean): string {
  const excerptLength = 60;
  const excerpt = highlight.selectedText.length > excerptLength
    ? highlight.selectedText.substring(0, excerptLength) + '...'
    : highlight.selectedText;

  const renderedAnnotation = renderMarkdown(highlight.annotation);

  return `
    <div class="annotation-item ${isSelected ? 'selected' : ''}" data-highlight-id="${highlight.id}">
      <div class="annotation-excerpt">"${escapeHtml(excerpt)}"</div>
      <div class="annotation-content">${renderedAnnotation}</div>
      <div class="annotation-actions">
        <button class="btn-text" data-action="edit-annotation" data-highlight-id="${highlight.id}">Edit</button>
        <button class="btn-text" data-action="delete-highlight" data-highlight-id="${highlight.id}">Delete</button>
      </div>
    </div>
  `;
}

/**
 * Show modal for creating/editing annotation
 */
export function showAnnotationModal(
  selectionText: string,
  existingAnnotation?: string,
  onSave?: (annotation: string) => void,
  onCancel?: () => void
): void {
  const modal = document.createElement('div');
  modal.className = 'modal';
  modal.innerHTML = `
    <div class="modal-content">
      <h3>Add Annotation</h3>
      <div class="modal-excerpt">"${escapeHtml(selectionText.substring(0, 100))}${selectionText.length > 100 ? '...' : ''}"</div>
      <textarea
        id="annotation-input"
        class="annotation-input"
        placeholder="Enter your annotation (markdown supported)..."
      >${escapeHtml(existingAnnotation || '')}</textarea>
      <div class="modal-actions">
        <button class="btn-primary" id="save-annotation">Save</button>
        <button class="btn-secondary" id="cancel-annotation">Cancel</button>
      </div>
    </div>
  `;

  document.body.appendChild(modal);

  const input = modal.querySelector('#annotation-input') as HTMLTextAreaElement;
  const saveBtn = modal.querySelector('#save-annotation') as HTMLButtonElement;
  const cancelBtn = modal.querySelector('#cancel-annotation') as HTMLButtonElement;

  input.focus();

  const cleanup = () => {
    modal.remove();
  };

  saveBtn.onclick = () => {
    const annotation = input.value.trim();
    if (annotation && onSave) {
      onSave(annotation);
    }
    cleanup();
  };

  cancelBtn.onclick = () => {
    if (onCancel) {
      onCancel();
    }
    cleanup();
  };

  // Close on background click
  modal.onclick = (e) => {
    if (e.target === modal) {
      if (onCancel) {
        onCancel();
      }
      cleanup();
    }
  };

  // ESC to close
  const escHandler = (e: KeyboardEvent) => {
    if (e.key === 'Escape') {
      if (onCancel) {
        onCancel();
      }
      cleanup();
      document.removeEventListener('keydown', escHandler);
    }
  };
  document.addEventListener('keydown', escHandler);
}

/**
 * Show share modal
 */
export function showShareModal(gistId: string): void {
  const url = getShareableUrl(gistId);

  const modal = document.createElement('div');
  modal.className = 'modal';
  modal.innerHTML = `
    <div class="modal-content">
      <h3>Share Gist</h3>
      <p>Anyone with this link can view your gist:</p>
      <div class="share-url-container">
        <input type="text" class="share-url" value="${url}" readonly id="share-url">
        <button class="btn-primary" id="copy-url">Copy</button>
      </div>
      <div class="modal-actions">
        <button class="btn-secondary" id="close-share">Close</button>
      </div>
    </div>
  `;

  document.body.appendChild(modal);

  const input = modal.querySelector('#share-url') as HTMLInputElement;
  const copyBtn = modal.querySelector('#copy-url') as HTMLButtonElement;
  const closeBtn = modal.querySelector('#close-share') as HTMLButtonElement;

  input.select();

  copyBtn.onclick = async () => {
    try {
      await navigator.clipboard.writeText(url);
      copyBtn.textContent = 'Copied!';
      setTimeout(() => {
        copyBtn.textContent = 'Copy';
      }, 2000);
    } catch (error) {
      console.error('Failed to copy:', error);
      alert('Failed to copy URL');
    }
  };

  const cleanup = () => {
    modal.remove();
  };

  closeBtn.onclick = cleanup;

  modal.onclick = (e) => {
    if (e.target === modal) {
      cleanup();
    }
  };
}

/**
 * Setup event handlers for the editor
 */
export function setupEditorHandlers(
  state: AppState,
  onStateChange: (newState: Partial<AppState>) => void
): () => void {
  const cleanupFns: Array<() => void> = [];

  // Setup text selection handler in preview mode
  if (state.viewMode === 'preview' && state.gist && state.isOwner) {
    const previewContent = document.getElementById('preview-content');
    if (previewContent) {
      const handleMouseUp = () => {
        const selectionInfo = getSelectionInfo(previewContent);
        if (selectionInfo) {
          showAnnotationModal(
            selectionInfo.selectedText,
            undefined,
            async (annotation) => {
              const highlight = createHighlight(selectionInfo, annotation);
              if (state.gist) {
                await saveHighlight(state.gist.id, highlight);
                state.gist.highlights.push(highlight);
                onStateChange({ gist: state.gist });
              }
              clearSelection();
            },
            () => {
              clearSelection();
            }
          );
        }
      };

      previewContent.addEventListener('mouseup', handleMouseUp);
      cleanupFns.push(() => previewContent.removeEventListener('mouseup', handleMouseUp));

      // Setup highlight click handlers
      const cleanupHighlightHandlers = setupHighlightClickHandlers(
        previewContent,
        (highlightId) => {
          onStateChange({ selectedHighlightId: highlightId });
          emphasizeHighlight(highlightId);
          scrollToHighlight(highlightId);
        }
      );
      cleanupFns.push(cleanupHighlightHandlers);
    }
  }

  // Setup annotation panel handlers
  const annotationPanel = document.getElementById('annotations-panel');
  if (annotationPanel) {
    const handleClick = async (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      const action = target.dataset.action;
      const highlightId = target.dataset.highlightId;

      if (!action || !highlightId || !state.gist) return;

      if (action === 'delete-highlight') {
        if (confirm('Delete this highlight?')) {
          await deleteHighlight(state.gist.id, highlightId);
          state.gist.highlights = state.gist.highlights.filter(h => h.id !== highlightId);
          onStateChange({ gist: state.gist, selectedHighlightId: null });
        }
      } else if (action === 'edit-annotation') {
        const highlight = state.gist.highlights.find(h => h.id === highlightId);
        if (highlight) {
          showAnnotationModal(
            highlight.selectedText,
            highlight.annotation,
            async (annotation) => {
              highlight.annotation = annotation;
              await saveHighlight(state.gist!.id, highlight);
              onStateChange({ gist: state.gist });
            }
          );
        }
      }
    };

    annotationPanel.addEventListener('click', handleClick);
    cleanupFns.push(() => annotationPanel.removeEventListener('click', handleClick));

    // Click annotation to scroll to highlight
    const handleAnnotationClick = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      const annotationItem = target.closest('.annotation-item') as HTMLElement;
      if (annotationItem) {
        const highlightId = annotationItem.dataset.highlightId;
        if (highlightId) {
          onStateChange({ selectedHighlightId: highlightId });
          emphasizeHighlight(highlightId);
          scrollToHighlight(highlightId);
        }
      }
    };

    annotationPanel.addEventListener('click', handleAnnotationClick);
    cleanupFns.push(() => annotationPanel.removeEventListener('click', handleAnnotationClick));
  }

  return () => {
    cleanupFns.forEach(fn => fn());
  };
}

/**
 * Escape HTML to prevent XSS
 */
function escapeHtml(text: string): string {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}
