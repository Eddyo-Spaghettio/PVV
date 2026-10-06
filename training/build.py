#!/usr/bin/env python3
"""
Builds the PVV training workbooks.

    python3 training/build.py

Reads   training/src/{marketing,financial,technical}.json   (the content)
        training/src/template.html + _css.txt               (the page shell)
        training/config.json                                (Google Sheet endpoint)
Writes  training/interactive/*.html                         (the workbooks)
        training/CURRICULUM.md                              (a readable summary)

No dependencies beyond Python 3.8+. Edit the JSON, run this, commit the result.
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT / "interactive"

THEMES = {
    "marketing": {"title": "Marketing", "accent": "#2d6a4f", "light": "#d8f3dc"},
    "financial": {"title": "Financial", "accent": "#1d3557", "light": "#e8eef4"},
    "technical": {"title": "Technical", "accent": "#5c4d7d", "light": "#ede8f5"},
}

KIND_LABEL = {"video": "Watch", "article": "Read", "tool": "Try", "template": "Open", "course": "Explore"}

# ---------------------------------------------------------------- figures
FIGURES = {
    "flyer": """<svg class="fig" viewBox="0 0 240 300" role="img" aria-label="A flyer layout with five zones: event name, date and time, location, one line of impact, and a QR code with logo">
<rect class="plain" x="6" y="6" width="228" height="288" rx="4"/>
<circle class="solid" cx="24" cy="42" r="10"/><text class="onsolid" x="24" y="47" text-anchor="middle">1</text>
<rect class="box" x="44" y="20" width="180" height="44" rx="3"/><text x="134" y="48" text-anchor="middle" font-size="18">Event name</text>
<circle class="solid" cx="24" cy="87" r="10"/><text class="onsolid" x="24" y="92" text-anchor="middle">2</text>
<rect class="box" x="44" y="72" width="180" height="30" rx="3"/><text x="134" y="92" text-anchor="middle">Date and time</text>
<circle class="solid" cx="24" cy="123" r="10"/><text class="onsolid" x="24" y="128" text-anchor="middle">3</text>
<rect class="box" x="44" y="110" width="180" height="26" rx="3"/><text x="134" y="128" text-anchor="middle">Location and address</text>
<circle class="solid" cx="24" cy="164" r="10"/><text class="onsolid" x="24" y="169" text-anchor="middle">4</text>
<rect class="box" x="44" y="144" width="180" height="40" rx="3"/><text x="134" y="168" text-anchor="middle">One line of impact</text>
<circle class="solid" cx="24" cy="228" r="10"/><text class="onsolid" x="24" y="233" text-anchor="middle">5</text>
<rect class="solid" x="44" y="198" width="60" height="60" rx="3"/><text class="onsolid" x="74" y="233" text-anchor="middle">QR</text>
<rect class="plain" x="114" y="210" width="110" height="36" rx="3"/><text x="169" y="233" text-anchor="middle">Logo</text>
</svg>""",
    "phone": """<svg class="fig" viewBox="0 0 200 330" role="img" aria-label="A phone-sized Reach Page wireframe: a mission sentence, three buttons, and one impact number">
<rect class="plain" x="6" y="6" width="188" height="318" rx="18"/>
<circle class="solid" cx="26" cy="62" r="10"/><text class="onsolid" x="26" y="67" text-anchor="middle">1</text>
<rect class="box" x="44" y="34" width="136" height="56" rx="4"/><text x="112" y="66" text-anchor="middle">Mission sentence</text>
<circle class="solid" cx="26" cy="140" r="10"/><text class="onsolid" x="26" y="145" text-anchor="middle">2</text>
<rect class="solid" x="44" y="104" width="136" height="28" rx="4"/><text class="onsolid" x="112" y="123" text-anchor="middle">Volunteer</text>
<rect class="solid" x="44" y="140" width="136" height="28" rx="4"/><text class="onsolid" x="112" y="159" text-anchor="middle">Donate</text>
<rect class="solid" x="44" y="176" width="136" height="28" rx="4"/><text class="onsolid" x="112" y="195" text-anchor="middle">Contact</text>
<circle class="solid" cx="26" cy="245" r="10"/><text class="onsolid" x="26" y="250" text-anchor="middle">3</text>
<rect class="box" x="44" y="220" width="136" height="50" rx="4"/><text x="112" y="250" text-anchor="middle">200 families a week</text>
</svg>""",
    "doors": """<div class="panels">
