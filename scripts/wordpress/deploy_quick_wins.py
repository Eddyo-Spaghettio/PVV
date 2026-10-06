#!/usr/bin/env python3
"""Implement PVV website quick wins: stats, story, case studies, audience pages, team, banner."""

import json
import base64
import os
import urllib.request
import urllib.error

BASE = "https://pvv.su.domains/wp-json/wp/v2"
USER = os.environ.get("WP_USER", "edyeres")
PASSWORD = os.environ["WP_APP_PASSWORD"]
SITE = "https://pvv.su.domains"
EMAIL = "edyeres@stanford.edu"
LEADER = "Edmund Dyer-Essig"
LIST_URL = "https://groups.google.com/a/lists.stanford.edu/g/proyecto-vidas-valiosas"

MISSION = (
    "The purpose of Proyecto Vidas Valiosas is to connect local non-profits and "
    "community organizations serving low-income communities with free, student-provided "
    "consulting services, providing technical, financial, and marketing support to "
    "support their operations and long-term success."
)


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


def banner(title, subtitle):
    return f"""
<!-- wp:group {{"align":"full","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|70","bottom":"var:preset|spacing|70","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}}}}},"backgroundColor":"contrast","textColor":"base","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignfull has-base-color has-contrast-background-color has-text-color has-background" style="padding-top:var(--wp--preset--spacing--70);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--70);padding-left:var(--wp--preset--spacing--50)"><!-- wp:heading {{"textAlign":"center","level":1,"fontSize":"xx-large"}} -->
<h1 class="wp-block-heading has-text-align-center has-xx-large-font-size">{title}</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {{"align":"center","fontSize":"medium"}} -->
<p class="has-text-align-center has-medium-font-size">{subtitle}</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
"""


ANNOUNCEMENT = f"""
<!-- wp:group {{"align":"full","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}}}}},"backgroundColor":"contrast","textColor":"base","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignfull has-base-color has-contrast-background-color has-text-color has-background pvv-announcement" style="padding-top:var(--wp--preset--spacing--30);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--30);padding-left:var(--wp--preset--spacing--50)"><!-- wp:paragraph {{"align":"center","fontSize":"small"}} -->
<p class="has-text-align-center has-small-font-size"><strong>Fall 2026 - Now recruiting Stanford students &amp; nonprofit partners.</strong> <a href="{SITE}/for-students/">Join as a student</a> · <a href="{SITE}/for-nonprofits/">Partner with us</a> · <a href="{LIST_URL}">Join our mailing list</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
"""

IMPACT_STATS = """
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|50","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}},"backgroundColor":"accent-5","layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-accent-5-background-color has-background" style="padding-top:var(--wp--preset--spacing--50);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--50);padding-left:var(--wp--preset--spacing--50)"><!-- wp:heading {"textAlign":"center","level":2} -->
<h2 class="wp-block-heading has-text-align-center">Our Impact</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","fontSize":"small"} -->
<p class="has-text-align-center has-small-font-size"><em>Update these numbers each quarter as PVV grows.</em></p>
<!-- /wp:paragraph -->

<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|30"},"margin":{"top":"var:preset|spacing|40"}}}} -->
<div class="wp-block-columns alignwide" style="margin-top:var(--wp--preset--spacing--40)"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {"className":"pvv-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30"}},"border":{"radius":"8px"}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group pvv-card" style="border-radius:8px;padding-top:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30)"><!-- wp:heading {"textAlign":"center","level":3,"fontSize":"xx-large"} -->
<h3 class="wp-block-heading has-text-align-center has-xx-large-font-size">5+</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","fontSize":"small"} -->
<p class="has-text-align-center has-small-font-size">Nonprofit partners</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {"className":"pvv-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30"}},"border":{"radius":"8px"}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group pvv-card" style="border-radius:8px;padding-top:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30)"><!-- wp:heading {"textAlign":"center","level":3,"fontSize":"xx-large"} -->
<h3 class="wp-block-heading has-text-align-center has-xx-large-font-size">30+</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","fontSize":"small"} -->
<p class="has-text-align-center has-small-font-size">Student consultants</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {"className":"pvv-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30"}},"border":{"radius":"8px"}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group pvv-card" style="border-radius:8px;padding-top:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30)"><!-- wp:heading {"textAlign":"center","level":3,"fontSize":"xx-large"} -->
<h3 class="wp-block-heading has-text-align-center has-xx-large-font-size">3</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","fontSize":"small"} -->
<p class="has-text-align-center has-small-font-size">Consulting tracks</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {"className":"pvv-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30"}},"border":{"radius":"8px"}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group pvv-card" style="border-radius:8px;padding-top:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30)"><!-- wp:heading {"textAlign":"center","level":3,"fontSize":"xx-large"} -->
<h3 class="wp-block-heading has-text-align-center has-xx-large-font-size">100%</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","fontSize":"small"} -->
<p class="has-text-align-center has-small-font-size">Free for partners</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->
"""

