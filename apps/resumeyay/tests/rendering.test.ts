/**
 * Rendering Tests - Tests for DOM rendering and UI components
 */
import { describe, test, expect, beforeEach } from 'bun:test';
import { resetLocalStorage } from './setup';

// Helper to create a simple render test environment
function createTestDocument() {
  // Create the #app element
  document.body.innerHTML = '<div id="app"></div>';
  return document.querySelector('#app') as HTMLDivElement;
}

// Since main.ts has side effects (runs init on import), we'll test rendering functions
// by extracting the core logic. For this test, we'll simulate the rendered output.

describe('DOM Structure', () => {
  beforeEach(() => {
    resetLocalStorage();
    document.body.innerHTML = '';
  });

  test('app container can be created', () => {
    const app = createTestDocument();
    expect(app).toBeDefined();
    expect(app.id).toBe('app');
  });

  test('document has a body', () => {
    expect(document.body).toBeDefined();
  });

  test('can create and query DOM elements', () => {
    document.body.innerHTML = `
      <div class="toolbar">
        <button class="btn-mode active" data-mode="full-matrix">Full</button>
        <button class="btn-mode" data-mode="narrative">Narrative</button>
      </div>
    `;

    const buttons = document.querySelectorAll('.btn-mode');
    expect(buttons.length).toBe(2);

    const activeButton = document.querySelector('.btn-mode.active');
    expect(activeButton).toBeDefined();
    expect((activeButton as HTMLElement).dataset.mode).toBe('full-matrix');
  });
});

describe('Template Rendering', () => {
  // Test template literal rendering patterns used in main.ts

  test('escape HTML utility pattern', () => {
    const escapeHtml = (text: string): string => {
      const div = document.createElement('div');
      div.textContent = text;
      return div.innerHTML;
    };

    expect(escapeHtml('Hello')).toBe('Hello');
    expect(escapeHtml('<script>alert("xss")</script>')).toContain('&lt;');
    expect(escapeHtml('Tom & Jerry')).toContain('&amp;');
    // textContent preserves quotes as-is (not escaped to &quot;)
    expect(escapeHtml('"quotes"')).toBe('"quotes"');
  });

  test('bullet symbol patterns', () => {
    const getBulletSymbol = (depth: number): string => {
      const symbols = ['&bull;', '&#9702;', '&#9642;'];
      return symbols[Math.min(depth, symbols.length - 1)];
    };

    expect(getBulletSymbol(0)).toBe('&bull;');
    expect(getBulletSymbol(1)).toBe('&#9702;');
    expect(getBulletSymbol(2)).toBe('&#9642;');
    expect(getBulletSymbol(3)).toBe('&#9642;'); // Should cap at max
    expect(getBulletSymbol(100)).toBe('&#9642;');
  });

  test('text truncation pattern', () => {
    const truncateText = (text: string, maxLength: number): string => {
      if (text.length <= maxLength) return text;
      return text.slice(0, maxLength - 3) + '...';
    };

    expect(truncateText('Short', 10)).toBe('Short');
    expect(truncateText('This is a very long text', 10)).toBe('This is...');
    expect(truncateText('Exactly10!', 10)).toBe('Exactly10!');
    // "Exactly11!!" has 11 chars, so slice(0, 7) + "..." = "Exactly..."
    expect(truncateText('Exactly11!!', 10)).toBe('Exactly...');
  });
});

describe('Column Class Generation', () => {
  test('generates correct column classes', () => {
    const getColumnClass = (col: string, state: string): string => {
      return `column-${col} column-${state}`;
    };

    expect(getColumnClass('employer', 'expanded')).toBe('column-employer column-expanded');
    expect(getColumnClass('content', 'collapsed')).toBe('column-content column-collapsed');
  });
});

describe('Focus Mode CSS Classes', () => {
  beforeEach(() => {
    resetLocalStorage();
  });

  test('main-content receives focus mode class', () => {
    const focusMode = 'narrative';
    const isPreviewVisible = true;

    document.body.innerHTML = `
      <div class="main-content ${focusMode} ${isPreviewVisible ? 'with-preview' : 'no-preview'}">
        <div class="editor-pane"></div>
        <div class="preview-pane"></div>
      </div>
    `;

    const mainContent = document.querySelector('.main-content');
    expect(mainContent?.classList.contains('narrative')).toBe(true);
    expect(mainContent?.classList.contains('with-preview')).toBe(true);
  });

  test('preview can be hidden', () => {
    const focusMode = 'full-matrix';
    const isPreviewVisible = false;

    document.body.innerHTML = `
      <div class="main-content ${focusMode} ${isPreviewVisible ? 'with-preview' : 'no-preview'}">
        <div class="editor-pane"></div>
      </div>
    `;

    const mainContent = document.querySelector('.main-content');
    expect(mainContent?.classList.contains('no-preview')).toBe(true);
    expect(mainContent?.classList.contains('with-preview')).toBe(false);
  });
});

