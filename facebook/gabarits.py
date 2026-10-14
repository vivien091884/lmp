"""Gabarits HTML des visuels et vidéos SMTEC (charte : bleu nuit #0f1b2b, jaune #f5b400, Inter)."""
import html as _h
import re

Y = "#f5b400"

# ---------- Illustrations (viewBox 0 0 480 400) ----------
TRACK = lambda x, w: (f'<rect x="{x}" y="295" width="{w}" height="60" rx="30" fill="#2a2f36"/>'
                      + "".join(f'<circle cx="{x + 30 + i * (w - 60) / 4:.0f}" cy="325" r="{20 if i in (0, 4) else 15}" fill="#5b6470"/>' for i in range(5)))
WHEEL = lambda cx, cy, r: f'<circle class="wheel" cx="{cx}" cy="{cy}" r="{r}" fill="#2a2f36" stroke="#5b6470" stroke-width="{r * .3:.0f}" stroke-dasharray="{r * .6:.0f} {r * .3:.0f}"/><circle cx="{cx}" cy="{cy}" r="{r * .3:.0f}" fill="#8a94a0"/>'
GEAR_PATH = ('<path d="M50 0h12l3 14a38 38 0 0 1 11 5l12-8 9 9-8 12a38 38 0 0 1 5 11l14 3v12l-14 3a38 38 0 0 1-5 11l8 12-9 9-12-8'
             'a38 38 0 0 1-11 5l-3 14H50l-3-14a38 38 0 0 1-11-5l-12 8-9-9 8-12a38 38 0 0 1-5-11l-14-3V50l14-3a38 38 0 0 1 5-11l-8-12 9-9 12 8'
             'a38 38 0 0 1 11-5z"/><circle cx="56" cy="56" r="18" fill="#0f1b2b"/>')

