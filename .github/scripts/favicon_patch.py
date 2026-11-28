"""Render favicons from the brand mark and link them in every page shell."""
import pathlib

assets = pathlib.Path(".github/scripts/brand_assets.py")
text = assets.read_text(encoding="utf-8")
if "favicon.ico" not in text:
    extra = (
        '\n\ndef favicons():\n'
        '    for size, name in ((32, "favicon-32.png"), (192, "favicon-192.png"), (180, "apple-touch-icon.png")):\n'
        '        logo(size).save("assets/" + name, optimize=True)\n'
        '    tile(64).save("/tmp/favicon-64.png")\n'
        '    Image.open("assets/favicon-32.png").save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])\n'
    )
    text = text.replace('if __name__ == "__main__":', extra + '\n\nif __name__ == "__main__":')
    text = text.replace('    print("wrote assets/logo.png', '    favicons()\n    print("wrote assets/logo.png')
    assets.write_text(text, encoding="utf-8")
    print("brand_assets.py: favicon step added")

kit = pathlib.Path([".github/scripts/site_kit.py"])
src = kit.read_text(encoding="utf-8")
old = '<link rel=\\"icon\\" href=\\"/assets/logo.svg\\" type=\\"image/svg+xml\\">'
new = (old + '<link rel=\\"apple-touch-icon\\" href=\\"/assets/apple-touch-icon.png\\">'
            '<link rel=\\"icon\\" sizes=\\"192x192\\" href=\\"/assets/favicon-192.png\\">')
if "apple-touch-icon" not in src:
    src = src.replace(old, new)
    kit.write_text(src, encoding="utf-8")
    print("site_kit.py: icon links added")
else:
    print("site_kit.py: already linked")

for wf in (".github/workflows/site-build.yml", ".github/workflows/brand-assets.yml"):
    p = pathlib.Path(wf)
    print(wf, "exists" if p.exists() else "MISSING")
