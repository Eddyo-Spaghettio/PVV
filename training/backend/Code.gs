/**
 * PVV Training Tracker: Google Apps Script backend.
 *
 * Receives answers from the training workbooks and writes them into this
 * spreadsheet. Also returns a person's saved answers so they can resume on
 * another device. Setup steps: training/docs/SHEET-SETUP.md
 *
 * Sheets this script manages:
 *   Responses  one row per person per question (latest answer wins)
 *   Progress   one row per person per module
 *   Members    one row per person per track
 *   Dashboard  formulas only; created by setup(), safe to restyle
 *
 * Reviewers: use the "Review status", "Reviewer" and "Review notes" columns on
 * the Responses sheet. The script never overwrites those.
 */

var SHEETS = {
  responses: 'Responses',
  progress: 'Progress',
  members: 'Members',
  dashboard: 'Dashboard'
};

var HEADERS = {
  Responses: ['Updated', 'Email', 'Name', 'Track', 'Module', 'Field ID', 'Type', 'Prompt', 'Answer',
              'Correct', 'Wrong attempts', 'Review status', 'Reviewer', 'Review notes', 'Key'],
  Progress: ['Updated', 'Email', 'Name', 'Track', 'Module', 'Title', 'Status',
             'Checklist done', 'Checklist total', 'Quizzes correct', 'Quizzes total',
             'Fields filled', 'Fields total', 'Key'],
  Members: ['Email', 'Name', 'Track', 'First seen', 'Last seen', 'Current module', 'Completed', 'Key']
};

var TRACKS = { marketing: true, financial: true, technical: true };

/* ------------------------------------------------------------ one-time setup */

/** Run this once from the Apps Script editor (Run > setup). Safe to run again. */
function setup() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  PropertiesService.getScriptProperties().setProperty('SHEET_ID', ss.getId());

  ['Responses', 'Progress', 'Members'].forEach(function (name) {
    var sh = ss.getSheetByName(name) || ss.insertSheet(name);
    var h = HEADERS[name];
    sh.getRange(1, 1, 1, h.length).setValues([h]).setFontWeight('bold');
    sh.setFrozenRows(1);
  });

  // Reviewers pick a status from a dropdown.
  var resp = ss.getSheetByName('Responses');
  var rule = SpreadsheetApp.newDataValidation()
    .requireValueInList(['Approved', 'Needs revision', 'Reviewed'], true)
    .setAllowInvalid(false).build();
  resp.getRange('L2:L5000').setDataValidation(rule);
  // Plain text for Prompt and Answer: keeps "March 15" and "=SUM(1)" exactly as typed.
  resp.getRange(2, 8, Math.max(resp.getMaxRows() - 1, 1), 2).setNumberFormat('@');
  resp.setColumnWidth(8, 320); resp.setColumnWidth(9, 320); resp.setColumnWidth(14, 240);
  resp.hideColumns(15); // Key
  ss.getSheetByName('Progress').hideColumns(14);
  ss.getSheetByName('Members').hideColumns(8);

  buildDashboard_(ss);

  var key = PropertiesService.getScriptProperties().getProperty('PVV_KEY');
  Logger.log(key
    ? 'Setup complete. PVV_KEY is set.'
    : 'Setup complete. NEXT: add a script property named PVV_KEY (Project Settings > Script properties) and put the same word in training/config.json.');
}

