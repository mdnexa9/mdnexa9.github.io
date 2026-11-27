"""Put the real Google Play icon and banner on the homepage and game pages."""
import pathlib
import re

BOLT_ICON = "https://play-lh.googleusercontent.com/4yEAavGbMxrFpBz5tyvDInHqL6vtW7CPzgmMX9KZOUSeUCzV5CM18agjNgEiVWfc3uplbkHhShLhm-TtH76m"
BOLT_SHOT = "https://play-lh.googleusercontent.com/EOpc2deXIaDpmEWtNEsp5xJWX-EBV4wKI86L8iG7gwfefNr_vZPuMTAAyCvAu6NNsPukH1WJy0qylEiKV6WCssM"
WORK_ICON = "https://play-lh.googleusercontent.com/sdqeJ5I8FS-lzxo3RT74YvVxdQ2R7m_jmhVFCme0NIN4H41gw2W_NiNLGXLfNLd69UMlvll3fj0ny4QhWOUtJg"
WORK_SHOT = "https://play-lh.googleusercontent.com/08UuRynGeMEUbVUl-MOWjDio4aOuQSthSuvRKov__tUz4zfyPZNSRbiDQl3qM_fPh6lxSgN9AI288m3pErSBsA"
CORPSE_ICON = "https://play-lh.googleusercontent.com/91apiWvNTjeAWJCf8wo_HKsepd55pk3MWvSxJkQhf5qsgI42LqsdKtzyXTvPmvBPMbkmcT3qivD-QXLfdlTPigk"
CORPSE_SHOT = "https://play-lh.googleusercontent.com/3ghx6RV5WtiKKoCKqPeQ8PPArXeYnBix9XSTViZmUK9ZQaZFYxPwujSlhza6cBMMY1ThYyl4Rd9uNEluqCTarA"
CSS = """.mdcards{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(290px,1fr))}
.mdcard{background:#0b0e1a;border:1px solid #1c2237;border-radius:20px;overflow:hidden;display:flex;flex-direction:column}
.mdcard>a{display:block;line-height:0}
.mdimg{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}
.mdfallback{aspect-ratio:16/9;display:flex;align-items:center;justify-content:center;background:radial-gradient(circle at 50% 45%,#241b52,#0a0d18 72%);line-height:1.2}
.mdfallback b{font-size:19px;letter-spacing:.03em;color:#cfc6ff}
.mdrow{display:flex;gap:14px;padding:16px 18px 20px;align-items:flex-start}
.mdic{width:54px;height:54px;border-radius:15px;flex:0 0 auto}
.mdrow h3{margin:0 0 5px;font-size:17px}
.mdrow p{margin:0;color:#94a1be;font-size:14px;line-height:1.55}
.mdsec{max-width:1080px;margin:0 auto;padding:70px 22px}
.mdsec h2{font-size:clamp(26px,3.4vw,36px);margin:0 0 10px;line-height:1.15}
.mdsec p.mdl{color:#9aa6c4;max-width:62ch;margin:0 0 30px;font-size:16.5px;line-height:1.65}
.mdabout{background:#080a13;border-top:1px solid #151b2c;border-bottom:1px solid #151b2c}
"""


def card(href, img, icon, title, text, alt):
    top = f'<a href="{href}"><img class="mdimg" src="{img}=w1000" alt="{alt}" loading="lazy"></a>' if img else f'<a href="{href}" class="mdfallback"><b>{title}</b></a>'
    pic = f'<img class="mdic" src="{icon}=w128" alt="{title} icon" loading="lazy">' if icon else ""
    return f'<article class="mdcard">{top}<div class="mdrow">{pic}<div><h3>{title}</h3><p>{text}</p></div></div></article>'


EN = """<style>%s</style><section class="mdsec" id="studio"><h2>What the studio makes</h2><p class="mdl">Games and small tools, each built around one clear idea. The artwork below is the artwork on Google Play.</p><div class="mdcards">%s</div></section><section class="mdsec mdabout" id="about"><h2>About the studio</h2><p class="mdl">MD Nexa is an independent software studio. We build puzzle games and small tools, and we keep every screen quiet enough to use one-handed on a phone.</p><p class="mdl">Our apps live on Google Play for now. Nothing in the way we build ties us to a single store, so publishing elsewhere later will be an addition rather than a rebuild.</p></section>"""

AR = """<style>%s</style><section class="mdsec" id="studio"><h2>ماذا يصنع الاستوديو</h2><p class="mdl">ألعاب وأدوات صغيرة، كل واحدة مبنية حول فكرة واحدة واضحة. الصور التالية هي نفسها المعروضة على Google Play.</p><div class="mdcards">%s</div></section><section class="mdsec mdabout" id="about"><h2>من نحن</h2><p class="mdl">‏MD Nexa استوديو برمجيات مستقل. نبني ألعاب ألغاز وأدوات صغيرة، ونحرص أن تبقى كل شاشة هادئة وتُستخدم بيد واحدة على الهاتف.</p><p class="mdl">تطبيقاتنا موجودة اليوم على Google Play. ولا شيء في طريقة بنائنا يحبسنا في متجر واحد؛ النشر على متجر آخر لاحقاً سيكون إضافة لا إعادة بناء.</p></section>"""

