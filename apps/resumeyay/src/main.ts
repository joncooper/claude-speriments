import { store } from './store';
import type { Entry, Section, ContentNode, FocusMode, ColumnConfig, StyleSettings } from './types';
import './style.css';

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
      <div class="preview-entry" style="margin-bottom: ${spacing.entryGap}px;">
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

function render(): void {
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

  attachEventListeners();
}

// ============================================================================
// EVENT HANDLERS
// ============================================================================

function attachEventListeners(): void {
  const app = document.querySelector<HTMLDivElement>('#app')!;

  // Focus mode buttons
  app.querySelectorAll('.btn-mode').forEach(btn => {
    btn.addEventListener('click', () => {
      const mode = (btn as HTMLElement).dataset.mode as FocusMode;
      store.setFocusMode(mode);
    });
  });

  // Column header clicks (toggle collapse)
  app.querySelectorAll('.column-header').forEach(header => {
    header.addEventListener('click', () => {
      const column = (header as HTMLElement).dataset.column as keyof ColumnConfig;
      store.toggleColumn(column);
    });
  });

  // Entry row clicks (set active)
  app.querySelectorAll('.entry-row').forEach(row => {
    row.addEventListener('click', () => {
      const entryId = (row as HTMLElement).dataset.entryId!;
      store.setActiveEntry(entryId);
    });
  });

  // Header field inputs
  app.querySelectorAll('.header-editor input').forEach(input => {
    input.addEventListener('input', (e) => {
      const field = (e.target as HTMLInputElement).dataset.field;
      const value = (e.target as HTMLInputElement).value;
      if (field === 'header.name') store.updateHeader({ name: value });
      else if (field === 'header.email') store.updateHeader({ email: value });
      else if (field === 'header.phone') store.updateHeader({ phone: value });
      else if (field === 'header.location') store.updateHeader({ location: value });
    });
  });

  // Entry field inputs
  app.querySelectorAll('.entry-row input[data-field]').forEach(input => {
    input.addEventListener('input', (e) => {
      const inputEl = e.target as HTMLInputElement;
      const field = inputEl.dataset.field;
      const row = inputEl.closest('.entry-row') as HTMLElement;
      const entryId = row.dataset.entryId!;
      const sectionId = row.dataset.sectionId!;
      const value = inputEl.value;

      if (field && entryId && sectionId) {
        store.updateEntry(sectionId, entryId, { [field]: value } as Partial<Entry>);
      }
    });
  });

  // Bullet inputs
  app.querySelectorAll('.bullet-input').forEach(input => {
    const inputEl = input as HTMLInputElement;

    inputEl.addEventListener('focus', () => {
      const bulletId = inputEl.dataset.bulletId!;
      const entryId = inputEl.dataset.entryId!;
      store.setActiveBullet(bulletId);
      store.setActiveEntry(entryId);
    });

    inputEl.addEventListener('input', () => {
      const bulletId = inputEl.dataset.bulletId!;
      const entryId = inputEl.dataset.entryId!;
      store.updateBullet(entryId, bulletId, inputEl.value);
    });
  });

  // Add bullet buttons
  app.querySelectorAll('.btn-add-bullet').forEach(btn => {
    btn.addEventListener('click', () => {
      const entryId = (btn as HTMLElement).dataset.entryId!;
      const newId = store.addBullet(entryId, null);
      setTimeout(() => {
        const newInput = document.querySelector(`[data-bullet-id="${newId}"] input`) as HTMLInputElement;
        if (newInput) newInput.focus();
      }, 50);
    });
  });

  // Add entry buttons
  app.querySelectorAll('.btn-add-entry').forEach(btn => {
    btn.addEventListener('click', () => {
      const sectionId = (btn as HTMLElement).dataset.sectionId!;
      store.addEntry(sectionId);
    });
  });

  // Add section button
  app.querySelector('.btn-add-section')?.addEventListener('click', () => {
    store.addSection('experience', 'New Section');
  });

  // Toggle preview
  app.querySelector('#btn-toggle-preview')?.addEventListener('click', () => {
    store.togglePreview();
  });

  // Style studio
  app.querySelector('#btn-style-studio')?.addEventListener('click', () => {
    store.toggleStyleStudio();
  });

  app.querySelector('.btn-close-studio')?.addEventListener('click', () => {
    store.toggleStyleStudio();
  });

  // Style presets
  app.querySelectorAll('.btn-preset').forEach(btn => {
    btn.addEventListener('click', () => {
      const preset = (btn as HTMLElement).dataset.preset as 'classic' | 'modern' | 'minimal' | 'dense';
      store.applyStylePreset(preset);
    });
  });

  // Style controls
  app.querySelectorAll('[data-style]').forEach(control => {
    control.addEventListener('change', (e) => {
      const path = (e.target as HTMLElement).dataset.style!;
      const [category, field] = path.split('.') as [keyof StyleSettings, string];
      const value = (e.target as HTMLInputElement | HTMLSelectElement).value;
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
  });

  // New resume
  app.querySelector('#btn-new')?.addEventListener('click', () => {
    if (confirm('Create a new blank resume? Your current data will be preserved in undo history.')) {
      store.newResume();
    }
  });

  // Load sample
  app.querySelector('#btn-sample')?.addEventListener('click', () => {
    if (confirm('Load sample resume data? Your current data will be preserved in undo history.')) {
      store.resetToSample();
    }
  });

  // Export button
  app.querySelector('.btn-export')?.addEventListener('click', async () => {
    const previewContent = document.querySelector('.preview-content') as HTMLElement | null;
    if (!previewContent) return;

    try {
      // Dynamic import of html2pdf
      const html2pdf = (await import('html2pdf.js')).default;

      const options = {
        margin: 0,
        filename: 'resume.pdf',
        image: { type: 'jpeg' as const, quality: 0.98 },
        html2canvas: { scale: 2, useCORS: true },
        jsPDF: { unit: 'in' as const, format: 'letter' as const, orientation: 'portrait' as const }
      };

      html2pdf().set(options).from(previewContent).save();
    } catch (error) {
      console.error('Export failed:', error);
      alert('Export failed. Please try again.');
    }
  });
}

// ============================================================================
// INITIALIZATION
// ============================================================================

function init(): void {
  // Subscribe to store changes
  store.subscribe(() => {
    render();
  });

  // Setup keyboard shortcuts
  setupKeyboardShortcuts();

  // Initial render
  render();
}

// Start the app
init();
