import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: true, // allows Vite to accept requests from any host
    // optional: explicitly allow your deployed host
    allowedHosts: ['notestask-frontend.onrender.com'],
  },
})