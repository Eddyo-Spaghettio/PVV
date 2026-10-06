#!/usr/bin/env python3
"""Add black/white/gold accent styling via site-wide CSS."""

import json
import base64
import os
import re
import urllib.request

USER = os.environ.get("WP_USER", "edyeres")
PASSWORD = os.environ["WP_APP_PASSWORD"]

GOLD_CSS = """
<style>
  :root {
    --pvv-gold: #C4A35A;
    --pvv-gold-light: #E2CFA0;
    --pvv-gold-bright: #D4AF37;
    --pvv-gold-subtle: rgba(196, 163, 90, 0.18);
    --pvv-black: #111111;
  }

  @keyframes pvv-fade-up {
    from { opacity: 0; transform: translateY(28px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @keyframes pvv-fade-in {
    from { opacity: 0; }
    to   { opacity: 1; }
  }
  @keyframes pvv-hero-glow {
    0%, 100% { opacity: 0.35; }
    50%       { opacity: 0.65; }
  }

  .pvv-hero-animate {
    animation: pvv-fade-up 0.9s cubic-bezier(0.22, 1, 0.36, 1) both;
  }
  .pvv-hero-animate-d1 { animation-delay: 0.12s; }
  .pvv-hero-animate-d2 { animation-delay: 0.24s; }
  .pvv-hero-animate-d3 { animation-delay: 0.36s; }
  .pvv-fade-in { animation: pvv-fade-in 1s ease both; }

  .pvv-card {
    transition: transform 0.28s cubic-bezier(0.22, 1, 0.36, 1),
                box-shadow 0.28s ease,
                border-color 0.28s ease;
  }
  .pvv-card:hover {
    transform: translateY(-6px);
    border-color: var(--pvv-gold) !important;
    box-shadow: 0 16px 40px rgba(196, 163, 90, 0.14);
  }

  .pvv-mission-glow::before {
    content: "";
    position: absolute;
    inset: -1px;
    border-radius: inherit;
    background: linear-gradient(135deg, transparent 40%, rgba(226, 207, 160, 0.08) 100%);
    animation: pvv-hero-glow 4s ease-in-out infinite;
    pointer-events: none;
  }

  /* Header border */
  header .wp-block-group.alignfull[style*="border-bottom"] {
    border-bottom-color: var(--pvv-gold) !important;
  }

  /* Site title & nav */
  .wp-block-site-title a {
    transition: color 0.2s ease;
  }
  .wp-block-site-title a:hover {
    color: var(--pvv-gold-bright) !important;
  }
  .wp-block-navigation-item__content {
    transition: color 0.2s ease;
  }
  .wp-block-navigation-item__content:hover {
    color: var(--pvv-gold-bright) !important;
  }

  /* Hero eyebrow label */
  .has-contrast-background-color p.has-small-font-size[style*="uppercase"] {
    color: var(--pvv-gold-light) !important;
  }

  /* Content links */
  main a:not(.wp-element-button) {
    transition: color 0.2s ease;
  }
  main a:not(.wp-element-button):hover {
    color: var(--pvv-gold-bright);
  }
  .has-contrast-background-color a:not(.wp-element-button) {
    color: var(--pvv-gold-light);
  }
  .has-contrast-background-color a:not(.wp-element-button):hover {
    color: var(--pvv-gold-bright);
  }

  /* Buttons on dark sections */
  .has-contrast-background-color .wp-block-button:not(.is-style-outline) .wp-block-button__link.has-base-background-color {
    background-color: var(--pvv-gold-light) !important;
    color: var(--pvv-black) !important;
    font-weight: 600;
  }
  .has-contrast-background-color .wp-block-button:not(.is-style-outline) .wp-block-button__link.has-base-background-color:hover {
    background-color: var(--pvv-gold-bright) !important;
  }
  .has-contrast-background-color .wp-block-button.is-style-outline .wp-block-button__link {
    border-color: var(--pvv-gold-light) !important;
    color: var(--pvv-gold-light) !important;
  }
  .has-contrast-background-color .wp-block-button.is-style-outline .wp-block-button__link:hover {
    background-color: var(--pvv-gold-subtle) !important;
    border-color: var(--pvv-gold-bright) !important;
    color: var(--pvv-gold-bright) !important;
  }

  /* Buttons on light sections */
  main .wp-block-button:not(.is-style-outline) .wp-block-button__link.wp-element-button {
    transition: background-color 0.2s ease, color 0.2s ease;
  }
  main .has-accent-5-background-color .wp-block-button .wp-block-button__link,
  main .wp-block-group:not(.has-contrast-background-color) .wp-block-button:not(.is-style-outline) .wp-block-button__link:not(.has-base-background-color) {
    background-color: var(--pvv-black) !important;
    color: #ffffff !important;
  }
  main .has-accent-5-background-color .wp-block-button .wp-block-button__link:hover,
  main .wp-block-group:not(.has-contrast-background-color) .wp-block-button:not(.is-style-outline) .wp-block-button__link:not(.has-base-background-color):hover {
    background-color: var(--pvv-gold) !important;
    color: var(--pvv-black) !important;
  }

  /* Mission & highlight boxes */
  main .has-accent-5-background-color.pvv-fade-in,
  main .pvv-mission-glow .has-accent-5-background-color {
    border-left: 3px solid var(--pvv-gold);
  }

  /* Section heading underline */
  main h2.has-text-align-center::after {
    content: "";
    display: block;
    width: 52px;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--pvv-gold), transparent);
    margin: 0.85rem auto 0;
  }

  /* FAQ accordion */
  details.pvv-faq-item {
    border-left: 3px solid transparent;
    padding-left: 1rem;
    margin-bottom: 0.5rem;
    transition: border-color 0.25s ease;
  }
  details.pvv-faq-item[open] {
    border-left-color: var(--pvv-gold);
  }
  details.pvv-faq-item summary {
    cursor: pointer;
    transition: color 0.2s ease;
  }
  details.pvv-faq-item summary:hover {
    color: var(--pvv-gold-bright);
  }

  /* Footer */
  footer.has-accent-5-background-color,
  .has-accent-5-background-color[style*="border-top"] {
    border-top-color: var(--pvv-gold) !important;
  }
  footer a:hover {
    color: var(--pvv-gold-bright) !important;
  }

  .wp-block-separator {
    border-color: var(--pvv-gold-subtle) !important;
  }

  @media (prefers-reduced-motion: reduce) {
    .pvv-hero-animate, .pvv-hero-animate-d1, .pvv-hero-animate-d2,
    .pvv-hero-animate-d3, .pvv-fade-in, .pvv-mission-glow::before {
      animation: none !important;
      opacity: 1 !important;
      transform: none !important;
    }
    .pvv-card { transition: none; }
    .pvv-card:hover { transform: none; }
  }
</style>
"""


def auth_header():
    token = base64.b64encode(f"{USER}:{PASSWORD}".encode()).decode()
    return {"Authorization": f"Basic {token}", "Content-Type": "application/json"}


def api(method, path, data=None):
    url = f"https://pvv.su.domains/wp-json/wp/v2{path}"
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, headers=auth_header(), method=method)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def main():
    header = api("GET", "/template-parts/twentytwentyfive//header?context=edit")
    content = header["content"]["raw"]

    # Replace existing wp:html style block or prepend new one
    html_block = f"<!-- wp:html -->\n{GOLD_CSS}\n<!-- /wp:html -->"
    if "<!-- wp:html -->" in content:
        content = re.sub(
            r"<!-- wp:html -->.*?<!-- /wp:html -->",
            html_block.strip(),
            content,
            count=1,
            flags=re.DOTALL,
        )
    else:
        content = html_block + "\n\n" + content

    api("POST", "/template-parts/twentytwentyfive//header", {"content": content})
    print("Applied gold accent CSS to site header (global styles)")


if __name__ == "__main__":
    main()