<div class="panel on"><h4>Door 1: PVV's own funding</h4><p>Pays for rides, events, and printing.</p><p>Applied for by the PVV Treasurer.</p><p><em>Examples: Haas transportation grants, Haas event co-sponsorship.</em></p></div>
<div class="panel"><h4>Door 2: client funding</h4><p>Pays for the client's programs.</p><p>Applied for by the client's director.</p><p><em>PVV researches, drafts, and advises. The client signs and submits.</em></p></div>
</div>""",
    "pipeline": """<div class="flow"><span class="step">Google Form</span><span class="arrow">&rarr;</span><span class="step">Google Sheet</span><span class="arrow">&rarr;</span><span class="step">Dashboard</span><span class="arrow">&rarr;</span><span class="step">Monthly report</span></div>""",
}

# ---------------------------------------------------------------- helpers
def esc(s):
    return html.escape(str(s), quote=True)


class BuildError(Exception):
    pass


def render_field(f, seen_ids, mod_no):
    fid = f["id"]
    if fid in seen_ids:
        raise BuildError(f"Duplicate id: {fid}")
    seen_ids.add(fid)
    if not fid.startswith(f"m{mod_no}_") and not fid.startswith(("cap_", "fb_")):
        raise BuildError(f"Field id '{fid}' in module {mod_no} should start with 'm{mod_no}_' (or 'cap_' / 'fb_')")
    typ = f.get("type", "text")
    attrs = f' id="{esc(fid)}" data-f="{esc(fid)}"'
    if f.get("capstone"):
        attrs += ' data-cap="1"'
        if f.get("required"):
            attrs += ' data-req="1"'
    if f.get("expect") is not None:
        attrs += f' data-expect="{esc(f["expect"])}"'
    if f.get("feedback"):
        attrs += ' data-fb="1"'
    if f.get("optional"):
        attrs += ' data-opt="1"'
    ph = f' placeholder="{esc(f["placeholder"])}"' if f.get("placeholder") else ""
    if typ == "scale":
        pts = int(f.get("points", 5))
        lid = f"{fid}_l"
        btns = "".join(
            f'<button type="button" class="scale-btn" role="radio" aria-checked="false" data-v="{i}">{i}</button>'
            for i in range(1, pts + 1))
        return (f'<label for="{esc(fid)}" id="{esc(lid)}">{f["label"]}</label>\n  '
                f'<div class="scale" role="radiogroup" aria-labelledby="{esc(lid)}" data-scale="{esc(fid)}">{btns}</div>\n  '
                f'<p class="scale-ends"><span>{f["low"]}</span><span>{f["high"]}</span></p>\n  '
                f'<input type="hidden"{attrs}>')
    out = [f'<label for="{esc(fid)}">{f["label"]}</label>']
    if typ == "textarea":
        out.append(f"<textarea{attrs}{ph}></textarea>")
    elif typ == "select":
        opts = "".join(f"<option>{esc(o)}</option>" for o in f["options"])
        out.append(f'<select{attrs}><option value="">Choose one</option>{opts}</select>')
    elif typ == "url":
        out.append(f'<input type="url"{attrs}{ph}>')
    else:
        out.append(f'<input type="text"{attrs}{ph}>')
    if f.get("expect") is not None:
        out.append(f'<p class="field-note" data-for="{esc(fid)}"></p>')
    if f.get("capstone"):
        out.append(f'<p class="field-note" id="rv_{esc(fid)}"></p>')
    return "\n  ".join(out)


def render_block(b, ctx):
    t = b["t"]
    if t == "p":
        return f'<p>{b["x"]}</p>'
    if t == "h3":
        return f'<h3>{b["x"]}</h3>'
    if t == "list":
        return "<ul>" + "".join(f"<li>{i}</li>" for i in b["items"]) + "</ul>"
    if t == "callout":
        return f'<div class="callout"><strong>{b["title"]}</strong>{b["x"]}</div>'
    if t == "table":
        head = "".join(f"<th>{c}</th>" for c in b["head"])
        rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in b["rows"])
        return f'<div class="card"><table><tr>{head}</tr>{rows}</table></div>'
    if t == "figure":
        fig = FIGURES.get(b["svg"])
        if not fig:
            raise BuildError(f"Unknown figure: {b['svg']}")
        if b.get("legend"):
            items = "".join(f"<li>{i}</li>" for i in b["legend"])
            fig = f'<div class="figrow">{fig}<ol class="legend">{items}</ol></div>'
        return f'<figure class="card">{fig}<figcaption>{b["caption"]}</figcaption></figure>'
    if t == "media":
        kind = KIND_LABEL.get(b.get("kind", "article"), "Read")
        mins = f", about {b['mins']} min" if b.get("mins") else ""
        src = f", {b['source']}" if b.get("source") else ""
        why = f'<p>{b["why"]}</p>' if b.get("why") else ""
        ctx["links"].append((b["title"], b["url"], kind))
        return (f'<div class="card media"><p class="kind">{kind}{mins}{src}</p>'
                f'<p><a href="{esc(b["url"])}" target="_blank" rel="noopener">{b["title"]}</a></p>{why}</div>')
    if t == "exercise":
        parts = [f'<h3>Exercise: {b["title"]}</h3>']
        if b.get("intro"):
            parts.append(f'<p>{b["intro"]}</p>')
        for f in b["fields"]:
            if b.get("capstone"):
                f = dict(f, capstone=True)
            parts.append(render_field(f, ctx["ids"], ctx["mod"]))
        return "\n  ".join(parts)
    if t == "quiz":
        qid = b["id"]
        if qid in ctx["ids"]:
            raise BuildError(f"Duplicate id: {qid}")
        ctx["ids"].add(qid)
        if not qid.startswith(f"q{ctx['mod']}_"):
            raise BuildError(f"Quiz id '{qid}' in module {ctx['mod']} should start with 'q{ctx['mod']}_'")
        if not (0 <= b["answer"] < len(b["options"])):
            raise BuildError(f"Quiz {qid}: answer index out of range")
        ctx["answers"].append(b["answer"])
        opts = "".join(f'<button type="button" class="quiz-option">{o}</button>' for o in b["options"])
        return (f'<div class="quiz" data-q="{esc(qid)}" data-a="{b["answer"]}" '
                f'data-ok="{esc(b["explain"])}" data-no="{esc(b["hint"])}">'
                f'<p>{b["q"]}</p>{opts}<div class="feedback" aria-live="polite"></div></div>')
    raise BuildError(f"Unknown block type: {t}")


def render_module(m, n, total, ctx_global):
    ctx = {"mod": n, "ids": ctx_global["ids"], "answers": ctx_global["answers"], "links": ctx_global["links"]}
    parts = []
    prev = None
    for b in m["blocks"]:
        if b["t"] == "quiz" and prev != "quiz":
            parts.append("<h3>Quick check</h3>")
        parts.append(render_block(b, ctx))
        prev = b["t"]
    body = "\n\n  ".join(parts)
    cl = "".join(
        f'\n    <label><input type="checkbox" data-cl="cl{n}" data-i="{i}" data-key="cl{n}_{i}"> {item}</label>'
        for i, item in enumerate(m["checklist"])
    )
    back = 0 if n == 1 else n - 1
    back_label = "Back to start" if n == 1 else "Back"
    if n < total:
        nxt = (f'<button class="btn" onclick="goMod({n + 1})">Next: {esc(ctx_global["modules"][n]["short"])}</button>')
        tail = ""
    else:
        nxt = '<button class="btn" id="completeBtn">Mark training complete</button>'
        tail = '\n  <p class="saved-note" id="completeNote"></p>'
    return f"""<!-- MODULE {n} -->
