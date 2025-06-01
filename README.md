# SIGMAS

## Membres du groupe

- Zeynab ABRO
- Théo ARTIGALA
- Clémentine BERAUD
- Gaspard DESCAMPS
- Emilie NGUYEN

## Description du projet

Un jeu en deux dimensions réalisé en Python avec Pygame dont le but est de lancer une balle à travers un anneau.

Langage : Python 
Bibliothèque : Pygame
Outils : PyCharm, GitHub

## Installation et prérequis
- Installer PyCharm Community Edition sur https://www.jetbrains.com/fr-fr/pycharm/download/
- Installer GIT sur https://git-scm.com/downloads
- Avoir un compte sur la platerforme GitHub ou GitLab (https://github.com/)
- Installer Python sur https://www.python.org/downloads/
  
1. Connectez-vous à votre compte GitHub
2. Créez un nouveau dépôt en cliquant sur le bouton "New Repository"
3. Renseignez un nouveau nom pour le repository
4. Cliquez sur Create repository
5. Copier l'URL du dépôt distant (ex : https://github.com/votre-utilisateur/nom-du-depot.git)
6. Ouvrez PyCharm
7. Depuis l'accueil, cliquez sur "Get from Version Control" ou allez dans File -> Project from Version Control -> Git
8. Dans le champ URL, collez l'URL de votre repository GitHub que vous avez copiée
9. Sélectionnez un dossier local où cloner votre projet et cliquez sur "Clone"
10. Le projet sera importé dans PyCharm, vous permettant ainsi de le modifier et de le synchroniser avec GitHub

## Fonctionnalités 

- Menu
- Trois niveaux
- Contrôle de la trajectoire de la balle (direction et force)
- Détection de collision avec l'anneau

## Contraintes

- Développement en Python
- Implémentation d'un calcul de trajectoire physique
- Utilisation de variables
- Présence de rétroactions visuelles pour le joueur
- Affichage graphique

## Documentation technique
- 10 fichiers .py
- 8 images .png
- 1 son .wav

*Fichiers .py :*
- main.py : programme principal qui lance le menu
- menu.py : fonction qui gère l'interface de démarrage
- jeu.py : fonctions qui permet de lancer le jeu
- niveau.py : classe implémentant le design des niveaux (obstacles)
- settings.py : initialisation des paramètres du jeu
- equation_horaire.py : fonction de calcul de la trajectoire de la balle
- hoop.py : classe implémentant les collisions et l'affichage de l'anneau et des murs
- fleches.py : fonction qui implémente la flèche directionnel
- ball.py : classe implémentant la balle (collisions, rebonds, ...)
- end_screen.py : fonction de fin de jeu

Ce tableau montre quels fichiers sont utilisés dans chaque fichier du jeu :

| ball.py      | end_screen.py   | hoop.py     | jeu.py         | main.py  | menu.py     | niveau.py   |
|--------------|-----------------|-------------|----------------|----------|-------------|-------------|
| settings.py  | settings.py     | settings.py | settings.py    | menu.py  | settings.py | settings.py |
|              | jeu.py          |             | flèches.py     |          | jeu.py      | hoop.py     |
|              | menu.py         |             | end_screen.py  |          | niveau.py   |             |
|              |                 |             | ball.py        |          |             |             |
|              |                 |             | niveau.py      |          |             |             |
|              |                 |             | hoop.py        |          |             |             |
  
  
