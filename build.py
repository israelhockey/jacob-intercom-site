"""Static site generator for jacobintercom.com.

  python3 build.py            -> out/site     (production: full documents, root-relative URLs)
                                 out/preview  (same pages with relative links, for a hosted preview)
"""
import html, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import PAGES  # noqa: E402

BASE = "https://jacobintercom.com"
# Path the site is served from. "/" on jacobintercom.com; "/jacob-intercom-site/" on GitHub Pages before the domain is attached.
SITE_BASE = os.environ.get("SITE_BASE", "/")
# Where the built site is actually served; link previews need full URLs on that host.
import hashlib
# Changes whenever the stylesheet or script changes, so browsers never keep an old copy.
ASSET_V = hashlib.md5(b"".join(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", f), "rb").read()
                               for f in ("site.css", "site.js"))).hexdigest()[:8]
PUBLIC_URL = os.environ.get("PUBLIC_URL", BASE).rstrip("/")
PHONE, PHONE_TEL = "718-252-2730", "+17182522730"
PHONE2, PHONE2_TEL = "212-837-2147", "+12128372147"
GTM_ID = "GTM-M2T83X8J"  # his existing Tag Manager container, carried over from the old site
FONTS = "https://fonts.googleapis.com/css2?family=Anton&family=Roboto:wght@400;500;700&display=swap"
NAV = [("intercom-repair/", "Repair"), ("intercom-maintenance-contract/", "Service agreements"),
       ("intercom-replacement/", "Upgrades"), ("lee-dan-intercom-systems/", "Lee-Dan"),
       ("projects/", "Projects"), ("about/", "About"), ("contact/", "Contact")]
BUILT = {p["path"] for p in PAGES}
SHOTS = {
    1: "Pre-war apartment building entrance with a stainless steel intercom panel beside the doors",
    2: "Hand pressing a button on a brass apartment buzzer panel",
    3: "Pre-war apartment lobby with brass mailboxes and an intercom panel",
    4: "Gloved hands testing the wiring inside an open intercom entry panel",
    5: "Video intercom door station with a camera and keypad beside a glass entrance",
    6: "Resident answering an intercom handset beside an apartment door",
    7: "Smartphone showing a video call from a building entrance",
    8: "Office building entrance with a video intercom and a card reader",
    9: "Key fob held to an access control reader",
    10: "Row of Manhattan walk-up buildings with an intercom at the entrance",
    11: "Pre-war Queens apartment building with a green entrance canopy",
    12: "Art deco apartment building entrance in the Bronx with an intercom panel",
    13: "Two-family brick house on Staten Island with doorbells and an intercom",
    14: "Dome security camera above an apartment building entrance",
    15: "Electric door strike in a metal door frame",
    16: "Intercom technician's tool bag, cable and meter on a lobby floor",
    17: "Building keys, a checklist and a floor plan on a desk",
    18: "Apartment building entrance at night with an intercom panel",
    19: "House front door with a video doorbell intercom",
    20: "Old beige apartment intercom station with three buttons",
    21: "Delivery packages stacked in an apartment building vestibule beside the intercom panel",
    22: "Meeting table with plans and papers in a pre-war building's community room",
    23: "Blank repair estimate on a clipboard beside an intercom handset station and cable",
    24: "Old brass buzzer panel removed beside a new stainless steel video intercom panel",
    25: "Lee-Dan apartment intercom station with Talk, Listen and Door buttons",
}
PRODUCT_SHOTS = {25}
PAGE_SHOT = {
    "intercom-repair/": 2, "intercom-repair/door-buzzer/": 6, "intercom-repair/door-release/": 15,
    "intercom-repair/no-audio/": 20, "intercom-repair/video/": 5, "intercom-repair/entry-panel/": 4,
    "intercom-repair/not-working/": 16, "intercom-repair/emergency/": 18, "contact/": 3,
    "intercom-installation/": 3, "intercom-installation/video/": 5, "intercom-installation/wireless/": 7,
    "intercom-installation/ip-smartphone/": 7, "intercom-installation/telephone-entry/": 8,
    "intercom-installation/audio/": 20, "intercom-replacement/": 24, "pricing/": 16,
    "property-managers/": 22, "superintendents/": 16, "vendor-onboarding/": 17, "projects/": 3, "intercom-maintenance-contract/": 17,
    "apartment-building-intercom/": 10, "co-op-condo-intercom/": 3, "commercial-intercom/": 8,
    "intercom-installation-brooklyn/": 1, "intercom-installation-manhattan/": 10, "intercom-installation-queens/": 11,
    "intercom-installation-bronx/": 12,
    "lee-dan-intercom-systems/": 25, "lee-dan-intercom-systems/repair/": 25, "lee-dan-intercom-systems/ir-203/": 25,
    "lee-dan-intercom-systems/ir-204/": 25, "lee-dan-intercom-systems/ir-205/": 25, "lee-dan-intercom-systems/parts/": 25, "intercom-installation-staten-island/": 13,
    "access-control/": 9, "access-control/key-fob/": 9, "access-control/electric-strikes-maglocks/": 15,
    "security-cameras/": 14, "security-cameras/apartment-buildings/": 14,
}