function buildDashboard_(ss) {
  var sh = ss.getSheetByName(SHEETS.dashboard) || ss.insertSheet(SHEETS.dashboard, 0);
  sh.clear();
  sh.getRange('A1').setValue('PVV training dashboard').setFontWeight('bold').setFontSize(14);
  sh.getRange('A2').setValue('Everything below is a formula. It updates as people work through the training.');

  sh.getRange('A4').setValue('By track').setFontWeight('bold');
  sh.getRange('A5:C5').setValues([['Track', 'People started', 'People finished']]).setFontWeight('bold');
  ['marketing', 'financial', 'technical'].forEach(function (t, i) {
    var r = 6 + i;
    sh.getRange(r, 1).setValue(t);
    sh.getRange(r, 2).setFormula('=COUNTIFS(Members!C:C,A' + r + ')');
    sh.getRange(r, 3).setFormula('=COUNTIFS(Members!C:C,A' + r + ',Members!G:G,"<>")');
  });

  sh.getRange('A10').setValue('Modules completed (checklist and quizzes all done)').setFontWeight('bold');
  sh.getRange('A11').setFormula('=IFERROR(QUERY(Progress!A:N,"select D, E, F, count(B) where G = \'Complete\' group by D, E, F order by D, E label D \'Track\', E \'Module\', F \'Title\', count(B) \'People\'",1),"Nothing yet")');

  sh.getRange('F10').setValue('Most-missed quiz questions').setFontWeight('bold');
  sh.getRange('F11').setFormula('=IFERROR(QUERY(Responses!A:O,"select D, E, H, sum(K) where G = \'quiz\' and K > 0 group by D, E, H order by sum(K) desc limit 10 label D \'Track\', E \'Module\', H \'Question\', sum(K) \'Wrong attempts\'",1),"Nothing yet")');

  sh.getRange('A30').setValue('Capstones waiting for review').setFontWeight('bold');
  sh.getRange('A31').setFormula('=IFERROR(QUERY(Responses!A:O,"select B, C, D, H, I where G = \'capstone\' and I is not null and L is null order by A desc label B \'Email\', C \'Name\', D \'Track\', H \'Prompt\', I \'Answer\'",1),"Nothing waiting")');

  sh.getRange('A50').setValue('Recent activity').setFontWeight('bold');
  sh.getRange('A51').setFormula('=IFERROR(QUERY(Members!A:H,"select B, C, F, E order by E desc limit 15 label B \'Name\', C \'Track\', F \'Current module\', E \'Last seen\'",1),"Nothing yet")');

  sh.setColumnWidth(1, 160);
  sh.setColumnWidth(3, 260);
  sh.setColumnWidth(8, 360);
}

/* ------------------------------------------------------------ web app */

function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(25000);
    var p = JSON.parse(e.postData.contents);
    if (!authorized_(p.key)) return json_({ ok: false, error: 'Not authorized' });
    if (p.action !== 'save') return json_({ ok: false, error: 'Unknown action' });
    return json_(save_(p));
  } catch (err) {
    return json_({ ok: false, error: String(err && err.message || err) });
  } finally {
    try { lock.releaseLock(); } catch (e2) {}
  }
}

function doGet(e) {
  try {
    var q = e.parameter || {};
    if (q.action === 'ping') return json_({ ok: true });
    if (!authorized_(q.key)) return json_({ ok: false, error: 'Not authorized' });
    if (q.action === 'load') return json_(load_(q));
    return json_({ ok: false, error: 'Unknown action' });
  } catch (err) {
    return json_({ ok: false, error: String(err && err.message || err) });
  }
}

function authorized_(key) {
  var expected = PropertiesService.getScriptProperties().getProperty('PVV_KEY');
  return !!expected && key === expected; // no PVV_KEY set means everything is refused
}

function json_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

function ss_() {
  var id = PropertiesService.getScriptProperties().getProperty('SHEET_ID');
  if (!id) throw new Error('Run setup() first');
  return SpreadsheetApp.openById(id);
}

/* ------------------------------------------------------------ save */

function clean_(s, max) {
  s = (s === null || s === undefined) ? '' : String(s);
  return s.length > (max || 5000) ? s.slice(0, max || 5000) : s;
  // Prompt and Answer cells are formatted as plain text (see setup), so a typed
  // answer is never turned into a date, number, or formula.
}

function save_(p) {
  var track = String(p.track || '').toLowerCase();
  if (!TRACKS[track]) throw new Error('Unknown track');
  var email = String((p.user && p.user.email) || '').trim().toLowerCase();
  var name = clean_(p.user && p.user.name, 200);
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) throw new Error('Invalid email');

  var ss = ss_();
  var now = new Date();

  saveItems_(ss.getSheetByName(SHEETS.responses), email, name, track, p.items || []);
  saveProgress_(ss.getSheetByName(SHEETS.progress), email, name, track, p.progress || [], now);
  saveMember_(ss.getSheetByName(SHEETS.members), email, name, track, p.last, p.complete, now);
  return { ok: true, saved: (p.items || []).length };
}

function indexKeys_(sheet, keyCol) {
  var last = sheet.getLastRow();
  var map = {};
  if (last < 2) return map;
  var vals = sheet.getRange(2, keyCol, last - 1, 1).getValues();
  for (var i = 0; i < vals.length; i++) map[vals[i][0]] = i + 2;
  return map;
}

