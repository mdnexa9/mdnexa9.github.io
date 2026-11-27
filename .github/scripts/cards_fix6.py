"""Final override for the app card grid, placed last in the head."""
import pathlib

RULE = ('<style>.mdcards{grid-template-columns:repeat(auto-fit,minmax(210px,1fr))!important;gap:18px!important}'
        '.mdcard{min-width:0}</style>')

for name in ("index.html", "ar/index.html"):
    f = pathlib.Path(name)
    h = f.read_text(encoding="utf-8")
    if "minmax(210px,1fr)!important" in h:
        print("already", name)
        continue
    h = h.replace("</head>", RULE + "</head>", 1)
    f.write_text(h, encoding="utf-8")
    print("patched", name)