def shot_file(n):
    return f"img/shot-{n:02d}.webp"
TITLES = {p["path"]: p.get("nav", p["h1"]) for p in PAGES}


class Ctx:
    def __init__(self, page, mode):
        self.page, self.mode = page, mode
        self.depth = page["path"].count("/")

    def url(self, path):
        if self.mode == "site":
            return SITE_BASE + path
        return "../" * self.depth + path + "index.html"

    def asset(self, name):
        return (SITE_BASE + "assets/" if self.mode == "site" else "../" * self.depth + "assets/") + name

    def img(self, n, eager=False):
        load = 'fetchpriority="high"' if eager else 'loading="lazy"'
        if n in PRODUCT_SHOTS:
            return (f'<img class="pic pic-product" src="{self.asset(shot_file(n))}" alt="{SHOTS[n]}" '
                    f'width="370" height="370" {load} decoding="async">')
        return (f'<img class="pic" src="{self.asset(shot_file(n))}" alt="{SHOTS[n]}" '
                f'width="1600" height="900" {load} decoding="async">')

    def link(self, path, text, cls=""):
        c = f' class="{cls}"' if cls else ""
        if path in BUILT:
            cur = ' aria-current="page"' if path == self.page["path"] else ""
            return f'<a href="{self.url(path)}"{c}{cur}>{text}</a>'
        return f'<span class="soon">{text}</span>'

    def expand(self, s):
        """[[path|text]] -> link when the page is built, plain text otherwise. {{tel}} etc. -> contact links."""
        s = re.sub(r"\[\[([^|\]]*)\|([^\]]+)\]\]", lambda m: self.link(m.group(1), m.group(2)), s)
        # [CAPITALISED PLACEHOLDER] -> highlighted, so nothing unconfirmed can pass for a real figure
        s = re.sub(r"\[([A-Z][A-Z0-9 ',:/.-]{2,})\]", r'<mark class="todo">[\1]</mark>', s)
        s = re.sub(r"\{\{u:([^}]*)\}\}", lambda m: self.url(m.group(1)), s)
        s = re.sub(r"\{\{a:([^}]*)\}\}", lambda m: self.asset(m.group(1)), s)
        s = re.sub(r"\{\{img:(\d+)\}\}", lambda m: self.img(int(m.group(1))), s)
        return (s.replace("{{tel}}", f'<a href="tel:{PHONE_TEL}">{PHONE}</a>')
                 .replace("{{tel2}}", f'<a href="tel:{PHONE2_TEL}">{PHONE2}</a>')
                 .replace("{{home}}", self.url("")))


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


