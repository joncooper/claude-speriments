/**
 * Firestore database operations
 */

import {
  collection,
  doc,
  getDoc,
  setDoc,
  updateDoc,
  deleteDoc,
  query,
  where,
  getDocs,
  orderBy,
  limit,
} from 'firebase/firestore';
import { nanoid } from 'nanoid';
import { db } from './firebase';
import type { Gist, GistDocument } from './models';
import { docToGist, gistToDoc } from './models';

const GISTS_COLLECTION = 'gists';

/**
 * Generate a short ID for a gist (8 characters)
 */
export function generateShortId(): string {
  return nanoid(8);
}

/**
 * Check if a gist ID already exists
 */
export async function gistExists(id: string): Promise<boolean> {
  const docRef = doc(db, GISTS_COLLECTION, id);
  const docSnap = await getDoc(docRef);
  return docSnap.exists();
}

/**
 * Generate a unique short ID (checks for collisions)
 */
export async function generateUniqueId(): Promise<string> {
  let id = generateShortId();
  let attempts = 0;
  const maxAttempts = 10;

  while (await gistExists(id)) {
    if (attempts++ > maxAttempts) {
      throw new Error('Failed to generate unique ID after multiple attempts');
    }
    id = generateShortId();
  }

  return id;
}

/**
 * Create a new gist
 */
export async function createGist(
  markdown: string,
  userId: string,
  title?: string
): Promise<Gist> {
  const id = await generateUniqueId();
  const now = new Date();

  const gist: Gist = {
    id,
    markdown,
    createdBy: userId,
    createdAt: now,
    updatedAt: now,
    highlights: [],
    title,
  };

  const docRef = doc(db, GISTS_COLLECTION, id);
  await setDoc(docRef, gistToDoc(gist));

  return gist;
}

/**
 * Get a gist by ID
 */
export async function getGist(id: string): Promise<Gist | null> {
  const docRef = doc(db, GISTS_COLLECTION, id);
  const docSnap = await getDoc(docRef);

  if (!docSnap.exists()) {
    return null;
  }

  return docToGist(docSnap.data() as GistDocument);
}

/**
 * Update a gist
 */
export async function updateGist(gist: Gist): Promise<void> {
  const docRef = doc(db, GISTS_COLLECTION, gist.id);
  const updatedGist = {
    ...gist,
    updatedAt: new Date(),
  };

  await updateDoc(docRef, gistToDoc(updatedGist) as any);
}

/**
 * Delete a gist
 */
export async function deleteGist(id: string): Promise<void> {
  const docRef = doc(db, GISTS_COLLECTION, id);
  await deleteDoc(docRef);
}

/**
 * Get all gists created by a user
 */
export async function getUserGists(userId: string, maxResults = 50): Promise<Gist[]> {
  const q = query(
    collection(db, GISTS_COLLECTION),
    where('createdBy', '==', userId),
    orderBy('updatedAt', 'desc'),
    limit(maxResults)
  );

  const querySnapshot = await getDocs(q);
  return querySnapshot.docs.map(doc => docToGist(doc.data() as GistDocument));
}

/**
 * Add or update a highlight in a gist
 */
export async function saveHighlight(
  gistId: string,
  highlight: Gist['highlights'][0]
): Promise<void> {
  const gist = await getGist(gistId);
  if (!gist) {
    throw new Error(`Gist ${gistId} not found`);
  }

  // Remove existing highlight with same ID if it exists
  const highlights = gist.highlights.filter(h => h.id !== highlight.id);
  highlights.push(highlight);

  gist.highlights = highlights;
  await updateGist(gist);
}

/**
 * Delete a highlight from a gist
 */
export async function deleteHighlight(gistId: string, highlightId: string): Promise<void> {
  const gist = await getGist(gistId);
  if (!gist) {
    throw new Error(`Gist ${gistId} not found`);
  }

  gist.highlights = gist.highlights.filter(h => h.id !== highlightId);
  await updateGist(gist);
}
