#!/usr/bin/env python3
"""Polish PVV WordPress site UI and fix content details."""

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
        raise RuntimeError(f"{method} {path} failed ({e.code}): {e.read().decode()}") from e


def page_banner(title, subtitle):
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


HOME = f"""
<!-- wp:group {{"align":"full","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|80","bottom":"var:preset|spacing|80","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}}}}},"backgroundColor":"contrast","textColor":"base","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignfull has-base-color has-contrast-background-color has-text-color has-background" style="padding-top:var(--wp--preset--spacing--80);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--80);padding-left:var(--wp--preset--spacing--50)"><!-- wp:paragraph {{"align":"center","style":{{"typography":{{"letterSpacing":"0.08em","textTransform":"uppercase","fontStyle":"normal","fontWeight":"600"}}}},"fontSize":"small"}} -->
<p class="has-text-align-center has-small-font-size" style="font-style:normal;font-weight:600;letter-spacing:0.08em;text-transform:uppercase">Stanford Student Organization</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"textAlign":"center","level":1,"fontSize":"xx-large"}} -->
<h1 class="wp-block-heading has-text-align-center has-xx-large-font-size">Proyecto Vidas Valiosas</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {{"align":"center","fontSize":"large"}} -->
<p class="has-text-align-center has-large-font-size">Free marketing, financial, and technical consulting for Bay Area nonprofits serving low-income communities.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons {{"layout":{{"type":"flex","justifyContent":"center"}},"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|40"}},"blockGap":"var:preset|spacing|20"}}}}}} -->
<div class="wp-block-buttons" style="margin-top:var(--wp--preset--spacing--40)"><!-- wp:button {{"backgroundColor":"base","textColor":"contrast"}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-contrast-color has-base-background-color has-text-color has-background wp-element-button" href="{SITE}/contact/">Partner With Us</a></div>
<!-- /wp:button -->

<!-- wp:button {{"className":"is-style-outline"}} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{SITE}/about-us/">About PVV</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->

<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|70","bottom":"var:preset|spacing|50"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--70);padding-bottom:var(--wp--preset--spacing--50)"><!-- wp:columns {{"align":"wide","style":{{"spacing":{{"blockGap":{{"left":"var:preset|spacing|40"}}}}}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|50","left":"var:preset|spacing|40","right":"var:preset|spacing|40"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group has-accent-5-background-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--50);padding-right:var(--wp--preset--spacing--40);padding-bottom:var(--wp--preset--spacing--50);padding-left:var(--wp--preset--spacing--40)"><!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">For Nonprofits</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Need help with grants, social media, or a website? PVV pairs your organization with a student consulting team at no cost.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><a href="{SITE}/contact/">Request a partnership →</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|50","left":"var:preset|spacing|40","right":"var:preset|spacing|40"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group has-accent-5-background-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--50);padding-right:var(--wp--preset--spacing--40);padding-bottom:var(--wp--preset--spacing--50);padding-left:var(--wp--preset--spacing--40)"><!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">For Stanford Students</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Build real consulting skills while supporting community organizations. Join marketing, financial, or technical project teams.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><a href="mailto:{EMAIL}">Get in touch →</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->

<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"bottom":"var:preset|spacing|70"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide" style="padding-bottom:var(--wp--preset--spacing--70)"><!-- wp:heading {{"textAlign":"center"}} -->
<h2 class="wp-block-heading has-text-align-center">What We Do</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {{"align":"center","style":{{"spacing":{{"margin":{{"bottom":"var:preset|spacing|50"}}}}}}}} -->
<p class="has-text-align-center" style="margin-bottom:var(--wp--preset--spacing--50)">Three consulting tracks. One mission: help small nonprofits operate like big ones.</p>
<!-- /wp:paragraph -->

<!-- wp:columns {{"align":"wide","style":{{"spacing":{{"blockGap":{{"left":"var:preset|spacing|40"}}}}}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"width":"1px","color":"var:preset|color|accent-6","radius":"8px"}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group" style="border-color:var(--wp--preset--color--accent-6);border-radius:8px;border-width:1px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--30)"><!-- wp:heading {{"level":3,"fontSize":"large"}} -->
<h3 class="wp-block-heading has-large-font-size">Marketing</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">Social media, flyers, campaigns, and Haas Center outreach to bring volunteers and donors to your door.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"width":"1px","color":"var:preset|color|accent-6","radius":"8px"}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group" style="border-color:var(--wp--preset--color--accent-6);border-radius:8px;border-width:1px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--30)"><!-- wp:heading {{"level":3,"fontSize":"large"}} -->
<h3 class="wp-block-heading has-large-font-size">Financial</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">Grant applications, structured budgets, and financial planning so your programs stay funded.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"width":"1px","color":"var:preset|color|accent-6","radius":"8px"}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group" style="border-color:var(--wp--preset--color--accent-6);border-radius:8px;border-width:1px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--30)"><!-- wp:heading {{"level":3,"fontSize":"large"}} -->
<h3 class="wp-block-heading has-large-font-size">Technical</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">Websites, forms, surveys, and data tools that save your team hours every week.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->

<!-- wp:group {{"align":"full","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|60","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignfull has-accent-5-background-color has-background" style="padding-top:var(--wp--preset--spacing--60);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--60);padding-left:var(--wp--preset--spacing--50)"><!-- wp:columns {{"verticalAlignment":"center"}} -->
<div class="wp-block-columns are-vertically-aligned-center"><!-- wp:column {{"verticalAlignment":"center","width":"66.66%"}} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:66.66%"><!-- wp:quote {{"className":"is-style-plain"}} -->
<blockquote class="wp-block-quote is-style-plain"><!-- wp:paragraph {{"fontSize":"large"}} -->
<p class="has-large-font-size">We connect local nonprofits serving low-income communities with free, student-provided consulting - so organizations can focus on their mission, not their operations.</p>
<!-- /wp:paragraph --></blockquote>
<!-- /wp:quote --></div>
<!-- /wp:column -->

<!-- wp:column {{"verticalAlignment":"center","width":"33.33%"}} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:33.33%"><!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>3</strong> consulting tracks<br><strong>100%</strong> free for partners<br><strong>Bay Area</strong> community focus</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->

<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|70","bottom":"var:preset|spacing|50"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--70);padding-bottom:var(--wp--preset--spacing--50)"><!-- wp:heading {{"textAlign":"center"}} -->
<h2 class="wp-block-heading has-text-align-center">How Partnering Works</h2>
<!-- /wp:heading -->

<!-- wp:columns {{"style":{{"spacing":{{"blockGap":{{"left":"var:preset|spacing|40"}},"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<div class="wp-block-columns" style="margin-top:var(--wp--preset--spacing--50)"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {{"level":4}} -->
<h4 class="wp-block-heading">1. Reach Out</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">Tell us about your organization and what support you need - marketing, financial, technical, or all three.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {{"level":4}} -->
<h4 class="wp-block-heading">2. Match &amp; Plan</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">We pair you with a student team, define scope together, and set a realistic timeline for deliverables.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {{"level":4}} -->
<h4 class="wp-block-heading">3. Deliver &amp; Hand Off</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">Your team builds the work product, trains your staff, and documents everything so you can keep it running.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->

<!-- wp:group {{"align":"full","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|80","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}}}}},"backgroundColor":"contrast","textColor":"base","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignfull has-base-color has-contrast-background-color has-text-color has-background" style="padding-top:var(--wp--preset--spacing--60);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--80);padding-left:var(--wp--preset--spacing--50)"><!-- wp:heading {{"textAlign":"center","fontSize":"x-large"}} -->
<h2 class="wp-block-heading has-text-align-center has-x-large-font-size">Ready to work together?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {{"align":"center"}} -->
<p class="has-text-align-center">Email {LEADER}, PVV President, to start a conversation.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons {{"layout":{{"type":"flex","justifyContent":"center"}},"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|30"}}}}}}}} -->
<div class="wp-block-buttons" style="margin-top:var(--wp--preset--spacing--30)"><!-- wp:button {{"backgroundColor":"base","textColor":"contrast"}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-contrast-color has-base-background-color has-text-color has-background wp-element-button" href="mailto:{EMAIL}">{EMAIL}</a></div>
<!-- /wp:button -->

<!-- wp:button {{"className":"is-style-outline"}} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{SITE}/projects/">View Our Services</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->
"""

