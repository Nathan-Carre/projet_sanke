# Projet n°2 du second semestre en IN200 : Le projet Snake

### Contexte:
Le but de ce projet est de créer un programme fonctionnel pour simuler le jeu "Snake": Un serpent qui se déplace sur un terrain de jeu prédéfini à l'avance. Le serpent doit manger des pommes, apparaissant de manière aléatoire sur le terrain, pour pouvoir gagner un point et ainsi agrandir son corps de un.

### Règles du jeu:
- Manger la pomme : lorsqu’elle est mangée, une autre pomme apparaît sur un case aléatoire du terrain, et la longueur du serpent augmente de 1.

- Le joueur est invité à entrer un pseudo dans le menu principal avant de lancer une partie. Le score du joueur est égal au nombre de pommes que le serpent a mangées sur le terrain. Le score de chaque parties est stocké dans un fichier txt, et le pseudo du joueur est indiqué à côté du nouveau score dans ce fichier.

- La partie s’arrête lorsque la tête du serpent percute un mur ou percute son propre corps.


## I°) Menu Principal:

A compléter


## II°) Fenêtre de jeu:
Dès lors que le joueur a appuyé sur le bouton Jouer dans le menu principal, une nouvelle fenêtre Tkinter contenant un canvas s'ouvre pour que le joueur puisse commencer à jouer. Le serpent commence automatiquement à se déplacer dès que la fenêtre de jeu Tkinter c'est ouverte. Il se déplace d'une manière plus au moins rapide en fonction de la vitesse choisie par le joueur dans le menu principal. 

- Tout d'abord, le serpent commence avec une longueur de deux cases, la tête et la queue, quelque soit le "niveau" choisi au préalable.
- Pour se déplacer, afin d'éviter les murs et manger la pomme sur le terrain, le joueur doit utiliser les flèches du clavier. Les flèches du haut, du bas, de gauche et de droite déplacent le serpent respectivement en haut, en bas, à gauche et à droite. 
- Si la tête du serpent venait à percuter son propre corps ou un des murs du terrain, la partie est terminée et le joueur a perdu.

## III°) Menu de fin:
A compléter