OUR_STORY = f"""
<!-- wp:heading -->
<h2 class="wp-block-heading">Our Story</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"medium"}} -->
<p class="has-medium-font-size">Bay Area nonprofits serving low-income communities do critical work - but many lack the staff, budget, or expertise to handle marketing campaigns, grant applications, and digital tools. At the same time, Stanford students want meaningful ways to apply their skills beyond the classroom.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Proyecto Vidas Valiosas was founded to bridge that gap.</strong> We are a student organization that pairs consulting teams with local community organizations, providing free support across marketing, financial, and technical needs. Unlike dev-only volunteer programs, PVV offers integrated consulting under one roof - and we prioritize long-term partnerships over one-off projects.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Today, PVV runs three consulting tracks, organizes volunteering events with transportation support, and hosts workshops that train members to serve nonprofits effectively. Our mission, defined in our constitution:</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">{MISSION}</p>
<!-- /wp:paragraph --></blockquote>
<!-- /wp:quote -->
"""

FOR_NONPROFITS = banner(
    "For Nonprofits",
    "Free marketing, financial, and technical consulting for Bay Area community organizations",
) + f"""
<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|80"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--80)"><!-- wp:paragraph {{"fontSize":"large"}} -->
<p class="has-large-font-size">PVV helps small nonprofits operate like big ones - at zero cost. We pair your organization with a team of Stanford student consultants who deliver real work products you can use long after the project ends.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">What You Can Get</h2>
<!-- /wp:heading -->

<!-- wp:columns {{"style":{{"spacing":{{"blockGap":{{"left":"var:preset|spacing|30"}}}}}}}} -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card has-accent-5-background-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--30);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30);padding-left:var(--wp--preset--spacing--30)"><!-- wp:heading {{"level":4}} -->
<h4 class="wp-block-heading">Marketing</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">Social media, flyers, campaigns, Haas Center student outreach.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card has-accent-5-background-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--30);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30);padding-left:var(--wp--preset--spacing--30)"><!-- wp:heading {{"level":4}} -->
<h4 class="wp-block-heading">Financial</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">Grant applications, budgets, fundraising planning, resource navigation.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card has-accent-5-background-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--30);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30);padding-left:var(--wp--preset--spacing--30)"><!-- wp:heading {{"level":4}} -->
<h4 class="wp-block-heading">Technical</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">Websites, forms, surveys, data tools, donation workflows.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:heading {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<h2 class="wp-block-heading" style="margin-top:var(--wp--preset--spacing--50)">Who We Partner With</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We prioritize nonprofits and community-based organizations serving <strong>low-income communities</strong> in the Bay Area - food pantries, legal aid clinics, youth programs, and similar CBOs.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<h2 class="wp-block-heading" style="margin-top:var(--wp--preset--spacing--50)">What to Expect</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><li><strong>Timeline:</strong> Most projects run one Stanford quarter (~8–10 weeks)</li><li><strong>Cost:</strong> Free - no fees for partner organizations</li><li><strong>Your role:</strong> Provide a point of contact, timely feedback, and program context</li><li><strong>Deliverables:</strong> Scoped together at the start; handoff documentation included</li><li><strong>After PVV:</strong> You keep all work products and maintain them independently</li></ul>
<!-- /wp:list -->

<!-- wp:heading {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<h2 class="wp-block-heading" style="margin-top:var(--wp--preset--spacing--50)">How to Apply</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Email us with your organization's name, mission, the community you serve, and what kind of support you need. We'll follow up to discuss fit and next steps.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="mailto:{EMAIL}?subject=PVV%20Partnership%20Inquiry">Email Partnership Inquiry</a></div>
<!-- /wp:button -->

<!-- wp:button {{"className":"is-style-outline"}} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{SITE}/projects/">See Example Projects</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->
"""

