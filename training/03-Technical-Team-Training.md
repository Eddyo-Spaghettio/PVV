# 💻 PVV Technical Team Training
## *Mission: Digitize - Agents of Operational Excellence*

**Proyecto Vidas Valiosas · Technical Consulting Track**  
**Difficulty:** Beginner-friendly · **Total XP:** 950 · **Track your progress:** `technical-module-tracker.csv`

---

> *"You're not building the next Facebook. You're building the thing that lets a overworked ED go home before 9pm - and that's actually harder and more heroic."*  
> - **Agent Formstack**, your fictional handler (think Nick Fury meets a UX designer)

---

## Meet the Cast

### 🎯 Training Client: **Bay Area Youth Alliance (BAYA)**

Fictional nonprofit providing mentorship for first-generation high school students.

| Field | Details |
|-------|---------|
| **Director** | James Okonkwo - former teacher, tech-phobic, wonderful |
| **Problem** | Everything is scattered: Google Docs, paper sign-in sheets, Instagram DMs |
| **Needs** | Simple website, mentor application form, student intake survey, basic data tracker |
| **Budget** | $0 for software (free tiers only) |

### Your Agent Team

| Agent | Specialty |
|-------|-------------|
| **Agent Formstack** | Forms, surveys, intake flows |
| **Web Weaver Wanda** | Websites without code |
| **Pipeline Pete** | Spreadsheets that don't suck |
| **Guardian Gate** | Accessibility & privacy |

---

## Module 0: Agent Briefing - What Tech Consulting Actually Is
**XP: 50 · Time: 30 min**

### PVV Technical Scope (From Constitution)

We help nonprofits with: - Websites, surveys, forms, online documents - Data collection & organization pipelines - Technical advice for operations, donations, management - Efficiency improvements generally

### The Consultant's Oath

1. **Simple beats clever** - If James can't update it alone in 6 months, rethink it  
2. **Free/low-cost first** - Clients rarely have SaaS budgets  
3. **Document everything** - You're leaving; they stay  
4. **No hero complex** - Don't over-build  
5. **Privacy matters** - Youth data = extra care  

### Build vs Advise vs Hand Off

| Situation | PVV action |
|-----------|------------|
| Client needs website | Build on Google Sites/Wix; train them to edit |
| Client asks "Should we use Salesforce?" | Advise; probably start with Sheets |
| Client has volunteer who knows WordPress | Document + light support; don't duplicate |

### Tech Stack Decision Tree

```
Need a website fast, no code, free?
  → Google Sites (simplest) or Wix (prettier)

Need forms/surveys?
  → Google Forms (free, familiar)

Need to track people over time?
  → Google Sheets + clear column schema

Need donations on website?
  → Givebutter / PayPal donate links (client sets up account)

Need advanced CRM?
  → Flag for future grant-funded purchase; don't impulse-buy Salesforce
```

### 🎯 Deliverable
Write BAYA's **tech problem statement** in 5 bullets. Interview a friend pretending to be James.

---

## Module 1: Website Mission - Bay Area Youth Alliance
**XP: 150 · Time: 2.5 hours · Hands-on build**

### Story Hook: The Website Is the Digital Front Door

Imagine Harry Potter trying to find Platform 9¾ with **no signs**. That's BAYA without a website - amazing program, invisible online.

### Step 1: Define Site Goals (Before Pixels)

Ask James:
1. What should visitors **do**? (Apply to mentor, donate, contact)
2. Who are the top 2 audiences? (Students, mentors, donors)
3. What **must** be on the homepage?

**BAYA answers (for training):** - Primary CTA: **Mentor application** + **Student program info** - Audiences: Potential mentors, student families - Must-have: Mission, impact stats, contact, application link

### Step 2: Site Map (Keep It Small)

```
HOME
├── About Us
├── Programs
│   ├── Mentor Program
│   └── Student Services
├── Get Involved (→ Application Form)
├── Donate (external link)
└── Contact
```

**Rule:** ≤7 top-level pages for small orgs.

### Step 3: Essential Page Elements

**Homepage must include:** - Clear headline (who you help + how) - Primary CTA button (contrasting color) - 1 impact stat ("150 students mentored since 2019") - Photo with permission - Footer: address, email, social, nonprofit EIN if public

**Example homepage copy:**

> **Headline:** *Mentorship for First-Gen Bay Area Students*  
> **Subhead:** Bay Area Youth Alliance pairs high school students with mentors who've walked the path to college and career.  
> **CTA Button:** [Become a Mentor]  
> **Stat strip:** 150 students · 80 volunteer mentors · 92% graduation rate

