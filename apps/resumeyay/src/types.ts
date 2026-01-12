// Resume Data Types following the PRD specification

export interface Link {
  id: string;
  label: string;
  url: string;
}

export interface Header {
  name: string;
  email: string;
  phone: string;
  location: string;
  links: Link[];
}

export interface ContentNode {
  id: string;
  text: string;
  children: ContentNode[];
  collapsed?: boolean;
}

export type SectionType = 'experience' | 'education' | 'projects' | 'skills' | 'custom';

export interface Entry {
  id: string;
  organization: string;
  role: string;
  dateStart: string;
  dateEnd: string; // "Present" or date string
  location: string;
  content: ContentNode[];
}

export interface Section {
  id: string;
  type: SectionType;
  title: string;
  entries: Entry[];
}

export interface Resume {
  id: string;
  header: Header;
  sections: Section[];
  createdAt: string;
  updatedAt: string;
}

// Focus Mode Types
export type FocusMode = 'full-matrix' | 'narrative' | 'timeline' | 'compact';

export type ColumnState = 'expanded' | 'collapsed' | 'hidden';

export interface ColumnConfig {
  employer: ColumnState;
  role: ColumnState;
  metadata: ColumnState;
  content: ColumnState;
}

export const FOCUS_MODE_CONFIGS: Record<FocusMode, ColumnConfig> = {
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

// Style Studio Types
export interface TypographySettings {
  primaryFont: string;
  headerFont: string;
  baseSize: number; // in pt
  lineHeight: number;
  nameScale: number;
  sectionHeaderScale: number;
}

export interface SpacingSettings {
  pageMargins: number; // in inches
  sectionGap: number; // in pt
  entryGap: number; // in pt
  bulletIndent: number; // in pt
  bulletSpacing: number; // in pt
}

export interface LayoutSettings {
  datePosition: 'right' | 'inline';
  locationPosition: 'with-date' | 'below';
  sectionDividers: 'none' | 'line' | 'double' | 'dots';
  columnMode: 'single' | 'two-column';
}

export interface ColorSettings {
  textColor: string;
  accentColor: string;
  dividerColor: string;
  linkColor: string;
}

export interface StyleSettings {
  typography: TypographySettings;
  spacing: SpacingSettings;
  layout: LayoutSettings;
  colors: ColorSettings;
}

export type StylePreset = 'classic' | 'modern' | 'minimal' | 'dense';

export const DEFAULT_STYLE_SETTINGS: StyleSettings = {
  typography: {
    primaryFont: 'Inter, system-ui, sans-serif',
    headerFont: 'Inter, system-ui, sans-serif',
    baseSize: 10,
    lineHeight: 1.4,
    nameScale: 2,
    sectionHeaderScale: 1.2,
  },
  spacing: {
    pageMargins: 0.75,
    sectionGap: 14,
    entryGap: 8,
    bulletIndent: 16,
    bulletSpacing: 4,
  },
  layout: {
    datePosition: 'right',
    locationPosition: 'with-date',
    sectionDividers: 'line',
    columnMode: 'single',
  },
  colors: {
    textColor: '#1A1A1A',
    accentColor: '#2563EB',
    dividerColor: '#E5E5E5',
    linkColor: '#2563EB',
  },
};

export const STYLE_PRESETS: Record<StylePreset, Partial<StyleSettings>> = {
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
      datePosition: 'right',
      locationPosition: 'with-date',
      sectionDividers: 'none',
      columnMode: 'single',
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

// Editor State Types
export interface EditorState {
  resume: Resume;
  focusMode: FocusMode;
  columnConfig: ColumnConfig;
  styleSettings: StyleSettings;
  activeEntryId: string | null;
  activeCellType: 'employer' | 'role' | 'metadata' | 'content' | null;
  activeBulletId: string | null;
  isStyleStudioOpen: boolean;
  isPreviewVisible: boolean;
  undoStack: Resume[];
  redoStack: Resume[];
}

// Cell Position for navigation
export interface CellPosition {
  sectionIndex: number;
  entryIndex: number;
  column: 'employer' | 'role' | 'metadata' | 'content';
  bulletIndex?: number;
}

// ============================================================================
// RESUME DNA - Variant System Types
// ============================================================================

/**
 * A Snapshot is a point-in-time save of a variant's configuration.
 * Useful for versioning different iterations of a resume variant.
 */
export interface Snapshot {
  id: string;
  name: string;
  createdAt: string;
  includedEntryIds: string[];  // Which entries from content pool are included
  includedBulletIds: string[]; // Which bullets within entries are included
  notes?: string;
}

/**
 * A Variant is a configuration of the resume content pool for a specific purpose.
 * For example: "Tech Lead at FAANG" vs "Engineering Manager at Startup"
 */
export interface ResumeVariant {
  id: string;
  name: string;
  targetRole?: string;
  targetCompany?: string;
  createdAt: string;
  updatedAt: string;
  includedEntryIds: string[];  // Which entries from content pool are included
  includedBulletIds: string[]; // Which bullets within entries are included
  snapshots: Snapshot[];
  isDefault?: boolean;
}

/**
 * A Job Description for targeting the resume.
 */
export interface JobDescription {
  id: string;
  title: string;
  company: string;
  description: string;
  requirements: string[];
  keywords: string[];
  url?: string;
  createdAt: string;
}

/**
 * Analysis result from LLM evaluation of resume vs job description.
 */
export interface ResumeAnalysis {
  id: string;
  variantId: string;
  jobDescriptionId: string;
  createdAt: string;
  overallScore: number; // 0-100
  keywordMatches: KeywordMatch[];
  suggestions: Suggestion[];
  missingSkills: string[];
  strongPoints: string[];
}

export interface KeywordMatch {
  keyword: string;
  found: boolean;
  inEntryIds: string[];
  importance: 'high' | 'medium' | 'low';
}

export interface Suggestion {
  id: string;
  type: 'add' | 'modify' | 'remove' | 'reorder';
  targetEntryId?: string;
  targetBulletId?: string;
  currentText?: string;
  suggestedText?: string;
  reason: string;
  priority: 'high' | 'medium' | 'low';
  applied?: boolean;
}

/**
 * The Resume Workspace contains the content pool and all variants.
 * This is the new top-level data structure.
 */
export interface ResumeWorkspace {
  id: string;
  contentPool: Resume;           // Master content (all entries/bullets)
  variants: ResumeVariant[];     // Different configurations of the content
  activeVariantId: string;       // Currently selected variant
  jobDescriptions: JobDescription[];
  analyses: ResumeAnalysis[];
  createdAt: string;
  updatedAt: string;
}

// Extended EditorState to support variants
export interface EditorStateV2 extends EditorState {
  workspace: ResumeWorkspace;
  isVariantPanelOpen: boolean;
  isJobPanelOpen: boolean;
  isAnalysisPanelOpen: boolean;
  activeJobDescriptionId: string | null;
  activeAnalysisId: string | null;
}

// ============================================================================
// FIT COACH - LLM-Assisted Resume Refinement
// ============================================================================

/**
 * A parsed requirement from a job description.
 * Tracks coverage status against the resume content.
 */
export interface JDRequirement {
  id: string;
  text: string;
  category: 'required' | 'preferred' | 'nice-to-have';
  keywords: string[];
  matchedBulletIds: string[];  // Bullets that address this requirement
  matchedEntryIds: string[];   // Entries that address this requirement
  coverageStatus: 'strong' | 'partial' | 'missing' | 'not-me';
  userNotes?: string;          // User's notes about this requirement
  notMeReason?: string;        // Why user marked this as "not me"
}

/**
 * A message in the Fit Coach conversation.
 */
export interface FitCoachMessage {
  id: string;
  role: 'coach' | 'user';
  content: string;
  timestamp: string;
  relatedRequirementId?: string;  // If discussing a specific requirement
  suggestedBullets?: string[];    // Coach-suggested bullet points
}

/**
 * A Fit Session tracks the iterative refinement process
 * for matching a resume variant to a job description.
 */
export interface FitSession {
  id: string;
  jobDescriptionId: string;
  variantId: string;
  requirements: JDRequirement[];
  conversationHistory: FitCoachMessage[];
  overallFitScore: number;       // 0-100, calculated from requirement coverage
  coverageBreakdown: {
    strong: number;
    partial: number;
    missing: number;
    notMe: number;
  };
  createdAt: string;
  updatedAt: string;
  isActive: boolean;
}

/**
 * Heat map data for highlighting keywords in the preview.
 */
export interface HeatMapHighlight {
  bulletId: string;
  keywords: string[];
  matchStrength: 'high' | 'medium' | 'low';
  requirementIds: string[];      // Which requirements this bullet addresses
}

/**
 * Parsed job description with structured requirements.
 */
export interface ParsedJobDescription {
  id: string;
  originalJobDescriptionId: string;
  title: string;
  company: string;
  requirements: JDRequirement[];
  parsedAt: string;
  rawText: string;
}

/**
 * Extended workspace to include Fit Coach sessions.
 */
export interface ResumeWorkspaceV2 extends ResumeWorkspace {
  fitSessions: FitSession[];
  activeFitSessionId: string | null;
  parsedJobDescriptions: ParsedJobDescription[];
}

/**
 * Extended editor state for Fit Coach mode.
 */
export interface EditorStateV3 extends EditorStateV2 {
  workspaceV2: ResumeWorkspaceV2;
  isFitCoachOpen: boolean;
  heatMapHighlights: HeatMapHighlight[];
  showHeatMap: boolean;
}
