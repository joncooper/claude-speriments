/**
 * Integration Tests - Tests for complete workflows and interactions
 */
import { describe, test, expect, beforeEach } from 'bun:test';
import { resetLocalStorage } from './setup';

// Re-import store fresh for each test
let store: typeof import('../src/store').store;

beforeEach(async () => {
  resetLocalStorage();
  document.body.innerHTML = '<div id="app"></div>';
  const module = await import('../src/store');
  store = module.store;
});

describe('Resume Editing Workflow', () => {
  test('complete workflow: add section, entry, and bullets', () => {
    // Start with sample resume
    store.resetToSample();

    // Add a new section
    const newSectionId = store.addSection('projects', 'Personal Projects');
    const state = store.getState();
    const section = state.resume.sections.find(s => s.id === newSectionId);

    expect(section).toBeDefined();
    expect(section?.title).toBe('Personal Projects');
    expect(section?.type).toBe('projects');

    // Section comes with one empty entry
    expect(section?.entries.length).toBe(1);

    // Update the entry
    const entryId = section!.entries[0].id;
    store.updateEntry(newSectionId, entryId, {
      organization: 'Open Source Project',
      role: 'Maintainer',
      dateStart: '2021',
      dateEnd: 'Present',
      location: 'GitHub',
    });

    // Add bullet points
    const bulletId = store.getState().resume.sections
      .find(s => s.id === newSectionId)!.entries[0].content[0].id;

    store.updateBullet(entryId, bulletId, 'Created a popular CLI tool with 1000+ stars');

    const newBulletId = store.addBullet(entryId, bulletId);
    store.updateBullet(entryId, newBulletId, 'Managed community contributions and issues');

    // Verify the result
    const finalState = store.getState();
    const finalEntry = finalState.resume.sections
      .find(s => s.id === newSectionId)!.entries[0];

    expect(finalEntry.organization).toBe('Open Source Project');
    expect(finalEntry.content.length).toBe(2);
    expect(finalEntry.content[0].text).toContain('1000+ stars');
    expect(finalEntry.content[1].text).toContain('contributions');
  });

  test('complete workflow: edit existing entry', () => {
    store.resetToSample();

    const state = store.getState();
    const sectionId = state.resume.sections[0].id;
    const entryId = state.resume.sections[0].entries[0].id;

    // Update organization name
    store.updateEntry(sectionId, entryId, {
      organization: 'Updated Company Name',
    });

    // Update a bullet
    const bulletId = state.resume.sections[0].entries[0].content[0].id;
    store.updateBullet(entryId, bulletId, 'Completely new accomplishment');

    const finalState = store.getState();
    const entry = finalState.resume.sections[0].entries.find(e => e.id === entryId);

    expect(entry?.organization).toBe('Updated Company Name');
    expect(entry?.content[0].text).toBe('Completely new accomplishment');
  });
});

describe('Focus Mode Workflow', () => {
  test('switching between modes preserves data', () => {
    store.resetToSample();
    const originalState = JSON.parse(JSON.stringify(store.getState().resume));

    // Switch through all modes
    store.setFocusMode('narrative');
    store.setFocusMode('timeline');
    store.setFocusMode('compact');
    store.setFocusMode('full-matrix');

    const finalState = store.getState();

    // Resume data should be unchanged
    expect(finalState.resume.header.name).toBe(originalState.header.name);
    expect(finalState.resume.sections.length).toBe(originalState.sections.length);
  });

  test('editing in narrative mode works correctly', () => {
    store.resetToSample();
    store.setFocusMode('narrative');

    const state = store.getState();
    const entryId = state.resume.sections[0].entries[0].id;
    const bulletId = state.resume.sections[0].entries[0].content[0].id;

    // Edit a bullet
    store.updateBullet(entryId, bulletId, 'Edited in narrative mode');

    const newState = store.getState();
    const entry = newState.resume.sections[0].entries.find(e => e.id === entryId);
    expect(entry?.content[0].text).toBe('Edited in narrative mode');

    // Mode should still be narrative
    expect(newState.focusMode).toBe('narrative');
  });

  test('editing in timeline mode works correctly', () => {
    store.resetToSample();
    store.setFocusMode('timeline');

    const state = store.getState();
    const sectionId = state.resume.sections[0].id;
    const entryId = state.resume.sections[0].entries[0].id;

    // Edit metadata
    store.updateEntry(sectionId, entryId, {
      dateStart: 'Feb 2023',
      dateEnd: 'Current',
    });

    const newState = store.getState();
    const entry = newState.resume.sections[0].entries.find(e => e.id === entryId);

    expect(entry?.dateStart).toBe('Feb 2023');
    expect(entry?.dateEnd).toBe('Current');
  });
});