<div class="module" id="mod{n}">
  <h2>Module {n}: {m["title"]}</h2>
  <p class="meta">About {m["mins"]} minutes</p>

  {body}

  <h3>Module {n} checklist</h3>
  <div class="checklist card" id="cl{n}">{cl}
  </div>

  <div class="nav-buttons">
    <button class="btn btn-outline" onclick="goMod({back})">{back_label}</button>
    {nxt}
  </div>{tail}
</div>"""


def render_feedback(fb, mods, n, ctx_global, other=""):
    ms = fb["module_scale"]
    fields = [dict(id=f"fb_mod{i}", type="scale", section=ms["section"], low=ms["low"], high=ms["high"], feedback=True,
                   label=ms["label"].replace("{title}", f"Module {i}: {m['title']}")) for i, m in enumerate(mods, 1)]
    fields += [dict(q, feedback=True) for q in fb["questions"]]
    parts, section = [], None
    for f in fields:
        if f.get("section") != section:
            section = f.get("section")
            parts.append(f"<h3>{section}</h3>")
        parts.append(render_field(f, ctx_global["ids"], n))
    body = "\n\n  ".join(parts)
    return f"""<!-- FEEDBACK -->
<div class="module" id="mod{n}">
  <h2>{fb["title"]}</h2>
  <p class="meta">About {fb["mins"]} minutes. Optional, but it helps.</p>
  <p>{fb["intro"]}</p>

  {body}

  <div class="nav-buttons">
    <button class="btn btn-outline" onclick="goMod({n - 1})">Back</button>
    <button class="btn" id="completeBtn">Mark training complete</button>
  </div>
  <p class="saved-note" id="completeNote"></p>
  {other}
