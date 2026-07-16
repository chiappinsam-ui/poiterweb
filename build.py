#!/usr/bin/env python3
"""Assemble St George Concrete Solutions pages from shared partials."""
import pathlib

OUT = pathlib.Path(__file__).parent

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<script>(function(){try{var t=localStorage.getItem('sg-theme');if(!t){t=(window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches)?'dark':'light';}document.documentElement.setAttribute('data-theme',t);}catch(e){document.documentElement.setAttribute('data-theme','light');}})();</script>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>@@TITLE@@</title>
<meta name="description" content="@@DESC@@">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='14' fill='%23B0431F'/%3E%3Ctext x='50' y='66' font-size='46' font-family='Arial,Helvetica,sans-serif' font-weight='800' fill='%23ffffff' text-anchor='middle'%3ESG%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

def header(active):
    def cls(name):
        return ' class="active" aria-current="page"' if name == active else ''
    links = "".join(
        f'      <a href="{p}.html"{cls(p)}>{label}</a>\n'
        for p, label in [("index", "Home"), ("about", "About"), ("services", "Services"),
                         ("gallery", "Gallery"), ("contact", "Contact")]
    )
    mlinks = "".join(
        f'    <a href="{p}.html"{cls(p)}>{label}</a>\n'
        for p, label in [("index", "Home"), ("about", "About"), ("services", "Services"),
                         ("gallery", "Gallery"), ("contact", "Contact")]
    )
    return f"""<header id="site-header">
  <div class="container nav-inner">
    <a href="index.html" class="logo" aria-label="St George Concrete Solutions — home">
      <img class="mark" src="Conclogo.jpg" alt="">
      <span class="word"><b>St George Concrete Solutions</b><small>Est. 2009 · Adelaide, SA</small></span>
    </a>
    <nav class="nav-links" aria-label="Primary">
{links}    </nav>
    <div class="nav-right">
      <button class="theme-toggle" id="themeToggle" aria-label="Toggle light and dark mode" aria-pressed="false">
        <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>
        <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>
      </button>
      <a href="tel:0881234567" class="nav-phone">
        <svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        <span><small>Call or text</small>(08) 8123 4567</span>
      </a>
      <a href="contact.html" class="btn btn-solid" style="padding:12px 22px;">
        <span>Free Quote</span>
        {ARROW}
      </a>
      <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mobilePanel"><span></span><span></span><span></span></button>
    </div>
  </div>
  <div class="mobile-panel" id="mobilePanel">
{mlinks}    <a href="contact.html" class="btn btn-solid">Get a Free Quote</a>
  </div>
</header>
<div class="overlay-dim" id="overlayDim"></div>
"""

FOOTER = f"""<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <div class="footer-logo"><img class="mark" src="Conclogo.jpg" alt=""> St George Concrete Solutions</div>
        <p>Adelaide's premier concrete design &amp; installation company. Licensed, insured, and locally owned since 2009.</p>
        <div class="footer-social">
          <a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg></a>
          <a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg></a>
          <a href="#" aria-label="Google Business Profile"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v8M8 12h8"/></svg></a>
        </div>
      </div>
      <div class="footer-col">
        <h5>Navigate</h5>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Services</h5>
        <ul>
          <li><a href="services.html">Stamped &amp; Decorative</a></li>
          <li><a href="services.html">Custom Driveways</a></li>
          <li><a href="services.html">Patios &amp; Outdoor Living</a></li>
          <li><a href="services.html">Pool Decks</a></li>
          <li><a href="services.html">Foundations &amp; Commercial</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Get in touch</h5>
        <ul>
          <li><a href="tel:0881234567">(08) 8123 4567</a></li>
          <li><a href="mailto:hello@stgeorgeconcrete.com.au">hello@stgeorgeconcrete.com.au</a></li>
          <li>8 Growers Road<br>Wingfield SA 5013</li>
          <li>Mon–Sat · 7am–6pm</li>
        </ul>
      </div>
    </div>
    <div class="footer-big-word" aria-hidden="true">CONCRETE</div>
    <div class="footer-bottom">
      <p>© <span id="year">2026</span> St George Concrete Solutions. All rights reserved.</p>
      <div class="legal">
        <a href="#">Privacy Policy</a>
        <a href="#">Terms of Service</a>
        <a href="#">SA Builder's Licence #BLD-204871</a>
      </div>
    </div>
  </div>
</footer>

<button id="top-btn" aria-label="Back to top">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
</button>

<script src="script.js"></script>
</body>
</html>
"""

