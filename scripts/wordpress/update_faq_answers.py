#!/usr/bin/env python3
"""Update FAQ page with draft answers."""

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

FAQ_SECTIONS = [
    ("About PVV", [
        (
            "What is Proyecto Vidas Valiosas?",
            "Proyecto Vidas Valiosas (PVV) is a Stanford student organization that connects "
            "local nonprofits and community-based organizations with free consulting in marketing, "
            "financial planning, and technology. We also organize volunteering events, workshops, "
            "and community-building activities for members throughout the year.",
        ),
        (
            "What makes PVV different from other Stanford service organizations?",
            "Most campus orgs specialize in one area - data, tech, or general service. PVV combines "
            "<strong>marketing, financial, and technical consulting under one roof</strong>, and we "
            "focus specifically on organizations serving <strong>low-income communities</strong> in "
            "the Bay Area. Our consulting is 100% free, we prioritize long-term partnerships over "
            "one-off projects, and we pair consulting work with direct volunteering.",
        ),
        (
            "Who does PVV serve?",
            "Two groups: (1) <strong>Nonprofit partners</strong> - local nonprofits and CBOs serving "
            "low-income communities, and (2) <strong>Stanford students</strong> - undergraduates and "
            "graduate students who want hands-on consulting experience and meaningful community impact.",
        ),
    ]),
    ("For Nonprofits", [
        (
            "Who can partner with PVV as a nonprofit?",
            "We partner with local nonprofits and community-based organizations, especially those "
            "serving disadvantaged and low-income communities in the Bay Area. If your organization "
            "needs marketing, financial, or technical support, email us - we'll discuss fit and scope.",
        ),
        (
            "Is PVV's consulting really free?",
            "Yes. All consulting is provided by Stanford student volunteers at <strong>no cost</strong> "
            "to partner organizations. PVV covers its own operational costs (transportation, printing, "
            "etc.) through Stanford funding sources like the Haas Center.",
        ),
        (
            "What kinds of projects can PVV help with?",
            "<strong>Marketing:</strong> social media, flyers, event promotion, Haas Center outreach.<br>"
            "<strong>Financial:</strong> grant applications, structured budgets, fundraising planning, "
            "resource navigation.<br>"
            "<strong>Technical:</strong> websites, forms, surveys, data collection pipelines, and tools "
            "to improve donations and operations.",
        ),
        (
            "How long does a typical consulting project take?",
            "Most projects run across a Stanford quarter (roughly 8–10 weeks), but timelines depend on "
            "scope. We define a realistic schedule with your organization during intake and check in "
            "regularly throughout the project.",
        ),
        (
            "What does PVV need from partner organizations?",
            "A primary point of contact, clarity on your goals, timely feedback on deliverables, and "
            "access to brand assets or program information as needed. Your leadership maintains final "
            "approval on all work - PVV advises and builds, but you own the outcomes.",
        ),
    ]),
    ("For Stanford Students", [
        (
            "Do I need prior consulting experience to join?",
            "No. PVV is built for students with little or no background in marketing, finance, or tech. "
            "We run training across all three tracks and pair newer members with more experienced ones on "
            "real client projects.",
        ),
        (
            "How do I get involved with PVV as a Stanford student?",
            f"Email <a href=\"mailto:{EMAIL}\">{EMAIL}</a> to learn about upcoming meetings, events, "
            "and open project teams. You can also ask about joining our mailing list to stay updated on "
            "PVV events throughout the quarter.",
        ),
        (
            "What is the time commitment for members?",
            "Commitment varies by role and project, but active members attend weekly general meetings "
            "and contribute to their consulting team's deliverables throughout the quarter. Category "
            "Chairs and officers may have additional responsibilities.",
        ),
        (
            "How are members placed on marketing, financial, or technical teams?",
            "Members join one of three consulting tracks - Marketing, Financial, or Technical - based "
            "on interest and skills. Consulting Category Chairs lead each track and assign members to "
            "client projects within their specialization.",
        ),
        (
            "Can graduate students join PVV?",
            "Yes. Membership is open to all interested Stanford undergraduate and graduate students. "
            "Students on a leave of absence may participate in events but cannot hold leadership positions.",
        ),
    ]),
    ("General", [
        (
            "Does PVV organize volunteering events?",
            "Yes. We organize volunteering events that bring Stanford students to serve local nonprofits "
            "directly, with transportation provided when available. These events complement our consulting "
            "work and help students connect with the community.",
        ),
        (
            "How can I contact PVV leadership?",
            f"Email <strong>{LEADER}</strong>, PVV President, at "
            f"<a href=\"mailto:{EMAIL}\">{EMAIL}</a>. For partnership inquiries, student interest, "
            "or general questions, email is the best way to reach us.",
        ),
    ]),
]


def auth_header():
    token = base64.b64encode(f"{USER}:{PASSWORD}".encode()).decode()
    return {"Authorization": f"Basic {token}", "Content-Type": "application/json"}


def api(method, path, data=None):
    url = f"{BASE}{path}"
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, headers=auth_header(), method=method)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def faq_item(question, answer):
    return f"""
<!-- wp:details {{"className":"pvv-faq-item"}} -->
<details class="wp-block-details pvv-faq-item"><summary>{question}</summary><!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">{answer}</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
"""


def build_faq_content():
    parts = [
        f"""
<!-- wp:group {{"align":"full","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|70","bottom":"var:preset|spacing|70","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}}}}},"backgroundColor":"contrast","textColor":"base","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignfull has-base-color has-contrast-background-color has-text-color has-background pvv-hero-animate" style="padding-top:var(--wp--preset--spacing--70);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--70);padding-left:var(--wp--preset--spacing--50)"><!-- wp:heading {{"textAlign":"center","level":1,"fontSize":"xx-large"}} -->
<h1 class="wp-block-heading has-text-align-center has-xx-large-font-size">FAQ</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {{"align":"center","fontSize":"medium"}} -->
<p class="has-text-align-center has-medium-font-size">Answers for nonprofits and Stanford students interested in working with PVV.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {{"align":"wide","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|80"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--80)">"""
    ]

    for i, (section_title, items) in enumerate(FAQ_SECTIONS):
        margin = "var:preset|spacing|50" if i > 0 else None
        if margin:
            parts.append(f"""
<!-- wp:heading {{"style":{{"spacing":{{"margin":{{"top":"{margin}"}}}}}}}} -->
<h2 class="wp-block-heading" style="margin-top:var(--wp--preset--spacing--50)">{section_title}</h2>
<!-- /wp:heading -->
""")
        else:
            parts.append(f"""
<!-- wp:heading -->
<h2 class="wp-block-heading">{section_title}</h2>
<!-- /wp:heading -->
""")
        for q, a in items:
            parts.append(faq_item(q, a))

    parts.append(f"""
<!-- wp:paragraph {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50"}}}}}}}} -->
<p style="margin-top:var(--wp--preset--spacing--50)">Still have a question? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
""")
    return "".join(parts)


def main():
    pages = {p["slug"]: p["id"] for p in api("GET", "/pages?per_page=50&context=edit")}
    faq_id = pages["faq"]
    api("POST", f"/pages/{faq_id}", {
        "content": build_faq_content(),
        "template": "page-no-title",
    })
    print(f"Updated FAQ page (id={faq_id}) with draft answers")


if __name__ == "__main__":
    main()