</div>"""


def render_start(data, theme, fb):
    mods = data["modules"]
    rows = "".join(f"<tr><td>{i}</td><td>{m['title']}</td><td>{m['mins']} min</td></tr>" for i, m in enumerate(mods, 1))
    rows += f"<tr><td>{len(mods) + 1}</td><td>{fb['title']} (optional)</td><td>{fb['mins']} min</td></tr>"
    total = sum(m["mins"] for m in mods)
    w = data["welcome"]
    return f"""<!-- START -->
<div class="module" id="mod0">
  <h2>Welcome to {theme['title']} training</h2>
  <p class="meta">About {total} minutes, plus a {fb['mins']}-minute feedback form</p>
  <p>{w['intro']}</p>

  <div class="callout">
    <strong>What you'll leave with</strong>
    {w['outcome']}
  </div>

  <div class="card">
    <table>
      <tr><th>#</th><th>Module</th><th>Time</th></tr>{rows}
    </table>
  </div>

  <div class="callout">
    <strong>How your answers are used</strong>
    Your name, email, and answers are saved to PVV's training sheet so your category chair can see your progress and give feedback. Use practice scenarios only. Never type real client names, contact details, or personal information into an exercise.
  </div>

  <div id="signupBox">
    <label for="u_name">Your name</label>
    <input type="text" id="u_name" autocomplete="name">
    <label for="u_email">Your email</label>
    <input type="text" id="u_email" autocomplete="email" inputmode="email">
    <button class="btn" id="startBtn" type="button">Save and begin</button>
    <p class="err" id="startErr" role="alert"></p>
  </div>

  <div id="resumeBox" style="display:none">
    <p>Welcome back, <strong id="whoName"></strong>. You can open any module from the tabs above, in any order.</p>
    <button class="btn" id="resumeBtn" type="button"></button>
    <p class="saved-note"><button class="linkbtn" id="switchUser" type="button">Not you? Switch person</button> &nbsp; <button class="linkbtn" id="downloadBtn" type="button">Download my answers (CSV)</button></p>
  </div>