ILL = {
    "pelle": f'''<g fill="{Y}"><rect x="60" y="210" width="230" height="80" rx="10"/><rect x="160" y="140" width="110" height="80" rx="8"/>
<rect x="172" y="152" width="86" height="50" rx="4" fill="#7fb3d9"/><path d="M260 200 L360 70 L385 85 L295 215 Z"/>
<path d="M360 70 L450 150 L430 168 L355 98 Z"/><path d="M430 160 L470 220 L415 245 L408 200 Z" fill="#d79c00"/></g>{TRACK(40, 290)}''',
    "bulldozer": f'''<g fill="{Y}"><rect x="90" y="200" width="250" height="90" rx="10"/><rect x="170" y="110" width="120" height="100" rx="8"/>
<rect x="184" y="124" width="92" height="56" rx="4" fill="#7fb3d9"/><path d="M340 230h50v20h-50z"/></g>
<path d="M390 160 q40 70 0 190 h30 q20-95 0-190z" fill="#d79c00"/>{TRACK(60, 310)}''',
    "chargeuse": f'''<g fill="{Y}"><rect x="40" y="200" width="250" height="90" rx="12"/><rect x="60" y="100" width="120" height="110" rx="8"/>
<rect x="74" y="114" width="92" height="64" rx="4" fill="#7fb3d9"/><path d="M270 220 L380 150 L395 170 L290 245 Z"/></g>
<path d="M370 120 h80 l20 90 h-110z" fill="#d79c00"/>{WHEEL(100, 310, 55)}{WHEEL(250, 310, 55)}''',
    "camion": f'''<rect x="20" y="110" width="290" height="190" rx="8" fill="#e8eef4"/><rect x="20" y="230" width="290" height="22" fill="{Y}"/>
<text x="44" y="200" font-family="Inter" font-weight="900" font-size="54" fill="#0f1b2b">PL</text>
<path d="M320 140h80l60 70v90H320z" fill="{Y}"/><path d="M334 154h60l46 54H334z" fill="#7fb3d9"/>
{WHEEL(90, 310, 40)}{WHEEL(200, 310, 40)}{WHEEL(390, 310, 40)}''',
    "fourgon": f'''<g transform="translate(30 110)"><rect x="0" y="40" width="260" height="120" rx="10" fill="#e8eef4"/><rect x="0" y="85" width="260" height="22" fill="{Y}"/>
<text x="22" y="76" font-family="Inter" font-weight="900" font-size="34" fill="#0f1b2b">SMTEC</text><path d="M260 70h80l50 50v40H260z" fill="#e8eef4"/>
<path d="M272 82h62l38 38h-100z" fill="#7fb3d9"/><rect x="384" y="132" width="20" height="12" rx="3" fill="{Y}"/>{WHEEL(70, 165, 32)}{WHEEL(330, 165, 32)}</g>''',
    "voiture": f'''<path d="M40 280 v-50 q0-30 30-35 l60-10 50-60 q10-10 25-10 h120 q15 0 25 12 l45 58 q45 5 45 45 v50z" fill="{Y}"/>
<path d="M195 135 h70 v50 h-110z M285 135 h45 l38 50 h-83z" fill="#7fb3d9"/>{WHEEL(130, 290, 42)}{WHEEL(350, 290, 42)}''',
    "cabine": f'''<rect x="140" y="60" width="300" height="290" rx="22" fill="#14324e" stroke="{Y}" stroke-width="10"/>
<rect x="100" y="110" width="44" height="200" rx="8" fill="#e8eef4" stroke="{Y}" stroke-width="4"/>
<g stroke="#c9d6e3" stroke-width="5">{"".join(f'<path d="M106 {130 + i * 20}h32"/>' for i in range(9))}</g>
<g fill="#b08a5a">{"".join(f'<circle cx="{20 + (i * 37) % 70}" cy="{110 + (i * 53) % 200}" r="{4 + i % 3 * 2}"/>' for i in range(14))}</g>
<g stroke="#7fd3ff" stroke-width="6" stroke-linecap="round"><path d="M190 160h90M210 210h110M190 260h80"/></g>
<circle cx="380" cy="115" r="38" fill="none" stroke="#7fd3ff" stroke-width="6"/><path d="M380 95v40M360 115h40" stroke="#7fd3ff" stroke-width="8" stroke-linecap="round"/>''',
    "engrenages": f'''<g fill="{Y}" transform="translate(40 30) scale(2.6)">{GEAR_PATH}</g><g fill="#7fb3d9" transform="translate(290 210) scale(1.4)">{GEAR_PATH}</g>''',
    "pieces": f'''<path d="M240 40 400 120v170L240 370 80 290V120z" fill="{Y}"/><path d="M240 40 400 120 240 200 80 120z" fill="#ffd34d"/>
<path d="M240 200v170" stroke="#d79c00" stroke-width="6"/><path d="M160 80 320 160v50" stroke="#0f1b2b" stroke-width="16" fill="none" opacity=".25"/>''',
    "batterie": f'''<rect x="80" y="110" width="320" height="220" rx="20" fill="#16263b" stroke="{Y}" stroke-width="10"/>
<rect x="130" y="80" width="50" height="30" rx="6" fill="{Y}"/><rect x="300" y="80" width="50" height="30" rx="6" fill="{Y}"/>
<g fill="#2ecc71">{"".join(f'<rect x="{115 + i * 66}" y="160" width="52" height="130" rx="8"/>' for i in range(4))}</g>
<path d="M140 50v24M128 62h24M312 62h24" stroke="#fff" stroke-width="6" stroke-linecap="round"/>''',
    "pneu": f'''<circle cx="240" cy="205" r="170" fill="#2a2f36"/><circle cx="240" cy="205" r="170" fill="none" stroke="#5b6470" stroke-width="34" stroke-dasharray="28 18"/>
<circle cx="240" cy="205" r="90" fill="#8a94a0"/><circle cx="240" cy="205" r="50" fill="{Y}"/>
{"".join(f'<circle cx="{240 + 70 * __import__("math").cos(i * 1.2566):.0f}" cy="{205 + 70 * __import__("math").sin(i * 1.2566):.0f}" r="9" fill="#2a2f36"/>' for i in range(5))}''',
    "huile": f'''<path d="M240 30 C240 30 100 190 100 260 a140 140 0 0 0 280 0 C380 190 240 30 240 30z" fill="{Y}"/>
<path d="M175 260 a65 65 0 0 0 65 65" stroke="#fff" stroke-width="16" fill="none" stroke-linecap="round" opacity=".6"/>''',
    "rapport": f'''<rect x="100" y="50" width="280" height="330" rx="18" fill="#e8eef4"/><rect x="180" y="30" width="120" height="44" rx="10" fill="{Y}"/>
{"".join(f'<path d="M140 {130 + i * 60} l14 14 26-30" stroke="#2ecc71" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/><rect x="200" y="{122 + i * 60}" width="140" height="16" rx="8" fill="#9fb0c2"/>' for i in range(4))}''',
    "bouclier": f'''<path d="M240 30 400 90v110c0 100-70 160-160 190C150 360 80 300 80 200V90z" fill="{Y}"/>
<path d="M165 205l50 50 100-110" stroke="#0f1b2b" stroke-width="26" fill="none" stroke-linecap="round" stroke-linejoin="round"/>''',
    "cyclone": f'''<path d="M120 230a80 80 0 0 1 30-150 110 110 0 0 1 200 20 70 70 0 0 1 10 130z" fill="#c9d6e3"/>
<g stroke="#7fd3ff" stroke-width="12" stroke-linecap="round" fill="none"><path d="M60 280h220a30 30 0 1 0-30-30"/><path d="M100 330h260a30 30 0 1 1-30 30"/></g>
<path d="M300 220l-40 70h40l-30 70" stroke="{Y}" stroke-width="14" fill="none" stroke-linejoin="round" stroke-linecap="round"/>''',
    "telephone": f'''<rect x="150" y="30" width="180" height="340" rx="30" fill="#e8eef4"/><rect x="166" y="70" width="148" height="250" rx="8" fill="#14324e"/>
<rect x="180" y="100" width="110" height="40" rx="14" fill="{Y}"/><rect x="200" y="160" width="100" height="40" rx="14" fill="#7fb3d9"/><rect x="180" y="220" width="80" height="40" rx="14" fill="{Y}"/>
<circle cx="240" cy="345" r="12" fill="#9fb0c2"/>''',
}

