"""Render favicons from the brand mark and add the icon links to the page shell."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from brand_assets import logo  # noqa: E402

for size, name in ((32, "favicon-32.png"), (192, "favicon-192.png"), (180, "apple-touch-icon.png")):
    logo(size).save("assets/" + name, optimize=True)
    print("wrote assets/" + name)

from PIL import Image  # noqa: E402
Image.open("assets/favicon-32.png").save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("wrote favicon.ico")

kit = pathlib.Path(".github/scripts/site_kit.py")
src = kit.read_text(encoding="utf-8")
BLOCK = '''
_ICONS = ('<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">'
          '<link rel="icon" sizes="192x192" href="/assets/favicon-192.png">')
SHELL = SHELL.replace('<link rel="stylesheet"', _ICONS + '<link rel="stylesheet"', 1)
'''
if "_ICONS" not in src:
    kit.write_text(src + BLOCK, encoding="utf-8")
    print("site_kit.py: icon links appended")
else:
    print("site_kit.py: already has icon links")
