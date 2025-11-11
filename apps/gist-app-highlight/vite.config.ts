import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  base: '/docs/sideshow/',
  build: {
    outDir: '../../docs/sideshow',
    emptyOutDir: true,
  },
})