# ---------- Petites icônes (viewBox 0 0 24 24) ----------
ICO = {
    "cle": '<path fill="#0f1b2b" d="M22 19.6 13.4 11a5.5 5.5 0 0 0-7-7.1l3.4 3.4-2.4 2.4-3.4-3.4a5.5 5.5 0 0 0 7.1 7l8.6 8.6z"/>',
    "engin": '<g fill="#0f1b2b"><rect x="2" y="12" width="11" height="5" rx="1"/><rect x="6" y="8" width="5" height="5"/><path d="M12 12 17 5l1.5 1-4.5 7z"/><path d="M17 5l5 4-1 1-4-3z"/><rect x="1" y="18" width="14" height="4" rx="2"/></g>',
    "boite": '<path fill="#0f1b2b" d="M12 2 3 6.5v11L12 22l9-4.5v-11zm0 2.2 6.6 3.3L12 10.8 5.4 7.5zM5 9.2l6 3v7.3l-6-3zm8 10.3v-7.3l6-3v7.3z"/>',
    "air": '<path fill="none" stroke="#0f1b2b" stroke-width="2.6" stroke-linecap="round" d="M3 8h11a3 3 0 1 0-3-3M3 12h16a3 3 0 1 1-3 3M3 16h8"/>',
    "doc": '<path fill="#0f1b2b" d="M6 2h9l5 5v15H6zm8 1.5V8h4.5zM9 12h8v2H9zm0 4h8v2H9z"/>',
    "camion": '<path fill="#0f1b2b" d="M1 5h13v10H1zm14 3h4l4 4v3h-8zM5 19a2 2 0 1 0 0-.01zm13 0a2 2 0 1 0 0-.01zM1 16h22v1H1z"/>',
    "voiture": '<path fill="#0f1b2b" d="M3 12l2-6h14l2 6v6h-3v-2H6v2H3zm3-1h12l-1.3-3.5H7.3zM6.5 15a1.5 1.5 0 1 0 0-.01zm11 0a1.5 1.5 0 1 0 0-.01z"/>',
    "check": '<path fill="none" stroke="#0f1b2b" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" d="M4 12l5 5L20 6"/>',
    "eclair": '<path fill="#0f1b2b" d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    "pin": '<path fill="#0f1b2b" d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/>',
    "huile": '<path fill="#0f1b2b" d="M12 2S5 10 5 15a7 7 0 0 0 14 0c0-5-7-13-7-13z"/>',
    "filtre": '<path fill="#0f1b2b" d="M3 4h18l-7 8v7l-4 2v-9z"/>',
    "oeil": '<path fill="#0f1b2b" d="M12 5C6 5 2 12 2 12s4 7 10 7 10-7 10-7-4-7-10-7zm0 11a4 4 0 1 1 0-8 4 4 0 0 1 0 8z"/>',
    "etoile": '<path fill="#0f1b2b" d="M12 2l3 7h7l-5.5 4.5 2 7.5L12 17l-6.5 4 2-7.5L2 9h7z"/>',
    "mairie": '<path fill="#0f1b2b" d="M12 2 2 7v2h20V7zM4 10h3v8H4zm6.5 0h3v8h-3zM17 10h3v8h-3zM2 19h20v3H2z"/>',
    "horloge": '<path fill="#0f1b2b" d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 10.4 4 2.3-1 1.7-5-3V6h2z"/>',
}


