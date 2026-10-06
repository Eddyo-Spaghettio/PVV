#!/usr/bin/env python3
"""Add a partners logo grid section to the PVV homepage."""

import json
import base64
import os
import re
import urllib.request
import urllib.error

BASE = "https://pvv.su.domains/wp-json/wp/v2"
USER = os.environ.get("WP_USER", "edyeres")
PASSWORD = os.environ["WP_APP_PASSWORD"]
SITE = "https://pvv.su.domains"

PARTNERS = [
    ("Eastside Community Pantry", "Food security · East Palo Alto"),
    ("Partner Organization 2", "Community services · Bay Area"),
    ("Partner Organization 3", "Youth programs · Peninsula"),
    ("Partner Organization 4", "Housing support · South Bay"),
    ("Partner Organization 5", "Health access · Bay Area"),
    ("Partner Organization 6", "Education · Bay Area"),
]


def auth_header():
    token = base64.b64encode(f"{USER}:{PASSWORD}".encode()).decode()
    return {"Authorization": f"Basic {token}", "Content-Type": "application/json"}


def api(method, path, data=None):
    url = f"{BASE}{path}"
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, headers=auth_header(), method=method)
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{method} {path} ({e.code}): {e.read().decode()}") from e


def partner_card(name, blurb):
    return f"""<!-- wp:group {{"className":"pvv-partner-card pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"radius":"8px","width":"1px"}},"borderColor":"accent-6"}},"backgroundColor":"base","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-partner-card pvv-card has-border-color has-accent-6-border-color has-base-background-color has-background" style="border-width:1px;border-radius:8px;padding-top:var(--wp--preset--spacing--30);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30);padding-left:var(--wp--preset--spacing--30)"><!-- wp:group {{"className":"pvv-partner-logo","layout":{{"type":"flex","flexWrap":"nowrap","justifyContent":"center","verticalAlignment":"center"}}}} -->
<div class="wp-block-group pvv-partner-logo"><!-- wp:paragraph {{"align":"center","fontSize":"small"}} -->
<p class="has-text-align-center has-small-font-size"><em>Logo</em></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:heading {{"textAlign":"center","level":4,"fontSize":"medium"}} -->
<h4 class="wp-block-heading has-text-align-center has-medium-font-size">{name}</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {{"align":"center","fontSize":"small"}} -->
<p class="has-text-align-center has-small-font-size">{blurb}</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->"""


def build_partners_section():
    cards = "\n\n".join(partner_card(name, blurb) for name, blurb in PARTNERS)
    return f"""
<!-- wp:group {{"align":"full","className":"pvv-partners-section","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|70","bottom":"var:preset|spacing|70","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignfull pvv-partners-section has-accent-5-background-color has-background" style="padding-top:var(--wp--preset--spacing--70);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--70);padding-left:var(--wp--preset--spacing--50)"><!-- wp:heading {{"textAlign":"center","level":2}} -->
<h2 class="wp-block-heading has-text-align-center">Our Partners</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {{"align":"center","fontSize":"small"}} -->
<p class="has-text-align-center has-small-font-size">Bay Area nonprofits and community organizations we have worked with. Replace each logo placeholder with an image and update the text in the editor.</p>
<!-- /wp:paragraph -->

<!-- wp:group {{"align":"wide","className":"pvv-partners-grid","style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}},"blockGap":"var:preset|spacing|30"}}}},"layout":{{"type":"default"}}}} -->
<div class="wp-block-group alignwide pvv-partners-grid" style="margin-top:var(--wp--preset--spacing--50)">
{cards}
</div>
<!-- /wp:group -->

<!-- wp:paragraph {{"align":"center","fontSize":"small","style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<p class="has-text-align-center has-small-font-size" style="margin-top:var(--wp--preset--spacing--50)">Interested in partnering? <a href="{SITE}/for-nonprofits/">Learn how to work with PVV →</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
"""


PARTNER_CSS = """
  .pvv-partners-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: var(--wp--preset--spacing--30);
  }
  .pvv-partner-card {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    height: 100%;
    text-align: center;
  }
  .pvv-partner-logo {
    min-height: 96px;
    margin-bottom: var(--wp--preset--spacing--20);
    padding: var(--wp--preset--spacing--20);
    border: 1px dashed var(--pvv-gold);
    border-radius: 8px;
    background: rgba(196, 163, 90, 0.06);
  }
  .pvv-partner-logo img {
    max-height: 72px;
    max-width: 100%;
    width: auto;
    height: auto;
    object-fit: contain;
    display: block;
    margin: 0 auto;
  }
  .pvv-partner-card .wp-block-heading {
    margin-top: 0;
    margin-bottom: 0.35rem;
  }
  .pvv-partner-card p.has-small-font-size:last-child {
    margin-bottom: 0;
    color: inherit;
    opacity: 0.85;
  }
  @media (max-width: 900px) {
    .pvv-partners-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  }
  @media (max-width: 560px) {
    .pvv-partners-grid { grid-template-columns: 1fr; }
  }
"""


def patch_header_css(header_content):
    if ".pvv-partners-grid" in header_content:
        return header_content
    return header_content.replace("</style>", PARTNER_CSS + "\n</style>", 1)


def patch_home(content):
    if "pvv-partners-section" in content or "Our Partners" in content:
        return content, False
    marker = '<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|80","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}},"backgroundColor":"contrast","textColor":"base","layout":{"type":"constrained"}} -->'
    idx = content.rfind(marker)
    if idx == -1:
        raise RuntimeError("Could not find CTA section marker on home page")
    section = build_partners_section().strip()
    return content[:idx] + section + "\n\n" + content[idx:], True


def main():
    pages = api("GET", "/pages?slug=home&context=edit")
    home = pages[0]
    updated, changed = patch_home(home["content"]["raw"])
    if not changed:
        print("Partners section already present on home")
    else:
        api("POST", f"/pages/{home['id']}", {"content": updated, "template": "page-no-title"})
        print(f"Updated home (id={home['id']}) with partners section")

    header = api("GET", "/template-parts/twentytwentyfive//header?context=edit")
    new_header = patch_header_css(header["content"]["raw"])
    if new_header != header["content"]["raw"]:
        api("POST", "/template-parts/twentytwentyfive//header", {"content": new_header})
        print("Updated header CSS for partners grid")
    else:
        print("Header CSS already includes partners styles")

    print("Done!")


if __name__ == "__main__":
    main()
