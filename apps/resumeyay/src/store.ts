import { v4 as uuidv4 } from 'uuid';
import type {
  Resume,
  Entry,
  Section,
  ContentNode,
  EditorState,
  FocusMode,
  ColumnConfig,
  StyleSettings,
} from './types';
import { DEFAULT_STYLE_SETTINGS } from './types';

// Local storage key
const STORAGE_KEY = 'resumeyay_data';
const STYLE_KEY = 'resumeyay_styles';

// Create a default content node
export function createContentNode(text: string = ''): ContentNode {
  return {
    id: uuidv4(),
    text,
    children: [],
    collapsed: false,
  };
}

// Create a default entry
export function createEntry(): Entry {
  return {
    id: uuidv4(),
    organization: '',
    role: '',
    dateStart: '',
    dateEnd: 'Present',
    location: '',
    content: [createContentNode()],
  };
}

// Entry templates for quick start
export type EntryTemplate = 'blank' | 'software-engineer' | 'product-manager' | 'education' | 'project';

export function createTemplatedEntry(template: EntryTemplate): Entry {
  const id = uuidv4();

  switch (template) {
    case 'software-engineer':
      return {
        id,
        organization: '',
        role: 'Software Engineer',
        dateStart: '',
        dateEnd: 'Present',
        location: '',
        content: [
          createContentNode('Led development of [feature/system] resulting in [metric] improvement'),
          createContentNode('Built [technology] system handling [scale] requests/users'),
          createContentNode('Collaborated with [teams] to deliver [project] on time'),
          createContentNode('Mentored [number] junior developers and conducted code reviews'),
        ],
      };

    case 'product-manager':
      return {
        id,
        organization: '',
        role: 'Product Manager',
        dateStart: '',
        dateEnd: 'Present',
        location: '',
        content: [
          createContentNode('Defined product roadmap for [product] serving [user count] users'),
          createContentNode('Increased [metric] by [percentage] through [initiative]'),
          createContentNode('Led cross-functional team of [number] across engineering, design, and marketing'),
          createContentNode('Conducted user research with [number]+ customers to inform product decisions'),
        ],
      };

    case 'education':
      return {
        id,
        organization: '',
        role: '',
        dateStart: '',
        dateEnd: '',
        location: '',
        content: [
          createContentNode('GPA: X.X/4.0'),
          createContentNode('Relevant coursework: [courses]'),
          createContentNode('Activities: [clubs, organizations]'),
        ],
      };

    case 'project':
      return {
        id,
        organization: '',
        role: '',
        dateStart: '',
        dateEnd: '',
        location: 'github.com/username/project',
        content: [
          createContentNode('Built [project type] using [technologies]'),
          createContentNode('[Key feature] enabling users to [benefit]'),
          createContentNode('[Metric] users/downloads/stars'),
        ],
      };

    case 'blank':
    default:
      return createEntry();
  }
}

// Create a default section
export function createSection(type: Section['type'] = 'experience', title: string = 'Experience'): Section {
  return {
    id: uuidv4(),
    type,
    title,
    entries: [createEntry()],
  };
}

