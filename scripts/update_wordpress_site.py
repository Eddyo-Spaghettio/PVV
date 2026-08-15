#!/usr/bin/env python3
"""Update PVV WordPress site content via REST API."""

import json
import base64
import os
import urllib.request
import urllib.error

BASE = "https://pvv.su.domains/wp-json/wp/v2"
USER = os.environ.get("WP_USER", "edyeres")
PASSWORD = os.environ["WP_APP_PASSWORD"]
SITE = "https://pvv.su.domains"


def auth_header():
    token = base64.b64encode(f"{USER}:{PASSWORD}".encode()).decode()
    return {"Authorization": f"Basic {token}", "Content-Type": "application/json"}


def api(method, path, data=None):
    url = f"{BASE}{path}"
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, headers=auth_header(), method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        err = e.read().decode()
        raise RuntimeError(f"{method} {path} failed ({e.code}): {err}") from e


def settings_api(data):
    url = "https://pvv.su.domains/wp-json/wp/v2/settings"
    body = json.dumps(data).encode()
    req = urllib.request.Request(url, data=body, headers=auth_header(), method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


HOME_CONTENT = """
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|80","bottom":"var:preset|spacing|80","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}},"backgroundColor":"contrast","textColor":"base","layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-base-color has-contrast-background-color has-text-color has-background" style="padding-top:var(--wp--preset--spacing--80);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--80);padding-left:var(--wp--preset--spacing--50)"><!-- wp:heading {"textAlign":"center","level":1,"fontSize":"xx-large"} -->
<h1 class="wp-block-heading has-text-align-center has-xx-large-font-size">Proyecto Vidas Valiosas</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","fontSize":"large"} -->
<p class="has-text-align-center has-large-font-size">Stanford's student-led nonprofit consulting group - free marketing, financial, and technical support for community organizations serving low-income communities.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"},"style":{"spacing":{"margin":{"top":"var:preset|spacing|40"}}}} -->
<div class="wp-block-buttons" style="margin-top:var(--wp--preset--spacing--40)"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="SITE/contact/">Partner With Us</a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="SITE/about-us/">Learn About PVV</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->

<!-- wp:group {"align":"wide","style":{"spacing":{"padding":{"top":"var:preset|spacing|70","bottom":"var:preset|spacing|40"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--70);padding-bottom:var(--wp--preset--spacing--40)"><!-- wp:paragraph {"align":"center","fontSize":"medium"} -->
<p class="has-text-align-center has-medium-font-size"><strong>Interested in working with PVV or joining our team?</strong> We connect Stanford students with local nonprofits and community-based organizations across the Bay Area. Reach out to learn how we can help your organization - or how you can get involved.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="mailto:edyeres@stanford.edu">Email Our President</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->

<!-- wp:group {"align":"wide","style":{"spacing":{"padding":{"bottom":"var:preset|spacing|70"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignwide" style="padding-bottom:var(--wp--preset--spacing--70)"><!-- wp:heading {"textAlign":"center"} -->
<h2 class="wp-block-heading has-text-align-center">What We Do</h2>
<!-- /wp:heading -->

<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|50","left":"var:preset|spacing|50"},"margin":{"top":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns alignwide" style="margin-top:var(--wp--preset--spacing--50)"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Marketing Consulting</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We help nonprofits get seen and get support - social media strategy, flyers, event promotion, and outreach to Stanford students through the Haas Center.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Financial Consulting</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We support grant applications, structured budgets, and financial planning so organizations can fund and sustain their programs.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Technical Consulting</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We build websites, forms, surveys, and data pipelines - practical tools that help small nonprofits operate more efficiently.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->

<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|60","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}},"backgroundColor":"accent-5","layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-accent-5-background-color has-background" style="padding-top:var(--wp--preset--spacing--60);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--60);padding-left:var(--wp--preset--spacing--50)"><!-- wp:quote {"align":"center","className":"is-style-plain"} -->
<blockquote class="wp-block-quote has-text-align-center is-style-plain"><!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size">"We connect local nonprofits serving low-income communities with free, student-provided consulting - so organizations can focus on their mission, not their operations."</p>
<!-- /wp:paragraph -->

<!-- wp:citation -->
<cite>Proyecto Vidas Valiosas mission</cite>
<!-- /wp:citation --></blockquote>
<!-- /wp:quote --></div>
<!-- /wp:group -->

<!-- wp:group {"align":"wide","style":{"spacing":{"padding":{"top":"var:preset|spacing|70","bottom":"var:preset|spacing|80"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--70);padding-bottom:var(--wp--preset--spacing--80)"><!-- wp:heading {"textAlign":"center"} -->
<h2 class="wp-block-heading has-text-align-center">Beyond Consulting</h2>
<!-- /wp:heading -->

<!-- wp:columns {"style":{"spacing":{"blockGap":{"left":"var:preset|spacing|40"},"margin":{"top":"var:preset|spacing|40"}}}} -->
<div class="wp-block-columns" style="margin-top:var(--wp--preset--spacing--40)"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Volunteering Events</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We organize service days that bring Stanford students directly to partner nonprofits, with transportation support when available.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Workshops &amp; Training</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Members build real skills through hands-on consulting training across marketing, finance, and technology.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Long-Term Partnerships</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We aim for sustained relationships with community organizations - not one-off projects - to strengthen programs over time.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"},"style":{"spacing":{"margin":{"top":"var:preset|spacing|60"}}}} -->
<div class="wp-block-buttons" style="margin-top:var(--wp--preset--spacing--60)"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="SITE/projects/">See Our Work</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->
""".replace("SITE", SITE)

ABOUT_CONTENT = """
<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size">Proyecto Vidas Valiosas (PVV) is a Stanford student organization that provides <strong>free consulting services</strong> to local nonprofits and community-based organizations serving low-income communities across the Bay Area.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Our Purpose</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We connect community organizations with Stanford students who can help with marketing, financial planning, and technical projects - the operational work that small nonprofits often lack the time, budget, or staff to tackle alone.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Our goal is to strengthen programs that support disadvantaged communities while giving students meaningful, hands-on experience in nonprofit consulting.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Who We Serve</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><li><strong>Nonprofit &amp; CBO partners</strong> - food pantries, legal aid clinics, youth programs, and other organizations working with low-income communities</li><li><strong>Stanford students</strong> - undergraduates and graduate students interested in consulting, public service, and community impact</li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2 class="wp-block-heading">How We Work</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>PVV members join one of three consulting tracks - <strong>Marketing</strong>, <strong>Financial</strong>, or <strong>Technical</strong> - and work in teams to deliver projects for partner organizations. We also host volunteering events, workshops, and community-building activities throughout the year.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Membership is open to all interested Stanford undergraduate and graduate students. We coordinate through CardinalEngage and partner closely with the Haas Center for Public Service.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Leadership</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>PVV is led by a team of student officers including a President, Vice President, Treasurer, Community Outreach Organizers, and Consulting Category Chairs for each specialization. Decisions are made collaboratively by active members.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="SITE/contact/">Contact Us</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->
""".replace("SITE", SITE)

PROJECTS_CONTENT = """
<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size">PVV partners with local nonprofits on real consulting projects across marketing, finance, and technology. Here is the kind of work our teams deliver.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Marketing Projects</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><li>Social media strategy and content calendars</li><li>Event flyers and promotional materials</li><li>Campaign planning for fundraisers and volunteer drives</li><li>Outreach to Stanford students via the Haas Center</li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Financial Projects</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><li>Grant research and application support</li><li>Line-item budgets for programs and funding proposals</li><li>Financial planning for donations and operational costs</li><li>Guidance on navigating benefits and available resources</li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Technical Projects</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><li>Nonprofit websites and landing pages</li><li>Volunteer intake and contact forms</li><li>Survey and data collection pipelines</li><li>Tools to improve donations, operations, and user engagement</li></ul>
<!-- /wp:list -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Partner With PVV</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Are you a nonprofit or community organization looking for support? We prioritize partners serving low-income communities in the Bay Area and look for projects where our student teams can make a lasting impact.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>Project highlights coming soon - check back as we publish work from current partnerships.</em></p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="SITE/contact/">Start a Conversation</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->
""".replace("SITE", SITE)

CONTACT_CONTENT = """
<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size">We would love to hear from you - whether you represent a nonprofit looking for support or a Stanford student interested in joining PVV.</p>
<!-- /wp:paragraph -->

<!-- wp:group {"style":{"spacing":{"padding":{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|50","right":"var:preset|spacing|50"},"margin":{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40"}}},"backgroundColor":"accent-5","layout":{"type":"constrained"}} -->
<div class="wp-block-group has-accent-5-background-color has-background" style="margin-top:var(--wp--preset--spacing--40);margin-bottom:var(--wp--preset--spacing--40);padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--50)"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Email</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>Ed Yeres, President</strong><br><a href="mailto:edyeres@stanford.edu">edyeres@stanford.edu</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For partnership inquiries, consulting requests, or general questions about PVV, email is the best way to reach our leadership team.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:heading -->
<h2 class="wp-block-heading">For Nonprofits</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Tell us about your organization, the community you serve, and what kind of support you need - marketing, financial, technical, or a combination. We will follow up to discuss whether PVV is a good fit for a consulting partnership.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">For Stanford Students</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Interested in joining PVV? Reach out to learn about our consulting tracks, upcoming events, and how to get involved. You can also find us on CardinalEngage.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="mailto:edyeres@stanford.edu">Send an Email</a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="SITE/about-us/">Learn About PVV</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->
""".replace("SITE", SITE)


def upsert_page(slug, title, content, existing_pages):
    for p in existing_pages:
        if p["slug"] == slug:
            return api("POST", f"/pages/{p['id']}", {"title": title, "content": content, "status": "publish"})
    return api("POST", "/pages", {"title": title, "slug": slug, "content": content, "status": "publish"})


def main():
    existing = api("GET", "/pages?per_page=50&context=edit")

    home = upsert_page("home", "Home", HOME_CONTENT, existing)
    about = upsert_page("about-us", "About Us", ABOUT_CONTENT, existing)
    projects = upsert_page("projects", "Projects", PROJECTS_CONTENT, existing)
    contact = upsert_page("contact", "Contact", CONTACT_CONTENT, existing)

    print(f"Home id={home['id']} link={home['link']}")
    print(f"About id={about['id']} link={about['link']}")
    print(f"Projects id={projects['id']} link={projects['link']}")
    print(f"Contact id={contact['id']} link={contact['link']}")

    # Trash sample page
    for p in existing:
        if p["slug"] == "sample-page":
            api("POST", f"/pages/{p['id']}", {"status": "draft"})
            print(f"Drafted sample page id={p['id']}")

    # Static front page
    settings_api({
        "show_on_front": "page",
        "page_on_front": home["id"],
        "description": "Free nonprofit consulting for community organizations - marketing, financial, and technical support from Stanford students.",
    })
    print("Set static front page and site tagline")

    # Update header with linked nav buttons
    header_content = f"""<!-- wp:group {{"align":"full","layout":{{"type":"default"}}}} -->
<div class="wp-block-group alignfull"><!-- wp:group {{"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group"><!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30"}}}}}},"layout":{{"type":"flex","flexWrap":"nowrap","justifyContent":"space-between"}}}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30)"><!-- wp:site-title {{"level":0,"isLink":true}} /-->

<!-- wp:group {{"style":{{"spacing":{{"blockGap":"var:preset|spacing|10"}}}},"layout":{{"type":"flex","flexWrap":"nowrap","justifyContent":"right"}}}} -->
<div class="wp-block-group"><!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{SITE}/">Home</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{SITE}/about-us/">About Us</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{SITE}/projects/">Projects</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{SITE}/contact/">Contact</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->"""

    api("POST", "/template-parts/twentytwentyfive//header", {"content": header_content})
    print("Updated header navigation")

    # Update navigation block (if used elsewhere)
    nav_content = f"""<!-- wp:navigation-link {{"label":"Home","type":"page","url":"{SITE}/","kind":"custom"}} /-->

<!-- wp:navigation-link {{"label":"About Us","type":"page","url":"{SITE}/about-us/","kind":"custom"}} /-->

<!-- wp:navigation-link {{"label":"Projects","type":"page","url":"{SITE}/projects/","kind":"custom"}} /-->

<!-- wp:navigation-link {{"label":"Contact","type":"page","url":"{SITE}/contact/","kind":"custom"}} /-->"""

    api("POST", "/navigation/4", {"content": nav_content})
    print("Updated navigation menu")

    # Assign page-no-title template to home for cleaner layout
    api("POST", f"/pages/{home['id']}", {"template": "page-no-title"})
    print("Set home page to no-title template")

    print("Done!")


if __name__ == "__main__":
    main()
