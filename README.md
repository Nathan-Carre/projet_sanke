# Projet n°2 du second semestre en IN200 : Le projet Snake

### Contexte:
Le but de ce projet est de créer un programme fonctionnel pour simuler le jeu "Snake": Un serpent qui se déplace sur un terrain de jeu prédéfini à l'avance. Le serpent doit manger des pommes, apparaissant de manière aléatoire sur le terrain, pour pouvoir gagner un point et ainsi agrandir son corps de un.

### Règles du jeu:
- Manger la pomme : lorsqu’elle est mangée, une autre pomme apparaît sur un case aléatoire du terrain, et la longueur du serpent augmente de 1.

- Le joueur est invité à entrer un pseudo dans le menu principal avant de lancer une partie. Le score du joueur est égal au nombre de pommes que le serpent a mangées sur le terrain. Le score de chaque parties est stocké dans un fichier txt, et le pseudo du joueur est indiqué à côté du nouveau score dans ce fichier.

- La partie s’arrête lorsque la tête du serpent percute un mur ou percute son propre corps.

### Mode d'emploi :
Apres avoir lancé le programme ("snake_final_fonctionnel.py") l'utilisateur doit 

     - Entrer son pseudo.
  
     - Choisir la vitesse de déplacement du serpent.
  
     - Choisir le niveau de jeu. L'utilisateur a ici le choix entre 5 niveaux de jeu, de plus en plus difficiles. 
  
     - Pour lancer la partie , l'utilisateur clique sur le bouton "jouer" et le jeu commence .
  
     - Le déplacement du serpent est contrôlé par l'utilisateur grâce aux quartes boutons Haut, Bas, Gauche et Droit de son clavier.
  
Lorsque le serpent percute un mur ou son propre corps, c'est la fin de la partie . L'utilisateur a le choix entre 

     - Rejouer la partie ( cliquer sur le bouton "rejouer" )
  
     - Revenir au menu principal (cliquer sur le bouton "revenir au menu" )
  
     - Quitter définitivement le jeu ( fermer la fenêtre tkinter )
  
     - L'utilisateur a aussi la possibilité de consulter ses 10 derniers scores dans le menu principal (cliquer sur le bouton "Tableau des scores" ).


## I°) Menu Principal:

A compléter

## II°) Tableau des scores:
À chaque fin de partie le score du joueur est sauvegardé à l'aide du système de sauvegarde. Afin de pouvoir avoir un aperçu de l'évolution de ses performances, le joueur a accès à un tableau des scores. Ce tableau lui donnera accès au score des 10 dernières parties classées du plus récent au plus ancien.

![alt texte](https://github.com/Nathan-Carre/projet_snake/blob/main/ressources%20readme/Tableau_scores.JPG)

Ce panel est accessible à partir du menu principal, une fois le pseudo du joueur saisi. Grâce à ce pseudo, les 10 derniers scores seront récupérés à partir du fichier portant le nom du joueur. Ce fichier contenant les scores du joueur, et est stocké sous le répertoire scores.

![alt texte](https://github.com/Nathan-Carre/projet_snake/blob/main/ressources%20readme/dossier_scores.JPG)

## III°) Fenêtre de jeu:
Dès lors que le joueur a appuyé sur le bouton Jouer dans le menu principal, une nouvelle fenêtre Tkinter contenant un canvas s'ouvre pour que le joueur puisse commencer à jouer. Le serpent commence automatiquement à se déplacer dès que la fenêtre de jeu Tkinter s'est ouverte. Il se déplace d'une manière plus au moins rapide en fonction de la vitesse choisie par le joueur dans le menu principal. 

- Tout d'abord, le serpent commence avec une longueur de deux cases, la tête et la queue, quelque soit le "niveau" choisi au préalable.
- Pour se déplacer, afin d'éviter les murs et manger la pomme (représentée par un cercle rouge ) sur le terrain, le joueur doit utiliser les flèches du clavier. Les flèches du haut, du bas, de gauche et de droite déplacent le serpent (représenté par une suite de rectangle vert) respectivement en haut, en bas, à gauche et à droite. 
- Si la tête du serpent venait à percuter son propre corps ou un des murs du terrain, la partie est terminée et le joueur a perdu.

## IV°) Menu de fin:
Lorsque vous avez perdu, vous accédez à un menu de fin, où vous pourrez visualiser le score effectué lors de votre partie. Vous aurez également 2 boutons vous permettant soit de rejouer, de revenir au menu, tout cela fonctionnel grâce au système de navigation.

## V°) Système de navigation :
Dans le but de simplifier la navigation entre les différents panels de notre jeu : 
- Menu
- Tableau des scores
- Jeu
- Fin de jeu

Nous avons voulu mettre en place un système de navigation, permettant de passer d'un panel à l'autre. Dans cette optique nous avons créé des fonctions permettant de générer chacun des panels, afin de les rendre réutilisables : 
- getPanMenu
- getPanScore
- getPanJeu
- getPanPerdu

Ses fonctions vont contenir tout le nécessaire au bon fonctionnement de chaque panel: 
- fonction intermediaire (commande utilisée par les boutons)
- variable local ...

Une fois les fonctions mise en place, nous avons décidé de mettre en place une petite fonction (switchPan) nous permettant de passer d'un panel à l'autre. Pour cela elle détruit le panel actuel (current pan / variable global) et le remplace par le panel cible passé en paramètre avant de l'activer.

![alt texte](https://github.com/Nathan-Carre/projet_snake/blob/main/ressources%20readme/switchpan.JPG)

## VI°) Système de sauvegarde :
Afin de pouvoir historiser les scores du joueur, et lui permettre de visualiser l'évolution de ses performances, nous avons mis en place un système de sauvegarde. Un système assez simple permettant de sauvegarder le score du joueur à chaque fin de partie. Le score, sera écrit dans un fichier portant le nom du joueur dans le répertoire "scores". Dans le cas ou le fichier existerait le score sera ajouté en haut du fichier afin de garder les scores classés du plus récent au plus ancien.

![alt texte](https://github.com/Nathan-Carre/projet_snake/blob/main/ressources%20readme/fichier_score.JPG)