FOR_STUDENTS = banner(
    "For Stanford Students",
    "Build real consulting skills while supporting Bay Area nonprofits",
) + f"""
<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|80"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--80)"><!-- wp:paragraph {{"fontSize":"large"}} -->
<p class="has-large-font-size">PVV is for students who want hands-on experience consulting for real community organizations - no prior marketing, finance, or tech background required.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Why Join PVV?</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><li>Work on <strong>real client projects</strong> with deliverables you can put on your resume</li><li>Choose a track: <strong>Marketing</strong>, <strong>Financial</strong>, or <strong>Technical</strong> consulting</li><li>Attend workshops and training designed for beginners</li><li>Participate in <strong>volunteering events</strong> with transportation support</li><li>Join a community of students interested in public service and social impact</li></ul>
<!-- /wp:list -->

<!-- wp:heading {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<h2 class="wp-block-heading" style="margin-top:var(--wp--preset--spacing--50)">Who Can Join?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Membership is open to all interested <strong>Stanford undergraduate and graduate students</strong>. No consulting experience needed - we provide training and pair newer members with experienced ones.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<h2 class="wp-block-heading" style="margin-top:var(--wp--preset--spacing--50)">Time Commitment</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Expect to attend weekly general meetings and contribute to your consulting team's deliverables throughout the quarter. Specific hours vary by project, but plan for roughly <strong>3–5 hours per week</strong> as a baseline.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<h2 class="wp-block-heading" style="margin-top:var(--wp--preset--spacing--50)">How to Get Involved</h2>
<!-- /wp:heading -->

<!-- wp:list {{"ordered":true}} -->
<ol class="wp-block-list"><li><a href="{LIST_URL}">Join the PVV mailing list</a> for event and meeting announcements</li><li>Email <a href="mailto:{EMAIL}">{EMAIL}</a> to introduce yourself</li><li>Attend a general meeting and pick a consulting track</li><li>Get matched to a project team</li></ol>
<!-- /wp:list -->

<!-- wp:buttons {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|40"}}}}}}}} -->
<div class="wp-block-buttons" style="margin-top:var(--wp--preset--spacing--40)"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{LIST_URL}">Join Mailing List</a></div>
<!-- /wp:button -->

<!-- wp:button {{"className":"is-style-outline"}} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{SITE}/faq/">Read FAQ</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->
"""

TEAM = banner("Our Team", "PVV leadership and consulting chairs") + f"""
<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|80"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--80)"><!-- wp:paragraph {{"fontSize":"large"}} -->
<p class="has-large-font-size">PVV is led by student officers and consulting category chairs. Update names and photos here each year after elections.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Executive Board</h2>
<!-- /wp:heading -->

<!-- wp:columns {{"style":{{"spacing":{{"blockGap":{{"left":"var:preset|spacing|30"}},"margin":{{"top":"var:preset|spacing|30"}}}}}}}} -->
<div class="wp-block-columns" style="margin-top:var(--wp--preset--spacing--30)"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card has-accent-5-background-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--30)"><!-- wp:heading {{"level":4}} -->
<h4 class="wp-block-heading">{LEADER}</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>President</strong><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card has-accent-5-background-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--30)"><!-- wp:heading {{"level":4}} -->
<h4 class="wp-block-heading">TBD</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>Vice President</strong><br>Update after elections</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card has-accent-5-background-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--30)"><!-- wp:heading {{"level":4}} -->
<h4 class="wp-block-heading">TBD</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>Treasurer</strong><br>Update after elections</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:heading {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<h2 class="wp-block-heading" style="margin-top:var(--wp--preset--spacing--50)">Community Outreach</h2>
<!-- /wp:heading -->

<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>Outreach Organizer</strong> - TBD</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>Outreach Organizer</strong> - TBD</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:heading {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<h2 class="wp-block-heading" style="margin-top:var(--wp--preset--spacing--50)">Consulting Category Chairs</h2>
<!-- /wp:heading -->

<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>Marketing Chair</strong> - TBD<br><strong>Marketing Chair</strong> - TBD</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>Financial Chair</strong> - TBD<br><strong>Financial Chair</strong> - TBD</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>Technical Chair</strong> - TBD<br><strong>Technical Chair</strong> - TBD</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:paragraph {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|40"}}}}}},"fontSize":"small"}} -->
<p class="has-small-font-size" style="margin-top:var(--wp--preset--spacing--40)"><em>Interested in leadership? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</em></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
"""

