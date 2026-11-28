"""Product pages plus the studio, contact, privacy and brand pages."""
import site_kit as kit

P = "https://play-lh.googleusercontent.com/"
PLAY = "https://play.google.com/store/apps/details?id="

ITEMS = [
    dict(slug="md-boltmaster", name="MD Bolt Master", tag="Puzzle game · Android", store=PLAY + "com.mdnexa.boltmaster",
         icon=P + "4yEAavGbMxrFpBz5tyvDInHqL6vtW7CPzgmMX9KZOUSeUCzV5CM18agjNgEiVWfc3uplbkHhShLhm-TtH76m=w128",
         shot=P + "EOpc2deXIaDpmEWtNEsp5xJWX-EBV4wKI86L8iG7gwfefNr_vZPuMTAAyCvAu6NNsPukH1WJy0qylEiKV6WCssM=w1200",
         lead="Sort every colour onto its own screw until the board is clean. One rule, taught in ten seconds, then a hundred boards that each ask for something slightly different.",
         specs=[("Price", "Free, no ads gate"), ("Languages", "14"), ("Offline", "Every level"), ("Platform", "Android 8+")],
         paras=[("How it plays", "Bolts arrive stacked in colours. You move a nut onto the screw of the same colour; a screw holds only its own. Levels grow by adding colours, tighter spacing and a few parts that need to be freed before others can move."),
                ("How it is built", "The board is generated from a solved state, so a level can never be impossible. Stars are earned per solve and spent on hints; the daily board is the same for every player and resets at local midnight.")],
         bullets=["A daily board shared by every player", "Stars for hints, earned by solving, never sold", "Written by hand in fourteen languages"]),
    dict(slug="md-darkflow", name="MD Darkflow", tag="Puzzle game · Android", store="",
         icon="", shot="",
         lead="Tap an arrow and it leaves the board, but only if its path is clear. A hundred levels, three hearts, and one hint a day.",
         specs=[("Status", "Google Play listing in progress"), ("Levels", "100"), ("Lives", "Three hearts"), ("Platform", "Android")],
         paras=[("How it plays", "Arrows sit on a black board pointing in four directions. Tap one and it slides off if nothing blocks the way; tap the wrong one and you lose a heart. The board is fully visible, so every loss is a mistake you can see coming next time."),
                ("How it is built", "Levels are authored, not generated, and ordered by the number of moves a clean solve needs. Three hearts per attempt, a hint that refills daily, and no timer anywhere.")],
         bullets=["Fully visible boards, no guessing", "Three hearts, no energy timers", "Hint refills once a day"]),
    dict(slug="md-corpses", name="MD Corpses", tag="Game · Android", store=PLAY + "com.mdnexa.corpses",
         icon=P + "91apiWvNTjeAWJCf8wo_HKsepd55pk3MWvSxJkQhf5qsgI42LqsdKtzyXTvPmvBPMbkmcT3qivD-QXLfdlTPigk=w128",
         shot=P + "3ghx6RV5WtiKKoCKqPeQ8PPArXeYnBix9XSTViZmUK9ZQaZFYxPwujSlhza6cBMMY1ThYyl4Rd9uNEluqCTarA=w1200",
         lead="A climbing game played with one finger: reach a little further each run and learn the rhythm of the mountain.",
         specs=[("Price", "Free"), ("Input", "One finger"), ("Sessions", "Under a minute"), ("Platform", "Android")],
         paras=[("How it plays", "Hold to grip, release to drop, and time the grab as the surface moves. Runs are short on purpose: you either reach the next ledge or you learn why you missed it."),
                ("How it is built", "Hand-tuned levels rather than an endless generator, so difficulty is deliberate. Nothing is locked behind an advert or a waiting timer.")],
         bullets=["One-finger control", "Short, repeatable runs", "No ad gates"]),
    dict(slug="md-work", name="MD Work", tag="Tool · Android", store=PLAY + "app.mdwork.notebook",
         icon=P + "sdqeJ5I8FS-lzxo3RT74YvVxdQ2R7m_jmhVFCme0NIN4H41gw2W_NiNLGXLfNLd69UMlvll3fj0ny4QhWOUtJg=w128",
         shot=P + "08UuRynGeMEUbVUl-MOWjDio4aOuQSthSuvRKov__tUz4zfyPZNSRbiDQl3qM_fPh6lxSgN9AI288m3pErSBsA=w1200",
         lead="A day-rate notebook for freelancers. Log the days you worked, pick a currency, and hand a client a clean figure.",
         specs=[("Sign-in", "Not required"), ("Storage", "On your device"), ("Currencies", "28"), ("Platform", "Android")],
         paras=[("What it does", "Set a daily rate and a currency, then mark the days you worked. MD Work keeps the month total, a yearly view and a short summary you can copy into an invoice."),
                ("What it does not do", "No account, no cloud, no analytics. Your notes stay in the app on your phone, which also means an uninstalled app takes its data with it.")],
         bullets=["Day and hour rates side by side", "28 currencies", "Nothing leaves your device"]),
]