EN_CARDS = "".join([
    card("/md-boltmaster/", BOLT_SHOT, BOLT_ICON, "MD Bolt Master", "Colour sorting on Android. Fourteen languages, plays offline, free on Google Play.", "MD Bolt Master store banner"),
    card("/md-darkflow/", "", "", "MD Darkflow", "Neon arrows and three hearts. The Google Play listing is still being set up.", "MD Darkflow"),
    card("/md-work/", WORK_SHOT, WORK_ICON, "MD Work", "A day-rate notebook for freelancers. No account needed.", "MD Work store banner"),
    card("/md-corpses/", CORPSE_SHOT, CORPSE_ICON, "MD Corpses", "A climbing game played with one finger.", "MD Corpses store banner"),
])
AR_CARDS = "".join([
    card("/md-boltmaster/", BOLT_SHOT, BOLT_ICON, "MD Bolt Master", "ترتيب الألوان على أندرويد. أربع عشرة لغة، يعمل بلا إنترنت، ومجاني على Google Play.", "بانر MD Bolt Master من المتجر"),
    card("/md-darkflow/", "", "", "MD Darkflow", "أسهم مضيئة وثلاثة قلوب. صفحة المتجر على Google Play قيد التجهيز.", "MD Darkflow"),
    card("/md-work/", WORK_SHOT, WORK_ICON, "MD Work", "دفتر أيام عمل للمستقلّين، دون تسجيل حساب.", "بانر MD Work من المتجر"),
    card("/md-corpses/", CORPSE_SHOT, CORPSE_ICON, "MD Corpses", "لعبة تسلّق بإصبع واحد.", "بانر MD Corpses من المتجر"),
])


def rebuild(path, block):
    f = pathlib.Path(path)
    h = f.read_text(encoding="utf-8")
    if "mdcards" in h:
        print(path, "already has cards")
        return
    cut = h.find("<style>\n.mdsec")
    if cut == -1:
        cut = h.find("<style>.mdsec")
    end = h.find("</main>")
    if cut != -1 and end > cut:
        h = h[:cut] + block + "\n" + h[end:]
    else:
        h = h.replace("</main>", block + "\n</main>", 1)
    f.write_text(h, encoding="utf-8")
    print(path, "rebuilt")


rebuild("index.html", EN % (CSS, EN_CARDS))
rebuild("ar/index.html", AR % (CSS, AR_CARDS))

HERO = ('<figure class="mdhero" style="max-width:980px;margin:8px auto 0;padding:0 22px">'
        '<img src="{icon}=w160" alt="{t} icon" style="width:78px;height:78px;border-radius:20px;display:block;margin:0 0 16px">'
        '<img src="{shot}=w1000" alt="{t} on Google Play" style="width:100%;border-radius:22px;display:block">'
        '<figcaption style="margin-top:12px;color:#8d9ab8;font-size:14px">Artwork from the Google Play listing.</figcaption></figure>')

for path, t, icon, shot in (("md-boltmaster/index.html", "MD Bolt Master", BOLT_ICON, BOLT_SHOT),
                            ("md-work/index.html", "MD Work", WORK_ICON, WORK_SHOT),
                            ("md-corpses/index.html", "MD Corpses", CORPSE_ICON, CORPSE_SHOT)):
    f = pathlib.Path(path)
    if not f.exists():
        continue
    h = f.read_text(encoding="utf-8")
    if "mdhero" in h:
        continue
    m = re.search(r'<h1 class="section-title">.*?</h1>', h, re.S)
    if not m:
        print(path, "no h1 anchor")
        continue
    h = h[: m.end()] + HERO.format(icon=icon, shot=shot, t=t) + h[m.end() :]
    f.write_text(h, encoding="utf-8")
    print(path, "hero added")

dark = pathlib.Path("md-darkflow/index.html")
if dark.exists():
    h = dark.read_text(encoding="utf-8")
    if "mdhero" not in h:
        block = ('<div class="mdhero" style="max-width:980px;margin:8px auto 0;padding:0 22px">'
                 '<div style="aspect-ratio:16/9;border-radius:22px;display:flex;flex-direction:column;align-items:center;'
                 'justify-content:center;gap:10px;background:radial-gradient(circle at 50% 45%,#241b52,#0a0d18 72%)">'
                 '<b style="font-size:22px;letter-spacing:.03em;color:#d6ceff">MD Darkflow</b>'
                 '<span style="color:#9d92e0;font-size:14px">Google Play listing coming soon</span></div></div>')
        m = re.search(r'<h1 class="section-title">.*?</h1>', h, re.S)
        if m:
            h = h[: m.end()] + block + h[m.end() :]
            dark.write_text(h, encoding="utf-8")
            print("md-darkflow: placeholder added")
