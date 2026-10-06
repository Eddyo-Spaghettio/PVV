# Set up the training tracker (Google Sheet)

This connects the workbooks to a Google Sheet so answers, quiz results, and progress arrive automatically. It takes about 10 minutes and is free. Do it once; after that, nothing needs doing except reviewing.

**Which Google account?** The sheet and script run as whoever creates them. Use a shared PVV account (or the president's) so access survives officer turnover, and add the officers who need it. If Stanford's Google Workspace blocks "Anyone" access in step 5, create the sheet from a PVV Gmail account instead.

## Steps

### 1. Create the sheet
Go to <https://sheets.new> and name it **PVV Training Tracker**.

### 2. Add the script
1. In the sheet, choose **Extensions > Apps Script**.
2. Delete the starter code.
3. Open [`training/backend/Code.gs`](../backend/Code.gs) on GitHub, copy everything, and paste it in.
4. Click **Save** (disk icon).

### 3. Choose a shared key
1. Click the **gear icon (Project Settings)** on the left.
2. Under **Script Properties**, click **Add script property**.
3. Property: `PVV_KEY`. Value: any made-up word or string, such as `blue-heron-4821`.
4. Save, and remember the value for step 6.

The key is a light spam filter, not a password. It will sit in the public repo, so don't reuse a real password.

### 4. Run setup once
1. Click **Editor** (the `< >` icon) on the left.
2. In the function dropdown at the top, choose **setup**, then click **Run**.
3. Google asks for permission. Click **Review permissions**, choose your account, then **Advanced > Go to PVV Training Tracker (unsafe) > Allow**. (The warning appears because the script is yours and hasn't been through Google's verification. It only touches this sheet.)
4. When it finishes, go back to the sheet. You should see tabs named **Dashboard, Responses, Progress, Members**.

### 5. Publish it as a web app
1. Click **Deploy > New deployment**.
2. Click the gear next to "Select type" and choose **Web app**.
3. Description: `v1`. **Execute as: Me.** **Who has access: Anyone.**
4. Click **Deploy** and copy the **Web app URL**. It ends in `/exec`.

### 6. Connect the workbooks
Edit [`training/config.json`](../config.json) on GitHub and fill in both values:

```json
{
  "endpoint": "https://script.google.com/macros/s/XXXX/exec",
  "key": "blue-heron-4821"
}
```

Commit the change. The workbooks rebuild automatically (see [EDITING.md](EDITING.md)); if that doesn't happen, run `python3 training/build.py` and commit the result.

### 7. Test it
1. Open `https://YOUR-USERNAME.github.io/PVV/training/interactive/marketing-workbook.html` (GitHub Pages can take a minute or two to update).
2. Enter your name and email, answer a quiz question, and type in one box.
3. Wait two seconds. A row should appear on the **Responses** tab, and the status line at the top of the workbook should say "Saved to PVV".
4. Optional check: add `?action=ping` to the end of your web app URL in a browser. You should see `{"ok":true}`.

## Using the sheet

| Tab | What it shows |
|-----|---------------|
| **Dashboard** | Who started and finished each track, which modules are complete, the most-missed quiz questions, capstones waiting for review, and recent activity. All formulas. |
| **Responses** | One row per person per question, with their latest answer. Quizzes show Correct and Wrong attempts. |
| **Progress** | One row per person per module: status, checklist, quiz, and field counts. |
| **Members** | One row per person per track, with where they left off and when they finished. |

### Reviewing capstones
On the **Responses** tab, find rows where **Type** is `capstone`. Open the link, then set **Review status** from the dropdown (Approved, Needs revision, Reviewed) and add **Review notes** if you like. The member sees your status and notes next to their capstone the next time they open the workbook. The script never overwrites these columns.

### Giving chairs access
Share the sheet with category chairs as **Editor** if they will review, or **Viewer** if they only look. The sheet's sharing list is your "admin login": only people you share with can see responses.

## Changing the script later
If you edit `Code.gs` in Apps Script, **Save** and then choose **Deploy > Manage deployments > pencil icon > Version: New version > Deploy**. The web app URL stays the same. Saving alone does not update the live version.

## Troubleshooting

| Symptom | Likely cause |
|---------|--------------|
| Status line says "Couldn't reach PVV's sheet" | The deployment's access isn't set to **Anyone**, or `endpoint` in `config.json` is wrong. Use the `/exec` URL, not `/dev`. |
| Status line says it saved, but no rows appear | The `key` in `config.json` doesn't match the `PVV_KEY` script property. |
| "Run setup() first" error | Step 4 wasn't completed. Run **setup** from the editor. |
| Edited the script but nothing changed | You need a **new version** deployment (see above). |

The workbooks keep working if the sheet is unreachable: answers stay in the browser and retry on their own. Members can also download their answers as a CSV from the Start tab.

## Privacy and housekeeping
- Members identify themselves by email only, with no password. Anyone who knows a member's email, plus the endpoint and key, could read that person's saved answers. The training uses practice scenarios only, and the workbook tells members never to enter real client information.
- Decide a retention period, for example deleting rows at the end of each academic year, and note it in your officer transition checklist.
- Add "PVV Training Tracker access" to the transition checklist so access passes to the incoming officers (Article V of the constitution).