def _segments(s):
    """'Air *pur* en cabine.' -> [('Air ', False), ('pur', True), (' en cabine.', False)]"""
    return [(t, i % 2 == 1) for i, t in enumerate(re.split(r"\*", s)) if t]


def fit(s, base, largeur=940):
    """Taille de police pour que la plus longue ligne du titre tienne dans la largeur."""
    n = max(len(l.replace("*", "")) for l in s.split("|"))
    return min(base, int(largeur / (0.53 * n)))


def words(s, start=0.2, step=0.15):
    """Titre animé mot par mot : *texte* = jaune (plusieurs mots possibles), | = retour à la ligne, _ = espace insécable."""
    out, i = [], 0
    for li, line in enumerate(s.split("|")):
        if li: out.append("<br>")
        for seg, y in _segments(line):
            for w in re.split(r"(\s+)", seg):
                if not w: continue
                if w.isspace(): out.append(" "); continue
                w = _h.escape(w).replace("_", "&nbsp;")
                out.append(f'<span class="w{" y" if y else ""}" style="animation-delay:{start + i * step:.2f}s">{w}</span>')
                i += 1
    return "".join(out)


def hl(s, tag="em"):
    """Titre statique : *texte* en jaune, | = retour à la ligne, _ = espace insécable."""
    out = []
    for li, line in enumerate(s.split("|")):
        if li: out.append("<br>")
        for seg, y in _segments(line):
            e = _h.escape(seg).replace("_", "&nbsp;")
            out.append(f"<{tag}>{e}</{tag}>" if y else e)
    return "".join(out)


HEAD = '<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="../base.css"><style>{css}</style></head><body>'
OUTRO = ('<div class="outro"><div class="logo">SMTEC<span>.</span></div><div class="tag">Mécanique engins &amp; véhicules · Nouvelle-Calédonie</div>'
         '<div class="cta">Écrivez-nous en MP</div></div><div class="stripe"></div></body></html>')
BRAND = '<div class="brand">SMTEC<span>.</span></div>'


