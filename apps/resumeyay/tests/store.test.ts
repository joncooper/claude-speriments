/**
 * Store Tests - Comprehensive tests for state management
 */
import { describe, test, expect, beforeEach } from 'bun:test';
import { resetLocalStorage } from './setup';

// We need to import fresh each time to reset state
let store: typeof import('../src/store').store;
let createContentNode: typeof import('../src/store').createContentNode;
let createEntry: typeof import('../src/store').createEntry;
let createSection: typeof import('../src/store').createSection;
let createSampleResume: typeof import('../src/store').createSampleResume;
let createEmptyResume: typeof import('../src/store').createEmptyResume;

beforeEach(async () => {
  resetLocalStorage();
  // Re-import to get fresh state
  const module = await import('../src/store');
  store = module.store;
  createContentNode = module.createContentNode;
  createEntry = module.createEntry;
  createSection = module.createSection;
  createSampleResume = module.createSampleResume;
  createEmptyResume = module.createEmptyResume;
});

describe('Factory Functions', () => {
  test('createContentNode creates a valid content node', () => {
    const node = createContentNode('Test bullet');
    expect(node.id).toBeDefined();
    expect(node.text).toBe('Test bullet');
    expect(node.children).toEqual([]);
    expect(node.collapsed).toBe(false);
  });

  test('createContentNode creates empty node when no text provided', () => {
    const node = createContentNode();
    expect(node.text).toBe('');
  });

  test('createEntry creates a valid entry with empty fields', () => {
    const entry = createEntry();
    expect(entry.id).toBeDefined();
    expect(entry.organization).toBe('');
    expect(entry.role).toBe('');
    expect(entry.dateStart).toBe('');
    expect(entry.dateEnd).toBe('Present');
    expect(entry.location).toBe('');
    expect(entry.content).toHaveLength(1);
    expect(entry.content[0].text).toBe('');
  });

  test('createSection creates a valid section', () => {
    const section = createSection('experience', 'Work Experience');
    expect(section.id).toBeDefined();
    expect(section.type).toBe('experience');
    expect(section.title).toBe('Work Experience');
    expect(section.entries).toHaveLength(1);
  });

  test('createSampleResume creates a resume with sample data', () => {
    const resume = createSampleResume();
    expect(resume.id).toBeDefined();
    expect(resume.header.name).toBe('Jane Developer');
    expect(resume.header.email).toBe('jane@example.com');
    expect(resume.sections.length).toBeGreaterThan(0);
    expect(resume.sections[0].type).toBe('experience');
  });

  test('createEmptyResume creates a blank resume', () => {
    const resume = createEmptyResume();
    expect(resume.id).toBeDefined();
    expect(resume.header.name).toBe('');
    expect(resume.header.email).toBe('');
    expect(resume.sections).toHaveLength(1);
  });
});

describe('Store State', () => {
  test('getState returns the current state', () => {
    const state = store.getState();
    expect(state).toBeDefined();
    expect(state.resume).toBeDefined();
    expect(state.focusMode).toBeDefined();
    expect(state.columnConfig).toBeDefined();
    expect(state.styleSettings).toBeDefined();
  });

  test('initial focus mode is full-matrix', () => {
    const state = store.getState();
    expect(state.focusMode).toBe('full-matrix');
  });

  test('initial column config has all columns expanded', () => {
    const state = store.getState();
    expect(state.columnConfig.employer).toBe('expanded');
    expect(state.columnConfig.role).toBe('expanded');
    expect(state.columnConfig.metadata).toBe('expanded');
    expect(state.columnConfig.content).toBe('expanded');
  });
});

describe('Header Updates', () => {
  test('updateHeader updates name', () => {
    store.updateHeader({ name: 'John Doe' });
    const state = store.getState();
    expect(state.resume.header.name).toBe('John Doe');
  });

  test('updateHeader updates email', () => {
    store.updateHeader({ email: 'john@example.com' });
    const state = store.getState();
    expect(state.resume.header.email).toBe('john@example.com');
  });

  test('updateHeader updates multiple fields', () => {
    store.updateHeader({
      name: 'Jane Smith',
      phone: '555-1234',
      location: 'New York, NY',
    });
    const state = store.getState();
    expect(state.resume.header.name).toBe('Jane Smith');
    expect(state.resume.header.phone).toBe('555-1234');
    expect(state.resume.header.location).toBe('New York, NY');
  });
});

