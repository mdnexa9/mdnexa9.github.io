"""Narrow the card column minimum inside the app-card style block."""
import pathlib

for name in ("index.html", "ar/index.html"):
    f = pathlib.Path(name)
    h = f.read_text(encoding="utf-8")
    if "minmax(200px,1fr)" in h:
        print("already", name)
        continue
    h = h.replace("minmax(250px,1fr)", "minmax(200px,1fr)")
    h = h.replace("minmax(290px,1fr)", "minmax(200px,1fr)")
    f.write_text(h, encoding="utf-8")
    print("patched", name)