# Fill in each profile URL when confirmed. Filled ones become footer links and schema "sameAs".
PROFILES = [
    ("Google", "https://maps.google.com/?cid=12939931405333589826"),
    ("Yelp", "https://www.yelp.com/biz/jacob-intercom-brooklyn-5"),
    ("BBB", "https://www.bbb.org/us/ny/brooklyn/profile/intercom-systems/jacob-intercom-llc-0121-144932"),
    ("Facebook", "https://www.facebook.com/jacobintercomnyc/"),
    ("Instagram", "https://www.instagram.com/jacob.intercom/"),
    ("LinkedIn", "https://www.linkedin.com/company/jacobintercom/"),
]
EXTRA_SAMEAS = ["https://x.com/jacobintercomNY", "https://www.pinterest.com/JacobIntercom/"]
GOOGLE_REVIEW = "https://search.google.com/local/writereview?placeid=ChIJF42LFM5EwokRQm_U8A3fk7M"

# Old WordPress URLs -> new pages (301). Borough, Lee-Dan and product URLs are unchanged.
REDIRECTS = {
    "/brownstone-intercom/": "/apartment-building-intercom/",
    "/home-intercom/": "/apartment-building-intercom/",
    "/guides/renters-broken-buzzer/": "/guides/tenant-intercom-complaints/",
    "/about-us/": "/about/",
    "/access-controls/": "/access-control/",
    "/cctv/": "/security-cameras/",
    "/intercoms/": "/intercom-installation/",
    "/contact-us/": "/contact/",
    "/blog/": "/guides/",
    "/blog/emergency-intercom-repair-services-in-new-york-a-full-guide/": "/intercom-repair/emergency/",
    "/blog/how-many-security-cameras-does-a-house-really-need/": "/security-cameras/",
    "/blog/how-to-choose-the-right-door-entry-system-for-your-nyc-property/": "/guides/best-intercom-systems-nyc-buildings/",
    "/blog/how-to-choose-the-right-surveillance-technology-for-a-home/": "/security-cameras/",
    "/blog/how-to-integrate-alarm-systems-with-electronic-door-access/": "/access-control/",
    "/blog/intercom-installation-articles/": "/intercom-installation/",
    "/blog/intercom-repair-articles/": "/intercom-repair/",
    "/blog/intercom-upgrade-articles/": "/guides/upgrade-buzzer-to-video/",
    "/blog/ip-based-intercom-systems-how-they-work-and-why-you-need-one/": "/intercom-installation/ip-smartphone/",
    "/blog/security-benefits-articles/": "/intercom-installation/video/",
    "/blog/traditional-intercom-vs-smart-intercom-system-whats-right-for-you/": "/guides/wired-vs-wireless-intercom/",
}
# WordPress leftovers that should not 404
WILDCARDS = {"/category/*": "/guides/", "/author/*": "/about/", "/tag/*": "/guides/", "/feed/*": "/", "/wp-content/*": "/", "/blog/*": "/guides/"}

BUSINESS = {
    "@context": "https://schema.org", "@type": "LocalBusiness", "@id": BASE + "/#business",
    "name": "Jacob Intercom", "url": BASE + "/", "telephone": "+1-718-252-2730",
    "email": "jacobintercom@gmail.com",
    "address": {"@type": "PostalAddress", "streetAddress": "209 Avenue F", "addressLocality": "Brooklyn",
                "addressRegion": "NY", "postalCode": "11218", "addressCountry": "US"},
    "geo": {"@type": "GeoCoordinates", "latitude": 40.6335388, "longitude": -73.976101},
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"],
         "opens": "09:00", "closes": "17:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "08:00", "closes": "16:00"}],
    "areaServed": ["Brooklyn", "Manhattan", "Queens", "The Bronx", "Staten Island"],
    "aggregateRating": {"@type": "AggregateRating", "ratingValue": 4.7, "reviewCount": 23},
}
if any(u for _, u in PROFILES):
    BUSINESS["sameAs"] = [u for _, u in PROFILES if u] + EXTRA_SAMEAS


def crumbs(ctx):
    parts = [p for p in ctx.page["path"].split("/") if p]
    trail, acc = [("", "Home")], ""
    for part in parts:
        acc += part + "/"
        trail.append((acc, TITLES.get(acc, part.replace("-", " ").title())))
    return trail


