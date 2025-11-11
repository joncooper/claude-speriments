/**
 * Markdown rendering utilities
 */

import { marked } from 'marked';
import DOMPurify from 'dompurify';
import type { Gist } from './models';

/**
 * Configure marked.js
 */
marked.setOptions({
  breaks: true,
  gfm: true,
});

/**
 * Render markdown to sanitized HTML
 */
export function renderMarkdown(markdown: string): string {
  const rawHtml = marked.parse(markdown) as string;
  return DOMPurify.sanitize(rawHtml);
}

/**
 * Apply highlights to rendered HTML
 *
 * This wraps highlighted text in <mark> elements with unique IDs
 */
export function applyHighlights(html: string, highlights: Gist['highlights']): string {
  // Create a temporary container to work with the DOM
  const container = document.createElement('div');
  container.innerHTML = html;

  // Sort highlights by start offset (apply from end to start to maintain offsets)
  const sortedHighlights = [...highlights].sort((a, b) => b.startOffset - a.startOffset);

  // Get all text content
  const textContent = container.textContent || '';

  // Apply each highlight
  for (const highlight of sortedHighlights) {
    try {
      applyHighlight(container, highlight, textContent);
    } catch (error) {
      console.error('Failed to apply highlight:', highlight.id, error);
    }
  }

  return container.innerHTML;
}

/**
 * Apply a single highlight to the container
 */
function applyHighlight(
  container: HTMLElement,
  highlight: Gist['highlights'][0],
  fullText: string
): void {
  const { startOffset, endOffset, id, color, selectedText } = highlight;

  // Verify the text still matches
  const actualText = fullText.substring(startOffset, endOffset);
  if (actualText !== selectedText) {
    console.warn(`Highlight text mismatch for ${id}. Expected: "${selectedText}", Got: "${actualText}"`);
    // Still try to apply it
  }

  // Find the text node and offset
  const startNode = findNodeAtOffset(container, startOffset);
  const endNode = findNodeAtOffset(container, endOffset);

  if (!startNode || !endNode) {
    console.error('Could not find nodes for highlight:', id);
    return;
  }

  // Create a range
  const range = document.createRange();
  range.setStart(startNode.node, startNode.offset);
  range.setEnd(endNode.node, endNode.offset);

  // Create the mark element
  const mark = document.createElement('mark');
  mark.id = `highlight-${id}`;
  mark.className = 'highlight';
  mark.dataset.highlightId = id;
  if (color) {
    mark.style.backgroundColor = color;
  }

  // Wrap the range in the mark
  try {
    range.surroundContents(mark);
  } catch (error) {
    // If surroundContents fails (e.g., range spans multiple elements),
    // extract the contents and wrap them
    const contents = range.extractContents();
    mark.appendChild(contents);
    range.insertNode(mark);
  }
}

/**
 * Find a text node at a specific character offset
 */
function findNodeAtOffset(
  container: HTMLElement,
  targetOffset: number
): { node: Node; offset: number } | null {
  let currentOffset = 0;

  function traverse(node: Node): { node: Node; offset: number } | null {
    if (node.nodeType === Node.TEXT_NODE) {
      const textLength = node.textContent?.length || 0;
      if (currentOffset + textLength >= targetOffset) {
        return {
          node,
          offset: targetOffset - currentOffset,
        };
      }
      currentOffset += textLength;
    } else if (node.nodeType === Node.ELEMENT_NODE) {
      for (const child of Array.from(node.childNodes)) {
        const result = traverse(child);
        if (result) return result;
      }
    }
    return null;
  }

  return traverse(container);
}

/**
 * Get the character offset of a position in the rendered HTML
 */
export function getCharacterOffset(container: HTMLElement, node: Node, offset: number): number {
  let currentOffset = 0;

  function traverse(currentNode: Node): number | null {
    if (currentNode === node) {
      return currentOffset + offset;
    }

    if (currentNode.nodeType === Node.TEXT_NODE) {
      currentOffset += currentNode.textContent?.length || 0;
    } else if (currentNode.nodeType === Node.ELEMENT_NODE) {
      for (const child of Array.from(currentNode.childNodes)) {
        const result = traverse(child);
        if (result !== null) return result;
      }
    }

    return null;
  }

  const result = traverse(container);
  return result !== null ? result : -1;
}

/**
 * Extract title from markdown (first H1 or first line)
 */
export function extractTitle(markdown: string): string {
  // Try to find an H1
  const h1Match = markdown.match(/^#\s+(.+)$/m);
  if (h1Match) {
    return h1Match[1].trim();
  }

  // Fall back to first non-empty line
  const firstLine = markdown.split('\n').find(line => line.trim().length > 0);
  if (firstLine) {
    // Trim to reasonable length
    return firstLine.trim().substring(0, 100);
  }

  return 'Untitled';
}
