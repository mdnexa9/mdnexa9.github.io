"""Remove Android-only framing from titles, descriptions and hero copy."""
import pathlib

PAIRS = [
    ("MD Work — free work notebook for Android | MD Nexa", "MD Work — a day-rate notebook with no sign-in | MD Nexa"),
    ("MD Corpses — one-finger climbing game for Android | MD Nexa", "MD Corpses — a one-finger climbing game | MD Nexa"),
    ("Services — Android apps &amp; digital platforms | MD Nexa", "Services — software, apps and digital platforms | MD Nexa"),
    ("Services — Android apps & digital platforms", "Services — software, apps and digital platforms"),
    ("تطبيقات أندرويد ومنصات رقمية", "تطبيقات ومنصات رقمية"),
    ("Android app studio", "software studio"),
    ("Android apps studio", "software studio"),
    ("استوديو تطبيقات أندرويد", "استوديو برمجيات"),
]

changed = 0
for path in sorted(pathlib.Path(".").rglob("*.html")):
    if any(p.startswith(".") for p in path.parts):
        continue
    text = path.read_text(encoding="utf-8")
    before = text
    for old, new in PAIRS:
        text = text.replace(old, new)
    if text != before:
        path.write_text(text, encoding="utf-8")
        changed += 1
print("pages changed:", changed)