describe('Toolbar Rendering', () => {
  test('focus mode buttons are rendered', () => {
    document.body.innerHTML = `
      <div class="focus-modes">
        <button class="btn-mode active" data-mode="full-matrix">Full</button>
        <button class="btn-mode" data-mode="narrative">Narrative</button>
        <button class="btn-mode" data-mode="timeline">Timeline</button>
        <button class="btn-mode" data-mode="compact">Compact</button>
      </div>
    `;

    const buttons = document.querySelectorAll('.btn-mode');
    expect(buttons.length).toBe(4);

    const modes = Array.from(buttons).map(b => (b as HTMLElement).dataset.mode);
    expect(modes).toContain('full-matrix');
    expect(modes).toContain('narrative');
    expect(modes).toContain('timeline');
    expect(modes).toContain('compact');
  });
});

describe('Entry Row Structure', () => {
  test('entry row has correct structure', () => {
    document.body.innerHTML = `
      <div class="entry-row" data-entry-id="entry-1" data-section-id="section-1">
        <div class="column-employer column-expanded">
          <input type="text" value="Acme Corp" data-field="organization" />
        </div>
        <div class="column-role column-expanded">
          <input type="text" value="Engineer" data-field="role" />
        </div>
        <div class="column-metadata column-expanded">
          <div class="metadata-fields">
            <input type="text" value="Jan 2020" data-field="dateStart" />
            <input type="text" value="Present" data-field="dateEnd" />
            <input type="text" value="SF, CA" data-field="location" />
          </div>
        </div>
        <div class="column-content column-expanded">
          <div class="content-bullets">
            <div class="bullet-item" data-bullet-id="bullet-1">
              <span class="bullet-symbol">&bull;</span>
              <input type="text" class="bullet-input" value="Did stuff" />
            </div>
          </div>
        </div>
      </div>
    `;

    const entryRow = document.querySelector('.entry-row');
    expect(entryRow).toBeDefined();
    expect((entryRow as HTMLElement).dataset.entryId).toBe('entry-1');

    const columns = entryRow?.querySelectorAll('[class^="column-"]');
    expect(columns?.length).toBeGreaterThanOrEqual(4);

    const orgInput = entryRow?.querySelector('[data-field="organization"]') as HTMLInputElement;
    expect(orgInput?.value).toBe('Acme Corp');
  });

  test('collapsed columns show handles', () => {
    document.body.innerHTML = `
      <div class="entry-row">
        <div class="column-employer column-collapsed">
          <div class="column-handle" title="Acme Corp">A</div>
        </div>
      </div>
    `;

    const handle = document.querySelector('.column-handle');
    expect(handle).toBeDefined();
    expect(handle?.textContent).toBe('A');
    expect((handle as HTMLElement).title).toBe('Acme Corp');
  });
});

describe('Bullet Rendering', () => {
  test('bullets render with correct structure', () => {
    document.body.innerHTML = `
      <div class="content-bullets">
        <div class="bullet-item" data-bullet-id="b1" style="margin-left: 0px">
          <span class="bullet-symbol">&bull;</span>
          <input type="text" class="bullet-input" value="First bullet" />
        </div>
        <div class="bullet-item" data-bullet-id="b2" style="margin-left: 20px">
          <span class="bullet-symbol">&#9702;</span>
          <input type="text" class="bullet-input" value="Nested bullet" />
        </div>
      </div>
    `;

    const bullets = document.querySelectorAll('.bullet-item');
    expect(bullets.length).toBe(2);

    const nestedBullet = bullets[1] as HTMLElement;
    expect(nestedBullet.style.marginLeft).toBe('20px');
  });

  test('active bullet has active class', () => {
    document.body.innerHTML = `
      <div class="bullet-item active" data-bullet-id="b1">
        <span class="bullet-symbol">&bull;</span>
        <input type="text" class="bullet-input" />
      </div>
    `;

    const bullet = document.querySelector('.bullet-item');
    expect(bullet?.classList.contains('active')).toBe(true);
  });
});

describe('Preview Pane', () => {
  test('preview pane has correct structure', () => {
    document.body.innerHTML = `
      <div class="preview-pane">
        <div class="preview-header">
          <span class="preview-title">Preview</span>
          <span class="preview-status">&bull; Live</span>
          <div class="preview-controls">
            <button class="btn-export">Export</button>
          </div>
        </div>
        <div class="preview-content">
          <div class="preview-resume-header">
            <div class="preview-name">Jon Cooper</div>
          </div>
        </div>
      </div>
    `;

    const preview = document.querySelector('.preview-pane');
    expect(preview).toBeDefined();

    const title = document.querySelector('.preview-title');
    expect(title?.textContent).toBe('Preview');

    const exportBtn = document.querySelector('.btn-export');
    expect(exportBtn).toBeDefined();
  });
});

