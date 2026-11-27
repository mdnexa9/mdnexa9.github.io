"""One-shot copy pass over the public pages. Idempotent: every edit is skipped
once its target text is already gone."""
import pathlib
import re

SHOT = "https://play-lh.googleusercontent.com/{}={}"
B1 = "4yEAavGbMxrFpBz5tyvDInHqL6vtW7CPzgmMX9KZOUSeUCzV5CM18agjNgEiVWfc3uplbkHhShLhm-TtH76m"
B2 = "12USW7aflgz466ifDehKTnMoAep_VHxDmKJ6jEBoDZWCSefOC-ThRX14Mqe0r8KF9XCzrpMqJts"
B3 = "EOpc2deXIaDpmEWtNEsp5xJWX-EBV4wKI86L8iG7gwfefNr_vZPuMTAAyCvAu6NNsPukH1WJy0qylEiKV6WCssM"

EN = [
    ("Android puzzle games", "independent software studio"),
    ("Android puzzle games: MD Bolt Master", "MD Bolt Master &amp; MD Darkflow"),
    ("Independent Android studio.", "Independent software studio."),
    ("Made for Android.", "Built for Android today, ready for the next store."),
    (">No account<", ">No timers<"),
    ("and never ask you to sign in.", "and stay out of your way."),
    ("no energy bars, no timers, no sign-up.", "no energy bars, no timers, no noise."),
    ("with no subscription, no trial timer and no account.", "with no subscription and no trial timer."),
]

AR = [
    ("ألعاب ألغاز أندرويد", "استوديو برمجيات وألعاب ألغاز"),
    ("استوديو أندرويد مستقل.", "استوديو برمجيات مستقل."),
    ("صُنع لأندرويد.", "صُنع لأندرويد اليوم، وجاهز للمتاجر القادمة."),
    (">بلا حساب<", ">بلا مؤقت<"),
    ("ولا تطلب منك حساباً.", "وتتركان القرار لك."),
    ("بلا طاقة، بلا مؤقت، بلا تسجيل.", "بلا طاقة، بلا مؤقت، بلا ضجيج."),
    ("بلا اشتراك وبلا مؤقت تجربة وبلا حساب.", "بلا اشتراك وبلا مؤقت تجربة."),
]

CSS = """<style>
.mdsec{max-width:1080px;margin:0 auto;padding:72px 22px}
.mdsec h2{font-size:clamp(26px,3.4vw,38px);margin:0 0 10px;line-height:1.15}
.mdsec p.mdl{color:#9aa6c4;max-width:62ch;margin:0 0 30px;font-size:17px;line-height:1.6}
.mdshots{display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(180px,1fr))}
.mdshots figure{margin:0;background:#0b0e1a;border:1px solid #1c2237;border-radius:20px;overflow:hidden}
.mdshots img{width:100%;display:block;aspect-ratio:9/16;object-fit:cover}
.mdshots figcaption{padding:12px 14px;font-size:13px;color:#8d9ab8}
.mdsoon{display:flex;flex-direction:column;justify-content:center;align-items:center;gap:14px;aspect-ratio:9/16;background:radial-gradient(circle at 50% 45%,#221a4d,#0a0d18 70%)}
.mdsoon b{font-size:19px;letter-spacing:.02em}
.mdsoon span{font-size:12px;color:#a99cf0}
.mdgrid{display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}
.mdgrid article{background:#0b0e1a;border:1px solid #1c2237;border-radius:20px;padding:22px}
.mdgrid h3{margin:0 0 8px;font-size:18px}
.mdgrid p{margin:0;color:#94a1be;font-size:14.5px;line-height:1.6}
.mdabout{background:#080a13;border-top:1px solid #151b2c;border-bottom:1px solid #151b2c}
</style>"""


def shots(lang):
    cap = ["One colour per screw", "Stars to spend on help", "The shared daily board"] if lang == "en" else ["لون واحد لكل برغي", "نجوم تُنفقها على المساعدة", "لوحة اليوم المشتركة"]
    head = ("Inside the games", "Real screens from Google Play, not mockups.") if lang == "en" else ("داخل الألعاب", "لقطات حقيقية من Google Play، لا تصميمات تخييلية.")
    figs = "".join(f'<figure><img src="{SHOT.format(u, "w480-h960")}" alt="{c}" loading="lazy"><figcaption>{c}</figcaption></figure>' for u, c in zip((B1, B2, B3), cap))
    soon = '<b>MD Darkflow</b><span>Store listing coming soon</span>' if lang == "en" else '<b>MD Darkflow</b><span>صفحة المتجر قريباً</span>'
    soonfig = '<figure class="mdsoon">' + soon + '</figure>'
    return f'<section class="mdsec" id="screens"><h2>{head[0]}</h2><p class="mdl">{head[1]}</p><div class="mdshots">{figs}{soonfig}</div></section>'