// Create a sample resume for demo
export function createSampleResume(): Resume {
  return {
    id: uuidv4(),
    header: {
      name: 'Jane Developer',
      email: 'jane@example.com',
      phone: '(555) 123-4567',
      location: 'San Francisco, CA',
      links: [
        { id: uuidv4(), label: 'LinkedIn', url: 'linkedin.com/in/janedev' },
        { id: uuidv4(), label: 'GitHub', url: 'github.com/janedev' },
      ],
    },
    sections: [
      {
        id: uuidv4(),
        type: 'experience',
        title: 'Experience',
        entries: [
          {
            id: uuidv4(),
            organization: 'Acme Corp',
            role: 'Senior Software Engineer',
            dateStart: 'Jan 2022',
            dateEnd: 'Present',
            location: 'San Francisco, CA',
            content: [
              {
                id: uuidv4(),
                text: 'Led cross-functional team of 8 engineers to deliver core platform',
                children: [
                  { id: uuidv4(), text: 'Coordinated with product, design, and QA stakeholders', children: [] },
                  { id: uuidv4(), text: 'Established agile ceremonies and reporting cadence', children: [] },
                ],
              },
              {
                id: uuidv4(),
                text: 'Architected event-driven system processing 50K events/second',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Reduced deployment time from 4 hours to 15 minutes through CI/CD improvements',
                children: [],
              },
            ],
          },
          {
            id: uuidv4(),
            organization: 'Initech',
            role: 'Software Engineer',
            dateStart: 'Mar 2019',
            dateEnd: 'Dec 2021',
            location: 'Austin, TX',
            content: [
              {
                id: uuidv4(),
                text: 'Built real-time analytics pipeline handling 1M+ daily active users',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Implemented comprehensive CI/CD reducing release cycle from weekly to daily',
                children: [],
              },
            ],
          },
          {
            id: uuidv4(),
            organization: 'Globex Inc',
            role: 'Junior Developer',
            dateStart: 'Jun 2017',
            dateEnd: 'Feb 2019',
            location: 'Denver, CO',
            content: [
              {
                id: uuidv4(),
                text: 'Developed RESTful APIs serving 100K+ requests per day',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Contributed to frontend React application used by 50K monthly users',
                children: [],
              },
            ],
          },
        ],
      },
      {
        id: uuidv4(),
        type: 'education',
        title: 'Education',
        entries: [
          {
            id: uuidv4(),
            organization: 'University of California, Berkeley',
            role: 'B.S. Computer Science',
            dateStart: '2013',
            dateEnd: '2017',
            location: 'Berkeley, CA',
            content: [
              {
                id: uuidv4(),
                text: 'GPA: 3.8/4.0, Magna Cum Laude',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Relevant coursework: Data Structures, Algorithms, Distributed Systems',
                children: [],
              },
            ],
          },
        ],
      },
    ],
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  };
}

// Create an empty resume
export function createEmptyResume(): Resume {
  return {
    id: uuidv4(),
    header: {
      name: '',
      email: '',
      phone: '',
      location: '',
      links: [],
    },
    sections: [createSection('experience', 'Experience')],
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  };
}

// State management
type Listener = () => void;

class Store {
  private state: EditorState;
  private listeners: Set<Listener> = new Set();
  private batchMode: boolean = false;
  private batchStartSnapshot: Resume | null = null;

  constructor() {
    this.state = this.loadState();
  }

  // Batch mode for grouping changes into a single undo entry
  startBatch(): void {
    if (!this.batchMode) {
      this.batchMode = true;
      this.batchStartSnapshot = JSON.parse(JSON.stringify(this.state.resume));
    }
  }

  endBatch(): void {
    if (this.batchMode && this.batchStartSnapshot) {
      // Only add to undo if something actually changed
      if (JSON.stringify(this.batchStartSnapshot) !== JSON.stringify(this.state.resume)) {
        this.state.undoStack.push(this.batchStartSnapshot);
        if (this.state.undoStack.length > 50) {
          this.state.undoStack.shift();
        }
        this.state.redoStack = [];
      }
      this.batchMode = false;
      this.batchStartSnapshot = null;
    }
  }

  private loadState(): EditorState {
    const savedResume = localStorage.getItem(STORAGE_KEY);
    const savedStyles = localStorage.getItem(STYLE_KEY);

    const resume = savedResume
      ? JSON.parse(savedResume) as Resume
      : createSampleResume();

    const styleSettings = savedStyles
      ? JSON.parse(savedStyles) as StyleSettings
      : { ...DEFAULT_STYLE_SETTINGS };

    return {
      resume,
      focusMode: 'full-matrix' as FocusMode,
      columnConfig: {
        employer: 'expanded',
        role: 'expanded',
        metadata: 'expanded',
        content: 'expanded',
      },
      styleSettings,
      activeEntryId: null,
      activeCellType: null,
      activeBulletId: null,
      isStyleStudioOpen: false,
      isPreviewVisible: true,
      undoStack: [],
      redoStack: [],
    };
  }

  getState(): EditorState {
    return this.state;
  }

  subscribe(listener: Listener): () => void {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  }

  private notify(): void {
    this.listeners.forEach(listener => listener());
  }

