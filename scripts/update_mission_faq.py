#!/usr/bin/env python3
"""Add mission content, FAQ page, and CSS animations to PVV site."""

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
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{method} {path} failed ({e.code}): {e.read().decode()}") from e


# Site-wide animation styles (injected via header HTML block)
ANIMATION_CSS = """
<style>
  @keyframes pvv-fade-up {
    from { opacity: 0; transform: translateY(28px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @keyframes pvv-fade-in {
    from { opacity: 0; }
    to   { opacity: 1; }
  }
  @keyframes pvv-hero-glow {
    0%, 100% { opacity: 0.4; }
    50%       { opacity: 0.7; }
  }
  .pvv-hero-animate {
    animation: pvv-fade-up 0.9s cubic-bezier(0.22, 1, 0.36, 1) both;
  }
  .pvv-hero-animate-d1 { animation-delay: 0.12s; }
  .pvv-hero-animate-d2 { animation-delay: 0.24s; }
  .pvv-hero-animate-d3 { animation-delay: 0.36s; }
  .pvv-fade-in {
    animation: pvv-fade-in 1s ease both;
  }
  .pvv-card {
    transition: transform 0.28s cubic-bezier(0.22, 1, 0.36, 1),
                box-shadow 0.28s ease;
  }
  .pvv-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.10);
  }
  .pvv-mission-glow {
    position: relative;
  }
  .pvv-mission-glow::before {
    content: "";
    position: absolute;
    inset: -1px;
    border-radius: inherit;
    background: linear-gradient(135deg, transparent 40%, rgba(255,255,255,0.06) 100%);
    animation: pvv-hero-glow 4s ease-in-out infinite;
    pointer-events: none;
  }
  @media (prefers-reduced-motion: reduce) {
    .pvv-hero-animate, .pvv-hero-animate-d1, .pvv-hero-animate-d2,
    .pvv-hero-animate-d3, .pvv-fade-in, .pvv-mission-glow::before {
      animation: none !important;
      opacity: 1 !important;
      transform: none !important;
    }
    .pvv-card { transition: none; }
    .pvv-card:hover { transform: none; box-shadow: none; }
  }
</style>
"""


def faq_item(question):
    return f"""
<!-- wp:details {{"className":"pvv-faq-item"}} -->
<details class="wp-block-details pvv-faq-item"><summary>{question}</summary><!-- wp:paragraph {{"fontSize":"small","textColor":"contrast-2"}} -->
<p class="has-contrast-2-color has-small-font-size"><em>Answer coming soon.</em></p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
"""


FAQ_QUESTIONS = [
    "What is Proyecto Vidas Valiosas?",
    "What makes PVV different from other Stanford service organizations?",
    "Who does PVV serve?",
    "Who can partner with PVV as a nonprofit?",
    "Is PVV's consulting really free?",
    "What kinds of projects can PVV help with?",
    "How long does a typical consulting project take?",
    "What does PVV need from partner organizations?",
    "Do I need prior consulting experience to join?",
    "How do I get involved with PVV as a Stanford student?",
    "What is the time commitment for members?",
    "How are members placed on marketing, financial, or technical teams?",
    "Can graduate students join PVV?",
    "Does PVV organize volunteering events?",
    "How can I contact PVV leadership?",
]

FAQ = f"""
<!-- wp:group {{"align":"full","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|70","bottom":"var:preset|spacing|70","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}}}}},"backgroundColor":"contrast","textColor":"base","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignfull has-base-color has-contrast-background-color has-text-color has-background pvv-hero-animate" style="padding-top:var(--wp--preset--spacing--70);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--70);padding-left:var(--wp--preset--spacing--50)"><!-- wp:heading {{"textAlign":"center","level":1,"fontSize":"xx-large"}} -->
<h1 class="wp-block-heading has-text-align-center has-xx-large-font-size">FAQ</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {{"align":"center","fontSize":"medium"}} -->
<p class="has-text-align-center has-medium-font-size">Common questions from nonprofits and Stanford students. Answers are being added - check back soon.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|80"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--80)"><!-- wp:heading -->
<h2 class="wp-block-heading">About PVV</h2>
<!-- /wp:heading -->

{"".join(faq_item(q) for q in FAQ_QUESTIONS[:3])}

<!-- wp:heading {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<h2 class="wp-block-heading" style="margin-top:var(--wp--preset--spacing--50)">For Nonprofits</h2>
<!-- /wp:heading -->

{"".join(faq_item(q) for q in FAQ_QUESTIONS[3:8])}

<!-- wp:heading {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<h2 class="wp-block-heading" style="margin-top:var(--wp--preset--spacing--50)">For Stanford Students</h2>
<!-- /wp:heading -->

{"".join(faq_item(q) for q in FAQ_QUESTIONS[8:13])}

<!-- wp:heading {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<h2 class="wp-block-heading" style="margin-top:var(--wp--preset--spacing--50)">General</h2>
<!-- /wp:heading -->

{"".join(faq_item(q) for q in FAQ_QUESTIONS[13:])}

<!-- wp:paragraph {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<p style="margin-top:var(--wp--preset--spacing--50)">Still have a question? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
"""

