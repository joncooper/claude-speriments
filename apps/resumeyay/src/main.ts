import { store } from './store';
import type { Entry, Section, ContentNode, FocusMode, ColumnConfig, StyleSettings } from './types';
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

function setupKeyboardShortcuts(): void {
  document.addEventListener('keydown', (e) => {
    const state = store.getState();

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

    // Handle bullet-specific shortcuts
    const activeBulletId = state.activeBulletId;
    const activeEntryId = state.activeEntryId;
    if (activeBulletId && activeEntryId) {
      const bulletInput = document.querySelector(`[data-bullet-id="${activeBulletId}"] input`) as HTMLInputElement;
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
              const newInput = document.querySelector(`[data-bullet-id="${newId}"] input`) as HTMLInputElement;
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
              const prevInput = document.querySelector(`[data-bullet-id="${prevId}"] input`) as HTMLInputElement;
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
          <button class="btn-add-entry" data-section-id="${section.id}">+ Add Entry</button>
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

function renderPreview(): string {
  const { resume, styleSettings, isPreviewVisible } = store.getState();
  const { typography, spacing, layout, colors } = styleSettings;

  if (!isPreviewVisible) return '';

  const renderPreviewBullets = (nodes: ContentNode[], depth: number = 0): string => {
    return nodes.map(node => `
      <div class="preview-bullet" style="margin-left: ${depth * spacing.bulletIndent}px; margin-bottom: ${spacing.bulletSpacing}px;">
        <span class="preview-bullet-symbol">${getBulletSymbol(depth)}</span>
        ${escapeHtml(node.text)}
      </div>
      ${node.children.length > 0 ? renderPreviewBullets(node.children, depth + 1) : ''}
    `).join('');
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

  return `
    <div class="preview-pane">
      <div class="preview-header">
        <span class="preview-title">Preview</span>
        <span class="preview-status">&bull; Live</span>
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

function renderToolbar(): string {
  const { focusMode, isPreviewVisible } = store.getState();

  return `
    <div class="toolbar">
      <div class="toolbar-left">
        <span class="app-title">resumeyay</span>
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
        <button class="btn-toolbar ${isPreviewVisible ? 'active' : ''}"
                id="btn-toggle-preview" title="Toggle Preview (Cmd+\\)">
          Preview
        </button>
        <button class="btn-toolbar" id="btn-style-studio" title="Style Studio (Cmd+Shift+S)">
          Style
        </button>
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

    // Add entry buttons
    const addEntryBtn = target.closest('.btn-add-entry') as HTMLElement | null;
    if (addEntryBtn) {
      const sectionId = addEntryBtn.dataset.sectionId!;
      store.addEntry(sectionId);
      return;
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

    // Export button
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

  // Handle style control changes via delegation
  app.addEventListener('change', (e) => {
    const target = e.target as HTMLInputElement | HTMLSelectElement;
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
    render();
  });

  // Setup keyboard shortcuts
  setupKeyboardShortcuts();

  // Initial render (forced to ensure it happens)
  render(true);
}

// Start the app
init();