ABOUT = page_banner("About Us", "Student-led consulting for community impact") + f"""
<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|80"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--80)"><!-- wp:paragraph {{"fontSize":"large"}} -->
<p class="has-large-font-size"><strong>Proyecto Vidas Valiosas (PVV)</strong> is a Stanford student organization providing free consulting to local nonprofits and community-based organizations serving low-income communities across the Bay Area.</p>
<!-- /wp:paragraph -->

<!-- wp:columns {{"style":{{"spacing":{{"blockGap":{{"left":"var:preset|spacing|50"}},"margin":{{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|50"}}}}}}}} -->
<div class="wp-block-columns" style="margin-top:var(--wp--preset--spacing--50);margin-bottom:var(--wp--preset--spacing--50)"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">Our Purpose</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">We connect community organizations with students who can help with marketing, financial planning, and technical projects - work that small nonprofits often lack the bandwidth to tackle alone.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">Our Approach</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">We prioritize long-term partnerships over one-off projects, and we build tools and systems our partners can maintain after we hand off.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Who We Serve</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><li><strong>Nonprofit partners</strong> - food pantries, legal aid clinics, youth programs, and CBOs serving low-income communities</li><li><strong>Stanford students</strong> - undergraduates and graduates interested in consulting and public service</li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2 class="wp-block-heading">What We Do Beyond Consulting</h2>
<!-- /wp:heading -->

<!-- wp:columns {{"style":{{"spacing":{{"blockGap":{{"left":"var:preset|spacing|30"}}}}}}}} -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>Volunteering events</strong><br>Service days with transportation support when available.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>Workshops</strong><br>Hands-on training in marketing, finance, and tech consulting.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>Community building</strong><br>Events that connect students with local organizations.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:separator {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|50"}}}}}}}} -->
<hr class="wp-block-separator has-alpha-channel-opacity" style="margin-top:var(--wp--preset--spacing--50);margin-bottom:var(--wp--preset--spacing--50)"/>
<!-- /wp:separator -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Leadership</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>PVV is led by student officers including a President, Vice President, Treasurer, Community Outreach Organizers, and Consulting Category Chairs. Decisions are made collaboratively by active members at weekly meetings.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{SITE}/contact/">Contact Leadership</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->
"""

