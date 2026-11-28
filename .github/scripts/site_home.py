"""Homepage: identity, flagship products, direction, studio."""
import site_kit as kit

P = "https://play-lh.googleusercontent.com/"
BOLT = dict(name="MD Bolt Master", icon=P + "4yEAavGbMxrFpBz5tyvDInHqL6vtW7CPzgmMX9KZOUSeUCzV5CM18agjNgEiVWfc3uplbkHhShLhm-TtH76m=w128",
            shot=P + "EOpc2deXIaDpmEWtNEsp5xJWX-EBV4wKI86L8iG7gwfefNr_vZPuMTAAyCvAu6NNsPukH1WJy0qylEiKV6WCssM=w1200",
            tag="Puzzle · Android", url="/md-boltmaster/",
            line="Sort every colour onto its own screw. One quiet mechanic, a hundred graded boards, and a daily one everybody shares.",
            tags=["Free on Google Play", "14 languages", "Plays offline"])
WORK = dict(name="MD Work", icon=P + "sdqeJ5I8FS-lzxo3RT74YvVxdQ2R7m_jmhVFCme0NIN4H41gw2W_NiNLGXLfNLd69UMlvll3fj0ny4QhWOUtJg=w128",
            shot=P + "08UuRynGeMEUbVUl-MOWjDio4aOuQSthSuvRKov__tUz4zfyPZNSRbiDQl3qM_fPh6lxSgN9AI288m3pErSBsA=w1200",
            tag="Tool · Android", url="/md-work/",
            line="A day-rate notebook for freelancers: log a day, see the month, hand a client a clean figure. No account, nothing to sync.",
            tags=["No sign-in", "Data stays on your phone"])
CORPSES = dict(name="MD Corpses", icon=P + "91apiWvNTjeAWJCf8wo_HKsepd55pk3MWvSxJkQhf5qsgI42LqsdKtzyXTvPmvBPMbkmcT3qivD-QXLfdlTPigk=w128",
               shot=P + "3ghx6RV5WtiKKoCKqPeQ8PPArXeYnBix9XSTViZmUK9ZQaZFYxPwujSlhza6cBMMY1ThYyl4Rd9uNEluqCTarA=w1200",
               tag="Game · Android", url="/md-corpses/",
               line="A climbing game you can play with one finger: reach a little further each run, learn the rhythm of the mountain.",
               tags=["One-finger play", "Short sessions"])


def prod_block(p, flip=False):
    shot = f'<div class="shot"><img src="{p["shot"]}" alt="{p["name"]}" loading="lazy"></div>'
    tags = "".join(f"<li>{t}</li>" for t in p["tags"])
    body = (f'<div><div class="appname"><img src="{p["icon"]}" alt="" loading="lazy">'
            f'<div><h3>{p["name"]}</h3><p class="tag">{p["tag"]}</p></div></div>'
            f'<p>{p["line"]}</p><ul class="tags">{tags}</ul>'
            f'<a class="link" href="{p["url"]}">Open the {p["name"]} page →</a></div>')
    return f'<div class="prod{" flip" if flip else ""}">{shot}{body}</div>'


DARK = ('<div class="prod flip"><div class="shot soon"><b>MD Darkflow</b><span>Google Play listing in progress</span></div>'
        '<div><div class="appname"><div><h3>MD Darkflow</h3><p class="tag">Puzzle · Android</p></div></div>'
        '<p>Tap an arrow and it leaves the board — but only if its path is clear. A hundred levels, three hearts, and a hint that refills once a day.</p>'
        '<ul class="tags"><li>In review on Google Play</li><li>100 levels</li></ul>'
        '<a class="link" href="/md-darkflow/">Read about MD Darkflow →</a></div></div>')

BODY = f"""<main>
<section class="hero"><div class="wrap">
<p class="eyebrow"><i></i>Independent software studio</p>
<h1 class="display">Small software,<br><em>finished properly.</em></h1>
<p class="lead">MD Nexa builds puzzle games and a few sharp tools. We keep the scope honest, write every screen by hand, and ship things that work on a phone in a basement with no signal.</p>
<div class="cta"><a class="btn" href="#products">See the products</a><a class="btn ghost" href="/studio/">How the studio works</a></div>
<div class="trust"><span>Google Play today</span><span>14 languages</span><span>Offline by default</span><span>No sign-in to play</span></div>
</div></section>
<section class="blk" id="products"><div class="wrap">
<p class="eyebrow"><i></i>The products</p>
<h2 class="sec">Four things we put our name on</h2>
<p class="sec">Each one started as a single sentence. If the sentence needs a paragraph, we cut the feature instead of rewriting the sentence.</p>
{prod_block(BOLT)}{DARK}{prod_block(WORK, True)}{prod_block(CORPSES)}
</div></section>
<section class="blk alt" id="direction"><div class="wrap">
<p class="eyebrow"><i></i>Direction</p>
<h2 class="sec">Android is the start, not the ceiling</h2>
<p class="sec">The studio is built so the same work can leave Google Play without being rebuilt. These are the three doors we are opening next.</p>
<div class="grid3">
<div class="card"><span class="num">01</span><h3>Beyond one store</h3><p>The games are written against a small internal layer, so a second storefront is a new wrapper — not a second codebase.</p></div>
<div class="card"><span class="num">02</span><h3>Beyond the phone</h3><p>Desktop and browser builds are on the table for the puzzle line. The boards already fit any window; the input layer is the work.</p></div>
<div class="card"><span class="num">03</span><h3>Beyond one genre</h3><p>MD Work is the first non-game product. Next are small utilities that share the same rule: one job, done without an account.</p></div>
</div></div></section>
<section class="blk" id="studio"><div class="wrap">
<p class="eyebrow"><i></i>The studio</p>
<h2 class="sec">Independent, small, and deliberately slow</h2>
p.sec
<div class="grid3">
<div class="card"><h3>One product at a time</h3><p>We finish a game before starting the next one. Updates are bugs and refinements, not a content treadmill.</p></div>
<div class="card"><h3>Written by people</h3><p>Every menu and every store page is written and checked in each of the fourteen languages we ship.</p></div>
<div class="card"><h3>Your data stays yours</h3><p>No account is needed to play. Nothing is synced to us unless a product says so on its own page.</p></div>
</div>
<div class="cta"><a class="btn ghost" href="/studio/">About the studio</a><a class="btn ghost" href="/contact/">Contact</a></div>
</div></section>
</main>""".replace("p.sec", '<p class="sec">MD Nexa is a software studio, not a publisher with a catalogue. The games are free, the tool is paid once, and none of it asks you to create an account before you can use it.</p>')

kit.save_css()
kit.write("index.html", kit.page("/", "MD Nexa — independent software studio",
                                  "MD Nexa builds puzzle games and small tools: MD Bolt Master, MD Darkflow, MD Corpses and MD Work. Free, offline and translated by hand.",
                                  BODY))
