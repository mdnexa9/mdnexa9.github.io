"""Wire the two new games into the home page, the games panel and the articles hub.

Idempotent: every step checks for its marker and does nothing when already applied.
"""
import pathlib
import re

PLAY_BOLT = "https://play.google.com/store/apps/details?id=com.mdnexa.boltmaster"
PLAY_DARK = "https://play.google.com/store/apps/details?id=com.mdnexa.Darkflow"
ARROW = (
    '<svg class="arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8" '
    'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
    'stroke-linejoin="round"/></svg>'
)

AR_CARD = """<div class="card">
              <div class="card-top">
                <img class="card-icon" src="assets/{icon}" alt="{name}" width="64" height="64" loading="lazy" decoding="async">
                <span class="pill" data-en="On Google Play">على Google Play</span>
              </div>
              <h3 class="card-name"><a href="{page}">{name}</a></h3>
              <p class="card-tagline" data-en="{tag_en}">{tag_ar}</p>
              <p class="card-desc" data-en="{desc_en}">{desc_ar}</p>
              <div class="card-meta">
                <span class="meta">Android</span>
                <span class="meta">Google Play</span>
                <span class="meta" data-en="Free">مجاني</span>
              </div>
              <div class="card-foot">
                <a class="card-cta" href="{play}" target="_blank" rel="noopener"><span data-en="Open in Play Store">افتح في بلاي ستور</span>
                  {arrow}
                </a>
              </div>
            </div>"""

EN_CARD = """<div class="card">
              <div class="card-top">
                <img class="card-icon" src="/assets/{icon}" alt="{name}" width="64" height="64" loading="lazy" decoding="async">
                <span class="pill">On Google Play</span>
              </div>
              <h3 class="card-name">{name}</h3>
              <p class="card-tagline">{tag_en}</p>
              <p class="card-desc">{desc_en}</p>
              <div class="card-meta"><span class="meta">Android</span><span class="meta">Google Play</span><span class="meta">Free</span></div>
              <div class="card-foot"><span class="card-cta"><a href="{play}" target="_blank" rel="noopener">Open in Play Store</a>
                  {arrow}
                </span></div>
            </div>"""

GAMES = {
    "MD Bolt Master": dict(
        icon="game-bolt.svg", page="/md-boltmaster/", play=PLAY_BOLT,
        tag_ar="لغز فرز الصواميل والبراغي", tag_en="The nuts and bolts sort puzzle",
        desc_ar="رتّب كل لون على برغيه: مستويات متدرجة، تحدٍ يومي جديد، ١٤ لغة، واللعبة تعمل بدون إنترنت.",
        desc_en="Sort every colour onto its own bolt: graded levels, a fresh daily challenge, 14 languages and offline play.",
    ),
    "MD Darkflow": dict(
        icon="game-darkflow.svg", page="/md-darkflow/", play=PLAY_DARK,
        tag_ar="لغز الأسهم على زجاج أسود", tag_en="The neon arrow puzzle",
        desc_ar="اضغط الأسهم لتفرغ اللوحة: ١٠٠ مستوى، تحدٍ يومي مشترك، ثلاثة قلوب وتلميح، ويعمل بدون إنترنت.",
        desc_en="Tap the arrows off the grid: 100 levels, a shared daily board, three hearts and a hint, all offline.",
    ),
}


def soon_blocks(text):
    """Find every .card--soon block with its exact span."""
    found = []
    for m in re.finditer(r'<(button|div) class="card card--soon"[^>]*>', text):
        if m.group(1) == "button":
            end = text.find("</button>", m.end())
            end = end + len("</button>")
        else:
            depth = 1
            end = m.end()
            for t in re.finditer(r"<div\b|</div>", text[m.end():]):
                depth += 1 if t.group(0) == "<div" else -1
                if depth == 0:
                    end = m.end() + t.end()
                    break
        found.append((m.start(), end, text[m.start():end]))
    return found


