/**
 * Highlight selection and management
 */

import { nanoid } from 'nanoid';
import { getCharacterOffset } from './markdown';
import type { Gist } from './models';

export interface SelectionInfo {
  startOffset: number;
  endOffset: number;
  selectedText: string;
}

/**
 * Get current text selection info
 */
export function getSelectionInfo(container: HTMLElement): SelectionInfo | null {
  const selection = window.getSelection();

  if (!selection || selection.isCollapsed || selection.rangeCount === 0) {
    return null;
  }

  const range = selection.getRangeAt(0);

  // Make sure selection is within our container
  if (!container.contains(range.commonAncestorContainer)) {
    return null;
  }

  const selectedText = range.toString().trim();
  if (!selectedText) {
    return null;
  }

  // Get character offsets
  const startOffset = getCharacterOffset(container, range.startContainer, range.startOffset);
  const endOffset = getCharacterOffset(container, range.endContainer, range.endOffset);

  if (startOffset === -1 || endOffset === -1) {
    console.error('Could not calculate offsets for selection');
    return null;
  }

  return {
    startOffset,
    endOffset,
    selectedText,
  };
}

/**
 * Create a new highlight from selection
 */
export function createHighlight(
  selectionInfo: SelectionInfo,
  annotation: string,
  color?: string
): Gist['highlights'][0] {
  return {
    id: nanoid(),
    startOffset: selectionInfo.startOffset,
    endOffset: selectionInfo.endOffset,
    selectedText: selectionInfo.selectedText,
    annotation,
    color: color || '#ffeb3b',
    createdAt: new Date(),
  };
}

/**
 * Clear current text selection
 */
export function clearSelection(): void {
  const selection = window.getSelection();
  if (selection) {
    selection.removeAllRanges();
  }
}

/**
 * Setup highlight click handlers
 */
export function setupHighlightClickHandlers(
  container: HTMLElement,
  onHighlightClick: (highlightId: string) => void
): () => void {
  const handleClick = (event: MouseEvent) => {
    const target = event.target as HTMLElement;
    const highlight = target.closest('[data-highlight-id]') as HTMLElement;

    if (highlight) {
      const highlightId = highlight.dataset.highlightId;
      if (highlightId) {
        event.preventDefault();
        onHighlightClick(highlightId);
      }
    }
  };

  container.addEventListener('click', handleClick);

  // Return cleanup function
  return () => {
    container.removeEventListener('click', handleClick);
  };
}

/**
 * Scroll highlight into view
 */
export function scrollToHighlight(highlightId: string): void {
  const element = document.getElementById(`highlight-${highlightId}`);
  if (element) {
    element.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
}

/**
 * Highlight a specific highlight (add visual emphasis)
 */
export function emphasizeHighlight(highlightId: string): void {
  // Remove emphasis from all highlights
  document.querySelectorAll('.highlight').forEach(el => {
    el.classList.remove('emphasized');
  });

  // Add emphasis to target highlight
  const element = document.getElementById(`highlight-${highlightId}`);
  if (element) {
    element.classList.add('emphasized');
  }
}

/**
 * Get default highlight colors
 */
export const HIGHLIGHT_COLORS = [
  { name: 'Yellow', value: '#ffeb3b' },
  { name: 'Green', value: '#c8e6c9' },
  { name: 'Blue', value: '#bbdefb' },
  { name: 'Pink', value: '#f8bbd0' },
  { name: 'Orange', value: '#ffe0b2' },
  { name: 'Purple', value: '#e1bee7' },
];
