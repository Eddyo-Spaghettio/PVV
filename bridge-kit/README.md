# Bridge Kit

Tangible youth-engagement packages for PVV partner nonprofits.

## Quick links

| What | Where |
|------|--------|
| **Live site** (after deploy) | GitHub Pages - see [docs/DEPLOY.md](docs/DEPLOY.md) |
| **PVV Console** | `/console/` on deployed site |
| **Reach Page (pilot)** | `/reach/rosalie-rendu-center/` |
| **Deploy guide** | [docs/DEPLOY.md](docs/DEPLOY.md) |
| **Console guide** | [docs/CONSOLE-GUIDE.md](docs/CONSOLE-GUIDE.md) |

## Local development

```bash
npm run build   # generate site/ from data/
npm run serve   # preview at localhost:3456
```

## Structure

```
data/clients/     ← Reach Page content (one JSON per org)
data/kits/        ← PVV tracking: checklist, calendar, liaison, metrics
console/          ← PVV member admin UI (source)
scripts/build.js  ← builds static site/
site/             ← deploy output (GitHub Pages)
```

## Update workflow

1. Edit in Console (or edit JSON directly)
2. Export / commit to `data/`
3. Push to `main` → auto-deploy

No app server. No database. $0 hosting.