def head(ctx):
    p = ctx.page
    title = "Jacob Intercom Preview" if (ctx.mode == "preview" and p["path"] == "") else p["title"]
    out = [f"<title>{html.escape(title)}</title>",
           f'<meta name="description" content="{html.escape(p["desc"], quote=True)}">']
    shot = p.get("shot") or PAGE_SHOT.get(p["path"], 1)
    if ctx.mode == "site":
        out.append(f'<link rel="canonical" href="{BASE}/{p["path"]}">')
        t, d = html.escape(p["title"], quote=True), html.escape(p["desc"], quote=True)
        share = f"{PUBLIC_URL}/assets/share.jpg"
        out += [f'<meta property="og:type" content="website">',
                f'<meta property="og:site_name" content="Jacob Intercom">',
                f'<meta property="og:url" content="{PUBLIC_URL}/{p["path"]}">',
                f'<meta property="og:title" content="{t}">',
                f'<meta property="og:description" content="{d}">',
                f'<meta property="og:image" content="{share}">',
                '<meta property="og:image:width" content="1200">',
                '<meta property="og:image:height" content="630">',
                '<meta property="og:image:alt" content="Jacob Intercom: New York intercom repair and installation for 35 years">',
                '<meta name="twitter:card" content="summary_large_image">',
                f'<meta name="twitter:image" content="{share}">']
    else:
        out.append('<meta name="robots" content="noindex">')
        out.append('<meta name="claude:viewport-fit-sides" content="cover">')
    out += [f'<link rel="stylesheet" href="{FONTS}">', f'<link rel="stylesheet" href="{ctx.asset("site.css")}?v={ASSET_V}">']
    out.append(f'<link rel="icon" href="{ctx.asset("favicon-32.png")}" sizes="32x32" type="image/png">')
    out.append(f'<link rel="apple-touch-icon" href="{ctx.asset("apple-touch-icon.png")}">')
    out.append('<meta name="theme-color" content="#3698C2">')
    if p.get("noindex") and ctx.mode == "site":
        out.append('<meta name="robots" content="noindex">')
    if ctx.mode == "site" and GTM_ID:
        out.append("<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});"
                   "var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;"
                   f"j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM_ID}');</script>")
    if p["path"] in ("", "contact/"):
        out.append(jsonld(BUSINESS))
    if p["path"]:
        out.append(jsonld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": f"{BASE}/{path}"}
            for i, (path, name) in enumerate(crumbs(ctx))]}))
    if p.get("faqs"):
        out.append(jsonld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
            for q, a in p["faqs"]]}))
    return "\n".join(out)


def header(ctx):
    nav = "".join(ctx.link(path, text) for path, text in NAV)
    return f"""<header class="site-header"><div class="wrap">
<a class="logo" href="{ctx.url('')}"><img src="{ctx.asset('logo-white.png')}" alt="Jacob Intercom, Intercom Specialist" width="400" height="86"></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav"><span class="menu-bars" aria-hidden="true"></span>Menu</button>
<nav class="nav" id="site-nav" aria-label="Main">{nav}</nav>
<div class="hdr-phones"><a href="tel:{PHONE_TEL}">{PHONE}</a><a href="tel:+12128372147">212-837-2147</a></div>
</div></header>"""

def reviews():
    quotes = [
        "Great service, quick response, very professional with reasonable prices. It took me a while to find a company that doesn't request a lot of information just to provide an estimate and an appointment.",
        "Jacob Intercom helped us modernize our building with a wireless intercom. Residents appreciate the convenience, and we appreciate the increased security.",
        "They arrived on time and explained every step of the installation. Their technician completed the job exactly as promised."]
    cards = "".join(f"<blockquote>&ldquo;{q}&rdquo;<footer>Google review</footer></blockquote>" for q in quotes)
    return f"""<section class="section band-tint" aria-label="Reviews"><div class="wrap">
<h2>4.7 stars from 23 Google reviews</h2>
<div class="reviews">{cards}</div>
</div></section>"""


