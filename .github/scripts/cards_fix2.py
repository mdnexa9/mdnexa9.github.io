"""Four cards per row and a centred Darkflow placeholder."""
import pathlib

EXTRA = (".mdcard>a.mdfallback{display:flex;flex-direction:column;align-items:center;justify-content:center;"
         "gap:8px;text-decoration:none;line-height:1.3;padding:0 16px}"
         ".mdfallback .t{font-size:19px;font-weight:600;color:#cfc6ff}"
         ".mdfallback .s{font-size:12.5px;color:#8f83d8}")

TEXT = {
    "index.html": "Google Play listing coming soon",
    "ar/index.html": "صفحة المتجر على Google Play قيد التجهيز",
}

for name, sub in TEXT.items():
    f = pathlib.Path(name)
    h = f.read_text(encoding="utf-8")
    h = h.replace("minmax(250px,1fr)", "minmax(205px,1fr)")
    h = h.replace('<a href="/md-darkflow/" class="mdfallback">',
                  '<a href="/md-darkflow/" class="mdfallback"><span class="t">MD Darkflow</span><span class="s">' + sub + "</span><span style=\"display:none\">")
    if EXTRA not in h:
        h = h.replace("</style>", EXTRA + "</style>", 1)
    f.write_text(h, encoding="utf-8")
    print("patched", name)