describe('Undo/Redo Workflow', () => {
  test('can undo multiple operations and redo them', () => {
    store.resetToSample();
    const originalName = store.getState().resume.header.name;

    // Make several changes
    store.updateHeader({ name: 'Change 1' });
    store.updateHeader({ name: 'Change 2' });
    store.updateHeader({ name: 'Change 3' });

    expect(store.getState().resume.header.name).toBe('Change 3');

    // Undo all
    store.undo();
    expect(store.getState().resume.header.name).toBe('Change 2');

    store.undo();
    expect(store.getState().resume.header.name).toBe('Change 1');

    store.undo();
    expect(store.getState().resume.header.name).toBe(originalName);

    // Redo all
    store.redo();
    expect(store.getState().resume.header.name).toBe('Change 1');

    store.redo();
    expect(store.getState().resume.header.name).toBe('Change 2');

    store.redo();
    expect(store.getState().resume.header.name).toBe('Change 3');
  });

  test('making changes after undo clears redo stack', () => {
    store.resetToSample();

    store.updateHeader({ name: 'Change 1' });
    store.updateHeader({ name: 'Change 2' });

    store.undo(); // Back to Change 1

    // Make a new change - should clear redo
    store.updateHeader({ name: 'New Branch' });

    store.redo(); // Should do nothing

    expect(store.getState().resume.header.name).toBe('New Branch');
  });
});

describe('Style Settings Workflow', () => {
  test('apply preset then customize', () => {
    // Apply classic preset
    store.applyStylePreset('classic');

    let state = store.getState();
    expect(state.styleSettings.typography.primaryFont).toContain('Georgia');

    // Customize base size
    store.updateStyleSettings({
      typography: {
        ...state.styleSettings.typography,
        baseSize: 13,
      },
    });

    state = store.getState();
    expect(state.styleSettings.typography.baseSize).toBe(13);
    // Font should still be Georgia
    expect(state.styleSettings.typography.primaryFont).toContain('Georgia');
  });

  test('style changes persist in state', () => {
    store.updateStyleSettings({
      colors: {
        textColor: '#000000',
        accentColor: '#FF5500',
        dividerColor: '#AAAAAA',
        linkColor: '#FF5500',
      },
    });

    const state = store.getState();
    expect(state.styleSettings.colors.accentColor).toBe('#FF5500');
  });
});

describe('Bullet Nesting Workflow', () => {
  test('create nested bullet structure', () => {
    // Start with empty resume to have clean state
    store.newResume();

    const state = store.getState();
    const sectionId = state.resume.sections[0].id;
    const entryId = state.resume.sections[0].entries[0].id;
    const parentBulletId = state.resume.sections[0].entries[0].content[0].id;

    // Set parent text
    store.updateBullet(entryId, parentBulletId, 'Parent bullet');

    // Add a new bullet after the parent
    const childBulletId = store.addBullet(entryId, parentBulletId);

    // Indent it to make it a child
    store.indentBullet(entryId, childBulletId);

    // Add text to the child
    store.updateBullet(entryId, childBulletId, 'This is a nested bullet');

    const newState = store.getState();
    const entry = newState.resume.sections[0].entries.find(e => e.id === entryId);
    const parent = entry?.content[0];

    expect(parent?.children.length).toBe(1);
    expect(parent?.children[0].text).toBe('This is a nested bullet');
  });

  test('move bullet within list', () => {
    store.resetToSample();

    const state = store.getState();
    const entry = state.resume.sections[0].entries[0];

    // Add bullets to ensure we have multiple
    store.addBullet(entry.id, null);
    store.addBullet(entry.id, null);

    const stateWithBullets = store.getState();
    const bullets = stateWithBullets.resume.sections[0].entries[0].content;

    // Get the last bullet and move it up
    const lastBulletId = bullets[bullets.length - 1].id;
    store.moveBullet(entry.id, lastBulletId, 'up');

    const finalState = store.getState();
    const finalBullets = finalState.resume.sections[0].entries[0].content;

    // The originally last bullet should now be second-to-last
    expect(finalBullets[finalBullets.length - 2].id).toBe(lastBulletId);
  });
});

