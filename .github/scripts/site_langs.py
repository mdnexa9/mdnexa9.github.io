"""Generate French, Spanish and German studio pages and wire them up."""
import pathlib

LANGS = {
    "fr": dict(
        title="MD Nexa — studio de logiciels indépendant et jeux de réflexion",
        desc="MD Nexa est un petit studio de logiciels indépendant. MD Bolt Master et MD Darkflow : des jeux de réflexion gratuits, hors ligne, en quatorze langues.",
        nav=["Jeux", "Studio", "Aide"],
        h1="Deux jeux de réflexion. Une règle claire.",
        lede="MD Bolt Master replace chaque boulon coloré sur sa vis, MD Darkflow efface les flèches néon d'un plateau noir. Les deux s'ouvrent en une seconde et fonctionnent hors ligne.",
        cta1="Découvrir MD Bolt Master", cta2="Voir MD Darkflow",
        gamehead="Nos jeux",
        b1=("MD Bolt Master", "Le jeu posé : chaque écrou va sur la vis de sa couleur. Niveaux progressifs, étoiles à dépenser en aide, un plateau quotidien commun à tous les joueurs."),
        d1=("MD Darkflow", "Le jeu vif : touchez une flèche pour la sortir du plateau, à condition que le chemin soit libre. Cent niveaux, trois cœurs."),
        abouthead="À propos du studio",
        about=("MD Nexa est un petit studio de logiciels indépendant. Nous faisons des jeux de réflexion pour Android et quelques outils, et chaque écran est écrit pour fonctionner dans les quatorze langues que nous livrons, sans aucune connexion.",
                "Aucun compte n'est nécessaire aujourd'hui. Si nous ajoutons une synchronisation plus tard, elle restera facultative : l'application fonctionnera exactement de la même façon sans elle.",
                "Android est la plateforme de nos jeux aujourd'hui. En grandissant, nous publierons ailleurs, et rien dans notre façon de construire ne nous enferme dans une seule boutique."),
        foot="Studio de logiciels indépendant. La simplicité est notre force.",
    ),
    "es": dict(
        title="MD Nexa — estudio de software independiente y juegos de lógica",
        desc="MD Nexa es un pequeño estudio de software independiente. MD Bolt Master y MD Darkflow: juegos de lógica gratis, sin conexión y en catorce idiomas.",
        nav=["Juegos", "Estudio", "Ayuda"],
        h1="Dos juegos de lógica. Una regla clara.",
        lede="MD Bolt Master coloca cada perno de color en su tornillo y MD Darkflow borra las flechas de neón de un tablero negro. Los dos abren en un segundo y funcionan sin conexión.",
        cta1="Ver MD Bolt Master", cta2="Ver MD Darkflow",
        gamehead="Nuestros juegos",
        b1=("MD Bolt Master", "El tranquilo: cada tuerca va al tornillo de su color. Niveles graduales, estrellas para gastar en ayuda y un tablero diario compartido por todos."),
        d1=("MD Darkflow", "El ágil: toca una flecha y sale del tablero, pero solo si el camino está libre. Cien niveles, tres corazones."),
        abouthead="Sobre el estudio",
        about=("MD Nexa es un pequeño estudio de software independiente. Hacemos juegos de lógica para Android y algunas herramientas, y cada pantalla está escrita para funcionar en los catorce idiomas que publicamos y sin ninguna conexión.",
                "Hoy no hace falta ninguna cuenta. Si más adelante añadimos sincronización, será opcional: la aplicación seguirá funcionando exactamente igual sin ella.",
                "Android es donde están nuestros juegos ahora. Según crezca el estudio publicaremos en otras plataformas, y nada en nuestra forma de construir nos encierra en una sola tienda."),
        foot="Estudio de software independiente. La sencillez es nuestra fuerza.",
    ),
    "de": dict(
        title="MD Nexa — unabhängiges Software-Studio und Knobelspiele",
        desc="MD Nexa ist ein kleines unabhängiges Software-Studio. MD Bolt Master und MD Darkflow: kostenlose Knobelspiele, offline und in vierzehn Sprachen.",
        nav=["Spiele", "Studio", "Hilfe"],
        h1="Zwei Knobelspiele. Eine klare Regel.",
        lede="MD Bolt Master legt jede farbige Mutter auf ihre eigene Schraube, MD Darkflow räumt die Neonpfeile vom schwarzen Brett. Beide öffnen in einer Sekunde und laufen offline.",
        cta1="MD Bolt Master ansehen", cta2="MD Darkflow ansehen",
        gamehead="Unsere Spiele",
        b1=("MD Bolt Master", "Das ruhige: jede Mutter auf die Schraube ihrer Farbe. Gestufte Level, Sterne für Hilfe und ein tägliches Brett für alle Spieler."),
        d1=("MD Darkflow", "Das scharfe: ein Pfeil verlässt das Brett, aber nur wenn der Weg frei ist. Hundert Level, drei Herzen."),
        abouthead="Über das Studio",
        about=("MD Nexa ist ein kleines unabhängiges Software-Studio. Wir bauen Knobelspiele für Android und einige Werkzeuge, und jeder Bildschirm ist so geschrieben, dass er in allen vierzehn Sprachen funktioniert — ganz ohne Verbindung.",
                "Ein Konto braucht heute niemand. Sollten wir später eine Synchronisierung ergänzen, bleibt sie freiwillig: Die App funktioniert ohne sie genau gleich.",
                "Android ist heute die Heimat unserer Spiele. Wenn das Studio wächst, veröffentlichen wir auch anderswo — und nichts in unserer Arbeitsweise bindet uns an einen einzigen Store."),
        foot="Unabhängiges Software-Studio. Einfachheit ist unsere Stärke.",
    ),
}