def quote(ctx):
    return f"""<section class="quote band-green" id="quote"><div class="wrap">
<div class="col stack">
<h2>Tell us about your buildings.</h2>
<p style="font-size:1.15rem;max-width:30em">One building with a dead riser or forty buildings to bring under one vendor: send the basics and we'll come back with next steps, usually the same business day.</p>
<p class="tel">{ctx.expand('{{tel}}')}</p>
<p class="tel">{ctx.expand('{{tel2}}')}</p>
<p><a href="mailto:jacobintercom@gmail.com" style="color:#fff">jacobintercom@gmail.com</a></p>
</div>
<form class="card" data-quote novalidate>
<div class="form-2"><label for="q-name">Name<input id="q-name" name="name" type="text" autocomplete="name"></label>
<label for="q-company">Company<input id="q-company" name="company" type="text" autocomplete="organization"></label></div>
<div class="form-2"><label for="q-role">Your role<select id="q-role" name="role"><option>Property manager</option><option>Building manager or super</option><option>Management company owner</option><option>Co-op or condo board</option><option>Building owner</option><option>Other</option></select></label>
<label for="q-need">What do you need?<select id="q-need" name="need"><option>A repair</option><option>A service agreement</option><option>A system replacement or upgrade</option><option>A survey of several buildings</option><option>Vendor documents (COI, W-9)</option></select></label></div>
<div class="form-2"><label for="q-phone">Phone<input id="q-phone" name="phone" type="tel" autocomplete="tel"></label>
<label for="q-email">Email<input id="q-email" name="email" type="email" autocomplete="email"></label></div>
<div class="form-2"><label for="q-buildings">Number of buildings<input id="q-buildings" name="buildings" type="number" min="1" inputmode="numeric"></label>
<label for="q-units">Total apartments<input id="q-units" name="units" type="number" min="1" inputmode="numeric"></label></div>
<label for="q-notes">Addresses and what's going on<textarea id="q-notes" name="notes" rows="3"></textarea></label>
<button class="btn btn-dark" type="submit">Send to Jacob Intercom</button>
<p class="form-msg" role="status" hidden></p>
</form>
</div></section>"""


def home_quote(ctx):
    """Short enquiry block for the home page: four fields, phones beside it."""
    return f"""<section class="home-contact" id="quote"><div class="wrap">
<div>
<h2>Tell us about your buildings</h2>
<p class="home-sub">One building or forty. We'll come back the same business day.</p>
<p class="home-big">{ctx.expand('{{tel}}')}</p>
<p class="home-big">{ctx.expand('{{tel2}}')}</p>
<p class="home-addr">209 Avenue F, Brooklyn, NY 11218<br>Monday to Thursday 9 to 5, Friday 8 to 4</p>
</div>
<form class="card" data-quote novalidate>
<div class="form-2"><label for="h-name">Name<input id="h-name" name="name" type="text" autocomplete="name"></label>
<label for="h-company">Company<input id="h-company" name="company" type="text" autocomplete="organization"></label></div>
<div class="form-2"><label for="h-phone">Phone<input id="h-phone" name="phone" type="tel" autocomplete="tel"></label>
<label for="h-buildings">Number of buildings<input id="h-buildings" name="buildings" type="number" min="1" inputmode="numeric"></label></div>
<button class="btn btn-brass" type="submit">Request a building survey</button>
<p class="form-msg" role="status" hidden></p>
</form>
</div></section>"""


