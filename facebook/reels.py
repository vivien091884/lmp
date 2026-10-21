"""Vidéos verticales 1080×1920 (Stories / Reels / statut WhatsApp), 4 par jour, générées à partir du contenu du jour (contenus.py).
reel-1 accroche (titre animé), reel-2 points clés, reel-3 illustration animée, reel-4 question + appel à l'action. Durée : DUREE_REEL s."""
import html as _h
import math
import re
from gabarits import ILL, GEAR_PATH, GRAIN, logo, words, hl

DUREE_REEL = 8
H = 1920


def _topo(n=26, couleur="#e0561c"):
    paths = []
    for k in range(n):
        pts = [f"{x},{120 + k * 78 + 38 * math.sin(x / 160 + k * .7) + 22 * math.sin(x / 70 + k * 1.3):.0f}" for x in range(-100, 1301, 50)]
        paths.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{couleur}" stroke-width="{1.4 if k % 4 else 2.4}" opacity="{.35 if k % 4 else .6}"/>')
    return f'<svg class="topo" viewBox="0 0 1200 2100" width="1200" height="2100">{"".join(paths)}</svg>'


GRAIN_V = GRAIN.replace('height="1080"', f'height="{H}"')
CSS = f"""
html,body{{height:{H}px}}
.topo{{animation:drift {DUREE_REEL}s linear both}}
.brand{{top:90px;left:50%;width:300px;margin-left:-150px}}
.stripe{{animation:grow {DUREE_REEL}s linear both}}
.kick{{position:absolute;top:250px;left:80px;right:80px;text-align:center;font-size:30px;font-weight:700;letter-spacing:6px;text-transform:uppercase;color:#e0561c;animation:fadeUp .5s .2s both}}
.outro{{animation-delay:5.4s}}
.outro .logo{{width:860px}}
.outro .tag{{animation-delay:6.6s}}
.outro .slog{{animation-delay:6.9s;font-size:44px}}
.outro .cta{{animation-delay:7.1s;font-size:40px;padding:26px 50px}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-26px)}}}}
"""


def _head(css):
    return ('<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="../base.css"><style>'
            + CSS + css + '</style></head><body>' + _topo() + '<div class="brand">' + logo() + '</div>')


OUTRO = ('<div class="outro"><div class="lat"></div>' + GRAIN_V + '<div class="logo">' + logo("laterite", 5.9) + '</div>'
         '<div class="tag">TERRAIN <b>•</b> TECHNIQUE <b>•</b> FIABILITÉ</div>'
         '<div class="slog">SMTEC, l\'exigence du terrain.</div><div class="cta">Écrivez-nous en MP</div></div>'
         '<div class="stripe"></div></body></html>')


def _kick(theme):
    return f'<div class="kick">{_h.escape(theme)}</div>'


def accroche(p):
    titre, _, ill, _ = p["visuel"]
    css = f"""
h1{{position:absolute;top:420px;left:70px;right:70px;text-align:center}}
.ill{{position:absolute;left:120px;top:1050px;width:840px;height:700px;animation:pop .7s cubic-bezier(.2,.9,.3,1.3) 1.8s both}}
.ill svg{{width:100%;height:100%;animation:float 2.6s ease-in-out 2.5s infinite}}"""
    return (_head(css) + _kick(p["theme"]) + f'<h1 style="font-size:{_fit(titre, 120)}px">{words(titre, .4, .18)}</h1>'
            f'<div class="ill"><svg viewBox="0 0 480 400">{ILL[ill]}</svg></div>' + OUTRO)


def points(p):
    titre, puces, _, _ = p["visuel"]
    css = """
h1{position:absolute;top:340px;left:70px;right:70px;text-align:center}
.cards{position:absolute;top:760px;left:80px;right:80px;display:flex;flex-direction:column;gap:34px}
.c{display:flex;align-items:center;gap:34px;background:#272624;border:2px solid #3a3836;border-left:12px solid #e0561c;border-radius:8px;padding:38px 40px;font-size:48px;font-weight:700;line-height:1.15;color:#f1e9dd;animation:inR .55s cubic-bezier(.2,.9,.3,1.1) both}
.c b{flex:none;width:96px;height:96px;border-radius:50%;background:#e0561c;color:#1d1c1b;font-size:56px;font-weight:900;display:flex;align-items:center;justify-content:center}"""
    c = "".join(f'<div class="c" style="animation-delay:{1.3 + i * .85:.2f}s"><b>{i + 1}</b>{_h.escape(t)}</div>' for i, t in enumerate(puces))
    return _head(css) + _kick(p["theme"]) + f'<h1 style="font-size:{_fit(titre, 84)}px">{words(titre, .3, .12)}</h1><div class="cards">{c}</div>' + OUTRO