HOME = f"""
<!-- wp:group {{"align":"full","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|80","bottom":"var:preset|spacing|80","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}}}}},"backgroundColor":"contrast","textColor":"base","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignfull has-base-color has-contrast-background-color has-text-color has-background" style="padding-top:var(--wp--preset--spacing--80);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--80);padding-left:var(--wp--preset--spacing--50)"><!-- wp:paragraph {{"align":"center","className":"pvv-hero-animate","style":{{"typography":{{"letterSpacing":"0.08em","textTransform":"uppercase","fontStyle":"normal","fontWeight":"600"}}}},"fontSize":"small"}} -->
<p class="has-text-align-center has-small-font-size pvv-hero-animate" style="font-style:normal;font-weight:600;letter-spacing:0.08em;text-transform:uppercase">Stanford Student Organization · Est. for Community Impact</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"textAlign":"center","level":1,"fontSize":"xx-large","className":"pvv-hero-animate pvv-hero-animate-d1"}} -->
<h1 class="wp-block-heading has-text-align-center has-xx-large-font-size pvv-hero-animate pvv-hero-animate-d1">Proyecto Vidas Valiosas</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {{"align":"center","fontSize":"large","className":"pvv-hero-animate pvv-hero-animate-d2"}} -->
<p class="has-text-align-center has-large-font-size pvv-hero-animate pvv-hero-animate-d2">Free marketing, financial, and technical consulting - built for nonprofits serving low-income communities.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons {{"className":"pvv-hero-animate pvv-hero-animate-d3","layout":{{"type":"flex","justifyContent":"center"}},"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|40"}},"blockGap":"var:preset|spacing|20"}}}}}} -->
<div class="wp-block-buttons pvv-hero-animate pvv-hero-animate-d3" style="margin-top:var(--wp--preset--spacing--40)"><!-- wp:button {{"backgroundColor":"base","textColor":"contrast"}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-contrast-color has-base-background-color has-text-color has-background wp-element-button" href="{SITE}/contact/">Partner With Us</a></div>
<!-- /wp:button -->

<!-- wp:button {{"className":"is-style-outline"}} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{SITE}/about-us/">Our Mission</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->

<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|70","bottom":"var:preset|spacing|50"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide pvv-mission-glow" style="padding-top:var(--wp--preset--spacing--70);padding-bottom:var(--wp--preset--spacing--50)"><!-- wp:heading {{"textAlign":"center"}} -->
<h2 class="wp-block-heading has-text-align-center">Our Mission</h2>
<!-- /wp:heading -->

<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}}},"border":{{"radius":"12px"}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group has-accent-5-background-color has-background pvv-fade-in" style="border-radius:12px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--50)"><!-- wp:paragraph {{"align":"center","fontSize":"large"}} -->
<p class="has-text-align-center has-large-font-size">{MISSION}</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"align":"center","fontSize":"small"}} -->
<p class="has-text-align-center has-small-font-size"><em> - Proyecto Vidas Valiosas Constitution, Article II</em></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->

<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"bottom":"var:preset|spacing|60"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide" style="padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:heading {{"textAlign":"center"}} -->
<h2 class="wp-block-heading has-text-align-center">What Makes PVV Different</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {{"align":"center","style":{{"spacing":{{"margin":{{"bottom":"var:preset|spacing|40"}}}}}}}} -->
<p class="has-text-align-center" style="margin-bottom:var(--wp--preset--spacing--40)">Most campus orgs specialize in one thing - tech, data, or general service. PVV is built around <strong>three consulting tracks under one roof</strong>, serving a specific community on purpose.</p>
<!-- /wp:paragraph -->

<!-- wp:columns {{"align":"wide","style":{{"spacing":{{"blockGap":{{"left":"var:preset|spacing|30"}}}}}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"contrast","textColor":"base","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card has-base-color has-contrast-background-color has-text-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--30);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30);padding-left:var(--wp--preset--spacing--30)"><!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>Three tracks, one team</strong><br>Marketing, financial, and technical consulting - integrated, not siloed.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"contrast","textColor":"base","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card has-base-color has-contrast-background-color has-text-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--30);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30);padding-left:var(--wp--preset--spacing--30)"><!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>Community-first focus</strong><br>We partner with orgs serving low-income communities across the Bay Area - by design, not by accident.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"contrast","textColor":"base","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card has-base-color has-contrast-background-color has-text-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--30);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30);padding-left:var(--wp--preset--spacing--30)"><!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>100% free, long-term</strong><br>No fees for partners. We build lasting relationships and hand off tools you can keep running.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"contrast","textColor":"base","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card has-base-color has-contrast-background-color has-text-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--30);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30);padding-left:var(--wp--preset--spacing--30)"><!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><strong>Consulting + service</strong><br>Student teams deliver projects <em>and</em> organize volunteering events with transportation support.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->

<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"bottom":"var:preset|spacing|50"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide" style="padding-bottom:var(--wp--preset--spacing--50)"><!-- wp:columns {{"style":{{"spacing":{{"blockGap":{{"left":"var:preset|spacing|40"}}}}}}}} -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|50","left":"var:preset|spacing|40","right":"var:preset|spacing|40"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card has-accent-5-background-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--50);padding-right:var(--wp--preset--spacing--40);padding-bottom:var(--wp--preset--spacing--50);padding-left:var(--wp--preset--spacing--40)"><!-- wp:heading {{"level":3}} -->
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
<div class="wp-block-column"><!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|50","left":"var:preset|spacing|40","right":"var:preset|spacing|40"}}}},"border":{{"radius":"8px"}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card has-accent-5-background-color has-background" style="border-radius:8px;padding-top:var(--wp--preset--spacing--50);padding-right:var(--wp--preset--spacing--40);padding-bottom:var(--wp--preset--spacing--50);padding-left:var(--wp--preset--spacing--40)"><!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">For Stanford Students</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Build real consulting skills while supporting community organizations. No prior experience required - just show up ready to learn.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><a href="mailto:{EMAIL}">Get in touch →</a> · <a href="{SITE}/faq/">Read FAQ</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->

<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"bottom":"var:preset|spacing|70"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide" style="padding-bottom:var(--wp--preset--spacing--70)"><!-- wp:heading {{"textAlign":"center"}} -->
<h2 class="wp-block-heading has-text-align-center">What We Do</h2>
<!-- /wp:heading -->

<!-- wp:columns {{"align":"wide","style":{{"spacing":{{"blockGap":{{"left":"var:preset|spacing|40"}},"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<div class="wp-block-columns alignwide" style="margin-top:var(--wp--preset--spacing--50)"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"width":"1px","color":"var:preset|color|accent-6","radius":"8px"}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card" style="border-color:var(--wp--preset--color--accent-6);border-radius:8px;border-width:1px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--30)"><!-- wp:heading {{"level":3,"fontSize":"large"}} -->
<h3 class="wp-block-heading has-large-font-size">Marketing</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">Social media, flyers, event promotion, and Haas Center outreach to bring volunteers and donors to your door.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"width":"1px","color":"var:preset|color|accent-6","radius":"8px"}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card" style="border-color:var(--wp--preset--color--accent-6);border-radius:8px;border-width:1px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--30)"><!-- wp:heading {{"level":3,"fontSize":"large"}} -->
<h3 class="wp-block-heading has-large-font-size">Financial</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">Grant applications, structured budgets, and financial planning so your programs stay funded.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {{"className":"pvv-card","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}}},"border":{{"width":"1px","color":"var:preset|color|accent-6","radius":"8px"}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group pvv-card" style="border-color:var(--wp--preset--color--accent-6);border-radius:8px;border-width:1px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--30)"><!-- wp:heading {{"level":3,"fontSize":"large"}} -->
<h3 class="wp-block-heading has-large-font-size">Technical</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">Websites, forms, surveys, and data tools that save your team hours every week.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->

<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"bottom":"var:preset|spacing|50"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide" style="padding-bottom:var(--wp--preset--spacing--50)"><!-- wp:heading {{"textAlign":"center"}} -->
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

<!-- wp:buttons {{"layout":{{"type":"flex","justifyContent":"center"}},"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|30"}},"blockGap":"var:preset|spacing|20"}}}}}} -->
<div class="wp-block-buttons" style="margin-top:var(--wp--preset--spacing--30)"><!-- wp:button {{"backgroundColor":"base","textColor":"contrast"}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-contrast-color has-base-background-color has-text-color has-background wp-element-button" href="mailto:{EMAIL}">{EMAIL}</a></div>
<!-- /wp:button -->

<!-- wp:button {{"className":"is-style-outline"}} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{SITE}/faq/">View FAQ</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->
"""