def img(file, w, h, label, alt):
    return (f'<img src="{file}" data-file="{file}" data-w="{w}" data-h="{h}" '
            f'data-label="{label}" alt="{alt}" loading="lazy">')

def banner(crumb, h1, p, imgfile="concrete19.png"):
    return f"""  <section class="page-banner">
    <div class="hero-bg">
      {img(imgfile, 1920, 900, "Page banner — crew on job site", "St George Concrete Solutions crew on a job site")}
    </div>
    <div class="container page-banner-inner">
      <div class="breadcrumb"><a href="index.html">Home</a><span>/</span><span>{crumb}</span></div>
      <h1>{h1}</h1>
      <p>{p}</p>
    </div>
  </section>
"""

def cta(eyebrow, title, primary_label, secondary_href, secondary_label):
    return f"""  <section class="cta-banner">
    <div class="cta-bg">
      {img("concrete15.png", 1920, 1200, "CTA banner — dusk shot of finished driveway", "Finished stamped concrete driveway at dusk")}
    </div>
    <div class="container cta-content reveal">
      <div class="eyebrow">{eyebrow}</div>
      <h2 class="section-title">{title}</h2>
      <p>Estimates are free, on-site, and pressure-free. Most projects are quoted within 48 hours.</p>
      <div class="cta-actions">
        <a href="contact.html" class="btn btn-solid"><span>{primary_label}</span>{ARROW}</a>
        <a href="{secondary_href}" class="btn btn-outline"><span>{secondary_label}</span></a>
      </div>
    </div>
  </section>
"""

def service_card(imgfile, tag, title, desc, bullets=None, link_href="services.html",
                 link_label="View service", delay="d1"):
    ul = ""
    if bullets:
        lis = "".join(f"<li>{b}</li>" for b in bullets)
        ul = f"\n            <ul>{lis}</ul>"
    return f"""        <article class="service-card reveal-scale {delay}">
          <div class="service-media">
            {img(imgfile, 800, 640, f"Service — {tag}", title + " in Adelaide, South Australia")}
            <span class="service-tag">{tag}</span>
          </div>
          <div class="service-body">
            <h3>{title}</h3>
            <p>{desc}</p>{ul}
            <a href="{link_href}" class="service-link"><span>{link_label}</span>{ARROW}</a>
          </div>
        </article>
"""

def gallery_item(imgfile, w, h, cat_slug, cat, title, extra="", href=None):
    size = f' {extra}' if extra else ''
    tag = "a" if href else "div"
    attr = f' href="{href}" aria-label="{cat}: {title} — open gallery"' if href else ''
    return f"""        <{tag} class="gallery-item{size}" data-cat="{cat_slug}"{attr}>
          {img(imgfile, w, h, f"Gallery — {title}", f"{cat}: {title}")}
          <div class="gallery-overlay"><div class="cat">{cat}</div><div class="ti">{title}</div></div>
        </{tag}>
"""

