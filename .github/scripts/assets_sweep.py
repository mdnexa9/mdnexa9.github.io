"""Every page gets the full icon set, the new share card and a fresh lastmod."""
import pathlib
import re

HEADSET = ('<link rel="manifest" href="/site.webmanifest">'
           '<link rel="icon" href="/favicon.ico" sizes="any">'
           '<link rel="icon" type="image/png" sizes="32x32" href="/assets/icon-32.png">'
           '<link rel="icon" type="image/png" sizes="192x192" href="/assets/icon-192.png">'
           '<link rel="icon" type="image/png" sizes="512x512" href="/assets/icon-512.png">'
           '<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">')

OLD_ICON = re.compile(r'<link rel="(?:shortcut )?icon"[^>]*>|<link rel="apple-touch-icon"[^>]*>', re.I)
OG = re.compile(r'<meta property="og:image" content="[^"]*"[^>]*>')

changed = 0
for path in sorted(pathlib.Path(".").rglob("*.html")):
    if any(part.startswith(".") for part in path.parts):
        continue
    html = path.read_text(encoding="utf-8")
    if not html.lstrip().lower().startswith("<!doctype") and "<head" not in html:
        continue
    before = html
    if '/assets/icon-192.png' not in html:
        html = OLD_ICON.sub("", html)
        html = html.replace("</head>", HEADSET + "</head>", 1)
    html = OG.sub('<meta property="og:image" content="https://mdnexa.online/assets/og-image.jpg">', html)
    if html != before:
        path.write_text(html, encoding="utf-8")
        changed += 1
print("pages updated:", changed)

sm = pathlib.Path("sitemap.xml")
if sm.exists():
    xml = sm.read_text(encoding="utf-8")
    if "<lastmod>" in xml:
        xml = re.sub(r"<lastmod>[^<]*</lastmod>", "<lastmod>2026-11-28</lastmod>", xml)
    else:
        xml = xml.replace("<loc>", "<lastmod>2026-11-28</lastmod><loc>")
    sm.write_text(xml, encoding="utf-8")
    print("sitemap lastmod refreshed")