def wide(lang):
    if lang == "en":
        head, lede = "One studio, several kinds of work", "Puzzle games are where the studio started. The same care goes into a notebook and a one-finger climbing game."
        cards = [("MD Bolt Master", "Colour sorting for Android, fourteen languages, fully offline."),
                 ("MD Darkflow", "Neon arrow puzzles with three hearts. Store listing coming soon."),
                 ("MD Work", "A day-rate notebook for freelancers. No sign-in needed."),
                 ("MD Corpses", "A climbing game played with one finger.")]
    else:
        head, lede = "استوديو واحد، أعمال متنوّعة", "الألغاز هي بداية الاستوديو، والعناية نفسها تمشي مع دفتر الأعمال ولعبة التسلّق بإصبع واحد."
        cards = [("MD Bolt Master", "ترتيب الألوان على أندرويد، أربع عشرة لغة، ويعمل بلا إنترنت."),
                 ("MD Darkflow", "ألغاز أسهم مضيئة بثلاثة قلوب. صفحة المتجر قريباً."),
                 ("MD Work", "دفتر أيام عمل للمستقلّين، دون تسجيل حساب."),
                 ("MD Corpses", "لعبة تسلّق بإصبع واحد.")]
    inner = "".join(f'<article><h3>{a}</h3><p>{b}</p></article>' for a, b in cards)
    return f'<section class="mdsec" id="studio"><h2>{head}</h2><p class="mdl">{lede}</p><div class="mdgrid">{inner}</div></section>'


def about(lang):
    if lang == "en":
        head = "About the studio"
        body = ("MD Nexa is a small independent software studio. We build puzzle games for Android and a handful of tools, "
                "and every screen is written so it works in all fourteen languages we ship and with no internet at all.",
                "You do not need an account to use our apps today. If we add sync or cloud saves later it will be optional: "
                "the app will keep working exactly the same without it.",
                "Android is where our games live now. As the studio grows we will publish on other platforms, and nothing "
                "in the way we build ties us to a single store.")
    else:
        head = "من نحن"
        body = ("MD Nexa استوديو برمجيات مستقل وصغير. نبني ألعاب ألغاز لأندرويد وحزمة أدوات، وكل شاشة مكتوبة لتعمل "
                "بأربع عشرة لغة نشحنها وبدون إنترنت إطلاقاً.",
                "لا تحتاج إلى حساب لاستخدام تطبيقاتنا اليوم. وإن أضفنا المزامنة أو الحفظ السحابي لاحقاً فسيكون اختيارياً: "
                "سيبقى التطبيق يعمل بالشكل نفسه بدونه.",
                "أندرويد هو مكان ألعابنا الآن. ومع نمو الاستوديو سننشر على منصّات أخرى، ولا شيء في طريقة بنائنا "
                "يحبسنا في متجر واحد.")
    ps = "".join(f"<p class=\"mdl\">{b}</p>" for b in body)
    return f'<section class="mdsec mdabout" id="about"><h2>{head}</h2>{ps}</section>'


def patch(path, pairs, lang):
    f = pathlib.Path(path)
    html = f.read_text(encoding="utf-8")
    hits = 0
    for old, new in pairs:
        if old in html:
            html = html.replace(old, new)
            hits += 1
    block = CSS + shots(lang) + wide(lang) + about(lang)
    if "id=\"screens\"" not in html:
        html = html.replace("</main>", block + "\n</main>", 1)
    f.write_text(html, encoding="utf-8")
    print(f"{path}: {hits} text edits")


patch("index.html", EN, "en")
patch("ar/index.html", AR, "ar")

note = pathlib.Path("md-work/index.html")
if note.exists():
    h = note.read_text(encoding="utf-8")
    if "md-nosignin" not in h:
        banner = ('<div class="md-nosignin" style="max-width:900px;margin:18px auto 0;padding:14px 18px;border-radius:14px;'
                  'background:#0d1220;border:1px solid #1d2438;color:#c7d0e6;font-size:15px;line-height:1.6;text-align:center">'
                  'MD Work works without an account. Nothing is locked behind a sign-in, and your notes stay on your device.</div>')
        h = re.sub(r"(<body[^>]*>)", r"\1\n" + banner.replace("\\", "\\\\"), h, count=1)
        note.write_text(h, encoding="utf-8")
        print("md-work: banner added")