# ---------------------------------------------------------------- INDEX
index_body = f"""<main id="main">

  <section class="hero">
    <div class="hero-bg">
      {img("concrete.png", 1920, 1080, "Hero — luxury stamped concrete patio, wide shot", "Luxury stamped concrete patio by St George Concrete Solutions")}
    </div>
    <div class="container hero-inner">
      <div class="eyebrow">Adelaide, South Australia · Licensed &amp; Insured · Est. 2009</div>
      <h1>Poured to last.<br><em>Finished to impress.</em></h1>
      <p class="lead">St George Concrete Solutions designs and hand-finishes driveways, patios, pool decks and foundations across Adelaide and the Adelaide Hills — engineered for our reactive clay soils, built to outlast them.</p>
      <div class="hero-cta">
        <a href="contact.html" class="btn btn-solid"><span>Get a Free Estimate</span>{ARROW}</a>
        <a href="gallery.html" class="btn btn-outline"><span>See Our Work</span>{ARROW}</a>
      </div>
      <div class="hero-ticket">
        <div class="cell"><b>15+</b><span>Years in Adelaide</span></div>
        <div class="cell"><b>800+</b><span>Projects poured</span></div>
        <div class="cell"><b>4.9★</b><span>Average rating</span></div>
        <div class="cell"><b>BLD-204871</b><span>Licensed &amp; insured</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center reveal">
        <div class="eyebrow">What we build</div>
        <h2 class="section-title">Concrete services, <em>elevated.</em></h2>
        <p class="section-sub">From a quiet backyard patio to a full commercial foundation — every project gets the same obsessive finish work.</p>
      </div>
      <div class="services-grid">
{service_card("concrete3.png", "Decorative", "Stamped &amp; Decorative", "Slate, cobblestone and wood-plank textures with hand-applied stains — no two patios look alike.", delay="d1")}
{service_card("concrete4.png", "Driveways", "Custom Driveways", "Exposed aggregate, broom-finish or stamped borders, engineered for Adelaide's heat cycles.", delay="d2")}
{service_card("concrete5.png", "Outdoor living", "Patios &amp; Outdoor Living", "Full outdoor rooms — fire features, seat walls and kitchens poured to match your home.", delay="d3")}
      </div>
      <div style="text-align:center; margin-top:52px;">
        <a href="services.html" class="btn btn-outline"><span>View All Six Services</span>{ARROW}</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container about-grid">
      <div class="about-media reveal-left">
        <div class="img-wrap">
          {img("concrete2.png", 900, 1125, "About — crew finishing a stamped concrete slab", "St George Concrete Solutions crew hand-finishing a stamped slab")}
        </div>
        <div class="about-badge"><span>EST.</span><b>2009</b><span>SA</span></div>
      </div>
      <div class="about-copy reveal-right">
        <div class="eyebrow">Who we are</div>
        <h2 class="section-title">Engineered for the clay. <em>Finished like marble.</em></h2>
        <p>For over fifteen years, St George Concrete Solutions has been the name Adelaide homeowners and builders trust for concrete that's batched for our reactive clay soils and hot summers, and finished with the precision of custom stonework.</p>
        <p>Every pour is led by a master finisher and backed by a craftsmanship warranty — because concrete is permanent, and we treat it that way.</p>
        <div class="about-points">
          <div class="about-point">
            <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2l3 7h7l-5.5 4.5L18 21l-6-4-6 4 1.5-7.5L2 9h7z"/></svg></div>
            <div><b>Master craftsmen</b><p>Decorative &amp; structural specialists.</p></div>
          </div>
          <div class="about-point">
            <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M9 12l2 2 4-4"/></svg></div>
            <div><b>Fully licensed</b><p>Licensed &amp; insured in South Australia.</p></div>
          </div>
          <div class="about-point">
            <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4.5 8-11V5l-8-3-8 3v6c0 6.5 8 11 8 11z"/></svg></div>
            <div><b>Lifetime warranty</b><p>On every structural pour.</p></div>
          </div>
          <div class="about-point">
            <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 1 0-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 0 0 0-7.78z"/></svg></div>
            <div><b>Locally loved</b><p>800+ Adelaide homes.</p></div>
          </div>
        </div>
        <a href="about.html" class="btn btn-outline" style="margin-top:14px;"><span>Learn Our Story</span>{ARROW}</a>
      </div>
    </div>
  </section>

  <section class="stats-band">
    <div class="container stats-grid">
      <div class="stat-card reveal"><div class="stat-num"><span class="count" data-target="15">0</span><span class="suffix">+</span></div><div class="stat-label">Years of excellence</div></div>
      <div class="stat-card reveal d1"><div class="stat-num"><span class="count" data-target="812">0</span><span class="suffix">+</span></div><div class="stat-label">Projects delivered</div></div>
      <div class="stat-card reveal d2"><div class="stat-num"><span class="count" data-target="100">0</span><span class="suffix">%</span></div><div class="stat-label">Licensed &amp; insured</div></div>
      <div class="stat-card reveal d3"><div class="stat-num"><span class="count" data-target="49" data-decimal="1">0</span><span class="suffix">★</span></div><div class="stat-label">Average client rating</div></div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center reveal">
        <div class="eyebrow">Recent work</div>
        <h2 class="section-title">A portfolio worth <em>standing on.</em></h2>
        <p class="section-sub">A small sample of driveways, patios and decorative work completed across Greater Adelaide.</p>
      </div>
      <div class="gallery-grid g-4 reveal">
{gallery_item("concrete9.png", 800, 1000, "driveways", "Driveways", "Belair Hills Estate", href="gallery.html")}
{gallery_item("concrete10.png", 1000, 640, "patios", "Patios", "Burnside Residence", href="gallery.html")}
{gallery_item("concrete11.png", 700, 640, "pool-decks", "Pool Decks", "Beaumont Pool", href="gallery.html")}
{gallery_item("concrete12.png", 700, 640, "decorative", "Decorative", "Glenelg Walkway", href="gallery.html")}
      </div>
      <div style="text-align:center; margin-top:52px;">
        <a href="gallery.html" class="btn btn-outline"><span>View the Full Gallery</span>{ARROW}</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center reveal">
        <div class="eyebrow">Client stories</div>
        <h2 class="section-title">Words from <em>our neighbors.</em></h2>
      </div>
      <div class="tm-wrap reveal">
        <div class="tm-track" id="tmTrack">
          <div class="tm-slide active">
            <div class="tm-stars" aria-hidden="true">★★★★★</div>
            <p class="quote">"They replaced our entire driveway and back patio in one week. The stamped pattern looks like natural slate — neighbors keep asking who did it."</p>
            <div class="tm-person">
              <span class="initials" aria-hidden="true">RM</span>
              <div class="who"><b>Rachel M.</b><span>Burnside, Adelaide</span></div>
            </div>
          </div>
          <div class="tm-slide">
            <div class="tm-stars" aria-hidden="true">★★★★★</div>
            <p class="quote">"Best bid, cleanest job site, and they finished a full day ahead of schedule. Our pool deck stays cool even in August."</p>
            <div class="tm-person">
              <span class="initials" aria-hidden="true">DT</span>
              <div class="who"><b>Derek T.</b><span>Beaumont, Adelaide</span></div>
            </div>
          </div>
          <div class="tm-slide">
            <div class="tm-stars" aria-hidden="true">★★★★★</div>
            <p class="quote">"As a builder I've used a lot of crews. St George Concrete Solutions is the only one I trust on foundations for custom homes."</p>
            <div class="tm-person">
              <span class="initials" aria-hidden="true">ML</span>
              <div class="who"><b>Marcus L.</b><span>General Contractor, Adelaide</span></div>
            </div>
          </div>
        </div>
        <div class="tm-nav">
          <button id="tmPrev" aria-label="Previous testimonial"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg></button>
          <div class="tm-dots" id="tmDots"></div>
          <button id="tmNext" aria-label="Next testimonial"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg></button>
        </div>
      </div>
    </div>
  </section>

{cta("Ready when you are", "Let's pour something <em>permanent.</em>", "Request a Free Estimate", "tel:0881234567", "(08) 8123 4567")}
</main>

"""

