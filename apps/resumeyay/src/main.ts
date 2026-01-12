import { store, workspaceStore, type EntryTemplate } from './store';
import type { Entry, Section, ContentNode, FocusMode, ColumnConfig, StyleSettings } from './types';
import { fitCoachStore, renderFitCoachPanel, getHeatMapClass } from './fit-coach';
import './style.css';

// ============================================================================
// INPUT PRESERVATION & DEBOUNCING
// ============================================================================

// Track active input to prevent re-render during typing
let activeInputInfo: {
  type: 'header' | 'entry' | 'bullet' | 'section' | 'style';
  field?: string;
  entryId?: string;
  sectionId?: string;
  bulletId?: string;
  cursorPos?: number;
} | null = null;

// Debounce timers for different input types
const debounceTimers: Map<string, ReturnType<typeof setTimeout>> = new Map();

// Batch undo: accumulate changes during typing, commit as single undo entry
let undoBatchTimeout: ReturnType<typeof setTimeout> | null = null;
let undoBatchInProgress = false;

function debounce(key: string, fn: () => void, delay: number = 300): void {
  const existingTimer = debounceTimers.get(key);
  if (existingTimer) {
    clearTimeout(existingTimer);
  }
  debounceTimers.set(key, setTimeout(() => {
    debounceTimers.delete(key);
    fn();
  }, delay));
}

function startUndoBatch(): void {
  if (!undoBatchInProgress) {
    undoBatchInProgress = true;
    store.startBatch();
  }
  if (undoBatchTimeout) {
    clearTimeout(undoBatchTimeout);
  }
  // Commit the batch after 1 second of inactivity
  undoBatchTimeout = setTimeout(() => {
    if (undoBatchInProgress) {
      store.endBatch();
      undoBatchInProgress = false;
    }
  }, 1000);
}

// Check if we should skip re-render (user is typing)
function shouldSkipRender(): boolean {
  if (!activeInputInfo) return false;

  // Find the active element
  const activeEl = document.activeElement;
  if (!activeEl || !(activeEl instanceof HTMLInputElement || activeEl instanceof HTMLSelectElement)) {
    activeInputInfo = null;
    return false;
  }

  return true;
}

// Restore focus after a render
function restoreFocus(): void {
  if (!activeInputInfo) return;

  setTimeout(() => {
    let selector = '';

    if (activeInputInfo!.type === 'header' && activeInputInfo!.field) {
      selector = `[data-field="${activeInputInfo!.field}"]`;
    } else if (activeInputInfo!.type === 'bullet' && activeInputInfo!.bulletId) {
      selector = `.bullet-input[data-bullet-id="${activeInputInfo!.bulletId}"]`;
    } else if (activeInputInfo!.type === 'entry' && activeInputInfo!.field) {
      selector = `.entry-row[data-entry-id="${activeInputInfo!.entryId}"] [data-field="${activeInputInfo!.field}"]`;
    } else if (activeInputInfo!.type === 'section' && activeInputInfo!.sectionId) {
      selector = `.section[data-section-id="${activeInputInfo!.sectionId}"] [data-field="section.title"]`;
    }

    if (selector) {
      const input = document.querySelector(selector) as HTMLInputElement;
      if (input) {
        input.focus();
        if (activeInputInfo!.cursorPos !== undefined) {
          input.setSelectionRange(activeInputInfo!.cursorPos, activeInputInfo!.cursorPos);
        }
      }
    }

    activeInputInfo = null;
  }, 0);
}

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================

