# PVV Console - Quick Guide

The Console is where PVV members build and track Bridge Kits. Nonprofits don't use this - they get the finished Reach Page link.

**URL (after deploy):** `[your-site]/console/`

---

## Tabs

### Overview - **Kit Progress** - check off the 7 Bridge Kit deliverables as you complete them. - **Assigned Liaison** - assign the PVV member responsible for this client this quarter. - **Metrics** - update monthly (page visits, sign-ups, event attendance, posts published).

### Edit Client - Change all Reach Page content: mission, colors, links, programs, impact stat. - Changes preview instantly in the Preview tab. - **Volunteer form URL:** When you create a Google Form for the client, paste it here - it overrides the generic volunteer page link on the Reach Page.

### Preview - Mobile-style preview of the Reach Page before publishing.

### QR Flyer - Auto-generated flyer with org name, impact line, and QR code pointing to the Reach Page. - **Download Flyer PNG** → print at Haas or FedEx.

### Stanford Pack - Pre-written **service4all** email and **CardinalEngage** event copy. - Replace `[LIAISON NAME]` by filling in Overview → Assigned Liaison. - **Copy email to clipboard** → send to Haas contact or post via service4all process.

### Calendar - 12 weeks of pre-written social posts for the client. - Edit drafts inline. Check **Done** when posted. - **Export CSV** → share with liaison or client.

---

## Saving your work

The Console **auto-saves drafts in your browser** (localStorage). That survives refresh but not a different computer.

To update the **live site for everyone:**

1. Click **Export JSON**
2. Commit files to `bridge-kit/data/` in the GitHub repo
3. Push to `main`

See [DEPLOY.md](./DEPLOY.md) for full steps.

---

## Roles

| Who | Does what in Console |
|-----|---------------------|
| **Marketing chair / liaison** | Calendar, Stanford pack, QR flyer |
| **Technical chair** | Edit Client (links, Reach Page content) |
| **Outreach** | Liaison assignment, metrics, checklist |
| **Any member** | Overview checklist, preview |

---

## Pilot client

**Rosalie Rendu Center** - ESL and family programs, East Palo Alto.  
Reach Page promotes volunteer conversation partners + links to their existing donate/volunteer pages.

After deploy, share Reach Page URL with Sister T / Maria Lozano (executive director) for approval before printing QR flyers.

---

## Client workload and long-term support

Bridge Kit is meant to **replace** tasks clients already struggle with (flyers, sign-up friction, social posts), not add a new role for the director.

| Client does | PVV / Assigned Liaison does |
|-------------|----------------------------|
| ~45 min kickoff call | Builds Reach Page, QR flyer, calendar, Stanford pack |
| Approve copy/photos once | Posts calendar content for 90 days |
| Optional: share program photos they already have | Recruits Stanford volunteers, updates metrics in Console |

After Quarter 1, a new Assigned Liaison takes over with handoff notes (~1 hr/week). The Reach Page and QR flyer keep working with no client maintenance.

Full model: [bridge-kit-proposal.md](../../docs/bridge-kit-proposal.md) sections *Minimal Work for Clients* and *Long-Term PVV Involvement*.