def product(it):
    shot = (f'<div class="shot"><img src="{it["shot"]}" alt="{it["name"]}" loading="lazy"></div>' if it["shot"]
            else '<div class="shot soon"><b>MD Darkflow</b><span>Google Play listing in progress</span></div>')
    icon = f'<img src="{it["icon"]}" alt="" loading="lazy">' if it["icon"] else ""
    cta = (f'<a class="btn" href="{it["store"]}">Get it on Google Play</a>' if it["store"]
           else '<span class="btn ghost" style="cursor:default">Coming to Google Play</span>')
    specs = "".join(f'<li><b>{k}</b><span>{v}</span></li>' for k, v in it["specs"])
    prose = "".join(f'<h2>{h}</h2><p>{p}</p>' for h, p in it["paras"])
    bullets = "".join(f"<li>{b}</li>" for b in it["bullets"])
    body = (f'<main><section class="hero"><div class="wrap"><p class="eyebrow"><i></i>{it["tag"]}</p>'
            f'<h1 class="display">{it["name"]}</h1><p class="lead">{it["lead"]}</p>'
            f'<div class="cta">{cta}<a class="btn ghost" href="/#products">All products</a></div>'
            f'<ul class="specs">{specs}</ul></div></section>'
            f'<section class="blk"><div class="wrap">{shot}<article class="prose">{prose}'
            f'<h2>What you get</h2><ul>{bullets}</ul></article></div></section></main>')
    return kit.page(f"/{it['slug']}/", f'{it["name"]} — MD Nexa', it["lead"][:155], body)


for it in ITEMS:
    kit.write(f"{it['slug']}/index.html", product(it))

STUDIO = """<main><section class="hero"><div class="wrap">
<p class="eyebrow"><i></i>About</p><h1 class="display">A studio that ships,<br><em>then keeps quiet.</em></h1>
<p class="lead">MD Nexa is an independent software studio. We build puzzle games and small tools, publish them ourselves, and keep the catalogue small enough that every product still gets finished.</p></div></section>
<section class="blk"><div class="wrap"><article class="prose">
<h2>What we believe</h2>
<p>Software should be understood without a tutorial. If a screen needs an explanation, the screen is wrong. That rule decides what we build and, more often, what we refuse to ship.</p>
<p>Products should work without a connection, because the interesting moment to play is on a train, in a basement, or on a plane. And nothing should require an account before it does its job.</p>
<h2>How we work</h2>
<p>One product at a time. A game is finished — levels, translations, store page, support — before the next one starts. Updates after launch are corrections and refinements rather than a content treadmill.</p>
<p>Everything is built on Android first because that is where our players are, but the layer under the games is deliberately thin, so a second storefront or a browser build is a wrapper rather than a rewrite.</p>
<h2>Contact</h2>
<p>Write to <a class="link" href="mailto:mdnexa9@gmail.com">mdnexa9@gmail.com</a> or use the <a class="link" href="/contact/">contact page</a>. Replies come from the people who build the apps.</p>
</article></div></section></main>"""
kit.write("studio/index.html", kit.page("/studio/", "Studio — MD Nexa", "MD Nexa is an independent software studio building puzzle games and small tools, one finished product at a time.", STUDIO))