ABOUT_MISSION_SECTION = f"""
<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|40","right":"var:preset|spacing|40"}}}},"border":{{"radius":"12px"}}}},"backgroundColor":"accent-5","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group has-accent-5-background-color has-background pvv-fade-in" style="border-radius:12px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--40);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--40)"><!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">Our Mission</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"medium"}} -->
<p class="has-medium-font-size">{MISSION}</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size"><em>Proyecto Vidas Valiosas Constitution, Article II</em></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
"""

HEADER = (
    f'<!-- wp:html -->\n{ANIMATION_CSS}\n<!-- /wp:html -->\n\n'
    + """<!-- wp:group {"align":"full","style":{"border":{"bottom":{"color":"var:preset|color|accent-6","width":"1px"}},"spacing":{"padding":{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignfull" style="border-bottom-color:var(--wp--preset--color--accent-6);border-bottom-width:1px;padding-top:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30)"><!-- wp:group {"layout":{"type":"constrained"}} -->
<div class="wp-block-group"><!-- wp:group {"align":"wide","layout":{"type":"flex","flexWrap":"nowrap","justifyContent":"space-between","verticalAlignment":"center"}} -->
<div class="wp-block-group alignwide"><!-- wp:site-title {"level":0,"style":{"typography":{"fontStyle":"normal","fontWeight":"700"}}} /-->

<!-- wp:navigation {"overlayMenu":"never","layout":{"type":"flex","justifyContent":"right"}} -->
<!-- wp:navigation-link {"label":"Home","url":"SITE/","kind":"custom"} /-->

<!-- wp:navigation-link {"label":"About","url":"SITE/about-us/","kind":"custom"} /-->

<!-- wp:navigation-link {"label":"Projects","url":"SITE/projects/","kind":"custom"} /-->

<!-- wp:navigation-link {"label":"FAQ","url":"SITE/faq/","kind":"custom"} /-->

<!-- wp:navigation-link {"label":"Contact","url":"SITE/contact/","kind":"custom"} /-->
<!-- /wp:navigation --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->""".replace("SITE", SITE)
)

