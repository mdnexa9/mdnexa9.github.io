"""Design system for mdnexa.online: tokens, page shell, header and footer."""
import pathlib

ORIGIN = "https://mdnexa.online"
CSS = """:root{--ink:#05060c;--panel:#0a0d18;--panel2:#0d1120;--line:#1b2236;--text:#eef1f9;--muted:#98a3bf;--grad:linear-gradient(96deg,#4ed5ff,#7b8cf8 55%,#9e6df7)}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--ink);color:var(--text);font:16px/1.65 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;-webkit-font-smoothing:antialiased}
img{max-width:100%}
a{color:inherit}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px}
header.site{position:sticky;top:0;z-index:60;background:rgba(5,6,12,.84);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
header.site .bar{display:flex;align-items:center;gap:16px;min-height:72px}
.brand{display:flex;align-items:center;gap:11px;text-decoration:none;font-weight:700;letter-spacing:.16em;font-size:13.5px}
.brand img{width:34px;height:34px}
nav.main{margin-left:auto;display:flex;gap:24px;flex-wrap:wrap}
nav.main a{text-decoration:none;color:var(--muted);font-size:14.5px}
nav.main a:hover{color:#fff}
.btn{display:inline-flex;align-items:center;gap:9px;padding:13px 22px;border-radius:999px;font-weight:650;font-size:15px;text-decoration:none;background:var(--grad);color:#08101f}
.btn.ghost{background:transparent;border:1px solid var(--line);color:var(--text)}
.btn.ghost:hover{border-color:#33405e}
.eyebrow{display:inline-flex;align-items:center;gap:10px;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:#8b96b4;margin:0 0 20px}
.eyebrow i{width:26px;height:1px;background:var(--grad);display:inline-block}
h1.display{font-size:clamp(38px,6vw,72px);line-height:1.03;letter-spacing:-.03em;margin:0 0 22px;font-weight:750}
h1.display em{font-style:normal;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.hero{padding:92px 0 70px;position:relative;overflow:hidden}
.hero:before{content:'';position:absolute;inset:-45% 15% auto 35%;height:660px;background:radial-gradient(circle at 50% 40%,rgba(126,92,240,.30),transparent 62%);filter:blur(26px);pointer-events:none}
.hero p.lead{font-size:clamp(17px,2vw,20px);color:#aab4cf;max-width:60ch;margin:0}
.hero .cta{display:flex;gap:14px;flex-wrap:wrap;margin-top:34px}
.trust{display:flex;gap:22px;flex-wrap:wrap;color:#7c87a4;font-size:13px;margin-top:34px;letter-spacing:.02em}
section.blk{padding:82px 0}
h2.sec{font-size:clamp(26px,3.6vw,40px);letter-spacing:-.02em;line-height:1.12;margin:0 0 16px;font-weight:700}
p.sec{color:var(--muted);max-width:64ch;margin:0 0 44px;font-size:17px}
.prod{display:grid;grid-template-columns:1fr 1.05fr;gap:46px;align-items:center;padding:36px 0;border-top:1px solid var(--line)}
.prod.flip{grid-template-columns:1.05fr 1fr}
.prod.flip .shot{order:-1}
.shot{border-radius:22px;overflow:hidden;border:1px solid var(--line);background:var(--panel);position:relative;line-height:0}
.shot img{width:100%;display:block}
.shot.soon{aspect-ratio:16/9;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;background:radial-gradient(circle at 50% 42%,#241b52,#0a0d18 72%);line-height:1.4;text-align:center;padding:20px}
.shot.soon b{font-size:20px;letter-spacing:.02em;color:#d6ceff}
.shot.soon span{font-size:12.5px;color:#9d92e0}
.appname{display:flex;align-items:center;gap:14px;margin:0 0 16px}
.appname img{width:56px;height:56px;border-radius:15px;border:1px solid var(--line);background:#0a0d18}
.appname h3{margin:0;font-size:23px;letter-spacing:-.01em}
.appname .tag{color:#8b96b4;font-size:13px;margin:3px 0 0}
.prod p{color:var(--muted);margin:0 0 18px}
.tags{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 22px;padding:0;list-style:none}
.tags li{font-size:12.5px;color:#b9c3dc;border:1px solid var(--line);border-radius:999px;padding:5px 11px}
.link{color:#9fb0ff;text-decoration:none;font-weight:650;font-size:15px}
.link:hover{color:#c8d3ff}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:20px;padding:26px}
.card h3{margin:0 0 9px;font-size:18px;letter-spacing:-.01em}
.card p{margin:0;color:var(--muted);font-size:14.6px}
.card .num{font-size:12px;letter-spacing:.16em;color:#7b86a4;display:block;margin:0 0 12px}
.alt{background:var(--panel2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.specs{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:18px;margin:34px 0 0;padding:0;list-style:none}
.specs li{border-top:1px solid var(--line);padding-top:12px}
.specs b{display:block;font-size:15px;font-weight:650}
.specs span{color:#8b96b4;font-size:13.5px}
article.prose{max-width:74ch}
article.prose h2{font-size:clamp(22px,3vw,30px);margin:44px 0 12px;letter-spacing:-.01em}
article.prose p,article.prose li{color:#aab4cf}
article.prose ul{padding-left:20px}
footer.site{border-top:1px solid var(--line);padding:56px 0 44px;color:#8590ac;font-size:14px}
footer.site .cols{display:flex;gap:64px;flex-wrap:wrap;justify-content:space-between}
footer.site h4{margin:0 0 14px;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:#727d9a}
footer.site a{color:#a9b4cf;text-decoration:none;display:block;margin:0 0 9px}
footer.site a:hover{color:#fff}
footer.site .bottom{margin-top:44px;padding-top:22px;border-top:1px solid var(--line);display:flex;gap:20px;flex-wrap:wrap;justify-content:space-between;font-size:13px;color:#6f7a96}
@media(max-width:860px){.prod,.prod.flip{grid-template-columns:1fr;gap:26px}.prod.flip .shot{order:0}.hero{padding:60px 0 44px}section.blk{padding:56px 0}nav.main{gap:16px;font-size:13.5px}.wrap{padding:0 18px}}
"""

