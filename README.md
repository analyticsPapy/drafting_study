# 2025 DATEV Challenge ROTH - RaceRanger Report

## Contexte de l'étude

Ce rapport publié par **RaceRanger** présente des données issues de l’édition 2025 de la course **DATEV Challenge Roth**, une épreuve de triathlon de longue distance. L’objectif est de promouvoir le fair-play en analysant les comportements de "drafting" chez les athlètes professionnels. 

Le "drafting" — ou aspiration-abri — est interdit dans les courses non-drafting comme Challenge Roth. RaceRanger utilise des capteurs pour mesurer objectivement les moments où un athlète entre dans la zone de sillage d’un concurrent sans dépasser dans les 25 secondes autorisées.

Les données ont été nettoyées pour retirer les 500 premiers et derniers mètres, ainsi que les zones où les dépassements sont quasi impossibles (ravitaillements et grandes côtes).

## Structure des données

Chaque ligne du tableau correspond à un(e) athlète et comprend :

- **Finish Position** : position finale dans la course
- **Race #** : numéro de dossard
- **Athlete Name** : nom de l’athlète
- **Total Illegal Time** : temps total passé dans une zone de drafting non autorisé
- **YOYOs** : nombre d’entrées-sorties dans la zone de drafting sans dépassement
- **Favourite Race Wheel # / Athlete / Time** : athlète le plus suivi et le temps d’aspiration illégale derrière lui
- **Single Longest Illegal Follow** : plus longue phase continue de drafting illégal, avec l’heure et l’athlète concerné
- **Overtakes** : nombre de dépassements réalisés
- **Slot Ins** : insertions illégales entre deux coureurs sans espace réglementaire

Les données montrent que les premiers au classement ont globalement une conduite propre, tandis que certains athlètes accumulent un temps conséquent en infraction, souvent via des "yo-yos".

## Utilité

Ce tableau peut servir aux organisateurs, officiels ou analystes du triathlon pour :
- identifier des schémas récurrents d'infractions
- sensibiliser les athlètes aux règles
- améliorer l’équité et la sécurité des épreuves longue distance