### Step 4: Build It (Choose Your Platform)

#### Option A: Google Sites (Recommended for Training)

**Pros:** Free, Google login, dead simple, Stanford-friendly  
**Cons:** Less design polish

**Lab steps:**
1. sites.google.com → Blank template
2. Name site: "Bay Area Youth Alliance - TEST"
3. Create pages from site map
4. Embed Google Form on "Get Involved" (Module 2)
5. Theme: clean, high contrast, mobile preview
6. Publish → share link with "Anyone with link"

#### Option B: Wix (More Design, Still Beginner)

**Pros:** Beautiful templates, nonprofit-friendly  
**Cons:** Free tier has ads; account tied to builder

**Lab steps:**
1. wix.com → Nonprofit template
2. Replace placeholder text
3. Connect custom domain later (client decision)
4. Mobile optimize every page

#### Option C: WordPress.com (Growth Path)

**Pros:** Scales long-term, plugins for donations  
**Cons:** Steeper learning curve - recommend only if client has ongoing tech volunteer

### Step 5: Pre-Launch Checklist - [ ] Mobile responsive (test phone view) - [ ] All links work - [ ] Contact info correct - [ ] Images have alt text - [ ] Privacy: no student full names/photos without releases - [ ] "Draft" watermark or password if not ready - [ ] Client approved copy

### 🎯 Deliverable
Live (or link-shared) BAYA test website with ≥4 pages + homepage CTA to form.

---

## Module 2: Forms & Surveys - No More Paper Chaos
**XP: 100 · Time: 90 min**

### Story Hook: Agent Formstack Infiltrates the Paperwork Fortress

James has a filing cabinet labeled **"Miscellaneous (Scary)."** Your mission: digital intake.

### Form vs Survey - Know the Difference

| Type | Purpose | Example |
|------|---------|---------|
| **Application form** | Collect structured signup data | Mentor application |
| **Survey** | Opinions, feedback, needs assessment | Student program interest survey |
| **Registration** | Event signup | Workshop RSVP |

### Mentor Application Form (Build This)

**Google Forms sections:**

**Section 1: About You** - Full name (short answer) - Email (short answer, required) - Phone (short answer) - LinkedIn or resume link (optional)

**Section 2: Background** - Why do you want to mentor? (paragraph) - Experience with youth (multiple choice + other) - Availability: checkboxes (Mon PM, Tue PM, etc.)

**Section 3: Safety & Compliance** - Can you pass a background check? (yes/no) - How did you hear about BAYA? (dropdown)

**Section 4: Consent** - "I agree to BAYA's volunteer policies" (checkbox, required)

### Form Design Best Practices

1. **Progressive disclosure** - Use sections, not one endless scroll
2. **Required fields sparingly** - Only what you'll actually use
3. **Clear confirmation message** - "Thanks! We'll email you within 5 business days."
4. **Response destination** - Google Sheet auto-linked; restrict access
5. **No duplicate questions** - James hates redundancy (everyone does)

### Student Needs Survey (Shorter)

For program planning (anonymous option): - Grade level (dropdown) - Interests: college prep, career exploration, wellness (checkboxes) - Preferred contact method (email/text/call) - Optional: "What would make this program most helpful?" (paragraph)

### Embed Forms on Website

Google Sites: Insert → Form → select your form  
Wix: Add → Contact & Forms → embed or built-in

### 🎯 Deliverable
Two Google Forms (mentor application + student survey) embedded on BAYA site.

---

## Module 3: Data Pipelines 101
**XP: 150 · Time: 2 hours**

### Story Hook: Pipeline Pete Builds the Plumber's Dream

A **data pipeline** = how information flows from collection → storage → use.

**BAYA pipeline:**

```
Mentor Form ──┐
              ├──→ Master Google Sheet ──→ Monthly report for James
Student Survey ┘         │
                         └──→ Mail merge / email list (optional)
```

### Master Sheet Schema (Design Before Data)

**Tab 1: Mentors**

| Column | Type | Notes |
|--------|------|-------|
| submission_id | auto | Form timestamp |
| name | text | |
| email | text | |
| status | dropdown | New / Interviewing / Active / Inactive |
| background_check | Y/N | |
| assigned_student | text | Blank until matched |
| notes | text | Internal only |

**Tab 2: Students**

| Column | Type | Notes |
|--------|------|-------|
| intake_date | date | |
| first_name | text | Consider initials only for privacy |
| grade | number | |
| program_track | dropdown | |
| mentor_assigned | text | |
| consent_on_file | Y/N | |

