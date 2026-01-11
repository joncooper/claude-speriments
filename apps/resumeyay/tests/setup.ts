/**
 * Test Setup - Configures happy-dom for DOM testing
 */
import { GlobalRegistrator } from '@happy-dom/global-registrator';

// Register happy-dom globals (window, document, etc.)
GlobalRegistrator.register();

// Mock localStorage
const localStorageMock = (() => {
  let store: Record<string, string> = {};
  return {
    getItem: (key: string) => store[key] ?? null,
    setItem: (key: string, value: string) => {
      store[key] = value;
    },
    removeItem: (key: string) => {
      delete store[key];
    },
    clear: () => {
      store = {};
    },
    get length() {
      return Object.keys(store).length;
    },
    key: (index: number) => Object.keys(store)[index] ?? null,
  };
})();

Object.defineProperty(globalThis, 'localStorage', {
  value: localStorageMock,
  writable: true,
});

// Mock confirm dialog (always returns true in tests)
Object.defineProperty(globalThis, 'confirm', {
  value: () => true,
  writable: true,
});

// Mock alert (no-op in tests)
Object.defineProperty(globalThis, 'alert', {
  value: () => {},
  writable: true,
});

// Export for use in tests
export { localStorageMock };

// Helper to reset localStorage between tests
export function resetLocalStorage() {
  localStorageMock.clear();
}

// Helper to create a fresh store instance
export async function createFreshStore() {
  // Clear localStorage first
  resetLocalStorage();

  // Dynamically import to get a fresh instance
  // We need to clear the module cache
  const storeModule = await import('../src/store');
  return storeModule;
}
