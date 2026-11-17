/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.html", "!./node_modules/**"],
  theme: {
    extend: {
      colors: {
        accent: {
          DEFAULT: "#3aa0ff",
          cyan: "#00e5ff",
          hover: "#2563eb",
          dim: "rgba(59,130,246,0.1)",
          strong: "#0757b5",
        },
        "accent-cyan": "#00e5ff",
        "accent-strong": "#0757b5",
        dark: { DEFAULT: "#0a0e1a", card: "#111827" },
        "dark-card": "#111827",
        bg: { DEFAULT: "#0f172a", card: "#1e293b", hover: "#334155" },
        ok: "#22c55e",
        warn: "#f59e0b",
        bad: "#ef4444",
        muted: "#64748b",
        edge: "#334155",
        navy: {
          DEFAULT: "#0a2a4a",
          900: "#0a0f1a",
          800: "#111827",
          700: "#1a2332",
          600: "#243044",
        },
        gold: {
          400: "#d4a843",
          500: "#c9952c",
          600: "#b07f1e",
          700: "#956b18",
        },
        ink: "#071a2b",
        ocean: "#0b4b82",
        sky: "#3aa0ff",
        mist: "#f5f7fb",
      },
      fontFamily: {
        display: ["Space Grotesk", "sans-serif"],
        body: ["Inter", "sans-serif"],
        sans: ["Inter", "system-ui", "sans-serif"],
      },
      boxShadow: {
        soft: "0 10px 30px rgba(7, 26, 43, 0.12)",
      },
    },
  },
  plugins: [],
};