**Tab 3: Dashboard (Summary)**

| Metric | Formula approach |
|--------|------------------|
| Active mentors | COUNTIF status=Active |
| Students waiting | COUNT blank mentor |
| New apps this month | COUNTIF date > start of month |

### Connecting Forms to Sheets

Google Forms automatically creates linked Sheet. **Do not** manually copy-paste weekly - that's how errors are born.

### Data Hygiene Rules - **One source of truth** - One master sheet, not seven - **No student PII in filenames** - "BAYA_Master_2026" not "Maria_Garcia_data" - **Access control** - James + designated staff only - **Backup** - File → Version history; periodic download

### Optional: Zapier/Make (Level Up)

If client has budget later, automate: - New mentor form → Slack notification to James - Not required for training - Sheets alone is victory

### Hands-On Lab

1. Create BAYA Master Spreadsheet with 3 tabs
2. Link mentor form responses to Mentors tab
3. Add data validation dropdowns for status fields
4. Create 3 summary counts on Dashboard tab
5. Write 1-paragraph "How to use this" guide for James

### Example "How to Use This" for James

> *When a mentor applies, their row appears automatically in the Mentors tab. Change "status" from New to Interviewing when you email them. Once matched, type the student's first name in assigned_student. Check the Dashboard tab Monday mornings for counts.*

### 🎯 Deliverable
Master spreadsheet + linked forms + user guide.

---

## Module 4: Accessibility & Mobile - The Invisible Boss
**XP: 100 · Time: 60 min**

### Story Hook: Guardian Gate Appears When You Forget Alt Text

**15–20% of users** benefit from accessible design (disabilities, slow connections, bright sunlight on phones). Nonprofits serve everyone - sites must work for everyone.

### Quick Accessibility Wins

| Issue | Fix |
|-------|-----|
| Images without descriptions | Add **alt text** describing the image |
| Low contrast text | Dark text on light background (4.5:1 ratio minimum) |
| Tiny tap targets | Buttons big enough for thumbs |
| PDF-only info | Also put key info in HTML text |
| Video without captions | Add captions or written summary |
| "Click here" links | Descriptive: "Download mentor handbook" |

### Mobile Test Protocol

1. Open site on phone (or browser dev tools mobile view)
2. Can you read headline without zooming?
3. Can you tap CTA easily?
4. Does form work on mobile?
5. Page load under 5 seconds on LTE?

### Tools (Free) - **WebAIM Contrast Checker** - contrast ratio - **WAVE browser extension** - accessibility scan - Google Lighthouse (Chrome DevTools) - audit score

### 🎯 Deliverable
Run WAVE or Lighthouse on BAYA site. Fix **3 issues**. Screenshot before/after.

---

## Module 5: Handoff & Documentation
**XP: 100 · Time: 75 min**

### Story Hook: You're Not Batman - You Must Leave the Manual

PVV students graduate. James stays. **Documentation is love.**

### Handoff Package Contents

```
BAYA_Digital_Handoff/
├── README.md (start here)
├── Website_Editing_Guide.pdf
├── Form_Management_Guide.pdf
├── Master_Sheet_Link.txt
├── Account_Inventory.xlsx
├── Troubleshooting_FAQ.md
└── assets/ (logos, approved photos)
```

### Account Inventory Template

| Service | URL | Login owner | PVV role | Client role |
|---------|-----|-------------|----------|-------------|
| Google Site | sites.google.com/... | james@baya.org | Builder | Owner |
| Google Forms | forms.google.com/... | james@baya.org | Builder | Owner |
| Master Sheet | docs.google.com/... | james@baya.org | Builder | Owner |

**Critical:** Transfer ownership to client before you graduate.

### Website Editing Guide (Outline)

1. How to log in  
2. How to edit text on each page  
3. How to add a news post (if applicable)  
4. What NOT to touch (theme settings unless trained)  
5. Who to contact for help (PVV → then hire freelancer)

### 30-Minute Training Session Script

Agenda for James: - 5 min: Site tour - 10 min: Edit homepage text live - 10 min: View form responses + update mentor status - 5 min: Q&A

Record session (with permission) for future staff.

### 🎯 Deliverable
Handoff folder structure + account inventory + 1-page editing guide.

---

## Module 6: Security & Privacy Basics
**XP: 100 · Time: 60 min**

### Story Hook: Thanos Snapped Half the Passwords (They Were "password123")

Nonprofits collect vulnerable populations' data. **You are a steward, not an owner.**

### Data Classification for BAYA