PROJECTS = page_banner("Projects & Services", "What PVV consulting teams deliver for partner organizations") + f"""
<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|80"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--80)"><!-- wp:paragraph {{"fontSize":"large"}} -->
<p class="has-large-font-size">Every partnership looks different, but most projects fall into one of three tracks. Browse below to see the kind of deliverables our teams produce.</p>
<!-- /wp:paragraph -->

<!-- wp:columns {{"style":{{"spacing":{{"blockGap":{{"left":"var:preset|spacing|40"}},"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<div class="wp-block-columns" style="margin-top:var(--wp--preset--spacing--50)"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group has-accent-5-background-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--30)"><!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">Marketing</h3>
<!-- /wp:heading -->

<!-- wp:list {{"fontSize":"small"}} -->
<ul class="wp-block-list has-small-font-size"><li>Social media strategy &amp; content calendars</li><li>Event flyers &amp; promotional materials</li><li>Fundraiser &amp; volunteer campaign planning</li><li>Haas Center student outreach</li></ul>
<!-- /wp:list --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group has-accent-5-background-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--30)"><!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">Financial</h3>
<!-- /wp:heading -->

<!-- wp:list {{"fontSize":"small"}} -->
<ul class="wp-block-list has-small-font-size"><li>Grant research &amp; application support</li><li>Line-item program budgets</li><li>Donation &amp; operational financial planning</li><li>Resource &amp; benefits navigation</li></ul>
<!-- /wp:list --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group has-accent-5-background-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--30)"><!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">Technical</h3>
<!-- /wp:heading -->

<!-- wp:list {{"fontSize":"small"}} -->
<ul class="wp-block-list has-small-font-size"><li>Nonprofit websites &amp; landing pages</li><li>Volunteer &amp; intake forms</li><li>Survey &amp; data collection pipelines</li><li>Donation &amp; operations tooling</li></ul>
<!-- /wp:list --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|50","left":"var:preset|spacing|40","right":"var:preset|spacing|40"}},"margin":{{"top":"var:preset|spacing|60"}}}},"border":{{"radius":"8px","width":"1px"}},"borderColor":"accent-6","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group has-border-color has-accent-6-border-color" style="border-width:1px;border-radius:8px;margin-top:var(--wp--preset--spacing--60);padding-top:var(--wp--preset--spacing--50);padding-right:var(--wp--preset--spacing--40);padding-bottom:var(--wp--preset--spacing--50);padding-left:var(--wp--preset--spacing--40)"><!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">Case Studies</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><em>Coming soon - we will highlight recent partnerships and deliverables here as projects wrap up.</em></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:buttons {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<div class="wp-block-buttons" style="margin-top:var(--wp--preset--spacing--50)"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{SITE}/contact/">Start a Partnership</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->
"""

