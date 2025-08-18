# Repository Guidelines

This repo hosts vmMemory, a single‑file, vanilla‑JS memory game with no build step. Keep changes small, focused, and friendly to static hosting.

## Project Structure & Module Organization
- `index.html`: Entire app (HTML, CSS, JS inlined). `THEMES` defines symbol sets and game data.
- `assets/`: Game art and media.
  - `backgrounds/`, `backgrounds_png/`: SVG sources and raster exports.
  - `tiles/`, `tiles_png/`: SVG sources and raster exports.
  - `sounds/` (optional): Place copied audio here and update `<audio src>`.
- No modules/build system; keep logic in `index.html` and prefer small helpers.

## Build, Test, and Development Commands
- Serve locally: `python3 -m http.server 8000` → open `http://localhost:8000/`.
- Open directly: double‑click `index.html` (note: timing/storage can vary by browser).
- Deploy: any static host (e.g., GitHub Pages); site root is the repo root.

## Coding Style & Naming Conventions
- Indentation: 2 spaces. Use `const`/`let`, arrow functions, and early returns.
- JavaScript: ES2015+, no frameworks; keep functions small and single‑purpose.
- CSS: use existing CSS variables, grid layout, and tokenized radius/shadows; keep styles in `index.html` unless a clear split is warranted.
- Assets: lowercase, hyphenated names (e.g., `dinosaur.svg`, `thai.png`). Place new art in `assets/backgrounds/` or `assets/tiles/` and export to matching `_png/` folders.
- Accessibility: preserve ARIA attributes, visible focus rings, and full keyboard support.

## Testing Guidelines
- Framework: none. Perform manual checks before PRs:
  - All board sizes render; flips/matches update moves and time.
  - Theme switch works; 2‑player mode tracks turns and scores.
  - Keyboard: arrows navigate; Enter/Space flips.
  - `localStorage` best time saves per grid size.
- Optional: add browser tests later (e.g., Playwright) under `e2e/`.

## Commit & Pull Request Guidelines
- Commits: imperative, concise scope (e.g., `ui: improve focus ring on cards`).
- PRs: include summary, rationale, and screenshots or short clips for UI changes.
- List test steps and affected board sizes/themes; link issues.
- Keep diffs focused; avoid large binaries (>1MB); optimize images (prefer SVG).

## Security & Configuration Tips
- No secrets or server code. Avoid third‑party inline scripts.
- If external audio changes, copy files to `assets/sounds/` and update `<audio src>` references.
