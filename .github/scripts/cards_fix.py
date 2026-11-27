"""Align the homepage app cards: one row, real 16:9 store crops, readable fallback."""
import pathlib

for name in ("index.html", "ar/index.html"):
    f = pathlib.Path(name)
    h = f.read_text(encoding="utf-8")
    before = h
    h = h.replace("minmax(290px,1fr)", "minmax(250px,1fr)")
    h = h.replace("=w1000\"", "=w1052-h592\"")
    h = h.replace(".mdcard>a{display:block;line-height:0}",
                  ".mdcard>a{display:block;line-height:0}.mdcard>a.mdfallback{line-height:1.35;text-align:center;padding:0 18px}")
    h = h.replace(".mdfallback b{font-size:19px", ".mdfallback b{display:block;font-size:19px")
    if h != before:
        f.write_text(h, encoding="utf-8")
        print("fixed", name)
    else:
        print("no change", name)
