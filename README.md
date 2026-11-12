# MD Nexa

Source of the MD Nexa studio site, published with GitHub Pages at https://mdnexa9.github.io/ .

The site lists the studio's Android apps and games, has a contact section (WhatsApp and email), and serves `app-ads.txt` from the domain root for AdMob verification.

## Files

- `index.html` — the single page (Arabic by default, English toggle), apps and games tabs, contact cards.
- `styles.css` — styling, dark navy theme with the cyan-to-violet gradient.
- `app.js` — language switch, tabs, contact links, and the "coming soon" notice shown when a game card is tapped.
- `app-ads.txt` — AdMob seller record, must stay at the repository root so Pages serves it at `/app-ads.txt`.
- `assets/` — logo, favicon, star field backdrop and product icons.

## Editing

The WhatsApp number and email live in the `CONTACT` object at the top of `app.js`. The games are marked with `data-soon` on their cards; replace a card with a normal link to `https://play.google.com/store/apps/details?id=...` once that game is published.

## Contact

- WhatsApp: +39 376 144 3811
- Email: mdnexa9@gmail.com
