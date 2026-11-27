"""Replace the whole Darkflow placeholder anchor with clean markup."""
import pathlib
import re

SUB = {
    "index.html": "Google Play listing coming soon",
    "ar/index.html": "صفحة المتجر قيد التجهيز",
}

for name, sub in SUB.items():
    f = pathlib.Path(name)
    h = f.read_text(encoding="utf-8")
    new = ('<a href="/md-darkflow/" class="mdfallback"><span class="t">MD Darkflow</span>'
           f'<span class="s">{sub}</span></a>')
    h2, n = re.subn(r'<a href="/md-darkflow/" class="mdfallback">.*?</a>', new, h, count=1, flags=re.S)
    if n:
        f.write_text(h2, encoding="utf-8")
        print("rewrote card in", name)
    else:
        print("pattern missing in", name)