function escapeHtml(text: string): string {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

function flattenBullets(nodes: ContentNode[], depth: number = 0): Array<{ node: ContentNode; depth: number }> {
  const result: Array<{ node: ContentNode; depth: number }> = [];
  for (const node of nodes) {
    result.push({ node, depth });
    if (node.children.length > 0) {
      result.push(...flattenBullets(node.children, depth + 1));
    }
  }
  return result;
}

function getBulletSymbol(depth: number): string {
  const symbols = ['&bull;', '&#9702;', '&#9642;'];
  return symbols[Math.min(depth, symbols.length - 1)];
}

function truncateText(text: string, maxLength: number): string {
  if (text.length <= maxLength) return text;
  return text.slice(0, maxLength - 3) + '...';
}

// ============================================================================
// KEYBOARD HANDLING
// ============================================================================

// Helper to find section ID for an entry
function findSectionForEntry(entryId: string): string | null {
  const state = store.getState();
  for (const section of state.resume.sections) {
    if (section.entries.some(e => e.id === entryId)) {
      return section.id;
    }
  }
  return null;
}

// Helper to get all bullets in order for an entry
function getAllBulletsInOrder(entryId: string): string[] {
  const state = store.getState();
  const bullets: string[] = [];

  for (const section of state.resume.sections) {
    const entry = section.entries.find(e => e.id === entryId);
    if (entry) {
      const collectBullets = (nodes: ContentNode[]) => {
        for (const node of nodes) {
          bullets.push(node.id);
          collectBullets(node.children);
        }
      };
      collectBullets(entry.content);
      break;
    }
  }
  return bullets;
}

// Helper to get all entries in order
function getAllEntriesInOrder(): Array<{ entryId: string; sectionId: string }> {
  const state = store.getState();
  const entries: Array<{ entryId: string; sectionId: string }> = [];

  for (const section of state.resume.sections) {
    for (const entry of section.entries) {
      entries.push({ entryId: entry.id, sectionId: section.id });
    }
  }
  return entries;
}

function setupKeyboardShortcuts(): void {
  document.addEventListener('keydown', (e) => {
    const state = store.getState();

    // Escape to blur and deselect
    if (e.key === 'Escape') {
      e.preventDefault();
      (document.activeElement as HTMLElement)?.blur();
      store.setActiveEntry(null);
      store.setActiveBullet(null);
      return;
    }

    // Cmd/Ctrl + number for focus modes
    if ((e.metaKey || e.ctrlKey) && !e.shiftKey) {
      switch (e.key) {
        case '1':
          e.preventDefault();
          store.setFocusMode('full-matrix');
          return;
        case '2':
          e.preventDefault();
          store.setFocusMode('narrative');
          return;
        case '3':
          e.preventDefault();
          store.setFocusMode('timeline');
          return;
        case '4':
          e.preventDefault();
          store.setFocusMode('compact');
          return;
        case '\\':
          e.preventDefault();
          store.togglePreview();
          return;
        case 'z':
          e.preventDefault();
          store.undo();
          return;
        case 'd':
        case 'D':
          // Cmd+D to duplicate entry
          if (state.activeEntryId) {
            e.preventDefault();
            const sectionId = findSectionForEntry(state.activeEntryId);
            if (sectionId) {
              const newId = store.duplicateEntry(sectionId, state.activeEntryId);
              if (newId) {
                store.setActiveEntry(newId);
              }
            }
          }
          return;
        case 'Backspace':
          // Cmd+Backspace to delete entry
          if (state.activeEntryId && !document.activeElement?.matches('input')) {
            e.preventDefault();
            const sectionId = findSectionForEntry(state.activeEntryId);
            if (sectionId && confirm('Delete this entry?')) {
              store.deleteEntry(sectionId, state.activeEntryId);
              store.setActiveEntry(null);
            }
          }
          return;
        case 'Enter':
          // Cmd+Enter to add new entry after current
          if (state.activeEntryId) {
            e.preventDefault();
            const sectionId = findSectionForEntry(state.activeEntryId);
            if (sectionId) {
              const newId = store.addEntry(sectionId, state.activeEntryId);
              if (newId) {
                store.setActiveEntry(newId);
                // Focus the first field of the new entry
                setTimeout(() => {
                  const newRow = document.querySelector(`.entry-row[data-entry-id="${newId}"]`);
                  const firstInput = newRow?.querySelector('input') as HTMLInputElement;
                  if (firstInput) firstInput.focus();
                }, 50);
              }
            }
          }
          return;
      }
    }

    // Cmd/Ctrl + Shift shortcuts
    if ((e.metaKey || e.ctrlKey) && e.shiftKey) {
      switch (e.key) {
        case 'z':
        case 'Z':
          e.preventDefault();
          store.redo();
          return;
        case 's':
        case 'S':
          e.preventDefault();
          store.toggleStyleStudio();
          return;
      }
    }

    // Arrow key navigation (without Cmd/Ctrl)
    if (!e.metaKey && !e.ctrlKey && (e.key === 'ArrowUp' || e.key === 'ArrowDown')) {
      const activeEl = document.activeElement;

      // Navigate between bullets
      if (activeEl?.classList.contains('bullet-input') && state.activeEntryId && state.activeBulletId) {
        const bullets = getAllBulletsInOrder(state.activeEntryId);
        const currentIndex = bullets.indexOf(state.activeBulletId);

        if (currentIndex !== -1) {
          const nextIndex = e.key === 'ArrowUp' ? currentIndex - 1 : currentIndex + 1;

          if (nextIndex >= 0 && nextIndex < bullets.length) {
            e.preventDefault();
            const nextBulletId = bullets[nextIndex];
            store.setActiveBullet(nextBulletId);
            setTimeout(() => {
              const nextInput = document.querySelector(`.bullet-input[data-bullet-id="${nextBulletId}"]`) as HTMLInputElement;
              if (nextInput) nextInput.focus();
            }, 0);
            return;
          }
        }
      }

      // Navigate between entries when not in an input
      if (!activeEl?.matches('input') && state.activeEntryId) {
        const entries = getAllEntriesInOrder();
        const currentIndex = entries.findIndex(e => e.entryId === state.activeEntryId);

        if (currentIndex !== -1) {
          const nextIndex = e.key === 'ArrowUp' ? currentIndex - 1 : currentIndex + 1;

          if (nextIndex >= 0 && nextIndex < entries.length) {
            e.preventDefault();
            store.setActiveEntry(entries[nextIndex].entryId);
            return;
          }
        }
      }
    }

    // Handle bullet-specific shortcuts
    const activeBulletId = state.activeBulletId;
    const activeEntryId = state.activeEntryId;
    if (activeBulletId && activeEntryId) {
      const bulletInput = document.querySelector(`.bullet-input[data-bullet-id="${activeBulletId}"]`) as HTMLInputElement;
      if (bulletInput && document.activeElement === bulletInput) {
        // Tab to indent
        if (e.key === 'Tab' && !e.shiftKey) {
          e.preventDefault();
          store.indentBullet(activeEntryId, activeBulletId);
          return;
        }
        // Shift+Tab to outdent
        if (e.key === 'Tab' && e.shiftKey) {
          e.preventDefault();
          store.outdentBullet(activeEntryId, activeBulletId);
          return;
        }
        // Enter to add new bullet
        if (e.key === 'Enter' && !e.metaKey && !e.ctrlKey) {
          e.preventDefault();
          const newId = store.addBullet(activeEntryId, activeBulletId);
          if (newId) {
            store.setActiveBullet(newId);
            setTimeout(() => {
              const newInput = document.querySelector(`.bullet-input[data-bullet-id="${newId}"]`) as HTMLInputElement;
              if (newInput) newInput.focus();
            }, 50);
          }
          return;
        }
        // Cmd+Up/Down to move bullet
        if ((e.metaKey || e.ctrlKey) && (e.key === 'ArrowUp' || e.key === 'ArrowDown')) {
          e.preventDefault();
          store.moveBullet(activeEntryId, activeBulletId, e.key === 'ArrowUp' ? 'up' : 'down');
          return;
        }
        // Backspace at start of empty bullet to delete
        if (e.key === 'Backspace' && bulletInput.value === '' && bulletInput.selectionStart === 0) {
          e.preventDefault();
          const prevId = store.deleteBullet(activeEntryId, activeBulletId);
          if (prevId) {
            store.setActiveBullet(prevId);
            setTimeout(() => {
              const prevInput = document.querySelector(`.bullet-input[data-bullet-id="${prevId}"]`) as HTMLInputElement;
              if (prevInput) {
                prevInput.focus();
                prevInput.setSelectionRange(prevInput.value.length, prevInput.value.length);
              }
            }, 50);
          }
          return;
        }
      }
    }
  });
}

// ============================================================================
// RENDER FUNCTIONS
// ============================================================================

function renderHeader(): string {
  const { resume } = store.getState();
  const { header } = resume;

  return `
    <div class="header-editor">
      <div class="header-name">
        <input type="text" value="${escapeHtml(header.name)}"
               placeholder="Your Name"
               data-field="header.name" />
      </div>
      <div class="header-details">
        <input type="email" value="${escapeHtml(header.email)}"
               placeholder="email@example.com"
               data-field="header.email" />
        <input type="tel" value="${escapeHtml(header.phone)}"
               placeholder="(555) 123-4567"
               data-field="header.phone" />
        <input type="text" value="${escapeHtml(header.location)}"
               placeholder="City, State"
               data-field="header.location" />
      </div>
      <div class="header-links">
        ${header.links.map(link => `
          <div class="header-link" data-link-id="${link.id}">
            <input type="text" value="${escapeHtml(link.label)}" placeholder="Label" data-field="link.label" />
            <input type="url" value="${escapeHtml(link.url)}" placeholder="URL" data-field="link.url" />
            <button class="btn-icon btn-remove-link" title="Remove link">&times;</button>
          </div>
        `).join('')}
        <button class="btn-add-link">+ Add Link</button>
      </div>
    </div>
  `;
}

function renderBullets(entryId: string, nodes: ContentNode[], depth: number = 0): string {
  const { activeBulletId, columnConfig, focusMode } = store.getState();
  const isCompact = focusMode === 'compact';
  const isCollapsed = columnConfig.content === 'collapsed';

  if (isCollapsed) {
    const flat = flattenBullets(nodes);
    const preview = flat.slice(0, 2).map(b => truncateText(b.node.text, 30)).join(', ');
    const more = flat.length > 2 ? ` +${flat.length - 2}` : '';
    return `<div class="content-collapsed-preview">${escapeHtml(preview)}${more}</div>`;
  }

  if (isCompact) {
    const flat = flattenBullets(nodes);
    const preview = flat.slice(0, 2).map(b => truncateText(b.node.text, 40)).join('; ');
    const more = flat.length > 2 ? `, +${flat.length - 2}` : '';
    return `<div class="content-compact">${escapeHtml(preview)}${more}</div>`;
  }

  return nodes.map(node => {
    const isActive = activeBulletId === node.id;
    return `
      <div class="bullet-item ${isActive ? 'active' : ''}"
           data-bullet-id="${node.id}"
           data-entry-id="${entryId}"
           style="margin-left: ${depth * 20}px">
        <span class="bullet-symbol">${getBulletSymbol(depth)}</span>
        <input type="text"
               class="bullet-input"
               value="${escapeHtml(node.text)}"
               placeholder="Enter accomplishment..."
               data-bullet-id="${node.id}"
               data-entry-id="${entryId}" />
      </div>
      ${node.children.length > 0 ? renderBullets(entryId, node.children, depth + 1) : ''}
    `;
  }).join('');
}

function renderEntry(section: Section, entry: Entry, _index: number): string {
  const { columnConfig, activeEntryId, focusMode } = store.getState();
  const isActive = activeEntryId === entry.id;
  const isCompact = focusMode === 'compact';

  const getColumnClass = (col: keyof ColumnConfig): string => {
    const state = columnConfig[col];
    return `column-${col} column-${state}`;
  };

  return `
    <div class="entry-row ${isActive ? 'active' : ''} ${isCompact ? 'compact' : ''}"
         data-entry-id="${entry.id}"
         data-section-id="${section.id}">
      <div class="${getColumnClass('employer')}">
        ${columnConfig.employer === 'collapsed'
          ? `<div class="column-handle" title="${escapeHtml(entry.organization)}">${entry.organization.charAt(0) || '?'}</div>`
          : `<input type="text" value="${escapeHtml(entry.organization)}"
                   placeholder="Company" data-field="organization" />`
        }
      </div>
      <div class="${getColumnClass('role')}">
        ${columnConfig.role === 'collapsed'
          ? `<div class="column-handle" title="${escapeHtml(entry.role)}">${entry.role.charAt(0) || '?'}</div>`
          : `<input type="text" value="${escapeHtml(entry.role)}"
                   placeholder="Role" data-field="role" />`
        }
      </div>
      <div class="${getColumnClass('metadata')}">
        ${columnConfig.metadata === 'collapsed'
          ? `<div class="column-handle" title="${entry.dateStart} - ${entry.dateEnd}">&hellip;</div>`
          : `<div class="metadata-fields">
               <input type="text" value="${escapeHtml(entry.dateStart)}"
                      placeholder="Start" data-field="dateStart" class="date-field" />
               <span class="date-separator">&ndash;</span>
               <input type="text" value="${escapeHtml(entry.dateEnd)}"
                      placeholder="End" data-field="dateEnd" class="date-field" />
               <input type="text" value="${escapeHtml(entry.location)}"
                      placeholder="Location" data-field="location" class="location-field" />
             </div>`
        }
      </div>
      <div class="${getColumnClass('content')}">
        ${columnConfig.content === 'collapsed'
          ? `<div class="column-handle" title="Content">&#9656;</div>`
          : `<div class="content-bullets">
               ${renderBullets(entry.id, entry.content)}
               ${!isCompact ? `<button class="btn-add-bullet" data-entry-id="${entry.id}">+ Add bullet</button>` : ''}
             </div>`
        }
      </div>
    </div>
  `;
}

function renderSection(section: Section): string {
  const { columnConfig, focusMode } = store.getState();

  return `
    <div class="section" data-section-id="${section.id}">
      <div class="section-header">
        <h2 class="section-title">
          <input type="text" value="${escapeHtml(section.title)}"
                 placeholder="Section Title" data-field="section.title" />
        </h2>
        <div class="section-actions">
          <div class="add-entry-dropdown">
            <button class="btn-add-entry" data-section-id="${section.id}">+ Add Entry</button>
            <div class="template-dropdown" data-section-id="${section.id}">
              <button class="template-option" data-template="blank">Blank Entry</button>
              <button class="template-option" data-template="software-engineer">Software Engineer</button>
              <button class="template-option" data-template="product-manager">Product Manager</button>
              <button class="template-option" data-template="education">Education</button>
              <button class="template-option" data-template="project">Project</button>
            </div>
          </div>
        </div>
      </div>
      <div class="entries-container">
        <div class="column-headers ${focusMode}">
          <div class="column-header column-employer ${columnConfig.employer}" data-column="employer">
            ${columnConfig.employer === 'collapsed' ? '&#9656;' : 'Employer'}
          </div>
          <div class="column-header column-role ${columnConfig.role}" data-column="role">
            ${columnConfig.role === 'collapsed' ? '&#9656;' : 'Role'}
          </div>
          <div class="column-header column-metadata ${columnConfig.metadata}" data-column="metadata">
            ${columnConfig.metadata === 'collapsed' ? '&#9656;' : 'Metadata'}
          </div>
          <div class="column-header column-content ${columnConfig.content}" data-column="content">
            ${columnConfig.content === 'collapsed' ? '&#9656;' : 'Content'}
          </div>
        </div>
        <div class="entries">
          ${section.entries.map((entry, i) => renderEntry(section, entry, i)).join('')}
        </div>
      </div>
    </div>
  `;
}

function renderEditor(): string {
  const { resume, focusMode } = store.getState();

  return `
    <div class="editor-container ${focusMode}">
      ${renderHeader()}
      <div class="sections">
        ${resume.sections.map(section => renderSection(section)).join('')}
      </div>
      <div class="add-section-container">
        <button class="btn-add-section">+ Add Section</button>
      </div>
    </div>
  `;
}

function renderFloatingHeader(): string {
  const { activeEntryId, focusMode, resume } = store.getState();

  if (focusMode !== 'narrative' || !activeEntryId) return '';

  for (const section of resume.sections) {
    const entry = section.entries.find(e => e.id === activeEntryId);
    if (entry) {
      return `
        <div class="floating-header">
          <span class="floating-org">${escapeHtml(entry.organization)}</span>
          <span class="floating-sep">&middot;</span>
          <span class="floating-role">${escapeHtml(entry.role)}</span>
          <span class="floating-sep">&middot;</span>
          <span class="floating-date">${escapeHtml(entry.dateStart)} &ndash; ${escapeHtml(entry.dateEnd)}</span>
        </div>
      `;
    }
  }
  return '';
}

// Helper to count words and estimate page fit
function getResumeStats(): { wordCount: number; bulletCount: number; estimatedPages: number } {
  const { resume } = store.getState();

  let wordCount = 0;
  let bulletCount = 0;

  // Count header words
  wordCount += (resume.header.name || '').split(/\s+/).filter(Boolean).length;

  // Count section content
  for (const section of resume.sections) {
    wordCount += (section.title || '').split(/\s+/).filter(Boolean).length;

    for (const entry of section.entries) {
      wordCount += (entry.organization || '').split(/\s+/).filter(Boolean).length;
      wordCount += (entry.role || '').split(/\s+/).filter(Boolean).length;
      wordCount += (entry.location || '').split(/\s+/).filter(Boolean).length;

      const countBullets = (nodes: ContentNode[]) => {
        for (const node of nodes) {
          bulletCount++;
          wordCount += (node.text || '').split(/\s+/).filter(Boolean).length;
          countBullets(node.children);
        }
      };
      countBullets(entry.content);
    }
  }

  // Rough estimate: ~400-500 words per page, adjusted for formatting
  // More bullets = more space used
  const estimatedPages = Math.max(1, Math.ceil((wordCount + bulletCount * 5) / 450));

  return { wordCount, bulletCount, estimatedPages };
}

function renderPreview(): string {
  const { resume, styleSettings, isPreviewVisible } = store.getState();
  const { typography, spacing, layout, colors } = styleSettings;

  if (!isPreviewVisible) return '';

  const renderPreviewBullets = (nodes: ContentNode[], depth: number = 0): string => {
    return nodes.map(node => {
      const heatMapClass = getHeatMapClass(node.id);
      return `
        <div class="preview-bullet ${heatMapClass}" data-bullet-id="${node.id}" style="margin-left: ${depth * spacing.bulletIndent}px; margin-bottom: ${spacing.bulletSpacing}px;">
          <span class="preview-bullet-symbol">${getBulletSymbol(depth)}</span>
          ${escapeHtml(node.text)}
        </div>
        ${node.children.length > 0 ? renderPreviewBullets(node.children, depth + 1) : ''}
      `;
    }).join('');
  };

  const renderPreviewEntry = (entry: Entry): string => {
    return `
      <div class="preview-entry" data-entry-id="${entry.id}" style="margin-bottom: ${spacing.entryGap}px;">
        <div class="preview-entry-header">
          <div class="preview-entry-left">
            <div class="preview-org" style="font-weight: 600;">${escapeHtml(entry.organization)}</div>
            <div class="preview-role">${escapeHtml(entry.role)}</div>
          </div>
          <div class="preview-entry-right" style="text-align: right;">
            <div class="preview-date">${escapeHtml(entry.dateStart)} &ndash; ${escapeHtml(entry.dateEnd)}</div>
            ${layout.locationPosition === 'with-date'
              ? `<div class="preview-location">${escapeHtml(entry.location)}</div>`
              : ''}
          </div>
        </div>
        ${layout.locationPosition === 'below'
          ? `<div class="preview-location-below">${escapeHtml(entry.location)}</div>`
          : ''}
        <div class="preview-bullets">
          ${renderPreviewBullets(entry.content)}
        </div>
      </div>
    `;
  };

  const renderPreviewSection = (section: Section): string => {
    return `
      <div class="preview-section" style="margin-bottom: ${spacing.sectionGap}px;">
        <div class="preview-section-title" style="font-size: ${typography.baseSize * typography.sectionHeaderScale}pt; font-weight: 600; margin-bottom: 8px; border-bottom: ${layout.sectionDividers === 'line' ? `1px solid ${colors.dividerColor}` : 'none'}; padding-bottom: 4px;">
          ${escapeHtml(section.title)}
        </div>
        ${section.entries.map(entry => renderPreviewEntry(entry)).join('')}
      </div>
    `;
  };

  const stats = getResumeStats();
  const pageWarning = stats.estimatedPages > 1;

  return `
    <div class="preview-pane">
      <div class="preview-header">
        <span class="preview-title">Preview</span>
        <span class="preview-status">&bull; Live</span>
        <div class="preview-stats">
          <span class="stat-item" title="Word count">${stats.wordCount} words</span>
          <span class="stat-item" title="Bullet points">${stats.bulletCount} bullets</span>
          <span class="stat-item ${pageWarning ? 'warning' : ''}" title="${pageWarning ? 'Consider trimming to fit 1 page' : 'Fits on 1 page'}">
            ~${stats.estimatedPages} ${stats.estimatedPages === 1 ? 'page' : 'pages'}
          </span>
        </div>
        <div class="preview-controls">
          <button class="btn-export" title="Export PDF">Export</button>
        </div>
      </div>
      <div class="preview-content" style="font-family: ${typography.primaryFont}; font-size: ${typography.baseSize}pt; line-height: ${typography.lineHeight}; color: ${colors.textColor}; padding: ${spacing.pageMargins}in;">
        <div class="preview-resume-header" style="text-align: center; margin-bottom: ${spacing.sectionGap}px;">
          <div class="preview-name" style="font-size: ${typography.baseSize * typography.nameScale}pt; font-weight: 600;">${escapeHtml(resume.header.name)}</div>
          <div class="preview-contact">
            ${[resume.header.email, resume.header.phone, resume.header.location].filter(Boolean).join(' | ')}
          </div>
          ${resume.header.links.length > 0
            ? `<div class="preview-links" style="color: ${colors.linkColor};">
                 ${resume.header.links.map(l => escapeHtml(l.url)).join(' | ')}
               </div>`
            : ''}
        </div>
        ${resume.sections.map(section => renderPreviewSection(section)).join('')}
      </div>
    </div>
  `;
}

function renderStyleStudio(): string {
  const { isStyleStudioOpen, styleSettings } = store.getState();

  if (!isStyleStudioOpen) return '';

  const { typography, spacing, layout, colors } = styleSettings;

  return `
    <div class="style-studio-overlay">
      <div class="style-studio">
        <div class="style-studio-header">
          <h2>Style Studio</h2>
          <button class="btn-close-studio">&times;</button>
        </div>
        <div class="style-studio-content">
          <div class="style-sidebar">
            <div class="style-section">
              <h3>Presets</h3>
              <div class="preset-buttons">
                <button class="btn-preset" data-preset="classic">Classic</button>
                <button class="btn-preset" data-preset="modern">Modern</button>
                <button class="btn-preset" data-preset="minimal">Minimal</button>
                <button class="btn-preset" data-preset="dense">Dense</button>
              </div>
            </div>
            <div class="style-section">
              <h3>Typography</h3>
              <label>
                Primary Font
                <select data-style="typography.primaryFont">
                  <option value="Inter, system-ui, sans-serif" ${typography.primaryFont.includes('Inter') ? 'selected' : ''}>Inter</option>
                  <option value="Georgia, serif" ${typography.primaryFont.includes('Georgia') ? 'selected' : ''}>Georgia</option>
                  <option value="system-ui, sans-serif" ${typography.primaryFont.includes('system-ui') && !typography.primaryFont.includes('Inter') ? 'selected' : ''}>System</option>
                </select>
              </label>
              <label>
                Base Size (pt)
                <input type="number" value="${typography.baseSize}" min="8" max="14" data-style="typography.baseSize" />
              </label>
              <label>
                Line Height
                <input type="number" value="${typography.lineHeight}" min="1" max="2" step="0.1" data-style="typography.lineHeight" />
              </label>
            </div>
            <div class="style-section">
              <h3>Spacing</h3>
              <label>
                Page Margins (in)
                <input type="number" value="${spacing.pageMargins}" min="0.25" max="1.5" step="0.1" data-style="spacing.pageMargins" />
              </label>
              <label>
                Section Gap (pt)
                <input type="number" value="${spacing.sectionGap}" min="6" max="24" data-style="spacing.sectionGap" />
              </label>
              <label>
                Entry Gap (pt)
                <input type="number" value="${spacing.entryGap}" min="2" max="16" data-style="spacing.entryGap" />
              </label>
            </div>
            <div class="style-section">
              <h3>Layout</h3>
              <label>
                Date Position
                <select data-style="layout.datePosition">
                  <option value="right" ${layout.datePosition === 'right' ? 'selected' : ''}>Right-aligned</option>
                  <option value="inline" ${layout.datePosition === 'inline' ? 'selected' : ''}>Inline</option>
                </select>
              </label>
              <label>
                Section Dividers
                <select data-style="layout.sectionDividers">
                  <option value="none" ${layout.sectionDividers === 'none' ? 'selected' : ''}>None</option>
                  <option value="line" ${layout.sectionDividers === 'line' ? 'selected' : ''}>Line</option>
                  <option value="double" ${layout.sectionDividers === 'double' ? 'selected' : ''}>Double</option>
                </select>
              </label>
            </div>
            <div class="style-section">
              <h3>Colors</h3>
              <label>
                Text Color
                <input type="color" value="${colors.textColor}" data-style="colors.textColor" />
              </label>
              <label>
                Accent Color
                <input type="color" value="${colors.accentColor}" data-style="colors.accentColor" />
              </label>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;
}

