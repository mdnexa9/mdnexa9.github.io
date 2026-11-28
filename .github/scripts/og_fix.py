"""1200x630 share card: the mark cropped tight and centred on the studio field."""
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from brand_assets import mark  # noqa: E402

W, H = 1200, 630
card = Image.new("RGB", (W, H), (5, 6, 12))
glow = Image.new("RGB", (W, H), (5, 6, 12))
gd = ImageDraw.Draw(glow)
for i in range(40, 0, -1):
    r = 90 + i * 7
    gd.ellipse([W // 2 - r, H // 2 - r * 0.62, W // 2 + r, H // 2 + r * 0.62],
               fill=(8 + i // 5, 6 + i // 6, 22 + i // 2))
card = Image.blend(card, glow.filter(ImageFilter.GaussianBlur(60)), 0.9)

m = mark()
m = m.crop(m.getbbox())
scale = (H * 0.62) / m.height
m = m.resize((int(m.width * scale), int(m.height * scale)), Image.LANCZOS)
card.paste(m, ((W - m.width) // 2, (H - m.height) // 2), m)
card.save("assets/og-image.jpg", quality=90, optimize=True)
print("og-image.jpg", card.size, pathlib.Path("assets/og-image.jpg").stat().st_size, "bytes")
