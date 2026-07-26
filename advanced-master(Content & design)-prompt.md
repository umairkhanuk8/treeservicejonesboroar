# ADVANCED Master Prompt v3 — Semantic SEO + Exact Page Layout System
### Content patterns from ny-hvac.com, moldremovaltucsonaz.net & Bellevue competitors
### Page layouts from 7 reference design screenshots (Home/Service/Area/About/Contact/Blog/FAQ)
### For use with Claude Code / Codex / Gemini

---

## 📋 STEP 1 — FILL THIS IN FOR EACH NEW SITE

```
NICHE / SERVICE: [e.g., Mold Removal / HVAC Repair / Home Remodeling]
PRIMARY CITY: [e.g., Tucson, AZ]
SERVICE AREAS (nearby cities/neighborhoods): [list 8-15]
ZIP CODES SERVED: [list if known]
BUSINESS NAME (placeholder): [e.g., ...]
PHONE (placeholder): [e.g., ...]

PRIMARY SEED KEYWORD: [e.g., mold removal tucson]
CORE SERVICES (each becomes a page): [list 6-15 services]

LOCAL CLIMATE/MARKET FACTORS: [e.g., monsoon season, older housing stock, 
desert humidity, coastal weather, tech-industry homeowners — whatever is 
locally relevant to this niche]

COMPETITOR URLS (optional, for reference): [paste 1-3 top-ranking competitor 
URLs in this niche/city if known]
```

---

## 🚀 STEP 2 — THE MASTER PROMPT (paste this whole block into Claude Code/Codex/Gemini)

