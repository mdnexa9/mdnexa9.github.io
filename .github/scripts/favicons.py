"""Icon set, social card, manifest, mobile header fix and hreflang for every page."""
import json
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from brand_assets import mark  # noqa: E402

root = pathlib.Path(".")
assets = root / "assets"
SIZES = (16, 32, 48, 96, 144, 180, 192, 256, 384, 512)
base = mark().crop(mark().getbbox())
side = max(base.size)
square = Image.new("RGBA", (side, side), (0, 0, 0, 0))
square.alpha_composite(base, ((side - base.width) // 2, (side - base.height) // 2))

for size in SIZES:
    square.resize((size, size), Image.LANCZOS).save(assets / f"icon-{size}.png", optimize=True)
print("icons:", len(SIZES))

# iOS wants an opaque tile, so put the mark on the dark rounded field.
tile = Image.new("RGB", (2048, 2048), (7, 10, 22))
mask = Image.new("L", (2048, 2048), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, 2047, 2047], radius=460, fill=255)
glow = Image.new("RGB", (2048, 2048), (7, 10, 22))
gd = ImageDraw.Draw(glow)
for i in range(22, 0, -1):
    r = int(2048 * (0.28 + i * 0.012))
    gd.ellipse([1024 - r, 800 - r * 0.8, 1024 + r, 800 + r * 0.8], fill=(30 + i * 3, 20 + i * 2, 82 + i * 5))
field = Image.blend(Image.new("RGB", (2048, 2048), (7, 10, 22)), glow.filter(ImageFilter.GaussianBlur(140)), 0.85)
m = mark().resize((int(2048 * 0.68), int(2048 * 0.68)), Image.LANCZOS)
field.paste(m, ((2048 - m.width) // 2, (2048 - m.height) // 2), m)
for size in (180, 512):
    field.resize((size, size), Image.LANCZOS).save(assets / ("apple-touch-icon.png" if size == 180 else "icon-512-rounded.png"), optimize=True)
print("touch icons done")

# Social card
og = Image.new("RGB", (1200, 630), (5, 6, 12))
od = ImageDraw.Draw(og)
for i in range(60, 0, -1):
    r = 120 + i * 6
    od.ellipse([600 - r, 300 - r * 0.7, 600 + r, 300 + r * 0.7], fill=(10 + i // 6, 8 + i // 8, 26 + i // 3))
og = og.filter(ImageFilter.GaussianBlur(46))
mk = mark().resize((620, 620), Image.LANCZOS)
og.paste(mk, (290, 5), mk)
og.save(assets / "og-image.jpg", quality=88, optimize=True)
print("social card done")

(root / "site.webmanifest").write_text(json.dumps({
    "name": "MD Nexa",
    "short_name": "MD Nexa",
    "icons": [
        {"src": "/assets/icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "/assets/icon-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "/assets/icon-512-rounded.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
    ],
    "theme_color": "#05060c",
    "background_color": "#05060c",
    "display": "standalone",
    "start_url": "/",
}, indent=2), encoding="utf-8")
print("manifest written")

Image.open(assets / "icon-48.png").save(root / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("favicon.ico written")

kit = pathlib.Path(".github/scripts/site_kit.py")
src = kit.read_text(encoding="utf-8")
BLOCK = '''
CSS += "@media(max-width:760px){header.site .bar{flex-wrap:wrap;padding:10px 0;gap:6px}.brand{white-space:nowrap}nav.main{width:100%;margin-left:0;overflow-x:auto;gap:18px;font-size:13.5px;padding:2px 0 6px}nav.main::-webkit-scrollbar{display:none}.hero h1{letter-spacing:-.02em}}"
_HEADSET = ('<link rel="manifest" href="/site.webmanifest">'
            '<link rel="icon" href="/favicon.ico" sizes="any">'
            '<link rel="icon" type="image/png" sizes="32x32" href="/assets/icon-32.png">'
            '<link rel="icon" type="image/png" sizes="192x192" href="/assets/icon-192.png">'
            '<link rel="icon" type="image/png" sizes="512x512" href="/assets/icon-512.png">'
            '<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">'
            '<meta name="apple-mobile-web-app-title" content="MD Nexa">'
            '<link rel="alternate" hreflang="en" href="https://mdnexa.online/">'
            '<link rel="alternate" hreflang="ar" href="https://mdnexa.online/ar/">'
            '<link rel="alternate" hreflang="x-default" href="https://mdnexa.online/">')
SHELL = SHELL.replace("</head>", _HEADSET + "</head>", 1)
'''
if "_HEADSET" not in src:
    kit.write_text(src + BLOCK, encoding="utf-8")
    print("site_kit.py: head set appended")
else:
    print("site_kit.py: already patched")