NAV = [("Products", "/#products"), ("Studio", "/studio/"), ("Brand", "/brand/"), ("Contact", "/contact/")]


def header():
    nav = "".join('<a href="%s">%s</a>' % (h, l) for l, h in NAV)
    return ('<header class="site"><div class="wrap bar"><a class="brand" href="/"><img src="/assets/logo.svg" alt="">MD NEXA</a>'
            '<nav class="main">' + nav + '<a href="/ar/" hreflang="ar">العربية</a></nav></div></header>')


FOOTER = """<footer class="site"><div class="wrap"><div class="cols">
<div><h4>Studio</h4><a href="/studio/">About</a><a href="/brand/">Brand</a><a href="/contact/">Contact</a><a href="/privacy/">Privacy</a></div>
<div><h4>Products</h4><a href="/md-boltmaster/">MD Bolt Master</a><a href="/md-darkflow/">MD Darkflow</a><a href="/md-corpses/">MD Corpses</a><a href="/md-work/">MD Work</a></div>
<div><h4>Elsewhere</h4><a href="https://play.google.com/store/apps/developer?id=MD+Nexa">Google Play</a><a href="/ar/" hreflang="ar">العربية</a><a href="mailto:mdnexa9@gmail.com">mdnexa9@gmail.com</a></div>
</div><div class="bottom"><span>© 2026 MD Nexa — independent software studio.</span><span>Android today, not Android forever.</span></div></div></footer>"""

SHELL = ("<!doctype html><html lang=\"{lang}\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
         "<title>{title}</title><meta name=\"description\" content=\"{desc}\">"
         "<link rel=\"canonical\" href=\"{origin}{path}\"><link rel=\"icon\" href=\"/assets/logo.svg\" type=\"image/svg+xml\"><link rel=\"apple-touch-icon\" href=\"/assets/apple-touch-icon.png\"><link rel=\"icon\" sizes=\"192x192\" href=\"/assets/favicon-192.png\">"
         "<meta name=\"theme-color\" content=\"#05060c\"><meta property=\"og:type\" content=\"website\">"
         "<meta property=\"og:title\" content=\"{title}\"><meta property=\"og:description\" content=\"{desc}\">"
         "<meta property=\"og:image\" content=\"{origin}/assets/og-image.jpg\"><meta name=\"twitter:card\" content=\"summary_large_image\">"
         "<link rel=\"stylesheet\" href=\"/assets/site.css\"></head><body>{header}{body}{footer}</body></html>")


def page(path, title, desc, body, lang="en"):
    return SHELL.format(lang=lang, title=title, desc=desc, origin=ORIGIN, path=path, header=header(), body=body, footer=FOOTER)


def write(path, html):
    f = pathlib.Path(path)
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(html, encoding="utf-8")
    print("wrote", path, len(html), "bytes")


def save_css():
    pathlib.Path("assets/site.css").write_text(CSS, encoding="utf-8")
    print("wrote assets/site.css", len(CSS), "bytes")

_ICONS = ('<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">'
          '<link rel="icon" sizes="192x192" href="/assets/favicon-192.png">')
SHELL = SHELL.replace('<link rel="stylesheet"', _ICONS + '<link rel="stylesheet"', 1)

CSS += "@media(max-width:760px){header.site .bar{flex-wrap:wrap;padding:10px 0;gap:6px}.brand{white-space:nowrap}nav.main{width:100%;margin-left:0;overflow-x:auto;gap:18px;font-size:13.5px;padding:2px 0 6px}nav.main::-webkit-scrollbar{display:none}.hero h1{letter-spacing:-.02em}}"
_HEADSET = ('<link rel="manifest" href="/site.webmanifest">'
            '<link rel="icon" href="/favicon.ico" sizes="any">'
            '<link rel="icon" type="image/png" sizes="32x32" href="/assets/icon-32.png">'
            '<link rel="icon" type="image/png" sizes="192x192" href="/assets/icon-192.png">'
            '<link rel="icon" type="image/png" sizes="512x512" href="/assets/icon-512.png">'
            '<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">'
            '<meta name="apple-mobile-web-app-title" content="MD Nexa">'
            '<link rel="alternate" hreflang="en" href="https://mdnexa.online/">'
            '<link rel="alternate" hreflang="ar" href="https://mdnexa.online/ar/">'
            '<link rel="alternate" hreflang="x-default" href="https://mdnexa.online/">')
SHELL = SHELL.replace("</head>", _HEADSET + "</head>", 1)
