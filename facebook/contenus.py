"""Les 29 publications SMTEC (jours de semaine du 16/10/2026 au 25/11/2026), dans l'ordre de diffusion.

Champs : theme, visuel=(titre, puces, illustration, pied), video=(gabarit, args...), texte, tags.
Dans les titres : *mot* = jaune, | = retour à la ligne, _ = espace insécable dans un mot animé.
"""

BASE = "#SMTEC #NouvelleCalédonie #Calédonie"

P = [
dict(theme="Présentation SMTEC",
 visuel=("Votre partenaire *mécanique*|en Calédonie.", ["Entretien & réparation sur site", "Engins, poids lourds, VL", "Pièces détachées & consommables", "Installateur agréé BMair"], "pelle", "Intervention sur vos chantiers"),
 video=("cartes", "Votre *mécanicien*|de chantier.", "Engins & véhicules · Nouvelle-Calédonie", [("cle", "Entretien & réparation"), ("engin", "SANY · SHANTUI · PL · VL"), ("boite", "Pièces détachées"), ("air", "Cabines filtrées BMair")]),
 texte="""👋 Vous ne nous connaissez pas encore ? On se présente !

SMTEC, c'est un atelier mobile de mécanique dédié aux engins de chantier et aux véhicules professionnels en Nouvelle-Calédonie.

🔧 Entretien et réparations, directement sur vos sites
🚜 Pelles, chargeuses, bulldozers (SANY, SHANTUI…), poids lourds, fourgons et VL
📦 Pièces détachées et consommables
🌬️ Revendeur et installateur agréé BMair pour la filtration des cabines

Notre objectif est simple : que vos machines restent au travail, pas à l'arrêt.

📩 Une question, un besoin d'entretien ? Écrivez-nous en message privé !""",
 tags="#Mécanique #EnginsDeChantier #BTP #Maintenance #SANY #SHANTUI"),

dict(theme="Intervention sur site",
 visuel=("On vient|*à vous.*", ["Déplacement sur vos chantiers", "Diagnostic sur place", "Réparation sans transport d'engin", "Moins d'immobilisation"], "fourgon", "Intervention sur vos chantiers"),
 video=("route", "On vient *à_vous.*", "Intervention directement sur vos chantiers", "pelle", "Moins d'immobilisation pour vos engins"),
 texte="""🚐 Votre engin est sur un chantier ? C'est là qu'on intervient.

Déplacer une pelle ou une chargeuse jusqu'à un atelier, c'est du temps, du transport et une machine qui ne produit pas. Chez SMTEC, on fait l'inverse : on vient à vous.

✅ Diagnostic sur place
✅ Entretien et réparations sur site
✅ Pièces et consommables apportés avec nous
✅ Rapport d'intervention après chaque passage

Résultat : votre engin repart plus vite et votre chantier avance.

📩 Besoin d'une intervention ? Écrivez-nous en message privé !""",
 tags="#InterventionSurSite #Mécanique #EnginsDeChantier #BTP #Chantier"),

dict(theme="BMair : air pur en cabine",
 visuel=("Air *pur*|en cabine.", ["Pressurisation de cabine", "Filtration HEPA H13", "Protection contre les poussières", "Installateur agréé BMair"], "cabine", "Santé des conducteurs = priorité"),
 video=("bmair", "Air *pur* en_cabine.", "Pressurisation & filtration BMair", ["Poussières bloquées", "Surpression", "Installateur agréé"]),
 texte="""🌬️ Vos conducteurs respirent-ils un air sain en cabine ?

Sur mine, en carrière ou sur chantier, les poussières finissent par entrer dans les cabines d'engins. Les systèmes BMair Protector et Protector Plus X règlent le problème :

🔹 La cabine est mise en surpression : l'air extérieur ne rentre plus par les interstices
🔹 L'air est filtré par un filtre HEPA H13
🔹 Le conducteur travaille dans un air propre, toute la journée

SMTEC est revendeur, installateur et réparateur agréé BMair en Nouvelle-Calédonie.

📩 Pour équiper vos engins, écrivez-nous en message privé !""",
 tags="#BMair #FiltrationCabine #SantéAuTravail #Mine #Carrière #Sécurité"),

dict(theme="Entretien préventif",
 visuel=("Entretien|*préventif.*", ["Vidange & filtres", "Contrôle des niveaux", "Pneus & batterie", "Points de sécurité"], "engrenages", "Moins de pannes, plus de production"),
 video=("checklist", "Entretien|*préventif.*", ["Vidange", "Filtres", "Pneus", "Batterie", "Sécurité"], "Moins de pannes, *plus_de_production.*"),
 texte="""⚙️ La meilleure réparation, c'est celle qu'on évite.

Un entretien préventif régulier permet de repérer l'usure avant qu'elle ne se transforme en panne… et en arrêt de chantier.

Lors de nos entretiens, on vérifie notamment :
✔️ Vidange et filtres
✔️ Niveaux et fuites
✔️ Pneus et trains de roulement
✔️ Batterie
✔️ Points de sécurité

Un engin suivi, c'est un engin qui dure, et des coûts mieux maîtrisés.

📩 Envie de mettre en place un suivi pour vos machines ? Écrivez-nous en message privé !""",
 tags="#EntretienPréventif #Maintenance #EnginsDeChantier #Mécanique #Flotte"),

dict(theme="Filtre HEPA H13 : toutes les 500 h",
 visuel=("Filtre BMair :|*500 h*|et on change.", ["Filtre HEPA H13", "Remplacement toutes les 500 h", "Numéro de série enregistré", "Intervention sur site"], "cabine", "Un filtre saturé ne protège plus"),
 video=("chiffre", "500 h", "Le rythme de remplacement du *filtre_HEPA_H13*", ["Filtre remplacé sur site", "Numéro de série tracé", "Cabine de nouveau protégée"]),
 texte="""⏱️ 500 heures : c'est l'intervalle normal de remplacement du filtre HEPA H13 d'un système BMair Protector.

Au-delà, le filtre se charge et la protection de la cabine diminue. Le bon réflexe : suivre les heures moteur et anticiper le changement.

Avec SMTEC :
🔹 On se déplace pour remplacer le filtre sur site
🔹 On relève et on enregistre le numéro de série du filtre (traçabilité)
🔹 On en profite pour vérifier l'état général de la machine

📩 Vos filtres arrivent à échéance ? Écrivez-nous en message privé !""",
 tags="#BMair #FiltreHEPA #FiltrationCabine #Maintenance #Mine #Carrière"),

dict(theme="3 réflexes pour faire durer vos engins",
 visuel=("3 réflexes pour|faire *durer*|vos engins.", ["Contrôler les niveaux", "Graisser régulièrement", "Surveiller le filtre à air", "Signaler vite toute anomalie"], "pelle", "De bons réflexes, des engins qui durent"),
 video=("etapes", "3 réflexes *au_quotidien*", [("Contrôler les niveaux", "Huile, liquide de refroidissement, hydraulique"), ("Graisser régulièrement", "Articulations et points de graissage"), ("Signaler toute anomalie", "Bruit, fuite, voyant : on agit tôt")]),
 texte="""💡 3 réflexes simples pour faire durer vos engins

1️⃣ Contrôler les niveaux avant de démarrer : huile moteur, liquide de refroidissement, hydraulique.
2️⃣ Graisser régulièrement les articulations : c'est ce qui protège les axes et les bagues.
3️⃣ Signaler vite toute anomalie : un bruit inhabituel, une petite fuite, un voyant… Plus on intervient tôt, moins la réparation coûte.

Ces gestes ne remplacent pas l'entretien périodique, mais ils font une vraie différence sur la durée de vie de vos machines.

📩 Un doute sur un engin ? Écrivez-nous en message privé !""",
 tags="#ConseilMécanique #EnginsDeChantier #Maintenance #BTP #Conducteurs"),

dict(theme="Engins SANY",
 visuel=("Engins *SANY* :|on s'en occupe.", ["Entretien périodique", "Diagnostic & réparation", "Pièces détachées", "Rapport après chaque visite"], "pelle", "Pelles, chargeuses et autres engins SANY"),
 video=("cartes", "Vos engins *SANY*", "Entretien, réparation et pièces", [("cle", "Entretien périodique"), ("oeil", "Diagnostic"), ("boite", "Pièces détachées"), ("doc", "Rapport détaillé")]),
 texte="""🚜 Vous travaillez avec des engins SANY ? SMTEC s'en occupe.

Pelles, chargeuses et autres matériels SANY : on assure leur entretien et leur réparation, directement sur vos chantiers.

🔧 Entretiens périodiques (vidanges, filtres, niveaux)
🔍 Diagnostic et réparation
📦 Approvisionnement en pièces détachées
📋 Rapport technique après chaque intervention

📩 Pour l'entretien de vos machines SANY, écrivez-nous en message privé !""",
 tags="#SANY #EnginsDeChantier #Pelle #Mécanique #Maintenance #BTP"),

dict(theme="Rapport technique après chaque visite",
 visuel=("Chaque visite,|un *rapport.*", ["Heures moteur & kilométrage", "Pneus, batterie, feux", "Extincteur & points de sécurité", "Photos à l'appui"], "rapport", "Vous savez où en est votre parc"),
 video=("checklist", "Un *rapport*|à chaque visite.", ["Heures moteur", "Pneus", "Batterie", "Feux", "Extincteur"], "Tout est *noté,_photographié,_suivi.*"),
 texte="""📋 Chez SMTEC, chaque intervention se termine par un rapport technique.

Vous savez précisément ce qui a été vérifié, ce qui a été fait et ce qui est à prévoir :
🔹 Kilométrage et heures moteur
🔹 État des pneus
🔹 Batterie (état de santé)
🔹 Feux, extincteur, contrôle technique
🔹 Chocs et anomalies, avec photos

C'est la base d'un suivi sérieux de votre parc… et un vrai plus lors des contrôles ou des audits.

📩 Envie d'y voir clair sur l'état de vos machines ? Écrivez-nous en message privé !""",
 tags="#RapportTechnique #Traçabilité #GestionDeFlotte #Maintenance #Mécanique"),

dict(theme="Poids lourds et camions",
 visuel=("Poids lourds :|on assure *aussi.*", ["Entretien périodique", "Réparations", "Contrôles de sécurité", "Intervention sur site"], "camion", "Vos camions aussi méritent un suivi"),
 video=("route", "Vos *camions* aussi.", "Entretien et réparation des poids lourds", "camion", "Vos camions restent sur la route"),
 texte="""🚛 SMTEC, ce n'est pas que les engins de chantier !

Nous assurons aussi l'entretien et la réparation de vos poids lourds :
🔧 Entretien périodique (vidanges, filtres, niveaux)
🔍 Diagnostic et réparations
🛞 Pneus, freinage, éclairage
🧯 Points de sécurité

Et toujours avec intervention possible sur votre site, pour limiter le temps d'immobilisation.

📩 Pour vos camions, écrivez-nous en message privé !""",
 tags="#PoidsLourds #Camion #Transport #Mécanique #Maintenance"),

dict(theme="Tour de parc",
 visuel=("Le *tour de parc*,|machine par|machine.", ["Inspection de chaque engin", "Un rapport par machine", "Priorités d'entretien", "Idéal pour planifier"], "rapport", "Une photo claire de l'état de votre parc"),
 video=("etapes", "Le *tour_de_parc* SMTEC", [("Inspection sur site", "Chaque engin et véhicule passé en revue"), ("Un rapport par machine", "Relevés, état, photos"), ("Un plan d'action", "Ce qui est urgent, ce qui peut attendre")]),
 texte="""🔎 Vous gérez plusieurs engins ou véhicules ? Pensez au tour de parc.

Le principe : on passe sur votre site et on inspecte vos machines une par une.

1️⃣ Inspection de chaque engin et véhicule
2️⃣ Un rapport par machine : heures, kilométrage, pneus, batterie, sécurité, photos
3️⃣ Une vision claire des priorités : ce qui est urgent, ce qui peut être planifié

Idéal pour préparer votre budget d'entretien et éviter les mauvaises surprises.

📩 Pour organiser un tour de parc, écrivez-nous en message privé !""",
 tags="#TourDeParc #GestionDeFlotte #Inspection #Maintenance #Entreprises"),

dict(theme="Engins SHANTUI",
 visuel=("Engins *SHANTUI* :|entretien|& réparation.", ["Bulldozers & chargeuses", "Entretien périodique", "Diagnostic & réparation", "Pièces détachées"], "bulldozer", "Intervention sur vos chantiers"),
 video=("route", "Vos engins *SHANTUI*", "Bulldozers, chargeuses et plus", "bulldozer", "Entretien et réparation sur site"),
 texte="""🚜 Bulldozers, chargeuses… vous avez des engins SHANTUI ? On s'en occupe aussi.

SMTEC assure l'entretien et la réparation des matériels SHANTUI directement sur vos sites :
🔧 Entretiens périodiques
🔍 Diagnostic et réparation
📦 Pièces détachées et consommables
📋 Rapport après chaque intervention

📩 Pour vos engins SHANTUI, écrivez-nous en message privé !""",
 tags="#SHANTUI #Bulldozer #Chargeuse #EnginsDeChantier #Mécanique #BTP"),

dict(theme="Mine et carrière : poussière",
 visuel=("La poussière ?|*Pas en cabine.*", ["Mine, carrière, terrassement", "Cabine en surpression", "Filtration HEPA H13", "Installation par SMTEC"], "cabine", "Revendeur & installateur agréé BMair"),
 video=("bmair", "Poussière ? *Dehors.*", "Mine · carrière · terrassement", ["Cabine en surpression", "Filtre HEPA H13", "Pose sur site"]),
 texte="""⛏️ Mine, carrière, terrassement : la poussière fait partie du décor… mais elle n'a rien à faire dans la cabine.

Respirer de la poussière toute la journée, c'est un vrai sujet de santé pour les conducteurs. La solution BMair :
🔹 Mise en surpression de la cabine
🔹 Filtration de l'air par filtre HEPA H13
🔹 Installation et entretien assurés par SMTEC, agréé BMair

📩 Pour équiper vos engins exposés, écrivez-nous en message privé !""",
 tags="#Mine #Carrière #BMair #FiltrationCabine #SantéAuTravail #Terrassement"),

dict(theme="Pièces détachées et consommables",
 visuel=("Pièces &|*consommables.*", ["Filtres & lubrifiants", "Pièces d'usure", "Filtres BMair", "Commande pour vos engins"], "pieces", "On s'occupe de trouver la bonne pièce"),
 video=("cartes", "La *bonne_pièce*, au_bon_moment.", "Pièces détachées et consommables", [("filtre", "Filtres"), ("huile", "Lubrifiants"), ("cle", "Pièces d'usure"), ("air", "Filtres BMair")]),
 texte="""📦 Une machine arrêtée faute de pièce, c'est du temps perdu.

SMTEC s'occupe aussi de l'approvisionnement en pièces détachées et consommables pour vos engins et véhicules :
🔹 Filtres (huile, gazole, air…)
🔹 Lubrifiants
🔹 Pièces d'usure
🔹 Filtres et pièces BMair

Vous nous dites quelle machine, on s'occupe de trouver la bonne référence.

📩 Besoin d'une pièce ? Écrivez-nous en message privé avec le modèle de votre engin !""",
 tags="#PiècesDétachées #Consommables #Filtres #EnginsDeChantier #Mécanique"),

dict(theme="Batterie : état de santé",
 visuel=("Votre batterie|est-elle en|*bonne santé ?*", ["Mesure de l'état de santé (SoH)", "Contrôle des bornes", "Test du démarrage", "Remplacement anticipé"], "batterie", "Évitez la panne au démarrage"),
 video=("chiffre", "SoH", "L'*état_de_santé* de votre batterie", ["Mesuré à chaque visite", "Noté dans le rapport", "Remplacement anticipé"]),
 texte="""🔋 Une batterie fatiguée prévient rarement : un matin, l'engin ne démarre plus.

À chaque visite, SMTEC mesure l'état de santé (SoH) de la batterie de vos engins et véhicules, et le note dans le rapport.

🔹 Vous voyez la batterie vieillir avant la panne
🔹 Vous pouvez planifier le remplacement au bon moment
🔹 Fini les chantiers bloqués au démarrage

📩 Pour un contrôle de vos batteries, écrivez-nous en message privé !""",
 tags="#Batterie #Maintenance #Prévention #EnginsDeChantier #Flotte"),

dict(theme="Pneus",
 visuel=("Pneus : la|*sécurité*|commence là.", ["Contrôle de l'usure", "Coupures & déformations", "Pression", "Suivi dans le rapport"], "pneu", "Des pneus suivis, des engins plus sûrs"),
 video=("checklist", "Vos *pneus*|sous_contrôle.", ["Usure", "Pression", "Coupures", "Déformations", "Suivi"], "Plus de sécurité, *moins_d'imprévus.*"),
 texte="""🛞 Sur chantier, les pneus souffrent : cailloux, ferraille, terrain accidenté…

Lors de nos visites, on contrôle l'état des pneus de vos engins et véhicules :
✔️ Niveau d'usure
✔️ Coupures, entailles et déformations
✔️ Pression
✔️ Et on note tout dans le rapport, pour suivre l'évolution

Un pneu surveillé, c'est moins de risques et moins de crevaisons en plein travail.

📩 Pour un contrôle, écrivez-nous en message privé !""",
 tags="#Pneus #Sécurité #EnginsDeChantier #PoidsLourds #Maintenance"),

dict(theme="Saison cyclonique : préparer ses engins",
 visuel=("Saison|*cyclonique :*|on anticipe.", ["Vérifier batteries & démarrage", "Faire le plein de consommables", "Sécuriser les engins", "Planifier l'entretien maintenant"], "cyclone", "Mieux vaut prévoir que réparer"),
 video=("etapes", "Saison cyclonique : *on_anticipe.*", [("Vérifier les engins", "Batteries, démarrage, niveaux"), ("Prévoir les consommables", "Filtres et lubrifiants en stock"), ("Planifier l'entretien", "Avant les épisodes de pluie")]),
 texte="""🌀 La saison cyclonique approche : c'est le bon moment pour faire le point sur vos engins.

1️⃣ Vérifier l'état des machines : batteries, démarrage, niveaux, éclairage
2️⃣ Prévoir les consommables : filtres et lubrifiants en stock, pour ne pas dépendre des délais
3️⃣ Planifier l'entretien maintenant, plutôt qu'en pleine période de fortes pluies

Des engins prêts, c'est un redémarrage plus rapide après les intempéries.

📩 Pour planifier un entretien avant la saison, écrivez-nous en message privé !""",
 tags="#SaisonCyclonique #Prévention #EnginsDeChantier #Maintenance #BTP"),

dict(theme="Sécurité avant démarrage",
 visuel=("Avant de|démarrer :|*les bons réflexes.*", ["Feux & avertisseurs", "Extincteur", "Rétroviseurs & visibilité", "Fuites sous la machine"], "bouclier", "La sécurité se vérifie chaque jour"),
 video=("checklist", "Avant de *démarrer.*", ["Feux", "Extincteur", "Rétroviseurs", "Ceinture", "Fuites"], "La sécurité, *chaque_jour.*"),
 texte="""🦺 Avant de démarrer un engin, quelques secondes de vérification peuvent éviter un accident.

✔️ Feux et avertisseurs fonctionnent
✔️ Extincteur présent et en état
✔️ Rétroviseurs propres et bien réglés
✔️ Ceinture de sécurité en bon état
✔️ Pas de fuite sous la machine

Lors de nos interventions, ces points de sécurité sont contrôlés et notés dans le rapport.

📩 Pour un contrôle de vos engins, écrivez-nous en message privé !""",
 tags="#Sécurité #PréventionDesRisques #EnginsDeChantier #Chantier #BTP"),

dict(theme="Collectivités et mairies",
 visuel=("Collectivités :|on entretient|*votre flotte.*", ["Engins de voirie", "Camions & utilitaires", "Véhicules légers", "Rapports pour vos services"], "camion", "Un interlocuteur pour tout votre parc"),
 video=("cartes", "Mairies & *collectivités*", "Un interlocuteur pour tout votre parc", [("engin", "Engins"), ("camion", "Camions & utilitaires"), ("voiture", "Véhicules légers"), ("doc", "Rapports détaillés")]),
 texte="""🏛️ Mairies, collectivités : SMTEC peut entretenir l'ensemble de votre parc.

🚜 Engins (pelles, chargeuses…)
🚛 Camions et utilitaires
🚗 Véhicules légers
📋 Un rapport par machine, pratique pour vos services techniques et votre suivi budgétaire

Un seul interlocuteur, des interventions sur place, une traçabilité complète.

📩 Pour en parler, écrivez-nous en message privé !""",
 tags="#Collectivités #Mairie #GestionDeFlotte #ServicesTechniques #Maintenance"),

dict(theme="Véhicules légers et utilitaires",
 visuel=("Véhicules|légers &|*utilitaires.*", ["Entretien périodique", "Diagnostic", "Freinage, pneus, éclairage", "Suivi de flotte"], "voiture", "Toute votre flotte au même endroit"),
 video=("route", "Vos *VL* aussi.", "Véhicules légers et utilitaires", "voiture", "Toute votre flotte suivie au même endroit"),
 texte="""🚗 Vos véhicules de service aussi ont besoin d'entretien !

SMTEC prend en charge les véhicules légers et utilitaires de votre entreprise :
🔧 Entretien périodique
🔍 Diagnostic
🛞 Pneus, freinage, éclairage
📋 Suivi dans le rapport, comme pour vos engins

Engins, camions, VL : toute votre flotte suivie par le même prestataire.

📩 Pour vos véhicules, écrivez-nous en message privé !""",
 tags="#VéhiculesUtilitaires #VL #GestionDeFlotte #Mécanique #Entretien"),

dict(theme="INRS ED 6228",
 visuel=("Air des cabines :|le *guide INRS.*", ["Aide-mémoire INRS ED 6228", "Assainissement de l'air", "Cabines d'engins mobiles", "Solutions BMair"], "cabine", "Une référence pour la prévention"),
 video=("chiffre", "ED 6228", "Le guide INRS sur *l'air_des_cabines*", ["Assainissement de l'air", "Cabines d'engins mobiles", "Solutions BMair"], 200),
 texte="""📘 Le saviez-vous ? L'INRS a publié un aide-mémoire dédié à la qualité de l'air dans les cabines d'engins : l'ED 6228, « Assainissement de l'air des cabines d'engins mobiles ».

Il explique pourquoi et comment protéger les conducteurs exposés aux poussières, notamment grâce à la filtration et à la mise en surpression des cabines.

C'est exactement le principe des systèmes BMair, que SMTEC installe et entretient en Nouvelle-Calédonie.

📩 Pour en savoir plus ou équiper vos engins, écrivez-nous en message privé !""",
 tags="#INRS #Prévention #SantéAuTravail #BMair #FiltrationCabine #Mine"),

dict(theme="En cas de panne",
 visuel=("Une *panne ?*|Voilà comment|on procède.", ["Vous nous contactez", "Diagnostic sur place", "Réparation ou commande de pièce", "Rapport d'intervention"], "telephone", "Réactivité et transparence"),
 video=("etapes", "Une *panne ?*", [("Vous nous écrivez", "Machine, lieu, symptômes"), ("On diagnostique sur place", "Pas besoin de déplacer l'engin"), ("On répare", "Ou on commande la pièce nécessaire")]),
 texte="""🚨 Un engin en panne sur votre chantier ? Voici comment on procède :

1️⃣ Vous nous contactez : type de machine, lieu, ce qui se passe (bruit, voyant, fuite…)
2️⃣ On se déplace pour le diagnostic, sans avoir besoin de transporter l'engin
3️⃣ On répare sur place, ou on commande la pièce nécessaire
4️⃣ Vous recevez un rapport d'intervention

📩 Une panne ? Écrivez-nous en message privé avec le maximum d'infos !""",
 tags="#Dépannage #Panne #EnginsDeChantier #Mécanique #InterventionSurSite"),

dict(theme="Vidange complète",
 visuel=("Une vidange,|*ce n'est pas*|*que l'huile.*", ["Huile moteur", "Filtre à huile", "Filtre à gazole", "Filtre à air & niveaux"], "huile", "Un moteur protégé plus longtemps"),
 video=("checklist", "Vidange|*complète.*", ["Huile moteur", "Filtre à huile", "Filtre gazole", "Filtre à air", "Niveaux"], "Un moteur protégé, *plus_longtemps.*"),
 texte="""🛢️ Une vidange, ce n'est pas seulement changer l'huile.

Pour bien protéger le moteur, on remplace aussi les filtres et on contrôle l'ensemble des niveaux :
✔️ Huile moteur
✔️ Filtre à huile
✔️ Filtre à gazole
✔️ Filtre à air
✔️ Niveaux (refroidissement, hydraulique…)

Et surtout : respecter les intervalles d'entretien prévus par le constructeur. C'est ce qui fait la différence sur la durée de vie du moteur.

📩 Une vidange à prévoir ? Écrivez-nous en message privé !""",
 tags="#Vidange #Entretien #Moteur #EnginsDeChantier #Maintenance"),

dict(theme="BMair Connect",
 visuel=("BMair|*Connect*|en Calédonie.", ["Système BMair connecté", "Adapté au réseau local", "Mise en service par SMTEC", "Suivi facilité"], "telephone", "Revendeur & installateur agréé BMair"),
 video=("cartes", "BMair *Connect*", "Mis en service par SMTEC en Nouvelle-Calédonie", [("air", "Système BMair"), ("eclair", "Connecté"), ("pin", "Réseau local"), ("cle", "Mise en service")]),
 texte="""📡 Vous utilisez ou envisagez BMair Connect ?

La version connectée des systèmes BMair nécessite une connexion réseau. En Nouvelle-Calédonie, SMTEC l'adapte au réseau local (carte SIM locale) pour qu'elle fonctionne correctement.

🔹 Installation et mise en service par SMTEC
🔹 Adaptation au réseau calédonien
🔹 Entretien et remplacement des filtres

📩 Pour plus d'infos sur BMair Connect, écrivez-nous en message privé !""",
 tags="#BMair #BMairConnect #FiltrationCabine #Connecté #Mine #Carrière"),

dict(theme="Traçabilité des filtres BMair",
 visuel=("Chaque filtre|*tracé.*", ["Filtre HEPA H13 remplacé", "Numéro de série relevé", "Enregistré dans l'appli BMair", "Noté dans le rapport"], "rapport", "Prêt en cas de contrôle"),
 video=("checklist", "Chaque filtre|*tracé.*", ["Filtre remplacé", "N° de série", "Appli BMair", "Rapport", "Archivé"], "Prêt *en_cas_de_contrôle.*"),
 texte="""🔎 Un filtre changé, c'est bien. Un filtre changé ET tracé, c'est mieux.

À chaque remplacement de filtre HEPA H13 sur un système BMair, SMTEC :
✔️ relève le numéro de série du filtre
✔️ l'enregistre dans l'application BMair
✔️ le reporte dans le rapport d'intervention

En cas de contrôle, vous pouvez prouver que la protection de vos conducteurs est bien entretenue.

📩 Pour l'entretien de vos systèmes BMair, écrivez-nous en message privé !""",
 tags="#BMair #Traçabilité #FiltreHEPA #SantéAuTravail #Conformité"),

dict(theme="Anticiper plutôt que subir",
 visuel=("*Anticiper*|coûte moins cher|que réparer.", ["Entretien planifié", "Usure repérée tôt", "Pièces commandées à l'avance", "Moins d'arrêts imprévus"], "engrenages", "Le préventif, c'est rentable"),
 video=("chiffre", "Anticiper", "plutôt que *subir_la_panne.*", ["Usure repérée tôt", "Pièces prévues à l'avance", "Moins d'arrêts imprévus"], 190),
 texte="""📅 Une panne imprévue coûte toujours plus cher qu'un entretien planifié.

Machine immobilisée, chantier ralenti, pièce à commander en urgence… alors qu'une partie de ces pannes se voit venir.

Avec un suivi régulier :
🔹 l'usure est repérée tôt
🔹 les pièces sont commandées à l'avance
🔹 les interventions sont planifiées quand ça vous arrange

📩 Mettons en place un plan d'entretien pour vos machines : écrivez-nous en message privé !""",
 tags="#Prévention #EntretienPréventif #Maintenance #Rentabilité #EnginsDeChantier"),

dict(theme="Nos engagements",
 visuel=("Nos|*engagements.*", ["Réactivité", "Transparence (rapport détaillé)", "Savoir-faire mécanique", "Proximité, sur vos sites"], "bouclier", "Ce que vous pouvez attendre de SMTEC"),
 video=("cartes", "Nos *engagements*", "Ce que vous pouvez attendre de SMTEC", [("eclair", "Réactivité"), ("doc", "Transparence"), ("cle", "Savoir-faire"), ("pin", "Proximité")]),
 texte="""🤝 Ce que vous pouvez attendre de SMTEC :

⚡ Réactivité : on se déplace sur vos sites pour limiter l'immobilisation
📋 Transparence : un rapport détaillé après chaque intervention, photos à l'appui
🔧 Savoir-faire : engins de chantier, poids lourds, véhicules légers, systèmes BMair
📍 Proximité : un interlocuteur local, qui connaît les contraintes calédoniennes

📩 Une question ? Écrivez-nous en message privé !""",
 tags="#Engagement #Confiance #Mécanique #EnginsDeChantier #Calédonie"),

dict(theme="Chargeuses",
 visuel=("Chargeuses :|*toujours prêtes*|à charger.", ["Entretien périodique", "Articulations & graissage", "Hydraulique", "Pneus"], "chargeuse", "Intervention directement sur vos sites"),
 video=("route", "Vos *chargeuses* au_top.", "Entretien et réparation sur site", "chargeuse", "Prêtes à charger, chaque jour"),
 texte="""🚜 La chargeuse, c'est souvent la machine qui ne s'arrête jamais sur un site.

Elle mérite un suivi régulier :
🔧 Entretien périodique (vidange, filtres, niveaux)
🔩 Contrôle des articulations et graissage
💧 Vérification du circuit hydraulique
🛞 État des pneus

SMTEC intervient directement sur votre site pour l'entretien et les réparations.

📩 Pour vos chargeuses, écrivez-nous en message privé !""",
 tags="#Chargeuse #EnginsDeChantier #Carrière #Maintenance #Mécanique"),

dict(theme="Demander un devis",
 visuel=("Un *devis ?*|Envoyez-nous|3 infos.", ["Le type et modèle de machine", "Les heures moteur / km", "Votre besoin", "Le lieu d'intervention"], "telephone", "On revient vers vous rapidement"),
 video=("etapes", "Un devis ? *3_infos.*", [("La machine", "Type, marque et modèle"), ("Les heures moteur", "Ou le kilométrage"), ("Votre besoin", "Entretien, panne, pièce, BMair…")]),
 texte="""📝 Vous voulez un devis ? Pour aller vite, envoyez-nous en message privé :

1️⃣ La machine : type, marque et modèle
2️⃣ Les heures moteur (ou le kilométrage)
3️⃣ Votre besoin : entretien, panne, pièce, installation BMair…

Et précisez le lieu d'intervention. Avec ces infos, on peut vous répondre rapidement et précisément.

📩 À vous de jouer : écrivez-nous en message privé !""",
 tags="#Devis #Mécanique #EnginsDeChantier #Entretien #Calédonie"),

dict(theme="Récapitulatif : SMTEC à votre service",
 visuel=("SMTEC,|*à votre service.*", ["Engins de chantier", "Poids lourds & VL", "Pièces & consommables", "Systèmes BMair"], "pelle", "Merci de nous suivre !"),
 video=("cartes", "Merci de nous *suivre !*", "SMTEC, à votre service", [("engin", "Engins de chantier"), ("camion", "Poids lourds & VL"), ("boite", "Pièces"), ("air", "BMair")]),
 texte="""🙏 Merci de suivre la page SMTEC !

Petit rappel de ce qu'on peut faire pour vous :
🚜 Entretien et réparation d'engins de chantier (SANY, SHANTUI…)
🚛 Poids lourds, utilitaires et véhicules légers
📦 Pièces détachées et consommables
🌬️ Installation et entretien des systèmes BMair
📋 Rapport technique après chaque intervention

N'hésitez pas à partager cette page à ceux qui pourraient en avoir besoin !

📩 Et pour toute demande : écrivez-nous en message privé.""",
 tags="#Mécanique #EnginsDeChantier #PoidsLourds #BMair #Maintenance"),
]