# ---------- Visuel fixe ----------
def visuel(titre, puces, ill, pied):
    css = """
.bg{position:absolute;inset:0;background:radial-gradient(circle at 80% 30%,#1d3550 0,#0f1b2b 60%)}
.stripe{animation:none}
.top{position:absolute;top:70px;left:80px;right:80px}
.logo{font-family:'Inter Display',Inter;font-weight:900;font-size:120px;letter-spacing:-3px;line-height:1}
.logo span{color:#f5b400}
.tag{margin-top:14px;font-size:30px;font-weight:600;color:#c9d6e3;letter-spacing:.5px}
h1{position:absolute;top:290px;left:80px;width:620px;font-size:60px}
h1 em{font-style:normal;color:#f5b400}
ul{position:absolute;top:640px;left:80px;list-style:none;font-size:30px;font-weight:500;line-height:1.75}
li::before{content:"";display:inline-block;width:14px;height:14px;background:#f5b400;margin-right:18px;transform:rotate(45deg) translateY(-3px)}
.ill{position:absolute;right:40px;top:290px;width:400px;height:333px}
.foot{position:absolute;bottom:58px;left:80px;right:80px;display:flex;justify-content:space-between;align-items:center;font-size:28px;font-weight:600}
.foot span:first-child{padding-right:24px}
.badge{flex:none;white-space:nowrap;background:#f5b400;color:#0f1b2b;padding:14px 26px;border-radius:12px;font-weight:800}"""
    lis = "".join(f"<li>{_h.escape(p)}</li>" for p in puces)
    return (HEAD.format(css=css) + '<div class="bg"></div><div class="top"><div class="logo">SMTEC<span>.</span></div>'
            '<div class="tag">Mécanique engins &amp; véhicules · Nouvelle-Calédonie</div></div>'
            f'<h1 style="font-size:{fit(titre, 60, 640)}px">{hl(titre)}</h1><svg class="ill" viewBox="0 0 480 400">{ILL[ill]}</svg><ul>{lis}</ul>'
            f'<div class="foot"><span>{_h.escape(pied)}</span><span class="badge">Écrivez-nous en MP</span></div>'
            '<div class="stripe"></div></body></html>')


# ---------- Vidéos ----------
def v_cartes(titre, sous_titre, cartes):
    css = """
h1{position:absolute;top:150px;left:70px;right:70px;font-size:92px}
.sub{position:absolute;top:385px;left:70px;right:70px;font-size:36px;font-weight:600;color:#c9d6e3;animation:fadeUp .6s 1.3s both}
.grid{position:absolute;top:500px;left:70px;right:70px;display:grid;grid-template-columns:1fr 1fr;gap:24px}
.card{background:#16263b;border:2px solid #2b4562;border-radius:20px;padding:30px 28px;display:flex;align-items:center;gap:22px;font-size:31px;font-weight:700;min-height:150px;animation:pop .5s cubic-bezier(.2,.9,.3,1.3) both}
.ic{flex:none;width:70px;height:70px;border-radius:18px;background:#f5b400;display:flex;align-items:center;justify-content:center}"""
    c = "".join(f'<div class="card" style="animation-delay:{2.0 + i * .5:.1f}s"><div class="ic"><svg width="40" height="40" viewBox="0 0 24 24">{ICO[ic]}</svg></div>{_h.escape(t)}</div>'
                for i, (ic, t) in enumerate(cartes))
    return HEAD.format(css=css) + BRAND + f'<h1 style="font-size:{fit(titre, 92)}px">{words(titre)}</h1><div class="sub">{_h.escape(sous_titre)}</div><div class="grid">{c}</div>' + OUTRO