def footer(ctx):
    return f"""<footer class="site-footer"><div class="wrap">
<div><a class="logo" href="{ctx.url('')}"><img src="{ctx.asset('logo-white.png')}" alt="Jacob Intercom" width="400" height="86" loading="lazy"></a><p>209 Avenue F, Brooklyn, NY 11218</p><p>Licence <span class="todo">[LICENCE NO.]</span>. Fully insured.</p><p>35 years in business.</p></div>
<div><strong>Call or email</strong><p>{ctx.expand('{{tel}}')}</p><p>{ctx.expand('{{tel2}}')}</p><p><a href="mailto:jacobintercom@gmail.com">jacobintercom@gmail.com</a></p></div>
<div><strong>Services</strong><p>{ctx.link('intercom-repair/', 'Intercom repair')}</p><p>{ctx.link('intercom-maintenance-contract/', 'Service agreements')}</p><p>{ctx.link('intercom-replacement/', 'Building upgrades')}</p><p>{ctx.link('property-managers/', 'Portfolio programs')}</p><p>{ctx.link('lee-dan-intercom-systems/', 'Lee-Dan systems')}</p></div>
<div><strong>Service areas</strong><p>{ctx.link('service-areas/', 'All service areas')}</p><p>{ctx.link('intercom-installation-brooklyn/', 'Brooklyn')}, {ctx.link('intercom-installation-manhattan/', 'Manhattan')}, {ctx.link('intercom-installation-queens/', 'Queens')}</p><p>{ctx.link('intercom-installation-bronx/', 'The Bronx')}, {ctx.link('intercom-installation-staten-island/', 'Staten Island')}</p></div>
<div><strong>Find us on</strong>{"".join(f'<p><a href="{u}" rel="noopener">{n}</a></p>' if u else f'<p>{n} <mark class="todo">[{n.upper()} URL]</mark></p>' for n, u in PROFILES)}</div>
<div><strong>Company</strong><p>{ctx.link('about/', 'About')}</p><p>{ctx.link('projects/', 'Projects')}</p><p>{ctx.link('vendor-onboarding/', 'Vendor onboarding')}</p><p>{ctx.link('superintendents/', 'For superintendents')}</p><p>{ctx.link('guides/', 'Guides')}</p><p>{ctx.link('reviews/', 'Reviews')}</p><p>{ctx.link('privacy/', 'Privacy')}</p></div>
</div></footer>
<div class="callbar"><a class="btn btn-brass" href="tel:{PHONE_TEL}">Call {PHONE}</a><a class="btn btn-ghost" href="#quote">Request a survey</a></div>
<script src="{ctx.asset('site.js')}?v={ASSET_V}"></script>"""


def article(ctx):
    p = ctx.page
    trail = crumbs(ctx)
    bc = " <span aria-hidden=\"true\">/</span> ".join(
        f'<a href="{ctx.url(path)}">{name}</a>' if i < len(trail) - 1 else f"<span>{name}</span>"
        for i, (path, name) in enumerate(trail))
    facts = "".join(f"<li>{ctx.expand(f)}</li>" for f in p.get("facts", []))
    faqs = ""
    if p.get("faqs"):
        items = "".join(f"<details><summary>{q}</summary><p>{ctx.expand(a)}</p></details>" for q, a in p["faqs"])
        faqs = f'<h2>Common questions</h2><div class="faq">{items}</div>'
    aside = p.get("aside") or {}
    n = p.get("shot") or PAGE_SHOT.get(p["path"])
    fig = f'<figure class="figure">{ctx.img(n, eager=True)}</figure>' if n else ""
    related = "".join(f"<li>{ctx.link(path, text)}</li>" for path, text in p.get("related", []))
    related = f'<p><strong>Related</strong></p><ul class="linklist">{related}</ul>' if related else ""
    return f"""<section class="hero"><div class="wrap stack" style="gap:20px">
<nav class="crumbs" aria-label="Breadcrumb">{bc}</nav>
<h1>{p['h1']}</h1>
<p class="lead">{ctx.expand(p['lead'])}</p>
<ul class="facts">{facts}</ul>
<div class="btn-row"><a class="btn btn-brass" href="tel:{PHONE_TEL}">Call {PHONE}</a><a class="btn btn-ghost" href="#quote">Request a building survey</a></div>
</div></section>
<div class="article"><div class="wrap">
<article class="prose{' prose-wide' if p.get('wide') else ''}">{fig}{ctx.expand(p['body'])}{faqs}</article>
{'' if p.get('wide') else '<!--aside-->'}<aside class="aside" aria-label="Get help"{' hidden' if p.get('wide') else ''}>
<p class="big">{aside.get('head', 'Talk to someone who fixes these')}</p>
<p>{ctx.expand(aside.get('text', 'Most repairs run $100 to $300. We find the fault and give you the price before any work starts.'))}</p>
<a class="btn btn-dark" href="tel:{PHONE_TEL}">Call {PHONE}</a>
<a class="btn btn-outline" href="#quote">Send us the details</a>
<p style="font-size:.92rem;color:var(--muted)">Monday to Thursday 9 to 5, Friday 8 to 4.</p>
{related}
</aside>
</div></div>"""


