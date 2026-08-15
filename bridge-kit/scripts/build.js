#!/usr/bin/env node
/**
 * Bridge Kit build - reads client JSON, outputs static Reach Pages + deploy bundle.
 * Usage: node scripts/build.js
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const DATA_CLIENTS = path.join(ROOT, 'data', 'clients');
const SITE = path.join(ROOT, 'site');
const ASSETS_SRC = path.join(ROOT, 'scripts', 'assets');

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function volunteerUrl(client) {
  return client.links.volunteerForm || client.links.volunteer;
}

function renderReachPage(client) {
  const b = client.brand;
  const programs = client.programs
    .map((p) => `<li>${escapeHtml(p)}</li>`)
    .join('\n          ');

  const missionEsBlock = client.bilingual && client.missionEs
    ? `<div class="mission-es" id="missionEs" hidden>${escapeHtml(client.missionEs)}</div>
        <button type="button" class="lang-toggle" id="langToggle" aria-pressed="false">Ver en español</button>`
    : '';

  const social = [];
  if (client.links.facebook) social.push(`<a href="${escapeHtml(client.links.facebook)}" target="_blank" rel="noopener">Facebook</a>`);
  if (client.links.instagram) social.push(`<a href="${escapeHtml(client.links.instagram)}" target="_blank" rel="noopener">Instagram</a>`);
  if (client.links.website) social.push(`<a href="${escapeHtml(client.links.website)}" target="_blank" rel="noopener">Website</a>`);

  const emailLine = client.links.email
    ? `<p><a href="mailto:${escapeHtml(client.links.email)}">${escapeHtml(client.links.email)}</a></p>`
    : '';

  const heroStyle = client.heroImage
    ? `background-image: url('${escapeHtml(client.heroImage)}');`
    : `background: ${escapeHtml(b.primary)};`;

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="${escapeHtml(client.mission.slice(0, 155))}">
  <title>${escapeHtml(client.name)} - Get Involved</title>
  <link rel="stylesheet" href="../../assets/reach.css">
  <style>
    :root {
      --primary: ${escapeHtml(b.primary)};
      --accent: ${escapeHtml(b.accent)};
      --text: ${escapeHtml(b.text)};
      --bg: ${escapeHtml(b.background || '#fafafa')};
    }
  </style>
</head>
<body>
  <header class="site-header">
    <img class="logo" src="${escapeHtml(client.brand.logo)}" alt="${escapeHtml(client.name)} logo" width="200" height="64">
  </header>

  <section class="hero" style="${heroStyle}">
    <div class="hero-content">
      <h1>${escapeHtml(client.name)}</h1>
      <p class="tagline">${escapeHtml(client.tagline)}</p>
    </div>
  </section>

  <main>
    <div class="stat-card">
      <div class="value">${escapeHtml(client.impactStat.value)}</div>
      <div class="label">${escapeHtml(client.impactStat.label)}</div>
    </div>

    <p class="mission" id="missionEn">${escapeHtml(client.mission)}</p>
    ${missionEsBlock}

    <div class="cta-group">
      <a class="cta cta-primary" href="${escapeHtml(volunteerUrl(client))}" target="_blank" rel="noopener">
        ${escapeHtml(client.cta.volunteerLabel)}
      </a>
      <a class="cta cta-accent" href="${escapeHtml(client.links.donate)}" target="_blank" rel="noopener">
        ${escapeHtml(client.cta.donateLabel)}
      </a>
      <a class="cta cta-outline" href="tel:${escapeHtml(client.links.phone)}">
        ${escapeHtml(client.cta.contactLabel)} · ${escapeHtml(client.links.phoneDisplay)}
      </a>
    </div>

    <section class="programs">
      <h2>Our Programs</h2>
      <ul>
          ${programs}
      </ul>
    </section>

    <section class="contact-card">
      <h2>Visit Us</h2>
      <p>${escapeHtml(client.links.address)}</p>
      <p><a href="tel:${escapeHtml(client.links.phone)}">${escapeHtml(client.links.phoneDisplay)}</a></p>
      ${emailLine}
      ${social.length ? `<div class="social-links">${social.join('\n        ')}</div>` : ''}
    </section>
  </main>

  <footer class="site-footer">
    <p>${escapeHtml(client.footerNote || '')}</p>
    <p class="pvv-badge">Reach Page built by <a href="https://haas.stanford.edu" target="_blank" rel="noopener">${escapeHtml(client.pvv?.builtBy || 'Proyecto Vidas Valiosas')}</a></p>
  </footer>

  <script>
    (function () {
      var btn = document.getElementById('langToggle');
      var en = document.getElementById('missionEn');
      var es = document.getElementById('missionEs');
      if (!btn || !es) return;
      btn.addEventListener('click', function () {
        var showEs = en.style.display !== 'none';
        en.style.display = showEs ? 'none' : 'block';
        es.hidden = showEs ? false : true;
        btn.textContent = showEs ? 'View in English' : 'Ver en español';
        btn.setAttribute('aria-pressed', showEs ? 'true' : 'false');
      });
    })();
  </script>
</body>
</html>`;
}

function renderSiteIndex(clients) {
  const cards = clients
    .map(
      (c) => `
    <a class="client-card" href="./reach/${escapeHtml(c.slug)}/">
      <h2>${escapeHtml(c.name)}</h2>
      <span class="arrow">View Reach Page →</span>
    </a>`
    )
    .join('\n');

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PVV Bridge Kit</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f5f5f5; color: #333; line-height: 1.5; }
    .hub { max-width: 560px; margin: 0 auto; padding: 2rem 1.25rem; }
    .hub h1 { font-size: 1.5rem; margin-bottom: 0.25rem; }
    .hub .sub { color: #666; margin-bottom: 2rem; font-size: 0.95rem; }
    .client-card {
      display: block; background: #fff; padding: 1.25rem; border-radius: 12px;
      margin-bottom: 0.75rem; text-decoration: none; color: inherit;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    .client-card h2 { font-size: 1.1rem; color: #009900; margin-bottom: 0.25rem; }
    .client-card .arrow { font-size: 0.85rem; color: #666; }
    .console-link {
      display: inline-block; margin-top: 1.5rem; padding: 0.6rem 1rem;
      background: #1a365d; color: #fff !important; border-radius: 8px;
      text-decoration: none; font-size: 0.9rem;
    }
  </style>
</head>
<body>
  <div class="hub">
    <h1>PVV Bridge Kit</h1>
    <p class="sub">Youth engagement pages for partner nonprofits. Built by Proyecto Vidas Valiosas.</p>
    ${cards || '<p>No clients yet.</p>'}
    <a class="console-link" href="./console/">PVV Console →</a>
  </div>
</body>
</html>`;
}

function copyDir(src, dest) {
  if (!fs.existsSync(src)) return;
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const s = path.join(src, entry.name);
    const d = path.join(dest, entry.name);
    if (entry.isDirectory()) copyDir(s, d);
    else fs.copyFileSync(s, d);
  }
}

function copyFile(src, dest) {
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.copyFileSync(src, dest);
}

function main() {
  console.log('Bridge Kit build starting…');

  if (fs.existsSync(SITE)) fs.rmSync(SITE, { recursive: true });
  fs.mkdirSync(SITE, { recursive: true });

  copyFile(path.join(ASSETS_SRC, 'reach.css'), path.join(SITE, 'assets', 'reach.css'));
  copyDir(path.join(ROOT, 'data', 'clients'), path.join(SITE, 'data', 'clients'));
  copyDir(path.join(ROOT, 'data', 'kits'), path.join(SITE, 'data', 'kits'));
  copyDir(path.join(ROOT, 'console'), path.join(SITE, 'console'));

  const indexData = readJson(path.join(DATA_CLIENTS, 'index.json'));

  for (const entry of indexData.clients) {
    const slug = entry.slug;
    const clientPath = path.join(DATA_CLIENTS, `${slug}.json`);
    if (!fs.existsSync(clientPath)) {
      console.warn(`  skip: missing ${slug}.json`);
      continue;
    }
    const client = readJson(clientPath);
    const html = renderReachPage(client);
    const outDir = path.join(SITE, 'reach', slug);
    fs.mkdirSync(outDir, { recursive: true });
    fs.writeFileSync(path.join(outDir, 'index.html'), html);
    console.log(`  ✓ reach/${slug}/`);
  }

  fs.writeFileSync(path.join(SITE, 'index.html'), renderSiteIndex(indexData.clients));
  console.log('  ✓ site/index.html');
  console.log('Build complete → ./site');
}

main();
