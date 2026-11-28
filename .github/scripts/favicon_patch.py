"""Render favicons from the brand mark and link them in every page shell."""
import pathlib

assets = pathlib.Path(".github/scripts/brand_assets.py")
text = assets.read_text(encoding="utf-8")
if "favicons()" not in text:
    extra = (
        '\n\ndef favicons():\n'
        '    for size, name in ((32, "favicon-32.png"), (192, "favicon-192.png")):\n'
        '        logo(size).save("assets/" + name, optimize=True)\n'
        '    from PIL import Image as _I\n'
        '    _I.open("assets/favicon-32.png").save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])\n'
    )
    text = text.replace('if __name__ == "__main__":', extra + '\nif __name__ == "__main__":')
    text = text.replace('    print("wrote assets/logo.png', '    favicons()\n    print("wrote assets/logo.png')
    assets.write_text(text, encoding="utf-8")
    print("brand_assets.py: favicon step added")
else:
    print("brand_assets.py: already patched")

kit_path = pathlib.Path(".github/scripts/site_kit.py")
src = kit_path.read_text(encoding="utf-8")
old = '<link rel=\\"icon\\" href=\\"/assets/logo.svg\\" type=\\"image/svg+xml\\">'
if old in src and "apple-touch-icon" not in src:
    new = (old + '<link rel=\\"apple-touch-icon\\" href=\\"/assets/apple-touch-icon.png\\">'
                '<link rel=\\"icon\\" sizes=\\"192x192\\" href=\\"/assets/favicon-192.png\\">')
    kit_path.write_text(src.replace(old, new), encoding="utf-8")
    print("site_kit.py: icon links added")
else:
    print("site_kit.py: unchanged")