# ---------------------------------------------------------------- ABOUT
about_body = f"""<main id="main">

{banner("About", "The crew behind <em>every pour.</em>", "Fifteen years, eight hundred projects, one standard: concrete finished like it matters — because it's permanent.")}

  <section class="section">
    <div class="container about-grid">
      <div class="about-media reveal-left">
        <div class="img-wrap">
          {img("concrete2.png", 900, 1125, "About — crew finishing a stamped concrete slab", "St George Concrete Solutions crew hand-finishing a stamped slab")}
        </div>
        <div class="about-badge"><span>EST.</span><b>2009</b><span>SA</span></div>
      </div>
      <div class="about-copy reveal-right">
        <div class="eyebrow">Our story</div>
        <h2 class="section-title">Engineered for the clay. <em>Finished like marble.</em></h2>
        <p>St George Concrete Solutions started in 2009 with one mixer truck and a promise: every slab we pour gets treated like it's going in our own backyard. Fifteen years later, that promise hasn't changed — just the size of the crew keeping it.</p>
        <p>We batch and cure for Adelaide's reactive clay soils, hand-finish every decorative detail, and stand behind the work with a craftsmanship warranty most contractors won't offer.</p>
        <div class="about-points">
          <div class="about-point">
            <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2l3 7h7l-5.5 4.5L18 21l-6-4-6 4 1.5-7.5L2 9h7z"/></svg></div>
            <div><b>Master craftsmen</b><p>Decorative &amp; structural specialists.</p></div>
          </div>
          <div class="about-point">
            <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M9 12l2 2 4-4"/></svg></div>
            <div><b>Fully licensed</b><p>Licensed &amp; insured in South Australia.</p></div>
          </div>
          <div class="about-point">
            <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4.5 8-11V5l-8-3-8 3v6c0 6.5 8 11 8 11z"/></svg></div>
            <div><b>Lifetime warranty</b><p>On every structural pour.</p></div>
          </div>
          <div class="about-point">
            <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 1 0-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 0 0 0-7.78z"/></svg></div>
            <div><b>Locally loved</b><p>800+ Adelaide homes.</p></div>
          </div>
        </div>
        <div class="about-sign">
          <span class="initials" aria-hidden="true">JH</span>
          <div class="who"><b>Jared Hardwick</b><span>Founder &amp; Master Finisher</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center reveal">
        <div class="eyebrow">What drives us</div>
        <h2 class="section-title">Our core <em>values.</em></h2>
      </div>
      <div class="values-grid">
        <div class="value-card reveal-scale d1">
          <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2l3 7h7l-5.5 4.5L18 21l-6-4-6 4 1.5-7.5L2 9h7z"/></svg></div>
          <h4>Precision</h4>
          <p>Every form, joint and finish measured twice, poured once.</p>
        </div>
        <div class="value-card reveal-scale d2">
          <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><path d="M22 4L12 14.01l-3-3"/></svg></div>
          <h4>Integrity</h4>
          <p>Firm quotes, honest timelines, no change-order surprises.</p>
        </div>
        <div class="value-card reveal-scale d3">
          <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4.5 8-11V5l-8-3-8 3v6c0 6.5 8 11 8 11z"/></svg></div>
          <h4>Durability</h4>
          <p>Mix designs engineered specifically for Adelaide's heat cycles.</p>
        </div>
        <div class="value-card reveal-scale d4">
          <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 1 0-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 0 0 0-7.78z"/></svg></div>
          <h4>Care</h4>
          <p>We treat every yard, driveway and deadline like it's our own.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center reveal">
        <div class="eyebrow">Leadership</div>
        <h2 class="section-title">Meet the <em>team.</em></h2>
        <p class="section-sub">The people who show up on your job site, every time.</p>
      </div>
      <div class="team-grid">
        <div class="team-card reveal-scale d1">
          <div class="team-media">{img("concrete20.png", 700, 875, "Team — Jared Hardwick, Founder", "Jared Hardwick, Founder and Master Finisher")}</div>
          <div class="team-info"><b>Jared Hardwick</b><span>Founder &amp; Master Finisher</span></div>
        </div>
        <div class="team-card reveal-scale d2">
          <div class="team-media">{img("concrete21.png", 700, 875, "Team — Operations Lead", "Maria Sanchez, Operations and Estimating")}</div>
          <div class="team-info"><b>Maria Sanchez</b><span>Operations &amp; Estimating</span></div>
        </div>
        <div class="team-card reveal-scale d3">
          <div class="team-media">{img("concrete22.png", 700, 875, "Team — Site Foreman", "Colby Reese, Field Foreman")}</div>
          <div class="team-info"><b>Colby Reese</b><span>Field Foreman</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="stats-band">
    <div class="container stats-grid">
      <div class="stat-card reveal"><div class="stat-num"><span class="count" data-target="15">0</span><span class="suffix">+</span></div><div class="stat-label">Years of excellence</div></div>
      <div class="stat-card reveal d1"><div class="stat-num"><span class="count" data-target="812">0</span><span class="suffix">+</span></div><div class="stat-label">Projects delivered</div></div>
      <div class="stat-card reveal d2"><div class="stat-num"><span class="count" data-target="22">0</span></div><div class="stat-label">Crew members</div></div>
      <div class="stat-card reveal d3"><div class="stat-num"><span class="count" data-target="49" data-decimal="1">0</span><span class="suffix">★</span></div><div class="stat-label">Average client rating</div></div>
    </div>
  </section>

{cta("Work with us", "Ready to meet the <em>crew?</em>", "Request a Free Estimate", "services.html", "Our Services")}
</main>

"""

