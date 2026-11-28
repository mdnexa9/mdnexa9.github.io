"""Render the MD Nexa brand assets from the submitted artwork.

Three rounded bars: short cyan on the left, a diagonal bar in the middle and a
 tall indigo bar on the right, on a near-black navy field with a purple glow.
"""
from PIL import Image, ImageDraw, ImageFilter

S = 2048


def grad(size, top, bottom):
    w, h = size
    img = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(1, h - 1)
        d.line([(0, y), (w, y)], fill=tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)))
    return img


def bar(w, h, r, top, bottom):
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=r, fill=255)
    shape = grad((w, h), top, bottom).convert("RGBA")
    shape.putalpha(mask)
    return shape


def paste_center(canvas, obj, cx, cy):
    canvas.alpha_composite(obj, (int(cx - obj.width / 2), int(cy - obj.height / 2)))


def mark():
    canvas = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    u = S / 1024
    paste_center(canvas, bar(int(97 * u), int(327 * u), int(48 * u), (78, 213, 255), (78, 120, 240)), 388 * u, 421 * u)
    paste_center(canvas, bar(int(97 * u), int(333 * u), int(48 * u), (92, 124, 246), (158, 109, 247)), 703 * u, 338 * u)
    mid = bar(int(97 * u), int(232 * u), int(48 * u), (79, 126, 242), (112, 94, 240))
    paste_center(canvas, mid.rotate(-35, expand=True, resample=Image.BICUBIC), 533 * u, 366 * u)
    return canvas


def tile(size):
    bg = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(bg).rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.22), fill=(7, 10, 22, 255))
    glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for i in range(24, 0, -1):
        rad = int(S * (0.30 + i * 0.010))
        gd.ellipse([S * 0.5 - rad, S * 0.50 - rad * 0.82, S * 0.5 + rad, S * 0.50 + rad * 0.82], fill=(92, 58, 208, int(2.6 * i)))
    bg.alpha_composite(glow.filter(ImageFilter.GaussianBlur(S * 0.045)))
    m = mark().resize((int(S * 0.70), int(S * 0.70)), Image.LANCZOS)
    bg.alpha_composite(m, ((S - m.width) // 2, (S - m.height) // 2))
    return bg.resize((size, size), Image.LANCZOS)


def logo(size):
    shape = mark()
    shape = shape.crop(shape.getbbox())
    side = max(shape.size)
    pad = int(side * 0.04)
    out = Image.new("RGBA", (side + 2 * pad, side + 2 * pad), (0, 0, 0, 0))
    out.alpha_composite(shape, ((out.width - shape.width) // 2, (out.height - shape.height) // 2))
    return out.resize((size, size), Image.LANCZOS)




def favicons():
    for size, name in ((32, "favicon-32.png"), (192, "favicon-192.png")):
        logo(size).save("assets/" + name, optimize=True)
    from PIL import Image as _I
    _I.open("assets/favicon-32.png").save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

if __name__ == "__main__":
    logo(256).save("assets/logo.png", optimize=True)
    tile(180).convert("RGB").save("assets/apple-touch-icon.png", optimize=True)
    tile(512).save("assets/icon-512.png", optimize=True)
    favicons()
    print("wrote assets/logo.png, assets/apple-touch-icon.png, assets/icon-512.png")
