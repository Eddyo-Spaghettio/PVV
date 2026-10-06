# Proyecto Vidas Valiosas - Project Hub

Everything PVV needs to operate, train members, and deliver Bridge Kits to partner nonprofits. No Cursor required - open any file in a browser or Google Drive.

---

## Start Here

| If you need to... | Open this |
|-------------------|-----------|
| **Run Bridge Kit (Reach Pages + Console)** | [`bridge-kit/README.md`](bridge-kit/README.md) · [Deploy guide](bridge-kit/docs/DEPLOY.md) |
| Understand how the club runs | [`docs/operations-plan.md`](docs/operations-plan.md) |
| Learn what Bridge Kit is and pitch it | [`docs/bridge-kit-proposal.md`](docs/bridge-kit-proposal.md) |
| Read the constitution | [`docs/constitution.md`](docs/constitution.md) |
| See the research behind our decisions | [`docs/research-notes.md`](docs/research-notes.md) |
| Onboard a new marketing member | [`training/interactive/marketing-workbook.html`](training/interactive/marketing-workbook.html) |
| Onboard a new financial member | [`training/interactive/financial-workbook.html`](training/interactive/financial-workbook.html) |
| Onboard a new technical member | [`training/interactive/technical-workbook.html`](training/interactive/technical-workbook.html) |

---

## Interactive Training (No Install Needed)

Three self-paced workbooks - Marketing, Financial, Technical. Each is **6 modules and about one hour**, with videos and readings, exercises, quick checks, and a capstone reviewed by your category chair. Open in any browser (Chrome, Safari, Firefox).

- **Members:** open your track from the table above. Enter your name and email, and your answers save automatically. You can resume on any device.
- **Chairs and officers:** answers and progress flow into a Google Sheet with a dashboard. One-time setup: [`training/docs/SHEET-SETUP.md`](training/docs/SHEET-SETUP.md).
- **Editing lessons:** [`training/docs/EDITING.md`](training/docs/EDITING.md).
- **Overview and ground rules:** [`training/README.md`](training/README.md).

Live URL (GitHub Pages serves this repo from `main`): `https://eddyo-spaghettio.github.io/PVV/training/interactive/`

---

## Bridge Kit (Live System)

Implemented in **`bridge-kit/`** - not just templates.

| Component | Path |
|-----------|------|
| PVV Console (team admin) | `bridge-kit/site/console/` after build |
| Pilot Reach Page | `bridge-kit/site/reach/rosalie-rendu-center/` |
| Client data | `bridge-kit/data/clients/` |
| Deploy to GitHub Pages | [bridge-kit/docs/DEPLOY.md](bridge-kit/docs/DEPLOY.md) |

```bash
cd bridge-kit && npm run build && npm run serve
# → http://localhost:3456/console/
```

Legacy copy-paste templates still in `templates/bridge-kit/` if needed.

---

## Folder Structure

```
PVV/
├── README.md                          <- you are here
├── bridge-kit/                        <- Reach Pages + PVV Console
│   └── site/                          <- generated, but committed ON PURPOSE: GitHub Pages serves from main
├── docs/                              <- operations plan, proposal, constitution, research
├── training/                          <- consultant training (see training/README.md)
│   ├── src/                           <- lesson content (JSON) and page template
│   ├── interactive/                   <- generated workbooks members open
│   ├── backend/Code.gs                <- Google Apps Script for the tracker sheet
│   ├── docs/                          <- SHEET-SETUP.md, EDITING.md
│   ├── templates/                     <- CSV templates used in exercises
│   └── archive/                       <- earlier quest docs and CSV trackers
├── templates/bridge-kit/              <- legacy client deliverable templates
├── scripts/wordpress/                 <- one-off WordPress site scripts
└── .github/workflows/                 <- Bridge Kit deploy, training rebuild
```

---

## Key Contacts (Quick Reference)

| Who | Email | For |
|-----|-------|-----|
| Geoff Baker, Haas Center | glbaker@stanford.edu | SSO advising, transport grants, space |
| Edmund Dyer-Essig | edyeres@stanford.edu | PVV President |

Full contact list and resource breakdown: see `docs/operations-plan.md`.