describe('Entry Operations', () => {
  test('addEntry adds a new entry to a section', () => {
    const state = store.getState();
    const sectionId = state.resume.sections[0].id;
    const initialCount = state.resume.sections[0].entries.length;

    const newEntryId = store.addEntry(sectionId);

    const newState = store.getState();
    expect(newState.resume.sections[0].entries.length).toBe(initialCount + 1);
    expect(newEntryId).toBeDefined();
  });

  test('updateEntry updates entry fields', () => {
    const state = store.getState();
    const sectionId = state.resume.sections[0].id;
    const entryId = state.resume.sections[0].entries[0].id;

    store.updateEntry(sectionId, entryId, {
      organization: 'New Company',
      role: 'Senior Developer',
    });

    const newState = store.getState();
    const entry = newState.resume.sections[0].entries.find(e => e.id === entryId);
    expect(entry?.organization).toBe('New Company');
    expect(entry?.role).toBe('Senior Developer');
  });

  test('deleteEntry removes an entry from section', () => {
    const state = store.getState();
    const sectionId = state.resume.sections[0].id;

    // Add an entry first to ensure we have at least 2
    store.addEntry(sectionId);
    const stateAfterAdd = store.getState();
    const entryToDelete = stateAfterAdd.resume.sections[0].entries[0].id;
    const countBefore = stateAfterAdd.resume.sections[0].entries.length;

    store.deleteEntry(sectionId, entryToDelete);

    const newState = store.getState();
    expect(newState.resume.sections[0].entries.length).toBe(countBefore - 1);
    expect(newState.resume.sections[0].entries.find(e => e.id === entryToDelete)).toBeUndefined();
  });

  test('moveEntry moves entry up', () => {
    const state = store.getState();
    const sectionId = state.resume.sections[0].id;

    // Add entries to have something to move
    store.addEntry(sectionId);
    const stateAfterAdd = store.getState();
    const secondEntryId = stateAfterAdd.resume.sections[0].entries[1].id;

    store.moveEntry(sectionId, secondEntryId, 'up');

    const newState = store.getState();
    expect(newState.resume.sections[0].entries[0].id).toBe(secondEntryId);
  });

  test('moveEntry moves entry down', () => {
    const state = store.getState();
    const sectionId = state.resume.sections[0].id;

    // Add entries to have something to move
    store.addEntry(sectionId);
    const stateAfterAdd = store.getState();
    const firstEntryId = stateAfterAdd.resume.sections[0].entries[0].id;

    store.moveEntry(sectionId, firstEntryId, 'down');

    const newState = store.getState();
    expect(newState.resume.sections[0].entries[1].id).toBe(firstEntryId);
  });
});

describe('Bullet Operations', () => {
  test('updateBullet updates bullet text', () => {
    const state = store.getState();
    const entry = state.resume.sections[0].entries[0];
    const bulletId = entry.content[0].id;

    store.updateBullet(entry.id, bulletId, 'Updated bullet text');

    const newState = store.getState();
    const updatedEntry = newState.resume.sections[0].entries.find(e => e.id === entry.id);
    expect(updatedEntry?.content[0].text).toBe('Updated bullet text');
  });

  test('addBullet adds a new bullet after specified bullet', () => {
    const state = store.getState();
    const entry = state.resume.sections[0].entries[0];
    const bulletId = entry.content[0].id;
    const initialCount = entry.content.length;

    const newBulletId = store.addBullet(entry.id, bulletId);

    const newState = store.getState();
    const updatedEntry = newState.resume.sections[0].entries.find(e => e.id === entry.id);
    expect(updatedEntry?.content.length).toBe(initialCount + 1);
    expect(newBulletId).toBeDefined();
  });

  test('addBullet with null afterBulletId adds to end', () => {
    const state = store.getState();
    const entry = state.resume.sections[0].entries[0];
    const initialCount = entry.content.length;

    const newBulletId = store.addBullet(entry.id, null);

    const newState = store.getState();
    const updatedEntry = newState.resume.sections[0].entries.find(e => e.id === entry.id);
    expect(updatedEntry?.content.length).toBe(initialCount + 1);
    expect(updatedEntry?.content[updatedEntry.content.length - 1].id).toBe(newBulletId);
  });

  test('deleteBullet removes a bullet', () => {
    const state = store.getState();
    const entry = state.resume.sections[0].entries[0];

    // Add a bullet first
    store.addBullet(entry.id, null);
    const stateAfterAdd = store.getState();
    const updatedEntry = stateAfterAdd.resume.sections[0].entries.find(e => e.id === entry.id);
    const bulletToDelete = updatedEntry!.content[0].id;
    const countBefore = updatedEntry!.content.length;

    store.deleteBullet(entry.id, bulletToDelete);

    const newState = store.getState();
    const finalEntry = newState.resume.sections[0].entries.find(e => e.id === entry.id);
    expect(finalEntry?.content.length).toBe(countBefore - 1);
  });

  test('indentBullet makes bullet a child of previous bullet', () => {
    const state = store.getState();
    const entry = state.resume.sections[0].entries[0];

    // Add a second bullet
    const newBulletId = store.addBullet(entry.id, entry.content[0].id);

    // Indent the second bullet
    store.indentBullet(entry.id, newBulletId);

    const newState = store.getState();
    const updatedEntry = newState.resume.sections[0].entries.find(e => e.id === entry.id);

    // The new bullet should be a child of the first bullet
    expect(updatedEntry?.content[0].children.length).toBeGreaterThan(0);
    expect(updatedEntry?.content[0].children[0].id).toBe(newBulletId);
  });

  test('moveBullet moves bullet up', () => {
    const state = store.getState();
    const entry = state.resume.sections[0].entries[0];

    // Add a second bullet
    const secondBulletId = store.addBullet(entry.id, entry.content[0].id);

    // Move it up
    store.moveBullet(entry.id, secondBulletId, 'up');

    const newState = store.getState();
    const updatedEntry = newState.resume.sections[0].entries.find(e => e.id === entry.id);
    expect(updatedEntry?.content[0].id).toBe(secondBulletId);
  });
});