// ============================================================================
// VARIANT & ANALYSIS PANELS
// ============================================================================

function renderVariantPanel(): string {
  const wsState = workspaceStore.getState();
  if (!wsState.isVariantPanelOpen) return '';

  const { workspace } = wsState;
  const activeVariant = workspaceStore.getActiveVariant();

  return `
    <div class="panel-overlay variant-panel-overlay">
      <div class="panel variant-panel">
        <div class="panel-header">
          <h2>Resume Variants</h2>
          <button class="btn-close-panel" data-panel="variant">&times;</button>
        </div>
        <div class="panel-content">
          <div class="variant-list">
            ${workspace.variants.map(variant => `
              <div class="variant-item ${variant.id === workspace.activeVariantId ? 'active' : ''}" data-variant-id="${variant.id}">
                <div class="variant-info">
                  <div class="variant-name">${escapeHtml(variant.name)} ${variant.isDefault ? '<span class="badge">Master</span>' : ''}</div>
                  ${variant.targetRole ? `<div class="variant-target">${escapeHtml(variant.targetRole)}${variant.targetCompany ? ` @ ${escapeHtml(variant.targetCompany)}` : ''}</div>` : ''}
                  <div class="variant-meta">${variant.includedEntryIds.length} entries, ${variant.snapshots.length} snapshots</div>
                </div>
                <div class="variant-actions">
                  <button class="btn-icon btn-select-variant" data-variant-id="${variant.id}" title="Select">&#10003;</button>
                  <button class="btn-icon btn-duplicate-variant" data-variant-id="${variant.id}" title="Duplicate">&#9113;</button>
                  ${!variant.isDefault ? `<button class="btn-icon btn-delete-variant" data-variant-id="${variant.id}" title="Delete">&times;</button>` : ''}
                </div>
              </div>
            `).join('')}
          </div>
          <div class="variant-create">
            <h3>Create New Variant</h3>
            <input type="text" id="new-variant-name" placeholder="Variant name (e.g., Tech Lead at FAANG)" />
            <input type="text" id="new-variant-role" placeholder="Target role (optional)" />
            <input type="text" id="new-variant-company" placeholder="Target company (optional)" />
            <button class="btn-primary btn-create-variant">Create Variant</button>
          </div>
          ${activeVariant && !activeVariant.isDefault ? `
            <div class="variant-snapshots">
              <h3>Snapshots for "${escapeHtml(activeVariant.name)}"</h3>
              ${activeVariant.snapshots.length > 0 ? `
                <div class="snapshot-list">
                  ${activeVariant.snapshots.map(snapshot => `
                    <div class="snapshot-item" data-snapshot-id="${snapshot.id}">
                      <div class="snapshot-info">
                        <div class="snapshot-name">${escapeHtml(snapshot.name)}</div>
                        <div class="snapshot-date">${new Date(snapshot.createdAt).toLocaleDateString()}</div>
                      </div>
                      <div class="snapshot-actions">
                        <button class="btn-sm btn-restore-snapshot" data-snapshot-id="${snapshot.id}">Restore</button>
                        <button class="btn-sm btn-delete-snapshot" data-snapshot-id="${snapshot.id}">&times;</button>
                      </div>
                    </div>
                  `).join('')}
                </div>
              ` : '<p class="empty-state">No snapshots yet</p>'}
              <div class="snapshot-create">
                <input type="text" id="new-snapshot-name" placeholder="Snapshot name" />
                <button class="btn-secondary btn-create-snapshot">Save Snapshot</button>
              </div>
            </div>
          ` : ''}
        </div>
      </div>
    </div>
  `;
}

