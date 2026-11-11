# jacobintercom.com

Static website for Jacob Intercom (intercom repair and installation, New York).

## Build

    python3 build.py

No dependencies beyond Python 3. Output:

| Folder | What it is |
| --- | --- |
| `out/site` | Production site: indexed, Google Tag Manager on, redirects, sitemap |
| `out/staging` | Review copy: same pages, hidden from search engines, no tracking |
| `out/preview` | Copy with relative links, for the Claude preview |

## Editing

- `content.py`: all page text. `[[path/|text]]` links to another page; `[CAPITALS IN BRACKETS]` marks a fact still needed and renders highlighted.
- `build.py`: page template, header and footer, schema, profile links (`PROFILES`), redirects (`REDIRECTS`), image captions (`SHOTS`).
- `assets/site.css`, `assets/site.js`: styles, the buzzer-panel troubleshooter, cost estimators (prices in `REPAIR` and `INSTALL`).
- `assets/img/`: images.

## Deploy

Netlify builds from this repo using `netlify.toml`. For launch, set `publish = "out/site"` and add the domain in Netlify.
`out/site/_redirects` (Netlify, Cloudflare Pages) and `out/site/vercel.json` (Vercel) map the old WordPress URLs.

## Before launch

- Fill every highlighted `[PLACEHOLDER]`.
- Hold back neighborhood pages that don't have a real job yet.
- Connect the lead form (backend in Lovable).
- Add the Google Search Console verification tag.
