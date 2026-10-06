# Editing the training

All lesson content lives in three files, one per track:

```
training/src/marketing.json
training/src/financial.json
training/src/technical.json
```

The workbooks in `training/interactive/` are **generated** from these files. Edit the JSON, not the HTML.

## The quick way (no install)

1. On GitHub, open the file you want, such as `training/src/marketing.json`, and click the pencil icon.
2. Make your edit and commit it to `main`.
3. A GitHub Action rebuilds the workbooks in about a minute and commits them. GitHub Pages then updates.

If the Action isn't running, use the local way below.

## The local way

```bash
python3 training/build.py
```

Needs Python 3.8 or newer and nothing else. It rewrites `training/interactive/*.html` and `training/CURRICULUM.md`. Open any workbook in a browser to preview it, then commit.

## How a module is written

Each module has a `title`, a short tab label (`short`), a time (`mins`), a list of `blocks`, and a `checklist`. Blocks appear in the order you list them.

| Block | Example | Shows |
|-------|---------|-------|
| `p` | `{"t": "p", "x": "Some text"}` | A paragraph. You can use `<strong>` and `<a href>` inside `x`. |
| `h3` | `{"t": "h3", "x": "A heading"}` | A sub-heading |
| `list` | `{"t": "list", "items": ["One", "Two"]}` | A bulleted list |
| `callout` | `{"t": "callout", "title": "Rule", "x": "Text"}` | The tinted highlight box |
| `table` | `{"t": "table", "head": ["A", "B"], "rows": [["1", "2"]]}` | A table |
| `media` | `{"t": "media", "kind": "video", "title": "...", "url": "https://...", "source": "Candid", "mins": 4, "why": "..."}` | A resource card. `kind` is `video`, `article`, `tool`, `template`, or `course`. |
| `figure` | `{"t": "figure", "svg": "flyer", "legend": ["..."], "caption": "..."}` | A diagram. Available: `flyer`, `phone`, `doors`, `pipeline`. |
| `exercise` | see below | Fill-in boxes whose answers are saved |
| `quiz` | see below | A multiple-choice question |

### An exercise

```json
{"t": "exercise", "title": "Define a campaign", "intro": "Optional lead-in text.", "fields": [
  {"id": "m2_goal", "type": "text", "label": "One goal, with a number", "placeholder": "e.g., 150 attendees"}
]}
```

- `type` can be `text`, `textarea`, `url`, or `select` (a `select` also needs `"options": ["A", "B"]`).
- Add `"expect": 1050` to a `text` field to make a self-checking math box. It says "That matches" or "Doesn't match yet" without revealing the answer.
- Add `"capstone": true` to the exercise to mark all its fields as capstone work. Chairs review these on the Dashboard. A field with `"required": true` must be filled before someone can mark the training complete.

### A quiz question

```json
{"t": "quiz", "id": "q3_a", "q": "The question?",
 "options": ["Wrong", "Right", "Wrong"], "answer": 1,
 "explain": "Shown when they get it right.", "hint": "Shown when they get it wrong."}
```

`answer` counts from **zero**: 0 is the first option, 1 is the second, and so on. Vary where the right answer sits.

## The feedback module

Every track ends with a short, optional **Feedback** module (a 1 to 5 rating for each module, a few overall ratings, and written comments). It is the same for all three tracks and lives in one file: `training/src/feedback.json`. The per-module ratings are generated automatically from each track's module titles, so adding a module needs no change here.

To add a question, add an entry to `questions`:

```json
{"id": "fb_pace", "type": "scale", "section": "The training overall", "label": "The pace felt right.", "low": "Too slow or fast", "high": "Just right"}
```

`type` can be `scale` (buttons 1 to 5), `select` (with `options`), or `textarea` (add `"optional": true` for comments). Feedback IDs start with `fb_`. Ratings count toward the module being "Complete" unless the field is marked optional.

## Rules that keep saved answers safe

- **IDs are permanent once people have used the training.** Field IDs (`m2_goal`), quiz IDs (`q3_a`), and capstone IDs (`cap_link`) are how answers are matched in the Google Sheet. Renaming one makes earlier answers look like a different question. Changing the *wording* is always fine.
- Field IDs start with the module number (`m2_`), quiz IDs with `q` and the module number (`q2_`), capstone fields with `cap_`. The build refuses duplicates.
- To retire a question, delete the block. Old answers stay in the sheet.

## Adding a module

1. Copy an existing module object (from `{` to the matching `}`) and paste it after the last one, with a comma.
2. Change its text, and give every field and quiz new IDs that use the new module number.
3. Keep each track near 60 minutes in total. The build warns if it drifts outside 50 to 70.
4. Rebuild.

## Adding a new track

Add it to `THEMES` in `training/build.py` and create `training/src/<name>.json`. The links at the top of every workbook, the landing page, and the "other teams" note are generated from `THEMES`, so they update by themselves.

## Changing a track's colors or look

Colors are set per track in `THEMES` at the top of `training/build.py`. The shared stylesheet is `training/src/_css.txt`, and the page layout and saving logic are in `training/src/template.html`. Changing those affects all three workbooks.