def v_route(titre, sous_titre, cible, message):
    css = """
h1{position:absolute;top:150px;left:70px;font-size:104px}
.sub{position:absolute;top:290px;left:70px;font-size:38px;font-weight:600;color:#c9d6e3;animation:fadeUp .6s 1.1s both}
.ground{position:absolute;left:0;right:0;top:830px;height:6px;background:#2b4562}
.road{position:absolute;left:0;right:0;top:842px;height:4px;background:repeating-linear-gradient(90deg,#2b4562 0 40px,transparent 40px 80px)}
.truck{position:absolute;left:0;top:520px;width:480px;height:400px;animation:drive 2.4s cubic-bezier(.3,.1,.2,1) .8s both}
@keyframes drive{from{transform:translateX(-560px)}to{transform:translateX(70px)}}
.truck .wheel{transform-box:fill-box;transform-origin:center;animation:spin .5s linear 5 .8s}
.cible{position:absolute;right:30px;top:476px;width:480px;height:400px;animation:fadeIn .4s .3s both}
.tool{position:absolute;left:680px;top:400px;width:120px;height:120px;border-radius:50%;background:#f5b400;display:flex;align-items:center;justify-content:center;animation:pop .45s cubic-bezier(.2,.9,.3,1.5) 3.3s both;z-index:3}
.tool svg{animation:wiggle .35s ease-in-out 3.8s 4 alternate}
@keyframes wiggle{from{transform:rotate(-25deg)}to{transform:rotate(25deg)}}
.ok{position:absolute;left:70px;right:70px;top:925px;display:flex;align-items:center;gap:20px;font-size:38px;font-weight:800;animation:fadeUp .5s 4.9s both}
.ok b{flex:none;width:58px;height:58px;border-radius:50%;background:#2ecc71;display:flex;align-items:center;justify-content:center}"""
    return (HEAD.format(css=css) + BRAND + f'<h1 style="font-size:{fit(titre, 104)}px">{words(titre)}</h1><div class="sub">{_h.escape(sous_titre)}</div>'
            '<div class="ground"></div><div class="road"></div>'
            f'<svg class="cible" viewBox="0 0 480 400">{ILL[cible]}</svg>'
            f'<svg class="truck" viewBox="0 0 480 400">{ILL["fourgon"].replace("translate(30 110)", "translate(30 150)")}</svg>'
            f'<div class="tool"><svg width="64" height="64" viewBox="0 0 24 24">{ICO["cle"]}</svg></div>'
            '<div class="ok"><b><svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12l5 5L20 6"/></svg></b>'
            f'{_h.escape(message)}</div>' + OUTRO)


def v_bmair(titre, sous_titre, puces):
    css = """
h1{position:absolute;top:150px;left:70px;font-size:96px}
.sub{position:absolute;top:270px;left:70px;font-size:38px;font-weight:600;color:#c9d6e3;animation:fadeUp .6s 1s both}
.dust{position:absolute;left:0;top:0;width:560px;height:1080px;overflow:hidden;animation:fadeIn .5s .4s both}
.dust i{position:absolute;left:-30px;border-radius:50%;background:#b08a5a;animation:fly 3s linear infinite}
@keyframes fly{0%{transform:translateX(0);opacity:0}10%{opacity:.9}88%{opacity:.9}100%{transform:translateX(560px);opacity:0}}
.cab{position:absolute;left:520px;top:400px;width:440px;height:400px;border:10px solid #f5b400;border-radius:26px 26px 12px 12px;background:#14324e;animation:pop .6s cubic-bezier(.2,.9,.3,1.3) .3s both}
.filter{position:absolute;left:500px;top:470px;width:54px;height:260px;border-radius:10px;background:repeating-linear-gradient(0deg,#e8eef4 0 10px,#c9d6e3 10px 20px);border:4px solid #f5b400;animation:pop .5s cubic-bezier(.2,.9,.3,1.4) 1.4s both}
.hepa{position:absolute;left:430px;top:745px;font-size:24px;font-weight:800;color:#0f1b2b;background:#f5b400;padding:6px 14px;border-radius:8px;animation:fadeUp .4s 1.7s both}
.air{position:absolute;left:600px;height:6px;width:120px;border-radius:3px;background:linear-gradient(90deg,transparent,#7fd3ff);animation:breeze 1.6s linear infinite}
@keyframes breeze{0%{transform:translateX(0);opacity:0}20%{opacity:1}100%{transform:translateX(220px);opacity:0}}
.airwrap{animation:fadeIn .5s 2s both}
.press{position:absolute;left:830px;top:420px;width:110px;height:110px;border-radius:50%;border:6px solid #7fd3ff;display:flex;align-items:center;justify-content:center;font-size:64px;font-weight:900;color:#7fd3ff;animation:pop .4s 2.6s both, pulse 1s ease-in-out 3s infinite}
@keyframes pulse{50%{transform:scale(1.12)}}
.list{position:absolute;left:70px;right:70px;top:870px;display:flex;flex-wrap:wrap;gap:16px}
.list div{background:#16263b;border:2px solid #2b4562;border-radius:14px;padding:14px 20px;font-size:27px;font-weight:700;animation:fadeUp .4s both}"""
    dust = "".join(f'<i style="top:{470 + i * 53 % 300}px;width:{8 + i % 3 * 4}px;height:{8 + i % 3 * 4}px;animation-delay:{-((i * .37) % 3):.2f}s"></i>' for i in range(36))
    air = "".join(f'<div class="air" style="top:{520 + i * 70}px;animation-delay:{-i * .45:.2f}s"></div>' for i in range(4))
    li = "".join(f'<div style="animation-delay:{3.4 + i * .4:.1f}s">{_h.escape(p)}</div>' for i, p in enumerate(puces))
    return (HEAD.format(css=css) + BRAND + f'<h1 style="font-size:{fit(titre, 96)}px">{words(titre)}</h1><div class="sub">{_h.escape(sous_titre)}</div>'
            f'<div class="dust">{dust}</div><div class="cab"></div><div class="airwrap">{air}</div>'
            f'<div class="filter"></div><div class="hepa">HEPA H13</div><div class="press">+</div><div class="list">{li}</div>' + OUTRO)


