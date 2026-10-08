# vxMemory

A minimalist, single‑file memory game built with vanilla JavaScript, HTML, and CSS. No build tools, no dependencies — just open and play.

## Features
- Multiple board sizes (up to 10×10).
- Themes: Classic, Animals, Foods, Shapes, Thai, Dinosaur.
- Solo or 2‑player hot‑seat mode with turn/score tracking.
- Accessible: keyboard navigation, ARIA live updates, visible focus.
- Best time stored per grid size via `localStorage`.

## Getting Started
- Quick open: double‑click `index.html` (behavior may vary by browser).
- Local server: `python3 -m http.server 8000` then visit `http://localhost:8000/`.
- Deploy: any static host (e.g., GitHub Pages). Site root is the repo root.

## Controls
- Arrows: move focus between cards.
- Enter/Space: flip card.
- Buttons: Restart or start a New Game from the side panel.

## Project Structure
- `index.html`: Entire app (HTML/CSS/JS inlined). `THEMES` defines symbol sets and game data.
- `assets/`: Game art/media.
  - `backgrounds/`, `backgrounds_png/`: SVG sources and raster exports.
  - `tiles/`, `tiles_png/`: SVG sources and raster exports.
  - `sounds/` (optional): add local audio and update `<audio src>` in `index.html`.

## Contributing
See `AGENTS.md` for coding style, testing checks, and PR guidelines. Keep changes small, focused, and framework‑free.

## License
- Code and original graphics: GPL‑3.0‑or‑later. See `LICENSE`.
- External audio is hotlinked from actions.google.com/sounds and is not included in this repo.

## Copyright
© 2025 Vionix Consulting. vxMemory is free software released under the GNU GPL v3.0 or later.

## Publisher attribution

The public product name is vxMemory. Existing cookie and best-score storage keys retain their identifiers so saved preferences and scores remain available. The control panel links to [Vionix Consulting](https://vionix.cloud) with a locally bundled publisher logo. About opens a native English/Thai dialog with purpose, source repository, issue tracker, GPL code license, and asset notices. Escape and Close dismiss the dialog and restore focus to About. The attribution area groups compact About/Support actions. Support is also available inside About and opens an English/Thai native dialog with the official Ko-fi Tip Panel for [Vionix Consulting](https://ko-fi.com/vionixconsulting). Optional one-time/monthly contributions support this and other free Vionix projects without game privileges. The iframe loads only on click, sends no game state or referrer, and is removed on close. The close area stays visible while the panel scrolls; checkout sits flush beneath a compact header without repeated explanatory copy. A ten-second loading delay reveals a new-tab recovery link. Opening from About closes About first and returns focus to its persistent trigger. Game state, timers, preferences and saved-score keys remain unchanged. Ko-fi controls payment UI/configuration; frame events never confirm payment completion. Actual monthly/payment behavior depends on account configuration and provider availability; delayed embeds can use the external recovery link.