CASE_STUDY = f"""
<!-- wp:heading {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<h2 class="wp-block-heading" style="margin-top:var(--wp--preset--spacing--50)">Case Study</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><em>Template - replace with a real PVV project when available.</em></p>
<!-- /wp:paragraph -->

<!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|50","left":"var:preset|spacing|40","right":"var:preset|spacing|40"}},"margin":{{"top":"var:preset|spacing|30"}}}},"border":{{"radius":"12px","width":"1px"}},"borderColor":"accent-6","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card has-border-color has-accent-6-border-color" style="border-width:1px;border-radius:12px;margin-top:var(--wp--preset--spacing--30);padding-top:var(--wp--preset--spacing--50);padding-right:var(--wp--preset--spacing--40);padding-bottom:var(--wp--preset--spacing--50);padding-left:var(--wp--preset--spacing--40)"><!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">Eastside Community Pantry - Marketing Campaign</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>Track:</strong> Marketing &nbsp;|&nbsp; <strong>Timeline:</strong> 8 weeks &nbsp;|&nbsp; <strong>Community:</strong> East Palo Alto</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":4}} -->
<h4 class="wp-block-heading">The Challenge</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">A local food pantry serving 200+ families weekly needed to promote a fundraiser and recruit Stanford student volunteers - but had no social media strategy and limited design capacity.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":4}} -->
<h4 class="wp-block-heading">What PVV Delivered</h4>
<!-- /wp:heading -->

<!-- wp:list {{"fontSize":"small"}} -->
<ul class="wp-block-list has-small-font-size"><li>4-week social media content calendar</li><li>Event flyer and promotional materials</li><li>Haas Center outreach blurb for Stanford students</li><li>Instagram captions and day-of event story script</li></ul>
<!-- /wp:list -->

<!-- wp:heading {{"level":4}} -->
<h4 class="wp-block-heading">Impact</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><em>[Add results here - e.g. event attendance, new followers, volunteers recruited]</em></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">Have a project to highlight? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<!-- /wp:paragraph -->
"""


def upsert_page(slug, title, content, pages):
    if slug in pages:
        pid = pages[slug]["id"]
        api("POST", f"/pages/{pid}", {"title": title, "content": content, "status": "publish", "template": "page-no-title"})
        print(f"Updated {slug} (id={pid})")
        return pid
    page = api("POST", "/pages", {"title": title, "slug": slug, "content": content, "status": "publish", "template": "page-no-title"})
    print(f"Created {slug} (id={page['id']}) link={page['link']}")
    return page["id"]