CONTACT = page_banner("Contact", "Reach PVV leadership - we respond to nonprofits and students") + f"""
<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|80"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--80)"><!-- wp:columns {{"style":{{"spacing":{{"blockGap":{{"left":"var:preset|spacing|50"}}}}}}}} -->
<div class="wp-block-columns"><!-- wp:column {{"width":"40%"}} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|50","left":"var:preset|spacing|40","right":"var:preset|spacing|40"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"contrast","textColor":"base","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group has-base-color has-contrast-background-color has-text-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--50);padding-right:var(--wp--preset--spacing--40);padding-bottom:var(--wp--preset--spacing--50);padding-left:var(--wp--preset--spacing--40)"><!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">Email</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>{LEADER}</strong><br>President, Proyecto Vidas Valiosas</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"fontSize":"medium"}} -->
<p class="has-medium-font-size"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">Best for partnership inquiries, student interest, and general questions.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button {{"backgroundColor":"base","textColor":"contrast","width":100}} -->
<div class="wp-block-button has-custom-width wp-block-button__width-100"><a class="wp-block-button__link has-contrast-color has-base-background-color has-text-color has-background wp-element-button" href="mailto:{EMAIL}">Send Email</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column {{"width":"60%"}} -->
<div class="wp-block-column" style="flex-basis:60%"><!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">For Nonprofits</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">Share your organization's mission, the community you serve, and what kind of support you need. We will follow up to discuss fit and next steps for a consulting partnership.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">For Stanford Students</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">Interested in joining a consulting track or learning more about PVV? Email us about upcoming meetings, workshops, and how to get involved - no prior experience required.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">What to Include</h3>
<!-- /wp:heading -->

<!-- wp:list {{"fontSize":"small"}} -->
<ul class="wp-block-list has-small-font-size"><li>Your name and affiliation (org or year/major)</li><li>What you're looking for from PVV</li><li>Any relevant timeline or deadlines</li></ul>
<!-- /wp:list --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->
"""