  private saveResume(): void {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(this.state.resume));
    this.state.resume.updatedAt = new Date().toISOString();
    this.notifySave();
  }

  private saveStyles(): void {
    localStorage.setItem(STYLE_KEY, JSON.stringify(this.state.styleSettings));
  }

  private pushUndo(): void {
    // Skip if we're in batch mode - the batch will handle undo
    if (this.batchMode) return;

    this.state.undoStack.push(JSON.parse(JSON.stringify(this.state.resume)));
    if (this.state.undoStack.length > 50) {
      this.state.undoStack.shift();
    }
    this.state.redoStack = [];
  }

  // Resume actions
  updateResume(updates: Partial<Resume>): void {
    this.pushUndo();
    this.state.resume = { ...this.state.resume, ...updates };
    this.saveResume();
    this.notify();
  }

  updateHeader(updates: Partial<Resume['header']>): void {
    this.pushUndo();
    this.state.resume.header = { ...this.state.resume.header, ...updates };
    this.saveResume();
    this.notify();
  }

  updateEntry(sectionId: string, entryId: string, updates: Partial<Entry>): void {
    this.pushUndo();
    const section = this.state.resume.sections.find(s => s.id === sectionId);
    if (section) {
      const entry = section.entries.find(e => e.id === entryId);
      if (entry) {
        Object.assign(entry, updates);
        this.saveResume();
        this.notify();
      }
    }
  }

  updateBullet(entryId: string, bulletId: string, text: string): void {
    this.pushUndo();
    for (const section of this.state.resume.sections) {
      const entry = section.entries.find(e => e.id === entryId);
      if (entry) {
        const updateNode = (nodes: ContentNode[]): boolean => {
          for (const node of nodes) {
            if (node.id === bulletId) {
              node.text = text;
              return true;
            }
            if (updateNode(node.children)) return true;
          }
          return false;
        };
        if (updateNode(entry.content)) {
          this.saveResume();
          this.notify();
          return;
        }
      }
    }
  }

  addBullet(entryId: string, afterBulletId: string | null, indent: boolean = false): string {
    this.pushUndo();
    const newNode = createContentNode();

    for (const section of this.state.resume.sections) {
      const entry = section.entries.find(e => e.id === entryId);
      if (entry) {
        if (!afterBulletId) {
          entry.content.push(newNode);
          this.saveResume();
          this.notify();
          return newNode.id;
        }

        const addAfter = (nodes: ContentNode[]): boolean => {
          for (let i = 0; i < nodes.length; i++) {
            if (nodes[i].id === afterBulletId) {
              if (indent) {
                nodes[i].children.push(newNode);
              } else {
                nodes.splice(i + 1, 0, newNode);
              }
              return true;
            }
            if (addAfter(nodes[i].children)) return true;
          }
          return false;
        };

        if (addAfter(entry.content)) {
          this.saveResume();
          this.notify();
          return newNode.id;
        }
      }
    }
    return '';
  }

  deleteBullet(entryId: string, bulletId: string): string | null {
    this.pushUndo();

    for (const section of this.state.resume.sections) {
      const entry = section.entries.find(e => e.id === entryId);
      if (entry) {
        const deleteNode = (nodes: ContentNode[], parentNodes?: ContentNode[]): string | null => {
          for (let i = 0; i < nodes.length; i++) {
            if (nodes[i].id === bulletId) {
              // Get previous bullet ID before deleting
              let prevId: string | null = null;
              if (i > 0) {
                prevId = nodes[i - 1].id;
              } else if (parentNodes && parentNodes.length > 0) {
                // Find the parent
                for (const parent of parentNodes) {
                  if (parent.children.includes(nodes[i])) {
                    prevId = parent.id;
                    break;
                  }
                }
              }

              nodes.splice(i, 1);
              return prevId;
            }
            const result = deleteNode(nodes[i].children, nodes);
            if (result !== undefined) return result;
          }
          return undefined as unknown as null;
        };

        const prevId = deleteNode(entry.content);
        if (prevId !== undefined) {
          this.saveResume();
          this.notify();
          return prevId;
        }
      }
    }
    return null;
  }

  indentBullet(entryId: string, bulletId: string): void {
    this.pushUndo();

    for (const section of this.state.resume.sections) {
      const entry = section.entries.find(e => e.id === entryId);
      if (entry) {
        const indent = (nodes: ContentNode[]): boolean => {
          for (let i = 1; i < nodes.length; i++) {
            if (nodes[i].id === bulletId) {
              const node = nodes.splice(i, 1)[0];
              nodes[i - 1].children.push(node);
              return true;
            }
            if (indent(nodes[i].children)) return true;
          }
          return false;
        };

        if (indent(entry.content)) {
          this.saveResume();
          this.notify();
        }
        return;
      }
    }
  }

  outdentBullet(entryId: string, bulletId: string): void {
    this.pushUndo();

    for (const section of this.state.resume.sections) {
      const entry = section.entries.find(e => e.id === entryId);
      if (entry) {
        const outdent = (nodes: ContentNode[], parent?: ContentNode[], grandparent?: ContentNode[]): boolean => {
          for (let i = 0; i < nodes.length; i++) {
            if (nodes[i].id === bulletId && parent && grandparent) {
              const node = nodes.splice(i, 1)[0];
              const parentIndex = grandparent.indexOf(parent[0]);
              if (parentIndex >= 0) {
                grandparent.splice(parentIndex + 1, 0, node);
                return true;
              }
            }
            for (const childNode of nodes) {
              if (outdent(childNode.children, nodes, parent || entry.content as unknown as ContentNode[])) {
                return true;
              }
            }
          }
          return false;
        };

        // Special handling for top-level outdent
        const outdentFromParent = (parentNodes: ContentNode[]): boolean => {
          for (let p = 0; p < parentNodes.length; p++) {
            const children = parentNodes[p].children;
            for (let c = 0; c < children.length; c++) {
              if (children[c].id === bulletId) {
                const node = children.splice(c, 1)[0];
                parentNodes.splice(p + 1, 0, node);
                return true;
              }
              if (outdentFromParent(children)) return true;
            }
          }
          return false;
        };

        if (outdentFromParent(entry.content)) {
          this.saveResume();
          this.notify();
        }
        return;
      }
    }
  }

  moveBullet(entryId: string, bulletId: string, direction: 'up' | 'down'): void {
    this.pushUndo();

    for (const section of this.state.resume.sections) {
      const entry = section.entries.find(e => e.id === entryId);
      if (entry) {
        const move = (nodes: ContentNode[]): boolean => {
          for (let i = 0; i < nodes.length; i++) {
            if (nodes[i].id === bulletId) {
              const targetIndex = direction === 'up' ? i - 1 : i + 1;
              if (targetIndex >= 0 && targetIndex < nodes.length) {
                [nodes[i], nodes[targetIndex]] = [nodes[targetIndex], nodes[i]];
                return true;
              }
              return false;
            }
            if (move(nodes[i].children)) return true;
          }
          return false;
        };

        if (move(entry.content)) {
          this.saveResume();
          this.notify();
        }
        return;
      }
    }
  }

  addEntry(sectionId: string, afterEntryId?: string): string {
    this.pushUndo();
    const newEntry = createEntry();

    const section = this.state.resume.sections.find(s => s.id === sectionId);
    if (section) {
      if (afterEntryId) {
        const index = section.entries.findIndex(e => e.id === afterEntryId);
        if (index >= 0) {
          section.entries.splice(index + 1, 0, newEntry);
        } else {
          section.entries.push(newEntry);
        }
      } else {
        section.entries.push(newEntry);
      }
      this.saveResume();
      this.notify();
    }
    return newEntry.id;
  }

  addTemplatedEntry(sectionId: string, template: EntryTemplate): string {
    this.pushUndo();
    const newEntry = createTemplatedEntry(template);

    const section = this.state.resume.sections.find(s => s.id === sectionId);
    if (section) {
      section.entries.push(newEntry);
      this.saveResume();
      this.notify();
    }
    return newEntry.id;
  }

  deleteEntry(sectionId: string, entryId: string): void {
    this.pushUndo();

    const section = this.state.resume.sections.find(s => s.id === sectionId);
    if (section) {
      const index = section.entries.findIndex(e => e.id === entryId);
      if (index >= 0 && section.entries.length > 1) {
        section.entries.splice(index, 1);
        this.saveResume();
        this.notify();
      }
    }
  }

  duplicateEntry(sectionId: string, entryId: string): string | null {
    this.pushUndo();

    const section = this.state.resume.sections.find(s => s.id === sectionId);
    if (section) {
      const entry = section.entries.find(e => e.id === entryId);
      if (entry) {
        // Deep clone the entry with new IDs
        const cloneContent = (nodes: ContentNode[]): ContentNode[] => {
          return nodes.map(node => ({
            id: uuidv4(),
            text: node.text,
            children: cloneContent(node.children),
            collapsed: node.collapsed,
          }));
        };

        const newEntry: Entry = {
          id: uuidv4(),
          organization: entry.organization,
          role: entry.role,
          dateStart: entry.dateStart,
          dateEnd: entry.dateEnd,
          location: entry.location,
          content: cloneContent(entry.content),
        };

        // Insert after the original
        const index = section.entries.findIndex(e => e.id === entryId);
        section.entries.splice(index + 1, 0, newEntry);

        this.saveResume();
        this.notify();
        return newEntry.id;
      }
    }
    return null;
  }

  moveEntry(sectionId: string, entryId: string, direction: 'up' | 'down'): void {
    this.pushUndo();

    const section = this.state.resume.sections.find(s => s.id === sectionId);
    if (section) {
      const index = section.entries.findIndex(e => e.id === entryId);
      const targetIndex = direction === 'up' ? index - 1 : index + 1;
      if (index >= 0 && targetIndex >= 0 && targetIndex < section.entries.length) {
        [section.entries[index], section.entries[targetIndex]] =
          [section.entries[targetIndex], section.entries[index]];
        this.saveResume();
        this.notify();
      }
    }
  }

  addSection(type: Section['type'], title: string): string {
    this.pushUndo();
    const newSection = createSection(type, title);
    this.state.resume.sections.push(newSection);
    this.saveResume();
    this.notify();
    return newSection.id;
  }

  // Focus mode actions
  setFocusMode(mode: FocusMode): void {
    const configs: Record<FocusMode, ColumnConfig> = {
      'full-matrix': {
        employer: 'expanded',
        role: 'expanded',
        metadata: 'expanded',
        content: 'expanded',
      },
      'narrative': {
        employer: 'collapsed',
        role: 'collapsed',
        metadata: 'collapsed',
        content: 'expanded',
      },
      'timeline': {
        employer: 'expanded',
        role: 'expanded',
        metadata: 'expanded',
        content: 'collapsed',
      },
      'compact': {
        employer: 'expanded',
        role: 'expanded',
        metadata: 'expanded',
        content: 'expanded',
      },
    };

    this.state.focusMode = mode;
    this.state.columnConfig = configs[mode];
    this.notify();
  }

  toggleColumn(column: keyof ColumnConfig): void {
    const current = this.state.columnConfig[column];
    const next = current === 'expanded' ? 'collapsed' : 'expanded';
    this.state.columnConfig[column] = next;
    this.state.focusMode = 'full-matrix'; // Reset to custom
    this.notify();
  }

  // Selection actions
  setActiveEntry(entryId: string | null): void {
    this.state.activeEntryId = entryId;
    this.notify();
  }

  setActiveCell(cellType: EditorState['activeCellType']): void {
    this.state.activeCellType = cellType;
    this.notify();
  }

  setActiveBullet(bulletId: string | null): void {
    this.state.activeBulletId = bulletId;
    this.notify();
  }

  // Style actions
  updateStyleSettings(updates: Partial<StyleSettings>): void {
    this.state.styleSettings = {
      ...this.state.styleSettings,
      ...updates,
    };
    this.saveStyles();
    this.notify();
  }

  applyStylePreset(preset: 'classic' | 'modern' | 'minimal' | 'dense'): void {
    const presets: Record<string, Partial<StyleSettings>> = {
      classic: {
        typography: {
          primaryFont: 'Georgia, serif',
          headerFont: 'Georgia, serif',
          baseSize: 11,
          lineHeight: 1.5,
          nameScale: 2,
          sectionHeaderScale: 1.2,
        },
        spacing: {
          pageMargins: 1,
          sectionGap: 16,
          entryGap: 10,
          bulletIndent: 18,
          bulletSpacing: 5,
        },
      },
      modern: {
        typography: {
          primaryFont: 'Inter, system-ui, sans-serif',
          headerFont: 'Inter, system-ui, sans-serif',
          baseSize: 10,
          lineHeight: 1.4,
          nameScale: 2.2,
          sectionHeaderScale: 1.15,
        },
        spacing: {
          pageMargins: 0.6,
          sectionGap: 18,
          entryGap: 8,
          bulletIndent: 16,
          bulletSpacing: 4,
        },
      },
      minimal: {
        typography: {
          primaryFont: 'system-ui, sans-serif',
          headerFont: 'system-ui, sans-serif',
          baseSize: 10,
          lineHeight: 1.35,
          nameScale: 1.8,
          sectionHeaderScale: 1.1,
        },
        spacing: {
          pageMargins: 0.75,
          sectionGap: 12,
          entryGap: 6,
          bulletIndent: 14,
          bulletSpacing: 3,
        },
        layout: {
          datePosition: 'right' as const,
          locationPosition: 'with-date' as const,
          sectionDividers: 'none' as const,
          columnMode: 'single' as const,
        },
      },
      dense: {
        typography: {
          primaryFont: 'system-ui, sans-serif',
          headerFont: 'system-ui, sans-serif',
          baseSize: 9,
          lineHeight: 1.25,
          nameScale: 1.6,
          sectionHeaderScale: 1.1,
        },
        spacing: {
          pageMargins: 0.5,
          sectionGap: 10,
          entryGap: 5,
          bulletIndent: 12,
          bulletSpacing: 2,
        },
      },
    };

    const presetSettings = presets[preset];
    if (presetSettings) {
      this.state.styleSettings = {
        ...this.state.styleSettings,
        ...presetSettings,
        typography: { ...this.state.styleSettings.typography, ...presetSettings.typography },
        spacing: { ...this.state.styleSettings.spacing, ...presetSettings.spacing },
        layout: { ...this.state.styleSettings.layout, ...presetSettings.layout },
        colors: { ...this.state.styleSettings.colors, ...presetSettings.colors },
      };
      this.saveStyles();
      this.notify();
    }
  }

  // UI state actions
  toggleStyleStudio(): void {
    this.state.isStyleStudioOpen = !this.state.isStyleStudioOpen;
    this.notify();
  }

  togglePreview(): void {
    this.state.isPreviewVisible = !this.state.isPreviewVisible;
    this.notify();
  }

  // Undo/Redo
  undo(): void {
    if (this.state.undoStack.length > 0) {
      this.state.redoStack.push(JSON.parse(JSON.stringify(this.state.resume)));
      this.state.resume = this.state.undoStack.pop()!;
      this.saveResume();
      this.notify();
    }
  }

  redo(): void {
    if (this.state.redoStack.length > 0) {
      this.state.undoStack.push(JSON.parse(JSON.stringify(this.state.resume)));
      this.state.resume = this.state.redoStack.pop()!;
      this.saveResume();
      this.notify();
    }
  }

  // Reset
  resetToSample(): void {
    this.pushUndo();
    this.state.resume = createSampleResume();
    this.saveResume();
    this.notify();
  }

  newResume(): void {
    this.pushUndo();
    this.state.resume = createEmptyResume();
    this.saveResume();
    this.notify();
  }

  // Export resume as JSON
  exportJSON(): string {
    return JSON.stringify({
      resume: this.state.resume,
      styleSettings: this.state.styleSettings,
      exportedAt: new Date().toISOString(),
      version: '1.0',
    }, null, 2);
  }

  // Import resume from JSON
  importJSON(json: string): boolean {
    try {
      const data = JSON.parse(json);

      if (!data.resume || !data.resume.id || !data.resume.header || !data.resume.sections) {
        throw new Error('Invalid resume data format');
      }

      this.pushUndo();
      this.state.resume = data.resume;

      if (data.styleSettings) {
        this.state.styleSettings = {
          ...this.state.styleSettings,
          ...data.styleSettings,
        };
        this.saveStyles();
      }

      this.saveResume();
      this.notify();
      return true;
    } catch (error) {
      console.error('Import failed:', error);
      return false;
    }
  }

  // Subscribe to save events
  private saveListeners: Set<() => void> = new Set();

  onSave(listener: () => void): () => void {
    this.saveListeners.add(listener);
    return () => this.saveListeners.delete(listener);
  }

  private notifySave(): void {
    this.saveListeners.forEach(listener => listener());
  }
}

// Singleton instance
export const store = new Store();