| Data type | Examples | Handling |
|-----------|----------|----------|
| **Public** | Mission, event flyers | Open |
| **Internal** | Volunteer schedules | Org-only sharing |
| **Sensitive** | Student names, grades, contact | Encrypted accounts, need-to-know |
| **Highly sensitive** | Background checks, abuse disclosures | Minimal collection; expert policies |

### Security Checklist - [ ] Use client's Google account (not your personal @stanford.edu for permanent ownership) - [ ] Enable 2-factor authentication on org accounts - [ ] Share folders with **specific emails**, not "anyone with link" for PII - [ ] Don't store passwords in Google Docs titled "PASSWORDS" - [ ] Use password manager recommendation (Bitwarden free, 1Password) - [ ] Delete test submissions with fake PII

### Youth Data (Extra Care) - Collect **minimum necessary** fields - Parent/guardian consent where required - No public website photos of minors without releases - Check if client needs formal privacy policy (often yes if collecting online)

### When to Escalate

Tell CCC / client board if: - Data breach suspected - Client asks you to store SSNs/bank info in Sheets (redirect to secure systems) - Website needs HIPAA/legal compliance beyond PVV scope

### 🎯 Deliverable
Security checklist completed for BAYA project + draft 1-paragraph privacy blurb for website footer.

**Example privacy blurb:**

> *Bay Area Youth Alliance collects information you submit through our forms solely to connect students with mentorship opportunities. We do not sell your data. Questions? Contact privacy@baya.org.*

---

## 🐉 FINAL BOSS BATTLE: Full Digital Toolkit
**XP: 200 · Time: 3–4 hours · Demo to Technical CCC**

Deploy the complete **BAYA Digital Toolkit** and present to Agent Formstack (your peers).

### Required Deliverables

| # | Component | Criteria |
|---|-----------|----------|
| 1 | Live website (≥4 pages) | Mobile-friendly, clear CTAs |
| 2 | Mentor application form | Embedded, confirmation message set |
| 3 | Student survey | Anonymous option included |
| 4 | Master data spreadsheet | 3 tabs, dashboard metrics |
| 5 | Accessibility fixes | 3+ issues resolved |
| 6 | Handoff documentation | Account inventory + editing guide |
| 7 | Security review | Checklist complete |
| 8 | 5-min live demo | Edit text, show form response flow |

### Demo Script

1. **Homepage tour** (30 sec) - audiences + CTAs  
2. **Submit test mentor application** (60 sec)  
3. **Show row appearing in sheet** (30 sec)  
4. **Update mentor status** (30 sec)  
5. **Show dashboard counts** (30 sec)  
6. **Explain handoff to James** (90 sec)  

### Grading Rubric

| Criteria | /25 |
|----------|-----|
| Usability for non-tech client | |
| Clean data structure | |
| Accessibility & mobile | |
| Documentation quality | |
| Privacy & security awareness | |

**70+ → Technical Consultant Ready** ✅

---

## Platform Comparison Reference

| Platform | Best for | Cost | PVV recommendation |
|----------|----------|------|---------------------|
| Google Sites | Fast free site, easy handoff | Free | ⭐ Start here |
| Wix | Pretty sites, events | Free tier | ⭐ If client wants design polish |
| WordPress.com | Long-term growth | Free–$ | If client has tech volunteer |
| Squarespace | Design-focused | Paid | Only if client already pays |
| Google Forms | Intake, surveys | Free | ⭐ Default |
| Tally | Nicer forms | Free tier | Alternative to Google Forms |
| Airtable | Database-lite | Free tier | When Sheets feels cramped |

---

## Real Client Project Checklist

```
□ Discovery: What exists? What's painful? What's the dream state?
□ Agree scope IN WRITING (email OK): deliverables, timeline, not-in-scope
□ Build on client-owned accounts (or transfer ASAP)
□ Weekly check-in with client contact
□ Test on mobile + accessibility scan
□ Handoff training session + documentation
□ 2-week support window after handoff (PVV policy - confirm with CCC)
□ Celebrate - you saved someone hours per week
```

---

## Further Reading - [Candid: Free Website Guide](https://candid.org/blogs/a-guide-to-creating-a-free-website-for-your-nonprofit/) - [Wix Nonprofit Website Guide](https://www.wix.com/blog/how-to-create-an-effective-non-profit-website) - [WebAIM Accessibility Resources](https://webaim.org/resources/) - PVV Constitution AY 2025–26, Article III (Technical Assistance scope)

---

*The mission is complete when James updates the homepage without texting you at midnight. Go build boring, reliable, beautiful tools. Agent Formstack out.*