def v_checklist(titre, items, message):
    css = """
h1{position:absolute;top:150px;left:70px;font-size:100px}
.g1{position:absolute;left:40px;top:430px;width:400px;height:400px;animation:pop .6s .3s both}
.g1 svg{width:100%;height:100%;animation:spin 6s linear infinite}
.g2{position:absolute;left:330px;top:720px;width:220px;height:220px;animation:pop .6s .5s both}
.g2 svg{width:100%;height:100%;animation:spinR 3.3s linear infinite}
.list{position:absolute;left:560px;right:40px;top:400px;display:flex;flex-direction:column;gap:26px}
.it{display:flex;align-items:center;gap:24px;font-size:42px;font-weight:700;animation:fadeUp .45s both}
.it svg{flex:none}
.tick{stroke-dasharray:50;stroke-dashoffset:50;animation:draw .35s ease-out both}
@keyframes draw{to{stroke-dashoffset:0}}
.msg{position:absolute;left:70px;right:70px;top:960px;font-size:38px;font-weight:800;animation:fadeUp .5s 4.6s both}"""
    its = "".join(
        f'<div class="it" style="animation-delay:{1.6 + n * .55:.2f}s"><svg width="56" height="56" viewBox="0 0 56 56"><rect x="3" y="3" width="50" height="50" rx="12" fill="#16263b" stroke="#2b4562" stroke-width="4"/>'
        f'<path class="tick" style="animation-delay:{1.9 + n * .55:.2f}s" d="M14 29l9 9 19-20" fill="none" stroke="#f5b400" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>{_h.escape(t)}</div>'
        for n, t in enumerate(items))
    return (HEAD.format(css=css) + BRAND + f'<h1 style="font-size:{fit(titre, 100)}px">{words(titre)}</h1>'
            f'<div class="g1"><svg viewBox="0 0 112 112" fill="#f5b400">{GEAR_PATH}</svg></div><div class="g2"><svg viewBox="0 0 112 112" fill="#7fb3d9">{GEAR_PATH}</svg></div>'
            f'<div class="list">{its}</div><div class="msg">{hl(message).replace("<em>", "<span class=y>").replace("</em>", "</span>")}</div>' + OUTRO)


