/**
 * Client-side routing
 */

import type { Route } from './models';

/**
 * Parse the current URL hash into a Route
 */
export function parseRoute(): Route {
  const hash = window.location.hash.slice(1); // Remove leading #

  if (!hash || hash === '/' || hash === '') {
    return { type: 'home' };
  }

  if (hash === '/create') {
    return { type: 'create' };
  }

  if (hash.startsWith('/edit/')) {
    const gistId = hash.slice(6);
    return { type: 'edit', gistId };
  }

  if (hash.startsWith('/')) {
    // Assume it's a gist ID
    const gistId = hash.slice(1);
    return { type: 'view', gistId };
  }

  // Default to home
  return { type: 'home' };
}

/**
 * Navigate to a route
 */
export function navigateTo(route: Route): void {
  switch (route.type) {
    case 'home':
      window.location.hash = '#/';
      break;
    case 'create':
      window.location.hash = '#/create';
      break;
    case 'edit':
      window.location.hash = `#/edit/${route.gistId}`;
      break;
    case 'view':
      window.location.hash = `#/${route.gistId}`;
      break;
  }
}

/**
 * Listen to route changes
 */
export function onRouteChange(callback: (route: Route) => void): () => void {
  const handler = () => {
    callback(parseRoute());
  };

  window.addEventListener('hashchange', handler);

  // Return cleanup function
  return () => {
    window.removeEventListener('hashchange', handler);
  };
}

/**
 * Get shareable URL for a gist
 */
export function getShareableUrl(gistId: string): string {
  const base = window.location.origin + window.location.pathname;
  return `${base}#/${gistId}`;
}
