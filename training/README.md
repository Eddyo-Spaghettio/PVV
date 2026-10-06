# PVV Consultant Training

**Proyecto Vidas Valiosas** offers free, student-provided consulting to local nonprofits. Every new consultant completes one short training for their team before working with a client.

## The tracks

Each track is **6 modules and about one hour**, with videos and readings, short exercises, quick checks, and a capstone your category chair reviews. A short, optional **Feedback** module at the end collects ratings and suggestions.

| Track | For | Modules |
|-------|-----|---------|
| **Marketing** | Social media, flyers, promoting events to Stanford students | Your role, Goal and audience, Message and story, Design a flyer, Channels and Stanford promotion, Measure and hand off |
| **Financial** | Grant research and writing | Two doors of funding, Find funders, Anatomy of a proposal, Budgets, Letters of inquiry, Track and stay in scope |
| **Technical** | Websites, forms, data | Discovery, Reach Page, Forms and surveys, Data and spreadsheets, Accessibility, Security and handoff |

Start page: `https://YOUR-USERNAME.github.io/PVV/training/interactive/` (or open `training/interactive/index.html`). A readable list of every module and linked resource is in [CURRICULUM.md](CURRICULUM.md).

## How it works for members

1. Open your track and enter your name and email on the Start tab.
2. Work through the modules in any order. The links at the top of every page switch between the Marketing, Financial, and Technical tracks, and you stay signed in. Finished tracks are marked "(done)". Answers save automatically, and you can leave and come back on any device: enter the same email and you'll resume where you left off.
3. Submit your capstone link in module 6, then rate the training in the optional Feedback module and click **Mark training complete**.
4. Your category chair reviews the capstone. Their status and notes appear next to it the next time you open the workbook.
5. Then you're assigned a **shadow project** with a real client, supervised by your chair, before solo client work.

## How it works for chairs and officers

- **Progress and answers** arrive in a Google Sheet, with a Dashboard of completion, most-missed questions, and capstones waiting for review. One-time setup: [docs/SHEET-SETUP.md](docs/SHEET-SETUP.md).
- **Editing lessons** means editing a JSON file, no code needed: [docs/EDITING.md](docs/EDITING.md).

## Folder guide

```
training/
├── README.md              you are here
├── CURRICULUM.md          generated list of modules and linked resources
├── config.json            the Google Sheet connection (endpoint and key)
├── build.py               regenerates the workbooks from src/
├── src/                   lesson content (marketing/financial/technical.json) and page template
├── interactive/           the generated workbooks members open
├── backend/Code.gs        Google Apps Script that writes answers to the Sheet
├── docs/                  setup and editing guides
├── templates/             CSV templates used in the exercises
└── archive/               earlier quest-style documents and CSV trackers, kept for reference
```

## Before client work: ground rules

- **PVV students advise; clients decide.** We help draft, research, and build. Final submissions and financial decisions belong to the nonprofit's leadership.
- **Two funding worlds.** Club funding (Haas transportation and event grants, other Stanford sources) supports PVV's own operations. Client funding (foundation, government, and corporate grants) supports the nonprofit. Never mix them on an application.
- **No legal or tax advice.** Send 501(c)(3) and similar questions to the client's board or accountant.
- **Brand and ethics.** Get client approval before publishing anything in their name, and permission before sharing anyone's story or photo.
- **Privacy.** Use practice scenarios in the training. Never type real client details into a workbook.

*¡Vidas valiosas merecen herramientas excelentes!*