function renderJobPanel(): string {
  const wsState = workspaceStore.getState();
  if (!wsState.isJobPanelOpen) return '';

  const { workspace, activeJobDescriptionId } = wsState;
  const activeJob = workspace.jobDescriptions.find(j => j.id === activeJobDescriptionId);

  return `
    <div class="panel-overlay job-panel-overlay">
      <div class="panel job-panel">
        <div class="panel-header">
          <h2>Job Descriptions</h2>
          <button class="btn-close-panel" data-panel="job">&times;</button>
        </div>
        <div class="panel-content">
          <div class="job-list">
            ${workspace.jobDescriptions.length > 0 ? workspace.jobDescriptions.map(job => `
              <div class="job-item ${job.id === activeJobDescriptionId ? 'active' : ''}" data-job-id="${job.id}">
                <div class="job-info">
                  <div class="job-title">${escapeHtml(job.title)}</div>
                  <div class="job-company">${escapeHtml(job.company)}</div>
                  <div class="job-keywords">${job.keywords.length} keywords</div>
                </div>
                <div class="job-actions">
                  <button class="btn-icon btn-select-job" data-job-id="${job.id}" title="Select">&#10003;</button>
                  <button class="btn-icon btn-analyze-job" data-job-id="${job.id}" title="Analyze">&#9783;</button>
                  <button class="btn-icon btn-start-fit-coach" data-job-id="${job.id}" title="Start Fit Coach">&#127919;</button>
                  <button class="btn-icon btn-delete-job" data-job-id="${job.id}" title="Delete">&times;</button>
                </div>
              </div>
            `).join('') : '<p class="empty-state">No job descriptions yet</p>'}
          </div>
          <div class="job-editor">
            <h3>${activeJob ? 'Edit Job Description' : 'Add Job Description'}</h3>
            <input type="text" id="job-title" placeholder="Job Title" value="${activeJob ? escapeHtml(activeJob.title) : ''}" />
            <input type="text" id="job-company" placeholder="Company" value="${activeJob ? escapeHtml(activeJob.company) : ''}" />
            <textarea id="job-description" placeholder="Paste job description here..." rows="8">${activeJob ? escapeHtml(activeJob.description) : ''}</textarea>
            <input type="text" id="job-keywords" placeholder="Keywords (comma separated)" value="${activeJob ? escapeHtml(activeJob.keywords.join(', ')) : ''}" />
            <div class="job-editor-actions">
              ${activeJob ? `
                <button class="btn-secondary btn-update-job">Update</button>
                <button class="btn-primary btn-new-job">New Job</button>
              ` : `
                <button class="btn-primary btn-add-job">Add Job</button>
              `}
            </div>
          </div>
        </div>
      </div>
    </div>
  `;
}