# ---------------------------------------------------------------- SERVICES
services_body = f"""<main id="main">

{banner("Services", "Concrete services, <em>elevated.</em>", "Six specialties, one crew, zero shortcuts — from a backyard patio to a full commercial foundation.")}

  <section class="section">
    <div class="container">
      <div class="services-grid">
{service_card("concrete3.png", "Decorative", "Stamped &amp; Decorative", "Slate, cobblestone and wood-plank textures with hand-applied stains for a look no two patios share.", ["Custom stamp patterns &amp; borders", "Acid, water &amp; integral staining", "Sealed for UV &amp; traffic durability"], "contact.html", "Get a quote", "d1")}
{service_card("concrete4.png", "Driveways", "Custom Driveways", "Exposed aggregate, broom-finish or stamped borders engineered for Adelaide's heat cycles.", ["Reinforced for vehicle load", "Control joints placed to prevent cracking", "Exposed aggregate &amp; broom finishes"], "contact.html", "Get a quote", "d2")}
{service_card("concrete5.png", "Outdoor living", "Patios &amp; Outdoor Living", "Full outdoor rooms — fire features, seat walls and kitchens poured to match your home.", ["Fire pits, seat walls &amp; kitchens", "Multi-level &amp; curved layouts", "Matched to existing hardscape"], "contact.html", "Get a quote", "d3")}
{service_card("concrete6.png", "Pool decks", "Pool Decks", "Cool-touch, slip-resistant knockdown finishes built for bare feet in July.", ["Cool-touch coatings &amp; light colors", "Slip-resistant knockdown texture", "Coping &amp; drainage detailing"], "contact.html", "Get a quote", "d1")}
{service_card("concrete7.png", "Countertops", "Concrete Countertops", "Hand-cast, sealed and polished countertops — a one-of-a-kind centerpiece.", ["Hand-cast in our shop, custom molds", "Polished, honed or acid-etched finish", "Integrated sinks &amp; drainboards"], "contact.html", "Get a quote", "d2")}
{service_card("concrete8.png", "Commercial", "Foundations &amp; Commercial", "Engineer-specified foundations, slabs and flatwork for builders and businesses.", ["Engineer-stamped footings &amp; slabs", "Commercial flatwork &amp; parking areas", "Body corporate &amp; builder coordination"], "contact.html", "Get a quote", "d3")}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center reveal">
        <div class="eyebrow">How it works</div>
        <h2 class="section-title">A process built on <em>precision.</em></h2>
        <p class="section-sub">No surprises, no shortcuts. Here's exactly what happens from first call to final walkthrough.</p>
      </div>
      <div class="process-grid">
        <div class="process-step reveal d1">
          <div class="process-num"><span>01</span></div>
          <h4>Consultation</h4>
          <p>We walk your site and talk through vision and budget — free, no pressure.</p>
        </div>
        <div class="process-step reveal d2">
          <div class="process-num"><span>02</span></div>
          <h4>Design &amp; quote</h4>
          <p>A detailed proposal with materials, finish samples and a firm price.</p>
        </div>
        <div class="process-step reveal d3">
          <div class="process-num"><span>03</span></div>
          <h4>Expert installation</h4>
          <p>Our crew forms, pours and hand-finishes on schedule, every time.</p>
        </div>
        <div class="process-step reveal d4">
          <div class="process-num"><span>04</span></div>
          <h4>Final walkthrough</h4>
          <p>We seal, clean up, and walk the finished project with you.</p>
        </div>
      </div>
    </div>
  </section>

{cta("Ready when you are", "Let's pour something <em>permanent.</em>", "Request a Free Estimate", "gallery.html", "See Our Work")}
</main>

"""

