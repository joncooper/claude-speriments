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
  ResumeWorkspace,
  ResumeVariant,
  Snapshot,
  JobDescription,
  ResumeAnalysis,
  KeywordMatch,
  Suggestion,
} from './types';
import { DEFAULT_STYLE_SETTINGS } from './types';

// Local storage keys
const STORAGE_KEY = 'resumeyay_data';
const STYLE_KEY = 'resumeyay_styles';
const WORKSPACE_KEY = 'resumeyay_workspace';

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

// Create a sample resume for demo (Jon Cooper's resume)
export function createSampleResume(): Resume {
  return {
    id: uuidv4(),
    header: {
      name: 'Jon Cooper',
      email: 'jon.cooper@gmail.com',
      phone: '415.860.6238',
      location: 'Old Greenwich, CT',
      links: [
        { id: uuidv4(), label: 'LinkedIn', url: 'linkedin.com/in/joncooper3' },
      ],
    },
    sections: [
      {
        id: uuidv4(),
        type: 'custom',
        title: 'Summary',
        entries: [
          {
            id: uuidv4(),
            organization: '',
            role: '',
            dateStart: '',
            dateEnd: '',
            location: '',
            content: [
              {
                id: uuidv4(),
                text: '"Player-coach" technology leader with 20+ years of experience architecting, scaling, and securing high-performance infrastructure in demanding financial environments',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Proven success in leading teams through periods of intense growth and meeting escalating infrastructure demands',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Directly responsible for driving a firm\'s 14x AUM growth by writing its core automated investment platform in Go/Python on Linux',
                children: [],
              },
            ],
          },
        ],
      },
      {
        id: uuidv4(),
        type: 'experience',
        title: 'Selected Experience',
        entries: [
          {
            id: uuidv4(),
            organization: 'First Republic Bank (now JPMorgan Chase)',
            role: 'Head of Marketing Technology & Analytics Strategy',
            dateStart: '05/2022',
            dateEnd: '07/2024',
            location: 'New York, NY and San Francisco, CA',
            content: [
              {
                id: uuidv4(),
                text: 'Recognized for cross-functional executive leadership by CMO and CEO and internally recruited to join them in transforming the marketing department of 200+ ($100M+ opex) by uniting technology, data, and analytics',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Directly managed team of 50 ($25M opex budget) that owned critical infrastructure: the bank\'s website, intranet, client-facing email systems, campaign orchestration and analytics, privacy and fair lending tools, client communications preferences',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Turned around and revitalized the team, identifying and rallying underutilized talent into leadership and redirecting underperformers; saved its "deeply in the red" portfolio of complex, time-sensitive, regulatorily exposed initiatives; cut $10M+ run-rate while doing so',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Resolved acrimonious and counterproductive dynamics between marketing, data, IT, digital channels, and compliance departments, ultimately achieving a true partnership with aligned roadmaps and matrixed teams',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Moved to JPMorgan Chase on retention contract in 07/2023 as technical SME; hands-on-keyboard technical lead in the data/analytics related aspects of ensuring that the many client communications were correctly done, under intense time pressure and regulatory scrutiny',
                children: [],
              },
            ],
          },
          {
            id: uuidv4(),
            organization: 'First Republic Bank (now JPMorgan Chase)',
            role: 'Head of Applied Analytics',
            dateStart: '12/2018',
            dateEnd: '05/2022',
            location: 'New York, NY and San Francisco, CA',
            content: [
              {
                id: uuidv4(),
                text: 'Recruited by deputy COO to lead federated analytics teams (modeled on Goldman\'s "strats") serving executive, and functional leadership during rapid growth to $232B (30% CAGR)',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Built the bank\'s next-gen cloud analytics, data, and development environment by building, buying, deploying, and integrating best-in-class technologies including AWS, Snowflake, Beacon, dbt, Sigma, Alation, Fivetran',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Converged 10+ siloed analytics teams and 500+ users from local machines onto Beacon, offering them hosted VSCode, Jupyter notebooks, elastic DAG batch scheduling, container and task orchestration, lightweight GUI/data application frameworks, all on a shared Python monorepo and Docker registry',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Owned Beacon Platform with extensive hands-on enterprise architecture, DevOps/SRE, and development work; managed the deployment of the product into an air-gapped AWS VPC with enterprise security controls',
                children: [],
              },
            ],
          },
          {
            id: uuidv4(),
            organization: 'Colchis Capital Management',
            role: 'Chief Technical Officer',
            dateStart: '06/2013',
            dateEnd: '09/2018',
            location: 'San Francisco, CA',
            content: [
              {
                id: uuidv4(),
                text: 'Drove technology powering AUM growth from $100M to $1.4B AUM, personally architecting and coding our institutional grade high speed systematic investment system, dominating the peer-to-peer credit marketplace by achieving and sustaining 90% fill rates, purchasing 200,000 individual loans totaling >$2B',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Wrote proprietary DSL and interpreter enabling credit team to write selection criteria in simple language, backtest it against replayed traffic, validate its correctness, and then deploy to our colocated environment for high speed execution (<50ms P99 end-to-end)',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Built enterprise data and analytics infrastructure for credit teams: migrated analysts from desktop SAS and Box file sharing to server-based SAS with SQL Server data warehouse and Tableau frontend; personally architected, built, and operated underlying VMWare cluster with Nimble SAN and PCIe flash accelerator, delivering 40x performance improvement',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Created "single pane of glass" web application unifying the live trading system, backtesting and verification, portfolio management dashboards, risk and scenario analytics, infrastructure monitoring into a centralized command center for the firm',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Created and ran cybersecurity and DR/BCP programs as CISO, including SEC liaison and investor due diligence',
                children: [],
              },
            ],
          },
          {
            id: uuidv4(),
            organization: 'Deutsche Bank / Arrowgrass Capital',
            role: 'Head of US Convertible Proprietary Trading',
            dateStart: '06/2004',
            dateEnd: '11/2004',
            location: 'New York, NY and London, UK',
            content: [
              {
                id: uuidv4(),
                text: 'Ran $5B convertible bond book backing high volume flow desk and capital markets team',
                children: [],
              },
            ],
          },
          {
            id: uuidv4(),
            organization: 'Deutsche Bank / Arrowgrass Capital',
            role: 'Portfolio Manager, US & Japan',
            dateStart: '11/2004',
            dateEnd: '07/2008',
            location: 'New York, NY and London, UK',
            content: [
              {
                id: uuidv4(),
                text: 'Recruited to join global head of convertibles in a carve-out, relocating to London on 1 day\'s notice',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Ran multi-$B convertible, capital structure, cross-asset arbitrage books (credit, equity, rates, vol)',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Wrote and relied on my own tools, e.g. for credit curve trading, debt vs equity, short-end basis, event arb, puttable/callable high-grade bond arbitrage',
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
            organization: 'New College of Florida',
            role: 'B.A. Software/Social Context',
            dateStart: '',
            dateEnd: '',
            location: '',
            content: [
              {
                id: uuidv4(),
                text: 'New College is Florida\'s public liberal arts honors college',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Faculty-backed bespoke major combining mathematics, software engineering, sociology',
                children: [],
              },
            ],
          },
          {
            id: uuidv4(),
            organization: 'Sun Microsystems (JavaSoft)',
            role: 'Intern and Co-Op Student',
            dateStart: '1996',
            dateEnd: '2001',
            location: 'Cupertino, CA and Chelmsford, MA',
            content: [
              {
                id: uuidv4(),
                text: '4 internships, one co-op semester on the team (initially of 25) that invented Java',
                children: [],
              },
              {
                id: uuidv4(),
                text: 'Wrote keynote demos for 12,000 attendee JavaOne conference',
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

  // Reset state to defaults - for testing
  __test_reset__(): void {
    this.state = this.loadState();
    this.batchMode = false;
    this.batchStartSnapshot = null;
    this.listeners.clear();
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

// ============================================================================
// WORKSPACE & VARIANT MANAGEMENT
// ============================================================================

// Helper to extract all entry IDs from a resume
function getAllEntryIds(resume: Resume): string[] {
  const ids: string[] = [];
  for (const section of resume.sections) {
    for (const entry of section.entries) {
      ids.push(entry.id);
    }
  }
  return ids;
}

// Helper to extract all bullet IDs from a resume
function getAllBulletIds(resume: Resume): string[] {
  const ids: string[] = [];
  const collectBullets = (nodes: ContentNode[]) => {
    for (const node of nodes) {
      ids.push(node.id);
      collectBullets(node.children);
    }
  };
  for (const section of resume.sections) {
    for (const entry of section.entries) {
      collectBullets(entry.content);
    }
  }
  return ids;
}

// Create a default variant that includes everything
export function createDefaultVariant(resume: Resume): ResumeVariant {
  return {
    id: uuidv4(),
    name: 'Master Resume',
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
    includedEntryIds: getAllEntryIds(resume),
    includedBulletIds: getAllBulletIds(resume),
    snapshots: [],
    isDefault: true,
  };
}

// Create a new workspace from a resume
export function createWorkspace(resume: Resume): ResumeWorkspace {
  const defaultVariant = createDefaultVariant(resume);
  return {
    id: uuidv4(),
    contentPool: resume,
    variants: [defaultVariant],
    activeVariantId: defaultVariant.id,
    jobDescriptions: [],
    analyses: [],
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  };
}

// Extended state interface for internal use
interface ExtendedState extends EditorState {
  workspace: ResumeWorkspace;
  isVariantPanelOpen: boolean;
  isJobPanelOpen: boolean;
  isAnalysisPanelOpen: boolean;
  activeJobDescriptionId: string | null;
  activeAnalysisId: string | null;
}

class WorkspaceStore {
  private state: ExtendedState;
  private listeners: Set<Listener> = new Set();
  private saveListeners: Set<() => void> = new Set();

  constructor(baseStore: Store) {
    // Load existing state from base store
    const baseState = baseStore.getState();

    // Load or create workspace
    const savedWorkspace = localStorage.getItem(WORKSPACE_KEY);
    const workspace = savedWorkspace
      ? JSON.parse(savedWorkspace) as ResumeWorkspace
      : createWorkspace(baseState.resume);

    this.state = {
      ...baseState,
      resume: workspace.contentPool,
      workspace,
      isVariantPanelOpen: false,
      isJobPanelOpen: false,
      isAnalysisPanelOpen: false,
      activeJobDescriptionId: null,
      activeAnalysisId: null,
    };
  }

  getState(): ExtendedState {
    return this.state;
  }

  getWorkspace(): ResumeWorkspace {
    return this.state.workspace;
  }

  subscribe(listener: Listener): () => void {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  }

  private notify(): void {
    this.listeners.forEach(listener => listener());
  }

  private saveWorkspace(): void {
    localStorage.setItem(WORKSPACE_KEY, JSON.stringify(this.state.workspace));
    this.state.workspace.updatedAt = new Date().toISOString();
    this.notifySave();
  }

  onSave(listener: () => void): () => void {
    this.saveListeners.add(listener);
    return () => this.saveListeners.delete(listener);
  }

  private notifySave(): void {
    this.saveListeners.forEach(listener => listener());
  }

  // ============================================================================
  // VARIANT MANAGEMENT
  // ============================================================================

  getActiveVariant(): ResumeVariant | undefined {
    return this.state.workspace.variants.find(v => v.id === this.state.workspace.activeVariantId);
  }

  setActiveVariant(variantId: string): void {
    if (this.state.workspace.variants.some(v => v.id === variantId)) {
      this.state.workspace.activeVariantId = variantId;
      this.saveWorkspace();
      this.notify();
    }
  }

  createVariant(name: string, targetRole?: string, targetCompany?: string): string {
    const activeVariant = this.getActiveVariant();
    const newVariant: ResumeVariant = {
      id: uuidv4(),
      name,
      targetRole,
      targetCompany,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      includedEntryIds: activeVariant ? [...activeVariant.includedEntryIds] : getAllEntryIds(this.state.workspace.contentPool),
      includedBulletIds: activeVariant ? [...activeVariant.includedBulletIds] : getAllBulletIds(this.state.workspace.contentPool),
      snapshots: [],
    };
    this.state.workspace.variants.push(newVariant);
    this.state.workspace.activeVariantId = newVariant.id;
    this.saveWorkspace();
    this.notify();
    return newVariant.id;
  }

  duplicateVariant(variantId: string, newName?: string): string | null {
    const variant = this.state.workspace.variants.find(v => v.id === variantId);
    if (!variant) return null;

    const newVariant: ResumeVariant = {
      id: uuidv4(),
      name: newName || `${variant.name} (Copy)`,
      targetRole: variant.targetRole,
      targetCompany: variant.targetCompany,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      includedEntryIds: [...variant.includedEntryIds],
      includedBulletIds: [...variant.includedBulletIds],
      snapshots: [],
    };
    this.state.workspace.variants.push(newVariant);
    this.state.workspace.activeVariantId = newVariant.id;
    this.saveWorkspace();
    this.notify();
    return newVariant.id;
  }

  deleteVariant(variantId: string): void {
    const variant = this.state.workspace.variants.find(v => v.id === variantId);
    if (!variant || variant.isDefault) return; // Can't delete default

    const index = this.state.workspace.variants.indexOf(variant);
    this.state.workspace.variants.splice(index, 1);

    // Switch to another variant if deleting active
    if (this.state.workspace.activeVariantId === variantId) {
      this.state.workspace.activeVariantId = this.state.workspace.variants[0]?.id || '';
    }
    this.saveWorkspace();
    this.notify();
  }

  updateVariant(variantId: string, updates: Partial<Pick<ResumeVariant, 'name' | 'targetRole' | 'targetCompany'>>): void {
    const variant = this.state.workspace.variants.find(v => v.id === variantId);
    if (variant) {
      Object.assign(variant, updates, { updatedAt: new Date().toISOString() });
      this.saveWorkspace();
      this.notify();
    }
  }

  // Toggle entry inclusion in active variant
  toggleEntryInVariant(entryId: string): void {
    const variant = this.getActiveVariant();
    if (!variant || variant.isDefault) return;

    const index = variant.includedEntryIds.indexOf(entryId);
    if (index >= 0) {
      variant.includedEntryIds.splice(index, 1);
    } else {
      variant.includedEntryIds.push(entryId);
    }
    variant.updatedAt = new Date().toISOString();
    this.saveWorkspace();
    this.notify();
  }

  // Toggle bullet inclusion in active variant
  toggleBulletInVariant(bulletId: string): void {
    const variant = this.getActiveVariant();
    if (!variant || variant.isDefault) return;

    const index = variant.includedBulletIds.indexOf(bulletId);
    if (index >= 0) {
      variant.includedBulletIds.splice(index, 1);
    } else {
      variant.includedBulletIds.push(bulletId);
    }
    variant.updatedAt = new Date().toISOString();
    this.saveWorkspace();
    this.notify();
  }

  // Check if entry is included in active variant
  isEntryIncluded(entryId: string): boolean {
    const variant = this.getActiveVariant();
    return variant ? variant.includedEntryIds.includes(entryId) : true;
  }

  // Check if bullet is included in active variant
  isBulletIncluded(bulletId: string): boolean {
    const variant = this.getActiveVariant();
    return variant ? variant.includedBulletIds.includes(bulletId) : true;
  }

  // ============================================================================
  // SNAPSHOT MANAGEMENT
  // ============================================================================

  createSnapshot(variantId: string, name: string, notes?: string): string | null {
    const variant = this.state.workspace.variants.find(v => v.id === variantId);
    if (!variant) return null;

    const snapshot: Snapshot = {
      id: uuidv4(),
      name,
      createdAt: new Date().toISOString(),
      includedEntryIds: [...variant.includedEntryIds],
      includedBulletIds: [...variant.includedBulletIds],
      notes,
    };
    variant.snapshots.push(snapshot);
    variant.updatedAt = new Date().toISOString();
    this.saveWorkspace();
    this.notify();
    return snapshot.id;
  }

  restoreSnapshot(variantId: string, snapshotId: string): void {
    const variant = this.state.workspace.variants.find(v => v.id === variantId);
    if (!variant) return;

    const snapshot = variant.snapshots.find(s => s.id === snapshotId);
    if (!snapshot) return;

    variant.includedEntryIds = [...snapshot.includedEntryIds];
    variant.includedBulletIds = [...snapshot.includedBulletIds];
    variant.updatedAt = new Date().toISOString();
    this.saveWorkspace();
    this.notify();
  }

  deleteSnapshot(variantId: string, snapshotId: string): void {
    const variant = this.state.workspace.variants.find(v => v.id === variantId);
    if (!variant) return;

    const index = variant.snapshots.findIndex(s => s.id === snapshotId);
    if (index >= 0) {
      variant.snapshots.splice(index, 1);
      variant.updatedAt = new Date().toISOString();
      this.saveWorkspace();
      this.notify();
    }
  }

  // ============================================================================
  // JOB DESCRIPTION MANAGEMENT
  // ============================================================================

  addJobDescription(job: Omit<JobDescription, 'id' | 'createdAt'>): string {
    const newJob: JobDescription = {
      ...job,
      id: uuidv4(),
      createdAt: new Date().toISOString(),
    };
    this.state.workspace.jobDescriptions.push(newJob);
    this.state.activeJobDescriptionId = newJob.id;
    this.saveWorkspace();
    this.notify();
    return newJob.id;
  }

  updateJobDescription(jobId: string, updates: Partial<Omit<JobDescription, 'id' | 'createdAt'>>): void {
    const job = this.state.workspace.jobDescriptions.find(j => j.id === jobId);
    if (job) {
      Object.assign(job, updates);
      this.saveWorkspace();
      this.notify();
    }
  }

  deleteJobDescription(jobId: string): void {
    const index = this.state.workspace.jobDescriptions.findIndex(j => j.id === jobId);
    if (index >= 0) {
      this.state.workspace.jobDescriptions.splice(index, 1);
      if (this.state.activeJobDescriptionId === jobId) {
        this.state.activeJobDescriptionId = this.state.workspace.jobDescriptions[0]?.id || null;
      }
      this.saveWorkspace();
      this.notify();
    }
  }

  setActiveJobDescription(jobId: string | null): void {
    this.state.activeJobDescriptionId = jobId;
    this.notify();
  }

  // Extract keywords from job description text (basic implementation)
  extractKeywords(text: string): string[] {
    // Common tech/business keywords to look for
    const keywordPatterns = [
      // Technical skills
      /\b(python|javascript|typescript|java|go|golang|rust|c\+\+|ruby|scala)\b/gi,
      /\b(aws|azure|gcp|cloud|kubernetes|docker|terraform)\b/gi,
      /\b(react|vue|angular|node\.?js|django|flask|spring)\b/gi,
      /\b(sql|nosql|postgres|mysql|mongodb|redis|elasticsearch)\b/gi,
      /\b(machine learning|ml|ai|data science|analytics)\b/gi,
      /\b(agile|scrum|kanban|devops|ci\/cd|sre)\b/gi,
      // Leadership/soft skills
      /\b(leadership|management|strategy|cross-functional|executive)\b/gi,
      /\b(communication|collaboration|stakeholder|team)\b/gi,
      // Business domains
      /\b(fintech|finance|banking|trading|investment)\b/gi,
      /\b(saas|b2b|enterprise|startup|scale)\b/gi,
    ];

    const found = new Set<string>();
    for (const pattern of keywordPatterns) {
      const matches = text.match(pattern) || [];
      matches.forEach(m => found.add(m.toLowerCase()));
    }

    // Also extract capitalized multi-word phrases (potential proper nouns/tech names)
    const phrases = text.match(/[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+/g) || [];
    phrases.slice(0, 10).forEach(p => found.add(p.toLowerCase()));

    return Array.from(found);
  }

  // ============================================================================
  // LLM ANALYSIS (with mock for testing)
  // ============================================================================

  // Mock LLM analysis function - in production this would call an actual LLM API
  async analyzeResumeVsJob(
    variantId: string,
    jobId: string,
    _options?: { useMock?: boolean }
  ): Promise<ResumeAnalysis> {
    const variant = this.state.workspace.variants.find(v => v.id === variantId);
    const job = this.state.workspace.jobDescriptions.find(j => j.id === jobId);

    if (!variant || !job) {
      throw new Error('Variant or job description not found');
    }

    // For now, always use mock (in production, check options.useMock)
    const analysis = this.mockAnalysis(variant, job);

    // Store the analysis
    this.state.workspace.analyses.push(analysis);
    this.state.activeAnalysisId = analysis.id;
    this.saveWorkspace();
    this.notify();

    return analysis;
  }

  // Mock analysis for testing
  private mockAnalysis(variant: ResumeVariant, job: JobDescription): ResumeAnalysis {
    const contentPool = this.state.workspace.contentPool;
    const resumeText = this.getResumeText(variant);

    // Simple keyword matching
    const keywords = job.keywords.length > 0 ? job.keywords : this.extractKeywords(job.description);
    const keywordMatches: KeywordMatch[] = keywords.map(keyword => {
      const found = resumeText.toLowerCase().includes(keyword.toLowerCase());
      const inEntryIds: string[] = [];

      // Find which entries contain the keyword
      for (const section of contentPool.sections) {
        for (const entry of section.entries) {
          if (!variant.includedEntryIds.includes(entry.id)) continue;
          const entryText = `${entry.organization} ${entry.role} ${entry.content.map(c => c.text).join(' ')}`.toLowerCase();
          if (entryText.includes(keyword.toLowerCase())) {
            inEntryIds.push(entry.id);
          }
        }
      }

      return {
        keyword,
        found,
        inEntryIds,
        importance: this.determineKeywordImportance(keyword, job.description) as 'high' | 'medium' | 'low',
      };
    });

    // Calculate score based on keyword matches
    const matchedCount = keywordMatches.filter(k => k.found).length;
    const highPriorityMatched = keywordMatches.filter(k => k.found && k.importance === 'high').length;
    const highPriorityTotal = keywordMatches.filter(k => k.importance === 'high').length;

    const baseScore = keywords.length > 0 ? (matchedCount / keywords.length) * 70 : 50;
    const highPriorityBonus = highPriorityTotal > 0 ? (highPriorityMatched / highPriorityTotal) * 30 : 15;
    const overallScore = Math.round(baseScore + highPriorityBonus);

    // Generate mock suggestions
    const suggestions: Suggestion[] = [];
    const missingKeywords = keywordMatches.filter(k => !k.found && k.importance === 'high');

    for (const missing of missingKeywords.slice(0, 3)) {
      suggestions.push({
        id: uuidv4(),
        type: 'add',
        reason: `Consider adding experience or skills related to "${missing.keyword}" as it appears to be important for this role.`,
        priority: 'high',
      });
    }

    // Find strong points
    const strongPoints: string[] = [];
    const matchedHighPriority = keywordMatches.filter(k => k.found && k.importance === 'high');
    for (const match of matchedHighPriority.slice(0, 3)) {
      strongPoints.push(`Strong ${match.keyword} experience matches job requirements`);
    }

    // Find missing skills
    const missingSkills = missingKeywords.map(k => k.keyword);

    return {
      id: uuidv4(),
      variantId: variant.id,
      jobDescriptionId: job.id,
      createdAt: new Date().toISOString(),
      overallScore,
      keywordMatches,
      suggestions,
      missingSkills,
      strongPoints,
    };
  }

  private getResumeText(variant: ResumeVariant): string {
    const contentPool = this.state.workspace.contentPool;
    const parts: string[] = [
      contentPool.header.name,
      contentPool.header.location,
    ];

    for (const section of contentPool.sections) {
      parts.push(section.title);
      for (const entry of section.entries) {
        if (!variant.includedEntryIds.includes(entry.id)) continue;
        parts.push(entry.organization, entry.role, entry.location);
        const collectText = (nodes: ContentNode[]) => {
          for (const node of nodes) {
            if (variant.includedBulletIds.includes(node.id)) {
              parts.push(node.text);
            }
            collectText(node.children);
          }
        };
        collectText(entry.content);
      }
    }

    return parts.join(' ');
  }

  private determineKeywordImportance(keyword: string, jobText: string): string {
    const lowerJob = jobText.toLowerCase();
    const lowerKeyword = keyword.toLowerCase();

    // Count occurrences
    const count = (lowerJob.match(new RegExp(lowerKeyword, 'g')) || []).length;

    // Check if in requirements section (simple heuristic)
    const requirementsSection = lowerJob.includes('requirements') || lowerJob.includes('qualifications');
    const inRequirements = requirementsSection && lowerJob.indexOf(lowerKeyword) > lowerJob.indexOf('requirements');

    if (count >= 3 || inRequirements) return 'high';
    if (count >= 2) return 'medium';
    return 'low';
  }

  getActiveAnalysis(): ResumeAnalysis | null {
    if (!this.state.activeAnalysisId) return null;
    return this.state.workspace.analyses.find(a => a.id === this.state.activeAnalysisId) || null;
  }

  setActiveAnalysis(analysisId: string | null): void {
    this.state.activeAnalysisId = analysisId;
    this.notify();
  }

  applySuggestion(analysisId: string, suggestionId: string): void {
    const analysis = this.state.workspace.analyses.find(a => a.id === analysisId);
    if (!analysis) return;

    const suggestion = analysis.suggestions.find(s => s.id === suggestionId);
    if (!suggestion) return;

    suggestion.applied = true;
    this.saveWorkspace();
    this.notify();
  }

  // ============================================================================
  // UI STATE
  // ============================================================================

  toggleVariantPanel(): void {
    this.state.isVariantPanelOpen = !this.state.isVariantPanelOpen;
    this.notify();
  }

  toggleJobPanel(): void {
    this.state.isJobPanelOpen = !this.state.isJobPanelOpen;
    this.notify();
  }

  toggleAnalysisPanel(): void {
    this.state.isAnalysisPanelOpen = !this.state.isAnalysisPanelOpen;
    this.notify();
  }

  // Sync content pool changes back to workspace
  syncContentPool(resume: Resume): void {
    this.state.workspace.contentPool = resume;
    this.state.resume = resume;

    // Update all variants to include any new entries/bullets
    const allEntryIds = getAllEntryIds(resume);
    const allBulletIds = getAllBulletIds(resume);

    for (const variant of this.state.workspace.variants) {
      if (variant.isDefault) {
        // Default variant always includes everything
        variant.includedEntryIds = allEntryIds;
        variant.includedBulletIds = allBulletIds;
      } else {
        // Remove deleted entries/bullets from other variants
        variant.includedEntryIds = variant.includedEntryIds.filter(id => allEntryIds.includes(id));
        variant.includedBulletIds = variant.includedBulletIds.filter(id => allBulletIds.includes(id));
      }
    }

    this.saveWorkspace();
    this.notify();
  }
}

// Singleton instances
export const store = new Store();
export const workspaceStore = new WorkspaceStore(store);

// Re-export for backward compatibility
export { WorkspaceStore, type ExtendedState };