```
ROLE
You are an expert local SEO strategist, semantic content architect, and 
[NICHE] industry specialist writing for [PRIMARY CITY]. You understand how 
Google traditional search, Google AI Overview, and LLM answer engines 
(ChatGPT, Perplexity, Claude, Gemini) extract, rank, and cite content.

===========================================
PART A — SITE ARCHITECTURE (build once)
===========================================
Build a complete lead-generation website for [NICHE] in [PRIMARY CITY] using 
Next.js + Tailwind CSS (or the framework this tool defaults to), fully 
responsive and mobile-first.

PAGES TO BUILD:
1. Home page
2. One page per core service: [CORE SERVICES]
3. One page per service area: [SERVICE AREAS]
4. About / Why Choose Us
5. FAQ (organized by category)
6. Contact
7. Blog index + 3 starter articles
8. Case Studies / Results section (can live on home + service pages)

Do not change this page architecture, section order, or remove/add sections 
once generated — see STRICT RULES below for anything you regenerate later.

===========================================
PART B — HEADING STRUCTURE (apply to every page)
===========================================
- One H1 per page only, containing the primary keyword + city naturally.
- H2s should mirror how a real customer would ask a question or state a need 
  (e.g., "How Fast Does [Problem] Get Worse in [City]?" not "Our Process").
- H3s break down H2 sections into scannable sub-points.
HOME PAGE section skeleton (do not remove or reorder):
  1. Hero (H1 + 2-3 sentence direct-answer intro + trust stats + CTA)
  2. Core services overview — 3 large image cards (H2)
  3. About the company — photo + credentials + 2 CTA buttons (H2)
  4. Full services grid — 10-12 short title+description items, 2-column (H2)
  5. CTA banner (dark, full-width)
  6. Why homeowners/customers choose us — icon row, 4-6 items (H2)
  7. Case studies / real results — 3 cards with images + numbers (H2)
  8. Testimonials — card row (H2)
  9. Tools/equipment or methodology used — icon grid (H2, if applicable)
  10. Step-by-step process — numbered, dark background (H2)
  11. Common problems & how to spot them — 2-column list, local/symptom-based (H2)
  12. Service area coverage — 2-column list (Nearby Cities / Neighborhoods) (H2)
  13. **Zip Codes We Serve** — dark section, zip codes as scannable chips (H2)
  14. **Find Us From Top [City] Locations** — dark section, 3-6 mini map/
      directions cards from recognizable public landmarks to the business (H2)
  15. CTA banner (dark, "Ready for a Free Evaluation?")
  16. **Our Location** — map embed + NAP box side by side (H2)
  17. Blog / Tips & Guides — 3 article cards (H2)
  18. FAQ — accordion, 5-8 Q&As (H2)
  19. Final CTA banner (dark, "#1 Choice for [Niche] in [City]")
  20. Footer: services/areas link columns + map embed + full NAP block

MULTIPLE CTA RULE (applies to all page types):
- Do not rely on a single CTA at the very bottom. Place a full-width CTA 
  banner after every 3-5 major sections where reader intent naturally peaks. 
  Vary the CTA copy each time (e.g., "Get a Free Estimate" vs "Call Now for 
  Same-Day Service" vs "Schedule Your Free Inspection") rather than repeating 
  identical button text throughout the page.

SERVICE PAGE section skeleton (do not remove or reorder):
  1. Hero (H1 + intro + 2 primary CTAs + 2 secondary trust CTAs)
  2. Full-width intro paragraph ("Full-Service [Service] in [City]")
  **Sidebar begins here (desktop: sticky right rail, ~30% width; mobile: 
  stacks below hero, above body):**
  - "Need Help Now?" card — call button + secondary CTA button
  - Business hours card
  - "Our Services" menu list — all core services, current page highlighted
  3. Body content, 8-12 H2/H3 subsections covering: what's included, 
     standards/methods used, special scenarios (insurance, storm/emergency 
     variants, cost factors), technical considerations specific to the 
     service, local expertise tie-in, and a closing standards/steps summary
  4. Trust icon badge row (4 items)
  5. "When You Need [Service]" — 4 symptom/trigger cards (H2)
  6. Step-by-step process for this service — numbered, 4 steps (H2)
  7. Common causes/sources — simple list (H2)
  8. Dark "Specialists" section — 4 icon trust badges (H2)
  9. FAQ specific to this service — accordion (H2)
  10. Service area chips — grid of served cities/areas (H2)
  11. Related services — 6 cards grid (H2)
  12. Related blog guides — 3 article cards (H2)
  13. Internal resource links — chip/tag row (H2)
  14. CTA banner (dark)
  15. "Located in the Heart of [City]" — map embed + NAP (H2)
  16. Footer (same as home page)

SERVICE AREA PAGE section skeleton (do not remove or reorder):
  1. Hero (H1 with service + area name + breadcrumb + intro + 2 CTAs)
  2. "Your Trusted [Niche] Specialists in [Area]" — image + intro (H2)
  **Sidebar begins here (same position/behavior as service page):**
  - "Reach Us" card — call button + secondary CTA
  - Business hours card
  - "Our Services" menu list
  3. Body content, 6-10 H2/H3 subsections covering: restoration/service 
     scope in this area, why this area has unique challenges (housing 
     stock, terrain, climate), response methods, moisture/technical 
     considerations, local approach, building materials common to the area, 
     documentation process, neighborhoods/surrounding communities served
  4. Trust icon badge row (4 items)
  5. CTA banner (dark)
  6. "[Issue] [Area] Property Owners Face" — 6 symptom cards grid (H2)
  7. "How We Handle Restoration/Service in [Area]" — numbered process, 4 steps (H2)
  8. Dark "What Sets Our [Area] Team Apart" — 4 icon cards (H2)
  9. CTA banner (dark)
  10. FAQ specific to this area — accordion (H2)
  11. Dark "Our [Area] Coverage Area" — map + directions CTA (H2)
  12. "Serving [Area] & Surrounding Regions" — 2-column list (Nearby Cities / 
      Neighborhoods) (H2)
  13. "Explore Our Full Range of Services" — 6 service cards grid (H2)
  14. Local blog guides — 3 article cards (H2)
  15. Internal resource links — chip/tag row (H2)
  16. CTA banner (dark)
  17. "Serving [Area] & Surrounding Communities" — text + map (H2)
  18. Footer (same as home page)

ABOUT PAGE section skeleton (do not remove or reorder):
  1. Hero (H1 + trust badges + 2 CTAs)
  2. Origin story — "How [Trigger Event] Built a [City] [Niche] Team" — logo/
     photo + team photo + stats row (years in business, projects completed, 
     communities served, response availability) (H2)
  3. "The [City] We Serve Every Day" — local city knowledge paragraph + stats 
     row (population, area, year founded) + neighborhoods paragraph (H2)
  4. "What Sets Us Apart" — 6 icon cards grid (H2)
  5. "Complete [Niche] Services for [City]" — icon list, 2 rows x 3 + 
     "View All Services" CTA (H2)
  6. Dark "We Know [City]'s [Niche] Challenges" — 4 cards (H2)
  7. "Serving [X]+ Communities Across [Region]" — city name grid + 
     "View All Service Areas" CTA (H2)
  8. "Questions About Our Company" — FAQ accordion (H2)
  9. "Learn More from Our Blog" — text + "Explore Blog" CTA (H2)
  10. CTA banner (dark)
  11. Larger dark CTA banner ("Need Help With [Niche]?")
  12. Footer (same as home page)

CONTACT PAGE section skeleton (do not remove or reorder):
  1. Hero (H1 "Contact Us" + intro + trust badges + 2 CTAs)
  2. "Let's Start Your [Project/Service]" — 3 contact-info cards (Call, 
     Email, Location) on the left + a lead/quote form on the right (H2)
  3. Full-width map embed below the contact section
  4. Trust icon badge row (4-5 items — response time, free estimate, 
     insurance-ready docs, etc.)
  5. "Quick Answer" — direct-answer paragraph: how to contact, response 
     expectations, what to do in an emergency (H2)
  6. "What to Expect After You Contact Us" — numbered timeline, 4 steps (H2)
  7. Dark "Services You Can Request" — 4 service cards (H2)
  8. "Common Questions About Reaching Our Team" — FAQ accordion, first item 
     open by default (H2)
  9. Footer (same as home page)

BLOG POST section skeleton (do not remove or reorder):
  1. Hero (H1 + breadcrumb + intro line + 2 CTAs)
  2. Featured image
  **Sidebar begins here (desktop: sticky right rail):**
  - "In This Article" Table of Contents card — jump links to each H2
  - "Need Help?" CTA card directly below the TOC card
  3. Body content: opens with a "Quick Answer" callout box, then 8-12 H2/H3 
     sections with practical, specific detail; one inline CTA banner placed 
     naturally mid-article; closes with a "The Bottom Line" summary section
  4. Author/company credibility box (name, credentials, one line of experience)
  5. "You Might Also Find Helpful" — 3 related article cards (H2)
  6. "Local Areas This Guide Applies To" — city chip row (H2)
  7. Internal resource links — chip/tag row (H2)
  8. Footer (same as home page)

FAQ PAGE section skeleton (do not remove or reorder):
  1. Hero (H1 + 2 CTAs)
  2. "FAQ Center" intro — direct-answer paragraph on how to use the page
  **Sidebar begins here:**
  - "Have a Question?" call CTA card
  - "Our Services" menu list
  3. Trust icon badge row (4 items)
  4. Main FAQ heading + **Sidebar: "FAQ Categories" jump-link list** — main 
     content organized into 8-12 numbered categories (e.g., "01. General 
     Services," "02. Emergency Response," "03. [Core Service]," 
     "04. [Core Service]," ... "10. Service Areas & Response Times"), each 
     category a labeled group of 5-8 accordion Q&As
  5. "Coverage Across [Region]" — city chip grid (H2)
  6. CTA banner (dark, "Still Have a Question?")
  7. Larger dark CTA banner ("Still Have Questions?")
  8. Footer (same as home page)

GLOBAL FOOTER (every page):
- Logo + 1-2 line company description + social icons
- Quick Links column (Home, About, Services, Areas, Blog, FAQ, Contact)
- Our Services column (linked list)
- Service Areas column (linked list)
- City stats strip (City, County, Population, Area, Zip Codes, relevant 
  local utility/authority if applicable)
- Map embed + full NAP block (Business Name, Address, Phone, Email, Hours, 
  License/Insurance line)
- Copyright + Privacy Policy + Terms of Service links

===========================================
PART C — SEMANTIC & ENTITY OPTIMIZATION
===========================================
Before writing, silently build (do not output this list, just use it to 
inform the writing):

1. ENTITIES TO WEAVE IN NATURALLY:
   - Competitor-common entities: the standard named concepts, certifications, 
     equipment, methods, and terminology that top-ranking [NICHE] sites in 
     this space consistently reference (e.g., for mold: IICRC, S500/S520 
     standards, HEPA, moisture meters; for HVAC: SEER rating, brand names, 
     BTU, ductwork; for remodeling: ADU, load-bearing walls, permits).
   - AI-relevant entities: adjacent concepts an LLM would associate with this 
     query cluster — related problems, related services, local landmarks, 
     local regulations/codes, local climate factors, industry certifications.
   - Do NOT list these separately in the output — integrate them into 
     sentences naturally, the way a real expert would reference them in 
     context.

2. KEY PHRASES & N-GRAMS:
   - Identify natural 2-4 word phrases customers actually search/say 
     (e.g., "burst pipe repair," "black mold in bathroom," "kitchen 
     remodel cost") and weave them into headings and body copy where they 
     fit naturally — never force them.
   - Include a few unique, stand-out phrases that differentiate this content 
     from generic competitor copy (specific to this business's approach, 
     local knowledge, or process).

3. NLP / SEMANTIC KEYWORDS:
   - Naturally include related terms Google's NLP models associate with the 
     main topic (synonyms, related actions, related outcomes) rather than 
     repeating the exact same keyword. Vary phrasing sentence to sentence.

4. WORD RELATIONSHIPS (apply naturally, don't force or list):
   - Use synonyms to avoid repetition (e.g., "repair," "fix," "restore," 
     "resolve" — rotate naturally).
   - Reference more specific terms (hyponyms) and broader category terms 
     (hypernyms) where relevant — e.g., under "water damage" mention specific 
     types like "burst pipe," "sewage backup," "roof leak."
   - Reference component/part terms (meronyms) relevant to the niche — e.g., 
     for HVAC: compressor, condenser, ductwork, thermostat.
   - Use proper nouns naturally: brand names, certifying bodies, local 
     landmarks, neighborhood names, relevant regulations.

5. LOCAL SEMANTIC SIGNALS:
   - Reference local climate, housing stock, regulations, or market 
     conditions relevant to [NICHE] in [PRIMARY CITY] — this is what 
     separates expert local content from generic templated copy.

===========================================
PART D — CONTENT QUALITY REQUIREMENTS (non-negotiable)
===========================================
- 100% unique content, written as if by a real, experienced [NICHE] 
  professional in [PRIMARY CITY] — not generic marketing filler.
- No AI-sounding phrases, no fluff, no keyword stuffing, no repeated 
  information across sections — every section must add distinct value.
- Strong readability: short paragraphs, active voice, concrete specifics 
  (numbers, timeframes, real scenarios) over vague claims.
- Analyze search intent first: write for real homeowners, property managers, 
  landlords, or business owners — search engines are the secondary audience.
- Every claim should be backed by a logical explanation, a specific example, 
  or a practical detail — never a bare marketing statement ("we're the 
  best") without substantiation.

WORD COUNT TARGETS:
- Home page: 2,500–3,500 words
- Service page: 1,800–2,500 words
- Service area page: 1,500–2,200 words
- Blog post: 800–1,500 words
- FAQ page: minimum 10 FAQs per category

===========================================
PART E — CASE STUDIES
===========================================
For every case study (aim for 3 per relevant page):
- Use a realistic scenario specific to [NICHE] and a named local area.
- Include a measurable before/after result (a number, percentage, or 
  timeframe — e.g., moisture % reduced, days to complete, cost saved).
- Focus on the outcome that matters most to the customer: problem solved, 
  money saved, property protected, satisfaction achieved.
- Keep format consistent: situation → action taken → measurable result.

===========================================
PART F — FAQ SECTIONS
===========================================
- Answer every question directly in the first sentence (featured-snippet 
  style) before adding supporting detail.
- Write questions the way real people phrase them (including voice-search 
  phrasing — full natural sentences, not fragment keywords).
- Keep answers concise (40-80 words) but complete enough to stand alone if 
  quoted by an AI answer engine.
- Cover: cost/pricing questions, process/timeline questions, 
  "do I need this" questions, safety/risk questions, insurance/warranty 
  questions (if applicable), and DIY-vs-professional questions.

===========================================
PART G — SERVICE AREA PAGES
===========================================
For each service area page:
- Write a unique description — no duplicated structure or phrasing across 
  area pages, even though the service is the same.
- Mention specific local challenges relevant to [NICHE] in that area (local 
  housing types, climate patterns, common problems specific to that 
  neighborhood/city).
- Reference weather/climate conditions where relevant to the niche.
- Demonstrate local market knowledge — mention how the area's real 
  characteristics (older homes, new construction, specific terrain, local 
  regulations) shape the work.
- Avoid any duplicate content between area pages — each must read as if 
  written by someone who actually knows that specific area.

===========================================
PART H — INTERNAL LINKING
===========================================
- Reference related service pages naturally within body copy where relevant 
  (not as a forced link list).
- Reference related service area pages naturally where relevant.
- Support topical authority through contextual, in-sentence internal links.
- Never force a link where it doesn't make natural sense in the sentence.

===========================================
PART I — E-E-A-T REQUIREMENTS
===========================================
Demonstrate throughout (not as a separate section, but woven into content):
- Real-world experience: specific scenarios, specific numbers, specific 
  local knowledge that only someone who does this work would know.
- Technical expertise: correct use of industry terminology and standards.
- Local market knowledge: housing stock, climate, regulations specific to 
  [PRIMARY CITY].
- Trustworthiness: licensing, insurance, certifications, transparent 
  process, honest caveats (e.g., "reactions vary by person" for health 
  claims — avoid fear-based or absolute claims that aren't defensible).
- Support every claim with a logical explanation or concrete example rather 
  than a generic marketing statement.

===========================================
PART J — SCHEMA & TECHNICAL SEO
===========================================
- LocalBusiness schema (NAP, hours, service area, geo coordinates)
- Service schema per service page
- FAQPage schema on FAQ + service pages
- AggregateRating/Review schema
- BreadcrumbList on all inner pages
- robots.txt allowing: Googlebot, Google-Extended, GPTBot, ChatGPT-User, 
  PerplexityBot, ClaudeBot, Bingbot
- XML sitemap listing all pages
- Unique title tag (under 60 chars) and meta description (150-160 chars) 
  per page, following pattern: "[Primary Keyword] in [City] | [Business Name]"

===========================================
PART K — DESIGN
===========================================
- Design must feel unique to [NICHE] — not a generic template. Choose colors, 
  typography, and layout that fit the industry and locality naturally 
  (e.g., trust-blue for restoration/HVAC, warm/earthy for remodeling, 
  bold-urgent tones for emergency services).
- Sticky header with click-to-call + primary CTA button, always visible on 
  mobile.
- Hero section answers "what we do + where" within 5 seconds, with trust 
  indicators (licensed/insured/years in business/rating).
- Thumb-friendly buttons (min 44x44px), no intrusive mobile popups.
- Fast-loading: optimize images, avoid render-blocking scripts, target Core 
  Web Vitals (LCP < 2.5s, CLS < 0.1, INP < 200ms).
- Map embeds: use standard Google Maps iframe embeds (no API key required) 
  for both the 6 "from landmark to business" mini-maps and the single larger 
  "Target City" map — lazy-load these iframes so they don't block initial 
  page load/LCP.
- Sidebars (services menu / area menu / table of contents): sticky on 
  desktop (stays visible while scrolling within its section), collapses to 
  a simple stacked block above or below main content on mobile — never a 
  fixed floating element that covers content on small screens.

===========================================
PART L — STRICT RULES FOR CONTENT REGENERATION/EDITS
===========================================
When asked to rewrite, refresh, or optimize existing content on this site:

DO NOT:
- Change the layout, section order, or page architecture
- Remove or add sections
- Change functionality or CTA placements

YOU MAY:
- Improve headings for SEO, user intent, and click-through rate
- Improve topical relevance and depth
- Improve readability and flow
- Improve conversion messaging within existing CTA placements

===========================================
OUTPUT INSTRUCTIONS
===========================================
When generating page content (as opposed to full site build):
- Return only the final content for the requested page/section.
- Do not explain your reasoning, do not add notes, do not add recommendations 
  — output only the finished content, formatted with proper heading tags.
- Follow the exact section skeleton for that page type from Part B (Home, 
  Service, Service Area, About, Contact, Blog Post, or FAQ) — do not mix 
  skeletons or drop sections.

When generating the full site (first build):
- After building, summarize: pages created + file paths, placeholder content 
  that needs real data before launch (images, phone, reviews, address), and 
  confirmation that schema/robots.txt/sitemap are in place.

NICHE: [NICHE / SERVICE]
CITY: [PRIMARY CITY]
SERVICE AREAS: [SERVICE AREAS]
CORE SERVICES: [CORE SERVICES]
PRIMARY KEYWORD: [PRIMARY SEED KEYWORD]
LOCAL FACTORS: [LOCAL CLIMATE/MARKET FACTORS]
```