CSS = """*{box-sizing:border-box}body{margin:0;background:#05060c;color:#e9edf9;font:16px/1.6 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}header{display:flex;align-items:center;gap:14px;max-width:1080px;margin:0 auto;padding:20px 22px}header img{width:34px;height:34px}header strong{font-size:16px;letter-spacing:.06em}nav{margin-left:auto;display:flex;gap:18px;flex-wrap:wrap}nav a{color:#a9b4cf;text-decoration:none;font-size:14px}nav a:hover{color:#fff}main{max-width:1080px;margin:0 auto;padding:0 22px}h1{font-size:clamp(30px,5vw,52px);line-height:1.1;margin:40px 0 16px;background:linear-gradient(92deg,#4ed5ff,#9e6df7);-webkit-background-clip:text;background-clip:text;color:transparent}.lede{font-size:18px;color:#a9b4cf;max-width:62ch}.btns{display:flex;gap:12px;flex-wrap:wrap;margin:28px 0 10px}.btn{display:inline-block;padding:13px 20px;border-radius:999px;text-decoration:none;font-weight:600;font-size:15px;background:linear-gradient(92deg,#4e78f0,#9e6df7);color:#fff}.btn.ghost{background:transparent;border:1px solid #26304a;color:#cdd6ea}h2{font-size:clamp(24px,3vw,32px);margin:64px 0 8px}.cards{display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));margin-top:18px}.card{background:#0b0e1a;border:1px solid #1c2237;border-radius:20px;padding:22px}.card h3{margin:0 0 8px;font-size:18px}.card p{margin:0;color:#94a1be;font-size:15px}footer{border-top:1px solid #151b2c;margin-top:72px;padding:26px 22px 40px;text-align:center;color:#7d88a4;font-size:14px}footer a{color:#a9b4cf;text-decoration:none}"""

LINKS = [("en", "English", "/"), ("ar", "العربية", "/ar/"), ("fr", "Français", "/fr/"), ("es", "Español", "/es/"), ("de", "Deutsch", "/de/")]


def page(code, d):
    alt = "".join(f'<link rel="alternate" hreflang="{c}" href="https://mdnexa.online{p}">' for c, _, p in LINKS)
    alt += '<link rel="alternate" hreflang="x-default" href="https://mdnexa.online/">'
    nav = "".join(f'<a href="#{"games" if i == 0 else "studio" if i == 1 else "about"}">{n}</a>' for i, n in enumerate(d["nav"]))
    about = "".join(f'<p class="lede">{p}</p>' for p in d["about"])
    return f"""<!doctype html><html lang="{code}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{d['title']}</title><meta name="description" content="{d['desc']}"><link rel="canonical" href="https://mdnexa.online/{code}/">{alt}
<meta property="og:title" content="{d['title']}"><meta property="og:description" content="{d['desc']}"><meta property="og:image" content="https://mdnexa.online/assets/og-image.jpg"><meta property="og:type" content="website">
<link rel="icon" href="/assets/logo.svg" type="image/svg+xml"><meta name="theme-color" content="#05060c"><style>{CSS}</style></head><body>
<header><img src="/assets/logo.svg" alt="MD Nexa"><strong>MD NEXA</strong><nav>{nav}</nav></header>
<main><h1>{d['h1']}</h1><p class="lede">{d['lede']}</p>
<div class="btns"><a class="btn" href="/md-boltmaster/">{d['cta1']}</a><a class="btn ghost" href="/md-darkflow/">{d['cta2']}</a></div>
<h2 id="games">{d['gamehead']}</h2><div class="cards"><article class="card"><h3>{d['b1'][0]}</h3><p>{d['b1'][1]}</p></article><article class="card"><h3>{d['d1'][0]}</h3><p>{d['d1'][1]}</p></article></div>
<h2 id="studio">{d['abouthead']}</h2>{about}
</main>
<footer><p id="about">{d['foot']}</p><p>{' · '.join(f'<a href="{p}">{n}</a>' for c, n, p in LINKS)}</p><p>mdnexa9@gmail.com · © 2026 MD Nexa</p></footer>
</body></html>"""


for code, d in LANGS.items():
    out = pathlib.Path(code)
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page(code, d), encoding="utf-8")
    print("wrote", code + "/index.html")

head_extra = "".join(f'<link rel="alternate" hreflang="{c}" href="https://mdnexa.online{p}">' for c, _, p in LINKS if c not in ("en", "ar"))
for path in ("index.html", "ar/index.html"):
    f = pathlib.Path(path)
    h = f.read_text(encoding="utf-8")
    if 'hreflang="fr"' not in h:
        h = h.replace("</head>", head_extra + "</head>", 1)
        f.write_text(h, encoding="utf-8")
        print("hreflang added:", path)

sm = pathlib.Path("sitemap.xml")
if sm.exists():
    x = sm.read_text(encoding="utf-8")
    add = "".join(f"<url><loc>https://mdnexa.online/{c}/</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>" for c in ("fr", "es", "de") if f"https://mdnexa.online/{c}/<" not in x)
    if add:
        sm.write_text(x.replace("</urlset>", add + "</urlset>", 1), encoding="utf-8")
        print("sitemap updated")