def patch_home(existing):
    content = existing
    if "pvv-announcement" not in content:
        # Insert announcement after first hero group (after first closing /wp:group of alignfull contrast)
        marker = "<!-- /wp:group -->\n\n<!-- wp:group {\"align\":\"wide\""
        if marker in content:
            content = content.replace(marker, "<!-- /wp:group -->\n\n" + ANNOUNCEMENT + "\n\n<!-- wp:group {\"align\":\"wide\"", 1)
        else:
            content = ANNOUNCEMENT + content
    if "Our Impact" not in content:
        marker = "<!-- wp:group {\"align\":\"wide\",\"style\":{\"spacing\":{\"padding\":{\"bottom\":\"var:preset|spacing|60\"}}},\"layout\":{\"type\":\"constrained\"}} -->\n<div class=\"wp-block-group alignwide\" style=\"padding-bottom:var(--wp--preset--spacing--60)\"><!-- wp:heading {\"textAlign\":\"center\"} -->\n<h2 class=\"wp-block-heading has-text-align-center\">What Makes PVV Different</h2>"
        if marker in content:
            content = content.replace(marker, IMPACT_STATS + "\n\n" + marker, 1)
    # Update student card links to for-students page
    content = content.replace(f'href="{SITE}/contact/">Request a partnership', f'href="{SITE}/for-nonprofits/">Request a partnership')
    old_student = f'<a href="{LIST_URL}">Join our mailing list →</a>'
    new_student = f'<a href="{SITE}/for-students/">Learn how to join →</a> · <a href="{LIST_URL}">Mailing list</a>'
    if old_student in content:
        content = content.replace(
            f'<p class="has-small-font-size"><a href="{LIST_URL}">Join our mailing list →</a> · <a href="mailto:{EMAIL}">Email us</a> · <a href="{SITE}/faq/">FAQ</a></p>',
            f'<p class="has-small-font-size"><a href="{SITE}/for-students/">Learn how to join →</a> · <a href="{LIST_URL}">Mailing list</a> · <a href="{SITE}/faq/">FAQ</a></p>',
        )
    return content


def patch_about(existing):
    if "Our Story" in existing:
        return existing
    # Insert after page banner (first full-width contrast group ending)
    idx = existing.find("<!-- /wp:group -->")
    if idx == -1:
        return OUR_STORY + existing
    idx2 = existing.find("<!-- /wp:group -->", idx + 20)
    insert_at = idx2 + len("<!-- /wp:group -->") if idx2 != -1 else idx + len("<!-- /wp:group -->")
    return existing[:insert_at] + "\n\n" + OUR_STORY + existing[insert_at:]


def patch_projects(existing):
    if "Eastside Community Pantry" in existing:
        return existing
    # Replace old "Case Studies coming soon" box or append
    old = "<!-- wp:heading {\"level\":3} -->\n<h3 class=\"wp-block-heading\">Case Studies</h3>"
    if old in existing:
        start = existing.find("<!-- wp:group {\"style\":{\"spacing\":{\"padding\":{\"top\":\"var:preset|spacing|50\"")
        if start != -1:
            end = existing.find("<!-- /wp:group -->", start) + len("<!-- /wp:group -->")
            return existing[:start] + CASE_STUDY.strip() + existing[end:]
    return existing + CASE_STUDY


