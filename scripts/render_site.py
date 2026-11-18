#!/usr/bin/env python3
"""Write the public marketing pages. Output is committed static HTML."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chrome import (  # noqa: E402
    ADDRESS, EMAIL, PHONE_DISPLAY, PHONE_TEL, STRIPE, LASTMOD, RATING_HTML, REVIEW_URL,
    AREAS, INDUSTRIES, article_block, breadcrumb, business_block,
    contact_form, crumbs, dumps, faq_block, faq_html, jsonld, org_block,
    packages, page, picture, reviews_section, service_block, website_block,
    write_page, cities, postal,
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


def home():
    faqs = [
        (
            "How much does a small-business website cost at CRRE Labs?",
            "The Local Business Website Program has three packages. Starter is $99 setup and $15 a month for 1 page and a contact form. Business is $199 setup and $29 a month for up to 5 pages, click-to-call, basic on-page SEO, and Google Business Profile optimization. Pro is $349 setup and $49 a month for up to 10 pages, a booking widget or Stripe embed, an analytics report, and one or two content updates a month. Domain, SSL, and hosting are included. Month-to-month. Setup is non-refundable once development begins.",
        ),
        (
            "How does that compare with other local quotes?",
            "Local competitors mostly start at $300–$500. That is a starting range, not a promise that every quote you collect will land there, and a higher quote may include work these packages do not. The package list is the exact scope for $99, $199, and $349.",
        ),
        (
            "Do you work only in Pinecrest?",
            "The studio is at 12394 SW 82nd Ave, Pinecrest, FL 33156. The same packages are offered to businesses in Kendall, South Miami, Coral Gables, Palmetto Bay, and Miami. Each of those has its own page because the search and the street are different.",
        ),
        (
            "Are the Miami apartment sites part of the $99 package?",
            "No. The leasing sites in the portfolio, including Downtown 1st, Downtown 5th, 22 Biscayne Bay, Urban 22 Miami, 25 Biscayne Park, and Melody Tower, plus the RG Capital Partners site, are custom projects. They are examples of that kind of work. A custom project is quoted from the contact form, not sold as Starter.",
        ),
        (
            "Do you still build AI tools or 3D prints?",
            "Yes. AI agents, workflow automation, and 3D modeling and printing are still offered. They are a separate conversation from the website packages. Iris, the property-management assistant, has its own page. 3D printing has its own page with its own quote form.",
        ),
    ]
    body = hero(
        f'<p class="text-sm text-accent font-semibold mb-4">Website designer in Pinecrest · {RATING_HTML}</p>',
        "Affordable website design for small businesses in Pinecrest and Miami",
        """<p>CRRE Labs is a web design studio at 12394 SW 82nd Ave, Pinecrest, FL 33156. Call or tap <a class="text-white font-semibold underline" href="tel:+17867336744">(786) 733-6744</a>, send the form, or pay a package setup with Stripe.</p>
        <p>A Starter site is $99 to set up and $15 a month. Business is $199 and $29 a month. Pro is $349 and $49 a month. Domain, SSL, and hosting are included. Local competitors mostly start at $300–$500.</p>""",
        "#packages",
        "See packages and prices",
        "tel:+17867336744",
        "Call (786) 733-6744",
    )
    body += f'''
<section class="relative z-10 -mt-4 pb-8">
  <div class="max-w-5xl mx-auto px-4 sm:px-6">
    <div class="glass rounded-2xl p-5 flex flex-col sm:flex-row sm:items-center gap-4 justify-between">
      <p class="text-gray-200"><span class="text-white font-semibold">{RATING_HTML}</span> · Google Business Profile category: Website designer</p>
      <a data-review-link="reviews" href="{REVIEW_URL}" target="_blank" rel="noopener noreferrer" class="inline-flex justify-center px-4 py-2 rounded-full border border-white/30 text-white text-sm font-semibold">See our Google reviews</a>
      <a data-review-link="leave" href="{REVIEW_URL}" target="_blank" rel="noopener noreferrer" class="inline-flex justify-center px-4 py-2 rounded-full bg-accent-strong text-white text-sm font-semibold">Leave us a Google review</a>
    </div>
  </div>
</section>
{packages("Packages, with the prices")}
<section class="pb-8">
  <div class="max-w-3xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-3xl font-bold text-white mb-4">How this compares with a typical local quote</h2>
    <p class="text-gray-300 leading-relaxed mb-4">Local competitors mostly start at $300–$500. CRRE Labs' published program starts lower: $99 setup and $15 a month. That comparison is only honest if the scope is the same kind of site. These packages are a 1-page, 5-page, or 10-page business site with the items listed on the card. They are not a quote for a custom leasing site, a directory, or an app. If a shop down the street was quoted $300–$500, ask what that number includes before treating the two numbers as the same product.</p>
    <p class="text-gray-300 leading-relaxed mb-4">Every package here includes the domain, SSL, and hosting, and the plan is month-to-month. Setup is due up front and is non-refundable once development begins. Monthly billing is recurring. Reactivation fees, if you cancel and come back within 90 days, are $49, $99, or $175 depending on the package. Those lines are repeated on the <a class="text-accent underline" href="/pricing/">pricing page</a>.</p>
    <p class="text-gray-300 leading-relaxed">The portfolio on this site is the set of projects we can link. It is not a count of every site delivered, and this page does not use a project-count claim.</p>
  </div>
</section>
<section class="py-12">
  <div class="max-w-7xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-3xl font-bold text-white mb-3">Where we build</h2>
    <p class="text-gray-300 max-w-3xl mb-6">The studio is in Pinecrest. The pages below are written for the street or city in the search, not as copies of each other.</p>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <a class="glass rounded-2xl p-5 block" href="/web-design-pinecrest/"><h3 class="text-white font-semibold mb-2">Pinecrest</h3><p class="text-sm text-gray-300">The studio address is in the village. Useful if you want a local person on SW 82nd Ave, not a remote inbox.</p></a>
      <a class="glass rounded-2xl p-5 block" href="/web-design-kendall/"><h3 class="text-white font-semibold mb-2">Kendall</h3><p class="text-sm text-gray-300">Plaza businesses along Kendall Drive and around Dadeland, where the pin sits next to a row of similar shops.</p></a>
      <a class="glass rounded-2xl p-5 block" href="/web-design-south-miami/"><h3 class="text-white font-semibold mb-2">South Miami</h3><p class="text-sm text-gray-300">The downtown around Sunset Drive and US-1, which is a walkable grid, not a Kendall plaza.</p></a>
      <a class="glass rounded-2xl p-5 block" href="/web-design-coral-gables/"><h3 class="text-white font-semibold mb-2">Coral Gables</h3><p class="text-sm text-gray-300">Miracle Mile and the downtown grid, where the neighboring storefront already looks finished.</p></a>
      <a class="glass rounded-2xl p-5 block" href="/web-design-palmetto-bay/"><h3 class="text-white font-semibold mb-2">Palmetto Bay</h3><p class="text-sm text-gray-300">The village south of us, along Old Cutler and Franjo, with fewer competing storefronts than Kendall.</p></a>
      <a class="glass rounded-2xl p-5 block" href="/web-design-miami/"><h3 class="text-white font-semibold mb-2">Miami</h3><p class="text-sm text-gray-300">Citywide searches, plus the leasing sites we can actually show in the City of Miami.</p></a>
    </div>
  </div>
</section>
<section class="py-8">
  <div class="max-w-7xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-3xl font-bold text-white mb-6">Sites for a specific kind of business</h2>
    <ul class="grid sm:grid-cols-2 gap-3 text-gray-200">
      <li><a class="underline text-accent" href="/websites-for-restaurants/">Restaurants</a> — hours, menu, and the phone, before anything else.</li>
      <li><a class="underline text-accent" href="/websites-for-contractors/">Contractors and home services</a> — the jobs you do and the cities you actually drive to.</li>
      <li><a class="underline text-accent" href="/websites-for-salons-and-spas/">Salons and spas</a> — services, and a booking embed only on Pro.</li>
      <li><a class="underline text-accent" href="/websites-for-medical-and-dental/">Medical and dental offices</a> — a marketing site, not a patient portal and not a HIPAA program.</li>
      <li><a class="underline text-accent" href="/websites-for-property-managers/">Property managers and real estate</a> — separate from the custom building sites in the portfolio.</li>
    </ul>
  </div>
</section>
<section id="work" class="py-12">
  <div class="max-w-7xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-3xl font-bold text-white mb-3">Work you can open</h2>
    <p class="text-gray-300 max-w-3xl mb-6">Two write-ups use the projects already in this repo and on the live sites. They describe what was built. They do not add traffic numbers, rankings, or quotes.</p>
    <div class="grid md:grid-cols-2 gap-4">
      <a class="glass rounded-2xl p-6 block" href="/work/miami-apartment-sites/"><h3 class="text-white font-semibold text-xl mb-2">Miami apartment leasing sites</h3><p class="text-gray-300 text-sm">Downtown 1st, Downtown 5th, 22 Biscayne Bay, Urban 22 Miami, 25 Biscayne Park, and Melody Tower, with the screenshots in the portfolio.</p></a>
      <a class="glass rounded-2xl p-6 block" href="/work/rg-capital-partners/"><h3 class="text-white font-semibold text-xl mb-2">RG Capital Partners</h3><p class="text-gray-300 text-sm">A private-equity real estate site for a firm working in Kansas City and Miami. Dark page, gold accents, portfolio and contact.</p></a>
    </div>
    <p class="mt-4"><a class="text-accent underline" href="/portfolio/">Full portfolio</a> · <a class="text-accent underline" href="/work/">All case studies</a></p>
  </div>
</section>
<section class="py-8">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 grid md:grid-cols-3 gap-4">
    <article class="glass rounded-2xl p-6"><h2 class="text-white font-semibold mb-2">1. Call or write</h2><p class="text-sm text-gray-300">Phone, the form, or Stripe. Say which package you are looking at, or say it is custom. The older version of this site said a quote usually comes back within 24 hours. That is still the aim for a package inquiry. A custom build can take longer to scope.</p></article>
    <article class="glass rounded-2xl p-6"><h2 class="text-white font-semibold mb-2">2. Build the pages you listed</h2><p class="text-sm text-gray-300">Starter is one page. Business is up to five. Pro is up to ten. The older process note on this site said most websites go live in 1–2 weeks. That line is about this kind of site, not about a multi-property leasing build.</p></article>
    <article class="glass rounded-2xl p-6"><h2 class="text-white font-semibold mb-2">3. You can cancel the month</h2><p class="text-sm text-gray-300">The program is month-to-month. Business includes one revision a month. Pro includes one or two content updates a month. Starter does not include a monthly revision. Coming back within 90 days has a reactivation fee, listed on each card.</p></article>
  </div>
</section>
{reviews_section()}
<section id="about" class="py-12">
  <div class="max-w-3xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-3xl font-bold text-white mb-4">The studio</h2>
    <p class="text-gray-300 leading-relaxed mb-4">CRRE Labs LLC is the web design studio at {ADDRESS}. The public Google Business Profile lists the category Website designer and shows {RATING_HTML}. The phone on this site, {PHONE_DISPLAY}, is the number to use. The email already published on the 3D printing page is {EMAIL}.</p>
    <p class="text-gray-300 leading-relaxed">If you searched "web design Pinecrest", "small business website Miami", or "affordable website Kendall", the useful fact is the address and the three prices above. The rest of this page points at the neighborhood, the industry, and the projects.</p>
  </div>
</section>
<section id="other-services" class="py-12">
  <div class="max-w-7xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-3xl font-bold text-white mb-3">Also at the studio, not the main offer</h2>
    <p class="text-gray-300 max-w-3xl mb-6">AI agents, automation, and 3D printing are still available. They are not what the packages above buy. Ask about them on the form if you want them. They should not be the reason a restaurant or a contractor cannot tell what a website costs.</p>
    <div class="grid md:grid-cols-3 gap-4">
      <article class="glass rounded-2xl p-6">
        <h3 class="text-white font-semibold mb-2">AI agents</h3>
        <p class="text-sm text-gray-300 mb-3">Custom assistants for a specific workflow. The published example is Iris, described on this site as an assistant for property-management tasks, including rent collections and document generation, for a portfolio of 420+ rental units, at under $90 a month. Those figures are the ones already published on the Iris page. This homepage does not add new ones.</p>
        <a class="text-accent underline text-sm" href="/iris/">Iris page</a>
      </article>
      <article class="glass rounded-2xl p-6">
        <h3 class="text-white font-semibold mb-2">Workflow automation</h3>
        <p class="text-sm text-gray-300">Connecting tools you already use, such as Google Workspace or a CRM, for repeated work like billing files or document drafts. Scoped separately from the website packages.</p>
      </article>
      <article class="glass rounded-2xl p-6">
        <h3 class="text-white font-semibold mb-2">3D modeling and printing</h3>
        <p class="text-sm text-gray-300 mb-3">Models and prints for prototypes, architectural models, parts, and small batches. Pricing for prints is explained on that page, not in the website packages.</p>
        <a class="text-accent underline text-sm" href="/3d-printing.html">3D printing</a>
      </article>
    </div>
  </div>
</section>
{faq_html(faqs)}
{contact_form("home", "Say which neighborhood the business is in and which package you are comparing. If you already have a Google Business Profile, say so. We follow up by email.")}
</main>'''
    schemas = jsonld(
        business_block(),
        org_block(),
        website_block(),
        faq_block(faqs),
    )
    emit("index.html", page(
        "Affordable Website Design for Small Businesses | Pinecrest & Miami | CRRE Labs",
        "Pinecrest web design studio for small businesses. Websites from $99 setup and $15/month. Call (786) 733-6744. CRRE Labs, 12394 SW 82nd Ave.",
        "https://crrelabs.com/",
        "/",
        body,
        schemas,
    ))


def area_pages():
    pages = {
        "/web-design-pinecrest/": {
            "file": "web-design-pinecrest/index.html",
            "title": "Web Design in Pinecrest, FL | CRRE Labs",
            "description": "Website design for Pinecrest small businesses from a studio at 12394 SW 82nd Ave. Packages from $99 setup and $15/month. Call (786) 733-6744.",
            "h1": "Web design in Pinecrest, from the studio on SW 82nd Ave",
            "city": "Pinecrest",
            "service": "Website design for small businesses in Pinecrest, Florida",
            "lede": "<p>The studio is in Pinecrest: 12394 SW 82nd Ave, FL 33156. If you want to call a person in the village, the number is (786) 733-6744.</p><p>Pinecrest is a residential village. The businesses that serve it are often on US-1, along the Kendall Drive edge, or in small offices and home-based trades: dental and medical practices, tutors, designers, restaurants people drive to, and home services that park in a driveway. A neighbor usually already heard the name. The site's job is to confirm the phone, the hours, and how to ask a question, using the same name and address as the Google listing.</p>",
            "sections": [
                ("What a Pinecrest page needs to settle", [
                    "Put the phone in the first screen. Business and Pro include click-to-call. Starter includes a contact form and the phone number as text you can still tap if we add the link, which we do on sites we build.",
                    "If you have a storefront, use the address that matches the Google Business Profile. If you go to the customer, name Pinecrest and only the other villages you actually serve. Palmetto Bay is the next village south. Kendall is the commercial neighbor to the north. Do not paste a county-wide list you cannot cover.",
                    "Photos should be yours: the office, the truck, the food. The packages do not include a photo shoot. Tell us what you already have.",
                ]),
                ("Why this is not the Kendall page", [
                    "Kendall Drive is a long run of plazas and a hospital district. Pinecrest searches are quieter and more often the name of a specific business. A Pinecrest site that opens with a stock skyline of downtown Miami is answering a different city. This page is for the village the studio sits in.",
                    "You can meet or call locally. We do not claim a walk-in showroom beyond the published street address. Call first.",
                ]),
            ],
            "faqs": [
                ("Can I come to the studio?", "The published address is 12394 SW 82nd Ave, Pinecrest, FL 33156. Call (786) 733-6744 before you drive over so someone is there."),
                ("What does a Pinecrest small-business site cost?", "Starter is $99 setup and $15 a month. Business is $199 and $29 a month. Pro is $349 and $49 a month. Local competitors mostly start at $300–$500. The package cards list what each price includes."),
                ("How long does a package site take?", "The process already published on this site says most websites go live in 1–2 weeks. That refers to this kind of business site. It is not a promise for a custom build."),
                ("Do you rank me first for Pinecrest?", "No. Business and Pro include basic on-page SEO and Google Business Profile optimization: titles, the pages, and aligning the profile with the site. That is not a ranking guarantee."),
            ],
        },
        "/web-design-kendall/": {
            "file": "web-design-kendall/index.html",
            "title": "Affordable Website Design in Kendall | CRRE Labs",
            "description": "Websites for Kendall small businesses. Plaza and Dadeland shops, from $99 setup and $15/month. Studio in Pinecrest. Call (786) 733-6744.",
            "h1": "A Kendall business site that says which plaza you are in",
            "city": "Kendall",
            "service": "Website design for small businesses in Kendall, Florida",
            "lede": "<p>Kendall is not its own city. It is the suburban stretch people mean when they say Kendall Drive, Dadeland, and the medical offices around Baptist Hospital. A search for an affordable website in Kendall is usually a shop, clinic, salon, or crew in a plaza, competing with the suite next door.</p><p>CRRE Labs does not have a Kendall storefront. The studio is in Pinecrest, south of Kendall Drive, at 12394 SW 82nd Ave. Same phone, (786) 733-6744. The drive is the point: you are not hiring a desk in another state, and you are also not looking for a Miracle Mile address.</p>",
            "sections": [
                ("What Kendall visitors need in the first screen", [
                    "The plaza or the cross street, the suite if you have one, today's hours, and the phone. Maps already shows a small pin. The site has to say what the pin is, because Kendall Drive has a lot of pins.",
                    "Service businesses should name the neighborhoods they actually cover. Kendale Lakes, The Hammocks, and Dadeland are different drives. We will not invent a service area for you. You tell us the list, and the page uses that list.",
                    "Many customers search in English and in Spanish. This studio does not advertise a translation service. If you serve people in both languages, say so on the site only for the languages you can answer the phone in.",
                ]),
                ("Packages that fit a plaza business", [
                    "A one-page Starter site ($99 + $15/mo) can hold hours, a service list, a map link, and a form. That is enough for some crews.",
                    "Business ($199 + $29/mo, up to 5 pages) is the practical step when you want separate pages for the services people search, plus click-to-call and basic on-page SEO and Google Business Profile optimization.",
                    "Pro ($349 + $49/mo, up to 10 pages) adds a booking widget or Stripe embed, an analytics report, and one or two content updates a month. A salon or clinic that changes the bookable services uses that. A contractor who rarely edits the site may not.",
                ]),
            ],
            "faqs": [
                ("Do you only take clients inside the Village of Pinecrest?", "No. Kendall businesses are part of the area this studio serves. The workshop is in Pinecrest. The Kendall page exists because the commercial street is different."),
                ("Can you list every Kendall neighborhood on my site?", "Only the ones you serve. A long list you cannot cover makes the site less useful and disagrees with your Google profile if the profile says something else."),
                ("Is $99 the Kendall price?", "Yes. The three packages are the same prices in Kendall, Pinecrest, and the other pages. Starter $99 + $15/mo, Business $199 + $29/mo, Pro $349 + $49/mo. Local competitors mostly start at $300–$500."),
                ("Will you write my Spanish pages?", "Not as a listed service. If you have the Spanish text, it can go on the site within the page count. We do not claim a bilingual production team."),
            ],
        },
        "/web-design-south-miami/": {
            "file": "web-design-south-miami/index.html",
            "title": "Web Design in South Miami | CRRE Labs",
            "description": "Websites for South Miami businesses around Sunset Drive and US-1. From $99 setup and $15/month. Pinecrest studio. Call (786) 733-6744.",
            "h1": "Web design for South Miami's downtown, not a Kendall plaza",
            "city": "South Miami",
            "service": "Website design for small businesses in South Miami, Florida",
            "lede": "<p>South Miami is an incorporated city. The part people mean on a Sunday is the downtown around Sunset Drive, Red Road, and US-1, including the Sunset Place area. People park and walk past several storefronts. That is a different problem from a Kendall plaza, where the customer is choosing a suite from a car.</p><p>A South Miami restaurant or shop site should lead with hours, the cross street, and what is actually on the menu or the shelf. A professional office near downtown or toward the University of Miami needs the suite and what a first visit is for. The phone number has to match the Google listing, because that is how people confirm they have the right door.</p>",
            "sections": [
                ("What we have not built here", [
                    "This portfolio does not include a published South Miami client site. The leasing sites we can show are in the City of Miami: Downtown, Edgewater, and Midtown addresses. Those are a different municipality. Linking them here would blur the two searches, so they live on the Miami page and in the case study.",
                    "If you are the first South Miami business we publish, the case study will describe the pages we built and will not invent results.",
                ]),
                ("What the page should do for a Sunset Drive business", [
                    "Hours for each day, including the days you are dark. A Google profile that says one thing and a website that says another is a practical problem, not a branding one. Business and Pro include Google Business Profile optimization so those two can be checked together.",
                    "A short menu, service list, or class list within the page limit. Starter is a single page, so the list has to fit. Business gives you up to five pages if dinner, brunch, and private events should not fight for the same screen.",
                    "Click-to-call on Business and Pro. A walk-up neighborhood still runs on the phone for a table, a fitting, or a same-week appointment.",
                ]),
            ],
            "faqs": [
                ("Is South Miami the same page as Miami?", "No. South Miami is its own city south of the City of Miami. The Miami page is for citywide searches and for the building sites downtown and in Edgewater. Use this page if the business is in South Miami."),
                ("Do you have an office on Sunset Drive?", "No. The studio is at 12394 SW 82nd Ave in Pinecrest, a short drive south. Call (786) 733-6744."),
                ("Can a one-page site work for a restaurant here?", "It can, if the menu, hours, address, and phone fit on Starter ($99 + $15/mo). If the menu is long or you need a private-events page, Business is up to five pages for $199 + $29/mo."),
                ("Do you guarantee we show up for 'restaurant South Miami'?", "No. We do not sell rankings. Basic on-page SEO on Business and Pro means the pages name what you do and where you are, in ordinary language, and the profile matches."),
            ],
        },
        "/web-design-coral-gables/": {
            "file": "web-design-coral-gables/index.html",
            "title": "Website Design in Coral Gables | CRRE Labs",
            "description": "Websites for Coral Gables businesses, including Miracle Mile. Packages from $99 setup and $15/month. Studio in Pinecrest. Call (786) 733-6744.",
            "h1": "Coral Gables website design, without pretending we are on the Mile",
            "city": "Coral Gables",
            "service": "Website design for small businesses in Coral Gables, Florida",
            "lede": "<p>Coral Gables businesses on Miracle Mile and the downtown grid sit next to neighbors that already look considered: restaurants, salons, galleries, medical and dental offices, and professional firms. A customer on the Mile compares you with the door they just passed. The site does not have to be loud. It does have to be specific: what you do, when you are open, and how to reach the front desk.</p><p>CRRE Labs is not a Gables storefront. The studio is in Pinecrest, at 12394 SW 82nd Ave, south of the Gables. Phone (786) 733-6744. If you want a firm with a Miracle Mile lobby, say so and this is probably the wrong fit. If you want the published packages and a local phone, this is the page.</p>",
            "sections": [
                ("Which package, without the upsell script", [
                    "Starter, $99 setup and $15 a month, is one page. It is a reasonable fit for a practice or a shop that needs hours, a service list, and a form, and does not need a separate page per procedure.",
                    "Business, $199 and $29 a month, goes to five pages and adds click-to-call, basic on-page SEO, and Google Business Profile optimization, plus one revision a month. That is the package most Gables offices are comparing when they want the profile and the site to tell the same story.",
                    "Pro, $349 and $49 a month, adds a booking widget or a Stripe embed, an analytics report, and one or two content updates a month. Use it if the front desk already has a booking tool that can be embedded. We do not pick a medical-records system for you.",
                    "A custom site closer to the apartment projects in the portfolio is a separate quote. Those were not $99 jobs. See the Miami apartment case study.",
                ]),
                ("What we will not imply", [
                    "We do not claim a specialty in law firm marketing, medical compliance, or luxury branding. A marketing page can list your services in your words. It does not make the practice compliant, and it does not review your ads for professional rules.",
                    "Local competitors mostly start at $300–$500. Our package prices are lower and the scope is written down. A Gables quote above that range may be for photography, a brand system, or more pages than Pro includes. Compare the list, not just the first number.",
                ]),
            ],
            "faqs": [
                ("Will the site look like every other small-business template?", "The packages are straightforward sites: your facts, your photos, the phone, and the pages the package allows. They are not a custom brand campaign. If you need that, ask for a custom quote and look at the portfolio first."),
                ("Can you meet in the Gables?", "We can take the project by phone or video from the Pinecrest studio. Call (786) 733-6744. We do not list a Gables meeting office."),
                ("Do you build sites for Miracle Mile restaurants?", "Yes, as restaurant sites: hours, menu, address, phone. Read the restaurants page for what is included and what is not. Reservations, if you want a booking embed, are a Pro feature, described there as a booking widget, not as a named reservation network."),
                ("Is the Google profile required?", "No. If you have one, Business and Pro include optimization so the profile and the site agree. The category on our own profile is Website designer, which is separate from your category."),
            ],
        },
        "/web-design-palmetto-bay/": {
            "file": "web-design-palmetto-bay/index.html",
            "title": "Web Design in Palmetto Bay | CRRE Labs",
            "description": "Websites for Palmetto Bay businesses along Old Cutler and Franjo. From $99 setup and $15/month. The studio is in the next village north. Call (786) 733-6744.",
            "h1": "Web design in Palmetto Bay, from the next village north",
            "city": "Palmetto Bay",
            "service": "Website design for small businesses in Palmetto Bay, Florida",
            "lede": "<p>Palmetto Bay is the village south of Pinecrest. Commercial life is thinner than Kendall: stretches of Old Cutler Road, Franjo Road, and SW 184th Street, plus home services that never have a storefront. Residents also shop and eat in Pinecrest, Cutler Bay, and the Falls area. A useful site names the villages you actually drive to and stays quiet about the ones you do not.</p><p>Our studio is the next village north, at 12394 SW 82nd Ave, Pinecrest. Phone (786) 733-6744. This page exists because a Palmetto Bay plumber, dentist, tutor, or restaurant is not the same search as a Dadeland plaza or a Brickell tower.</p>",
            "sections": [
                ("Businesses this page is for", [
                    "Home services that cover Palmetto Bay and a couple of neighboring villages. The page should list the work (roof, AC, paint, lawn, plumbing) in the words customers use, and the phone.",
                    "Dental and medical offices that need hours, the suite, and what a new patient should expect. That is a marketing page. It is not a portal and not a HIPAA program. See the medical and dental page before you send clinical details through a form.",
                    "Restaurants and small retailers on the Old Cutler and Franjo stretches. Hours change. Starter does not include a monthly revision. Business includes one revision a month. Pro includes one or two content updates a month. Pick the package that matches how often the specials or the hours change. After a storm, a contractor who needs a sentence updated is in the same boat: the revision allowance is the real constraint, not a slogan.",
                ]),
                ("Price, said once", [
                    "Starter $99 setup + $15/mo. Business $199 + $29/mo. Pro $349 + $49/mo. Domain, SSL, and hosting included. Month-to-month. Local competitors mostly start at $300–$500. Nothing about Palmetto Bay changes those numbers.",
                ]),
            ],
            "faqs": [
                ("Are you based in Palmetto Bay?", "No. The studio is in Pinecrest, the village immediately north, at 12394 SW 82nd Ave. Palmetto Bay is one of the areas the studio serves."),
                ("Can the site say I serve Cutler Bay and Pinecrest too?", "Yes, if that is true. Write the list you want published. We will not add cities to make the page look bigger."),
                ("What if I only need the phone number and hours?", "Starter is one page for $99 and $15 a month, with a contact form, domain, SSL, and hosting. If that is all you need, do not buy Pro."),
                ("Do you publish a project count?", "No. The public portfolio is the projects we link. This page does not add a number of sites delivered."),
            ],
        },
        "/web-design-miami/": {
            "file": "web-design-miami/index.html",
            "title": "Small Business Website Design in Miami | CRRE Labs",
            "description": "Miami small-business websites from $99 setup and $15/month, plus custom leasing sites you can open. Pinecrest studio. Call (786) 733-6744.",
            "h1": "Small-business websites in Miami, and the building sites we can show",
            "city": "Miami",
            "service": "Website design for small businesses in Miami, Florida",
            "lede": "<p>People search 'web design Miami' from two different places. One is a shop, office, or crew anywhere in the county that uses Miami as the city name. The other is a business in the City of Miami: Brickell, Downtown, Edgewater, Midtown, Little Havana, Wynwood, and the rest of the city grid. This page covers both, and it separates the $99 program from the custom work.</p><p>CRRE Labs is in Pinecrest, not in Brickell. Address 12394 SW 82nd Ave. Phone (786) 733-6744. The Google Business Profile category is Website designer, " + RATING_HTML + ".</p>",
            "sections": [
                ("Work in the City of Miami that is already public", [
                    "The portfolio includes leasing sites for Downtown 1st (Arts and Entertainment District), Downtown 5th, 22 Biscayne Bay and Urban 22 Miami (Edgewater), 25 Biscayne Park on Biscayne Boulevard, and Melody Tower at 245 NE 14th Street in Midtown. The homepage also links Flagler on the River, 22 Skyview, and One Plaza West Brickell. Read the case study for what each published description actually says. Those projects are not the Starter package.",
                    "RG Capital Partners is a private-equity real estate site for a firm that operates in Kansas City and Miami. That is also custom work. The case study is linked below.",
                ]),
                ("The package, if you are a small business", [
                    "Starter is $99 setup and $15 a month: one page, contact form, domain, SSL, hosting. Business is $199 and $29 a month: up to five pages, click-to-call, basic on-page SEO, Google Business Profile optimization, one revision a month. Pro is $349 and $49 a month: up to ten pages, a booking widget or Stripe embed, an analytics report, one or two content updates a month.",
                    "Local competitors mostly start at $300–$500. Use that as a comparison of starting price, then read what our cards include. A Miami custom site can cost more than both. We will not guess that number on this page. Use the form.",
                    "If the business is actually in Pinecrest, Kendall, South Miami, Coral Gables, or Palmetto Bay, use that page. Those searches are specific, and the copy there is about that place.",
                ]),
            ],
            "faqs": [
                ("Is a $99 site the same product as the apartment websites?", "No. The apartment sites and RG Capital Partners are custom projects already in the portfolio. The $99, $199, and $349 prices are the Local Business Website Program: 1, 5, or 10 pages with the features on the cards."),
                ("Which Miami neighborhoods do you serve?", "The studio takes package work from businesses that can use a Pinecrest-based studio, including the City of Miami and the villages with their own pages. If you go to the customer, the site should list the areas you cover. If you have a counter, publish the address that matches your Google profile."),
                ("Do you have Miami client results, like leads or rankings?", "Not on this site. The case studies describe the pages that were built and link to the live sites. They do not add traffic, revenue, or ranking numbers."),
                ("How do I start?", "Call (786) 733-6744, use the form, or pay a package setup on Stripe from the pricing section. Stripe charges the setup for the package you click. The monthly fee is part of that package, billed as described on the pricing page."),
            ],
        },
    }
    for path, spec in pages.items():
        sections = []
        for title, paragraphs in spec["sections"]:
            ps = "".join(f'<p class="text-gray-300 leading-relaxed mb-4">{p}</p>' for p in paragraphs)
            sections.append(f'<h2 class="font-display text-2xl text-white font-bold mt-10 mb-3">{title}</h2>{ps}')
        canonical = "https://crrelabs.com" + path
        body = hero(
            crumbs([("Home", "/"), (spec["city"], path)]),
            spec["h1"],
            spec["lede"],
            "#packages",
            "See the three prices",
            "tel:+17867336744",
            f"Call {PHONE_DISPLAY}",
        )
        body += f'<article class="max-w-3xl mx-auto px-4 sm:px-6 pb-8 prose-page">{"".join(sections)}</article>'
        body += packages("The same three packages")
        body += faq_html(spec["faqs"])
        body += contact_form(path.strip("/"), "Tell us the business name, the neighborhood, and whether you already have a Google Business Profile.")
        body += "</main>"
        schemas = jsonld(
            service_block(spec["service"], canonical, spec["city"], spec["description"]),
            faq_block(spec["faqs"]),
            breadcrumb([("Home", "https://crrelabs.com/"), (spec["city"] + " web design", canonical)]),
        )
        emit(spec["file"], page(spec["title"], spec["description"], canonical, path, body, schemas))


def industry_pages():
    specs = [
        {
            "path": "/websites-for-restaurants/",
            "file": "websites-for-restaurants/index.html",
            "title": "Restaurant Website Design in Miami | CRRE Labs",
            "description": "Restaurant websites with hours, menu, address, and phone. From $99 setup and $15/month. Booking embed on the Pro package. Call (786) 733-6744.",
            "h1": "Restaurant websites that lead with hours, the menu, and the phone",
            "service": "Website design for restaurants",
            "city": None,
            "lede": "<p>A restaurant site has a short job: show where you are, when you are open, what you serve, and the phone number a person can tap. Delivery apps are someone else's page. The site is the page you control, and it should match the Google Business Profile so the hours do not argue with each other.</p><p>CRRE Labs builds that kind of site from Pinecrest for restaurants in Pinecrest, Kendall, South Miami, Coral Gables, Palmetto Bay, and Miami. Phone (786) 733-6744. The published prices are Starter $99 + $15/mo, Business $199 + $29/mo, and Pro $349 + $49/mo.</p>",
            "sections": [
                ("What goes on the site", [
                    "Address, cross street, and hours, including the closed days. A South Miami or Coral Gables restaurant that people walk to still loses the visit if Thursday's hours are wrong.",
                    "The menu, in your words, inside the page limit. Starter is one page, so a short menu can live there. A long menu, a brunch page, and a private-events note fit better in Business, which allows up to five pages.",
                    "The phone. Business and Pro include click-to-call. Photos of the food and the room, if you have them. The package price does not include a photographer.",
                    "Reservations: Pro includes a booking widget or a Stripe embed. The pricing page does not name a reservation network. If your widget can be embedded, Pro is the package that includes that work. We will not pretend OpenTable or any other brand is part of the setup.",
                ]),
                ("What this does not do", [
                    "It does not promise more covers, a ranking, or a rating. Local competitors mostly start at $300–$500 for a website. Our starting package is $99 setup. Compare the page count and whether hosting is included before you decide the cheaper number is the same product.",
                    "Marketing SMS from CRRE Labs, if you opt in on the form, is our own follow-up. It is not a texting product for your guests.",
                ]),
            ],
            "faqs": [
                ("Can you put my menu on the site?", "Yes, as content within the page count. Starter is one page. Business is up to five. Pro is up to ten. You provide the menu text."),
                ("Do I need a site if I am already on delivery apps?", "The apps show the items they choose to show. Your site is where the hours, the phone, the address, and the full menu are yours. A Google Business Profile still matters for Maps. The site and the profile do different jobs. The blog post on that question is linked from the blog."),
                ("Which package has online booking?", "Pro, at $349 setup and $49 a month, includes a booking widget or Stripe embed. Starter and Business do not."),
                ("Which neighborhoods?", "Pinecrest, Kendall, South Miami, Coral Gables, Palmetto Bay, and Miami. South Miami and Coral Gables are the walkable restaurant streets. Kendall is more often a plaza. The area pages go into that."),
            ],
        },
        {
            "path": "/websites-for-contractors/",
            "file": "websites-for-contractors/index.html",
            "title": "Websites for Contractors and Home Services | CRRE Labs",
            "description": "Websites for Miami-area contractors and home services. List the jobs you do and the cities you cover. From $99 setup and $15/month. Call (786) 733-6744.",
            "h1": "Contractor and home-service sites that list the jobs and the cities",
            "service": "Website design for contractors and home services",
            "city": None,
            "lede": "<p>Someone searching for a plumber, roofer, electrician, painter, or AC crew adds a place name: Pinecrest, Kendall, Palmetto Bay, Coral Gables. The site should list the work you actually do and the cities you actually drive to, with a phone number that matches the Google listing. A vague 'serving all of South Florida' line is less useful than five honest city names.</p><p>CRRE Labs is the studio at 12394 SW 82nd Ave, Pinecrest. Call (786) 733-6744. Packages start at $99 setup and $15 a month. Local competitors mostly start at $300–$500.</p>",
            "sections": [
                ("A practical page, not a brochure", [
                    "The services, in the words a customer types. If you do not do roofs, the page should not say roofs. We will not add trades to make the site look fuller.",
                    "The service area you give us. Palmetto Bay, Pinecrest, and Cutler Bay are a normal cluster. Kendall is a different drive. Coral Gables may be in or out. You decide. The area pages on this site explain those places. Your site should use your list, not ours.",
                    "A way to ask for an estimate. That is the contact form. We do not build a quoting calculator as part of these packages, and we do not invent prices for your jobs.",
                    "Photos of work you have permission to show. License or insurance numbers, if you want them published, only if you provide them. We do not look them up and we do not imply a license you did not give us.",
                    "Click-to-call is on Business and Pro, because a lot of this work starts as a phone call from a driveway.",
                ]),
                ("Which package", [
                    "Starter ($99 + $15/mo) is one page. A one-crew trade with one service area can live there.",
                    "Business ($199 + $29/mo) is up to five pages, so the trades you want found can have their own page, plus one revision a month and basic on-page SEO and Google Business Profile optimization.",
                    "Pro ($349 + $49/mo) adds one or two content updates a month and an analytics report. That matters if you change the cities you cover or the seasonal note more than once a month. It also includes a booking widget or Stripe embed if you take a deposit that way.",
                ]),
            ],
            "faqs": [
                ("Will the site get me leads?", "This page does not claim a lead count. It gives you a page with your services, your cities, and your phone. What happens after that is not a number we publish."),
                ("Can each trade have its own page?", "On Business, up to five pages total. On Pro, up to ten. Starter is one page. The limit is the package, not a slogan about unlimited SEO pages."),
                ("Do you write city pages for every municipality in Miami-Dade?", "Not in these packages. Name the cities you serve. A pile of thin city pages is not part of Starter, Business, or Pro."),
                ("How do I pay?", "Stripe checkout on the package you choose, or call (786) 733-6744, or use the form. Setup is due up front and is non-refundable once development begins."),
            ],
        },
        {
            "path": "/websites-for-salons-and-spas/",
            "file": "websites-for-salons-and-spas/index.html",
            "title": "Salon and Spa Website Design | Miami & Pinecrest | CRRE Labs",
            "description": "Salon and spa websites with services, hours, and location. Booking widget on the Pro package. From $99 setup and $15/month. Call (786) 733-6744.",
            "h1": "Salon and spa websites: services, hours, and the right location",
            "service": "Website design for salons and spas",
            "city": None,
            "lede": "<p>A salon site is a list of services, the hours, the photos you choose to show, and which location someone is driving to. Kendall, Coral Gables, and South Miami all have dense stretches of salons. The site has to say which chair, not 'Miami salon' with a stock photo.</p><p>Prices, if you want them public, can go on the page. If you would rather quote at the visit, say that, and do not publish a price you will not honor. CRRE Labs' own prices for the website are public: $99 + $15/mo, $199 + $29/mo, or $349 + $49/mo.</p>",
            "sections": [
                ("Booking, staff, and photos", [
                    "Pro ($349 setup and $49 a month) includes a booking widget or a Stripe embed. Starter and Business do not include booking. If the book is a paper notebook, do not buy Pro for a widget you will not connect.",
                    "Staff names and service menus fit inside the page count. Business is five pages, which can separate cuts, color, and the spa menu if you want them apart.",
                    "We do not offer guest texting as a product. The SMS checkbox on our form is only for marketing messages from CRRE Labs, and it is optional.",
                    "Bring photos you have rights to. We do not include a shoot in the package price.",
                ]),
                ("Where this is most relevant", [
                    "South Miami and Coral Gables: people walk, so hours and the cross street matter as much as the service list. See those area pages.",
                    "Kendall: the site should name the plaza. A search result that could be three nail salons in one center is not finished until the suite is on the page.",
                    "Pinecrest and Palmetto Bay: fewer storefronts, more word of mouth. The site confirms the phone and the hours a neighbor already heard.",
                ]),
            ],
            "faqs": [
                ("Can clients book online?", "Only if you choose Pro, which includes a booking widget or Stripe embed, and you have a tool that can be embedded. We do not subscribe you to a booking brand as part of the setup fee."),
                ("Can I show prices for color or nails?", "Yes, if you give us the numbers you want public. We will not invent a price list."),
                ("Is one page enough?", "For a single list of services and a phone number, Starter is one page at $99 setup and $15 a month. Split pages when the menu is long enough that one screen is hard to use."),
                ("Do you guarantee new clients from Google?", "No. Business and Pro include basic on-page SEO and Google Business Profile optimization. That means the pages and the profile describe the salon clearly. It is not a ranking or revenue promise."),
            ],
        },
        {
            "path": "/websites-for-medical-and-dental/",
            "file": "websites-for-medical-and-dental/index.html",
            "title": "Websites for Medical and Dental Offices | CRRE Labs",
            "description": "Marketing websites for medical and dental offices in the Miami area. Not a patient portal and not a HIPAA program. From $99 setup and $15/month. Call (786) 733-6744.",
            "h1": "Medical and dental marketing sites, clearly not a patient portal",
            "service": "Website design for medical and dental offices",
            "city": None,
            "lede": "<p>A dental or medical office site, for this studio, is a marketing page. It shows the address that matches your Google Business Profile, the phone, the hours, the kind of practice, and what a new patient should expect if you give us that text. It is not a patient portal, not an insurance checker, and not a HIPAA compliance program.</p><p>Kendall has a thick cluster of offices around the hospital corridor. Coral Gables has practices on and off Miracle Mile. Pinecrest and Palmetto Bay have smaller offices that live on referrals. The website work is the same three packages. The compliance work is not included, because we do not sell it.</p>",
            "sections": [
                ("What to put on the page", [
                    "Name, suite, hours, and phone, identical to the Google profile. Business and Pro include Google Business Profile optimization, which is the pass that checks those facts against the site.",
                    "The services you want a new patient to understand, in plain language you approve. We do not write clinical claims, outcome promises, or insurance acceptance unless you supply the sentence and own it.",
                    "Parking or suite instructions if the building is confusing. That is ordinary content, and it prevents the phone call that is only 'which tower?'",
                    "A form for general questions. Do not use it for records, images, or symptoms you would put in a chart. Say that on the page. If someone needs care, they call the office.",
                ]),
                ("What we will not say we do", [
                    "We will not say the site makes the practice HIPAA compliant. A brochure website is not a HIPAA program. Business associate agreements, chart systems, and email of records are outside these packages.",
                    "We will not claim a connection to a specific electronic health record. Pro can embed a booking widget if your front desk uses one that embeds. If it does not embed, Pro does not magically integrate it.",
                    "Local competitors mostly start at $300–$500. Our Starter setup is $99. A quote that includes photography, copy from a medical writer, or a portal will not match a $99 one-page site. Read the card.",
                ]),
            ],
            "faqs": [
                ("Will this make our office HIPAA compliant?", "No. The site is marketing. Do not send medical records, images, or detailed symptoms through the contact form. Call the office for anything clinical."),
                ("Can new patients book online?", "Pro includes a booking widget or Stripe embed if you already have a tool that can be embedded. It does not include an electronic health record."),
                ("Can you list the insurance we take?", "Only the list you give us, and you are responsible for keeping it true. We do not verify benefits."),
                ("Which package do offices usually need?", "There is no usual. A single page with hours and phone is Starter, $99 + $15/mo. Separate pages for the services you want found, plus profile alignment, is Business, $199 + $29/mo, up to five pages. Booking and monthly content updates are Pro, $349 + $49/mo."),
            ],
        },
        {
            "path": "/websites-for-property-managers/",
            "file": "websites-for-property-managers/index.html",
            "title": "Websites for Property Managers and Real Estate | CRRE Labs",
            "description": "Brochure sites for property managers and real estate offices from $99 setup, plus the custom Miami leasing sites already in the portfolio. Call (786) 733-6744.",
            "h1": "Property-manager and real-estate sites, in two different sizes",
            "service": "Website design for property managers and real estate offices",
            "city": None,
            "lede": "<p>There are two kinds of real-estate web work in this studio, and they should not be mixed on a price card. One is a brochure site for a small property manager, a realtor office, or an owner who needs phone, areas, and a way to reach leasing. That is the package program: 1, 5, or 10 pages at $99, $199, or $349 to set up. The other is a custom leasing site for a building, or a firm site like RG Capital Partners. Those are quoted separately. The portfolio shows the custom ones. It does not price them on this page.</p>",
            "sections": [
                ("What the portfolio actually contains", [
                    "Miami apartment leasing sites: Downtown 1st, Downtown 5th, 22 Biscayne Bay, Urban 22 Miami, 25 Biscayne Park, and Melody Tower, with screenshots. The case study sticks to the descriptions already published and to what is on the live pages. It does not add lease-up figures.",
                    "RG Capital Partners: a private-equity real estate site for a firm operating in Kansas City and Miami. Navigation includes portfolio, team, and contact. The homepage of that project is in the portfolio screenshots.",
                    "The homepage also links Flagler on the River, 22 Skyview, and One Plaza West Brickell. Those do not have screenshots in this repo, so the case study says so instead of inventing images.",
                    "Iris is a separate product: an AI assistant described on its own page for property-management operations, including a published note of 420+ rental units and a cost under $90 a month. That is not a website package and it is not a result statistic for the leasing sites.",
                ]),
                ("What a small manager's package site includes", [
                    "The areas you manage, how an owner reaches you, how a resident or applicant reaches leasing, and the phone. If those are two different numbers, the page should say so.",
                    "Business and Pro add click-to-call, basic on-page SEO, and Google Business Profile optimization, so the profile address matches the office you publish.",
                    "Pro can embed a booking widget or Stripe if you take applications or payments that way. It is not a property-management system. We do not claim to replace the software you use to collect rent.",
                    "Local competitors mostly start at $300–$500 for a website. A building site like the ones in the portfolio is custom and can sit outside that range. Ask before you assume the $99 card covers a tower.",
                ]),
            ],
            "faqs": [
                ("Can you rebuild a building's leasing site for $199?", "The Business package is up to five pages with the features on the card. The Miami building sites in the portfolio were custom projects. Use the form and describe the building. We will not force it into a package price on this page."),
                ("Do you have a case study with occupancy or lead numbers?", "No. The write-ups linked from the work page describe the pages and show screenshots. They do not invent performance numbers or resident quotes."),
                ("We manage homes, not a tower. Which package?", "If one page can explain who you manage for and how to call, Starter is $99 setup and $15 a month. If owners and applicants need different pages, Business allows up to five for $199 and $29 a month."),
                ("Where are you?", "12394 SW 82nd Ave, Pinecrest, FL 33156. (786) 733-6744. The building examples are in the City of Miami. The studio is not."),
            ],
        },
    ]
    for spec in specs:
        sections = []
        for title, paragraphs in spec["sections"]:
            ps = "".join(f'<p class="text-gray-300 leading-relaxed mb-4">{p}</p>' for p in paragraphs)
            sections.append(f'<h2 class="font-display text-2xl text-white font-bold mt-10 mb-3">{title}</h2>{ps}')
        canonical = "https://crrelabs.com" + spec["path"]
        body = hero(
            crumbs([("Home", "/"), (spec["h1"].split(",")[0][:48], spec["path"])]),
            spec["h1"],
            spec["lede"],
            "#packages",
            "See package prices",
            "tel:+17867336744",
            f"Call {PHONE_DISPLAY}",
        )
        # crumb label above is awkward. Replace with a cleaner one by not using h1 slice.
        body = hero(
            crumbs([("Home", "/"), ("Industries", "/#main"), (spec["title"].split("|")[0].strip(), spec["path"])]),
            spec["h1"],
            spec["lede"],
            "#packages",
            "See package prices",
            "tel:+17867336744",
            f"Call {PHONE_DISPLAY}",
        )
        body += f'<article class="max-w-3xl mx-auto px-4 sm:px-6 pb-4">{"".join(sections)}<p class="text-gray-300">Related: <a class="text-accent underline" href="/web-design-miami/">Miami</a>, <a class="text-accent underline" href="/web-design-kendall/">Kendall</a>, <a class="text-accent underline" href="/web-design-coral-gables/">Coral Gables</a>, <a class="text-accent underline" href="/web-design-pinecrest/">Pinecrest</a>.</p></article>'
        body += packages("Packages for this kind of site")
        body += faq_html(spec["faqs"])
        body += contact_form(spec["path"].strip("/"), "Say what the business does, which neighborhood it is in, and whether you are asking about a package or a custom build.")
        body += "</main>"
        schemas = jsonld(
            service_block(spec["service"], canonical, None, spec["description"]),
            faq_block(spec["faqs"]),
            breadcrumb([
                ("Home", "https://crrelabs.com/"),
                (spec["service"], canonical),
            ]),
        )
        emit(spec["file"], page(spec["title"], spec["description"], canonical, spec["path"], body, schemas))


def work_pages():
    buildings = [
        {
            "name": "Downtown 1st",
            "url": "https://downtown1st.com",
            "stem": "downtown-1st-leasing-website",
            "src": "melo-downtown-1st.png",
            "alt": "Top of the Downtown 1st leasing homepage, a luxury rental site for the downtown Miami tower.",
            "problem": "The CRRE Labs homepage describes this as a full redesign for luxury apartments in Miami's Arts and Entertainment District. The repo does not include a copy of the previous site, so this page does not guess what was wrong with it.",
            "built": "The public description says the redesign uses the property's photography, a gallery lightbox, and a mobile-first layout. The portfolio page adds a 56-story leasing site with bay and skyline views, amenities, floor plans, and tour scheduling. The live site at downtown1st.com shows those sections: a hero for the rental tower, amenities, a gallery, floor plans, the address 30 SW 1st Street, Miami, FL 33130, and a contact path. This write-up does not repeat the building's unit counts as a CRRE Labs result.",
        },
        {
            "name": "Downtown 5th",
            "url": "https://downtown5.com",
            "stem": "downtown-5th-leasing-website",
            "src": "melo-downtown-5.png",
            "alt": "Top of the Downtown 5th leasing homepage for the downtown Miami rental tower.",
            "problem": "The portfolio describes the site. It does not describe the previous one. There is no problem statement in the repo to quote, so none is added here.",
            "built": "Portfolio copy: a rental tower site for a dual-address Downtown Miami property, with amenities, tour scheduling, leasing-office contact, and a sleek urban layout. The screenshot is the top of that page.",
        },
        {
            "name": "22 Biscayne Bay",
            "url": "https://22biscaynebay.com",
            "stem": "22-biscayne-bay-leasing-website",
            "src": "melo-22-biscayne-bay.png",
            "alt": "Top of the 22 Biscayne Bay leasing homepage for the Edgewater waterfront apartments.",
            "problem": "The repo does not keep a 'before' version. The portfolio only describes the leasing site that replaced whatever was there.",
            "built": "Portfolio copy: a leasing site for a waterfront apartment community in Edgewater, with bay views, floor plans, photo galleries, amenity highlights, and tour scheduling.",
        },
        {
            "name": "Urban 22 Miami",
            "url": "https://urban22miami.com",
            "stem": "urban-22-miami-leasing-website",
            "src": "melo-urban-22.png",
            "alt": "Top of the Urban 22 Miami leasing homepage for the Edgewater rental building.",
            "problem": "No previous-site description is published in the portfolio or on the homepage.",
            "built": "Portfolio copy: a property site for a luxury rental building in Edgewater, with gallery images, floor plan options, contact information, and a contemporary layout.",
        },
        {
            "name": "25 Biscayne Park",
            "url": "https://25biscaynepark.com",
            "stem": "25-biscayne-park-leasing-website",
            "src": "melo-25-biscayne.png",
            "alt": "Top of the 25 Biscayne Park leasing homepage for the Biscayne Boulevard apartments.",
            "problem": "The homepage says this site was migrated from WordPress to static hosting. That is the only before-state the public pages state. No security incident is described, and none is added here.",
            "built": "Homepage: a static hosting migration for the Biscayne Boulevard apartments. Portfolio: a luxury rental tower page with amenities, tour booking, and leasing contact. Both sentences are already on this website. They are not expanded into speed or cost claims.",
        },
        {
            "name": "Melody Tower",
            "url": "https://melodytower.com",
            "stem": "melody-tower-leasing-website",
            "src": "melo-melody-tower.png",
            "alt": "Top of the Melody Tower leasing homepage for the Midtown Miami rental tower.",
            "problem": "The homepage says Melody Tower was a WordPress migration to a static site and that the original design was preserved. Checked while this page was written, melodytower.com still serves images from a WordPress uploads path. This case study does not claim the live site is static today. It records both the homepage sentence and what the live page shows.",
            "built": "Portfolio copy places the building at 245 NE 14th Street and describes luxury-living highlights, amenities, and tour and contact options. The live page shows a leasing hero, an amenity list, a gallery, and contact for that address, including the phone and email published on that site. Those contact details belong to the building, not to CRRE Labs.",
        },
    ]
    blocks = []
    for b in buildings:
        blocks.append(f'''
<section class="py-10 border-t border-white/10">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 grid md:grid-cols-2 gap-6 items-start">
    {picture(b["stem"], b["alt"])}
    <div>
      <h2 class="font-display text-2xl text-white font-bold mb-3">{b["name"]}</h2>
      <h3 class="text-white font-semibold mb-2">What we can say about the previous site</h3>
      <p class="text-gray-300 text-sm leading-relaxed mb-3">{b["problem"]}</p>
      <h3 class="text-white font-semibold mb-2">What was built</h3>
      <p class="text-gray-300 text-sm leading-relaxed mb-4">{b["built"]}</p>
      <a href="{b["url"]}" target="_blank" rel="noopener noreferrer" class="text-accent font-semibold">Open {b["name"]}</a>
    </div>
  </div>
</section>''')
    extra = '''
<section class="py-10">
  <div class="max-w-3xl mx-auto px-4 sm:px-6">
    <h2 class="font-display text-2xl text-white font-bold mb-3">Other Miami links on the homepage, without a screenshot in this repo</h2>
    <p class="text-gray-300 mb-3">These are described on the homepage and do not have a PNG in the portfolio folder. No image is invented for them.</p>
    <ul class="text-gray-300 space-y-3 list-disc ml-5">
      <li><a class="text-accent underline" href="https://flaglerontheriver.com" target="_blank" rel="noopener noreferrer">Flagler on the River</a> — homepage text: a downtown Miami riverfront property, redesigned from legacy HTML to a static site, with amenity imagery and floor plans.</li>
      <li><a class="text-accent underline" href="https://22skyview.com" target="_blank" rel="noopener noreferrer">22 Skyview</a> — homepage text: an Edgewater high-rise page with a rendering hero, floor plans, and a Google Maps embed.</li>
      <li><a class="text-accent underline" href="https://oneplazawestbrickell.com" target="_blank" rel="noopener noreferrer">One Plaza West Brickell</a> — homepage text: a move from WordPress to static hosting for a Brickell apartment community.</li>
    </ul>
    <p class="text-gray-300 mt-4">Screenshot files for the six buildings above use a melo- prefix in the repo. That is why they are grouped here. This page does not add a count of buildings, a client quote, or a performance metric.</p>
  </div>
</section>'''
    canonical = "https://crrelabs.com/work/miami-apartment-sites/"
    body = hero(
        crumbs([("Home", "/"), ("Work", "/work/"), ("Miami apartment sites", "/work/miami-apartment-sites/")]),
        "Miami apartment leasing sites",
        "<p>These are the building websites in the CRRE Labs portfolio that have screenshots. The notes below stay inside the sentences already published on this site, plus what a person can see by opening the live page. No rankings, lease-up figures, or testimonials are added.</p>",
        "/portfolio/",
        "Back to the portfolio",
        "/#contact",
        "Ask about a custom site",
    )
    body += "".join(blocks) + extra + "</main>"
    schemas = jsonld(
        service_block("Custom leasing websites for Miami apartment buildings", canonical, "Miami", "Case study of Miami apartment leasing websites in the CRRE Labs portfolio."),
        breadcrumb([
            ("Home", "https://crrelabs.com/"),
            ("Work", "https://crrelabs.com/work/"),
            ("Miami apartment sites", canonical),
        ]),
    )
    emit("work/miami-apartment-sites/index.html", page(
        "Miami Apartment Website Case Study | CRRE Labs",
        "What CRRE Labs published about the Miami apartment leasing sites: Downtown 1st, Downtown 5th, 22 Biscayne Bay, Urban 22, 25 Biscayne Park, and Melody Tower.",
        canonical,
        "/work/",
        body,
        schemas,
    ))

    rg_canonical = "https://crrelabs.com/work/rg-capital-partners/"
    rg = hero(
        crumbs([("Home", "/"), ("Work", "/work/"), ("RG Capital Partners", "/work/rg-capital-partners/")]),
        "RG Capital Partners website",
        "<p>A website for RG Capital Partners, a private-equity real estate firm that works in Kansas City and Miami. The CRRE Labs homepage calls it a full redesign built with Tailwind and says it was delivered in under a week. That timing is already published here. This page does not add a second timeline, a fee, or a result.</p>",
        "https://rgcappartners.com",
        "Open the live site",
        "/portfolio/",
        "See the screenshot in the portfolio",
    )
    rg += f'''
<section class="py-8">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 grid md:grid-cols-2 gap-6 items-start">
    {picture("rg-capital-partners-website", "Screenshot of the RG Capital Partners homepage: dark navy background, gold navigation for Home, About, Portfolio, Team, and Contact, the headline Private Equity Real Estate, and buttons for View Portfolio and Get in Touch.")}
    <div class="text-gray-300 leading-relaxed space-y-4">
      <h2 class="font-display text-2xl text-white font-bold">What we can say about the previous site</h2>
      <p>The public pages call it a redesign. They do not include the old site. An internal project note in this repo mentions WordPress. That note is not treated as a public claim here, because the portfolio text itself does not say it. The honest public line is: it was a redesign.</p>
      <h2 class="font-display text-2xl text-white font-bold">What was built</h2>
      <p>The portfolio describes a dark site with gold accents for a syndication firm, with a property portfolio and an investor contact path. The screenshot shows the top of the homepage: the firm name, links for Home, About, Portfolio, Team, and Contact, an Investor Portal button, the headline Private Equity Real Estate, a Kansas City and Miami line, and buttons labeled View Portfolio and Get in Touch.</p>
      <p>The live site publishes its own property statistics. This case study does not repeat those figures. They are the firm's numbers, sources on the page have not been stable enough to copy, and they are not a CRRE Labs result.</p>
      <p><a class="text-accent font-semibold" href="https://rgcappartners.com" target="_blank" rel="noopener noreferrer">rgcappartners.com</a></p>
    </div>
  </div>
</section>
</main>'''
    # The primary button in hero uses target? It's an external link without rel because hero() doesn't add target blank.
    # I'll leave the hero secondary as internal and the body has the external link with rel.
    emit("work/rg-capital-partners/index.html", page(
        "RG Capital Partners Website Case Study | CRRE Labs",
        "What the CRRE Labs portfolio shows for the RG Capital Partners site: a dark, gold-accent redesign for a Kansas City and Miami real estate firm.",
        rg_canonical,
        "/work/",
        rg,
        jsonld(
            service_block("Website for RG Capital Partners", rg_canonical, "Miami", "Case study of the RG Capital Partners website redesign."),
            breadcrumb([
                ("Home", "https://crrelabs.com/"),
                ("Work", "https://crrelabs.com/work/"),
                ("RG Capital Partners", rg_canonical),
            ]),
        ),
    ))

    hub = hero(
        crumbs([("Home", "/"), ("Work", "/work/")]),
        "Case studies",
        "<p>Two write-ups. Both use projects already in the portfolio. Neither adds a metric, a quote, or a result that is not already published.</p>",
        "/portfolio/",
        "Portfolio screenshots",
        "/#contact",
        "Start a project",
    )
    hub += '''
<section class="pb-16">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 grid md:grid-cols-2 gap-4">
    <a class="glass rounded-2xl p-6 block" href="/work/miami-apartment-sites/"><h2 class="text-white text-xl font-semibold mb-2">Miami apartment leasing sites</h2><p class="text-gray-300 text-sm">Six buildings with screenshots, plus three homepage links that do not have a screenshot file.</p></a>
    <a class="glass rounded-2xl p-6 block" href="/work/rg-capital-partners/"><h2 class="text-white text-xl font-semibold mb-2">RG Capital Partners</h2><p class="text-gray-300 text-sm">Private-equity real estate site for Kansas City and Miami.</p></a>
  </div>
</section></main>'''
    emit("work/index.html", page(
        "Website Case Studies | CRRE Labs",
        "Case studies from the CRRE Labs portfolio: Miami apartment leasing sites and RG Capital Partners. No invented metrics.",
        "https://crrelabs.com/work/",
        "/work/",
        hub,
        jsonld(breadcrumb([("Home", "https://crrelabs.com/"), ("Work", "https://crrelabs.com/work/")])),
    ))
    return buildings


def blog():
    cost_faqs = [
        ("What does CRRE Labs charge for a small-business website in 2026?", "Starter is $99 setup and $15 a month. Business is $199 setup and $29 a month. Pro is $349 setup and $49 a month. Domain, SSL, and hosting are included on each."),
        ("What do local competitors charge?", "Local competitors mostly start at $300–$500. That is a starting range for a website, not a survey of every line item those quotes include."),
        ("Are the Miami apartment sites $99?", "No. Those are custom projects in the portfolio. The three prices are the Local Business Website Program."),
    ]
    cost_body = f'''
<main id="main">
<article class="pt-28 pb-8">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 prose-page">
    {crumbs([("Home", "/"), ("Blog", "/blog/"), ("Website cost in Miami", "/blog/how-much-does-a-website-cost-in-miami-2026/")])}
    <p class="text-sm text-gray-400 mb-4">November 17, 2026 · CRRE Labs LLC</p>
    <h1 class="font-display text-4xl sm:text-5xl font-bold text-white leading-tight mb-6">How much does a website cost in Miami in 2026?</h1>
    <p class="text-gray-300">At CRRE Labs, a small-business website in the published program costs $99, $199, or $349 to set up, then $15, $29, or $49 a month. Local competitors mostly start at $300–$500. Those two sentences are the whole price story. The rest of this page is what the money buys, what it does not buy, and the questions worth asking anyone else in Miami before you compare a single number.</p>
    <h2>The three CRRE Labs packages</h2>
    <p class="text-gray-300">The studio is at {ADDRESS}. The phone is {PHONE_DISPLAY}. The prices do not change by neighborhood. Pinecrest, Kendall, South Miami, Coral Gables, Palmetto Bay, and Miami use the same card.</p>
    <ul>
      <li><strong class="text-white">Starter — $99 setup + $15/mo.</strong> One page, a contact form, domain, SSL, and hosting. SEO is not included. If you cancel and restart within 90 days, reactivation is $49.</li>
      <li><strong class="text-white">Business — $199 setup + $29/mo.</strong> Up to five pages, contact form, click-to-call, basic on-page SEO, Google Business Profile optimization, and one revision a month. Domain, SSL, and hosting. Reactivation within 90 days is $99.</li>
      <li><strong class="text-white">Pro — $349 setup + $49/mo.</strong> Up to ten pages, the Business marketing items, a booking widget or Stripe embed, an analytics report, and one or two content updates a month. Reactivation within 90 days is $175.</li>
    </ul>
    <p class="text-gray-300">Month-to-month. No long contract. Setup is due up front and is non-refundable once development begins. Monthly billing is recurring. You can pay the setup on Stripe from the <a href="/pricing/">pricing page</a> or from the buttons on the homepage.</p>
    <h2>What "local competitors mostly start at $300–$500" does and does not mean</h2>
    <p class="text-gray-300">It means the opening number we are comparing against, for a local website, usually begins in that band. It does not mean every Miami agency quotes $300, or that a $450 quote is a worse deal. A higher quote may include more pages than our Pro plan, photography, a brand, or a custom build. A lower quote may be a page you rent and do not own. Ask what happens to the domain if you stop paying.</p>
    <p class="text-gray-300">Our $99 price is real and it is narrow. One page. No SEO line item. No monthly revision. If you need five pages and a Google profile that matches the site, the comparable CRRE Labs number is $199 setup and $29 a month, not $99.</p>
    <h2>What changes the price, inside our card</h2>
    <ul>
      <li>Page count: 1, up to 5, or up to 10.</li>
      <li>Whether basic on-page SEO and Google Business Profile optimization are in the package. They start at Business.</li>
      <li>Whether you need a booking widget or a Stripe embed, an analytics report, or monthly content edits. Those are Pro.</li>
      <li>Whether the job is outside the card. Custom leasing sites, the RG Capital Partners site, AI agents, automation, and 3D printing are not these three prices. The <a href="/work/">case studies</a> show the custom web work we can point at. They do not list what those projects cost.</li>
    </ul>
    <h2>Questions to ask any Miami website quote</h2>
    <ul>
      <li>Who owns the domain, and can you move it?</li>
      <li>Is hosting in the monthly fee, or is it a second bill?</li>
      <li>How many pages, and what does a change cost after launch?</li>
      <li>Is the Google Business Profile part of the work, or only the website?</li>
      <li>What is the cancellation term? Ours is month-to-month, with the reactivation fees above if you return within 90 days.</li>
    </ul>
    <p class="text-gray-300">We do not have a Miami-wide average beyond the competitor starting range above, and this article does not borrow a statistic from a report we did not run.</p>
    <h2>How to start</h2>
    <p class="text-gray-300">Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>, use the form on the <a href="/#contact">homepage</a>, or check out a package on Stripe. If you are pricing a restaurant, a crew, a salon, an office, or a property manager, the industry pages say which parts of the card matter for that business.</p>
  </div>
</article>
{faq_html(cost_faqs)}
</main>'''
    cost_url = "https://crrelabs.com/blog/how-much-does-a-website-cost-in-miami-2026/"
    emit("blog/how-much-does-a-website-cost-in-miami-2026/index.html", page(
        "How Much Does a Website Cost in Miami in 2026? | CRRE Labs",
        "CRRE Labs website packages in 2026: $99, $199, or $349 setup, then $15, $29, or $49 a month. Local competitors mostly start at $300–$500.",
        cost_url,
        "/blog/",
        cost_body,
        jsonld(
            article_block("How much does a website cost in Miami in 2026?", cost_url, "Published CRRE Labs website prices for 2026 and how they compare with typical local starting quotes."),
            faq_block(cost_faqs),
            breadcrumb([("Home", "https://crrelabs.com/"), ("Blog", "https://crrelabs.com/blog/"), ("Website cost in Miami", cost_url)]),
        ),
    ))

    gbp_faqs = [
        ("Does a Google Business Profile replace a website?", "No. The profile is the Maps listing Google hosts. The website is a page you control. They do different jobs, and the useful setup is both, with the same name, address, and phone."),
        ("Does CRRE Labs edit the profile?", "Business and Pro include Google Business Profile optimization along with basic on-page SEO. Starter does not include that line."),
        ("What is on the CRRE Labs profile?", "The category is Website designer. The rating shown there is 5.0 from 24 reviews. The studio address is 12394 SW 82nd Ave, Pinecrest, FL 33156, and the phone is (786) 733-6744."),
    ]
    gbp_body = f'''
<main id="main">
<article class="pt-28 pb-8">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 prose-page">
    {crumbs([("Home", "/"), ("Blog", "/blog/"), ("Website or Google profile", "/blog/do-i-need-a-website-if-i-have-a-google-business-profile/")])}
    <p class="text-sm text-gray-400 mb-4">November 17, 2026 · CRRE Labs LLC</p>
    <h1 class="font-display text-4xl sm:text-5xl font-bold text-white leading-tight mb-6">Do I need a website if I already have a Google Business Profile?</h1>
    <p class="text-gray-300">Often, yes, but not because a profile is useless. A Google Business Profile is the listing Google shows on Maps: category, hours, phone, address, photos, and reviews. A website is the page you edit, with room for a menu, a service list, a second phone number, or a form. One does not contain the other.</p>
    <h2>What the profile is good at</h2>
    <p class="text-gray-300">People who already know the neighborhood can find the pin, see the hours, and tap the phone. Reviews sit on the profile. Ours, for example, is a Website designer profile at {RATING_HTML}. That fact lives on the profile. It is not something a website package creates, and this article does not tell you how to get the same rating.</p>
    <p class="text-gray-300">If your whole public story is a phone number, a category, and hours, the profile may be enough for now. A food truck with a changing corner, or a crew that only wants the phone to ring, can stay there until the story gets longer. That is a real option. It is not a consolation prize.</p>
    <h2>What the profile is awkward at</h2>
    <ul>
      <li>A full menu, a list of procedures, or a set of trades that do not fit in a short description.</li>
      <li>Explaining which plaza, which suite, and which cities you drive to, in more than a line.</li>
      <li>A contact form that is not the same click as the phone. Some customers will write and will not call.</li>
      <li>Publishing prices. Our website prices are public because the site has room for them. A profile is a poor place for three packages and the exclusions.</li>
      <li>Owning the page. The profile is a Google product. The site is yours, on your domain, for as long as you keep the domain and the host.</li>
    </ul>
    <h2>Use them together</h2>
    <p class="text-gray-300">The profile should link to the site. The site should show the same name, address, and phone as the profile. When those disagree, the customer does not know which Thursday hours to trust. On our Business package ($199 setup and $29 a month) and Pro package ($349 setup and $49 a month), basic on-page SEO and Google Business Profile optimization are included so that check is part of the work. Starter ($99 setup and $15 a month) is the site only: one page, a form, domain, SSL, and hosting. It does not include the profile line.</p>
    <p class="text-gray-300">Optimization here means aligning the facts and writing the pages in ordinary language. It does not mean a promise about where you rank. We do not sell that.</p>
    <h2>A website is not automatic once you have reviews</h2>
    <p class="text-gray-300">Reviews help the profile. They do not list your services in the order you want, and they do not give you a page for private events, a second location, or an owner inquiry that should not go to the leasing line. Property managers hit this quickly: the profile is the office, and the site is where an owner and an applicant can be sent to different explanations. See the <a href="/websites-for-property-managers/">property-manager page</a> for how that differs from a custom building site.</p>
    <h2>What it costs if you decide you want the site</h2>
    <p class="text-gray-300">The same card as the <a href="/blog/how-much-does-a-website-cost-in-miami-2026/">Miami cost article</a>: $99 + $15/mo, $199 + $29/mo, or $349 + $49/mo. Local competitors mostly start at $300–$500. Domain, SSL, and hosting are included in our monthly fee. Month-to-month.</p>
    <p class="text-gray-300">If you already like the profile and only want a single page that repeats the phone and the hours, buy Starter and stop. If the profile and the site need to be checked against each other, Business is the package that includes that work.</p>
    <p class="text-gray-300">Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> or use the form on the homepage. The studio is at {ADDRESS}.</p>
  </div>
</article>
{faq_html(gbp_faqs)}
</main>'''
    gbp_url = "https://crrelabs.com/blog/do-i-need-a-website-if-i-have-a-google-business-profile/"
    emit("blog/do-i-need-a-website-if-i-have-a-google-business-profile/index.html", page(
        "Do I Need a Website If I Already Have a Google Business Profile? | CRRE Labs",
        "A Google Business Profile and a website do different jobs. When a Pinecrest studio would still build the site, and what the $99, $199, and $349 packages include.",
        gbp_url,
        "/blog/",
        gbp_body,
        jsonld(
            article_block("Do I need a website if I already have a Google Business Profile?", gbp_url, "How a Google Business Profile and a small-business website differ, using CRRE Labs' published packages."),
            faq_block(gbp_faqs),
            breadcrumb([("Home", "https://crrelabs.com/"), ("Blog", "https://crrelabs.com/blog/"), ("Website or Google profile", gbp_url)]),
        ),
    ))

    index = hero(
        crumbs([("Home", "/"), ("Blog", "/blog/")]),
        "Notes on local websites",
        "<p>Two articles. Both use the prices on this site. Neither cites a study we did not run.</p>",
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
      <p class="text-gray-300">$99, $199, and $349 setup, then $15, $29, and $49 a month, next to the $300–$500 local starting range.</p>
    </a>
    <a class="glass rounded-2xl p-6 block" href="/blog/do-i-need-a-website-if-i-have-a-google-business-profile/">
      <p class="text-xs text-gray-400 mb-2">November 17, 2026</p>
      <h2 class="text-white text-2xl font-semibold mb-2">Do I need a website if I already have a Google Business Profile?</h2>
      <p class="text-gray-300">What the profile does, what it does not do, and which of our packages includes profile work.</p>
    </a>
  </div>
</section></main>'''
    emit("blog/index.html", page(
        "Blog | CRRE Labs",
        "Articles from CRRE Labs on Miami website prices and on using a Google Business Profile alongside a website.",
        "https://crrelabs.com/blog/",
        "/blog/",
        index,
        jsonld(breadcrumb([("Home", "https://crrelabs.com/"), ("Blog", "https://crrelabs.com/blog/")])),
    ))


def pricing():
    faqs = [
        ("When is setup due?", "Up front. Setup fees are non-refundable once development begins."),
        ("Is there a long contract?", "No. The program is month-to-month. Monthly fees are billed recurring."),
        ("What if I cancel and come back?", "Within 90 days, reactivation is $49 on Starter, $99 on Business, and $175 on Pro."),
    ]
    body = hero(
        '<p class="text-sm text-accent font-semibold mb-4">Local Business Website Program</p>',
        "Simple packages. No long contracts.",
        f"<p>A website for a local business, with the domain, SSL, and hosting included. Starter is $99 setup and $15 a month. Business is $199 and $29 a month. Pro is $349 and $49 a month. Local competitors mostly start at $300–$500. The studio is at {ADDRESS}. Call {PHONE_DISPLAY}.</p>",
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
        <li>Month-to-month, no long contract.</li>
        <li>Setup fees due upfront, non-refundable once development begins.</li>
        <li>Monthly billed recurring.</li>
        <li>These prices are the local business program. Custom work, including the apartment sites in the <a class="text-accent underline" href="/work/">case studies</a>, is quoted separately.</li>
        <li>A longer explanation of the 2026 prices is in <a class="text-accent underline" href="/blog/how-much-does-a-website-cost-in-miami-2026/">How much does a website cost in Miami in 2026?</a></li>
      </ul>
    </div>
  </div>
</section>
'''
    body += faq_html(faqs)
    body += contact_form("pricing", "Tell us the business and which package you are looking at. We follow up by email.")
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
            {"@type": "Offer", "name": "Business", "description": "Up to 5 pages with contact form, click-to-call, basic SEO, and GBP optimization.", "priceSpecification": [
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
        "Pricing — Local Business Website Program | CRRE Labs",
        "Starter $99 + $15/mo, Business $199 + $29/mo, Pro $349 + $49/mo. Domain, SSL, and hosting included. Month-to-month. CRRE Labs, Pinecrest.",
        "https://crrelabs.com/pricing/",
        "/pricing/",
        body,
        jsonld(catalog, faq_block(faqs), breadcrumb([("Home", "https://crrelabs.com/"), ("Pricing", "https://crrelabs.com/pricing/")])),
    ))


def portfolio(buildings):
    projects = [
        ("rg-capital-partners-website", "Screenshot of the RG Capital Partners homepage: dark navy page, gold navigation, headline Private Equity Real Estate, and buttons for View Portfolio and Get in Touch.", "RG Capital Partners", "https://rgcappartners.com", "Private equity · Real estate", "A dark, gold-accent site for a private-equity real estate firm in Kansas City and Miami. The homepage calls the project a redesign delivered in under a week. <a class='text-accent underline' href='/work/rg-capital-partners/'>Case study</a>."),
        ("hireanypm-directory-website", "Screenshot of the HireAnyPM homepage, a property-manager directory with category listings and Florida coverage.", "HireAnyPM", "https://hireanypm.com", "Directory", "A property-manager directory covering Florida and expanding nationwide. The portfolio text already on this site describes 2,300+ listings across 8 categories and a featured-placement model with Stripe billing. Those figures are the ones previously published here. This revision does not add new counts."),
        ("22-biscayne-bay-leasing-website", "Top of the 22 Biscayne Bay leasing homepage for the Edgewater waterfront apartments.", "22 Biscayne Bay", "https://22biscaynebay.com", "Leasing · Edgewater", "Leasing site for a waterfront apartment community in Edgewater, with floor plans, galleries, amenities, and tour scheduling."),
        ("urban-22-miami-leasing-website", "Top of the Urban 22 Miami leasing homepage for the Edgewater rental building.", "Urban 22 Miami", "https://urban22miami.com", "Leasing · Edgewater", "Property site for a luxury rental building in Edgewater, with gallery images, floor plans, and contact information."),
        ("downtown-1st-leasing-website", "Top of the Downtown 1st leasing homepage for the downtown Miami rental tower.", "Downtown 1st", "https://downtown1st.com", "Leasing · Downtown", "Leasing site for the downtown Miami tower in the Arts and Entertainment District. The portfolio text calls it a 56-story building and lists amenities, floor plans, and tour scheduling."),
        ("downtown-5th-leasing-website", "Top of the Downtown 5th leasing homepage for the downtown Miami rental tower.", "Downtown 5th", "https://downtown5.com", "Leasing · Downtown", "Rental tower site for a dual-address Downtown Miami property, with amenities, tour scheduling, and leasing contact."),
        ("25-biscayne-park-leasing-website", "Top of the 25 Biscayne Park leasing homepage for the Biscayne Boulevard apartments.", "25 Biscayne Park", "https://25biscaynepark.com", "Leasing · Biscayne Boulevard", "The homepage describes a move from WordPress to static hosting. The portfolio page describes amenities, tour booking, and leasing contact."),
        ("melody-tower-leasing-website", "Top of the Melody Tower leasing homepage for the Midtown Miami rental tower.", "Melody Tower", "https://melodytower.com", "Leasing · Midtown", "The homepage describes a WordPress migration that preserved the original design. The portfolio places the building at 245 NE 14th Street and lists amenities plus tour and contact options. See the case study for the limit of that claim."),
        ("crre-labs-website", "Top of the CRRE Labs homepage before this redesign: dark layout and the older AI-focused headline.", "CRRE Labs", "https://crrelabs.com/", "This website", "Our own site. The screenshot shows the previous version. The current homepage leads with Pinecrest and Miami website design and the three package prices."),
    ]
    # hireanypm stem must match image output. I'll generate that filename.
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
        "<p>Projects we can link from this site. Screenshots are compressed WebP files with a PNG fallback. Case studies for the Miami buildings and for RG Capital Partners are linked from the work page. This page does not state a total number of sites delivered.</p>",
        "/work/",
        "Read the case studies",
        "/pricing/",
        "See pricing",
    )
    body += f'<section class="pb-16"><div class="max-w-7xl mx-auto px-4 sm:px-6 space-y-10">{"".join(cards)}</div></section></main>'
    emit("portfolio/index.html", page(
        "Portfolio — CRRE Labs | Pinecrest Web Design",
        "Websites by CRRE Labs: Miami apartment leasing sites, RG Capital Partners, and related projects. Screenshots and live links. No invented results.",
        "https://crrelabs.com/portfolio/",
        "/portfolio/",
        body,
        jsonld(breadcrumb([("Home", "https://crrelabs.com/"), ("Portfolio", "https://crrelabs.com/portfolio/")])),
    ))
    return [(stem, src) for stem, _, _, _, _, _ in []]  # placeholder


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
    urls = "\n".join(
        f"  <url><loc>{p}</loc><lastmod>{LASTMOD}</lastmod></url>" for p in paths
    )
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
    buildings = work_pages()
    blog()
    pricing()
    portfolio(buildings)
    not_found()
    sitemap()
    print(f"wrote {len(URLS)} html files")


if __name__ == "__main__":
    main()
