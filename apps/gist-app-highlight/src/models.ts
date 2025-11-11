/**
 * Data models for Sideshow
 */

import { Timestamp } from 'firebase/firestore';

/**
 * A highlight represents a selected portion of text with an annotation
 */
export interface Highlight {
  /** Unique identifier for the highlight */
  id: string;

  /** Character offset in the rendered HTML where highlight starts */
  startOffset: number;

  /** Character offset in the rendered HTML where highlight ends */
  endOffset: number;

  /** The actual text that was highlighted (for verification) */
  selectedText: string;

  /** The annotation/sidenote content (supports markdown) */
  annotation: string;

  /** Optional color for the highlight (hex code) */
  color?: string;

  /** When the highlight was created */
  createdAt: Date;
}

/**
 * A gist represents a markdown document with highlights and annotations
 */
export interface Gist {
  /** Short ID for URL sharing (e.g., "aB3xK9mQ") */
  id: string;

  /** Raw markdown content */
  markdown: string;

  /** Firebase user ID of the creator */
  createdBy: string;

  /** When the gist was created */
  createdAt: Date;

  /** When the gist was last updated */
  updatedAt: Date;

  /** Array of highlights with annotations */
  highlights: Highlight[];

  /** Optional title (extracted from first H1 or user-provided) */
  title?: string;
}

/**
 * Firestore document representation (uses Timestamp instead of Date)
 */
export interface GistDocument {
  id: string;
  markdown: string;
  createdBy: string;
  createdAt: Timestamp;
  updatedAt: Timestamp;
  highlights: HighlightDocument[];
  title?: string;
}

export interface HighlightDocument {
  id: string;
  startOffset: number;
  endOffset: number;
  selectedText: string;
  annotation: string;
  color?: string;
  createdAt: Timestamp;
}

/**
 * Convert Firestore document to Gist
 */
export function docToGist(doc: GistDocument): Gist {
  return {
    ...doc,
    createdAt: doc.createdAt.toDate(),
    updatedAt: doc.updatedAt.toDate(),
    highlights: doc.highlights.map(h => ({
      ...h,
      createdAt: h.createdAt.toDate(),
    })),
  };
}

/**
 * Convert Gist to Firestore document
 */
export function gistToDoc(gist: Gist): GistDocument {
  return {
    ...gist,
    createdAt: Timestamp.fromDate(gist.createdAt),
    updatedAt: Timestamp.fromDate(gist.updatedAt),
    highlights: gist.highlights.map(h => ({
      ...h,
      createdAt: Timestamp.fromDate(h.createdAt),
    })),
  };
}

/**
 * User state for the application
 */
export interface User {
  uid: string;
  email: string | null;
  displayName: string | null;
  photoURL: string | null;
}

/**
 * Application view modes
 */
export type ViewMode = 'edit' | 'preview';

/**
 * Application state
 */
export interface AppState {
  user: User | null;
  gist: Gist | null;
  viewMode: ViewMode;
  isOwner: boolean;
  selectedHighlightId: string | null;
}

/**
 * Application routes
 */
export type Route =
  | { type: 'home' }
  | { type: 'create' }
  | { type: 'edit', gistId: string }
  | { type: 'view', gistId: string };