def build_header():
    return f"""<!-- wp:html -->
<style>
  :root {{
    --pvv-gold: #C4A35A;
    --pvv-gold-light: #E2CFA0;
    --pvv-gold-bright: #D4AF37;
    --pvv-gold-subtle: rgba(196, 163, 90, 0.18);
    --pvv-black: #111111;
  }}
  .pvv-announcement a {{ color: var(--pvv-gold-light) !important; font-weight: 600; }}
  .pvv-announcement a:hover {{ color: var(--pvv-gold-bright) !important; }}
  @keyframes pvv-fade-up {{ from {{ opacity: 0; transform: translateY(28px); }} to {{ opacity: 1; transform: translateY(0); }} }}
  @keyframes pvv-fade-in {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
  @keyframes pvv-hero-glow {{ 0%, 100% {{ opacity: 0.35; }} 50% {{ opacity: 0.65; }} }}
  .pvv-hero-animate {{ animation: pvv-fade-up 0.9s cubic-bezier(0.22, 1, 0.36, 1) both; }}
  .pvv-hero-animate-d1 {{ animation-delay: 0.12s; }}
  .pvv-hero-animate-d2 {{ animation-delay: 0.24s; }}
  .pvv-hero-animate-d3 {{ animation-delay: 0.36s; }}
  .pvv-fade-in {{ animation: pvv-fade-in 1s ease both; }}
  .pvv-card {{ transition: transform 0.28s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.28s ease, border-color 0.28s ease; }}
  .pvv-card:hover {{ transform: translateY(-6px); border-color: var(--pvv-gold) !important; box-shadow: 0 16px 40px rgba(196, 163, 90, 0.14); }}
  .pvv-mission-glow::before {{ content: ""; position: absolute; inset: -1px; border-radius: inherit; background: linear-gradient(135deg, transparent 40%, rgba(226, 207, 160, 0.08) 100%); animation: pvv-hero-glow 4s ease-in-out infinite; pointer-events: none; }}
  header .wp-block-group.alignfull[style*="border-bottom"] {{ border-bottom-color: var(--pvv-gold) !important; }}
  .wp-block-site-title a {{ transition: color 0.2s ease; }}
  .wp-block-site-title a:hover {{ color: var(--pvv-gold-bright) !important; }}
  .wp-block-navigation-item__content {{ transition: color 0.2s ease; }}
  .wp-block-navigation-item__content:hover {{ color: var(--pvv-gold-bright) !important; }}
  .has-contrast-background-color p.has-small-font-size[style*="uppercase"] {{ color: var(--pvv-gold-light) !important; }}
  main a:not(.wp-element-button) {{ transition: color 0.2s ease; }}
  main a:not(.wp-element-button):hover {{ color: var(--pvv-gold-bright); }}
  .has-contrast-background-color a:not(.wp-element-button) {{ color: var(--pvv-gold-light); }}
  .has-contrast-background-color a:not(.wp-element-button):hover {{ color: var(--pvv-gold-bright); }}
  .has-contrast-background-color .wp-block-button:not(.is-style-outline) .wp-block-button__link.has-base-background-color {{ background-color: var(--pvv-gold-light) !important; color: var(--pvv-black) !important; font-weight: 600; }}
  .has-contrast-background-color .wp-block-button.is-style-outline .wp-block-button__link {{ border-color: var(--pvv-gold-light) !important; color: var(--pvv-gold-light) !important; }}
  main h2.has-text-align-center::after {{ content: ""; display: block; width: 52px; height: 2px; background: linear-gradient(90deg, transparent, var(--pvv-gold), transparent); margin: 0.85rem auto 0; }}
  main .has-accent-5-background-color.pvv-fade-in, main .pvv-mission-glow .has-accent-5-background-color {{ border-left: 3px solid var(--pvv-gold); }}
  details.pvv-faq-item {{ border-left: 3px solid transparent; padding-left: 1rem; transition: border-color 0.25s ease; }}
  details.pvv-faq-item[open] {{ border-left-color: var(--pvv-gold); }}
  footer.has-accent-5-background-color, .has-accent-5-background-color[style*="border-top"] {{ border-top-color: var(--pvv-gold) !important; }}
  footer a:hover {{ color: var(--pvv-gold-bright) !important; }}
  @media (prefers-reduced-motion: reduce) {{ .pvv-hero-animate, .pvv-hero-animate-d1, .pvv-hero-animate-d2, .pvv-hero-animate-d3, .pvv-fade-in, .pvv-mission-glow::before {{ animation: none !important; }} .pvv-card:hover {{ transform: none; }} }}
</style>
<!-- /wp:html -->

<!-- wp:group {{"align":"full","style":{{"border":{{"bottom":{{"color":"var:preset|color|accent-6","width":"1px"}}}},"spacing":{{"padding":{{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30"}}}}}},"layout":{{"type":"default"}}}} -->
<div class="wp-block-group alignfull" style="border-bottom-color:var(--wp--preset--color--accent-6);border-bottom-width:1px;padding-top:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30)"><!-- wp:group {{"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group"><!-- wp:group {{"align":"wide","layout":{{"type":"flex","flexWrap":"nowrap","justifyContent":"space-between","verticalAlignment":"center"}}}} -->
<div class="wp-block-group alignwide"><!-- wp:site-title {{"level":0,"style":{{"typography":{{"fontStyle":"normal","fontWeight":"700"}}}}}} /-->

<!-- wp:navigation {{"overlayMenu":"never","layout":{{"type":"flex","justifyContent":"right","flexWrap":"wrap"}}}} -->
<!-- wp:navigation-link {{"label":"Home","url":"{SITE}/","kind":"custom"}} /-->

<!-- wp:navigation-link {{"label":"About","url":"{SITE}/about-us/","kind":"custom"}} /-->

<!-- wp:navigation-link {{"label":"Nonprofits","url":"{SITE}/for-nonprofits/","kind":"custom"}} /-->

<!-- wp:navigation-link {{"label":"Students","url":"{SITE}/for-students/","kind":"custom"}} /-->

<!-- wp:navigation-link {{"label":"Projects","url":"{SITE}/projects/","kind":"custom"}} /-->

<!-- wp:navigation-link {{"label":"Team","url":"{SITE}/team/","kind":"custom"}} /-->

<!-- wp:navigation-link {{"label":"FAQ","url":"{SITE}/faq/","kind":"custom"}} /-->

<!-- wp:navigation-link {{"label":"Contact","url":"{SITE}/contact/","kind":"custom"}} /-->
<!-- /wp:navigation --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->"""