def v_chiffre(gros, legende, lignes, taille=300):
    css = f"""
.big{{position:absolute;top:170px;left:0;right:0;text-align:center;font-family:'Inter Display',Inter;font-weight:900;font-size:{taille}px;letter-spacing:-8px;color:#f5b400;line-height:1;animation:zoom .9s cubic-bezier(.2,.9,.3,1.2) .3s both}}
@keyframes zoom{{from{{opacity:0;transform:scale(2.4);filter:blur(12px)}}to{{opacity:1;transform:none;filter:none}}}}
.leg{{position:absolute;top:{170 + taille + 30}px;left:70px;right:70px;text-align:center;font-size:44px;font-weight:800;animation:fadeUp .6s 1.2s both}}
.lines{{position:absolute;top:{170 + taille + 150}px;left:120px;right:120px;display:flex;flex-direction:column;gap:22px}}
.ln{{display:flex;align-items:center;gap:22px;font-size:34px;font-weight:600;color:#dbe4ee;animation:slide .5s cubic-bezier(.2,.9,.3,1.1) both}}
.ln::before{{content:"";flex:none;width:18px;height:18px;background:#f5b400;transform:rotate(45deg)}}
@keyframes slide{{from{{opacity:0;transform:translateX(-80px)}}to{{opacity:1;transform:none}}}}
.ring{{position:absolute;left:50%;top:{170 + taille / 2}px;width:{taille * 1.9:.0f}px;height:{taille * 1.9:.0f}px;margin:-{taille * .95:.0f}px 0 0 -{taille * .95:.0f}px;border:6px solid #2b4562;border-radius:50%;animation:ring 2.4s ease-out .4s infinite}}
@keyframes ring{{from{{transform:scale(.4);opacity:1}}to{{transform:scale(1.15);opacity:0}}}}"""
    ln = "".join(f'<div class="ln" style="animation-delay:{2.2 + i * .6:.1f}s">{_h.escape(l)}</div>' for i, l in enumerate(lignes))
    return HEAD.format(css=css) + BRAND + f'<div class="ring"></div><div class="big">{_h.escape(gros)}</div><div class="leg">{hl(legende).replace("<em>", "<span class=y>").replace("</em>", "</span>")}</div><div class="lines">{ln}</div>' + OUTRO


def v_etapes(titre, etapes):
    css = """
h1{position:absolute;top:150px;left:70px;right:70px;font-size:88px}
.steps{position:absolute;top:430px;left:70px;right:70px;display:flex;flex-direction:column;gap:30px}
.st{display:flex;align-items:center;gap:30px;background:#16263b;border:2px solid #2b4562;border-radius:22px;padding:24px 30px;animation:slide .55s cubic-bezier(.2,.9,.3,1.1) both}
.n{flex:none;width:96px;height:96px;border-radius:50%;background:#f5b400;color:#0f1b2b;font-family:'Inter Display',Inter;font-weight:900;font-size:58px;display:flex;align-items:center;justify-content:center}
.st div:last-child{font-size:36px;font-weight:700;line-height:1.2}
.st small{display:block;font-size:26px;font-weight:500;color:#9fb0c2;margin-top:6px}
@keyframes slide{from{opacity:0;transform:translateX(-120px)}to{opacity:1;transform:none}}
.line{position:absolute;left:117px;top:470px;width:6px;height:0;background:#f5b400;animation:grow 3s linear 1.6s both}
@keyframes grow{to{height:380px}}"""
    st = "".join(f'<div class="st" style="animation-delay:{1.4 + i * 1.1:.1f}s"><div class="n">{i + 1}</div><div>{_h.escape(t)}<small>{_h.escape(s)}</small></div></div>'
                 for i, (t, s) in enumerate(etapes))
    return HEAD.format(css=css) + BRAND + f'<h1 style="font-size:{fit(titre, 88)}px">{words(titre)}</h1><div class="steps">{st}</div>' + OUTRO


VIDEOS = {"cartes": v_cartes, "route": v_route, "bmair": v_bmair, "checklist": v_checklist, "chiffre": v_chiffre, "etapes": v_etapes}