# ---------------------------------------------------------------- GALLERY
gallery_body = f"""<main id="main">

{banner("Gallery", "A portfolio worth <em>standing on.</em>", "Driveways, patios, pool decks and decorative work completed across Greater Adelaide. Tap any project to see it larger.")}

  <section class="section">
    <div class="container">
      <div class="gallery-filters reveal" role="group" aria-label="Filter projects">
        <button class="filter-btn active" data-filter="all">All Work</button>
        <button class="filter-btn" data-filter="driveways">Driveways</button>
        <button class="filter-btn" data-filter="patios">Patios</button>
        <button class="filter-btn" data-filter="pool-decks">Pool Decks</button>
        <button class="filter-btn" data-filter="decorative">Decorative</button>
        <button class="filter-btn" data-filter="commercial">Commercial</button>
      </div>
      <div class="gallery-grid reveal" id="galleryGrid">
{gallery_item("concrete9.png", 800, 1000, "driveways", "Driveways", "Belair Hills Estate", "tall")}
{gallery_item("concrete10.png", 1000, 640, "patios", "Patios", "Burnside Residence", "wide")}
{gallery_item("concrete11.png", 700, 640, "pool-decks", "Pool Decks", "Beaumont Pool")}
{gallery_item("concrete12.png", 700, 640, "decorative", "Decorative", "Glenelg Walkway")}
{gallery_item("concrete13.png", 800, 1000, "commercial", "Commercial", "Hindmarsh Plaza", "tall")}
{gallery_item("concrete14.png", 1000, 640, "driveways", "Driveways", "Crafers Custom Home", "wide")}
{gallery_item("concrete23.png", 700, 640, "pool-decks", "Pool Decks", "McLaren Vale Resort Home")}
{gallery_item("concrete24.png", 700, 640, "decorative", "Decorative", "Norwood Kitchen Remodel")}
      </div>
    </div>
  </section>

  <div id="lightbox" role="dialog" aria-modal="true" aria-label="Project photo viewer">
    <button class="lb-close" id="lbClose" aria-label="Close"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg></button>
    <button class="lb-prev" id="lbPrev" aria-label="Previous photo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg></button>
    <div class="lb-inner">
      <img id="lbImg" src="" alt="">
      <div class="lb-cap" id="lbCap"></div>
    </div>
    <button class="lb-next" id="lbNext" aria-label="Next photo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg></button>
  </div>

{cta("Like what you see?", "Your project could be <em>next.</em>", "Request a Free Estimate", "services.html", "Our Services")}
</main>

"""