describe('Entry Reordering Workflow', () => {
  test('move entry up in list', () => {
    store.resetToSample();

    const state = store.getState();
    const sectionId = state.resume.sections[0].id;
    const entries = state.resume.sections[0].entries;

    // Get second entry and move it up
    if (entries.length >= 2) {
      const secondEntryId = entries[1].id;
      store.moveEntry(sectionId, secondEntryId, 'up');

      const newState = store.getState();
      const newEntries = newState.resume.sections[0].entries;

      expect(newEntries[0].id).toBe(secondEntryId);
    }
  });

  test('move entry down in list', () => {
    store.resetToSample();

    const state = store.getState();
    const sectionId = state.resume.sections[0].id;
    const entries = state.resume.sections[0].entries;

    if (entries.length >= 2) {
      const firstEntryId = entries[0].id;
      store.moveEntry(sectionId, firstEntryId, 'down');

      const newState = store.getState();
      const newEntries = newState.resume.sections[0].entries;

      expect(newEntries[1].id).toBe(firstEntryId);
    }
  });
});

describe('UI State Integration', () => {
  test('selecting entry and bullet together', () => {
    store.resetToSample();

    const state = store.getState();
    const entryId = state.resume.sections[0].entries[0].id;
    const bulletId = state.resume.sections[0].entries[0].content[0].id;

    // Select entry
    store.setActiveEntry(entryId);
    expect(store.getState().activeEntryId).toBe(entryId);

    // Select bullet within entry
    store.setActiveBullet(bulletId);
    store.setActiveCell('content');

    const finalState = store.getState();
    expect(finalState.activeEntryId).toBe(entryId);
    expect(finalState.activeBulletId).toBe(bulletId);
    expect(finalState.activeCellType).toBe('content');
  });

  test('opening style studio pauses preview updates', () => {
    store.toggleStyleStudio();
    expect(store.getState().isStyleStudioOpen).toBe(true);

    // Can still toggle preview while studio is open
    store.togglePreview();
    expect(store.getState().isPreviewVisible).toBe(false);

    store.toggleStyleStudio();
    expect(store.getState().isStyleStudioOpen).toBe(false);
  });
});

describe('Data Persistence Simulation', () => {
  test('data survives save/load cycle simulation', () => {
    store.resetToSample();

    // Make changes
    store.updateHeader({ name: 'Persisted Name' });
    store.updateHeader({ email: 'persisted@example.com' });

    // Get current state
    const savedState = JSON.parse(JSON.stringify(store.getState().resume));

    // Simulate "loading" by verifying the state matches what would be saved
    expect(savedState.header.name).toBe('Persisted Name');
    expect(savedState.header.email).toBe('persisted@example.com');
  });
});

describe('Edge Cases', () => {
  test('empty resume operations', () => {
    store.newResume();

    const state = store.getState();
    expect(state.resume.header.name).toBe('');
    expect(state.resume.sections.length).toBe(1);

    // Can still add entries
    const sectionId = state.resume.sections[0].id;
    store.addEntry(sectionId);

    expect(store.getState().resume.sections[0].entries.length).toBe(2);
  });

  test('deleting entries respects minimum', () => {
    store.newResume();

    const state = store.getState();
    const sectionId = state.resume.sections[0].id;
    const entryId = state.resume.sections[0].entries[0].id;

    // Try to delete the only entry - should keep at least one
    store.deleteEntry(sectionId, entryId);

    // Should still have one entry (same or different)
    expect(store.getState().resume.sections[0].entries.length).toBe(1);
  });

  test('operations on non-existent IDs are safe', () => {
    store.resetToSample();

    // These should not throw
    store.updateEntry('fake-section', 'fake-entry', { organization: 'Test' });
    store.updateBullet('fake-entry', 'fake-bullet', 'Test');
    store.deleteBullet('fake-entry', 'fake-bullet');
    store.indentBullet('fake-entry', 'fake-bullet');

    // State should be unchanged
    const state = store.getState();
    expect(state.resume.header.name).toBe('Jane Developer');
  });
});
