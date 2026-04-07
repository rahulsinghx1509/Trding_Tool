import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './lib/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        background: '#0b1020',
        surface: '#111831',
        accent: '#7c3aed',
        muted: '#94a3b8',
      },
      boxShadow: {
        soft: '0 20px 45px rgba(15, 23, 42, 0.25)',
      },
    },
  },
  plugins: [],
};

export default config;