def illustration(p):
    _, _, ill, pied = p["visuel"]
    css = """
.halo{position:absolute;left:90px;top:380px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,#3a2418 0,#1d1c1b 70%);animation:pop .8s .1s both}
.g1{position:absolute;left:40px;top:330px;width:300px;height:300px;opacity:.9;animation:pop .6s .3s both}
.g1 svg,.g2 svg{width:100%;height:100%}
.g1 svg{animation:spin 5s linear infinite}
.g2{position:absolute;right:50px;top:1080px;width:200px;height:200px;animation:pop .6s .5s both}
.g2 svg{animation:spinR 3s linear infinite}
.ill{position:absolute;left:100px;top:520px;width:880px;height:733px;animation:pop .8s cubic-bezier(.2,.9,.3,1.3) .6s both}
.ill svg{width:100%;height:100%;animation:float 2.4s ease-in-out 1.4s infinite}
.ill .wheel{transform-box:fill-box;transform-origin:center;animation:spin .8s linear infinite}
.msg{position:absolute;left:80px;right:80px;top:1400px;text-align:center;font-weight:800;line-height:1.15;text-transform:uppercase;color:#f1e9dd}"""
    return (_head(css) + _kick(p["theme"]) + '<div class="halo"></div>'
            f'<div class="g1"><svg viewBox="0 0 112 112" fill="#e0561c">{GEAR_PATH}</svg></div><div class="g2"><svg viewBox="0 0 112 112" fill="#cfc3b1">{GEAR_PATH}</svg></div>'
            f'<div class="ill"><svg viewBox="0 0 480 400">{ILL[ill]}</svg></div>'
            f'<div class="msg" style="font-size:{_fit(_coupe(pied), 84)}px">{words(_coupe(pied), 2.0, .16)}</div>' + OUTRO)


def question(p):
    accro = _accroche(p["texte"])
    css = """
.q{position:absolute;top:300px;left:50%;margin-left:-160px;width:320px;height:320px;font-size:400px;font-weight:900;line-height:1;color:#e0561c;text-align:center;animation:zoom .8s cubic-bezier(.2,.9,.3,1.2) .2s both}
@keyframes zoom{from{opacity:0;transform:scale(2.2) rotate(-12deg);filter:blur(10px)}to{opacity:1;transform:none;filter:none}}
.t{position:absolute;top:760px;left:80px;right:80px;text-align:center;font-weight:800;line-height:1.18;color:#f1e9dd}
.btn{position:absolute;left:0;right:0;margin:0 auto;width:fit-content;top:1480px;white-space:nowrap;background:#e0561c;color:#1d1c1b;font-size:50px;font-weight:900;padding:34px 60px;border-radius:10px;animation:fadeUp .5s 3.2s both}
.btn i{position:absolute;inset:0;border-radius:10px;border:5px solid #e0561c;animation:ring 1.2s ease-out 3.7s infinite}
@keyframes ring{from{transform:scale(1);opacity:1}to{transform:scale(1.35,1.7);opacity:0}}"""
    taille = max(54, min(92, int(2600 / max(len(accro), 1) ** .82)))
    return (_head(css) + _kick(p["theme"]) + '<div class="q">?</div>'
            f'<div class="t" style="font-size:{taille}px">{words(accro, 1.0, .1)}</div>'
            '<div class="btn"><i></i>Écrivez-nous en MP</div>' + OUTRO)


def _fit(s, base, largeur=940):
    n = max(len(l.replace("*", "")) for l in s.split("|"))
    return min(base, int(largeur / (0.74 * n)))


def _coupe(s):
    """Coupe un message en deux lignes équilibrées."""
    m = s.split()
    if len(m) < 4: return s
    best = min(range(1, len(m)), key=lambda i: abs(len(" ".join(m[:i])) - len(" ".join(m[i:]))))
    return " ".join(m[:best]) + "|" + " ".join(m[best:])


def _accroche(texte):
    """Première ligne du texte, sans emoji (première phrase si elle est trop longue)."""
    l = texte.strip().split("\n")[0]
    l = re.sub(r"[\U0001F000-\U0001FAFF☀-➿️‍⬀-⯿]", "", l)
    l = re.sub(r"\s+", " ", l).strip()
    if len(l) > 100:  # trop long pour l'écran : première phrase seulement
        l = re.split(r"(?<=[.!?…])\s", l)[0]
    return l


REELS = [("reel-1-accroche", accroche), ("reel-2-points-cles", points), ("reel-3-illustration", illustration), ("reel-4-question", question)]
