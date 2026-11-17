#!/usr/bin/env python3
"""Shared HTML for the public CRRE Labs pages. Run via scripts/render_site.py."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHONE_DISPLAY = "(786) 733-6744"
PHONE_TEL = "+17867336744"
EMAIL = "hello@crrelabs.com"
ADDRESS = "12394 SW 82nd Ave, Pinecrest, FL 33156"
STREET = "12394 SW 82nd Ave"
LASTMOD = "2026-11-17"
FORM_ACTION = "https://crre-sms-hubspot-4207-prod.twil.io/form/contact"
STRIPE = {
    "starter": "https://buy.stripe.com/9B6eVd1AKgCP3R3f4gdwc07",
    "business": "https://buy.stripe.com/aFa4gz93c4U7gDPaO0dwc08",
    "pro": "https://buy.stripe.com/00wcN54MWgCP1IVg8kdwc09",
}
CSP = (
    "default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://*.googletagmanager.com; "
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; "
    "font-src 'self' data: https://fonts.gstatic.com https://cdnjs.cloudflare.com; "
    "img-src 'self' data: https://crrelabs.com https://www.crrelabs.com https://*.google-analytics.com https://*.googletagmanager.com; "
    "connect-src 'self' https://crre-sms-hubspot-4207-prod.twil.io https://*.google-analytics.com https://*.analytics.google.com https://*.googletagmanager.com; "
    "form-action 'self' https://crre-sms-hubspot-4207-prod.twil.io; frame-src 'none'; object-src 'none'; base-uri 'self'; upgrade-insecure-requests"
)

AREAS = [
    ("Pinecrest", "/web-design-pinecrest/"),
    ("Kendall", "/web-design-kendall/"),
    ("South Miami", "/web-design-south-miami/"),
    ("Coral Gables", "/web-design-coral-gables/"),
    ("Palmetto Bay", "/web-design-palmetto-bay/"),
    ("Miami", "/web-design-miami/"),
]
INDUSTRIES = [
    ("Restaurants", "/websites-for-restaurants/"),
    ("Contractors and home services", "/websites-for-contractors/"),
    ("Salons and spas", "/websites-for-salons-and-spas/"),
    ("Medical and dental offices", "/websites-for-medical-and-dental/"),
    ("Property managers and real estate", "/websites-for-property-managers/"),
]

SMS = (
    'I separately agree to receive <strong class="text-gray-200">marketing SMS</strong> from CRRE Labs LLC about web design, '
    "AI automation, demos, and promotional offers. Msg frequency varies (up to 5/month). Msg &amp; data rates may apply. "
    'Reply STOP to opt out, HELP for help. Consent is not a condition of purchase. '
    '<a href="/sms-policy/" class="text-accent hover:underline">SMS Policy</a>, '
    '<a href="/privacy/" class="text-accent hover:underline">Privacy Policy</a>, and '
    '<a href="/terms/" class="text-accent hover:underline">Terms of Service</a>.'
)


def dumps(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False)


def postal():
    return {
        "@type": "PostalAddress",
        "streetAddress": STREET,
        "addressLocality": "Pinecrest",
        "addressRegion": "FL",
        "postalCode": "33156",
        "addressCountry": "US",
    }


def cities(names=None):
    names = names or [name for name, _ in AREAS]
    return [
        {"@type": "City", "name": name, "containedInPlace": {"@type": "State", "name": "Florida"}}
        for name in names
    ]


def org_block():
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "CRRE Labs LLC",
        "url": "https://crrelabs.com/",
        "logo": "https://crrelabs.com/logo.jpg",
        "email": EMAIL,
        "telephone": "+1-786-733-6744",
        "address": postal(),
        "sameAs": ["TODO_GBP_URL"],
    }


def business_block():
    return {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": "CRRE Labs LLC",
        "url": "https://crrelabs.com/",
        "logo": "https://crrelabs.com/logo.jpg",
        "image": "https://crrelabs.com/assets/og-image.png",
        "description": "Website design studio in Pinecrest, Florida, building affordable websites for small businesses in Pinecrest, Kendall, South Miami, Coral Gables, Palmetto Bay, and Miami.",
        "email": EMAIL,
        "telephone": "+1-786-733-6744",
        "priceRange": "$",
        "address": postal(),
        "geo": {"@type": "GeoCoordinates", "latitude": 25.6654, "longitude": -80.3093},
        "areaServed": cities(),
        "serviceType": ["Website design", "Small business websites"],
        "sameAs": ["TODO_GBP_URL"],
    }


def website_block():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "CRRE Labs",
        "url": "https://crrelabs.com/",
    }


def service_block(name, url, city, description):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "serviceType": "Website design",
        "description": description,
        "url": url,
        "provider": {
            "@type": "ProfessionalService",
            "name": "CRRE Labs LLC",
            "url": "https://crrelabs.com/",
            "telephone": "+1-786-733-6744",
            "email": EMAIL,
            "address": postal(),
        },
        "areaServed": cities([city]) if city else cities(),
        "offers": [
            {"@type": "Offer", "name": "Starter setup", "price": "99", "priceCurrency": "USD", "description": "One-time setup. Monthly fee is $15."},
            {"@type": "Offer", "name": "Business setup", "price": "199", "priceCurrency": "USD", "description": "One-time setup. Monthly fee is $29."},
            {"@type": "Offer", "name": "Pro setup", "price": "349", "priceCurrency": "USD", "description": "One-time setup. Monthly fee is $49."},
        ],
    }


def faq_block(pairs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in pairs
        ],
    }


def breadcrumb(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": url}
            for i, (name, url) in enumerate(items)
        ],
    }


def article_block(headline, url, description):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": headline,
        "description": description,
        "datePublished": LASTMOD,
        "dateModified": LASTMOD,
        "mainEntityOfPage": url,
        "author": {"@type": "Organization", "name": "CRRE Labs LLC", "url": "https://crrelabs.com/"},
        "publisher": {
            "@type": "Organization",
            "name": "CRRE Labs LLC",
            "logo": {"@type": "ImageObject", "url": "https://crrelabs.com/logo.jpg"},
        },
    }


def jsonld(*blocks):
    return "\n".join(
        f'<script type="application/ld+json">\n{dumps(block)}\n</script>' for block in blocks
    )


def nav(current):
    def item(href, label):
        current_attr = ' aria-current="page"' if href == current else ""
        weight = "text-white" if href == current else "text-gray-300"
        return f'<a href="{href}" class="nav-link text-sm {weight} hover:text-white transition"{current_attr}>{label}</a>'

    def details(label, links, mobile=False):
        rows = []
        for text, href in links:
            mark = ' aria-current="page"' if href == current else ""
            if mobile:
                rows.append(f'<a href="{href}" class="block py-1 text-gray-300 hover:text-white"{mark}>{html.escape(text)}</a>')
            else:
                rows.append(f'<a href="{href}" class="block px-4 py-2 text-sm text-gray-200 hover:bg-white/5 hover:text-white"{mark}>{html.escape(text)}</a>')
        if mobile:
            return (
                f'<details class="nav-details"><summary class="text-gray-300">{label}</summary>'
                f'<div class="pl-3 pt-2 space-y-1">{"".join(rows)}</div></details>'
            )
        return (
            f'<details class="nav-details relative"><summary class="nav-link text-sm text-gray-300 hover:text-white">{label}</summary>'
            f'<div class="absolute left-0 mt-3 w-64 glass rounded-xl py-2 z-50">{"".join(rows)}</div></details>'
        )

    desktop = f'''
    <nav class="hidden lg:flex items-center gap-6" aria-label="Primary">
      {item("/", "Home")}
      {item("/pricing/", "Pricing")}
      {item("/portfolio/", "Portfolio")}
      {item("/work/", "Work")}
      {details("Areas", AREAS)}
      {details("Industries", INDUSTRIES)}
      {item("/blog/", "Blog")}
      <a href="tel:+{PHONE_TEL}" class="text-sm text-white font-semibold hover:text-accent">{PHONE_DISPLAY}</a>
      <a href="{('#contact' if current == '/' else '/#contact')}" class="px-4 py-2 bg-accent-strong text-white rounded-full text-sm font-semibold hover:bg-blue-800 transition">Get a quote</a>
    </nav>'''
    mobile_links = [
        ("/", "Home"),
        ("/pricing/", "Pricing"),
        ("/portfolio/", "Portfolio"),
        ("/work/", "Work"),
        ("/blog/", "Blog"),
    ]
    mobile = "\n".join(
        f'<a href="{href}" class="block text-gray-200 hover:text-white"{" aria-current=\"page\"" if href == current else ""}>{label}</a>'
        for href, label in mobile_links
    )
    return f'''
<a class="skip-link" href="#main">Skip to content</a>
<header id="header" class="fixed top-0 w-full z-50 transition-all duration-300">
<div class="max-w-7xl mx-auto px-4 sm:px-6 py-4 flex items-center justify-between gap-4">
  <a href="/" class="flex items-center gap-3 shrink-0">
    <img src="/logo.jpg" alt="" width="40" height="40" class="h-10 w-10 rounded-lg object-cover">
    <span class="font-display font-bold text-xl text-white">CRRE Labs</span>
  </a>
  {desktop}
  <div class="flex items-center gap-3 lg:hidden">
    <a href="tel:+{PHONE_TEL}" class="text-sm font-semibold text-white">{PHONE_DISPLAY}</a>
    <button id="menu-btn" class="text-white text-sm font-semibold px-3 py-2 border border-white/20 rounded-lg" aria-expanded="false" aria-controls="mobile-menu">Menu</button>
  </div>
</div>
<div id="mobile-menu" class="hidden lg:hidden bg-dark-card/95 backdrop-blur-xl border-t border-white/10 px-6 py-6 space-y-4">
  {mobile}
  {details("Areas", AREAS, mobile=True)}
  {details("Industries", INDUSTRIES, mobile=True)}
  <a href="tel:+{PHONE_TEL}" class="block text-accent font-semibold">Call {PHONE_DISPLAY}</a>
  <a href="/#contact" class="block text-accent">Get a quote</a>
</div>
</header>'''


def footer():
    def col(title, links):
        items = "\n".join(
            f'<li><a class="hover:text-white" href="{href}">{html.escape(label)}</a></li>' for label, href in links
        )
        return f'<div><h2 class="font-display text-white text-sm font-semibold mb-3">{title}</h2><ul class="space-y-2 text-sm text-gray-400">{items}</ul></div>'

    return f'''
<footer class="border-t border-white/10 py-12">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 grid gap-10 md:grid-cols-2 lg:grid-cols-4">
    <div>
      <p class="font-display font-semibold text-white text-lg">CRRE Labs LLC</p>
      <p class="text-sm text-gray-300 mt-3 leading-relaxed">Website design studio<br>{ADDRESS}</p>
      <p class="text-sm mt-3"><a class="text-white font-semibold hover:text-accent" href="tel:+{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
      <p class="text-sm mt-1"><a class="text-gray-300 hover:text-white" href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    {col("Areas", AREAS)}
    {col("Industries", INDUSTRIES)}
    {col("More", [("Pricing", "/pricing/"), ("Portfolio", "/portfolio/"), ("Case studies", "/work/"), ("Blog", "/blog/"), ("Iris", "/iris/"), ("3D printing", "/3d-printing.html"), ("Contact", "/#contact")])}
  </div>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 mt-10 pt-6 border-t border-white/10 flex flex-col md:flex-row gap-3 md:justify-between text-xs text-gray-400">
    <p>© 2026 CRRE Labs LLC · {ADDRESS} · {PHONE_DISPLAY}</p>
    <p><a class="hover:text-white" href="/privacy/">Privacy Policy</a> · <a class="hover:text-white" href="/terms/">Terms of Service</a> · <a class="hover:text-white" href="/sms-policy/">SMS Policy</a></p>
  </div>
</footer>
<div class="fixed bottom-0 inset-x-0 z-40 lg:hidden bg-[#0a0e1a]/95 border-t border-white/10 backdrop-blur px-4 py-3 grid grid-cols-2 gap-3">
  <a href="tel:+{PHONE_TEL}" class="text-center py-3 rounded-full bg-accent-strong text-white font-semibold">Call</a>
  <a href="/#contact" class="text-center py-3 rounded-full border border-white/30 text-white font-semibold">Get a quote</a>
</div>'''


def head(title, description, canonical, schemas, robots="index, follow"):
    return f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:site_name" content="CRRE Labs">
<meta property="og:locale" content="en_US">
<meta property="og:image" content="https://crrelabs.com/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="CRRE Labs, website design for small businesses in Pinecrest and Miami">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(description)}">
<meta name="twitter:image" content="https://crrelabs.com/assets/og-image.png">
<meta name="theme-color" content="#0a0e1a">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="referrer" content="strict-origin-when-cross-origin">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Space+Grotesk:wght@500;600;700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-BJ1J3E32GP"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-BJ1J3E32GP');
</script>
{schemas}
</head>
<body class="font-body has-callbar">
<noscript><style>.reveal{{opacity:1!important;transform:none!important}}</style></noscript>'''


def scripts():
    return '<script src="/assets/site-config.js"></script>\n<script src="/assets/site.js"></script>\n</body>\n</html>\n'


def page(title, description, canonical, current, body, schemas):
    return head(title, description, canonical, schemas) + nav(current) + body + footer() + scripts()


def write_page(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return "https://crrelabs.com/" + rel.replace("index.html", "")


def picture(stem, alt, width=1280, height=800):
    safe_alt = html.escape(alt)
    return f'''<picture>
  <source srcset="/portfolio/screenshots/{stem}.webp" type="image/webp">
  <img src="/portfolio/screenshots/{stem}.jpg" alt="{safe_alt}" width="{width}" height="{height}" loading="lazy" decoding="async" class="w-full h-full object-cover object-top">
</picture>'''


def packages(heading="Website packages"):
    cards = [
        ("Starter", "15", "99", "website-starter", STRIPE["starter"], False, [
            "1 page",
            "Contact form",
            "Domain, SSL, and hosting",
            "SEO is not included",
            "Reactivation within 90 days: $49",
        ]),
        ("Business", "29", "199", "website-business", STRIPE["business"], True, [
            "Up to 5 pages",
            "Contact form and click-to-call",
            "Basic on-page SEO and Google Business Profile optimization",
            "1 revision a month",
            "Domain, SSL, and hosting",
            "Reactivation within 90 days: $99",
        ]),
        ("Pro", "49", "349", "website-pro", STRIPE["pro"], False, [
            "Up to 10 pages",
            "Contact form and click-to-call",
            "Basic on-page SEO and Google Business Profile optimization",
            "Booking widget or Stripe embed",
            "Analytics report",
            "1–2 content updates a month",
            "Domain, SSL, and hosting",
            "Reactivation within 90 days: $175",
        ]),
    ]
    html_cards = []
    for name, monthly, setup, plan, url, featured, features in cards:
        klass = "glass-featured" if featured else "glass"
        badge = '<span class="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-1 bg-accent-strong text-white text-xs font-semibold rounded-full">Most popular</span>' if featured else ""
        items = "\n".join(
            f'<li class="flex gap-2 text-sm text-gray-200"><span aria-hidden="true" class="text-accent-cyan">✓</span><span>{html.escape(feature)}</span></li>'
            for feature in features
        )
        button = "bg-accent-strong text-white hover:bg-blue-800" if featured else "border border-white/30 text-white hover:bg-white/5"
        html_cards.append(f'''
<article class="{klass} rounded-2xl p-6 flex flex-col relative">
  {badge}
  <h3 class="font-display text-lg text-white font-semibold">{name}</h3>
  <p class="mt-3"><span class="stat-num font-display text-4xl font-bold">${monthly}</span><span class="text-gray-300 text-sm">/mo</span></p>
  <p class="text-sm text-gray-300 mb-4">+ ${setup} one-time setup</p>
  <ul class="space-y-2 mb-6 flex-1">{items}</ul>
  <a href="{url}" data-plan="{plan}" data-item-name="{name} website package" data-value="{setup}" target="_blank" rel="noopener noreferrer" class="block text-center px-5 py-3 rounded-full font-semibold {button}">Pay setup with Stripe</a>
</article>''')
    return f'''
<section id="packages" class="py-16">
  <div class="max-w-7xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-3xl sm:text-4xl font-bold text-white mb-3">{heading}</h2>
    <p class="text-gray-300 max-w-3xl mb-8">Month-to-month. Setup is due up front and is non-refundable once development begins. Monthly billing is recurring. The full table, including what is not included, is on the <a class="text-accent underline" href="/pricing/">pricing page</a>.</p>
    <div class="grid lg:grid-cols-3 gap-6">{''.join(html_cards)}</div>
  </div>
</section>'''


def contact_form(page_id, intro):
    return f'''
<section id="contact" class="py-16">
  <div class="max-w-2xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-3xl font-bold text-white mb-3">Tell us about the business</h2>
    <p class="text-gray-300 mb-6">{intro}</p>
    <form id="contact-form" data-lead-form class="space-y-4" action="{FORM_ACTION}" method="POST">
      <input type="hidden" name="_page" value="{html.escape(page_id)}">
      <input type="text" name="company_website" value="" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;height:0;width:0;opacity:0">
      <div class="grid sm:grid-cols-2 gap-4">
        <input type="text" name="name" aria-label="Name" placeholder="Name" autocomplete="name" required class="w-full px-4 py-3 bg-dark-card border border-white/15 rounded-xl text-white">
        <input type="email" name="email" aria-label="Email" placeholder="Email" autocomplete="email" required class="w-full px-4 py-3 bg-dark-card border border-white/15 rounded-xl text-white">
      </div>
      <input type="tel" name="phone" aria-label="Phone number, optional" placeholder="Phone number (optional)" autocomplete="tel" class="w-full px-4 py-3 bg-dark-card border border-white/15 rounded-xl text-white">
      <label class="block text-sm text-gray-300" for="service-select">What do you need?</label>
      <select id="service-select" name="service" class="w-full px-4 py-3 bg-dark-card border border-white/15 rounded-xl text-gray-200">
        <option value="">Select one</option>
        <option value="website-starter">Local business website — Starter ($99 + $15/mo)</option>
        <option value="website-business">Local business website — Business ($199 + $29/mo)</option>
        <option value="website-pro">Local business website — Pro ($349 + $49/mo)</option>
        <option value="website">Custom website, outside the packages</option>
        <option value="ai-agent">Custom AI agent</option>
        <option value="automation">Workflow automation</option>
        <option value="3d">3D modeling and 3D printing</option>
      </select>
      <textarea name="message" aria-label="Project details" placeholder="What does the business do, and which neighborhood is it in?" rows="5" required class="w-full px-4 py-3 bg-dark-card border border-white/15 rounded-xl text-white"></textarea>
      <p class="text-sm text-gray-400">Submitting this form sends your inquiry. We follow up by email. Providing a phone number does not opt you in to SMS.</p>
      <label class="flex items-start gap-3 text-sm text-gray-300 pt-3 border-t border-white/10">
        <input type="checkbox" name="sms_consent" value="yes" class="mt-1">
        <span>{SMS}</span>
      </label>
      <button type="submit" class="w-full py-3 bg-accent-strong text-white font-semibold rounded-xl hover:bg-blue-800">Send message</button>
    </form>
    <p class="mt-8 text-sm text-gray-300">Or call <a class="text-white font-semibold" href="tel:+{PHONE_TEL}">{PHONE_DISPLAY}</a>. Studio: {ADDRESS}. Email: <a class="underline" href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  </div>
</section>'''


def faq_html(pairs):
    rows = []
    for q, a in pairs:
        rows.append(
            f'<details class="glass rounded-xl p-4"><summary class="font-semibold text-white cursor-pointer">{html.escape(q)}</summary>'
            f'<p class="text-gray-300 mt-3 leading-relaxed">{html.escape(a)}</p></details>'
        )
    return f'<section class="py-8"><div class="max-w-3xl mx-auto px-4 sm:px-6"><h2 class="font-display text-3xl font-bold text-white mb-4">Questions</h2><div class="space-y-3">{"".join(rows)}</div></div></section>'


def crumbs(items):
    parts = []
    for i, (name, url) in enumerate(items):
        if i == len(items) - 1:
            parts.append(f'<li class="text-gray-200" aria-current="page">{html.escape(name)}</li>')
        else:
            parts.append(f'<li><a class="text-accent hover:underline" href="{url}">{html.escape(name)}</a></li>')
    return f'<nav aria-label="Breadcrumb" class="text-sm mb-6"><ol class="flex flex-wrap gap-2 text-gray-400">{"".join(parts)}</ol></nav>'


RATING_HTML = '<span data-google-rating>5.0</span> from <span data-google-review-count>24</span> Google reviews'
REVIEW_URL = "https://g.page/r/CVrw8wHphIngEAI/review"


def reviews_section():
    return f'''
<section id="reviews" class="py-16" aria-labelledby="reviews-heading">
  <div class="max-w-7xl mx-auto px-4 sm:px-6">
    <h2 id="reviews-heading" class="font-display text-3xl font-bold text-white mb-3">Google reviews</h2>
    <p class="text-gray-300 max-w-3xl mb-4">Google Business Profile category: Website designer. Rating on that profile: {RATING_HTML}. The quotes themselves are not printed here yet.</p>
    <div class="flex flex-col sm:flex-row flex-wrap gap-3 mb-4">
      <a id="google-reviews-link" data-review-link="reviews" href="{REVIEW_URL}" target="_blank" rel="noopener noreferrer" class="inline-flex justify-center px-5 py-3 rounded-full bg-accent-strong text-white font-semibold">See our Google reviews</a>
      <a data-review-link="leave" href="{REVIEW_URL}" target="_blank" rel="noopener noreferrer" class="inline-flex justify-center px-5 py-3 rounded-full border border-white/30 text-white font-semibold">Leave us a Google review</a>
      <a data-review-link="profile" href="#reviews" class="inline-flex justify-center px-5 py-3 rounded-full border border-white/30 text-white font-semibold" aria-disabled="true">Google Business Profile</a>
    </div>
    <p id="review-link-note" class="text-sm text-amber-200 mb-6">The Google Business Profile URL is still a TODO in <code>assets/site-config.js</code>. The profile button stays on this page until that is replaced. The review cards below are placeholders, not customer testimonials.</p>
    <div id="review-list" class="grid md:grid-cols-3 gap-4">
      <article class="glass rounded-2xl p-6" aria-label="Placeholder for a Google review">
        <p class="text-xs font-semibold uppercase tracking-wide text-amber-200">Placeholder — not a customer review</p>
        <p class="text-gray-200 mt-3">Replace this card with a real Google review in assets/site-config.js.</p>
        <p class="text-sm text-gray-400 mt-4">Reviewer: PLACEHOLDER</p>
      </article>
      <article class="glass rounded-2xl p-6" aria-label="Placeholder for a Google review">
        <p class="text-xs font-semibold uppercase tracking-wide text-amber-200">Placeholder — not a customer review</p>
        <p class="text-gray-200 mt-3">Replace this card with a real Google review in assets/site-config.js.</p>
        <p class="text-sm text-gray-400 mt-4">Reviewer: PLACEHOLDER</p>
      </article>
      <article class="glass rounded-2xl p-6" aria-label="Placeholder for a Google review">
        <p class="text-xs font-semibold uppercase tracking-wide text-amber-200">Placeholder — not a customer review</p>
        <p class="text-gray-200 mt-3">Replace this card with a real Google review in assets/site-config.js.</p>
        <p class="text-sm text-gray-400 mt-4">Reviewer: PLACEHOLDER</p>
      </article>
    </div>
  </div>
</section>'''
