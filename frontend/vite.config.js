import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',  // Adjust this path as needed
    emptyOutDir: true,
  },
  server: {
    proxy: {
      '/api': 'http://localhost:8000',  // Proxy API requests to Django
    },
  },
});