def build_footer():
    tpl = """<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|70","bottom":"var:preset|spacing|50","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}},"border":{"top":{"color":"var:preset|color|accent-6","width":"1px"}}},"backgroundColor":"accent-5","layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-accent-5-background-color has-background" style="border-top-color:var(--wp--preset--color--accent-6);border-top-width:1px;padding-top:var(--wp--preset--spacing--70);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--50);padding-left:var(--wp--preset--spacing--50)"><!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|40"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:site-title {"level":3,"style":{"typography":{"fontStyle":"normal","fontWeight":"700"}}} /-->

<!-- wp:site-tagline {"fontSize":"small"} /-->

<!-- wp:paragraph {"fontSize":"small","style":{"spacing":{"margin":{"top":"var:preset|spacing|30"}}}} -->
<p class="has-small-font-size" style="margin-top:var(--wp--preset--spacing--30)"><a href="mailto:EMAIL">EMAIL</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"30%"} -->
<div class="wp-block-column" style="flex-basis:30%"><!-- wp:heading {"level":4,"fontSize":"small"} -->
<h4 class="wp-block-heading has-small-font-size">Explore</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><a href="SITE/about-us/">About</a><br><a href="SITE/projects/">Projects</a><br><a href="SITE/team/">Team</a><br><a href="SITE/faq/">FAQ</a><br><a href="SITE/contact/">Contact</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"30%"} -->
<div class="wp-block-column" style="flex-basis:30%"><!-- wp:heading {"level":4,"fontSize":"small"} -->
<h4 class="wp-block-heading has-small-font-size">Get Involved</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><a href="SITE/for-nonprofits/">For nonprofits</a><br><a href="SITE/for-students/">For students</a><br><a href="LIST_URL">Join mailing list</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:separator {"style":{"spacing":{"margin":{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|30"}}}} -->
<hr class="wp-block-separator has-alpha-channel-opacity" style="margin-top:var(--wp--preset--spacing--50);margin-bottom:var(--wp--preset--spacing--30)"/>
<!-- /wp:separator -->

<!-- wp:paragraph {"align":"center","fontSize":"small"} -->
<p class="has-text-align-center has-small-font-size">© 2026 Proyecto Vidas Valiosas · Stanford University</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->"""
    return tpl.replace("SITE", SITE).replace("EMAIL", EMAIL).replace("LIST_URL", LIST_URL)


def main():
    raw_pages = api("GET", "/pages?per_page=50&context=edit")
    pages = {p["slug"]: p for p in raw_pages}

    # New pages
    upsert_page("for-nonprofits", "For Nonprofits", FOR_NONPROFITS, pages)
    upsert_page("for-students", "For Students", FOR_STUDENTS, pages)
    upsert_page("team", "Team", TEAM, pages)

    # Patch existing
    home = patch_home(pages["home"]["content"]["raw"])
    api("POST", f"/pages/{pages['home']['id']}", {"content": home, "template": "page-no-title"})
    print("Updated home")

    about = patch_about(pages["about-us"]["content"]["raw"])
    api("POST", f"/pages/{pages['about-us']['id']}", {"content": about, "template": "page-no-title"})
    print("Updated about-us")

    projects = patch_projects(pages["projects"]["content"]["raw"])
    api("POST", f"/pages/{pages['projects']['id']}", {"content": projects, "template": "page-no-title"})
    print("Updated projects")

    api("POST", "/template-parts/twentytwentyfive//header", {"content": build_header()})
    print("Updated header")

    api("POST", "/template-parts/twentytwentyfive//footer", {"content": build_footer()})
    print("Updated footer")

    print("All quick wins deployed!")


if __name__ == "__main__":
    main()