CONTACT = """<main><section class="hero"><div class="wrap">
<p class="eyebrow"><i></i>Contact</p><h1 class="display">Say it plainly.<br><em>We read everything.</em></h1>
<p class="lead">One address for support, press and partnership: <a class="link" href="mailto:mdnexa9@gmail.com">mdnexa9@gmail.com</a>. Most replies go out within two working days.</p></div></section>
<section class="blk"><div class="wrap"><div class="grid3">
<div class="card"><span class="num">01</span><h3>Bugs</h3><p>Name the app, the phone model and what you tapped before it broke. A screenshot helps more than a description.</p></div>
<div class="card"><span class="num">02</span><h3>Press</h3><p>Assets, icons and screenshots are on the <a class="link" href="/brand/">brand page</a>. Ask us for review keys or extra material.</p></div>
<div class="card"><span class="num">03</span><h3>Partnerships</h3><p>Ports, localisation and store publishing. Tell us the platform and the timeline; we answer with a plan, not a deck.</p></div>
</div></div></section></main>"""
kit.write("contact/index.html", kit.page("/contact/", "Contact — MD Nexa", "Contact MD Nexa for support, press assets or partnership questions. Replies within two working days.", CONTACT))

PRIVACY = """<main><section class="hero"><div class="wrap">
<p class="eyebrow"><i></i>Privacy</p><h1 class="display">What we collect:<br><em>as little as possible.</em></h1>
<p class="lead">The short version: this website sets no cookies and runs no analytics, and none of our apps require an account.</p></div></section>
<section class="blk"><div class="wrap"><article class="prose">
<h2>This website</h2><p>Pages are served statically. We do not set cookies, do not run a tracking script and do not build a profile of visitors. Server logs kept by the host contain IP addresses and are used only for security and capacity.</p>
<h2 id="apps">Our apps</h2><p>Games and tools work without an account. Progress and notes are stored on your device. Google Play may collect install and crash data under Google's own policies; the Play listing of each app carries the current data-safety declaration.</p>
<h2>Children</h2><p>None of our apps is directed at children under 13, and we do not knowingly collect personal data from them.</p>
<h2>Your requests</h2><p>To ask what is held about you, or to have it removed, write to <a class="link" href="mailto:mdnexa9@gmail.com">mdnexa9@gmail.com</a>. Because we do not run accounts, deleting an app removes its data with it.</p>
<h2>Changes</h2><p>If this policy changes, the date below changes with it.</p><p><small>Last updated 28 November 2026.</small></p>
</article></div></section></main>"""
kit.write("privacy/index.html", kit.page("/privacy/", "Privacy — MD Nexa", "How MD Nexa handles data: no cookies or analytics on the site, no accounts in the apps, notes stay on your device.", PRIVACY))

BRAND = """<main><section class="hero"><div class="wrap">
<p class="eyebrow"><i></i>Brand</p><h1 class="display">The mark and<br><em>how to use it.</em></h1>
<p class="lead">Three rounded bars — cyan, diagonal, indigo — on a near-black field. The mark stands alone; the wordmark is set in spaced capitals beside it.</p>
<div class="cta"><a class="btn" href="/assets/logo.svg">Download SVG</a><a class="btn ghost" href="/assets/icon-512.png">512 px PNG</a></div></div></section>
<section class="blk"><div class="wrap"><div class="grid3">
<div class="card"><span class="num">01</span><h3>Clear space</h3><p>Keep a margin equal to the width of one bar on every side. Never place the mark on a busy photo.</p></div>
<div class="card"><span class="num">02</span><h3>Colour</h3><p>Cyan #4ED5FF to indigo #9E6DF7. On light backgrounds use the dark field tile, not the bare bars.</p></div>
<div class="card"><span class="num">03</span><h3>Don't</h3><p>No outlines, no shadows, no rotation, no recolouring into a single flat hue. Don't rebuild the bars by hand.</p></div>
</div><article class="prose"><h2>Files</h2><ul>
<li><a class="link" href="/assets/logo.svg">logo.svg</a> — transparent vector, for screens</li>
<li><a class="link" href="/assets/logo.png">logo.png</a> — 256 px transparent PNG</li>
<li><a class="link" href="/assets/icon-512.png">icon-512.png</a> — app icon, rounded field</li>
<li><a class="link" href="/assets/apple-touch-icon.png">apple-touch-icon.png</a> — 180 px</li>
</ul></article></div></section></main>"""
kit.write("brand/index.html", kit.page("/brand/", "Brand — MD Nexa", "The MD Nexa mark, its colours and clear-space rules, plus downloadable logo files.", BRAND))
print("pages done")
