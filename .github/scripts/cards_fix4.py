"""Deterministic four-column card row on desktop, stacked on phones."""
import pathlib

RULE = "@media(min-width:960px){.mdcards{grid-template-columns:repeat(4,1fr)}}.mdcards{gap:18px}"

for name in ("index.html", "ar/index.html"):
    f = pathlib.Path(name)
    h = f.read_text(encoding="utf-8")
    if RULE in h:
        print("already", name)
        continue
    h = h.replace("</style>", RULE + "</style>", 1)
    f.write_text(h, encoding="utf-8")
    print("patched", name)