function saveItems_(sheet, email, name, track, items) {
  var map = indexKeys_(sheet, 15);
  var fresh = [];
  items.forEach(function (it) {
    if (!it || !it.id) return;
    var key = email + '|' + track + '|' + it.id;
    var t = Number(it.t) || Date.now();
    var correct = (it.type === 'quiz') ? !!it.correct : '';
    var wrong = (it.type === 'quiz') ? (Number(it.wrong) || 0) : '';
    var row = map[key];
    if (row) {
      var existing = sheet.getRange(row, 1).getValue();
      var existingMs = existing instanceof Date ? existing.getTime() : 0;
      if (t < existingMs - 1000) return; // an older device must not overwrite newer work
      sheet.getRange(row, 1).setValue(new Date(t));
      sheet.getRange(row, 3).setValue(name);
      sheet.getRange(row, 9, 1, 3).setValues([[clean_(it.answer), correct, wrong]]);
    } else {
      fresh.push([new Date(t), email, name, track, Number(it.module) || '', it.id, clean_(it.type, 20),
                  clean_(it.prompt, 500), clean_(it.answer), correct, wrong, '', '', '', key]);
    }
  });
  if (fresh.length) {
    var start = sheet.getLastRow() + 1;
    sheet.getRange(start, 8, fresh.length, 2).setNumberFormat('@'); // before writing values
    sheet.getRange(start, 1, fresh.length, 15).setValues(fresh);
  }
}

function saveProgress_(sheet, email, name, track, rows, now) {
  var map = indexKeys_(sheet, 14);
  var fresh = [];
  rows.forEach(function (r) {
    var key = email + '|' + track + '|' + r.module;
    var vals = [now, email, name, track, Number(r.module), clean_(r.title, 200), clean_(r.status, 20),
                Number(r.checklistDone) || 0, Number(r.checklistTotal) || 0,
                Number(r.quizCorrect) || 0, Number(r.quizTotal) || 0,
                Number(r.fieldsFilled) || 0, Number(r.fieldsTotal) || 0, key];
    if (map[key]) sheet.getRange(map[key], 1, 1, 14).setValues([vals]);
    else fresh.push(vals);
  });
  if (fresh.length) sheet.getRange(sheet.getLastRow() + 1, 1, fresh.length, 14).setValues(fresh);
}

function saveMember_(sheet, email, name, track, last, complete, now) {
  var key = email + '|' + track;
  var row = indexKeys_(sheet, 8)[key];
  var completed = complete ? clean_(complete, 10) : '';
  if (row) {
    var cur = sheet.getRange(row, 7).getValue();
    sheet.getRange(row, 2).setValue(name);
    sheet.getRange(row, 5).setValue(now);
    if (Number(last) > 0) sheet.getRange(row, 6).setValue(Number(last));
    if (completed && !cur) sheet.getRange(row, 7).setValue(completed);
  } else {
    sheet.appendRow([email, name, track, now, now, Number(last) || 1, completed, key]);
  }
}

/* ------------------------------------------------------------ load (resume) */

function load_(q) {
  var track = String(q.track || '').toLowerCase();
  var email = String(q.email || '').trim().toLowerCase();
  if (!TRACKS[track] || !email) throw new Error('Missing track or email');

  var ss = ss_();
  var out = { ok: true, items: [], last: 0, complete: '' };

  var sheet = ss.getSheetByName(SHEETS.responses);
  var last = sheet.getLastRow();
  if (last >= 2) {
    var vals = sheet.getRange(2, 1, last - 1, 15).getValues();
    var prefix = email + '|' + track + '|';
    vals.forEach(function (r) {
      if (String(r[14]).indexOf(prefix) !== 0) return;
      var updated = r[0] instanceof Date ? r[0].getTime() : 0;
      var item = {
        id: r[5], type: r[6], answer: r[8], t: updated,
        correct: r[6] === 'quiz' ? (r[9] === true || String(r[9]).toUpperCase() === 'TRUE') : null,
        wrong: Number(r[10]) || 0
      };
      if (r[11]) item.review = { status: r[11], notes: r[13] || '' };
      out.items.push(item);
    });
  }

  var members = ss.getSheetByName(SHEETS.members);
  var mrow = indexKeys_(members, 8)[email + '|' + track];
  if (mrow) {
    var m = members.getRange(mrow, 1, 1, 8).getValues()[0];
    out.last = Number(m[5]) || 0;
    out.complete = m[6] instanceof Date ? Utilities.formatDate(m[6], Session.getScriptTimeZone(), 'yyyy-MM-dd') : String(m[6] || '');
  }
  return out;
}
