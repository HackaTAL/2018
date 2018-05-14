![Hackathon CORIA-TALN 2018](https://raw.githubusercontent.com/HackaTAL/2018/gh-pages/Hackathon_CORIA-TALN_2018.gif)

# Fake ou pas Fake ?

## Hackathon CORIA-TALN 2018
---------------
*(hackathon en recherche d’information et traitement automatique des langues)*

### Résumé

Tâches : détection et visualisation de fausses informations sur les réseaux  
Site web : http://hackatal.github.io/2018  
Dates : 14 et 15 mai 2018  
Lieu : IRISA, Rennes  
Prix : Qwant (par vote)  
Inscription (gratuite mais obligatoire) : https://goo.gl/forms/soTeFTikjWol8bj13  

### Description

Dans le cadre de la conférence CORIA-TALN-RJC 2018 est organisé un hackathon, 3ème édition côté CORIA (Hack Days) et TALN (HackaTAL). L’évènement porte sur des problématiques en RI et en TAL. L’objectif est de réunir les communautés scientifiques, et au delà, autour de défis à relever, pour modéliser, prototyper, coder, expérimenter, développer, tester, évaluer, échanger, etc. - par équipes, dans une ambiance décontractée :) !

Les tâches proposées portent cette année sur la détection et le traitement d’informations manifestement fausses, un sujet de préoccupation pour les médias et citoyens. Ces problématiques, nouvelles pour la société de l’information, soulèvent de nombreuses questions et nous essaierons de voir si des traitements RI et TAL peuvent y répondre, pour mieux comprendre les phénomènes en jeu et y réagir, plus rapidement et de manière plus adéquate, à l’aide d’algorithmes du domaine.

Un jeu de données sera fourni par la société Storyzy sur la thématique de la vaccination, qui est un sujet occasionnant la diffusion de nombreuses fausses nouvelles. Il contiendra des textes provenant de divers sites web en anglais et en français, ainsi que des transcriptions automatiques de vidéos sur cette même thématique.

L’événement est ouvert à tous (informaticiens, linguistes, journalistes), ne nécessite aucune préparation particulière et ne requiert pas de compétences spécifiques aux tâches que nous proposons... tout le monde est bienvenu !

### Tâches

**1. Détection : repérer et catégoriser les fausses informations**

*Objectifs*

Parmi les informations disponibles en ligne certaines sont manifestement fausses et il n’est pas évident de faire la part des choses, autant pour les médias, entreprises ou laboratoires (notamment à cause des volumes de données à traiter), que pour les citoyens : quels indices caractérisent les fausses informations ? L’objectif de cette tâche est de voir si des algorithmes TAL et RI sont capables de détecter et catégoriser finement ces fausses informations.

*Sous-tâches*

- parmi un ensemble de textes, déterminer automatiquement lesquels sont des faux (contrefactuels, détournés, trompeurs, parodiques),
- catégoriser les fausses informations parmi un ensemble de catégories prédéfinies (sites propagandistes, conspirationnistes, pseudo-science, satires),
- caractériser les faux d’un point de vue linguistique : quels modes d’expression, quelles tournures sont utilisées pour propager de fausses informations.

**2. Visualisation : agrégation des fausses nouvelles pour une vision synthétique**

*Objectifs*

Le traitement des fausses nouvelles soulève d’autres questions lorsque l’on tient compte des liens (informationnels, thématiques, linguistiques) entre ces dernières, ou au sein des médias et des réseaux sociaux. Certaines reprennent des fausses nouvelles déjà connues, les complètent ou les modifient. Il est aussi intéressant d’étudier les mécanismes de leur propagation sur des réseaux (statiques) ou sur les relations temporelles (dynamiques).

*Sous-tâches*

- regrouper les fausses nouvelles de manière non-supervisée ou peu supervisée,
- déterminer la structure d’un réseau de fausses nouvelles, pour identifier des liens orientés selon l’axe temporel et l’axe thématique,
- détecter des communautés (sites ou individus) qui propagent des fausses nouvelles.