function renderAnalysisPanel(): string {
  const wsState = workspaceStore.getState();
  if (!wsState.isAnalysisPanelOpen) return '';

  const analysis = workspaceStore.getActiveAnalysis();
  const { workspace } = wsState;

  if (!analysis) {
    return `
      <div class="panel-overlay analysis-panel-overlay">
        <div class="panel analysis-panel">
          <div class="panel-header">
            <h2>Resume Analysis</h2>
            <button class="btn-close-panel" data-panel="analysis">&times;</button>
          </div>
          <div class="panel-content">
            <p class="empty-state">No analysis yet. Select a job description and click "Analyze" to see how your resume matches.</p>
            ${workspace.analyses.length > 0 ? `
              <div class="analysis-history">
                <h3>Previous Analyses</h3>
                ${workspace.analyses.slice(-5).reverse().map(a => {
                  const job = workspace.jobDescriptions.find(j => j.id === a.jobDescriptionId);
                  const variant = workspace.variants.find(v => v.id === a.variantId);
                  return `
                    <div class="analysis-history-item" data-analysis-id="${a.id}">
                      <div class="analysis-history-info">
                        <span class="analysis-score score-${getScoreClass(a.overallScore)}">${a.overallScore}%</span>
                        <span class="analysis-job">${job ? escapeHtml(job.title) : 'Unknown'}</span>
                        <span class="analysis-variant">${variant ? escapeHtml(variant.name) : 'Unknown'}</span>
                      </div>
                      <button class="btn-sm btn-view-analysis" data-analysis-id="${a.id}">View</button>
                    </div>
                  `;
                }).join('')}
              </div>
            ` : ''}
          </div>
        </div>
      </div>
    `;
  }

  const job = workspace.jobDescriptions.find(j => j.id === analysis.jobDescriptionId);
  const variant = workspace.variants.find(v => v.id === analysis.variantId);

  return `
    <div class="panel-overlay analysis-panel-overlay">
      <div class="panel analysis-panel analysis-panel-full">
        <div class="panel-header">
          <h2>Resume Analysis</h2>
          <button class="btn-close-panel" data-panel="analysis">&times;</button>
        </div>
        <div class="panel-content">
          <div class="analysis-header">
            <div class="analysis-score-large score-${getScoreClass(analysis.overallScore)}">
              <span class="score-number">${analysis.overallScore}</span>
              <span class="score-label">Match Score</span>
            </div>
            <div class="analysis-meta">
              <div><strong>Job:</strong> ${job ? escapeHtml(job.title) + ' @ ' + escapeHtml(job.company) : 'Unknown'}</div>
              <div><strong>Variant:</strong> ${variant ? escapeHtml(variant.name) : 'Unknown'}</div>
              <div><strong>Analyzed:</strong> ${new Date(analysis.createdAt).toLocaleString()}</div>
            </div>
          </div>

          ${analysis.strongPoints.length > 0 ? `
            <div class="analysis-section">
              <h3>Strong Points</h3>
              <ul class="strong-points-list">
                ${analysis.strongPoints.map(p => `<li class="strong-point">${escapeHtml(p)}</li>`).join('')}
              </ul>
            </div>
          ` : ''}

          ${analysis.missingSkills.length > 0 ? `
            <div class="analysis-section">
              <h3>Missing Skills</h3>
              <div class="missing-skills">
                ${analysis.missingSkills.map(s => `<span class="skill-tag missing">${escapeHtml(s)}</span>`).join('')}
              </div>
            </div>
          ` : ''}

          <div class="analysis-section">
            <h3>Keyword Matches</h3>
            <div class="keyword-matches">
              ${analysis.keywordMatches.map(k => `
                <span class="keyword-tag ${k.found ? 'found' : 'missing'} importance-${k.importance}" title="${k.importance} priority">
                  ${escapeHtml(k.keyword)}
                  ${k.found ? '&#10003;' : '&#10007;'}
                </span>
              `).join('')}
            </div>
          </div>

          ${analysis.suggestions.length > 0 ? `
            <div class="analysis-section">
              <h3>Suggestions</h3>
              <div class="suggestions-list">
                ${analysis.suggestions.map(s => `
                  <div class="suggestion-item priority-${s.priority} ${s.applied ? 'applied' : ''}">
                    <div class="suggestion-type">${s.type.toUpperCase()}</div>
                    <div class="suggestion-reason">${escapeHtml(s.reason)}</div>
                    ${s.suggestedText ? `<div class="suggestion-text">"${escapeHtml(s.suggestedText)}"</div>` : ''}
                    ${!s.applied ? `<button class="btn-sm btn-apply-suggestion" data-analysis-id="${analysis.id}" data-suggestion-id="${s.id}">Mark Done</button>` : '<span class="applied-badge">Applied</span>'}
                  </div>
                `).join('')}
              </div>
            </div>
          ` : ''}
        </div>
      </div>
    </div>
  `;
}

function getScoreClass(score: number): string {
  if (score >= 80) return 'excellent';
  if (score >= 60) return 'good';
  if (score >= 40) return 'fair';
  return 'poor';
}

// Auto-save indicator state
let saveIndicatorTimeout: ReturnType<typeof setTimeout> | null = null;

function showSaveIndicator(status: 'saving' | 'saved'): void {
  const indicator = document.querySelector('.save-indicator');
  if (!indicator) return;

  if (saveIndicatorTimeout) {
    clearTimeout(saveIndicatorTimeout);
  }

  indicator.textContent = status === 'saving' ? 'Saving...' : 'Saved';
  indicator.classList.add('visible');

  if (status === 'saved') {
    saveIndicatorTimeout = setTimeout(() => {
      indicator.classList.remove('visible');
    }, 2000);
  }
}

function renderToolbar(): string {
  const { focusMode, isPreviewVisible } = store.getState();
  const wsState = workspaceStore.getState();
  const { workspace, isVariantPanelOpen, isJobPanelOpen, isAnalysisPanelOpen } = wsState;

  return `
    <div class="toolbar">
      <div class="toolbar-left">
        <span class="app-title">resumeyay</span>
        <span class="save-indicator">Saved</span>
        <div class="toolbar-separator"></div>
        <div class="variant-switcher">
          <select id="variant-select" title="Active Variant">
            ${workspace.variants.map(v => `
              <option value="${v.id}" ${v.id === workspace.activeVariantId ? 'selected' : ''}>
                ${escapeHtml(v.name)}${v.isDefault ? ' (Master)' : ''}
              </option>
            `).join('')}
          </select>
          <button class="btn-icon btn-variants ${isVariantPanelOpen ? 'active' : ''}" id="btn-variants" title="Manage Variants">&#9776;</button>
        </div>
      </div>
      <div class="toolbar-center">
        <div class="focus-modes">
          <button class="btn-mode ${focusMode === 'full-matrix' ? 'active' : ''}"
                  data-mode="full-matrix" title="Full Matrix (Cmd+1)">
            Full
          </button>
          <button class="btn-mode ${focusMode === 'narrative' ? 'active' : ''}"
                  data-mode="narrative" title="Narrative Focus (Cmd+2)">
            Narrative
          </button>
          <button class="btn-mode ${focusMode === 'timeline' ? 'active' : ''}"
                  data-mode="timeline" title="Timeline Focus (Cmd+3)">
            Timeline
          </button>
          <button class="btn-mode ${focusMode === 'compact' ? 'active' : ''}"
                  data-mode="compact" title="Compact Review (Cmd+4)">
            Compact
          </button>
        </div>
      </div>
      <div class="toolbar-right">
        <button class="btn-toolbar ${isJobPanelOpen ? 'active' : ''}" id="btn-jobs" title="Job Descriptions">
          Jobs
        </button>
        <button class="btn-toolbar ${isAnalysisPanelOpen ? 'active' : ''}" id="btn-analysis" title="Resume Analysis">
          Analyze
        </button>
        <button class="btn-toolbar ${fitCoachStore.getState().isCoachPanelOpen ? 'active' : ''}" id="btn-fit-coach" title="Fit Coach">
          Fit Coach
        </button>
        <div class="toolbar-separator"></div>
        <button class="btn-toolbar ${isPreviewVisible ? 'active' : ''}"
                id="btn-toggle-preview" title="Toggle Preview (Cmd+\\)">
          Preview
        </button>
        <button class="btn-toolbar" id="btn-style-studio" title="Style Studio (Cmd+Shift+S)">
          Style
        </button>
        <div class="toolbar-separator"></div>
        <button class="btn-toolbar" id="btn-import" title="Import JSON">Import</button>
        <button class="btn-toolbar" id="btn-export-json" title="Export JSON">Export</button>
        <div class="toolbar-separator"></div>
        <button class="btn-toolbar" id="btn-new">New</button>
        <button class="btn-toolbar" id="btn-sample">Sample</button>
      </div>
    </div>
  `;
}