# ---------------------------------------------------------------- CONTACT
contact_body = f"""<main id="main">

{banner("Contact", "Let's talk about your <em>project.</em>", "Fill out the form or reach us directly — we respond to every inquiry within one business day.")}

  <section class="section">
    <div class="container">
      <div class="contact-grid">
        <div class="reveal-left">
          <div class="contact-info-card">
            <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg></div>
            <div><b>Call or text</b>
            <p><a href="tel:0881234567">(08) 8123 4567</a><br>Mon–Sat, 7am–6pm</p></div>
          </div>
          <div class="contact-info-card">
            <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 6l-10 7L2 6"/><path d="M2 6h20v12H2z"/></svg></div>
            <div><b>Email us</b>
            <p><a href="mailto:hello@stgeorgeconcrete.com.au">hello@stgeorgeconcrete.com.au</a><br>We reply within 24 hours</p></div>
          </div>
          <div class="contact-info-card">
            <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4.5 8-11a8 8 0 10-16 0c0 6.5 8 11 8 11z"/><circle cx="12" cy="11" r="3"/></svg></div>
            <div><b>Visit the yard</b>
            <p>8 Growers Road<br>Wingfield SA 5013</p></div>
          </div>
        </div>

        <form class="contact-form reveal-right" id="contactForm">
          <div class="form-body">
            <div class="form-row">
              <div class="field">
                <label for="fname">Full name</label>
                <input type="text" id="fname" name="name" autocomplete="name" required>
              </div>
              <div class="field">
                <label for="fphone">Phone number</label>
                <input type="tel" id="fphone" name="phone" autocomplete="tel" required>
              </div>
            </div>
            <div class="form-row">
              <div class="field">
                <label for="femail">Email address</label>
                <input type="email" id="femail" name="email" autocomplete="email" required>
              </div>
              <div class="field">
                <label for="fservice">Service needed</label>
                <select id="fservice" name="service">
                  <option value="">Select a service</option>
                  <option>Stamped &amp; Decorative Concrete</option>
                  <option>Custom Driveways</option>
                  <option>Patios &amp; Outdoor Living</option>
                  <option>Pool Decks</option>
                  <option>Concrete Countertops</option>
                  <option>Foundations &amp; Commercial</option>
                </select>
              </div>
            </div>
            <div class="form-row">
              <div class="field full">
                <label for="fmsg">Tell us about your project</label>
                <textarea id="fmsg" name="message" rows="4"></textarea>
              </div>
            </div>
            <button type="submit" class="btn btn-solid btn-block"><span>Send My Request</span>{ARROW}</button>
            <p class="form-note">This form is a front-end demo — connect it to your email service or CRM to go live.</p>
          </div>
          <div class="form-success" role="status">
            <div class="ok"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg></div>
            <h3>Request sent</h3>
            <p style="color:var(--ink-2);margin:8px auto 0;">Thanks — we'll get back to you within one business day. Need us sooner? Call <a href="tel:0881234567" style="color:var(--accent);font-weight:600;">(08) 8123 4567</a>.</p>
          </div>
        </form>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container area-grid">
      <div class="area-copy reveal-left">
        <div class="eyebrow">Where we work</div>
        <h2 class="section-title">Proudly serving <em>Greater Adelaide.</em></h2>
        <p>Based in Wingfield, our crews cover all of Greater Adelaide — from beachside suburbs to Adelaide Hills communities. If you're nearby but not on the list, call us; we probably pour there too.</p>
      </div>
      <div class="ledger reveal-right" aria-label="Service area and distance from headquarters">
        <div class="ledger-head"><span>Service area</span><span>From our yard</span></div>
        <div class="ledger-row"><b>Wingfield</b><span class="hq">HQ</span></div>
        <div class="ledger-row"><b>Port Adelaide</b><span>6 km</span></div>
        <div class="ledger-row"><b>Norwood</b><span>12 km</span></div>
        <div class="ledger-row"><b>Glenelg</b><span>14 km</span></div>
        <div class="ledger-row"><b>Mount Barker</b><span>35 km</span></div>
        <div class="ledger-row"><b>Gawler</b><span>40 km</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container faq-grid">
      <div class="reveal-left">
        <div class="eyebrow">Good to know</div>
        <h2 class="section-title" style="margin-top:18px;">Frequently asked <em>questions.</em></h2>
        <p class="section-sub" style="margin-top:14px;">Can't find your answer? Call us at <a href="tel:0881234567" style="color:var(--accent);font-weight:600;">(08) 8123 4567</a> — a real human answers.</p>
      </div>
      <div class="faq-list reveal-right">
        <div class="faq-item open">
          <button class="faq-q" type="button"><span>How much does concrete cost per square foot?</span><span class="faq-plus" aria-hidden="true"></span></button>
          <div class="faq-a"><p>Basic broom-finish concrete typically runs $90–$130/m² installed, while stamped and decorative work runs $150–$260/m² depending on pattern, colour and site prep. Every quote includes a full line-item breakdown — no surprises.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" type="button"><span>How long does concrete take to cure?</span><span class="faq-plus" aria-hidden="true"></span></button>
          <div class="faq-a"><p>Concrete is typically safe to walk on in 24–48 hours and drivable in about 7 days. Full structural cure takes roughly 28 days, though the surface is fully usable well before then.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" type="button"><span>Do you offer free estimates?</span><span class="faq-plus" aria-hidden="true"></span></button>
          <div class="faq-a"><p>Always. We'll walk your site, discuss finishes and provide a firm, written quote — usually within 48 hours — at no cost or obligation.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" type="button"><span>What's the difference between stamped and stained concrete?</span><span class="faq-plus" aria-hidden="true"></span></button>
          <div class="faq-a"><p>Stamping presses a texture (stone, slate, wood) into wet concrete for a 3D pattern. Staining adds color and depth to the surface. Most premium projects combine both for a natural stone look.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" type="button"><span>Do you work with body corporates and builders?</span><span class="faq-plus" aria-hidden="true"></span></button>
          <div class="faq-a"><p>Yes — we regularly work directly with body corporates, architects and builders on new-build and community projects across Greater Adelaide, and handle all required documentation.</p></div>
        </div>
      </div>
    </div>
  </section>

</main>

"""