describe('Section Operations', () => {
  test('addSection adds a new section', () => {
    const state = store.getState();
    const initialCount = state.resume.sections.length;

    const newSectionId = store.addSection('education', 'Education');

    const newState = store.getState();
    expect(newState.resume.sections.length).toBe(initialCount + 1);

    const newSection = newState.resume.sections.find(s => s.id === newSectionId);
    expect(newSection?.type).toBe('education');
    expect(newSection?.title).toBe('Education');
  });
});

describe('Focus Modes', () => {
  test('setFocusMode changes to narrative mode', () => {
    store.setFocusMode('narrative');
    const state = store.getState();

    expect(state.focusMode).toBe('narrative');
    expect(state.columnConfig.employer).toBe('collapsed');
    expect(state.columnConfig.role).toBe('collapsed');
    expect(state.columnConfig.metadata).toBe('collapsed');
    expect(state.columnConfig.content).toBe('expanded');
  });

  test('setFocusMode changes to timeline mode', () => {
    store.setFocusMode('timeline');
    const state = store.getState();

    expect(state.focusMode).toBe('timeline');
    expect(state.columnConfig.employer).toBe('expanded');
    expect(state.columnConfig.role).toBe('expanded');
    expect(state.columnConfig.metadata).toBe('expanded');
    expect(state.columnConfig.content).toBe('collapsed');
  });

  test('setFocusMode changes to compact mode', () => {
    store.setFocusMode('compact');
    const state = store.getState();

    expect(state.focusMode).toBe('compact');
    expect(state.columnConfig.employer).toBe('expanded');
    expect(state.columnConfig.role).toBe('expanded');
    expect(state.columnConfig.metadata).toBe('expanded');
    expect(state.columnConfig.content).toBe('expanded');
  });

  test('setFocusMode changes to full-matrix mode', () => {
    // First change to another mode
    store.setFocusMode('narrative');

    // Then back to full-matrix
    store.setFocusMode('full-matrix');
    const state = store.getState();

    expect(state.focusMode).toBe('full-matrix');
    expect(state.columnConfig.employer).toBe('expanded');
    expect(state.columnConfig.role).toBe('expanded');
    expect(state.columnConfig.metadata).toBe('expanded');
    expect(state.columnConfig.content).toBe('expanded');
  });

  test('toggleColumn toggles a column between expanded and collapsed', () => {
    const state = store.getState();
    expect(state.columnConfig.employer).toBe('expanded');

    store.toggleColumn('employer');

    const newState = store.getState();
    expect(newState.columnConfig.employer).toBe('collapsed');

    store.toggleColumn('employer');

    const finalState = store.getState();
    expect(finalState.columnConfig.employer).toBe('expanded');
  });
});

