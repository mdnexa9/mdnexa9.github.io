"""Inline-style the Darkflow placeholder so nothing overrides its layout."""
import pathlib
import re

SUB = {"index.html": "Google Play listing coming soon", "ar/index.html": "صفحة المتجر قيد التجهيز"}
STYLE = ("display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;"
         "aspect-ratio:16/9;background:radial-gradient(circle at 50% 45%,#241b52,#0a0d18 72%);"
         "text-decoration:none;line-height:1.3;color:#cfc6ff;text-align:center;padding:0 14px")

for name, sub in SUB.items():
    f = pathlib.Path(name)
    h = f.read_text(encoding="utf-8")
    new = (f'<a href="/md-darkflow/" class="mdfallback" style="{STYLE}">'
           '<b style="font-size:18px;font-weight:600">MD Darkflow</b>'
           f'<span style="font-size:12.5px;color:#9d92e0">{sub}</span></a>')
    h2, n = re.subn(r'<a href="/md-darkflow/" class="mdfallback"[^>]*>.*?</a>', new, h, count=1, flags=re.S)
    if n:
        f.write_text(h2, encoding="utf-8")
        print("inline placeholder in", name)
    else:
        print("no match in", name)