PAGES = {
    "index.html": {
        "title": "St George Concrete Solutions | Premium Concrete in Adelaide, SA",
        "desc": "Adelaide's premier concrete design & installation company. Stamped concrete, driveways, patios, pool decks & more. Licensed, insured, 15+ years.",
        "active": "index", "body": index_body,
    },
    "about.html": {
        "title": "About Us | St George Concrete Solutions",
        "desc": "15+ years of concrete craftsmanship in Adelaide. Meet the crew behind St George Concrete Solutions.",
        "active": "about", "body": about_body,
    },
    "services.html": {
        "title": "Services | St George Concrete Solutions",
        "desc": "Stamped concrete, driveways, patios, pool decks, countertops & foundations — Adelaide's premium concrete services.",
        "active": "services", "body": services_body,
    },
    "gallery.html": {
        "title": "Gallery | St George Concrete Solutions",
        "desc": "Browse driveways, patios, pool decks, decorative and commercial concrete projects completed across Greater Adelaide, South Australia.",
        "active": "gallery", "body": gallery_body,
    },
    "contact.html": {
        "title": "Contact | St George Concrete Solutions",
        "desc": "Get a free concrete estimate in Adelaide, Norwood, Glenelg, Port Adelaide, Mount Barker & Gawler, South Australia.",
        "active": "contact", "body": contact_body,
    },
}

for fname, cfg in PAGES.items():
    html = (HEAD.replace("@@TITLE@@", cfg["title"]).replace("@@DESC@@", cfg["desc"])
            + header(cfg["active"]) + "\n" + cfg["body"] + FOOTER)
    (OUT / fname).write_text(html, encoding="utf-8")
    print(f"wrote {fname} ({len(html):,} bytes)")