describe('Selection State', () => {
  test('setActiveEntry sets the active entry', () => {
    const state = store.getState();
    const entryId = state.resume.sections[0].entries[0].id;

    store.setActiveEntry(entryId);

    const newState = store.getState();
    expect(newState.activeEntryId).toBe(entryId);
  });

  test('setActiveEntry can clear the selection', () => {
    const state = store.getState();
    const entryId = state.resume.sections[0].entries[0].id;

    store.setActiveEntry(entryId);
    store.setActiveEntry(null);

    const newState = store.getState();
    expect(newState.activeEntryId).toBeNull();
  });

  test('setActiveBullet sets the active bullet', () => {
    const state = store.getState();
    const bulletId = state.resume.sections[0].entries[0].content[0].id;

    store.setActiveBullet(bulletId);

    const newState = store.getState();
    expect(newState.activeBulletId).toBe(bulletId);
  });

  test('setActiveCell sets the active cell type', () => {
    store.setActiveCell('employer');
    expect(store.getState().activeCellType).toBe('employer');

    store.setActiveCell('content');
    expect(store.getState().activeCellType).toBe('content');

    store.setActiveCell(null);
    expect(store.getState().activeCellType).toBeNull();
  });
});

describe('Undo/Redo', () => {
  test('undo reverts the last change', () => {
    const state = store.getState();
    const originalName = state.resume.header.name;

    store.updateHeader({ name: 'New Name' });
    expect(store.getState().resume.header.name).toBe('New Name');

    store.undo();
    expect(store.getState().resume.header.name).toBe(originalName);
  });

  test('redo reapplies an undone change', () => {
    store.updateHeader({ name: 'New Name' });
    store.undo();

    const stateBefore = store.getState();

    store.redo();

    expect(store.getState().resume.header.name).toBe('New Name');
  });

  test('multiple undos work correctly', () => {
    const originalName = store.getState().resume.header.name;

    store.updateHeader({ name: 'First Change' });
    store.updateHeader({ name: 'Second Change' });
    store.updateHeader({ name: 'Third Change' });

    expect(store.getState().resume.header.name).toBe('Third Change');

    store.undo();
    expect(store.getState().resume.header.name).toBe('Second Change');

    store.undo();
    expect(store.getState().resume.header.name).toBe('First Change');

    store.undo();
    expect(store.getState().resume.header.name).toBe(originalName);
  });

  test('undo after making a new change clears redo stack', () => {
    store.updateHeader({ name: 'First Change' });
    store.updateHeader({ name: 'Second Change' });

    store.undo(); // Now "Second Change" is in redo stack

    store.updateHeader({ name: 'New Branch' });

    store.redo(); // Should do nothing since redo stack was cleared

    expect(store.getState().resume.header.name).toBe('New Branch');
  });
});

describe('Batch Undo', () => {
  test('batch mode groups multiple updates into single undo entry', () => {
    const originalName = store.getState().resume.header.name;
    const undoStackSize = store.getState().undoStack.length;

    // Start batch mode (simulates typing)
    store.startBatch();

    // Make multiple changes (simulates typing each character)
    store.updateHeader({ name: 'T' });
    store.updateHeader({ name: 'Te' });
    store.updateHeader({ name: 'Tes' });
    store.updateHeader({ name: 'Test' });

    // End batch mode
    store.endBatch();

    expect(store.getState().resume.header.name).toBe('Test');

    // Should only have added ONE entry to undo stack
    expect(store.getState().undoStack.length).toBe(undoStackSize + 1);

    // Single undo should revert all batched changes
    store.undo();
    expect(store.getState().resume.header.name).toBe(originalName);
  });

  test('empty batch does not add to undo stack', () => {
    const undoStackSize = store.getState().undoStack.length;

    store.startBatch();
    // No changes made
    store.endBatch();

    expect(store.getState().undoStack.length).toBe(undoStackSize);
  });

  test('batch with identical start/end state does not add to undo stack', () => {
    store.updateHeader({ name: 'Original' });
    const undoStackSize = store.getState().undoStack.length;

    store.startBatch();
    store.updateHeader({ name: 'Temp' });
    store.updateHeader({ name: 'Original' }); // Back to original
    store.endBatch();

    // No net change, so nothing added to undo stack
    expect(store.getState().undoStack.length).toBe(undoStackSize);
  });

  test('nested startBatch calls only create one batch', () => {
    const originalName = store.getState().resume.header.name;
    const undoStackSize = store.getState().undoStack.length;

    store.startBatch();
    store.updateHeader({ name: 'First' });
    store.startBatch(); // Should be ignored
    store.updateHeader({ name: 'Second' });
    store.endBatch();

    expect(store.getState().resume.header.name).toBe('Second');
    expect(store.getState().undoStack.length).toBe(undoStackSize + 1);

    store.undo();
    expect(store.getState().resume.header.name).toBe(originalName);
  });
});