def render(page, mode):
    ctx = Ctx(page, mode)
    main = ctx.expand(page["html"]) if page.get("html") else article(ctx)
    form = home_quote(ctx) if page.get("home_form") else quote(ctx)
    body = header(ctx) + "\n<main>" + main + ("" if page.get("no_reviews") else reviews()) + form + "</main>\n" + footer(ctx)
    if mode == "preview" and page["path"] == "":
        return head(ctx) + "\n" + body  # the preview host wraps its entry page in its own document
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + head(ctx) + "\n</head>\n<body>\n" + body + "\n</body>\n</html>\n")


def main():
    out = os.path.join(HERE, "out")
    shutil.rmtree(out, ignore_errors=True)
    for mode in ("site", "preview"):
        root = os.path.join(out, mode)
        shutil.copytree(os.path.join(HERE, "assets"), os.path.join(root, "assets"))
        for page in PAGES:
            d = os.path.join(root, page["path"])
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
                f.write(render(page, mode))
    if True:  # sitemap and robots for production
        root = os.path.join(out, "site")
        urls = "".join(f"<url><loc>{BASE}/{p['path']}</loc></url>" for p in PAGES if not p.get("noindex"))
        shutil.copy(os.path.join(root, "404", "index.html"), os.path.join(root, "404.html"))
        open(os.path.join(root, "sitemap.xml"), "w").write(
            f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
        lines = []
        for src, dst in REDIRECTS.items():
            lines += [f"{src} {dst} 301", f"{src.rstrip('/')} {dst} 301"]
        lines += [f"{src} {dst} 301" for src, dst in WILDCARDS.items()]
        open(os.path.join(root, "_redirects"), "w").write("\n".join(lines) + "\n")
        vr = []
        for src, dst in REDIRECTS.items():
            vr.append({"source": src.rstrip("/") + "{/}?", "destination": dst, "permanent": True})
        for src, dst in WILDCARDS.items():
            vr.append({"source": src.replace("*", ":path*"), "destination": dst, "permanent": True})
        json.dump({"trailingSlash": True, "redirects": vr}, open(os.path.join(root, "vercel.json"), "w"), indent=2)
        open(os.path.join(root, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    words = {p["path"] or "/": len(re.sub("<[^>]+>", " ", p.get("html") or p["body"]).split()) for p in PAGES}
    print(len(PAGES), "pages"); [print(f"  {w:5d} words  {k}") for k, w in words.items()]


if __name__ == "__main__":
    main()


def build_forwarding_pages(root):
    """One small page at each old WordPress address that forwards to its new page."""
    for src, dst in REDIRECTS.items():
        d = os.path.join(root, src.strip("/"))
        if os.path.exists(os.path.join(d, "index.html")):
            continue
        os.makedirs(d, exist_ok=True)
        target = SITE_BASE + dst.lstrip("/")
        open(os.path.join(d, "index.html"), "w").write(
            '<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<title>Moved</title><link rel="canonical" href="{BASE}{dst}">'
            f'<meta http-equiv="refresh" content="0; url={target}"><meta name="robots" content="noindex">'
            f'</head><body><p>This page has moved to <a href="{target}">{BASE}{dst}</a>.</p></body></html>')


def build_staging():
    """A copy of the production site for client review on a temporary host: hidden from search engines, no analytics."""
    import glob
    src, dst = os.path.join(HERE, "out", "site"), os.path.join(HERE, "out", "staging")
    shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(src, dst)
    gtm = re.compile(r"<script>\(function\(w,d,s,l,i\).*?</script>", re.S)
    for f in glob.glob(os.path.join(dst, "**", "*.html"), recursive=True):
        t = open(f, encoding="utf-8").read()
        t = gtm.sub("", t).replace("<head>\n", '<head>\n<meta name="robots" content="noindex, nofollow">\n', 1)
        open(f, "w", encoding="utf-8").write(t)
    open(os.path.join(dst, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
    os.remove(os.path.join(dst, "sitemap.xml"))


if __name__ == "__main__":
    build_forwarding_pages(os.path.join(HERE, "out", "site"))
    build_staging()