FOOTER_EXTRA_FAQ = """<br><a href="SITE/faq/">FAQ</a>""".replace("SITE", SITE)


def patch_about_page(existing_content):
    banner_end = existing_content.find("<!-- /wp:group -->") + len("<!-- /wp:group -->")
    return existing_content[:banner_end] + "\n\n" + ABOUT_MISSION_SECTION + existing_content[banner_end:]


def patch_footer(existing_footer):
    old = '<a href="SITE/contact/">Contact</a></p>'
    new = f'<a href="SITE/contact/">Contact</a>{FOOTER_EXTRA_FAQ}</p>'
    return existing_footer.replace("SITE", SITE).replace(old.replace("SITE", SITE), new.replace("SITE", SITE))


def main():
    pages = {p["slug"]: p for p in api("GET", "/pages?per_page=50&context=edit")}

    # Home
    api("POST", f"/pages/{pages['home']['id']}", {"content": HOME, "template": "page-no-title"})
    print("Updated home with mission + animations")

    # About - prepend mission block after banner
    about_content = patch_about_page(pages["about-us"]["content"]["raw"])
    api("POST", f"/pages/{pages['about-us']['id']}", {"content": about_content, "template": "page-no-title"})
    print("Updated about with constitution mission")

    # FAQ - create or update
    if "faq" in pages:
        faq_id = pages["faq"]["id"]
        api("POST", f"/pages/{faq_id}", {"content": FAQ, "status": "publish", "template": "page-no-title"})
        print(f"Updated faq (id={faq_id})")
    else:
        faq = api("POST", "/pages", {
            "title": "FAQ",
            "slug": "faq",
            "content": FAQ,
            "status": "publish",
            "template": "page-no-title",
        })
        print(f"Created faq (id={faq['id']}) link={faq['link']}")

    # Header with CSS + FAQ nav
    api("POST", "/template-parts/twentytwentyfive//header", {"content": HEADER})
    print("Updated header with animation CSS + FAQ link")

    # Footer - add FAQ link
    footer = api("GET", "/template-parts/twentytwentyfive//footer?context=edit")
    footer_content = footer["content"]["raw"]
    if "/faq/" not in footer_content:
        footer_content = footer_content.replace(
            f'<a href="{SITE}/contact/">Contact</a></p>',
            f'<a href="{SITE}/contact/">Contact</a><br><a href="{SITE}/faq/">FAQ</a></p>',
        )
        api("POST", "/template-parts/twentytwentyfive//footer", {"content": footer_content})
    print("Updated footer")

    # Site tagline - mission-aligned
    url = "https://pvv.su.domains/wp-json/wp/v2/settings"
    body = json.dumps({
        "description": "Free student consulting for Bay Area nonprofits serving low-income communities - marketing, financial, and technical.",
    }).encode()
    req = urllib.request.Request(url, data=body, headers=auth_header(), method="POST")
    with urllib.request.urlopen(req, timeout=20):
        pass
    print("Updated site tagline")
    print("Done!")


if __name__ == "__main__":
    main()