</div>"""


def render_trackbar(current):
    parts = ['<a href="index.html">All tracks</a>']
    for t, th in THEMES.items():
        if t == current:
            parts.append(f'<span aria-current="page" data-track="{t}" data-label="{th["title"]}">{th["title"]}</span>')
        else:
            parts.append(f'<a href="{t}-workbook.html" data-track="{t}" data-label="{th["title"]}">{th["title"]}</a>')
    return "\n  ".join(parts)


def render_other_tracks(current):
    links = ", ".join(f'<a href="{t}-workbook.html">{th["title"]}</a>' for t, th in THEMES.items() if t != current)
    return (f'<p class="saved-note">Curious how the other PVV teams work? You can open the {links} training '
            f'any time. Each one takes about an hour.</p>')


def build_track(track, cfg):
    theme = THEMES[track]
    data = json.loads((SRC / f"{track}.json").read_text(encoding="utf-8"))
    mods = data["modules"]
    if len(mods) < 5:
        raise BuildError(f"{track}: needs at least 5 modules (has {len(mods)})")
    total_min = sum(m["mins"] for m in mods)
    if not 50 <= total_min <= 70:
        print(f"  warning: {track} totals {total_min} minutes (target is about 60)")

    fb = json.loads((SRC / "feedback.json").read_text(encoding="utf-8"))
    ctx_global = {"ids": set(), "answers": [], "links": [], "modules": mods + [{"short": fb["short"]}]}
    nav = ['<button class="active" data-mod="0">Start</button>']
    for i, m in enumerate(mods, 1):
        nav.append(f'<button data-mod="{i}">{i}. {m["short"]}</button>')
    nav.append(f'<button data-mod="{len(mods) + 1}">{len(mods) + 1}. {fb["short"]}</button>')
    modules_html = "\n\n".join(render_module(m, i, len(mods) + 1, ctx_global) for i, m in enumerate(mods, 1))
    modules_html += "\n\n" + render_feedback(fb, mods, len(mods) + 1, ctx_global, render_other_tracks(track))

    css = (SRC / "_css.txt").read_text(encoding="utf-8").replace("%%ACCENT_LIGHT%%", theme["light"]).replace("%%ACCENT%%", theme["accent"])
    page_cfg = {"endpoint": cfg.get("endpoint", ""), "key": cfg.get("key", ""), "track": track}
    tpl = (SRC / "template.html").read_text(encoding="utf-8")
    page = (tpl.replace("%%CSS%%", css)
               .replace("%%TITLE%%", theme["title"])
               .replace("%%TRACK%%", track)
               .replace("%%SUBTITLE%%", f"{len(mods)} short modules, about an hour in total, plus a quick feedback form. Your progress saves automatically, and you can pick up where you left off.")
               .replace("%%TRACKBAR%%", render_trackbar(track))
               .replace("%%NAV%%", "\n".join(nav))
               .replace("%%START%%", render_start(data, theme, fb))
               .replace("%%MODULES%%", modules_html)
               .replace("%%CFG%%", json.dumps(page_cfg)))
    (OUT / f"{track}-workbook.html").write_text(page, encoding="utf-8")
    print(f"  {track}: {len(mods)} modules, {total_min} min, {len(ctx_global['ids'])} fields/quizzes")
    return data, theme, ctx_global


def write_index(tracks):
    css = (SRC / "_css.txt").read_text(encoding="utf-8").replace("%%ACCENT_LIGHT%%", "#d8f3dc").replace("%%ACCENT%%", "#2d6a4f")
    items = "".join(
        f'<div class="card"><h3 style="margin-top:0">{THEMES[t]["title"]} track</h3>'
        f'<p>{len(d["modules"])} modules, about {sum(m["mins"] for m in d["modules"])} minutes. {d["welcome"]["card"]}</p>'
        f'<a class="btn" style="text-decoration:none;display:inline-block" href="{t}-workbook.html">Open {THEMES[t]["title"]} training</a></div>'
        for t, d in tracks.items()
    )
    page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PVV Training</title><style>
{css}</style></head><body>
<!-- GENERATED FILE. Run: python3 training/build.py -->
<div class="header"><h1>PVV Training</h1><p>Pick your consulting track. Each one takes about an hour.</p></div>
<div class="container">
<p>Proyecto Vidas Valiosas connects local nonprofits with free, student-provided consulting. Choose the team you joined. Your progress saves automatically, so you can stop and come back.</p>
{items}
</div></body></html>"""
    (OUT / "index.html").write_text(page, encoding="utf-8")


def write_curriculum(tracks, ctxs):
    lines = ["# Training curriculum", "",
             "*Generated by `training/build.py`. Edit `training/src/*.json`, not this file.*", ""]
    for t, d in tracks.items():
        mods = d["modules"]
        lines += [f"## {THEMES[t]['title']} track ({sum(m['mins'] for m in mods)} min)", ""]
        for i, m in enumerate(mods, 1):
            lines.append(f"{i}. **{m['title']}** ({m['mins']} min)")
        lines.append(f"{len(mods) + 1}. **Feedback** (optional, 2 min)")
        lines += ["", "Linked resources:", ""]
        seen = set()
        for title, url, kind in ctxs[t]["links"]:
            if url in seen:
                continue
            seen.add(url)
            lines.append(f"- {kind}: [{re.sub('<[^>]+>', '', title)}]({url})")
        lines.append("")
    (ROOT / "CURRICULUM.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    cfg = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
    OUT.mkdir(exist_ok=True)
    tracks, ctxs = {}, {}
    print("Building workbooks:")
    for t in THEMES:
        d, theme, ctx = build_track(t, cfg)
        tracks[t], ctxs[t] = d, ctx
    write_index(tracks)
    write_curriculum(tracks, ctxs)
    print("Wrote training/interactive/*.html and training/CURRICULUM.md")
    if not cfg.get("endpoint"):
        print("Note: config.json has no endpoint yet, so workbooks save in the browser only.")


if __name__ == "__main__":
    try:
        main()
    except BuildError as e:
        print(f"Build error: {e}", file=sys.stderr)
        sys.exit(1)
