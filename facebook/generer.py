"""Génère les dossiers AAAA-MM-JJ (publication.md, visuel.html, video.html) pour chaque jour de semaine à partir du 16/10/2026,
puis les week-ends à partir du 24/10/2026 (une publication par jour du 21/10 au 18/11).
Rendu PNG/MP4 ensuite avec rendre.js :  python3 generer.py && node rendre.js"""
import datetime as dt, json, os
from contenus import P, W, BASE
from gabarits import visuel, VIDEOS
from reels import REELS, DUREE_REEL

REELS_DU, REELS_AU = dt.date(2026, 10, 21), dt.date(2026, 11, 18)  # 5 vidéos par jour sur ces 29 jours

def jours(debut, n):
    d = debut
    while n:
        if d.weekday() < 5:
            yield d; n -= 1
        d += dt.timedelta(1)

def week_ends(debut, n):
    d = debut
    while n:
        if d.weekday() >= 5:
            yield d; n -= 1
        d += dt.timedelta(1)

JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
index = []
pubs = sorted([*zip(jours(dt.date(2026, 10, 16), len(P)), P), *zip(week_ends(dt.date(2026, 10, 24), len(W)), W)], key=lambda x: x[0])
for d, p in pubs:
    rep = d.isoformat(); os.makedirs(rep, exist_ok=True)
    open(f"{rep}/visuel.html", "w").write(visuel(*p["visuel"]))
    g, *args = p["video"]
    open(f"{rep}/video.html", "w").write(VIDEOS[g](*args))
    fichiers = "**Fichiers :** visuel-smtec.png (image 1080×1080) · video-smtec.mp4 (vidéo 9,5 s, 1080×1080)"
    if REELS_DU <= d <= REELS_AU:
        for nom, f in REELS:
            open(f"{rep}/{nom}.html", "w").write(f(p))
        fichiers += (f"\n\n**Vidéos verticales 1080×1920 ({DUREE_REEL} s) pour Stories, Reels et WhatsApp :** "
                     + " · ".join(f"{nom}.mp4" for nom, _ in REELS))
    open(f"{rep}/publication.md", "w").write(
        f"# {JOURS[d.weekday()].capitalize()} {d:%d/%m/%Y} : {p['theme']}\n\n"
        f"{fichiers}\n\n---\n\n"
        f"{p['texte']}\n\n{BASE} {p['tags']}\n")
    index.append((d, p["theme"], g))
json.dump([d.isoformat() for d, *_ in index], open("dates.json", "w"))
with open("calendrier.md", "w") as f:
    f.write("# Calendrier éditorial Facebook SMTEC\n\nUne publication par jour du 21/10 au 18/11/2026 (week-ends compris), puis en semaine jusqu'au 25/11, préparée à l'avance : `facebook/AAAA-MM-JJ/` contient "
            "`publication.md` (texte à copier-coller), `visuel-smtec.png` et `video-smtec.mp4`.\n\n"
            "Du 21/10 au 18/11, **5 vidéos par jour** : `video-smtec.mp4` (vidéo principale de la publication, carrée) + 4 vidéos verticales "
            "1080×1920 pour Stories, Reels et WhatsApp (`reel-1-accroche`, `reel-2-points-cles`, `reel-3-illustration`, `reel-4-question`).\n\n"
            "Pour modifier un contenu : éditer `contenus.py`, puis `python3 generer.py && node rendre.js && node rendre_reels.js`.\n\n"
            "| Date | Thème | Vidéo |\n|---|---|---|\n| 14/10/2026 | Présentation SMTEC (image seule) | – |\n")
    for d, t, g in index:
        f.write(f"| {JOURS[d.weekday()][:3]}. {d:%d/%m/%Y} | {t} | {g} |\n")
print(len(index), "publications :", index[0][0], "→", index[-1][0])
