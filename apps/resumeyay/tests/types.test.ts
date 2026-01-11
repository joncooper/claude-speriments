/**
 * Type Definition Tests - Tests for type constants and default values
 */
import { describe, test, expect } from 'bun:test';
import {
  DEFAULT_STYLE_SETTINGS,
  STYLE_PRESETS,
  FOCUS_MODE_CONFIGS,
} from '../src/types';
import type {
  Resume,
  Entry,
  Section,
  ContentNode,
  FocusMode,
  ColumnConfig,
  StyleSettings,
  TypographySettings,
  SpacingSettings,
  LayoutSettings,
  ColorSettings,
} from '../src/types';

describe('DEFAULT_STYLE_SETTINGS', () => {
  test('has valid typography settings', () => {
    const { typography } = DEFAULT_STYLE_SETTINGS;

    expect(typography.primaryFont).toBeDefined();
    expect(typography.headerFont).toBeDefined();
    expect(typography.baseSize).toBeGreaterThan(0);
    expect(typography.lineHeight).toBeGreaterThan(0);
    expect(typography.nameScale).toBeGreaterThan(0);
    expect(typography.sectionHeaderScale).toBeGreaterThan(0);
  });

  test('has valid spacing settings', () => {
    const { spacing } = DEFAULT_STYLE_SETTINGS;

    expect(spacing.pageMargins).toBeGreaterThan(0);
    expect(spacing.sectionGap).toBeGreaterThan(0);
    expect(spacing.entryGap).toBeGreaterThan(0);
    expect(spacing.bulletIndent).toBeGreaterThan(0);
    expect(spacing.bulletSpacing).toBeGreaterThan(0);
  });

  test('has valid layout settings', () => {
    const { layout } = DEFAULT_STYLE_SETTINGS;

    expect(['right', 'inline']).toContain(layout.datePosition);
    expect(['with-date', 'below']).toContain(layout.locationPosition);
    expect(['none', 'line', 'double', 'dots']).toContain(layout.sectionDividers);
    expect(['single', 'two-column']).toContain(layout.columnMode);
  });

  test('has valid color settings', () => {
    const { colors } = DEFAULT_STYLE_SETTINGS;

    expect(colors.textColor).toMatch(/^#[0-9A-Fa-f]{6}$/);
    expect(colors.accentColor).toMatch(/^#[0-9A-Fa-f]{6}$/);
    expect(colors.dividerColor).toMatch(/^#[0-9A-Fa-f]{6}$/);
    expect(colors.linkColor).toMatch(/^#[0-9A-Fa-f]{6}$/);
  });
});

describe('STYLE_PRESETS', () => {
  test('classic preset has serif fonts', () => {
    const classic = STYLE_PRESETS.classic;
    expect(classic.typography?.primaryFont).toContain('serif');
  });

  test('modern preset has sans-serif fonts', () => {
    const modern = STYLE_PRESETS.modern;
    expect(modern.typography?.primaryFont).toContain('sans-serif');
  });

  test('minimal preset has no section dividers', () => {
    const minimal = STYLE_PRESETS.minimal;
    expect(minimal.layout?.sectionDividers).toBe('none');
  });

  test('dense preset has smaller font size', () => {
    const dense = STYLE_PRESETS.dense;
    expect(dense.typography?.baseSize).toBeLessThan(10);
  });

  test('all presets have typography defined', () => {
    expect(STYLE_PRESETS.classic.typography).toBeDefined();
    expect(STYLE_PRESETS.modern.typography).toBeDefined();
    expect(STYLE_PRESETS.minimal.typography).toBeDefined();
    expect(STYLE_PRESETS.dense.typography).toBeDefined();
  });

  test('all presets have spacing defined', () => {
    expect(STYLE_PRESETS.classic.spacing).toBeDefined();
    expect(STYLE_PRESETS.modern.spacing).toBeDefined();
    expect(STYLE_PRESETS.minimal.spacing).toBeDefined();
    expect(STYLE_PRESETS.dense.spacing).toBeDefined();
  });
});

describe('FOCUS_MODE_CONFIGS', () => {
  test('full-matrix has all columns expanded', () => {
    const config = FOCUS_MODE_CONFIGS['full-matrix'];
    expect(config.employer).toBe('expanded');
    expect(config.role).toBe('expanded');
    expect(config.metadata).toBe('expanded');
    expect(config.content).toBe('expanded');
  });

  test('narrative has content expanded and others collapsed', () => {
    const config = FOCUS_MODE_CONFIGS['narrative'];
    expect(config.employer).toBe('collapsed');
    expect(config.role).toBe('collapsed');
    expect(config.metadata).toBe('collapsed');
    expect(config.content).toBe('expanded');
  });

  test('timeline has content collapsed and others expanded', () => {
    const config = FOCUS_MODE_CONFIGS['timeline'];
    expect(config.employer).toBe('expanded');
    expect(config.role).toBe('expanded');
    expect(config.metadata).toBe('expanded');
    expect(config.content).toBe('collapsed');
  });

  test('compact has all columns expanded', () => {
    const config = FOCUS_MODE_CONFIGS['compact'];
    expect(config.employer).toBe('expanded');
    expect(config.role).toBe('expanded');
    expect(config.metadata).toBe('expanded');
    expect(config.content).toBe('expanded');
  });
});

describe('Type Shapes', () => {
  // These tests verify the structure of types at runtime
  // by creating objects that should match the types

  test('ContentNode structure is valid', () => {
    const node: ContentNode = {
      id: 'test-id',
      text: 'Test text',
      children: [],
      collapsed: false,
    };

    expect(node.id).toBeDefined();
    expect(node.text).toBeDefined();
    expect(Array.isArray(node.children)).toBe(true);
  });

  test('ContentNode can have nested children', () => {
    const node: ContentNode = {
      id: 'parent',
      text: 'Parent',
      children: [
        {
          id: 'child1',
          text: 'Child 1',
          children: [
            {
              id: 'grandchild',
              text: 'Grandchild',
              children: [],
            },
          ],
        },
        {
          id: 'child2',
          text: 'Child 2',
          children: [],
        },
      ],
    };

    expect(node.children).toHaveLength(2);
    expect(node.children[0].children).toHaveLength(1);
  });

  test('Entry structure is valid', () => {
    const entry: Entry = {
      id: 'entry-1',
      organization: 'Acme Corp',
      role: 'Engineer',
      dateStart: 'Jan 2020',
      dateEnd: 'Present',
      location: 'SF, CA',
      content: [
        {
          id: 'bullet-1',
          text: 'Did stuff',
          children: [],
        },
      ],
    };

    expect(entry.id).toBeDefined();
    expect(entry.organization).toBeDefined();
    expect(entry.content).toHaveLength(1);
  });

  test('Section structure is valid', () => {
    const section: Section = {
      id: 'section-1',
      type: 'experience',
      title: 'Work Experience',
      entries: [],
    };

    expect(section.id).toBeDefined();
    expect(section.type).toBe('experience');
    expect(Array.isArray(section.entries)).toBe(true);
  });

  test('Section types are constrained', () => {
    const validTypes = ['experience', 'education', 'projects', 'skills', 'custom'];

    validTypes.forEach(type => {
      const section: Section = {
        id: 'test',
        type: type as Section['type'],
        title: 'Test',
        entries: [],
      };
      expect(section.type).toBe(type);
    });
  });

  test('Resume structure is valid', () => {
    const resume: Resume = {
      id: 'resume-1',
      header: {
        name: 'John Doe',
        email: 'john@example.com',
        phone: '555-1234',
        location: 'NYC',
        links: [],
      },
      sections: [],
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
    };

    expect(resume.id).toBeDefined();
    expect(resume.header.name).toBeDefined();
    expect(Array.isArray(resume.sections)).toBe(true);
  });

  test('FocusMode values are valid', () => {
    const validModes: FocusMode[] = ['full-matrix', 'narrative', 'timeline', 'compact'];

    validModes.forEach(mode => {
      expect(FOCUS_MODE_CONFIGS[mode]).toBeDefined();
    });
  });

  test('ColumnConfig structure is valid', () => {
    const config: ColumnConfig = {
      employer: 'expanded',
      role: 'collapsed',
      metadata: 'expanded',
      content: 'collapsed',
    };

    expect(['expanded', 'collapsed', 'hidden']).toContain(config.employer);
    expect(['expanded', 'collapsed', 'hidden']).toContain(config.role);
    expect(['expanded', 'collapsed', 'hidden']).toContain(config.metadata);
    expect(['expanded', 'collapsed', 'hidden']).toContain(config.content);
  });
});

describe('Style Settings Types', () => {
  test('TypographySettings structure is valid', () => {
    const typography: TypographySettings = {
      primaryFont: 'Inter, sans-serif',
      headerFont: 'Georgia, serif',
      baseSize: 10,
      lineHeight: 1.4,
      nameScale: 2,
      sectionHeaderScale: 1.2,
    };

    expect(typography.baseSize).toBeGreaterThan(0);
    expect(typography.lineHeight).toBeGreaterThan(0);
  });

  test('SpacingSettings structure is valid', () => {
    const spacing: SpacingSettings = {
      pageMargins: 0.75,
      sectionGap: 14,
      entryGap: 8,
      bulletIndent: 16,
      bulletSpacing: 4,
    };

    Object.values(spacing).forEach(value => {
      expect(value).toBeGreaterThan(0);
    });
  });

  test('LayoutSettings structure is valid', () => {
    const layout: LayoutSettings = {
      datePosition: 'right',
      locationPosition: 'with-date',
      sectionDividers: 'line',
      columnMode: 'single',
    };

    expect(['right', 'inline']).toContain(layout.datePosition);
    expect(['with-date', 'below']).toContain(layout.locationPosition);
  });

  test('ColorSettings structure is valid', () => {
    const colors: ColorSettings = {
      textColor: '#1A1A1A',
      accentColor: '#2563EB',
      dividerColor: '#E5E5E5',
      linkColor: '#2563EB',
    };

    Object.values(colors).forEach(color => {
      expect(color).toMatch(/^#[0-9A-Fa-f]{6}$/);
    });
  });

  test('StyleSettings combines all settings', () => {
    const settings: StyleSettings = {
      typography: DEFAULT_STYLE_SETTINGS.typography,
      spacing: DEFAULT_STYLE_SETTINGS.spacing,
      layout: DEFAULT_STYLE_SETTINGS.layout,
      colors: DEFAULT_STYLE_SETTINGS.colors,
    };

    expect(settings.typography).toBeDefined();
    expect(settings.spacing).toBeDefined();
    expect(settings.layout).toBeDefined();
    expect(settings.colors).toBeDefined();
  });
});