HEADER = """<!-- wp:group {"align":"full","style":{"border":{"bottom":{"color":"var:preset|color|accent-6","width":"1px"}},"spacing":{"padding":{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignfull" style="border-bottom-color:var(--wp--preset--color--accent-6);border-bottom-width:1px;padding-top:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30)"><!-- wp:group {"layout":{"type":"constrained"}} -->
<div class="wp-block-group"><!-- wp:group {"align":"wide","layout":{"type":"flex","flexWrap":"nowrap","justifyContent":"space-between","verticalAlignment":"center"}} -->
<div class="wp-block-group alignwide"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|20"}},"layout":{"type":"flex","flexWrap":"nowrap","verticalAlignment":"center"}} -->
<div class="wp-block-group"><!-- wp:site-title {"level":0,"style":{"typography":{"fontStyle":"normal","fontWeight":"700"}}} /--></div>
<!-- /wp:group -->

<!-- wp:navigation {"overlayMenu":"never","layout":{"type":"flex","justifyContent":"right"}} -->
<!-- wp:navigation-link {"label":"Home","url":"SITE/","kind":"custom"} /-->

<!-- wp:navigation-link {"label":"About","url":"SITE/about-us/","kind":"custom"} /-->

<!-- wp:navigation-link {"label":"Projects","url":"SITE/projects/","kind":"custom"} /-->

<!-- wp:navigation-link {"label":"Contact","url":"SITE/contact/","kind":"custom"} /-->
<!-- /wp:navigation --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->""".replace("SITE", SITE)

FOOTER = """<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|70","bottom":"var:preset|spacing|50","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}},"border":{"top":{"color":"var:preset|color|accent-6","width":"1px"}}},"backgroundColor":"accent-5","layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-accent-5-background-color has-background" style="border-top-color:var(--wp--preset--color--accent-6);border-top-width:1px;padding-top:var(--wp--preset--spacing--70);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--50);padding-left:var(--wp--preset--spacing--50)"><!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column {"width":"50%"} -->
<div class="wp-block-column" style="flex-basis:50%"><!-- wp:site-title {"level":3,"style":{"typography":{"fontStyle":"normal","fontWeight":"700"}}} /-->

<!-- wp:site-tagline {"fontSize":"small"} /-->

<!-- wp:paragraph {"fontSize":"small","style":{"spacing":{"margin":{"top":"var:preset|spacing|30"}}}} -->
<p class="has-small-font-size" style="margin-top:var(--wp--preset--spacing--30)"><a href="mailto:EMAIL">EMAIL</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"25%"} -->
<div class="wp-block-column" style="flex-basis:25%"><!-- wp:heading {"level":4,"fontSize":"small"} -->
<h4 class="wp-block-heading has-small-font-size">Pages</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><a href="SITE/">Home</a><br><a href="SITE/about-us/">About Us</a><br><a href="SITE/projects/">Projects</a><br><a href="SITE/contact/">Contact</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"25%"} -->
<div class="wp-block-column" style="flex-basis:25%"><!-- wp:heading {"level":4,"fontSize":"small"} -->
<h4 class="wp-block-heading has-small-font-size">Get Involved</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><a href="SITE/contact/">Partner as a nonprofit</a><br><a href="mailto:EMAIL">Join as a student</a><br><a href="SITE/projects/">See our services</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:separator {"style":{"spacing":{"margin":{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|30"}}}} -->
<hr class="wp-block-separator has-alpha-channel-opacity" style="margin-top:var(--wp--preset--spacing--50);margin-bottom:var(--wp--preset--spacing--30)"/>
<!-- /wp:separator -->

<!-- wp:paragraph {"align":"center","fontSize":"small"} -->
<p class="has-text-align-center has-small-font-size">© 2026 Proyecto Vidas Valiosas · Stanford University</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->""".replace("SITE", SITE).replace("EMAIL", EMAIL)


def main():
    pages = {p["slug"]: p["id"] for p in api("GET", "/pages?per_page=50&context=edit")}
    updates = {
        "home": HOME,
        "about-us": ABOUT,
        "projects": PROJECTS,
        "contact": CONTACT,
    }
    for slug, content in updates.items():
        pid = pages[slug]
        api("POST", f"/pages/{pid}", {"content": content, "template": "page-no-title"})
        print(f"Updated {slug} (id={pid})")

    api("POST", "/template-parts/twentytwentyfive//header", {"content": HEADER})
    print("Updated header")

    api("POST", "/template-parts/twentytwentyfive//footer", {"content": FOOTER})
    print("Updated footer")

    print("Done!")


if __name__ == "__main__":
    main()
