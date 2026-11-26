#!/usr/bin/env python3
"""Build sitemap.xml from content/pages.json.

Every group in the manifest becomes one <url> entry per language in its
`alternates` map, and each entry carries the full hreflang set so Google sees
the same cluster from every side. Run it after adding or editing content:

    python3 tools/build_sitemap.py            # writes sitemap.xml
    python3 tools/build_sitemap.py --check    # exit 1 if sitemap.xml is stale

Nothing else on the site is touched: no page is rewritten, no existing
canonical is changed.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
import xml.dom.minidom

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "content" / "pages.json"
SITEMAP = ROOT / "sitemap.xml"

HEADER = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
    'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
)
FOOTER = "</urlset>\n"


def load() -> dict:
    with MANIFEST.open(encoding="utf-8") as fh:
        return json.load(fh)


def render(data: dict) -> str:
    base = data["base"].rstrip("/")
    default = data.get("x_default")
    out = [HEADER]
    for group in data["groups"]:
        alts = group["alternates"]
        # A group may be single-language; then it is its own x-default.
        group_default = group.get("x_default")
        if group_default is None:
            group_default = default if default in alts else next(iter(alts))
        if group_default not in alts:
            raise SystemExit(
                f"group {group['key']}: x_default {group_default!r} not in alternates"
            )
        for lang, path in alts.items():
            loc = base + path
            out.append("  <url>\n")
            out.append(f"    <loc>{loc}</loc>\n")
            out.append(f"    <lastmod>{group['lastmod']}</lastmod>\n")
            out.append(f"    <changefreq>{group['changefreq']}</changefreq>\n")
            out.append(f"    <priority>{group['priority'][lang]}</priority>\n")
            for alt_lang, alt_path in alts.items():
                out.append(
                    f'    <xhtml:link rel="alternate" hreflang="{alt_lang}" '
                    f'href="{base + alt_path}"/>\n'
                )
            out.append(
                f'    <xhtml:link rel="alternate" hreflang="x-default" '
                f'href="{base + alts[group_default]}"/>\n'
            )
            out.append("  </url>\n")
    out.append(FOOTER)
    return "".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if sitemap.xml is out of date")
    args = parser.parse_args()

    text = render(load())
    xml.dom.minidom.parseString(text)  # fail loudly on malformed output

    current = SITEMAP.read_text(encoding="utf-8") if SITEMAP.exists() else ""
    if args.check:
        if current != text:
            print("sitemap.xml is stale: run python3 tools/build_sitemap.py", file=sys.stderr)
            return 1
        print(f"sitemap.xml up to date ({text.count('<loc>')} urls)")
        return 0

    SITEMAP.write_text(text, encoding="utf-8")
    print(f"wrote sitemap.xml with {text.count('<loc>')} urls")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