def patch_home(path, lang):
    p = pathlib.Path(path)
    text = p.read_text(encoding="utf-8")
    changed = False
    if "card--soon" in text:
        for start, end, block in reversed(soon_blocks(text)):
            name = next((n for n in GAMES if n in block), None)
            if not name:
                continue
            data = dict(GAMES[name])
            tpl = AR_CARD if lang == "ar" else EN_CARD
            if lang == "ar":
                new = tpl.format(arrow=ARROW, **data)
            else:
                new = tpl.format(arrow=ARROW, **{k: v for k, v in data.items() if k in
                                                 ("icon", "name", "tag_en", "desc_en", "play")})
            text = text[:start] + new + text[end:]
            changed = True
    if lang == "ar" and "md-boltmaster/" not in text:
        anchor = "</div>\n        </div>"
        extra = ('\n            <div class="hero-actions" style="margin-block-start:22px">\n'
                 '              <a class="btn btn-outline" href="/md-boltmaster/">صفحة MD Bolt Master</a>\n'
                 '              <a class="btn btn-outline" href="/md-darkflow/">صفحة MD Darkflow</a>\n'
                 '            </div>')
        idx = text.find("panel-games")
        close = text.find(anchor, idx)
        if idx > 0 and close > 0:
            text = text[:close + len("</div>")] + extra + text[close + len("</div>"):]
            changed = True
    if changed:
        p.write_text(text, encoding="utf-8")
        print("patched", path)


HUB = """
    <section class="products">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow"><span class="dot" aria-hidden="true"></span>ألعابنا</p>
          <h2 class="section-title">مقالات عن ألعابنا الجديدة</h2>
          <p class="section-sub">أدلة قصيرة لـ MD Darkflow وMD Bolt Master، من إعداد فريق MD Nexa.</p>
        </div>
        <div class="cards">
          <a class="card" href="/articles/arrow-puzzle-strategy/"><h3 class="card-name">سبع قواعد تحلّ بها أي لوحة أسهم</h3><p class="card-desc">البداية من الحواف، وعدّ السدادات، ومتى تستخدم التلميح.</p></a>
          <a class="card" href="/articles/arrow-puzzle-daily-challenge/"><h3 class="card-name">كيف تبني سلسلة في التحدي اليومي</h3><p class="card-desc">خطة لوحة اليوم بقلبين وتلميح واحد.</p></a>
          <a class="card" href="/articles/best-offline-puzzle-games/"><h3 class="card-name">أفضل ألعاب ألغاز تعمل بدون إنترنت</h3><p class="card-desc">كيف تختار لعبة تفتح في الطائرة.</p></a>
          <a class="card" href="/articles/nuts-and-bolts-sort-tips/"><h3 class="card-name">كيف ترتّب الصواميل دون أن تعلق</h3><p class="card-desc">خمس قواعد تمنع إغلاق اللوحة.</p></a>
          <a class="card" href="/articles/bolt-master-level-guide/"><h3 class="card-name">دليل مستويات MD Bolt Master</h3><p class="card-desc">ما يتغيّر في كل مرحلة وكيف تستخدم النجوم.</p></a>
          <a class="card" href="/articles/color-sort-puzzle-benefits/"><h3 class="card-name">لماذا ألغاز فرز الألوان مريحة للدماغ</h3><p class="card-desc">قاعدة واحدة وجلسات قصيرة بلا مؤقت.</p></a>
        </div>
        <p class="section-sub" style="margin-block-start:22px"><a href="/games/">كل الألعاب والأدلة →</a></p>
      </div>
    </section>
"""


def patch_hub():
    p = pathlib.Path("articles/index.html")
    if not p.exists():
        return
    text = p.read_text(encoding="utf-8")
    if "arrow-puzzle-strategy" in text or "</main>" not in text:
        return
    text = text.replace("</main>", HUB + "  </main>", 1)
    p.write_text(text, encoding="utf-8")
    print("patched articles hub")


def swap_og_image():
    for f in pathlib.Path(".").rglob("*.html"):
        text = f.read_text(encoding="utf-8")
        if "og-cover.jpg" in text:
            f.write_text(text.replace("og-cover.jpg", "og-image.jpg"), encoding="utf-8")
            print("og image", f)


def extend_llms():
    p = pathlib.Path("llms.txt")
    if not p.exists():
        return
    text = p.read_text(encoding="utf-8")
    if "md-darkflow" in text:
        return
    text += "\n## Games\n- MD Darkflow: https://mdnexa.online/md-darkflow/ (Play: " + PLAY_DARK + ")\n"
    text += "- MD Bolt Master: https://mdnexa.online/md-boltmaster/ (Play: " + PLAY_BOLT + ")\n"
    text += "- Games hub and guides: https://mdnexa.online/games/\n"
    p.write_text(text, encoding="utf-8")
    print("extended llms.txt")


if __name__ == "__main__":
    patch_home("index.html", "ar")
    patch_home("en/index.html", "en")
    patch_hub()
    swap_og_image()
    extend_llms()
    print("done")