describe('Style Settings', () => {
  test('updateStyleSettings updates typography', () => {
    store.updateStyleSettings({
      typography: {
        primaryFont: 'Georgia, serif',
        headerFont: 'Georgia, serif',
        baseSize: 12,
        lineHeight: 1.6,
        nameScale: 2.5,
        sectionHeaderScale: 1.3,
      },
    });

    const state = store.getState();
    expect(state.styleSettings.typography.primaryFont).toBe('Georgia, serif');
    expect(state.styleSettings.typography.baseSize).toBe(12);
  });

  test('updateStyleSettings updates spacing', () => {
    store.updateStyleSettings({
      spacing: {
        pageMargins: 1,
        sectionGap: 20,
        entryGap: 12,
        bulletIndent: 20,
        bulletSpacing: 6,
      },
    });

    const state = store.getState();
    expect(state.styleSettings.spacing.pageMargins).toBe(1);
    expect(state.styleSettings.spacing.sectionGap).toBe(20);
  });

  test('updateStyleSettings updates colors', () => {
    store.updateStyleSettings({
      colors: {
        textColor: '#000000',
        accentColor: '#FF0000',
        dividerColor: '#CCCCCC',
        linkColor: '#0000FF',
      },
    });

    const state = store.getState();
    expect(state.styleSettings.colors.textColor).toBe('#000000');
    expect(state.styleSettings.colors.accentColor).toBe('#FF0000');
  });

  test('applyStylePreset applies classic preset', () => {
    store.applyStylePreset('classic');

    const state = store.getState();
    expect(state.styleSettings.typography.primaryFont).toContain('Georgia');
    expect(state.styleSettings.typography.baseSize).toBe(11);
  });

  test('applyStylePreset applies modern preset', () => {
    store.applyStylePreset('modern');

    const state = store.getState();
    expect(state.styleSettings.typography.primaryFont).toContain('Inter');
    expect(state.styleSettings.typography.baseSize).toBe(10);
  });

  test('applyStylePreset applies minimal preset', () => {
    store.applyStylePreset('minimal');

    const state = store.getState();
    expect(state.styleSettings.layout.sectionDividers).toBe('none');
  });

  test('applyStylePreset applies dense preset', () => {
    store.applyStylePreset('dense');

    const state = store.getState();
    expect(state.styleSettings.typography.baseSize).toBe(9);
    expect(state.styleSettings.spacing.pageMargins).toBe(0.5);
  });
});

describe('UI State', () => {
  test('toggleStyleStudio toggles the style studio visibility', () => {
    expect(store.getState().isStyleStudioOpen).toBe(false);

    store.toggleStyleStudio();
    expect(store.getState().isStyleStudioOpen).toBe(true);

    store.toggleStyleStudio();
    expect(store.getState().isStyleStudioOpen).toBe(false);
  });

  test('togglePreview toggles the preview visibility', () => {
    expect(store.getState().isPreviewVisible).toBe(true);

    store.togglePreview();
    expect(store.getState().isPreviewVisible).toBe(false);

    store.togglePreview();
    expect(store.getState().isPreviewVisible).toBe(true);
  });
});

describe('Resume Reset', () => {
  test('resetToSample resets to sample resume', () => {
    // Modify the resume
    store.updateHeader({ name: 'Modified Name' });

    // Reset to sample
    store.resetToSample();

    const state = store.getState();
    expect(state.resume.header.name).toBe('Jane Developer');
  });

  test('newResume creates a blank resume', () => {
    // Ensure there's data first
    store.resetToSample();

    // Create new resume
    store.newResume();

    const state = store.getState();
    expect(state.resume.header.name).toBe('');
    expect(state.resume.header.email).toBe('');
  });
});

describe('Subscription', () => {
  test('subscribe is called when state changes', () => {
    let callCount = 0;
    const unsubscribe = store.subscribe(() => {
      callCount++;
    });

    store.updateHeader({ name: 'Test' });
    expect(callCount).toBe(1);

    store.updateHeader({ email: 'test@test.com' });
    expect(callCount).toBe(2);

    unsubscribe();

    store.updateHeader({ phone: '555-1234' });
    expect(callCount).toBe(2); // Should not increment after unsubscribe
  });
});