### Prix Qwant

Qwant soutient l’événement et apporte un prix à une équipe, selon des critères liées à l’originalité et l’adéquation de la solution proposée à la tâche choisie. Le prix sera attribué selon un vote des participants et organisateurs, le mardi soir.

### Planning

Lundi 14 mai :

- 13h-14h : accueil et café
- 14h-15h : présentation du hackathon
- 15h-18h : développements en équipes
- 18h-19h : présentations invitées
	- Denis Teyssou, [AFP](https://www.afp.com) - Quelques cas « réels » de désinformation du point de vue du TAL
	- Arnaud Bichet, [Storyzy](http://storyzy.com) - Brand Safety : protéger la marque contre les Fake News
	- Timothée Gidoin, [Datagora](https://www.datagora.fr/) - Comment utiliser au mieux les données statistiques publiques pour lutter contre la désinformation ?
	- Christophe Servan, [Qwant](http://qwant.com) - TBA
	- Emmanuel Vincent, [Climate Feedback](http://climatefeedback.org) - Une approche collaborative pour contrer la désinformation scientifique sur le climat
- 19h-20h : pause repas
- 20h-00h : développements en équipes

Mardi 15 mai :

- 09h-12h : accueil, café, développements en équipes
- 12h-14h : déjeuner et café
- 14h-17h : développements en équipes
- 17h-18h : présentation des résultats
- 18h-19h : cocktail
- 18h-19h : remise du prix et conclusion

### Organisation pratique

BYOD (amenez votre ordinateur)  
Pas de critères pour participer, le hackathon est ouvert à tous !  
Aucune préparation requise des participants en amont de l’évènement  

**Données**

[Données train et test, script d'évaluation](http://damien.nouvels.net/bazar/hackathon2018/)

**Explications sur les script d'évaluation**

*Format attendu*

Fichier tabulaire tsv contenant deux champs : id et type.

*Évaluation d'un fichier : eval-hackathon2018.py*

```bash
python3 eval-hackathon2018.py -h
Usage :
usage: eval-hackathon2018.py [-h] [-g GOLD] [-p PRED] [-s]
optional arguments:
  -h, --help            show this help message and exit
  -g GOLD, --gold GOLD  gold path file
  -p PRED, --pred PRED  pred path file
  -s, --satire          include satire (only for english)
```

Exemple :

`python3 eval-hackathon2018.py -g storyzy_en_ref.tsv -p storyzy_en_hyp.tsv`

*Évaluation globale sur en, fr, yt : summary-eval.sh*

Script pour avoir un résumé global rapidement (c'est juste un raccourci).

`sh summary-eval.sh [GOLD_FR] [PRED_FR] [GOLD_EN] [PRED_EN] [GOLD_YT] [PRED_YT]`

Inscrivez-vous sur la [Liste des participants](https://docs.google.com/spreadsheets/d/18Z6Zm4Ixpx91x7Y1F7yt0iOZvSn41aYXYFGgIGoNFnk/edit?usp=sharing)

Logiciels et données en ligne

- [Git](https://github.com/HackaTAL/2018)
- [Liste de ressources](https://github.com/HackaTAL/2018/blob/master/ressources.md)
- [API chat noir](https://github.com/HackaTAL/2018/blob/master/chatnoir.md)

### Organisateurs

Arnaud Bichet (Storyzy)  
Kevin Deturck (Viseo / ERTIM)  
Nicolas Dugué (LIUM)  
Loïc Grobol (LaTTiCe)  
Gael Guibon (LIS, Caléa)  
Charles Huyghues-Despointes (Bertin)  
Antoine Laurent (LIUM)  
Damien Nouvel (ERTIM)  
Benjamin Piwowarski (LIP6)  
Ramon Ruti (Storyzy)  
Christophe Servan (Qwant)  
Raphaël Troncy (Eurecom)  
Julien Velcin (ERIC)  
