# Bridge Kit - Deploy Guide

How to update the live site **without Cursor**.

---

## One-time GitHub Pages setup

1. Push the `PVV` repo to GitHub (or create a dedicated `pvv-bridge-kit` repo with only the `bridge-kit/` folder).
2. In GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Push to `main`. The workflow `.github/workflows/bridge-kit-pages.yml` builds and deploys automatically.
4. Your site will be at `https://[username].github.io/[repo-name]/` (or a custom domain later).

If the repo is named `PVV`, Reach Page URL example:
`https://yourusername.github.io/PVV/reach/rosalie-rendu-center/`

---

## Daily workflow for PVV members

### Option A - Edit in Console, export, commit (recommended)

1. Open **`/console/`** on the deployed site (or run locally - see below).
2. Edit client info, checklist, calendar, Stanford pack.
3. Click **Export JSON**. Downloads `client-{slug}.json` and `kit-{slug}.json`.
4. Rename and place them:
   - `client-{slug}.json` → `bridge-kit/data/clients/{slug}.json`
   - `kit-{slug}.json` → `bridge-kit/data/kits/{slug}.json`
5. Commit and push to `main`:
   ```bash
   cd bridge-kit
   git add data/
   git commit -m "Update Rosalie Rendu Center Bridge Kit"
   git push
   ```
6. GitHub Actions redeploys in ~1–2 minutes.

### Option B - Edit JSON directly

1. Edit `bridge-kit/data/clients/[slug].json` for Reach Page content.
2. Edit `bridge-kit/data/kits/[slug].json` for checklist, calendar, liaison.
3. Push to `main`.

---

## Run locally (preview before push)

```bash
cd bridge-kit
npm run build      # generates ./site
npm run serve      # opens http://localhost:3456
```

Then visit:

- Hub: `http://localhost:3456/`
- Reach Page: `http://localhost:3456/reach/rosalie-rendu-center/`
- Console: `http://localhost:3456/console/`

Requires Node.js installed. No npm install needed (build uses Node built-ins only).

---

## Add a new client

1. Copy `data/clients/rosalie-rendu-center.json` → `data/clients/new-org-slug.json`
2. Copy `data/kits/rosalie-rendu-center.json` → `data/kits/new-org-slug.json`
3. Update slug, name, and all fields.
4. Add entry to `data/clients/index.json`:
   ```json
   { "slug": "new-org-slug", "name": "Org Name", "status": "active", "added": "2026-09-01" }
   ```
5. Push. Build creates `site/reach/new-org-slug/`.

---

## Handoff to nonprofit

Give the director:
1. **Reach Page URL** (their mobile sign-up hub)
2. **QR flyer PNG** (from Console → QR Flyer → Download)
3. **One-page guide:** "To update text, call your PVV liaison. After handoff, edit via [Google Sites if migrated] or contact us."

Keep volunteer sign-up on a **Google Form the client owns** - update `links.volunteerForm` in client JSON when ready.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Console says "Could not load data" | Run `npm run build` first; serve the `site/` folder, not `console/` alone |
| Reach Page looks old after edit | Did you push to `main`? Check Actions tab for deploy status |
| QR code blank | Wait for page load; QR library loads from CDN - needs internet |
| Wrong URL on QR | GitHub Pages base path - URL is auto-detected from browser location |

---

*PVV Bridge Kit v1.0*
