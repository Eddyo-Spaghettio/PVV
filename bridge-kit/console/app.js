/**
 * PVV Bridge Kit Console
 * Loads client/kit JSON, edits in browser, exports for git commit.
 */

const BASE = new URL('.', window.location.href);
const DATA = new URL('../data/', BASE);

let clientsIndex = [];
let currentSlug = null;
let client = null;
let kit = null;
let dirty = false;

const CHECKLIST_LABELS = {
  reachPage: 'Reach Page built',
  qrFlyer: 'QR flyer generated & printed',
  stanfordPack: 'Stanford Channel Pack ready',
  contentCalendar: '90-day calendar filled',
  liaisonAssigned: 'Assigned Liaison named',
  clientApproved: 'Client director approved',
  handoffDoc: 'Handoff doc delivered',
};

const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => document.querySelectorAll(sel);

async function fetchJson(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`Failed to load ${url}`);
  return res.json();
}

function toast(msg) {
  const el = $('#toast');
  el.textContent = msg;
  el.classList.add('show');
  setTimeout(() => el.classList.remove('show'), 2800);
}

function downloadJson(filename, obj) {
  const blob = new Blob([JSON.stringify(obj, null, 2)], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = filename;
  a.click();
  URL.revokeObjectURL(a.href);
}

function reachPageUrl(slug) {
  const origin = window.location.origin + window.location.pathname.replace(/console\/?.*$/, '');
  return `${origin}reach/${slug}/`;
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function renderPreviewHtml(c) {
  const b = c.brand;
  const vol = c.links.volunteerForm || c.links.volunteer;
  const programs = (c.programs || []).map((p) => `<li>${escapeHtml(p)}</li>`).join('');
  const hero = c.heroImage ? `background-image:url('${escapeHtml(c.heroImage)}')` : `background:${escapeHtml(b.primary)}`;

  return `<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="${new URL('../assets/reach.css', BASE).href}">
<style>:root{--primary:${b.primary};--accent:${b.accent};--text:${b.text};--bg:${b.background||'#fafafa'}}</style></head>
<body>
<header class="site-header"><img class="logo" src="${escapeHtml(b.logo)}" alt="logo"></header>
<section class="hero" style="${hero}"><div class="hero-content"><h1>${escapeHtml(c.name)}</h1><p class="tagline">${escapeHtml(c.tagline)}</p></div></section>
<main>
<div class="stat-card"><div class="value">${escapeHtml(c.impactStat?.value)}</div><div class="label">${escapeHtml(c.impactStat?.label)}</div></div>
<p class="mission">${escapeHtml(c.mission)}</p>
<div class="cta-group">
<a class="cta cta-primary" href="${escapeHtml(vol)}">Volunteer</a>
<a class="cta cta-accent" href="${escapeHtml(c.links.donate)}">Donate</a>
<a class="cta cta-outline" href="tel:${escapeHtml(c.links.phone)}">Call</a>
</div>
<section class="programs"><h2>Programs</h2><ul>${programs}</ul></section>
</main></body></html>`;
}

function updatePreview() {
  const iframe = $('#previewFrame');
  if (!iframe || !client) return;
  iframe.srcdoc = renderPreviewHtml(client);
}

function updateProgress() {
  if (!kit?.checklist) return;
  const keys = Object.keys(CHECKLIST_LABELS);
  const done = keys.filter((k) => kit.checklist[k]).length;
  const pct = Math.round((done / keys.length) * 100);
  $('#progressFill').style.width = pct + '%';
  $('#progressLabel').textContent = `${done}/${keys.length} complete (${pct}%)`;
}

function renderChecklist() {
  const ul = $('#checklist');
  ul.innerHTML = '';
  for (const [key, label] of Object.entries(CHECKLIST_LABELS)) {
    const li = document.createElement('li');
    const cb = document.createElement('input');
    cb.type = 'checkbox';
    cb.checked = !!kit.checklist[key];
    cb.addEventListener('change', () => {
      kit.checklist[key] = cb.checked;
      markDirty();
      updateProgress();
    });
    li.appendChild(cb);
    li.appendChild(document.createTextNode(label));
    ul.appendChild(li);
  }
  updateProgress();
}

function renderClientForm() {
  const f = $('#clientForm');
  f.innerHTML = `
    <div class="grid-2">
      <div><label>Organization name</label><input id="c_name" value="${escapeHtml(client.name)}"></div>
      <div><label>Tagline</label><input id="c_tagline" value="${escapeHtml(client.tagline)}"></div>
    </div>
    <label>Mission (English)</label><textarea id="c_mission">${escapeHtml(client.mission)}</textarea>
    <label>Mission (Spanish)</label><textarea id="c_missionEs">${escapeHtml(client.missionEs || '')}</textarea>
    <div class="grid-2">
      <div><label>Impact stat value</label><input id="c_statVal" value="${escapeHtml(client.impactStat?.value)}"></div>
      <div><label>Impact stat label</label><input id="c_statLabel" value="${escapeHtml(client.impactStat?.label)}"></div>
    </div>
    <label>Programs (one per line)</label><textarea id="c_programs" rows="6">${(client.programs || []).join('\n')}</textarea>
    <div class="grid-2">
      <div><label>Primary color</label><input id="c_primary" type="text" value="${escapeHtml(client.brand?.primary)}"></div>
      <div><label>Accent color</label><input id="c_accent" type="text" value="${escapeHtml(client.brand?.accent)}"></div>
    </div>
    <label>Logo URL</label><input id="c_logo" type="url" value="${escapeHtml(client.brand?.logo)}">
    <label>Hero image URL</label><input id="c_hero" type="url" value="${escapeHtml(client.heroImage || '')}">
    <label>Donate link</label><input id="c_donate" type="url" value="${escapeHtml(client.links?.donate)}">
    <label>Volunteer link (website page)</label><input id="c_volunteer" type="url" value="${escapeHtml(client.links?.volunteer)}">
    <label>Volunteer form (Google Form - overrides volunteer link on Reach Page)</label><input id="c_volForm" type="url" value="${escapeHtml(client.links?.volunteerForm || '')}" placeholder="https://docs.google.com/forms/...">
    <div class="grid-2">
      <div><label>Phone (tel link, digits only)</label><input id="c_phone" value="${escapeHtml(client.links?.phone)}"></div>
      <div><label>Phone (display)</label><input id="c_phoneDisp" value="${escapeHtml(client.links?.phoneDisplay)}"></div>
    </div>
    <label>Address</label><input id="c_address" value="${escapeHtml(client.links?.address)}">
    <label>Footer note</label><input id="c_footer" value="${escapeHtml(client.footerNote || '')}">
  `;

  f.querySelectorAll('input, textarea').forEach((el) => {
    el.addEventListener('input', syncClientFromForm);
  });
}

function syncClientFromForm() {
  client.name = $('#c_name').value;
  client.tagline = $('#c_tagline').value;
  client.mission = $('#c_mission').value;
  client.missionEs = $('#c_missionEs').value;
  client.impactStat = { value: $('#c_statVal').value, label: $('#c_statLabel').value };
  client.programs = $('#c_programs').value.split('\n').map((s) => s.trim()).filter(Boolean);
  client.brand.primary = $('#c_primary').value;
  client.brand.accent = $('#c_accent').value;
  client.brand.logo = $('#c_logo').value;
  client.heroImage = $('#c_hero').value;
  client.links.donate = $('#c_donate').value;
  client.links.volunteer = $('#c_volunteer').value;
  client.links.volunteerForm = $('#c_volForm').value;
  client.links.phone = $('#c_phone').value;
  client.links.phoneDisplay = $('#c_phoneDisp').value;
  client.links.address = $('#c_address').value;
  client.footerNote = $('#c_footer').value;
  markDirty();
  updatePreview();
  updateQrFlyer();
}

function renderLiaisonMetrics() {
  $('#liaisonName').value = kit.liaison?.name || '';
  $('#liaisonEmail').value = kit.liaison?.email || '';
  $('#metricVisits').value = kit.metrics?.pageVisits ?? '';
  $('#metricSignups').value = kit.metrics?.volunteerSignups ?? '';
  $('#metricAttendees').value = kit.metrics?.stanfordAttendees ?? '';
  $('#metricPosts').value = kit.metrics?.postsPublished ?? '';
  $('#kitNotes').value = kit.notes || '';
}

function renderStanfordPack() {
  const url = reachPageUrl(currentSlug);
  let body = kit.stanfordPack?.service4allBody || '';
  body = body.replace('[REACH PAGE URL]', url);
  body = body.replace('[LIAISON NAME]', kit.liaison?.name || '[LIAISON NAME]');
  body = body.replace('[LIAISON EMAIL]', kit.liaison?.email || '[LIAISON EMAIL]');

  $('#s4allSubject').value = kit.stanfordPack?.service4allSubject || '';
  $('#s4allBody').value = body;
  $('#ceTitle').value = kit.stanfordPack?.cardinalEngageTitle || '';
  $('#ceDesc').value = kit.stanfordPack?.cardinalEngageDescription || '';

  $('#s4allPreview').textContent = `Subject: ${$('#s4allSubject').value}\n\n${$('#s4allBody').value}`;
}

function renderCalendar() {
  const tbody = $('#calendarBody');
  tbody.innerHTML = '';
  (kit.calendar || []).forEach((row, i) => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>Wk ${row.week}</td>
      <td>${escapeHtml(row.platform)}</td>
      <td>${escapeHtml(row.type)}</td>
      <td><textarea class="post-input" data-i="${i}" data-field="draft">${escapeHtml(row.draft)}</textarea></td>
      <td><input type="checkbox" data-i="${i}" data-field="done" ${row.done ? 'checked' : ''}></td>
    `;
    tbody.appendChild(tr);
  });

  tbody.querySelectorAll('[data-i]').forEach((el) => {
    el.addEventListener('input', () => {
      const i = +el.dataset.i;
      kit.calendar[i][el.dataset.field] = el.type === 'checkbox' ? el.checked : el.value;
      markDirty();
    });
    el.addEventListener('change', () => {
      const i = +el.dataset.i;
      kit.calendar[i][el.dataset.field] = el.checked;
      markDirty();
    });
  });
}

function updateQrFlyer() {
  if (!client) return;
  const url = reachPageUrl(currentSlug);
  $('#qrUrl').textContent = url;
  $('#flyerTitle').textContent = client.name;
  $('#flyerImpact').textContent = client.impactStat
    ? `${client.impactStat.value} ${client.impactStat.label}`
    : client.tagline;

  const canvas = $('#qrCanvas');
  if (!canvas) return;
  const draw = () => {
    if (!window.QRCode) return;
    QRCode.toCanvas(canvas, url, { width: 180, margin: 2, color: { dark: client.brand?.primary || '#009900' } }, (err) => {
      if (err) console.error(err);
    });
  };
  if (window.QRCode) draw();
  else setTimeout(draw, 500);
}

function markDirty() {
  dirty = true;
  localStorage.setItem(`pvv-draft-${currentSlug}`, JSON.stringify({ client, kit }));
}

async function loadClient(slug) {
  currentSlug = slug;
  dirty = false;

  const draft = localStorage.getItem(`pvv-draft-${slug}`);
  if (draft) {
    try {
      const parsed = JSON.parse(draft);
      client = parsed.client;
      kit = parsed.kit;
      toast('Loaded saved draft from browser');
    } catch (_) { /* fall through */ }
  }

  if (!client) {
    [client, kit] = await Promise.all([
      fetchJson(new URL(`clients/${slug}.json`, DATA)),
      fetchJson(new URL(`kits/${slug}.json`, DATA)),
    ]);
  }

  $('#clientTitle').textContent = client.name;
  $$('.client-list button').forEach((b) => b.classList.toggle('active', b.dataset.slug === slug));

  renderChecklist();
  renderClientForm();
  renderLiaisonMetrics();
  renderStanfordPack();
  renderCalendar();
  updatePreview();
  updateQrFlyer();
}

function syncKitFromOverview() {
  kit.liaison = { name: $('#liaisonName').value, email: $('#liaisonEmail').value, notes: kit.liaison?.notes || '' };
  kit.metrics = {
    pageVisits: $('#metricVisits').value ? +$('#metricVisits').value : null,
    volunteerSignups: $('#metricSignups').value ? +$('#metricSignups').value : null,
    stanfordAttendees: $('#metricAttendees').value ? +$('#metricAttendees').value : null,
    postsPublished: +$('#metricPosts').value || 0,
    lastUpdated: new Date().toISOString().split('T')[0],
  };
  kit.notes = $('#kitNotes').value;
  kit.stanfordPack = {
    service4allSubject: $('#s4allSubject').value,
    service4allBody: $('#s4allBody').value,
    cardinalEngageTitle: $('#ceTitle').value,
    cardinalEngageDescription: $('#ceDesc').value,
  };
}

function exportAll() {
  syncClientFromForm();
  syncKitFromOverview();
  downloadJson(`client-${currentSlug}.json`, client);
  setTimeout(() => downloadJson(`kit-${currentSlug}.json`, kit), 300);
  toast('Downloaded client-{slug}.json and kit-{slug}.json → place in data/clients/ and data/kits/');
}

function exportCalendarCsv() {
  const rows = [['Week', 'Platform', 'Type', 'Draft', 'Visual', 'Done']];
  (kit.calendar || []).forEach((r) => {
    rows.push([r.week, r.platform, r.type, r.draft, r.visual || '', r.done ? 'yes' : 'no']);
  });
  const csv = rows.map((r) => r.map((c) => `"${String(c).replace(/"/g, '""')}"`).join(',')).join('\n');
  const blob = new Blob([csv], { type: 'text/csv' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `${currentSlug}-calendar.csv`;
  a.click();
  toast('Calendar exported as CSV');
}

function downloadFlyerPng() {
  const wrap = $('#flyerExport');
  html2canvas(wrap, { scale: 2, backgroundColor: '#ffffff' }).then((canvas) => {
    const a = document.createElement('a');
    a.download = `${currentSlug}-qr-flyer.png`;
    a.href = canvas.toDataURL('image/png');
    a.click();
    toast('Flyer downloaded');
    kit.checklist.qrFlyer = true;
    renderChecklist();
  });
}

function copyStanfordEmail() {
  const text = `Subject: ${$('#s4allSubject').value}\n\n${$('#s4allBody').value}`;
  navigator.clipboard.writeText(text).then(() => toast('Copied to clipboard'));
}

function switchTab(name) {
  $$('.tabs button').forEach((b) => b.classList.toggle('active', b.dataset.tab === name));
  $$('.panel').forEach((p) => p.classList.toggle('active', p.id === `panel-${name}`));
  if (name === 'preview') updatePreview();
  if (name === 'qr') updateQrFlyer();
}

async function init() {
  const index = await fetchJson(new URL('clients/index.json', DATA));
  clientsIndex = index.clients;
  const ul = $('#clientList');
  ul.innerHTML = '';

  clientsIndex.forEach((c) => {
    const btn = document.createElement('button');
    btn.textContent = c.name;
    btn.dataset.slug = c.slug;
    btn.addEventListener('click', () => loadClient(c.slug));
    ul.appendChild(btn);
  });

  $$('.tabs button').forEach((b) => {
    b.addEventListener('click', () => switchTab(b.dataset.tab));
  });

  $('#exportBtn').addEventListener('click', exportAll);
  $('#exportCalBtn').addEventListener('click', exportCalendarCsv);
  $('#downloadFlyerBtn').addEventListener('click', downloadFlyerPng);
  $('#copyEmailBtn').addEventListener('click', copyStanfordEmail);
  $('#openReachBtn').addEventListener('click', () => window.open(reachPageUrl(currentSlug), '_blank'));

  ['liaisonName', 'liaisonEmail', 'metricVisits', 'metricSignups', 'metricAttendees', 'metricPosts', 'kitNotes', 's4allSubject', 's4allBody', 'ceTitle', 'ceDesc'].forEach((id) => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('input', () => { syncKitFromOverview(); markDirty(); });
  });

  if (clientsIndex.length) await loadClient(clientsIndex[0].slug);
}

init().catch((err) => {
  console.error(err);
  $('.content').innerHTML = `<div class="card"><p>Could not load data. Run <code>npm run build</code> first, then serve the <code>site/</code> folder.</p><p>${escapeHtml(err.message)}</p></div>`;
});
