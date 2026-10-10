# vxMemory

A minimalist, single‑file memory game built with vanilla JavaScript, HTML, and CSS. No build tools — open and play. The optional donation dialog uses a locally bundled QR encoder.

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

The public product name is vxMemory. Existing cookie and best-score storage keys retain their identifiers so saved preferences and scores remain available. The complete control-panel identity links to [Vionix Consulting](https://vionix.cloud), with the bundled logo centred beside the product/publisher text. About opens a native English/Thai dialog with a fixed close header, identity/purpose, icon-led source/issue resources, separate GPL code licence/asset notices and a copyright/Support footer. Escape and Close dismiss the dialog and restore focus to About. The attribution area groups icon-labelled About/Support actions in equal-width columns. Support is also available inside About and opens an English/Thai native dialog with the official Ko-fi Tip Panel for [Vionix Consulting](https://ko-fi.com/vionixconsulting). Optional one-time/monthly contributions support this and other free Vionix projects without game privileges. The iframe loads only on click, sends no game state or referrer, and is removed on close. The close area stays visible while the panel scrolls; the compact iframe sits within symmetric responsive margins beneath the fixed header without repeated explanatory copy. A ten-second loading delay reveals a new-tab recovery link. Opening from About closes About first and returns focus to its persistent trigger. Game state, timers, preferences and saved-score keys remain unchanged. Native focus restoration is backed by explicit originating-button focus; delayed close events do not steal focus from a newly selected control. Ko-fi owns its internal card layout and payment UI/configuration; the app centres the iframe box, and frame events never confirm payment completion. Actual monthly/payment behavior depends on account configuration and provider availability; delayed embeds can use the external recovery link.


## Usage-based support reminders

Completed games, including two-player games, count once toward a local, optional reminder. Its first cycle requires three completed games, activity on three distinct local dates and 72 elapsed hours since the first completion. Later cycles require three new completions and 28 elapsed days since a reminder or Support interaction; games completed during cooldown count. Showing a reminder consumes the cycle. Not now restarts the cooldown; Don’t remind me disables automatic reminders for this app/browser. Manual Support restarts cooldown without re-enabling reminders. Reload clears the session card without repeating its consumed cycle. Scores and existing cookie preferences retain their behavior.

The English/Thai card has three 44px actions, polite announcement and no auto-hide or focus movement. It waits for fact/win dialogs to close, suspends during renewed board interaction and resumes at a safe boundary. Its position clears visible attribution controls. Existing boards, game timers and progression remain active. Only selecting Support opens the donation dialog; Ko-fi remains its default method; closing payment returns focus to the persistent Support control.

The local policy/controller lives inside index.html without dependencies or backend integration. A versioned vxMemory.support-reminders storage record holds bounded usage/date history, first-use time, cooldown and opt-out. App-specific Web Locks serialize writes and foreground presentation claims across tabs. Corrupt/unavailable storage or missing coordination disables automatic reminders; manual Support remains available. Usage is never reconstructed from scores, shared across apps or included in app data.

Verification uses deterministic injected clock/storage/lock tests and the workspace browser harness, outside shipped app code. Cover timing/date boundaries, repeat counts, concurrency, opt-out/manual interactions, completed solo/two-player games, deferred dialogs, active gameplay, reload silence and intercepted payment frames. Review English/Thai themes at 320/390/768/1440px and enlarged text, retaining keyboard matching/new-game checks.

Run the local policy suite with `node --test tests/support-reminder-policy.test.mjs`. Browser verification uses the workspace harness with intercepted payment/audio fixtures; machine-specific browser imports stay outside this repository.

`tests/crypto-support.browser.mjs` exports `verifyCryptoSupport` for that harness. Supply a Playwright page, local URL, app name, locale, viewport width and an independent QR decoder. It covers all eight destinations, method switching, clipboard recovery, keyboard controls, compact layouts, close/reopen cleanup and preserved game state.

## Crypto support

Support offers Ko-fi/Crypto tabs with Ko-fi selected on every opening. Switching methods preserves the mounted checkout and selected network; closing removes both. Crypto uses one persistent icon selector ordered Bitcoin, Ethereum Mainnet, Solana, Base, Arbitrum One, Optimism, Polygon PoS and BNB Smart Chain, with uniform rows and keyboard arrows/Home/End/typeahead, Enter/Space selection, Escape cancellation and outside dismissal. Public receiving addresses are maintained by the wallet owner. Asset captions are familiar, nonexclusive hints: BTC for Bitcoin; otherwise the native asset, USDC, USDT and other tokens, including Solana. Show a full selectable address, a primary Copy address action and a local address-only 180px QR. The concise panel has no network-instruction footer. Use 24px desktop/16px mobile outer padding, 16px section gaps, 4px receiving-label/address grouping and 12px before Copy. Reserve two address lines at widths up to 480px. QR starts behind Show QR code at widths up to 420px or heights up to 720px. Only successful clipboard completion shows Copied for two seconds; live feedback takes no layout space. Failed copy selects the address and offers manual recovery. Network changes discard stale clipboard results; new attempts, changes and close clear the feedback timer. Crypto performs no wallet connection, transfer, balance lookup or payment confirmation. English/Thai labels follow the existing game language. Wallet addresses and crypto UI stay in the existing game script; games, timers, scores and reminder policy are unchanged.

The static host serves `assets/vendor/qrcode-generator.js` (qrcode-generator 2.0.4, Kazuhiko Arase, MIT). The complete notice is in `assets/vendor/qrcode-generator.LICENSE`; no build step, remote QR service or additional runtime origin is required. Include these local assets when publishing the site.
