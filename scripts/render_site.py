#!/usr/bin/env python3
"""Write the public marketing pages. Output is committed static HTML."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chrome import (  # noqa: E402
    ADDRESS, EMAIL, PHONE_DISPLAY, PHONE_TEL, LASTMOD, RATING_HTML, REVIEW_URL,
    AREAS, INDUSTRIES, article_block, breadcrumb, business_block,
    contact_form, crumbs, faq_block, faq_html, jsonld, org_block,
    packages, page, picture, reviews_section, service_block, website_block,
    write_page,
)

URLS = []


def emit(rel, content):
    URLS.append(write_page(rel, content))


def hero(kicker, h1, lede, primary_href, primary_label, secondary_href, secondary_label):
    return f'''
<main id="main">
<section class="relative pt-28 pb-16 overflow-hidden">
  <div class="hero-bg"></div>
  <div class="grid-overlay"></div>
  <div class="orb orb-1"></div>
  <div class="orb orb-2"></div>
  <div class="relative z-10 max-w-5xl mx-auto px-4 sm:px-6">
    {kicker}
    <h1 class="font-display text-4xl sm:text-5xl lg:text-6xl font-bold text-white leading-tight glow-text mb-6">{h1}</h1>
    <div class="text-lg text-gray-300 max-w-3xl leading-relaxed space-y-4">{lede}</div>
    <div class="flex flex-col sm:flex-row gap-3 mt-8">
      <a href="{primary_href}" class="px-6 py-3 bg-accent-strong text-white font-semibold rounded-full text-center hover:bg-blue-800">{primary_label}</a>
      <a href="{secondary_href}" class="px-6 py-3 border border-white/30 text-white font-semibold rounded-full text-center hover:bg-white/5">{secondary_label}</a>
    </div>
  </div>
</section>'''


def prose(paragraphs):
    return "".join(f'<p class="text-gray-300 leading-relaxed mb-4">{p}</p>' for p in paragraphs)


def article(blocks):
    parts = []
    for title, paragraphs in blocks:
        parts.append(
            f'<h2 class="font-display text-2xl text-white font-bold mt-10 mb-3">{title}</h2>{prose(paragraphs)}'
        )
    return f'<article class="max-w-3xl mx-auto px-4 sm:px-6 pb-4">{"".join(parts)}</article>'


def local_page(path, title, description, h1, lede, blocks, faqs, service_name, city, cta):
    canonical = "https://crrelabs.com" + path
    body = hero(
        crumbs([("Home", "/"), (h1.split(",")[0], path)]),
        h1,
        lede,
        "#packages",
        "See packages",
        f"tel:{PHONE_TEL}",
        f"Call {PHONE_DISPLAY}",
    )
    body += article(blocks)
    body += packages("Clear packages, local prices")
    body += faq_html(faqs)
    body += contact_form(path.strip("/"), cta)
    body += "</main>"
    schemas = jsonld(
        service_block(service_name, canonical, city, description),
        faq_block(faqs),
        breadcrumb([("Home", "https://crrelabs.com/"), (service_name, canonical)]),
    )
    emit(path.strip("/") + "/index.html", page(title, description, canonical, path, body, schemas))


def home():
    faqs = [
        (
            "How much does a small-business website cost?",
            "Starter is $99 to set up and $15 a month for one page, a contact form, and hosting with the domain and SSL. Business is $199 and $29 a month for up to five pages, click-to-call, basic on-page SEO, and help aligning your Google listing. Pro is $349 and $49 a month for up to ten pages, a booking or payment embed, an analytics report, and one or two content updates a month. Every plan is month to month.",
        ),
        (
            "How do your prices compare locally?",
            "Many local quotes start around $300 to $500. Our small-business sites start at $99 to set up and $15 a month, with hosting included. A larger custom project, such as a full leasing site, is priced on its own.",
        ),
        (
            "Do you only work in Pinecrest?",
            "The studio is at 12394 SW 82nd Ave in Pinecrest. We also build for businesses in Kendall, South Miami, Coral Gables, Palmetto Bay, and across Miami. Call (786) 733-6744.",
        ),
        (
            "Is a building website the same price as Starter?",
            "Starter, Business, and Pro cover a small-business site of one, five, or ten pages. A full leasing site for a Miami building is custom work. Tell us about the property and we'll quote it.",
        ),
        (
            "Can you help beyond the website?",
            "Yes. We also build assistants such as Iris for property managers, connect the tools you already run, and produce 3D models and prints. Mention it on the form.",
        ),
    ]
    body = hero(
        f'<p class="text-sm text-accent font-semibold mb-4">Pinecrest web design studio · {RATING_HTML}</p>',
        "Affordable website design for small businesses in Pinecrest and Miami",
        f"""<p>CRRE Labs builds straightforward websites for local businesses, from a studio at 12394 SW 82nd Ave in Pinecrest. Call <a class="text-white font-semibold underline" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>, send a note, or start a package today.</p>
        <p>Starter is $99 to set up and $15 a month. Business is $199 and $29 a month. Pro is $349 and $49 a month. The domain, SSL, and hosting are included. Many local quotes begin around $300 to $500.</p>""",
        "#packages",
        "See packages and prices",
        f"tel:{PHONE_TEL}",
        f"Call {PHONE_DISPLAY}",
    )
    body += f'''
<section class="relative z-10 -mt-4 pb-8">
  <div class="max-w-5xl mx-auto px-4 sm:px-6">
    <div class="glass rounded-2xl p-5 flex flex-col sm:flex-row sm:items-center gap-4 justify-between">
      <p class="text-gray-200"><span class="text-white font-semibold">{RATING_HTML}</span></p>
      <a data-review-link="reviews" href="{REVIEW_URL}" target="_blank" rel="noopener noreferrer" class="inline-flex justify-center px-4 py-2 rounded-full border border-white/30 text-white text-sm font-semibold">See our Google reviews</a>
      <a data-review-link="leave" href="{REVIEW_URL}" target="_blank" rel="noopener noreferrer" class="inline-flex justify-center px-4 py-2 rounded-full bg-accent-strong text-white text-sm font-semibold">Leave us a Google review</a>
    </div>
  </div>
</section>
{packages("Packages, with the prices")}
<section class="pb-8">
  <div class="max-w-3xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-3xl font-bold text-white mb-4">A clear price, close to home</h2>
    <p class="text-gray-300 leading-relaxed mb-4">Many local website quotes start around $300 to $500 before hosting. A CRRE Labs small-business site starts at $99 to set up and $15 a month, with the domain, SSL, and hosting included, and you can cancel any month.</p>
    <p class="text-gray-300 leading-relaxed">Starter, Business, and Pro are for a shop, office, or crew that needs a clear site and a phone call. A custom project, such as a full leasing site, is quoted on its own. If you pause and come back within 90 days, reactivation is $49, $99, or $175 depending on the plan. Details sit on the <a class="text-accent underline" href="/pricing/">pricing page</a>.</p>
  </div>
</section>
<section class="py-12">
  <div class="max-w-7xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-3xl font-bold text-white mb-3">Web design near you</h2>
    <p class="text-gray-300 max-w-3xl mb-6">The studio is in Pinecrest. We build for the neighborhoods around it, and the work looks different on each street.</p>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <a class="glass rounded-2xl p-5 block" href="/web-design-pinecrest/"><h3 class="text-white font-semibold mb-2">Pinecrest</h3><p class="text-sm text-gray-300">A village business site from the studio on SW 82nd Ave. Phone, hours, and a neighbor who can call you back.</p></a>
      <a class="glass rounded-2xl p-5 block" href="/web-design-kendall/"><h3 class="text-white font-semibold mb-2">Kendall</h3><p class="text-sm text-gray-300">Plaza shops along Kendall Drive and Dadeland, with the suite and the phone up front.</p></a>
      <a class="glass rounded-2xl p-5 block" href="/web-design-south-miami/"><h3 class="text-white font-semibold mb-2">South Miami</h3><p class="text-sm text-gray-300">Sunset Drive and US-1, where people park once and walk. Hours and the cross street do the selling.</p></a>
      <a class="glass rounded-2xl p-5 block" href="/web-design-coral-gables/"><h3 class="text-white font-semibold mb-2">Coral Gables</h3><p class="text-sm text-gray-300">Miracle Mile and the downtown grid. Calm sites for offices, salons, and restaurants.</p></a>
      <a class="glass rounded-2xl p-5 block" href="/web-design-palmetto-bay/"><h3 class="text-white font-semibold mb-2">Palmetto Bay</h3><p class="text-sm text-gray-300">Old Cutler and Franjo. Home services, dentists, and smaller restaurants that cover a few villages.</p></a>
      <a class="glass rounded-2xl p-5 block" href="/web-design-miami/"><h3 class="text-white font-semibold mb-2">Miami</h3><p class="text-sm text-gray-300">Small-business sites across the city, plus leasing sites for Miami apartment buildings.</p></a>
    </div>
  </div>
</section>
<section class="py-8">
  <div class="max-w-7xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-3xl font-bold text-white mb-6">Websites for the way you work</h2>
    <ul class="grid sm:grid-cols-2 gap-3 text-gray-200">
      <li><a class="underline text-accent" href="/websites-for-restaurants/">Restaurants</a> — hours, the menu, and a phone people can tap.</li>
      <li><a class="underline text-accent" href="/websites-for-contractors/">Contractors and home services</a> — the jobs you do and the neighborhoods you cover.</li>
      <li><a class="underline text-accent" href="/websites-for-salons-and-spas/">Salons and spas</a> — services, photos, and booking on the Pro plan.</li>
      <li><a class="underline text-accent" href="/websites-for-medical-and-dental/">Medical and dental offices</a> — a welcoming site for new patients.</li>
      <li><a class="underline text-accent" href="/websites-for-property-managers/">Property managers and real estate</a> — a clear way for owners and applicants to reach you.</li>
    </ul>
  </div>
</section>
<section id="work" class="py-12">
  <div class="max-w-7xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-3xl font-bold text-white mb-3">Recent work</h2>
    <p class="text-gray-300 max-w-3xl mb-6">A few sites you can open today. Each one gives visitors a simple next step: call, tour, or get in touch.</p>
    <div class="grid md:grid-cols-2 gap-4">
      <a class="glass rounded-2xl p-6 block" href="/work/miami-apartment-sites/"><h3 class="text-white font-semibold text-xl mb-2">Miami apartment communities</h3><p class="text-gray-300 text-sm">Leasing sites for Downtown 1st, Downtown 5th, 22 Biscayne Bay, Urban 22 Miami, 25 Biscayne Park, and Melody Tower.</p></a>
      <a class="glass rounded-2xl p-6 block" href="/work/rg-capital-partners/"><h3 class="text-white font-semibold text-xl mb-2">RG Capital Partners</h3><p class="text-gray-300 text-sm">A private-equity real estate firm working in Kansas City and Miami, with a clear path to the portfolio and the team.</p></a>
    </div>
    <p class="mt-4"><a class="text-accent underline" href="/portfolio/">See the portfolio</a> · <a class="text-accent underline" href="/work/">Read the stories</a></p>
  </div>
</section>
<section class="py-8">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 grid md:grid-cols-3 gap-4">
    <article class="glass rounded-2xl p-6"><h2 class="text-white font-semibold mb-2">1. Tell us about the business</h2><p class="text-sm text-gray-300">Call, send the form, or check out a package. Share what you do and which neighborhood you serve. Package questions usually get a reply within a day.</p></article>
    <article class="glass rounded-2xl p-6"><h2 class="text-white font-semibold mb-2">2. We put you online</h2><p class="text-sm text-gray-300">Starter is one page. Business is up to five. Pro is up to ten. Most package sites are ready in one to two weeks, with your phone and hours easy to find.</p></article>
    <article class="glass rounded-2xl p-6"><h2 class="text-white font-semibold mb-2">3. Stay as long as it helps</h2><p class="text-sm text-gray-300">Plans are month to month. Business includes one revision a month. Pro includes one or two content updates a month, so hours and specials can stay current.</p></article>
  </div>
</section>
{reviews_section()}
<section id="about" class="py-12">
  <div class="max-w-3xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-3xl font-bold text-white mb-4">A studio in Pinecrest</h2>
    <p class="text-gray-300 leading-relaxed mb-4">CRRE Labs LLC designs websites at {ADDRESS}. Call {PHONE_DISPLAY} or email {EMAIL}. Customers have left us {RATING_HTML}.</p>
    <p class="text-gray-300 leading-relaxed">If you searched for web design in Pinecrest, a small-business website in Miami, or an affordable site in Kendall, you are in the right place. Pick a package, or tell us what you need.</p>
  </div>
</section>
<section id="other-services" class="py-12">
  <div class="max-w-7xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-3xl font-bold text-white mb-3">When you need more than a website</h2>
    <p class="text-gray-300 max-w-3xl mb-6">The packages above are for your website. If you also want help with daily work, or a physical model, we can do that too.</p>
    <div class="grid md:grid-cols-3 gap-4">
      <article class="glass rounded-2xl p-6">
        <h3 class="text-white font-semibold mb-2">Iris for property managers</h3>
        <p class="text-sm text-gray-300 mb-3">Iris helps with rent follow-up, paperwork, and the small tasks that fill a property manager's day. It looks after 420+ homes for under $90 a month.</p>
        <a class="text-accent underline text-sm" href="/iris/">See Iris</a>
      </article>
      <article class="glass rounded-2xl p-6">
        <h3 class="text-white font-semibold mb-2">Tools that talk to each other</h3>
        <p class="text-sm text-gray-300">We connect Google Workspace, your CRM, and the other software you already pay for, so billing files and routine emails do not sit in a queue.</p>
      </article>
      <article class="glass rounded-2xl p-6">
        <h3 class="text-white font-semibold mb-2">Models and prints</h3>
        <p class="text-sm text-gray-300 mb-3">Prototypes, architectural models, and small-batch parts, made in-house. Ask for a print quote when you have a file or an idea.</p>
        <a class="text-accent underline text-sm" href="/3d-printing.html">3D printing</a>
      </article>
    </div>
  </div>
</section>
{faq_html(faqs)}
{contact_form("home", "Tell us what the business does, where it is, and which package fits. We reply by email.")}
</main>'''
    emit("index.html", page(
        "Affordable Website Design for Small Businesses | Pinecrest & Miami | CRRE Labs",
        "Pinecrest web design studio for small businesses. Websites from $99 setup and $15/month. Call (786) 733-6744. CRRE Labs, 12394 SW 82nd Ave.",
        "https://crrelabs.com/",
        "/",
        body,
        jsonld(business_block(), org_block(), website_block(), faq_block(faqs)),
    ))


def area_pages():
    pages = [
        dict(
            path="/web-design-pinecrest/",
            title="Web Design in Pinecrest, FL | CRRE Labs",
            description="Web design in Pinecrest from a studio at 12394 SW 82nd Ave. Sites from $99 setup and $15/month. Call (786) 733-6744.",
            h1="Web design in Pinecrest, FL",
            city="Pinecrest",
            service="Website design for small businesses in Pinecrest, Florida",
            lede="<p>Pinecrest customers often arrive with your name already in mind, from a neighbor or a school pickup line. Your website should make the phone, the hours, and the address just as easy to trust.</p><p>CRRE Labs is at 12394 SW 82nd Ave, in the village. Call (786) 733-6744 and you will reach the studio, not a call center.</p>",
            blocks=[
                ("Built for a residential village", [
                    "The businesses that serve Pinecrest sit along US-1, on the Kendall Drive edge, and in small offices people drive to: dentists, tutors, designers, restaurants, and home services that pull into a driveway.",
                    "Lead with the phone. If you have a shop, show the same address customers already use to find you. If you go to them, name Pinecrest and the nearby villages you truly cover, such as Palmetto Bay just to the south.",
                    "Bring photos of your office, your truck, or your food. We will design around what you have.",
                ]),
                ("Local, and easy to reach", [
                    "Call and you'll talk to the studio directly, not a call center. Most package sites are ready in one to two weeks, and you can cancel the monthly plan whenever it stops being useful.",
                ]),
            ],
            faqs=[
                ("Can I visit the studio?", "Yes. We are at 12394 SW 82nd Ave, Pinecrest, FL 33156. Call (786) 733-6744 before you come so someone is here."),
                ("What does a Pinecrest business site cost?", "Starter is $99 setup and $15 a month. Business is $199 and $29 a month. Pro is $349 and $49 a month. Many other local quotes start around $300 to $500."),
                ("How fast can we launch?", "Most package sites are ready in one to two weeks. A larger custom project takes a conversation first."),
                ("Will you promise the top Google spot?", "We write clear pages and, on Business and Pro, line the site up with your Google listing. Reviews, location, and the rest of the market still shape where you show up."),
            ],
        ),
        dict(
            path="/web-design-kendall/",
            title="Web Design in Kendall, FL | CRRE Labs",
            description="Affordable web design in Kendall for plaza shops, clinics, and crews. From $99 setup and $15/month. Call (786) 733-6744.",
            h1="Web design in Kendall, FL",
            city="Kendall",
            service="Website design for small businesses in Kendall, Florida",
            lede="<p>Kendall Drive and the Dadeland end of US-1 are lined with plazas. A customer comparing three salons or three dentists needs to see your suite, your hours, and your phone before they tap the neighbor.</p><p>Our studio is a short drive south, in Pinecrest, at 12394 SW 82nd Ave. The number is (786) 733-6744.</p>",
            blocks=[
                ("Made for plaza businesses", [
                    "Restaurants, salons, dental and medical offices, and home-service crews around Kendall Drive and Baptist Hospital all fight for the same glance. Put the cross street and the suite in the first screen, then the work you actually do.",
                    "If you cover Kendale Lakes, The Hammocks, or Dadeland, say so. Leave off the corners you do not drive to. Customers can tell.",
                    "If your customers call in English and Spanish, publish only the languages you answer the phone in. We will place the words you give us.",
                ]),
                ("Pick the size that matches the shop", [
                    "Starter, $99 to set up and $15 a month, holds hours, services, and a form on one page. Business, $199 and $29 a month, opens that into five pages with click-to-call and a Google listing that matches the site. Pro, $349 and $49 a month, adds booking and a couple of content updates a month when the menu or the book changes.",
                ]),
            ],
            faqs=[
                ("Do I have to be in Pinecrest?", "No. Kendall businesses are a regular part of our work. The studio is in Pinecrest, a few minutes south of Kendall Drive."),
                ("Should the site list every Kendall neighborhood?", "List the ones you serve. A long list you cannot cover makes the next call harder, not easier."),
                ("Is the Kendall price different?", "Same three plans: $99 + $15/mo, $199 + $29/mo, and $349 + $49/mo. Hosting is included."),
                ("Can the site be in Spanish?", "If you have the Spanish wording, and you can answer those calls, we will put it on the site within your page count."),
            ],
        ),
        dict(
            path="/web-design-south-miami/",
            title="Web Design in South Miami, FL | CRRE Labs",
            description="Web design in South Miami for Sunset Drive shops, restaurants, and offices. From $99 setup and $15/month. Call (786) 733-6744.",
            h1="Web design in South Miami, FL",
            city="South Miami",
            service="Website design for small businesses in South Miami, Florida",
            lede="<p>South Miami's downtown is a place people park and walk: Sunset Drive, Red Road, and US-1. A restaurant or shop wins the next block when the hours, the cross street, and today's offer are obvious.</p><p>CRRE Labs is a short drive south in Pinecrest. Call (786) 733-6744.</p>",
            blocks=[
                ("For a sidewalk full of choices", [
                    "Show the days you are open and the days you are dark. A person standing on Sunset Drive will check the phone in their hand, then the door.",
                    "A short menu, service list, or class list fits on Starter. Dinner, brunch, and private events deserve their own space, which is what Business is for: up to five pages at $199 to set up and $29 a month.",
                    "Offices near downtown and toward the university need the suite, what a first visit is for, and a form for questions that are easier to write than to ask on the sidewalk.",
                ]),
                ("The phone still closes it", [
                    "Business and Pro include click-to-call, because a table, a fitting, or a same-week appointment often starts as a tap. We will use the number you want customers to dial.",
                ]),
            ],
            faqs=[
                ("Is South Miami the same as the City of Miami?", "South Miami is its own city, south of downtown. If your shop is on Sunset Drive, start here. If you are in Edgewater, Downtown, or Midtown, the Miami page is the better fit."),
                ("Do you have an office on Sunset Drive?", "The studio is at 12394 SW 82nd Ave in Pinecrest. Call (786) 733-6744 and we will help from there."),
                ("Can a restaurant launch on one page?", "Yes, when the menu, hours, address, and phone fit on Starter at $99 and $15 a month. A longer menu belongs on Business."),
                ("Do you guarantee a ranking for restaurants here?", "We make the hours, the place, and the menu easy to find, and on Business and Pro we line that up with your Google listing."),
            ],
        ),
        dict(
            path="/web-design-coral-gables/",
            title="Website Design in Coral Gables, FL | CRRE Labs",
            description="Website design in Coral Gables for Miracle Mile businesses. From $99 setup and $15/month. Studio in Pinecrest. Call (786) 733-6744.",
            h1="Website design in Coral Gables, FL",
            city="Coral Gables",
            service="Website design for small businesses in Coral Gables, Florida",
            lede="<p>On Miracle Mile and the downtown grid, the business next door already looks finished. Your site can be quiet and specific: what you do, when you are open, and how the front desk answers.</p><p>CRRE Labs works from Pinecrest, a short drive south, at 12394 SW 82nd Ave. Call (786) 733-6744.</p>",
            blocks=[
                ("A fit for the Mile", [
                    "Restaurants, salons, galleries, and professional offices do well with a site that respects the street. Starter, at $99 and $15 a month, is enough when one page can hold hours and a service list.",
                    "Business, at $199 and $29 a month, is the practical step when you want up to five pages, click-to-call, and a Google listing that tells the same story as the site. One revision a month keeps a seasonal menu or a new provider current.",
                    "Pro, at $349 and $49 a month, adds a booking or payment embed when the front desk already uses a tool that can sit on the site, plus one or two content updates a month.",
                ]),
                ("When you want something larger", [
                    "A custom site, closer to the Miami leasing projects in our portfolio, is a separate quote. Look at the work, then call. We will tell you which path fits before any design starts.",
                ]),
            ],
            faqs=[
                ("Will the site feel generic?", "The packages are clean and direct: your facts, your photos, your phone. If you want a fully custom design, like the apartment sites in the portfolio, ask for that quote."),
                ("Can we meet in the Gables?", "We work by phone or video from the Pinecrest studio. Call (786) 733-6744."),
                ("Do you build restaurant sites on the Mile?", "Yes. Hours, menu, address, and phone come first. Online booking is part of Pro when you already have a tool we can embed."),
                ("Do I need a Google listing first?", "Helpful, and not required to start. Business and Pro include time to line the listing up with the site."),
            ],
        ),
        dict(
            path="/web-design-palmetto-bay/",
            title="Web Design in Palmetto Bay, FL | CRRE Labs",
            description="Web design in Palmetto Bay for home services, offices, and local restaurants. From $99 setup and $15/month. Call (786) 733-6744.",
            h1="Web design in Palmetto Bay, FL",
            city="Palmetto Bay",
            service="Website design for small businesses in Palmetto Bay, Florida",
            lede="<p>Palmetto Bay is quieter than Kendall Drive. Along Old Cutler, Franjo Road, and SW 184th Street, the businesses are often home services, dental offices, tutors, and a smaller set of restaurants. Residents also shop and eat in Pinecrest and Cutler Bay.</p><p>We are the next village north, at 12394 SW 82nd Ave in Pinecrest. Call (786) 733-6744.</p>",
            blocks=[
                ("Say where you actually drive", [
                    "A roofer, a dentist, or a tutor in Palmetto Bay should name the villages they cover and skip the ones they do not. That honesty is what gets the right call.",
                    "New patients and new homeowners want hours, the suite, and what to expect on the first visit. Put that in plain language and leave the phone number where a thumb can find it.",
                ]),
                ("Updates when the week changes", [
                    "Hours and specials move. Starter is a steady one-page site at $99 and $15 a month. Business adds one revision a month. Pro adds one or two content updates a month, which is the right fit after a busy storm week or a seasonal menu.",
                    "The prices are the same here as in Pinecrest: $99 + $15/mo, $199 + $29/mo, and $349 + $49/mo, with hosting included.",
                ]),
            ],
            faqs=[
                ("Are you based in Palmetto Bay?", "The studio is in Pinecrest, the village just north, at 12394 SW 82nd Ave. Palmetto Bay is part of the area we serve every week."),
                ("Can the site mention Cutler Bay and Pinecrest?", "Yes, when you really work there. Send the list you want published."),
                ("What if I only need hours and a phone number?", "Starter is one page for $99 and $15 a month, with a contact form and hosting. That is enough for a lot of crews."),
                ("How do I start?", "Call (786) 733-6744 or send the form. Tell us the trade and the villages you cover."),
            ],
        ),
        dict(
            path="/web-design-miami/",
            title="Small Business Website Design in Miami | CRRE Labs",
            description="Small-business website design in Miami from $99 setup and $15/month, plus custom leasing sites. Pinecrest studio. Call (786) 733-6744.",
            h1="Small business website design in Miami",
            city="Miami",
            service="Website design for small businesses in Miami, Florida",
            lede="<p>Some searches mean the City of Miami. Others mean a business anywhere in the county that simply says Miami. Either way, the useful site is the one that gets the right person on the phone.</p><p>CRRE Labs is in Pinecrest, at 12394 SW 82nd Ave. Call (786) 733-6744. Customers rate us 5.0 from 24 Google reviews.</p>",
            blocks=[
                ("A simple site for a local business", [
                    "Starter is $99 to set up and $15 a month: one page, a contact form, and hosting. Business is $199 and $29 a month: up to five pages, click-to-call, and help aligning your Google listing. Pro is $349 and $49 a month: up to ten pages, booking or payments, and a couple of content updates each month.",
                    "Many other Miami quotes start around $300 to $500. If you need more than ten pages, we will price that as its own project.",
                    "If you are actually in Pinecrest, Kendall, South Miami, Coral Gables, or Palmetto Bay, those pages speak to your street. Start there when it matches.",
                ]),
                ("Leasing sites for Miami buildings", [
                    "We have also designed leasing sites for Downtown 1st, Downtown 5th, 22 Biscayne Bay, Urban 22 Miami, 25 Biscayne Park, and Melody Tower, plus Flagler on the River, 22 Skyview, and One Plaza West. RG Capital Partners, a firm working in Kansas City and Miami, is in the portfolio too.",
                    "Those are custom projects. <a class=\"text-accent underline\" href=\"/work/miami-apartment-sites/\">See the apartment stories</a>, then tell us about yours.",
                ]),
            ],
            faqs=[
                ("Are the apartment websites part of the $99 plan?", "The $99, $199, and $349 prices are for a small-business site. A full leasing site is custom. Describe the building on the form and we will quote it."),
                ("Which parts of Miami do you cover?", "Package work is welcome from businesses across Miami, with the studio in Pinecrest. If you go to the customer, we will list the areas you cover. If you have a counter, we will publish the address your customers already use."),
                ("How long does a new site take?", "Most package sites are ready in one to two weeks, so you can start getting calls from your new site fast."),
                ("How do I begin?", "Call (786) 733-6744, use the form, or check out a package. Stripe takes the setup fee for the plan you choose."),
            ],
        ),
    ]
    for spec in pages:
        local_page(
            spec["path"], spec["title"], spec["description"], spec["h1"], spec["lede"],
            spec["blocks"], spec["faqs"], spec["service"], spec["city"],
            "Tell us the business name, the neighborhood, and whether you already have a Google listing.",
        )


def industry_pages():
    specs = [
        dict(
            path="/websites-for-restaurants/",
            title="Restaurant Website Design in Miami | CRRE Labs",
            description="Restaurant websites with hours, menu, address, and phone. From $99 setup and $15/month. Booking on Pro. Call (786) 733-6744.",
            h1="Restaurant websites that lead with the meal and the phone",
            service="Website design for restaurants",
            lede="<p>Guests want three things before they leave the couch: where you are, when you are open, and what you serve. Delivery apps are someone else's menu. Your site is the one you control, and it should agree with the hours on your Google listing.</p><p>We build those sites from Pinecrest for restaurants in Pinecrest, Kendall, South Miami, Coral Gables, Palmetto Bay, and Miami. Call (786) 733-6744.</p>",
            blocks=[
                ("What guests should see first", [
                    "Address, cross street, and hours, including the days you are closed. A walk-up street in South Miami or Coral Gables still loses the visit when Thursday is wrong.",
                    "Your menu, in your words. A short menu fits on Starter, one page at $99 and $15 a month. Brunch, dinner, and private events fit more naturally on Business, up to five pages at $199 and $29 a month.",
                    "Photos of the food and the room, if you have them. Online booking is part of Pro, at $349 and $49 a month, when you already use a tool we can place on the site.",
                ]),
                ("A price you can compare", [
                    "Many local website quotes start around $300 to $500. Our restaurant sites start at $99 to set up and $15 a month, with hosting included, and you can stop the monthly plan when you want.",
                ]),
            ],
            faqs=[
                ("Can you put my menu on the site?", "Yes. You send the menu, and we place it within the page count of the plan you choose."),
                ("I am already on delivery apps. Do I still need a site?", "The apps show what they choose to show. Your site is where the hours, the phone, the address, and the full menu are yours. Your Google listing still helps people find the door."),
                ("Which plan includes reservations?", "Pro, at $349 setup and $49 a month, includes a booking or payment embed. Starter and Business focus on the menu, the hours, and the phone."),
                ("Where do you work?", "Pinecrest, Kendall, South Miami, Coral Gables, Palmetto Bay, and Miami. South Miami and Coral Gables are the walkable streets. Kendall is more often a plaza."),
            ],
        ),
        dict(
            path="/websites-for-contractors/",
            title="Websites for Contractors and Home Services | CRRE Labs",
            description="Websites for Miami-area contractors and home services. From $99 setup and $15/month. Call (786) 733-6744.",
            h1="Contractor websites that list the work and the neighborhoods",
            service="Website design for contractors and home services",
            lede="<p>Someone searching for a plumber, roofer, electrician, painter, or AC crew adds a place: Pinecrest, Kendall, Palmetto Bay, Coral Gables. Your site should list the work you do and the cities you drive to, with a phone number that matches your Google listing.</p><p>CRRE Labs is at 12394 SW 82nd Ave in Pinecrest. Call (786) 733-6744. Sites start at $99 to set up and $15 a month.</p>",
            blocks=[
                ("A site that gets the right call", [
                    "Name the trades in the words a homeowner would type. If you do not do roofs, leave roofs off. The goal is the next useful call, not a longer list.",
                    "Send us the cities you cover. Palmetto Bay, Pinecrest, and Cutler Bay are a natural cluster. Kendall is a different drive. We will publish your list.",
                    "Estimates start with the contact form and the phone. Business and Pro add click-to-call, because a lot of this work begins in a driveway. Share photos you are happy to show, and any license number you want on the site.",
                ]),
                ("Which plan fits a crew", [
                    "Starter, $99 and $15 a month, is one page for a single trade and a tight service area. Business, $199 and $29 a month, gives each trade room of its own, up to five pages, plus one revision a month. Pro, $349 and $49 a month, adds a couple of updates a month and a way to take a deposit online.",
                ]),
            ],
            faqs=[
                ("Will the site bring jobs on its own?", "It gives homeowners your services, your cities, and your phone in one place. What happens after they call depends on the work, the season, and you."),
                ("Can each trade have its own page?", "Business allows up to five pages. Pro allows up to ten. Starter is a single page."),
                ("Will you create a page for every city in the county?", "We name the cities you serve. A pile of thin city pages is outside these three plans."),
                ("How do I pay?", "Stripe checkout on the plan you choose, a call to (786) 733-6744, or the form. Setup is paid up front."),
            ],
        ),
        dict(
            path="/websites-for-salons-and-spas/",
            title="Salon and Spa Website Design in Miami | CRRE Labs",
            description="Salon and spa websites with services, hours, and photos. Booking on the Pro plan. From $99 setup and $15/month. Call (786) 733-6744.",
            h1="Salon and spa websites with the services, the hours, and the right chair",
            service="Website design for salons and spas",
            lede="<p>Kendall, Coral Gables, and South Miami are full of salons. The site has to say which location, which services, and how to book or call. A stock photo of a city skyline does not get someone into your chair.</p><p>If you want prices public, send the numbers you honor. Our own website prices are public too: $99 + $15/mo, $199 + $29/mo, or $349 + $49/mo.</p>",
            blocks=[
                ("Services, staff, and the book", [
                    "A clear service list and your hours belong on every plan. Staff names fit inside the page count. Business, up to five pages, can separate cuts, color, and spa services.",
                    "Pro, at $349 to set up and $49 a month, includes a booking or payment embed when you already use a tool we can place on the site. If the book is still a paper notebook, Starter or Business will serve you better.",
                    "Send photos you have the right to use. We design with what you bring.",
                ]),
                ("Different streets, different first screens", [
                    "In South Miami and Coral Gables, people walk, so the cross street matters as much as the service list. In Kendall, name the plaza. In Pinecrest and Palmetto Bay, the site often confirms a recommendation a neighbor already made.",
                ]),
            ],
            faqs=[
                ("Can clients book online?", "Yes on Pro, when you have a booking tool we can embed. Starter and Business focus on services, hours, photos, and the phone."),
                ("Can I show color or nail prices?", "Yes. Send the prices you want public and we will place them."),
                ("Is one page enough?", "For a single list of services and a phone number, Starter at $99 and $15 a month is enough. Split the menu when one screen gets hard to scan."),
                ("Do you promise new clients from Google?", "Business and Pro include basic on-page SEO and time on your Google listing so the salon is described clearly. Results depend on reviews, location, and the market."),
            ],
        ),
        dict(
            path="/websites-for-medical-and-dental/",
            title="Websites for Medical and Dental Offices | CRRE Labs",
            description="Websites for medical and dental offices in the Miami area. Hours, location, and new-patient info. From $99 setup and $15/month. Call (786) 733-6744.",
            h1="Medical and dental websites that welcome a new patient",
            service="Website design for medical and dental offices",
            lede="<p>A new patient wants the address, the hours, the phone, and a plain explanation of the practice. That is the site we build: a front door on the web, with the same details as your Google listing.</p><p>Kendall has a thick run of offices near the hospital. Coral Gables has practices on and off Miracle Mile. Pinecrest and Palmetto Bay often grow by referral. The three website plans are the same. Call (786) 733-6744.</p>",
            blocks=[
                ("What belongs on the front door", [
                    "Name, suite, hours, and phone, matching the listing patients already trust. Business and Pro include time to check those facts against your Google listing.",
                    "Describe the care you want a new patient to understand, in language you approve. Parking or suite directions help when the building is confusing.",
                    "The form is for general questions. Patients who need care should call the office. Clinical records stay in your system, where they belong.",
                ]),
                ("Booking without a software project", [
                    "Pro can embed the scheduler your front desk already uses, when that tool can sit on a page. It is a website feature, priced at $349 to set up and $49 a month, alongside up to ten pages and a couple of content updates.",
                    "Many local quotes start around $300 to $500. Starter, at $99 and $15 a month, is the right size when one page can carry hours and the phone.",
                ]),
            ],
            faqs=[
                ("Is this a patient portal?", "It is the public website: location, hours, phone, and what a new patient should know. Records and clinical messages stay with your office."),
                ("Can new patients book online?", "On Pro, yes, if your current scheduler can be embedded. The plan does not replace your records system."),
                ("Can you list the insurance we take?", "Send the list you want public, and keep it current. You know which plans you accept."),
                ("Which plan do offices choose?", "One page with hours and a phone is Starter, $99 + $15/mo. Separate pages for the services you want found is Business, $199 + $29/mo. Booking and monthly updates are Pro, $349 + $49/mo."),
            ],
        ),
        dict(
            path="/websites-for-property-managers/",
            title="Websites for Property Managers and Real Estate | CRRE Labs",
            description="Websites for property managers and real estate offices from $99 setup, plus custom Miami leasing sites. Call (786) 733-6744.",
            h1="Websites for property managers and real estate offices",
            service="Website design for property managers and real estate offices",
            lede="<p>Owners, residents, and applicants should each know how to reach you. A small office needs a clear brochure site. A single building needs a leasing site with photos, amenities, and a way to ask for a tour. We do both, and they are priced differently.</p>",
            blocks=[
                ("A brochure site for a small office", [
                    "Starter, Business, and Pro cover one, five, or ten pages at $99, $199, or $349 to set up, then $15, $29, or $49 a month. Use them to explain where you manage, how an owner reaches you, and how an applicant reaches leasing.",
                    "If those are two different numbers, the site should say so. Business and Pro add click-to-call and time to align your Google listing with the office address.",
                    "Pro can embed a form of payment or a scheduler if you take applications that way. Your property-management software stays the system of record.",
                ]),
                ("Leasing sites and firm sites", [
                    "Our portfolio includes leasing sites for Downtown 1st, Downtown 5th, 22 Biscayne Bay, Urban 22 Miami, 25 Biscayne Park, and Melody Tower, plus RG Capital Partners, a private-equity firm in Kansas City and Miami.",
                    "Those projects are custom. <a class=\"text-accent underline\" href=\"/work/\">Read the stories</a> and then tell us about the building or the firm. Iris, our assistant for day-to-day property operations, lives on its <a class=\"text-accent underline\" href=\"/iris/\">own page</a>.",
                ]),
            ],
            faqs=[
                ("Can a building site be the $199 plan?", "Business is up to five pages for a small office. A full leasing site is custom. Describe the property and we will quote it."),
                ("Do the stories include occupancy numbers?", "They describe the sites and link to them. We keep the numbers that belong to your building off our marketing."),
                ("We manage homes, not a tower. Where do we start?", "If one page can explain who you serve and how to call, Starter is $99 and $15 a month. If owners and applicants need different explanations, Business allows up to five pages."),
                ("Where are you?", "12394 SW 82nd Ave, Pinecrest, FL 33156. (786) 733-6744. The building examples are in Miami. The studio is in Pinecrest."),
            ],
        ),
    ]
    for spec in specs:
        local_page(
            spec["path"], spec["title"], spec["description"], spec["h1"], spec["lede"],
            spec["blocks"], spec["faqs"], spec["service"], None,
            "Tell us the business, the neighborhood, and whether you want a package or a custom site.",
        )


def work_pages():
    buildings = [
        ("Downtown 1st", "https://downtown1st.com", "downtown-1st-leasing-website",
         "Downtown 1st leasing site, a luxury rental tower in downtown Miami.",
         "A leasing site for a 56-story rental tower in the Arts and Entertainment District. Visitors see the residences, the amenities, the floor plans, and a way to ask for a tour. The building is at 30 SW 1st Street."),
        ("Downtown 5th", "https://downtown5.com", "downtown-5th-leasing-website",
         "Downtown 5th leasing site for a downtown Miami rental tower.",
         "A rental tower in downtown Miami. The site leads with amenities, a way to schedule a tour, and leasing contact."),
        ("22 Biscayne Bay", "https://22biscaynebay.com", "22-biscayne-bay-leasing-website",
         "22 Biscayne Bay leasing site for waterfront apartments in Edgewater.",
         "Waterfront apartments in Edgewater. The site shows bay views, floor plans, photo galleries, amenities, and tour scheduling."),
        ("Urban 22 Miami", "https://urban22miami.com", "urban-22-miami-leasing-website",
         "Urban 22 Miami leasing site for an Edgewater rental building.",
         "A contemporary leasing site for a luxury rental building in Edgewater, with galleries, floor plans, and a direct way to ask about availability."),
        ("25 Biscayne Park", "https://25biscaynepark.com", "25-biscayne-park-leasing-website",
         "25 Biscayne Park leasing site for apartments on Biscayne Boulevard.",
         "Apartments on Biscayne Boulevard. The site presents the amenities, tour booking, and leasing contact in a layout that is quick on a phone."),
        ("Melody Tower", "https://melodytower.com", "melody-tower-leasing-website",
         "Melody Tower leasing site for a Midtown Miami rental tower.",
         "A Midtown rental tower at 245 NE 14th Street. Visitors can browse the amenities and reach the leasing office without hunting."),
    ]
    blocks = []
    for name, url, stem, alt, copy in buildings:
        blocks.append(f'''
<section class="py-10 border-t border-white/10">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 grid md:grid-cols-2 gap-6 items-start">
    {picture(stem, alt)}
    <div>
      <h2 class="font-display text-2xl text-white font-bold mb-3">{name}</h2>
      <p class="text-gray-300 leading-relaxed mb-4">{copy}</p>
      <a href="{url}" target="_blank" rel="noopener noreferrer" class="text-accent font-semibold">Visit {name}</a>
    </div>
  </div>
</section>''')
    extra = '''
<section class="py-10">
  <div class="max-w-3xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-2xl text-white font-bold mb-3">More Miami rental sites</h2>
    <p class="text-gray-300 mb-3">A few more communities we have put online:</p>
    <ul class="text-gray-300 space-y-3 list-disc ml-5">
      <li><a class="text-accent underline" href="https://flaglerontheriver.com" target="_blank" rel="noopener noreferrer">Flagler on the River</a> — a downtown riverfront community, with amenities and floor plans.</li>
      <li><a class="text-accent underline" href="https://22skyview.com" target="_blank" rel="noopener noreferrer">22 Skyview</a> — an Edgewater high-rise, with floor plans and a map.</li>
      <li><a class="text-accent underline" href="https://oneplazawestbrickell.com" target="_blank" rel="noopener noreferrer">One Plaza West</a> — an apartment community with a fast, simple layout for prospective residents.</li>
    </ul>
  </div>
</section>'''
    canonical = "https://crrelabs.com/work/miami-apartment-sites/"
    body = hero(
        crumbs([("Home", "/"), ("Work", "/work/"), ("Miami apartments", "/work/miami-apartment-sites/")]),
        "Leasing websites for Miami apartment communities",
        "<p>These are leasing sites for Miami rental buildings. Each one helps a future resident see the building and ask for a tour. If you manage a community and want something in this spirit, tell us about it.</p>",
        "/portfolio/",
        "See the portfolio",
        "/#contact",
        "Start a project",
    )
    body += "".join(blocks) + extra + "</main>"
    emit("work/miami-apartment-sites/index.html", page(
        "Miami Apartment Website Design | CRRE Labs",
        "Leasing websites for Miami apartment communities, including Downtown 1st, 22 Biscayne Bay, and Melody Tower. Designed by CRRE Labs in Pinecrest.",
        canonical,
        "/work/",
        body,
        jsonld(
            service_block("Leasing websites for Miami apartment communities", canonical, "Miami", "Leasing websites for Miami apartment communities by CRRE Labs."),
            breadcrumb([
                ("Home", "https://crrelabs.com/"),
                ("Work", "https://crrelabs.com/work/"),
                ("Miami apartments", canonical),
            ]),
        ),
    ))

    rg_canonical = "https://crrelabs.com/work/rg-capital-partners/"
    rg = hero(
        crumbs([("Home", "/"), ("Work", "/work/"), ("RG Capital Partners", "/work/rg-capital-partners/")]),
        "A website for RG Capital Partners",
        "<p>RG Capital Partners buys and steadies commercial property in Kansas City and Miami. They needed a site that introduces the firm, shows the portfolio, and gives an investor a clear way to get in touch. We delivered it in under a week.</p>",
        "https://rgcappartners.com",
        "Visit the site",
        "/portfolio/",
        "Back to the portfolio",
    )
    rg += f'''
<section class="py-8">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 grid md:grid-cols-2 gap-6 items-start">
    {picture("rg-capital-partners-website", "RG Capital Partners homepage, with the headline Private Equity Real Estate and buttons to view the portfolio or get in touch.")}
    <div class="text-gray-300 leading-relaxed space-y-4">
      <h2 class="font-display text-2xl text-white font-bold">What visitors find</h2>
      <p>The homepage opens with the firm, then offers Home, About, Portfolio, Team, and Contact, plus an investor portal. Two buttons do the rest of the work: view the portfolio, or get in touch.</p>
      <p>The properties and the firm's own figures live on their site. Our job was to make that story easy to follow.</p>
      <p><a class="text-accent font-semibold" href="https://rgcappartners.com" target="_blank" rel="noopener noreferrer">rgcappartners.com</a></p>
    </div>
  </div>
</section>
</main>'''
    emit("work/rg-capital-partners/index.html", page(
        "RG Capital Partners Website | CRRE Labs",
        "Website for RG Capital Partners, a private-equity real estate firm in Kansas City and Miami. Designed by CRRE Labs.",
        rg_canonical,
        "/work/",
        rg,
        jsonld(
            service_block("Website for RG Capital Partners", rg_canonical, "Miami", "Website for RG Capital Partners by CRRE Labs."),
            breadcrumb([
                ("Home", "https://crrelabs.com/"),
                ("Work", "https://crrelabs.com/work/"),
                ("RG Capital Partners", rg_canonical),
            ]),
        ),
    ))

    hub = hero(
        crumbs([("Home", "/"), ("Work", "/work/")]),
        "Work",
        "<p>Two stories from recent projects. Open the live sites, then tell us about yours.</p>",
        "/portfolio/",
        "Portfolio",
        "/#contact",
        "Start a project",
    )
    hub += '''
<section class="pb-16">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 grid md:grid-cols-2 gap-4">
    <a class="glass rounded-2xl p-6 block" href="/work/miami-apartment-sites/"><h2 class="text-white text-xl font-semibold mb-2">Miami apartment communities</h2><p class="text-gray-300 text-sm">Leasing sites that help a future resident picture the building and ask for a tour.</p></a>
    <a class="glass rounded-2xl p-6 block" href="/work/rg-capital-partners/"><h2 class="text-white text-xl font-semibold mb-2">RG Capital Partners</h2><p class="text-gray-300 text-sm">A private-equity real estate site for Kansas City and Miami.</p></a>
  </div>
</section></main>'''
    emit("work/index.html", page(
        "Web Design Work | CRRE Labs",
        "Recent web design from CRRE Labs: Miami apartment leasing sites and RG Capital Partners.",
        "https://crrelabs.com/work/",
        "/work/",
        hub,
        jsonld(breadcrumb([("Home", "https://crrelabs.com/"), ("Work", "https://crrelabs.com/work/")])),
    ))


def blog():
    cost_faqs = [
        ("What does CRRE Labs charge in 2026?", "Starter is $99 setup and $15 a month. Business is $199 setup and $29 a month. Pro is $349 setup and $49 a month. Domain, SSL, and hosting are included on each."),
        ("What do other local quotes look like?", "Many start around $300 to $500. Ask what that number includes, especially hosting and how many pages you get."),
        ("Are the Miami apartment sites $99?", "Those are custom projects. The three prices above are for a small-business website."),
    ]
    cost_body = f'''
<main id="main">
<article class="pt-28 pb-8">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 prose-page">
    {crumbs([("Home", "/"), ("Blog", "/blog/"), ("Website cost in Miami", "/blog/how-much-does-a-website-cost-in-miami-2026/")])}
    <p class="text-sm text-gray-400 mb-4">November 17, 2026 · CRRE Labs</p>
    <h1 class="font-display text-4xl sm:text-5xl font-bold text-white leading-tight mb-6">How much does a website cost in Miami in 2026?</h1>
    <p class="text-gray-300">A small-business website from CRRE Labs is $99, $199, or $349 to set up, then $15, $29, or $49 a month. Many other local quotes start around $300 to $500. Here is what our prices buy, and what to ask before you compare a single number.</p>
    <h2>Three ways to start</h2>
    <p class="text-gray-300">The studio is at {ADDRESS}. Call {PHONE_DISPLAY}. The price is the same in Pinecrest, Kendall, South Miami, Coral Gables, Palmetto Bay, and Miami.</p>
    <ul>
      <li><strong class="text-white">Starter — $99 setup + $15/mo.</strong> One page, a contact form, and hosting with the domain and SSL. If you leave and come back within 90 days, reactivation is $49.</li>
      <li><strong class="text-white">Business — $199 setup + $29/mo.</strong> Up to five pages, click-to-call, basic on-page SEO, help with your Google listing, and one revision a month. Reactivation within 90 days is $99.</li>
      <li><strong class="text-white">Pro — $349 setup + $49/mo.</strong> Up to ten pages, plus a booking or payment embed, an analytics report, and one or two content updates a month. Reactivation within 90 days is $175.</li>
    </ul>
    <p class="text-gray-300">Every plan is month to month. Setup is paid up front and stays with us once design begins. You can pay the setup on the <a href="/pricing/">pricing page</a>.</p>
    <h2>What a higher quote might include</h2>
    <p class="text-gray-300">A $450 quote is not automatically a worse deal. It may cover more pages, photography, or a custom build. A lower quote may be a page you rent. Ask who owns the domain, whether hosting is included, how edits work after launch, and what happens if you cancel. Ours is month to month, with the reactivation fees above if you return within 90 days.</p>
    <p class="text-gray-300">Our $99 plan is real, and it is focused: one page, hosting included, no monthly revision. If you want five pages and a Google listing that matches the site, the number to compare is $199 to set up and $29 a month.</p>
    <h2>When the price changes</h2>
    <ul>
      <li>Page count: one, up to five, or up to ten.</li>
      <li>On-page SEO and Google listing help, which start on Business.</li>
      <li>Booking, payments, an analytics report, or monthly edits, which are Pro.</li>
      <li>Work outside the card. Leasing sites, assistants, and 3D printing are quoted on their own. The <a href="/work/">stories</a> show the kind of custom web work we take on.</li>
    </ul>
    <h2>Start with a conversation</h2>
    <p class="text-gray-300">Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>, use the form on the <a href="/#contact">homepage</a>, or check out a package. If you run a restaurant, a crew, a salon, an office, or a property business, the industry pages explain which plan tends to fit.</p>
  </div>
</article>
{faq_html(cost_faqs)}
</main>'''
    cost_url = "https://crrelabs.com/blog/how-much-does-a-website-cost-in-miami-2026/"
    emit("blog/how-much-does-a-website-cost-in-miami-2026/index.html", page(
        "How Much Does a Website Cost in Miami in 2026? | CRRE Labs",
        "CRRE Labs website prices in 2026: $99, $199, or $349 to set up, then $15, $29, or $49 a month. Many local quotes start around $300 to $500.",
        cost_url,
        "/blog/",
        cost_body,
        jsonld(
            article_block("How much does a website cost in Miami in 2026?", cost_url, "CRRE Labs website prices for 2026 and how they compare with typical local starting quotes."),
            faq_block(cost_faqs),
            breadcrumb([("Home", "https://crrelabs.com/"), ("Blog", "https://crrelabs.com/blog/"), ("Website cost in Miami", cost_url)]),
        ),
    ))

    gbp_faqs = [
        ("Does a Google listing replace a website?", "They do different jobs. The listing helps people find you on Maps. The website is where you explain the services, the menu, or the next step in as much detail as you need."),
        ("Do your plans include the Google listing?", "Business and Pro include time to align your listing with the site. Starter is the website itself: one page, a form, and hosting."),
        ("Where can I see your reviews?", "We are at 5.0 from 24 Google reviews. The studio is at 12394 SW 82nd Ave, Pinecrest, FL 33156, and the phone is (786) 733-6744."),
    ]
    gbp_body = f'''
<main id="main">
<article class="pt-28 pb-8">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 prose-page">
    {crumbs([("Home", "/"), ("Blog", "/blog/"), ("Website or Google listing", "/blog/do-i-need-a-website-if-i-have-a-google-business-profile/")])}
    <p class="text-sm text-gray-400 mb-4">November 17, 2026 · CRRE Labs</p>
    <h1 class="font-display text-4xl sm:text-5xl font-bold text-white leading-tight mb-6">Do I need a website if I already have a Google Business Profile?</h1>
    <p class="text-gray-300">Often, yes. A Google Business Profile is the Maps listing: hours, phone, address, photos, and reviews. A website is the page you edit, with room for a menu, a service list, or a form. One does not replace the other.</p>
    <h2>What the listing does well</h2>
    <p class="text-gray-300">People who already know the neighborhood can find the pin, see the hours, and tap the phone. Reviews live there too. Ours are {RATING_HTML}. A listing can be enough for a while if all you need is the phone to ring.</p>
    <h2>Where a website helps</h2>
    <ul>
      <li>A full menu, a list of services, or several trades that will not fit in a short description.</li>
      <li>The plaza, the suite, and the cities you drive to, spelled out.</li>
      <li>A form for people who will write and will not call.</li>
      <li>Prices you are ready to publish. Ours are on the site because there is room for three plans and what each one includes.</li>
      <li>A page on your own domain, for as long as you keep it.</li>
    </ul>
    <h2>Use them together</h2>
    <p class="text-gray-300">Point the listing at the site. Put the same name, address, and phone on both. When the hours disagree, the customer does not know which Thursday to trust. Business ($199 setup and $29 a month) and Pro ($349 setup and $49 a month) include that alignment. Starter ($99 setup and $15 a month) is the site itself.</p>
    <p class="text-gray-300">That work means the facts match and the pages are written in ordinary language. It is not a promise about where you rank.</p>
    <h2>Reviews are not the whole story</h2>
    <p class="text-gray-300">Reviews help people choose you. They do not lay out private events, a second location, or a separate path for an owner and an applicant. Property managers feel that quickly. The <a href="/websites-for-property-managers/">property-manager page</a> shows the difference between a small office site and a custom building site.</p>
    <h2>If you decide you want the site</h2>
    <p class="text-gray-300">The same prices as in <a href="/blog/how-much-does-a-website-cost-in-miami-2026/">what a Miami website costs in 2026</a>: $99 + $15/mo, $199 + $29/mo, or $349 + $49/mo. Hosting is included. Plans are month to month.</p>
    <p class="text-gray-300">If you only need the phone and the hours repeated on a single page, choose Starter. If the listing and the site should be checked against each other, choose Business.</p>
    <p class="text-gray-300">Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> or use the form on the homepage. The studio is at {ADDRESS}.</p>
  </div>
</article>
{faq_html(gbp_faqs)}
</main>'''
    gbp_url = "https://crrelabs.com/blog/do-i-need-a-website-if-i-have-a-google-business-profile/"
    emit("blog/do-i-need-a-website-if-i-have-a-google-business-profile/index.html", page(
        "Do I Need a Website If I Already Have a Google Business Profile? | CRRE Labs",
        "A Google listing and a website do different jobs. When a Pinecrest studio would still build the site, and what $99, $199, and $349 include.",
        gbp_url,
        "/blog/",
        gbp_body,
        jsonld(
            article_block("Do I need a website if I already have a Google Business Profile?", gbp_url, "How a Google Business Profile and a small-business website fit together, using CRRE Labs prices."),
            faq_block(gbp_faqs),
            breadcrumb([("Home", "https://crrelabs.com/"), ("Blog", "https://crrelabs.com/blog/"), ("Website or Google listing", gbp_url)]),
        ),
    ))

    index = hero(
        crumbs([("Home", "/"), ("Blog", "/blog/")]),
        "Notes for local businesses",
        "<p>Two practical reads: what a website costs here in 2026, and how a Google listing fits next to a site you own.</p>",
        "/pricing/",
        "See pricing",
        "/#contact",
        "Ask a question",
    )
    index += '''
<section class="pb-16">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 space-y-4">
    <a class="glass rounded-2xl p-6 block" href="/blog/how-much-does-a-website-cost-in-miami-2026/">
      <p class="text-xs text-gray-400 mb-2">November 17, 2026</p>
      <h2 class="text-white text-2xl font-semibold mb-2">How much does a website cost in Miami in 2026?</h2>
      <p class="text-gray-300">$99, $199, and $349 to set up, then $15, $29, and $49 a month, next to the $300 to $500 quotes we often hear.</p>
    </a>
    <a class="glass rounded-2xl p-6 block" href="/blog/do-i-need-a-website-if-i-have-a-google-business-profile/">
      <p class="text-xs text-gray-400 mb-2">November 17, 2026</p>
      <h2 class="text-white text-2xl font-semibold mb-2">Do I need a website if I already have a Google Business Profile?</h2>
      <p class="text-gray-300">What the listing does well, and which of our plans includes help keeping it in sync with the site.</p>
    </a>
  </div>
</section></main>'''
    emit("blog/index.html", page(
        "Blog | CRRE Labs",
        "Notes from CRRE Labs on Miami website prices and on using a Google Business Profile alongside your website.",
        "https://crrelabs.com/blog/",
        "/blog/",
        index,
        jsonld(breadcrumb([("Home", "https://crrelabs.com/"), ("Blog", "https://crrelabs.com/blog/")])),
    ))


def pricing():
    faqs = [
        ("When is setup due?", "Up front. Once we start designing, the setup fee stays with us."),
        ("Is there a long contract?", "No. Plans are month to month. The monthly fee is billed each month."),
        ("What if I cancel and come back?", "Within 90 days, reactivation is $49 on Starter, $99 on Business, and $175 on Pro."),
    ]
    body = hero(
        '<p class="text-sm text-accent font-semibold mb-4">Local business websites</p>',
        "Simple packages. No long contracts.",
        f"<p>A website for a local business, with the domain, SSL, and hosting included. Starter is $99 setup and $15 a month. Business is $199 and $29 a month. Pro is $349 and $49 a month. Many local quotes start around $300 to $500. The studio is at {ADDRESS}. Call {PHONE_DISPLAY}.</p>",
        "#packages",
        "Compare the three",
        "#contact",
        "Ask a question",
    )
    body += packages("Website packages")
    body += '''
<section class="pb-12">
  <div class="max-w-6xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-3xl font-bold text-white mb-6 text-center">Compare packages</h2>
    <div class="glass rounded-2xl overflow-x-auto">
      <table class="compare-table w-full min-w-[720px] text-sm text-gray-200">
        <thead><tr class="text-xs uppercase tracking-wide text-gray-400"><th>Feature</th><th>Starter</th><th>Business</th><th>Pro</th></tr></thead>
        <tbody>
          <tr><td>Setup (one-time)</td><td class="text-white font-semibold">$99</td><td class="text-white font-semibold">$199</td><td class="text-white font-semibold">$349</td></tr>
          <tr><td>Monthly</td><td class="text-white font-semibold">$15/mo</td><td class="text-white font-semibold">$29/mo</td><td class="text-white font-semibold">$49/mo</td></tr>
          <tr><td>Pages</td><td>1</td><td>Up to 5</td><td>Up to 10</td></tr>
          <tr><td>Contact form</td><td>Yes</td><td>Yes, plus click-to-call</td><td>Yes, plus click-to-call</td></tr>
          <tr><td>SEO</td><td>Not included</td><td>Basic on-page and Google Business Profile</td><td>Basic on-page and Google Business Profile</td></tr>
          <tr><td>Revisions / updates</td><td>Not included</td><td>1 revision a month</td><td>1–2 content updates a month</td></tr>
          <tr><td>Booking / payments</td><td>Not included</td><td>Not included</td><td>Booking widget or Stripe embed</td></tr>
          <tr><td>Analytics report</td><td>Not included</td><td>Not included</td><td>Included</td></tr>
          <tr><td>Domain, SSL, hosting</td><td>Included</td><td>Included</td><td>Included</td></tr>
          <tr><td>Reactivation within 90 days</td><td>$49</td><td>$99</td><td>$175</td></tr>
        </tbody>
      </table>
    </div>
    <div class="glass rounded-2xl p-6 mt-6 max-w-3xl mx-auto">
      <h3 class="text-white font-semibold mb-3">Good to know</h3>
      <ul class="text-sm text-gray-300 space-y-2 list-disc ml-5">
        <li>Month to month. No long contract.</li>
        <li>Setup is due up front. Once design begins, that fee stays with us.</li>
        <li>The monthly fee is billed each month and covers the domain, SSL, and hosting.</li>
        <li>These prices are for a small-business site. Custom work, including the apartment sites in our <a class="text-accent underline" href="/work/">stories</a>, is quoted on its own.</li>
        <li>Read <a class="text-accent underline" href="/blog/how-much-does-a-website-cost-in-miami-2026/">what a website costs in Miami in 2026</a> for a longer look at the numbers.</li>
      </ul>
    </div>
  </div>
</section>
'''
    body += faq_html(faqs)
    body += contact_form("pricing", "Tell us about the business and which package you are considering. We reply by email.")
    body += "</main>"
    catalog = {
        "@context": "https://schema.org",
        "@type": "OfferCatalog",
        "name": "CRRE Labs Local Business Website Program",
        "url": "https://crrelabs.com/pricing/",
        "provider": {
            "@type": "ProfessionalService",
            "name": "CRRE Labs LLC",
            "url": "https://crrelabs.com/",
            "telephone": "+1-786-733-6744",
            "email": EMAIL,
        },
        "itemListElement": [
            {"@type": "Offer", "name": "Starter", "description": "1-page local business website with contact form, domain, SSL, and hosting.", "priceSpecification": [
                {"@type": "UnitPriceSpecification", "price": "99", "priceCurrency": "USD", "name": "One-time setup"},
                {"@type": "UnitPriceSpecification", "price": "15", "priceCurrency": "USD", "billingDuration": "P1M", "name": "Monthly"},
            ]},
            {"@type": "Offer", "name": "Business", "description": "Up to 5 pages with contact form, click-to-call, basic SEO, and Google listing help.", "priceSpecification": [
                {"@type": "UnitPriceSpecification", "price": "199", "priceCurrency": "USD", "name": "One-time setup"},
                {"@type": "UnitPriceSpecification", "price": "29", "priceCurrency": "USD", "billingDuration": "P1M", "name": "Monthly"},
            ]},
            {"@type": "Offer", "name": "Pro", "description": "Up to 10 pages with booking or Stripe embed, analytics, and monthly content updates.", "priceSpecification": [
                {"@type": "UnitPriceSpecification", "price": "349", "priceCurrency": "USD", "name": "One-time setup"},
                {"@type": "UnitPriceSpecification", "price": "49", "priceCurrency": "USD", "billingDuration": "P1M", "name": "Monthly"},
            ]},
        ],
    }
    emit("pricing/index.html", page(
        "Website Pricing for Local Businesses | CRRE Labs",
        "Starter $99 + $15/mo, Business $199 + $29/mo, Pro $349 + $49/mo. Domain, SSL, and hosting included. Month to month. CRRE Labs, Pinecrest.",
        "https://crrelabs.com/pricing/",
        "/pricing/",
        body,
        jsonld(catalog, faq_block(faqs), breadcrumb([("Home", "https://crrelabs.com/"), ("Pricing", "https://crrelabs.com/pricing/")])),
    ))


def portfolio(_buildings=None):
    projects = [
        ("rg-capital-partners-website", "RG Capital Partners homepage, with the headline Private Equity Real Estate and a way to view the portfolio or get in touch.", "RG Capital Partners", "https://rgcappartners.com", "Private equity · Real estate", "A calm, dark site for a private-equity firm in Kansas City and Miami. Visitors can see the portfolio, meet the team, and get in touch. Delivered in under a week. <a class='text-accent underline' href='/work/rg-capital-partners/'>Read the story</a>."),
        ("hireanypm-directory-website", "HireAnyPM homepage, a directory where Florida property managers can be found.", "HireAnyPM", "https://hireanypm.com", "Directory", "A directory that helps people find property managers across Florida, with search and a featured spot for managers who want to stand out."),
        ("22-biscayne-bay-leasing-website", "22 Biscayne Bay leasing homepage for waterfront apartments in Edgewater.", "22 Biscayne Bay", "https://22biscaynebay.com", "Leasing · Edgewater", "Waterfront apartments in Edgewater, with floor plans, galleries, amenities, and a way to schedule a tour."),
        ("urban-22-miami-leasing-website", "Urban 22 Miami leasing homepage for an Edgewater rental building.", "Urban 22 Miami", "https://urban22miami.com", "Leasing · Edgewater", "A contemporary look at a luxury rental building in Edgewater, with galleries, floor plans, and contact details."),
        ("downtown-1st-leasing-website", "Downtown 1st leasing homepage for a downtown Miami rental tower.", "Downtown 1st", "https://downtown1st.com", "Leasing · Downtown", "A 56-story rental tower in the Arts and Entertainment District, with amenities, floor plans, and tour requests."),
        ("downtown-5th-leasing-website", "Downtown 5th leasing homepage for a downtown Miami rental tower.", "Downtown 5th", "https://downtown5.com", "Leasing · Downtown", "A downtown rental tower with amenities, tour scheduling, and an easy way to reach leasing."),
        ("25-biscayne-park-leasing-website", "25 Biscayne Park leasing homepage for apartments on Biscayne Boulevard.", "25 Biscayne Park", "https://25biscaynepark.com", "Leasing · Biscayne Boulevard", "Apartments on Biscayne Boulevard, with amenities, tour booking, and leasing contact that is easy to find on a phone."),
        ("melody-tower-leasing-website", "Melody Tower leasing homepage for a Midtown Miami rental tower.", "Melody Tower", "https://melodytower.com", "Leasing · Midtown", "A Midtown tower at 245 NE 14th Street, with amenities and a direct line to the leasing office."),
        ("crre-labs-website", "CRRE Labs homepage for a Pinecrest web design studio.", "CRRE Labs", "https://crrelabs.com/", "Our studio", "The site you are on: Pinecrest and Miami web design, three published prices, and a phone number you can tap."),
    ]
    cards = []
    for i, (stem, alt, name, url, tags, copy) in enumerate(projects):
        media = picture(stem, alt)
        text = f'''<div class="p-8 flex flex-col justify-center">
          <p class="tag inline-block mb-3 w-fit">{tags}</p>
          <h2 class="font-display text-2xl text-white font-bold mb-3">{name}</h2>
          <p class="text-gray-300 mb-4">{copy}</p>
          <a href="{url}" {"target=\"_blank\" rel=\"noopener noreferrer\"" if url.startswith("http") else ""} class="text-accent font-semibold">Visit site</a>
        </div>'''
        if i % 2:
            inner = f'{text}<div class="overflow-hidden">{media}</div>'
        else:
            inner = f'<div class="overflow-hidden">{media}</div>{text}'
        cards.append(f'<article class="project-card glass rounded-2xl overflow-hidden"><div class="grid md:grid-cols-2">{inner}</div></article>')
    body = hero(
        crumbs([("Home", "/"), ("Portfolio", "/portfolio/")]),
        "Portfolio",
        "<p>Sites for apartment communities, a real estate firm, and a Florida directory. Open any of them, then tell us what you want customers to do on yours.</p>",
        "/work/",
        "Read the stories",
        "/pricing/",
        "See pricing",
    )
    body += f'<section class="pb-16"><div class="max-w-7xl mx-auto px-4 sm:px-6 space-y-10">{"".join(cards)}</div></section></main>'
    emit("portfolio/index.html", page(
        "Portfolio — Web Design in Pinecrest | CRRE Labs",
        "Web design by CRRE Labs in Pinecrest: Miami apartment leasing sites, RG Capital Partners, and more.",
        "https://crrelabs.com/portfolio/",
        "/portfolio/",
        body,
        jsonld(breadcrumb([("Home", "https://crrelabs.com/"), ("Portfolio", "https://crrelabs.com/portfolio/")])),
    ))


def not_found():
    body = hero(
        "",
        "That page is not on this site",
        f"<p>The link may be old, or the address may be mistyped. The studio is still at {ADDRESS}. Call {PHONE_DISPLAY}.</p>",
        "/",
        "Go to the homepage",
        "/pricing/",
        "See pricing",
    )
    body += '''
<section class="pb-16"><div class="max-w-3xl mx-auto px-4 sm:px-6 grid sm:grid-cols-2 gap-3 text-gray-200">
  <a class="glass rounded-xl p-4" href="/web-design-pinecrest/">Pinecrest web design</a>
  <a class="glass rounded-xl p-4" href="/web-design-miami/">Miami web design</a>
  <a class="glass rounded-xl p-4" href="/portfolio/">Portfolio</a>
  <a class="glass rounded-xl p-4" href="/blog/">Blog</a>
  <a class="glass rounded-xl p-4" href="/work/">Case studies</a>
  <a class="glass rounded-xl p-4" href="/#contact">Contact</a>
</div></section></main>'''
    write_page("404.html", page(
        "Page not found | CRRE Labs",
        "That page is not on the CRRE Labs site. Call (786) 733-6744 or go back to Pinecrest and Miami website design.",
        "https://crrelabs.com/404.html",
        "/",
        body,
        "",
    ).replace('content="index, follow"', 'content="noindex, follow"'))


def sitemap():
    paths = [
        "https://crrelabs.com/",
        "https://crrelabs.com/pricing/",
        "https://crrelabs.com/portfolio/",
        "https://crrelabs.com/iris/",
        "https://crrelabs.com/3d-printing.html",
        "https://crrelabs.com/games/",
        "https://crrelabs.com/games/hoops.html",
        "https://crrelabs.com/games/tictactoe.html",
        "https://crrelabs.com/work/",
        "https://crrelabs.com/work/miami-apartment-sites/",
        "https://crrelabs.com/work/rg-capital-partners/",
        "https://crrelabs.com/blog/",
        "https://crrelabs.com/blog/how-much-does-a-website-cost-in-miami-2026/",
        "https://crrelabs.com/blog/do-i-need-a-website-if-i-have-a-google-business-profile/",
    ]
    for _, href in AREAS + INDUSTRIES:
        paths.append("https://crrelabs.com" + href)
    urls = "\n".join(f"  <url><loc>{p}</loc><lastmod>{LASTMOD}</lastmod></url>" for p in paths)
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
'''
    (Path(__file__).resolve().parents[1] / "sitemap.xml").write_text(xml)


def main():
    home()
    area_pages()
    industry_pages()
    work_pages()
    blog()
    pricing()
    portfolio()
    not_found()
    sitemap()
    print(f"wrote {len(URLS)} html files")


if __name__ == "__main__":
    main()