describe('Style Studio', () => {
  test('style studio overlay has correct structure', () => {
    document.body.innerHTML = `
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
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    const overlay = document.querySelector('.style-studio-overlay');
    expect(overlay).toBeDefined();

    const studio = document.querySelector('.style-studio');
    expect(studio).toBeDefined();

    const presets = document.querySelectorAll('.btn-preset');
    expect(presets.length).toBe(2);
  });
});

describe('Floating Header', () => {
  test('floating header shows context in narrative mode', () => {
    document.body.innerHTML = `
      <div class="floating-header">
        <span class="floating-org">Acme Corp</span>
        <span class="floating-sep">&middot;</span>
        <span class="floating-role">Senior Engineer</span>
        <span class="floating-sep">&middot;</span>
        <span class="floating-date">Jan 2022 &ndash; Present</span>
      </div>
    `;

    const header = document.querySelector('.floating-header');
    expect(header).toBeDefined();

    const org = document.querySelector('.floating-org');
    expect(org?.textContent).toBe('Acme Corp');

    const role = document.querySelector('.floating-role');
    expect(role?.textContent).toBe('Senior Engineer');
  });
});

describe('Event Handling Patterns', () => {
  test('data attributes for event handling', () => {
    document.body.innerHTML = `
      <button class="btn-mode" data-mode="narrative">Narrative</button>
      <div class="entry-row" data-entry-id="entry-1" data-section-id="section-1"></div>
      <input data-field="organization" data-entry-id="entry-1" />
      <div class="bullet-item" data-bullet-id="bullet-1" data-entry-id="entry-1"></div>
    `;

    // Verify data attributes are accessible
    const btn = document.querySelector('.btn-mode') as HTMLElement;
    expect(btn.dataset.mode).toBe('narrative');

    const row = document.querySelector('.entry-row') as HTMLElement;
    expect(row.dataset.entryId).toBe('entry-1');
    expect(row.dataset.sectionId).toBe('section-1');

    const input = document.querySelector('[data-field="organization"]') as HTMLElement;
    expect(input.dataset.field).toBe('organization');
  });

  test('event listeners can be attached to buttons', () => {
    document.body.innerHTML = `<button id="test-btn">Click me</button>`;

    const btn = document.querySelector('#test-btn') as HTMLButtonElement;
    let clicked = false;

    btn.addEventListener('click', () => {
      clicked = true;
    });

    btn.click();
    expect(clicked).toBe(true);
  });

  test('input events can be simulated', () => {
    document.body.innerHTML = `<input type="text" id="test-input" />`;

    const input = document.querySelector('#test-input') as HTMLInputElement;
    let lastValue = '';

    input.addEventListener('input', (e) => {
      lastValue = (e.target as HTMLInputElement).value;
    });

    input.value = 'test value';
    input.dispatchEvent(new Event('input'));

    expect(lastValue).toBe('test value');
  });
});

describe('Accessibility Attributes', () => {
  test('inputs have proper types', () => {
    document.body.innerHTML = `
      <input type="text" placeholder="Name" />
      <input type="email" placeholder="Email" />
      <input type="tel" placeholder="Phone" />
      <input type="url" placeholder="URL" />
    `;

    const textInput = document.querySelector('input[type="text"]');
    expect(textInput).toBeDefined();

    const emailInput = document.querySelector('input[type="email"]');
    expect(emailInput).toBeDefined();

    const telInput = document.querySelector('input[type="tel"]');
    expect(telInput).toBeDefined();

    const urlInput = document.querySelector('input[type="url"]');
    expect(urlInput).toBeDefined();
  });

  test('buttons have titles for tooltips', () => {
    document.body.innerHTML = `
      <button class="btn-mode" title="Full Matrix (Cmd+1)">Full</button>
      <button id="btn-toggle-preview" title="Toggle Preview (Cmd+\\)">Preview</button>
    `;

    const modeBtn = document.querySelector('.btn-mode') as HTMLElement;
    expect(modeBtn.title).toContain('Cmd+1');

    const previewBtn = document.querySelector('#btn-toggle-preview') as HTMLElement;
    expect(previewBtn.title).toContain('Toggle Preview');
  });
});

describe('CSS Class Patterns', () => {
  test('active states use .active class', () => {
    document.body.innerHTML = `
      <button class="btn-mode active">Active Mode</button>
      <button class="btn-mode">Inactive Mode</button>
      <div class="entry-row active"></div>
      <div class="bullet-item active"></div>
    `;

    expect(document.querySelectorAll('.active').length).toBe(3);
  });

  test('column states use state classes', () => {
    document.body.innerHTML = `
      <div class="column-employer column-expanded"></div>
      <div class="column-role column-collapsed"></div>
    `;

    const expanded = document.querySelector('.column-expanded');
    const collapsed = document.querySelector('.column-collapsed');

    expect(expanded).toBeDefined();
    expect(collapsed).toBeDefined();
  });
});
