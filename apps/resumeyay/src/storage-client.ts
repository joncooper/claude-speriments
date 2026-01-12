/**
 * Storage Client for Git-Backed Server
 *
 * Provides a clean API for persisting workspace data with full version history.
 * Falls back to localStorage when server is unavailable.
 */

import type { ResumeWorkspace, ResumeWorkspaceV2 } from './types';

const DEFAULT_SERVER_URL = 'http://localhost:3001';

interface HistoryEntry {
  sha: string;
  message: string;
  date: string;
}

interface StorageClient {
  load(): Promise<ResumeWorkspaceV2 | null>;
  save(workspace: ResumeWorkspaceV2, message?: string): Promise<boolean>;
  getHistory(limit?: number): Promise<HistoryEntry[]>;
  getVersion(sha: string): Promise<ResumeWorkspaceV2 | null>;
  revert(sha: string): Promise<ResumeWorkspaceV2 | null>;
  isServerAvailable(): Promise<boolean>;
}

class GitStorageClient implements StorageClient {
  private serverUrl: string;
  private serverAvailable: boolean | null = null;
  private localStorageKey = 'resumeyay-workspace';

  constructor(serverUrl = DEFAULT_SERVER_URL) {
    this.serverUrl = serverUrl;
  }

  async isServerAvailable(): Promise<boolean> {
    if (this.serverAvailable !== null) {
      return this.serverAvailable;
    }

    try {
      const response = await fetch(`${this.serverUrl}/health`, {
        method: 'GET',
        signal: AbortSignal.timeout(2000),
      });
      this.serverAvailable = response.ok;
    } catch {
      this.serverAvailable = false;
    }

    return this.serverAvailable;
  }

  async load(): Promise<ResumeWorkspaceV2 | null> {
    // Try server first
    if (await this.isServerAvailable()) {
      try {
        const response = await fetch(`${this.serverUrl}/workspace`);
        if (response.ok) {
          const data = await response.json();
          // Also cache in localStorage as backup
          this.saveToLocalStorage(data);
          return this.migrateToV2(data);
        }
      } catch (error) {
        console.warn('Failed to load from server, falling back to localStorage:', error);
      }
    }

    // Fallback to localStorage
    return this.loadFromLocalStorage();
  }

  async save(workspace: ResumeWorkspaceV2, message?: string): Promise<boolean> {
    // Always save to localStorage as backup
    this.saveToLocalStorage(workspace);

    // Try server
    if (await this.isServerAvailable()) {
      try {
        const url = new URL(`${this.serverUrl}/workspace`);
        if (message) {
          url.searchParams.set('message', message);
        }

        const response = await fetch(url.toString(), {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(workspace),
        });

        return response.ok;
      } catch (error) {
        console.warn('Failed to save to server:', error);
        return false;
      }
    }

    return true; // Saved to localStorage
  }

  async getHistory(limit = 50): Promise<HistoryEntry[]> {
    if (!(await this.isServerAvailable())) {
      return [];
    }

    try {
      const response = await fetch(`${this.serverUrl}/history?limit=${limit}`);
      if (response.ok) {
        return await response.json();
      }
    } catch (error) {
      console.warn('Failed to get history:', error);
    }

    return [];
  }

  async getVersion(sha: string): Promise<ResumeWorkspaceV2 | null> {
    if (!(await this.isServerAvailable())) {
      return null;
    }

    try {
      const response = await fetch(`${this.serverUrl}/version/${sha}`);
      if (response.ok) {
        const data = await response.json();
        return this.migrateToV2(data);
      }
    } catch (error) {
      console.warn('Failed to get version:', error);
    }

    return null;
  }

  async revert(sha: string): Promise<ResumeWorkspaceV2 | null> {
    if (!(await this.isServerAvailable())) {
      return null;
    }

    try {
      const response = await fetch(`${this.serverUrl}/revert/${sha}`, {
        method: 'POST',
      });
      if (response.ok) {
        const data = await response.json();
        this.saveToLocalStorage(data);
        return this.migrateToV2(data);
      }
    } catch (error) {
      console.warn('Failed to revert:', error);
    }

    return null;
  }

  // Private methods

  private loadFromLocalStorage(): ResumeWorkspaceV2 | null {
    try {
      const stored = localStorage.getItem(this.localStorageKey);
      if (stored) {
        return this.migrateToV2(JSON.parse(stored));
      }
    } catch (error) {
      console.warn('Failed to load from localStorage:', error);
    }
    return null;
  }

  private saveToLocalStorage(workspace: ResumeWorkspace | ResumeWorkspaceV2): void {
    try {
      localStorage.setItem(this.localStorageKey, JSON.stringify(workspace));
    } catch (error) {
      console.warn('Failed to save to localStorage:', error);
    }
  }

  private migrateToV2(workspace: ResumeWorkspace | ResumeWorkspaceV2): ResumeWorkspaceV2 {
    // Check if already V2
    if ('fitSessions' in workspace) {
      return workspace as ResumeWorkspaceV2;
    }

    // Migrate V1 to V2
    return {
      ...workspace,
      fitSessions: [],
      activeFitSessionId: null,
      parsedJobDescriptions: [],
    };
  }
}

// Export singleton instance
export const storageClient = new GitStorageClient();

// Export class for custom configurations
export { GitStorageClient };
export type { StorageClient, HistoryEntry };
