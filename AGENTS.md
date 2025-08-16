# Repository Guidelines

## Project Structure & Module Organization
- Root `index.html`: Single-file app (HTML/CSS/JS inlined). No build step.
- `assets/`: Game art.
  - `backgrounds/` and `tiles/`: SVG sources; `_png/` folders contain raster exports.
- Game data: symbol sets live in the `THEMES` object inside `index.html`.

## Build, Test, and Development Commands
- Serve locally (recommended for `localStorage` and audio):
  - `python3 -m http.server 8000` then open `http://localhost:8000/`.
- Open directly: double-click `index.html` (works, but timing/storage may vary across browsers).
- Deploy: any static host (e.g., GitHub Pages) — site root is the repo root.

## Coding Style & Naming Conventions
- Indentation: 2 spaces. Keep functions small and single‑purpose.
- JavaScript: vanilla ES2015+; prefer `const`/`let`, arrow functions, and early returns. No frameworks.
- CSS: use existing CSS variables, box‑shadow/radius tokens, and grid layout; keep styles in `index.html` unless a clear split is warranted.
- Assets: use lowercase, hyphenated names (e.g., `dinosaur.svg`, `thai.png`). Place new art in `assets/backgrounds/` or `assets/tiles/` and export to matching `_png/` if needed.
- Accessibility: preserve ARIA attributes, focus states, and keyboard support.

## Testing Guidelines
- Framework: none currently. Run manual checks before PRs:
  - All board sizes render; flips/matches update moves and time.
  - Theme switch works; 2‑player mode tracks turns and scores.
  - Keyboard: arrows navigate; Enter/Space flips.
  - `localStorage` best time saves per grid size.
- Optional: add browser tests (e.g., Playwright) under `e2e/` with a lightweight script and GitHub Actions later.

## Commit & Pull Request Guidelines
- Commits: imperative mood, concise scope (e.g., `ui: improve focus ring on cards`).
- PRs: include summary, rationale, and screenshots or short clips for UI changes; list test steps and affected board sizes/themes; link issues when applicable.
- Keep diffs focused; avoid large binary assets (>1MB). Optimize images (SVG preferred).

## Security & Configuration Tips
- No secrets or server code. Avoid third‑party inline scripts. If external audio becomes unavailable, copy files into `assets/sounds/` and update `<audio src>` references.