# Publications du week-end (samedi et dimanche) pour avoir une publication par jour du 21/10 au 18/11/2026, dans l'ordre de diffusion.
W = [
dict(theme="Liquide de refroidissement et chaleur",
 visuel=("Chaleur :|gardez votre moteur|*au frais.*", ["Niveau de liquide à froid", "Radiateur propre et dégagé", "Durites sans fissure", "Ventilateur & courroie"], "engrenages", "Surchauffe = casse moteur"),
 video=("checklist", "Moteur|*au_frais.*", ["Niveau", "Radiateur", "Durites", "Courroie"], "Pas de surchauffe, *pas_de_casse.*"),
 texte="""🌡️ Avec la chaleur calédonienne, le circuit de refroidissement de vos engins travaille dur.

Une surchauffe peut abîmer sérieusement un moteur. Quelques contrôles simples :
✔️ Vérifier le niveau de liquide de refroidissement, moteur froid (jamais bouchon ouvert à chaud !)
✔️ Garder le radiateur propre : poussière et latérite bouchent les ailettes
✔️ Contrôler l'état des durites
✔️ Vérifier le ventilateur et la courroie

Au moindre doute sur la température moteur, on arrête et on vérifie.

📩 Besoin d'un contrôle ? Écrivez-nous en message privé !""",
 tags="#Refroidissement #Moteur #ConseilMécanique #EnginsDeChantier #Maintenance"),

dict(theme="Bulldozers : le train de roulement",
 visuel=("Bulldozers :|surveillez le|*train de roulement.*", ["Tension des chenilles", "Galets & barbotins", "Patins et boulons", "Nettoyage régulier"], "bulldozer", "Les chenilles, ça s'entretient"),
 video=("route", "Vos *bulldozers* au_top.", "Train de roulement contrôlé sur site", "bulldozer", "Chenilles vérifiées, engin prêt"),
 texte="""🚜 Sur un bulldozer, le train de roulement représente une grosse part des coûts d'entretien.

Les bons réflexes :
🔹 Vérifier la tension des chenilles : trop tendues ou trop lâches, elles s'usent plus vite
🔹 Surveiller galets, barbotins et roues folles
🔹 Contrôler les patins et le serrage des boulons
🔹 Nettoyer régulièrement : la boue et les cailloux accélèrent l'usure

SMTEC contrôle et entretient vos bulldozers (SHANTUI et autres marques) directement sur vos chantiers.

📩 Écrivez-nous en message privé !""",
 tags="#Bulldozer #SHANTUI #Chenilles #EnginsDeChantier #Maintenance"),

dict(theme="Voyant rouge : les bons gestes",
 visuel=("Voyant *rouge ?*|On s'arrête.", ["Arrêter l'engin en sécurité", "Ne pas insister", "Noter le voyant et les heures", "Nous appeler"], "telephone", "Mieux vaut un arrêt qu'une casse"),
 video=("etapes", "Voyant rouge ? *3_gestes*", [("On s'arrête", "Engin à l'arrêt, en sécurité"), ("On ne redémarre pas", "Pression d'huile, température : on ne force pas"), ("On nous appelle", "Voyant, heures moteur, photo")]),
 texte="""🚨 Un voyant rouge s'allume sur le tableau de bord ? Ce n'est pas le moment d'insister.

Pression d'huile, température moteur, charge… Un voyant rouge signale un problème sérieux.

1️⃣ Arrêtez l'engin dès que possible, en sécurité
2️⃣ Ne redémarrez pas « pour voir » : c'est souvent comme ça qu'une petite panne devient une grosse casse
3️⃣ Notez le voyant, les heures moteur, prenez une photo et contactez-nous

📩 Un voyant allumé ? Écrivez-nous en message privé !""",
 tags="#Sécurité #Panne #ConseilMécanique #EnginsDeChantier #Conducteurs"),

dict(theme="Moteur : 3 bonnes pratiques",
 visuel=("Votre moteur|vous dit|*merci.*", ["Laisser monter en température", "Éviter le ralenti prolongé", "Laisser refroidir avant l'arrêt", "Respecter les vidanges"], "engrenages", "De bonnes habitudes, un moteur qui dure"),
 video=("etapes", "Moteur : *3_habitudes*", [("Chauffer en douceur", "Quelques minutes avant de forcer"), ("Éviter le ralenti prolongé", "Carburant gaspillé, moteur encrassé"), ("Refroidir avant l'arrêt", "Un peu de ralenti après un gros effort")]),
 texte="""🛠️ 3 habitudes simples qui prolongent la vie d'un moteur diesel :

1️⃣ Laisser le moteur monter en température quelques minutes avant de le solliciter fort.
2️⃣ Éviter les longs ralentis inutiles : carburant gaspillé et moteur qui s'encrasse.
3️⃣ Après un travail intensif, laisser tourner un peu au ralenti avant de couper : le turbo vous remerciera.

Bon dimanche à tous !

📩 Une question sur vos moteurs ? Écrivez-nous en message privé.""",
 tags="#Moteur #Diesel #ConseilMécanique #EnginsDeChantier #Maintenance"),

dict(theme="Filtre à air moteur et poussière",
 visuel=("Poussière :|le *filtre à air*|en première ligne.", ["Contrôle régulier", "Remplacement à l'échéance", "Joint et boîtier étanches", "Préfiltre nettoyé"], "pieces", "Un moteur qui respire bien dure plus"),
 video=("cartes", "Le *filtre_à_air*, ça_compte", "Poussière et latérite : protégez le moteur", [("filtre", "Contrôle régulier"), ("horloge", "Remplacement à l'échéance"), ("check", "Boîtier étanche"), ("oeil", "Indicateur surveillé")]),
 texte="""💨 Sur nos chantiers et nos mines, la poussière est partout… y compris là où elle ne devrait pas aller : dans le moteur.

Le filtre à air est sa première protection :
🔹 Contrôlez-le régulièrement, surtout en milieu très poussiéreux
🔹 Remplacez-le à l'échéance, sans attendre qu'il soit colmaté
🔹 Vérifiez l'étanchéité du boîtier et du joint
🔹 Surveillez l'indicateur de colmatage s'il y en a un

Un filtre colmaté, c'est un moteur qui perd en puissance et consomme plus.

📩 Besoin de filtres ou d'un entretien ? Écrivez-nous en message privé !""",
 tags="#FiltreAir #Moteur #Poussière #Mine #EnginsDeChantier"),

dict(theme="Engin à l'arrêt prolongé",
 visuel=("Engin|*à l'arrêt ?*|Préparez-le.", ["Pleins faits, niveaux OK", "Batterie débranchée ou chargée", "Vérins rentrés, graissés", "Remise en route contrôlée"], "pelle", "Un redémarrage sans mauvaise surprise"),
 video=("etapes", "Arrêt prolongé ? *3_étapes*", [("Avant l'arrêt", "Niveaux faits, engin propre"), ("Pendant", "Batterie protégée, vérins rentrés"), ("Au redémarrage", "Contrôle complet avant de travailler")]),
 texte="""⏸️ Un engin qui reste plusieurs semaines sans tourner (fin de chantier, congés, saison calme) ? Quelques précautions évitent les mauvaises surprises :

1️⃣ Avant l'arrêt : niveaux faits, engin nettoyé, plein de carburant pour limiter la condensation
2️⃣ Pendant : batterie débranchée ou maintenue en charge, vérins rentrés et graissés pour protéger les tiges
3️⃣ Au redémarrage : contrôle des niveaux, des fuites et de la batterie avant de reprendre le travail

📩 On peut s'occuper de la remise en route de vos engins : écrivez-nous en message privé !""",
 tags="#ConseilMécanique #EnginsDeChantier #Batterie #Maintenance #Hivernage"),

dict(theme="Utilitaires : avant de prendre la route",
 visuel=("Avant la route,|*un contrôle.*", ["Pneus & pression", "Freins", "Éclairage", "Niveaux & essuie-glaces"], "fourgon", "Utilitaires et VL prêts à rouler"),
 video=("route", "Prêt pour *la_route ?*", "Contrôle de vos utilitaires et VL", "camion", "Pneus, freins, feux : vérifiés"),
 texte="""🚐 Vos fourgons, pick-up et utilitaires roulent beaucoup entre Nouméa et la brousse. Avant un long trajet, quelques points à vérifier :

✅ Pneus : usure et pression (roue de secours comprise)
✅ Freins : bruit, vibration, efficacité
✅ Éclairage et clignotants
✅ Niveaux : huile, liquide de refroidissement, lave-glace
✅ Essuie-glaces

SMTEC entretient aussi les véhicules légers et utilitaires de votre flotte.

📩 Un contrôle avant la route ? Écrivez-nous en message privé !""",
 tags="#Utilitaires #VL #Flotte #Sécurité #Entretien"),

dict(theme="Fuites hydrauliques",
 visuel=("Petite fuite,|*gros risques.*", ["Flexibles usés ou frottés", "Raccords desserrés", "Joints de vérins", "Niveau d'huile hydraulique"], "huile", "Une fuite se traite tout de suite"),
 video=("checklist", "Fuite|*hydraulique ?*", ["Flexibles", "Raccords", "Vérins", "Niveau"], "On répare *avant_la_casse.*"),
 texte="""💧 Une petite tache d'huile sous l'engin ? Ne la laissez pas grandir.

Une fuite hydraulique, c'est :
⚠️ Un risque pour la sécurité (un flexible qui éclate, c'est dangereux)
⚠️ Une perte de puissance et de précision
⚠️ De l'huile qui coûte cher… et qui pollue

Les points à surveiller : flexibles usés ou qui frottent, raccords desserrés, joints de vérins, niveau d'huile hydraulique.

⚠️ Ne cherchez jamais une fuite sous pression avec la main.

📩 Une fuite repérée ? Écrivez-nous en message privé !""",
 tags="#Hydraulique #Sécurité #EnginsDeChantier #Maintenance #Environnement"),
]
