# Proyecto Vidas Valiosas - Project Hub

Everything PVV needs to operate, train members, and deliver Bridge Kits to partner nonprofits. No Cursor required - open any file in a browser or Google Drive.

---

## Start Here

| If you need to... | Open this |
|-------------------|-----------|
| **Run Bridge Kit (Reach Pages + Console)** | [`bridge-kit/README.md`](bridge-kit/README.md) · [Deploy guide](bridge-kit/docs/DEPLOY.md) |
| Understand how the club runs | [`docs/operations-plan.md`](docs/operations-plan.md) |
| Learn what Bridge Kit is and pitch it | [`docs/bridge-kit-proposal.md`](docs/bridge-kit-proposal.md) |
| Revise the constitution | [`docs/constitution-2026-draft.md`](docs/constitution-2026-draft.md) |
| See the research behind our decisions | [`docs/research-notes.md`](docs/research-notes.md) |
| Onboard a new marketing member | [`training/interactive/marketing-workbook.html`](training/interactive/marketing-workbook.html) |
| Onboard a new financial member | [`training/interactive/financial-workbook.html`](training/interactive/financial-workbook.html) |
| Onboard a new technical member | [`training/interactive/technical-workbook.html`](training/interactive/technical-workbook.html) |

---

## Interactive Training (No Install Needed)

Three self-paced HTML workbooks. Open in any browser - Chrome, Safari, Firefox. Progress and exercises save automatically in the browser.

**To use during the school year:**
1. Upload the `training/interactive/` folder to PVV's shared Google Drive
2. Share the link with new members - they open the HTML file in their browser
3. Or host on Google Sites / GitHub Pages if you want a permanent URL

Each workbook has 3 modules (~45–60 min each), fill-in exercises, quick-check quizzes, and completion checklists.

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
├── README.md                          ← you are here
├── bridge-kit/                        ← Reach Pages + PVV Console (deploy via GitHub Pages)
├── .github/workflows/                 ← Pages deploy workflow
├── docs/
│   ├── operations-plan.md             ← how to keep the club running
│   ├── bridge-kit-proposal.md         ← youth engagement product proposal
│   ├── constitution-2026-draft.md   ← revised constitution
│   └── research-notes.md            ← evidence behind our decisions
├── training/
│   ├── interactive/
│   │   ├── marketing-workbook.html
│   │   ├── financial-workbook.html
│   │   └── technical-workbook.html
│   └── templates/                     ← CSV templates for projects
└── templates/
    └── bridge-kit/                    ← legacy client deliverable templates
```

---

## Key Contacts (Quick Reference)

| Who | Email | For |
|-----|-------|-----|
| Geoff Baker, Haas Center | glbaker@stanford.edu | SSO advising, transport grants, space |
| Edmund Dyer-Essig | edyeres@stanford.edu | PVV President |

Full contact list and resource breakdown: see `docs/operations-plan.md`.
