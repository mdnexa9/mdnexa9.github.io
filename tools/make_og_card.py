#!/usr/bin/env python3
"""Build assets/og-card.png, the 1200x630 social preview card for MD Nexa.

The card reproduces the brand identity used on the site: the dark navy canvas,
the "N" mark in the cyan-to-violet gradient (same geometry as assets/logo.svg)
and the MD NEXA wordmark in Space Grotesk.

    python3 tools/make_og_card.py                  # writes assets/og-card.png
    python3 tools/make_og_card.py --out /tmp/x.png # write somewhere else

Needs Pillow (pip install pillow) and the Space Grotesk variable font. Point
FONT_PATH at a SpaceGrotesk[wght].ttf, or drop one in /tmp/fonts/. Only the card
is touched; no page is rewritten.
"""
from __future__ import annotations

import argparse
import math
import pathlib
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "og-card.png"

W, H = 1200, 630
BG = (5, 7, 15)
CYAN = (94, 224, 255)
BLUE = (76, 124, 245)
MID_BLUE = (74, 168, 240)
VIOLET = (162, 116, 255)
SOFT = (147, 160, 192)

FONT_CANDIDATES = (
    "/tmp/fonts/SpaceGrotesk-var.ttf",
    "/usr/share/fonts/truetype/space-grotesk/SpaceGrotesk[wght].ttf",
    str(ROOT / "tools" / "SpaceGrotesk[wght].ttf"),
)


def load_font(size: int, weight: int) -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES:
        if pathlib.Path(path).is_file():
            font = ImageFont.truetype(path, size)
            try:
                font.set_variation_by_axes([weight])
            except Exception:
                pass
            return font
    raise SystemExit("Space Grotesk font not found; set FONT_CANDIDATES")


def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def vertical_gradient(size, top, bottom):
    w, h = size
    img = Image.new("RGB", (1, h))
    px = img.load()
    for y in range(h):
        px[0, y] = lerp(top, bottom, y / max(h - 1, 1))
    return img.resize((w, h), Image.BILINEAR)


def rounded_mask(size, box, radius):
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(box, radius=radius, fill=255)
    return mask


def glow(size, center, radius, color, strength):
    """Soft radial light, returned as an RGBA layer."""
    w, h = size
    layer = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(layer)
    steps = 48
    for i in range(steps, 0, -1):
        r = radius * i / steps
        alpha = int(strength * (1 - i / steps) ** 1.7)
        if alpha <= 0:
            continue
        draw.ellipse(
            [center[0] - r, center[1] - r, center[0] + r, center[1] + r],
            fill=alpha,
        )
    layer = layer.filter(ImageFilter.GaussianBlur(radius / 6))
    out = Image.new("RGBA", (w, h), color + (0,))
    out.putalpha(layer)
    return out


def draw_mark(size: int) -> Image.Image:
    """The N mark from assets/logo.svg, drawn at `size` px square."""
    s = size / 120.0 * 4  # 4x supersample, cropped back down later
    canvas = Image.new("RGBA", (int(120 * s), int(120 * s)), (0, 0, 0, 0))

    def bar(box, top, bottom, radius, angle=0.0, pivot=(60, 57)):
        x0, y0, x1, y1 = (v * s for v in box)
        layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        grad = vertical_gradient(
            (int(x1 - x0), int(y1 - y0)), top, bottom
        ).convert("RGBA")
        mask = rounded_mask(
            canvas.size, (x0, y0, x1, y1), radius * s
        )
        grad_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        grad_layer.paste(grad, (int(x0), int(y0)))
        layer.paste(grad_layer, (0, 0), mask)
        if angle:
            layer = layer.rotate(
                angle, resample=Image.BICUBIC, center=(pivot[0] * s, pivot[1] * s)
            )
        canvas.alpha_composite(layer)

    bar((20, 40, 42, 92), CYAN, BLUE, 11)
    bar((78, 26, 100, 92), (91, 134, 255), VIOLET, 11)
    bar((43, 37, 77, 58), MID_BLUE, (124, 91, 246), 10.5, angle=-38)

    bbox = canvas.getbbox()
    mark = canvas.crop(bbox) if bbox else canvas
    height = int(size * 1.0)
    width = round(mark.width * height / mark.height)
    return mark.resize((width, height), Image.LANCZOS)


def build(out: pathlib.Path) -> None:
    card = Image.new("RGBA", (W, H), BG + (255,))

    # Light: cyan from the upper left, violet from the lower right.
    card.alpha_composite(glow((W, H), (250, 120), 620, CYAN, 42))
    card.alpha_composite(glow((W, H), (980, 540), 620, VIOLET, 58))
    card.alpha_composite(glow((W, H), (600, 300), 420, (60, 80, 180), 30))

    # The faint star field used across the site.
    rnd = random.Random(20261126)
    stars = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(stars)
    for _ in range(150):
        x, y = rnd.uniform(0, W), rnd.uniform(0, H)
        r = rnd.choice((1, 1, 1, 2))
        a = rnd.randint(18, 70)
        sd.ellipse([x, y, x + r, y + r], fill=(200, 220, 255, a))
    card.alpha_composite(stars)

    # Vignette to keep the centre readable.
    vign = Image.new("L", (W, H), 0)
    ImageDraw.Draw(vign).ellipse([-180, -260, W + 180, H + 260], fill=255)
    vign = vign.filter(ImageFilter.GaussianBlur(140))
    dark = Image.new("RGBA", (W, H), (0, 0, 0, 120))
    card = Image.composite(card, Image.alpha_composite(card, dark), vign)

    # Mark, with a soft halo behind it.
    mark = draw_mark(196)
    mx = (W - mark.width) // 2
    my = 74
    halo = glow((W, H), (W // 2, my + mark.height // 2), 300, (110, 120, 255), 46)
    card.alpha_composite(halo)
    card.alpha_composite(mark, (mx, my))

    draw = ImageDraw.Draw(card)

    # Wordmark: MD in Light, NEXA in Bold, as on the site.
    y = my + mark.height + 34
    light = load_font(88, 300)
    bold = load_font(88, 700)
    md = "MD"
    nexa = "NEXA"
    gap = 22
    w_md = draw.textlength(md, font=light)
    w_nexa = draw.textlength(nexa, font=bold)
    x = (W - (w_md + gap + w_nexa)) / 2
    draw.text((x, y), md, font=light, fill=(226, 232, 245), anchor="la")
    draw.text((x + w_md + gap, y), nexa, font=bold, fill=(255, 255, 255), anchor="la")

    # Gradient rule.
    rule_y = y + 128
    rule_w = 132
    rule = vertical_gradient((1, 4), CYAN, VIOLET).resize((rule_w, 4), Image.BILINEAR)
    card.alpha_composite(rule.convert("RGBA"), ((W - rule_w) // 2, rule_y))

    # Tagline and domain.
    small = load_font(30, 500)
    draw.text(
        (W // 2, rule_y + 46),
        "Android apps & games",
        font=small,
        fill=SOFT,
        anchor="ma",
    )
    domain_font = load_font(30, 700)
    draw.text(
        (W // 2, rule_y + 92),
        "mdnexa.online",
        font=domain_font,
        fill=(150, 200, 255),
        anchor="ma",
    )

    out.parent.mkdir(parents=True, exist_ok=True)
    card.convert("RGB").save(out, "PNG", optimize=True)
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=str(OUT))
    build(pathlib.Path(parser.parse_args().out))