---

## 🔁 How to reuse this for every new niche/site

1. Copy Part A's fill-in block, complete it for the new niche/city.
2. Paste the whole Master Prompt (with your fills applied) into Claude Code, 
   Codex, or Gemini for the initial full build.
3. For ongoing content work (new blog posts, refreshing a service page, 
   adding a new area page), just reference Part L's strict rules and ask for 
   the one page/section you need — the AI will follow the same standards 
   without needing the whole prompt repeated.
4. Keep a swipe file of 2-3 real competitor URLs per niche (like the 3 you 
   gave me) — pasting one into the "COMPETITOR URLS" field before a build 
   gives the AI a concrete quality bar to match or beat.

---

## 📎 Sources behind this prompt

- **ny-hvac.com / moldremovaltucsonaz.net / Bellevue remodeling competitors** 
  — used for content patterns: entity usage, FAQ phrasing, case study 
  structure, local semantic detail.
- **7 reference design screenshots (Home, Service, Area, About, Contact, 
  Blog Post, FAQ)** — used to build the exact section-by-section layout 
  blueprints in Part B, including sidebar behavior, zip code sections, map 
  embeds, multi-CTA placement, and the footer NAP/map pattern. This is the 
  visual design system the AI should replicate for any new niche — only the 
  colors, imagery, and copy change per business.

This prompt combines proven content patterns with a proven visual layout 
system into one repeatable build process.