// Track if event delegation is set up
let eventDelegationSetup = false;

function render(force: boolean = false): void {
  // Skip render if user is actively typing (unless forced)
  if (!force && shouldSkipRender()) {
    return;
  }

  const { isPreviewVisible, focusMode } = store.getState();

  const app = document.querySelector<HTMLDivElement>('#app')!;
  app.innerHTML = `
    <div class="app-container">
      ${renderToolbar()}
      ${renderFloatingHeader()}
      <div class="main-content ${focusMode} ${isPreviewVisible ? 'with-preview' : 'no-preview'}">
        <div class="editor-pane">
          ${renderEditor()}
        </div>
        ${renderPreview()}
      </div>
      ${renderStyleStudio()}
      ${renderVariantPanel()}
      ${renderJobPanel()}
      ${renderAnalysisPanel()}
      ${renderFitCoachPanel()}
    </div>
  `;

  // Set up event delegation once
  if (!eventDelegationSetup) {
    setupEventDelegation();
    eventDelegationSetup = true;
  }

  // Restore focus if needed
  restoreFocus();
}

// ============================================================================
// EVENT DELEGATION (Single listeners on app container)
// ============================================================================

function setupEventDelegation(): void {
  const app = document.querySelector<HTMLDivElement>('#app')!;

  // Handle all clicks via delegation
  app.addEventListener('click', (e) => {
    const target = e.target as HTMLElement;

    // Focus mode buttons
    const modeBtn = target.closest('.btn-mode') as HTMLElement | null;
    if (modeBtn) {
      const mode = modeBtn.dataset.mode as FocusMode;
      store.setFocusMode(mode);
      return;
    }

    // Column header clicks (toggle collapse)
    const columnHeader = target.closest('.column-header') as HTMLElement | null;
    if (columnHeader) {
      const column = columnHeader.dataset.column as keyof ColumnConfig;
      store.toggleColumn(column);
      return;
    }

    // Entry row clicks (set active) - but not when clicking inputs
    if (!target.matches('input, button')) {
      const entryRow = target.closest('.entry-row') as HTMLElement | null;
      if (entryRow) {
        const entryId = entryRow.dataset.entryId!;
        store.setActiveEntry(entryId);
        return;
      }
    }

    // Add bullet buttons
    const addBulletBtn = target.closest('.btn-add-bullet') as HTMLElement | null;
    if (addBulletBtn) {
      const entryId = addBulletBtn.dataset.entryId!;
      const newId = store.addBullet(entryId, null);
      setTimeout(() => {
        const newInput = document.querySelector(`.bullet-input[data-bullet-id="${newId}"]`) as HTMLInputElement;
        if (newInput) newInput.focus();
      }, 50);
      return;
    }

    // Add entry buttons - toggle dropdown
    const addEntryBtn = target.closest('.btn-add-entry') as HTMLElement | null;
    if (addEntryBtn) {
      const dropdown = addEntryBtn.nextElementSibling as HTMLElement;
      if (dropdown?.classList.contains('template-dropdown')) {
        // Close other dropdowns
        document.querySelectorAll('.template-dropdown.visible').forEach(d => {
          if (d !== dropdown) d.classList.remove('visible');
        });
        dropdown.classList.toggle('visible');
      }
      return;
    }

    // Template option selection
    const templateOption = target.closest('.template-option') as HTMLElement | null;
    if (templateOption) {
      const dropdown = templateOption.closest('.template-dropdown') as HTMLElement;
      const sectionId = dropdown?.dataset.sectionId!;
      const template = templateOption.dataset.template as EntryTemplate;

      if (sectionId && template) {
        const newId = store.addTemplatedEntry(sectionId, template);
        store.setActiveEntry(newId);

        // Focus the first input of the new entry
        setTimeout(() => {
          const newRow = document.querySelector(`.entry-row[data-entry-id="${newId}"]`);
          const firstInput = newRow?.querySelector('input') as HTMLInputElement;
          if (firstInput) firstInput.focus();
        }, 50);
      }

      dropdown?.classList.remove('visible');
      return;
    }

    // Close dropdowns when clicking elsewhere
    if (!target.closest('.add-entry-dropdown')) {
      document.querySelectorAll('.template-dropdown.visible').forEach(d => {
        d.classList.remove('visible');
      });
    }

    // Add section button
    if (target.closest('.btn-add-section')) {
      store.addSection('experience', 'New Section');
      return;
    }

    // Toggle preview
    if (target.closest('#btn-toggle-preview')) {
      store.togglePreview();
      return;
    }

    // Style studio
    if (target.closest('#btn-style-studio')) {
      store.toggleStyleStudio();
      return;
    }

    if (target.closest('.btn-close-studio')) {
      store.toggleStyleStudio();
      return;
    }

    // Style presets
    const presetBtn = target.closest('.btn-preset') as HTMLElement | null;
    if (presetBtn) {
      const preset = presetBtn.dataset.preset as 'classic' | 'modern' | 'minimal' | 'dense';
      store.applyStylePreset(preset);
      return;
    }

    // New resume
    if (target.closest('#btn-new')) {
      if (confirm('Create a new blank resume? Your current data will be preserved in undo history.')) {
        store.newResume();
      }
      return;
    }

    // Load sample
    if (target.closest('#btn-sample')) {
      if (confirm('Load sample resume data? Your current data will be preserved in undo history.')) {
        store.resetToSample();
      }
      return;
    }

    // Export PDF button
    if (target.closest('.btn-export')) {
      const previewContent = document.querySelector('.preview-content') as HTMLElement | null;
      if (!previewContent) return;

      import('html2pdf.js').then(({ default: html2pdf }) => {
        const options = {
          margin: 0,
          filename: 'resume.pdf',
          image: { type: 'jpeg' as const, quality: 0.98 },
          html2canvas: { scale: 2, useCORS: true },
          jsPDF: { unit: 'in' as const, format: 'letter' as const, orientation: 'portrait' as const }
        };
        html2pdf().set(options).from(previewContent).save();
      }).catch((error) => {
        console.error('Export failed:', error);
        alert('Export failed. Please try again.');
      });
      return;
    }

    // Export JSON button
    if (target.closest('#btn-export-json')) {
      const json = store.exportJSON();
      const blob = new Blob([json], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `resume-${new Date().toISOString().slice(0, 10)}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      return;
    }

    // Import JSON button
    if (target.closest('#btn-import')) {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = '.json,application/json';
      input.onchange = (e) => {
        const file = (e.target as HTMLInputElement).files?.[0];
        if (file) {
          const reader = new FileReader();
          reader.onload = (e) => {
            const json = e.target?.result as string;
            if (store.importJSON(json)) {
              alert('Resume imported successfully!');
            } else {
              alert('Import failed. Please check the file format.');
            }
          };
          reader.readAsText(file);
        }
      };
      input.click();
      return;
    }

    // ============================================================================
    // VARIANT PANEL HANDLERS
    // ============================================================================

    // Open variants panel
    if (target.closest('#btn-variants')) {
      workspaceStore.toggleVariantPanel();
      return;
    }

    // Open jobs panel
    if (target.closest('#btn-jobs')) {
      workspaceStore.toggleJobPanel();
      return;
    }

    // Open analysis panel
    if (target.closest('#btn-analysis')) {
      workspaceStore.toggleAnalysisPanel();
      return;
    }

    // Close panels
    const closeBtn = target.closest('.btn-close-panel') as HTMLElement | null;
    if (closeBtn) {
      const panel = closeBtn.dataset.panel;
      if (panel === 'variant') workspaceStore.toggleVariantPanel();
      else if (panel === 'job') workspaceStore.toggleJobPanel();
      else if (panel === 'analysis') workspaceStore.toggleAnalysisPanel();
      return;
    }

    // Select variant
    const selectVariantBtn = target.closest('.btn-select-variant') as HTMLElement | null;
    if (selectVariantBtn) {
      const variantId = selectVariantBtn.dataset.variantId!;
      workspaceStore.setActiveVariant(variantId);
      return;
    }

    // Duplicate variant
    const duplicateVariantBtn = target.closest('.btn-duplicate-variant') as HTMLElement | null;
    if (duplicateVariantBtn) {
      const variantId = duplicateVariantBtn.dataset.variantId!;
      workspaceStore.duplicateVariant(variantId);
      return;
    }

    // Delete variant
    const deleteVariantBtn = target.closest('.btn-delete-variant') as HTMLElement | null;
    if (deleteVariantBtn) {
      const variantId = deleteVariantBtn.dataset.variantId!;
      if (confirm('Delete this variant?')) {
        workspaceStore.deleteVariant(variantId);
      }
      return;
    }

    // Create variant
    if (target.closest('.btn-create-variant')) {
      const name = (document.getElementById('new-variant-name') as HTMLInputElement)?.value.trim();
      const role = (document.getElementById('new-variant-role') as HTMLInputElement)?.value.trim();
      const company = (document.getElementById('new-variant-company') as HTMLInputElement)?.value.trim();
      if (name) {
        workspaceStore.createVariant(name, role || undefined, company || undefined);
      }
      return;
    }

    // Create snapshot
    if (target.closest('.btn-create-snapshot')) {
      const name = (document.getElementById('new-snapshot-name') as HTMLInputElement)?.value.trim();
      const activeVariant = workspaceStore.getActiveVariant();
      if (name && activeVariant) {
        workspaceStore.createSnapshot(activeVariant.id, name);
      }
      return;
    }

    // Restore snapshot
    const restoreSnapshotBtn = target.closest('.btn-restore-snapshot') as HTMLElement | null;
    if (restoreSnapshotBtn) {
      const snapshotId = restoreSnapshotBtn.dataset.snapshotId!;
      const activeVariant = workspaceStore.getActiveVariant();
      if (activeVariant && confirm('Restore this snapshot? Current selection will be replaced.')) {
        workspaceStore.restoreSnapshot(activeVariant.id, snapshotId);
      }
      return;
    }

    // Delete snapshot
    const deleteSnapshotBtn = target.closest('.btn-delete-snapshot') as HTMLElement | null;
    if (deleteSnapshotBtn) {
      const snapshotId = deleteSnapshotBtn.dataset.snapshotId!;
      const activeVariant = workspaceStore.getActiveVariant();
      if (activeVariant && confirm('Delete this snapshot?')) {
        workspaceStore.deleteSnapshot(activeVariant.id, snapshotId);
      }
      return;
    }

    // ============================================================================
    // JOB PANEL HANDLERS
    // ============================================================================

    // Select job
    const selectJobBtn = target.closest('.btn-select-job') as HTMLElement | null;
    if (selectJobBtn) {
      const jobId = selectJobBtn.dataset.jobId!;
      workspaceStore.setActiveJobDescription(jobId);
      return;
    }

    // Delete job
    const deleteJobBtn = target.closest('.btn-delete-job') as HTMLElement | null;
    if (deleteJobBtn) {
      const jobId = deleteJobBtn.dataset.jobId!;
      if (confirm('Delete this job description?')) {
        workspaceStore.deleteJobDescription(jobId);
      }
      return;
    }

    // Add job
    if (target.closest('.btn-add-job')) {
      const title = (document.getElementById('job-title') as HTMLInputElement)?.value.trim();
      const company = (document.getElementById('job-company') as HTMLInputElement)?.value.trim();
      const description = (document.getElementById('job-description') as HTMLTextAreaElement)?.value.trim();
      const keywordsStr = (document.getElementById('job-keywords') as HTMLInputElement)?.value.trim();
      const keywords = keywordsStr ? keywordsStr.split(',').map(k => k.trim()).filter(Boolean) : workspaceStore.extractKeywords(description);

      if (title && company) {
        workspaceStore.addJobDescription({
          title,
          company,
          description,
          requirements: [],
          keywords,
        });
      }
      return;
    }

    // Update job
    if (target.closest('.btn-update-job')) {
      const wsState = workspaceStore.getState();
      const jobId = wsState.activeJobDescriptionId;
      if (jobId) {
        const title = (document.getElementById('job-title') as HTMLInputElement)?.value.trim();
        const company = (document.getElementById('job-company') as HTMLInputElement)?.value.trim();
        const description = (document.getElementById('job-description') as HTMLTextAreaElement)?.value.trim();
        const keywordsStr = (document.getElementById('job-keywords') as HTMLInputElement)?.value.trim();
        const keywords = keywordsStr ? keywordsStr.split(',').map(k => k.trim()).filter(Boolean) : [];

        workspaceStore.updateJobDescription(jobId, { title, company, description, keywords });
      }
      return;
    }

    // New job (clear form)
    if (target.closest('.btn-new-job')) {
      workspaceStore.setActiveJobDescription(null);
      return;
    }

    // Analyze job
    const analyzeJobBtn = target.closest('.btn-analyze-job') as HTMLElement | null;
    if (analyzeJobBtn) {
      const jobId = analyzeJobBtn.dataset.jobId!;
      const activeVariant = workspaceStore.getActiveVariant();
      if (activeVariant) {
        workspaceStore.analyzeResumeVsJob(activeVariant.id, jobId).then(() => {
          workspaceStore.toggleJobPanel();
          workspaceStore.toggleAnalysisPanel();
        });
      }
      return;
    }

    // ============================================================================
    // ANALYSIS PANEL HANDLERS
    // ============================================================================

    // View analysis
    const viewAnalysisBtn = target.closest('.btn-view-analysis') as HTMLElement | null;
    if (viewAnalysisBtn) {
      const analysisId = viewAnalysisBtn.dataset.analysisId!;
      workspaceStore.setActiveAnalysis(analysisId);
      return;
    }

    // Apply suggestion
    const applySuggestionBtn = target.closest('.btn-apply-suggestion') as HTMLElement | null;
    if (applySuggestionBtn) {
      const analysisId = applySuggestionBtn.dataset.analysisId!;
      const suggestionId = applySuggestionBtn.dataset.suggestionId!;
      workspaceStore.applySuggestion(analysisId, suggestionId);
      return;
    }

    // ============================================================================
    // FIT COACH PANEL HANDLERS
    // ============================================================================

    // Open Fit Coach panel
    if (target.closest('#btn-fit-coach')) {
      fitCoachStore.toggleCoachPanel();
      return;
    }

    // Close Fit Coach panel
    const closeFitCoachBtn = target.closest('.btn-close-panel[data-panel="fit-coach"]');
    if (closeFitCoachBtn) {
      fitCoachStore.closeCoachPanel();
      return;
    }

    // Save Claude API key
    if (target.closest('.btn-save-api-key')) {
      const input = document.getElementById('claude-api-key') as HTMLInputElement;
      if (input && input.value && input.value !== '••••••••••••') {
        fitCoachStore.setApiKey(input.value);
        alert('API key saved!');
      }
      return;
    }

    // Select requirement in coverage grid
    const requirementItem = target.closest('.requirement-item') as HTMLElement | null;
    if (requirementItem && !target.closest('button')) {
      const reqId = requirementItem.dataset.requirementId!;
      fitCoachStore.selectRequirement(reqId);
      return;
    }

    // Focus on requirement
    const focusReqBtn = target.closest('.btn-focus-req') as HTMLElement | null;
    if (focusReqBtn) {
      const reqId = focusReqBtn.dataset.requirementId!;
      fitCoachStore.selectRequirement(reqId);
      // Scroll to conversation and start coaching about this requirement
      const conversationEl = document.querySelector('.coach-conversation');
      if (conversationEl) {
        conversationEl.scrollIntoView({ behavior: 'smooth' });
      }
      return;
    }

    // Mark requirement as "Not me"
    const notMeBtn = target.closest('.btn-not-me') as HTMLElement | null;
    if (notMeBtn) {
      const reqId = notMeBtn.dataset.requirementId!;
      const reason = prompt('Optional: Why is this not applicable to you?');
      fitCoachStore.markNotMe(reqId, reason || undefined);
      return;
    }

    // Undo "Not me"
    const undoNotMeBtn = target.closest('.btn-undo-not-me') as HTMLElement | null;
    if (undoNotMeBtn) {
      const reqId = undoNotMeBtn.dataset.requirementId!;
      fitCoachStore.updateRequirementStatus(reqId, 'missing');
      return;
    }

    // Send message to coach
    if (target.closest('.btn-send-message')) {
      const input = document.getElementById('coach-message-input') as HTMLTextAreaElement;
      if (input && input.value.trim()) {
        const activeVariant = workspaceStore.getActiveVariant();
        const wsState = workspaceStore.getState();
        if (activeVariant) {
          fitCoachStore.sendMessage(input.value.trim(), wsState.workspace.contentPool, activeVariant);
          input.value = '';
        }
      }
      return;
    }

    // Refresh coverage
    if (target.closest('.btn-refresh-coverage')) {
      const activeVariant = workspaceStore.getActiveVariant();
      const wsState = workspaceStore.getState();
      if (activeVariant) {
        fitCoachStore.refreshCoverage(wsState.workspace.contentPool, activeVariant);
      }
      return;
    }

    // End session
    if (target.closest('.btn-end-session')) {
      if (confirm('End this Fit Coach session?')) {
        fitCoachStore.endSession();
      }
      return;
    }

    // Start Fit Coach from job panel
    const startFitCoachBtn = target.closest('.btn-start-fit-coach') as HTMLElement | null;
    if (startFitCoachBtn) {
      const jobId = startFitCoachBtn.dataset.jobId!;
      const job = workspaceStore.getState().workspace.jobDescriptions.find(j => j.id === jobId);
      const activeVariant = workspaceStore.getActiveVariant();
      const wsState = workspaceStore.getState();

      if (job && activeVariant) {
        workspaceStore.toggleJobPanel();
        fitCoachStore.startFitSession(job, wsState.workspace.contentPool, activeVariant);
      }
      return;
    }
  });

  // Handle all input events via delegation with debouncing
  app.addEventListener('input', (e) => {
    const target = e.target as HTMLInputElement;
    if (!target.matches('input')) return;

    // Header field inputs
    const headerEditor = target.closest('.header-editor');
    if (headerEditor) {
      const field = target.dataset.field;
      const value = target.value;

      // Track active input for preservation
      activeInputInfo = {
        type: 'header',
        field: field,
        cursorPos: target.selectionStart ?? undefined,
      };

      // Start batch for undo grouping
      startUndoBatch();

      // Debounce the store update
      debounce(`header.${field}`, () => {
        if (field === 'header.name') store.updateHeader({ name: value });
        else if (field === 'header.email') store.updateHeader({ email: value });
        else if (field === 'header.phone') store.updateHeader({ phone: value });
        else if (field === 'header.location') store.updateHeader({ location: value });
      }, 150);
      return;
    }

    // Entry field inputs
    const entryRow = target.closest('.entry-row') as HTMLElement | null;
    if (entryRow && target.dataset.field) {
      const field = target.dataset.field;
      const entryId = entryRow.dataset.entryId!;
      const sectionId = entryRow.dataset.sectionId!;
      const value = target.value;

      // Track active input for preservation
      activeInputInfo = {
        type: 'entry',
        field: field,
        entryId: entryId,
        sectionId: sectionId,
        cursorPos: target.selectionStart ?? undefined,
      };

      // Start batch for undo grouping
      startUndoBatch();

      // Debounce the store update
      debounce(`entry.${entryId}.${field}`, () => {
        if (field && entryId && sectionId) {
          store.updateEntry(sectionId, entryId, { [field]: value } as Partial<Entry>);
        }
      }, 150);
      return;
    }

    // Bullet inputs
    if (target.classList.contains('bullet-input')) {
      const bulletId = target.dataset.bulletId!;
      const entryId = target.dataset.entryId!;
      const value = target.value;

      // Track active input for preservation
      activeInputInfo = {
        type: 'bullet',
        bulletId: bulletId,
        entryId: entryId,
        cursorPos: target.selectionStart ?? undefined,
      };

      // Start batch for undo grouping
      startUndoBatch();

      // Debounce the store update
      debounce(`bullet.${bulletId}`, () => {
        store.updateBullet(entryId, bulletId, value);
      }, 150);
      return;
    }
  });

  // Handle focus events for bullet inputs
  app.addEventListener('focus', (e) => {
    const target = e.target as HTMLInputElement;
    if (target.classList.contains('bullet-input')) {
      const bulletId = target.dataset.bulletId!;
      const entryId = target.dataset.entryId!;
      store.setActiveBullet(bulletId);
      store.setActiveEntry(entryId);
    }
  }, true);

  // Handle blur events to clear active input tracking
  app.addEventListener('blur', (e) => {
    const target = e.target as HTMLElement;
    if (target.matches('input')) {
      // Clear active input after a short delay (allow debounced updates to complete)
      setTimeout(() => {
        if (document.activeElement !== target) {
          activeInputInfo = null;
        }
      }, 200);
    }
  }, true);

  // Handle style control and other select changes via delegation
  app.addEventListener('change', (e) => {
    const target = e.target as HTMLInputElement | HTMLSelectElement;

    // Variant select dropdown
    if (target.id === 'variant-select') {
      workspaceStore.setActiveVariant(target.value);
      return;
    }

    // Heat map toggle
    if (target.id === 'show-heatmap') {
      fitCoachStore.toggleHeatMap();
      return;
    }

    // Style controls
    if (!target.dataset.style) return;

    const path = target.dataset.style;
    const [category, field] = path.split('.') as [keyof StyleSettings, string];
    const value = target.value;
    const state = store.getState();

    const updates: Partial<StyleSettings> = {};
    if (category === 'typography') {
      updates.typography = {
        ...state.styleSettings.typography,
        [field]: field === 'baseSize' || field === 'lineHeight' || field === 'nameScale' || field === 'sectionHeaderScale'
          ? parseFloat(value)
          : value,
      };
    } else if (category === 'spacing') {
      updates.spacing = {
        ...state.styleSettings.spacing,
        [field]: parseFloat(value),
      };
    } else if (category === 'layout') {
      updates.layout = {
        ...state.styleSettings.layout,
        [field]: value,
      };
    } else if (category === 'colors') {
      updates.colors = {
        ...state.styleSettings.colors,
        [field]: value,
      };
    }

    store.updateStyleSettings(updates);
  });

  // Preview-Editor Sync Highlighting
  // When hovering over an entry row, highlight the corresponding preview entry
  app.addEventListener('mouseenter', (e) => {
    const target = e.target as HTMLElement;

    // Check if we're entering an entry row
    const entryRow = target.closest('.entry-row') as HTMLElement | null;
    if (entryRow) {
      const entryId = entryRow.dataset.entryId;
      if (entryId) {
        // Highlight the corresponding preview entry
        const previewEntry = document.querySelector(`.preview-entry[data-entry-id="${entryId}"]`);
        if (previewEntry) {
          previewEntry.classList.add('sync-highlight');
        }
      }
    }

    // Check if we're entering a preview entry
    const previewEntry = target.closest('.preview-entry') as HTMLElement | null;
    if (previewEntry) {
      const entryId = previewEntry.dataset.entryId;
      if (entryId) {
        // Highlight the corresponding entry row
        const entryRowToHighlight = document.querySelector(`.entry-row[data-entry-id="${entryId}"]`);
        if (entryRowToHighlight) {
          entryRowToHighlight.classList.add('sync-highlight');
        }
      }
    }
  }, true);

  app.addEventListener('mouseleave', (e) => {
    const target = e.target as HTMLElement;

    // Check if we're leaving an entry row
    const entryRow = target.closest('.entry-row') as HTMLElement | null;
    if (entryRow) {
      const entryId = entryRow.dataset.entryId;
      if (entryId) {
        const previewEntry = document.querySelector(`.preview-entry[data-entry-id="${entryId}"]`);
        if (previewEntry) {
          previewEntry.classList.remove('sync-highlight');
        }
      }
    }

    // Check if we're leaving a preview entry
    const previewEntry = target.closest('.preview-entry') as HTMLElement | null;
    if (previewEntry) {
      const entryId = previewEntry.dataset.entryId;
      if (entryId) {
        const entryRowToRemove = document.querySelector(`.entry-row[data-entry-id="${entryId}"]`);
        if (entryRowToRemove) {
          entryRowToRemove.classList.remove('sync-highlight');
        }
      }
    }
  }, true);
}

// ============================================================================
// INITIALIZATION
// ============================================================================

function init(): void {
  // Subscribe to store changes - skip render when typing (handled by shouldSkipRender)
  store.subscribe(() => {
    // Sync content pool changes to workspace
    workspaceStore.syncContentPool(store.getState().resume);
    render();
  });

  // Subscribe to workspace store changes
  workspaceStore.subscribe(() => {
    render();
  });

  // Subscribe to fit coach store changes
  fitCoachStore.subscribe(() => {
    render();
  });

  // Subscribe to save events for the save indicator
  store.onSave(() => {
    showSaveIndicator('saved');
  });

  workspaceStore.onSave(() => {
    showSaveIndicator('saved');
  });

  // Setup keyboard shortcuts
  setupKeyboardShortcuts();

  // Initial render (forced to ensure it happens)
  render(true);
}

// Start the app
init();
