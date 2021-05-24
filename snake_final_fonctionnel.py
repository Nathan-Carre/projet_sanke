import tkinter as tk
import random
import os
################CONSTANTE################################################################

WIDTH = 800
HEIGHT = 600
taille_case = 40
dirX = -1
dirY = 0
pseudo = ""
score = 0
currentNiveau = ""
fonte = ("Kristen ITC","20")
fonteListe = ("Kristen ITC","12")
couleurFond = "darkgrey"
couleurBoutonSelect = "green"
couleurBoutonDefaut = "SystemButtonFace"
delaiLent = 200
delaiMoyen = 150
delaiRapide = 100

###########VARIABLES DE JEU########################################################################

pommes = []
murs = []
idSerpent = []
delai = delaiMoyen

###########FONCTIONS DE JEU###########################################################################       

def decors(nomFichier):
    """Génération du décor correspondant au niveau pré-sélectionné dans le menu principal"""
    global murs, pomme, serpent, idSerpent, dirX, dirY
    # On réinitialise les variables de jeu : 
    serpent = []
    murs = []
    pommes = []
    idSerpent = []
    dirX = -1
    dirY = 0
    x, y = 0, 0
    # On crée le nouveau décor
    niveau = open(nomFichier)
    for ligne in niveau:
        for i in range(len(ligne)):
            case = ligne[i]
            if case == "X":
                temp = env_jeu.create_rectangle(x, y, x+40, y+40, fill='black')
                murs.append(temp)
            elif case == "P":
                pomme = env_jeu.create_oval(x, y, x+40, y+40, fill='red')
            elif case == "T":
                idSerpent.append(env_jeu.create_rectangle(x, y, x+40, y+40, fill='green'))
            elif case == "Q":
                idSerpent.append(env_jeu.create_rectangle(x, y, x+40, y+40, fill='green'))
            x += 40
        x = 0
        y += 40
    serpent = [env_jeu.coords(idSerpent[0]), env_jeu.coords(idSerpent[-1])]
    niveau.close()


def deplacement_serpent_auto():
    """Déplace de manière continue le serpent sur le canevas"""
    global murs, pomme, dirX, dirY, serpent, prochaines_coords, coords_murs, delai
    coords_murs = []
    prochaines_coords = [(serpent[0][0] + dirX * taille_case), (serpent[0][1] + dirY * taille_case), 
    (serpent[0][2] + dirX * taille_case), (serpent[0][3] + dirY * taille_case)] 
    for i in murs:
        coords_murs.append(env_jeu.coords(i))
    serpent.insert(0, prochaines_coords) 
    serpent.remove(serpent[-1])
    for i in range(len(serpent)):
        env_jeu.coords(idSerpent[i], serpent[i])
    if serpent[0] == env_jeu.coords(pomme):
        manger_pomme()
    if percuter():
        perduhahatnul()
    else:
        snake.after(delai, deplacement_serpent_auto)


def deplacement_serpent_up():
    """Modifie la direction du serpent vers le haut sur le canevas"""
    global dirX, dirY
    if dirX != 0 and dirY != 1:
        dirX, dirY = 0, -1 


def deplacement_serpent_down():
    """Modifie la direction du serpent vers la bas sur le canevas"""
    global dirX, dirY
    if dirX != 0 and dirY != -1:
        dirX, dirY = 0, 1


def deplacement_serpent_right():
    """Modifie la direction du serpent vers la droite sur le canevas"""
    global dirX, dirY
    if dirX != -1 and dirY != 0:
        dirX, dirY = 1, 0 


def deplacement_serpent_left():
    """Modifie la direction du serpent sur le canevas"""
    global dirX, dirY
    if dirX != 1 and dirY != 0:
        dirX, dirY = -1, 0


def manger_pomme():
    """Ajout d'une nouvelle pomme et des actions qui en découlent, selon les règles données dans les consignes"""
    global pomme, score, serpent, murs, prochaines_coords, dirX, dirY, idSerpent
    creer = False
    while not creer:
        p1 = 40 * random.randint(1,18)
        p2 = 40 * random.randint(1, 13)
        over = env_jeu.find_overlapping(p1, p2, p1 +40, p2 +40)
        if len(over) == 0:
            creer = True
    env_jeu.coords(pomme, p1, p2, p1 + taille_case, p2 + taille_case)
    serpent.append(serpent[-1])
    idSerpent.append(env_jeu.create_rectangle(serpent[-1], fill="green"))
    score += 1



def percuter():
    """Prend en compte la percussion de la tête avec un autre item du canvas, puis termine la partie ou non selon les règles données dans les consignes."""
    global serpent
    x_tete, y_tete, x1_tete, y1_tete = serpent[0]
    x_centre = (x_tete + x1_tete)//2 
    y_centre = (y_tete + y1_tete)//2
    for mur in murs :
        if mur in env_jeu.find_overlapping(x_centre, y_centre, x_centre, y_centre) : 
            return True
    for i in range(1, len(idSerpent)):
        if idSerpent[i] in env_jeu.find_overlapping(x_centre, y_centre, x_centre, y_centre)  :
            return True
    return False   


def quitter(): 
    snake.destroy()

def perduhahatnul():
    """Termine la partie et affiche un nouveau menu pour choisir si l'on veut: rejouer, revenir au menu ou bien sauvegarder son score."""
    save_score()
    switchPan(getPanPerdu())


def save_score():
    """Sauvegarde le score du joueur une fois la partie terminée sous /scores/pseudo_du_joueur."""
    global pseudo, score
    file_path = "./scores/" + pseudo + ".txt"
    old_scores = ""
    if os.path.exists(file_path):
        # récupérer le contenue du fichier score
        f = open(file_path, "r")
        old_scores = f.read()
        f.close()
    elif not os.path.exists("./scores"):
        # si le dossier score n'existe pas on le crée
        os.makedirs("./scores")
    # on ajoute le nouveau score en haut du fichier suivi par les anciens
    # classés du plus récent au plus ancien
    f = open(file_path, "w")
    f.write(str(score) + '\n' + old_scores)
    f.close()

###########FONCTIONS PANNEL###########################################################################      

def switchPan(pannel):
    global current_pan
    current_pan.destroy()
    current_pan = pannel
    current_pan.pack()


def getPanMenu():
    """Permet de construire le pannel menu et comprend toute les fontions de gestion des actions"""
    
    def importerNiveaux():
        """Permet d'importer les différents niveaux(en format ".txt") dans le menu"""
        listeFichier = os.listdir()
        niveaux = []
        for fichier in listeFichier:
            if fichier[0:6] == "niveau":
                niveaux.append(fichier)
        for n in niveaux:
            listeNiveaux.insert(tk.END,n)
        if len(niveaux):
            listeNiveaux.select_set(0)
        listeNiveaux.config(height=len(niveaux))
        return listeNiveaux


    def jouer():
        """Lance la partie dans une nouvelle fenêtre et suprimme la fenêtre "menu". """
        global pseudo, env_jeu, score, idSerpent, dirX, dirY, currentNiveau, murs
        # on recrée le canvas avec un nouveau pannel jeu
        newPanJeu = getPanJeu()
        env_jeu.destroy()
        env_jeu = tk.Canvas(newPanJeu, width=WIDTH, heigh=HEIGHT, bg=couleurFond)
        env_jeu.pack()
        pseudo = etryPseudo.get()
        currentNiveau = listeNiveaux.get(listeNiveaux.curselection())
        score = 0
        decors(currentNiveau)
        switchPan(newPanJeu)
        deplacement_serpent_auto()

        
    def scores():
        """Lance le tableau des scores"""
        global pseudo
        pseudo = etryPseudo.get()
        switchPan(getPanScore())


    def lent():
        """Pour de sélectionner dans le menu principale la vitesse (lente) du serpent et donc le niveau de difficulté"""
        global delai
        btLent.config(bg=couleurBoutonSelect)
        btMoyen.config(bg=couleurBoutonDefaut)
        btRapide.config(bg=couleurBoutonDefaut)
        delai = delaiLent


    def moyen():
        """Pour de sélectionner dans le menu principale la vitesse (moyenne) du serpent et donc le niveau de difficulté"""
        global delai
        btLent.config(bg=couleurBoutonDefaut)
        btMoyen.config(bg=couleurBoutonSelect)
        btRapide.config(bg=couleurBoutonDefaut)
        delai = delaiMoyen


    def rapide():
        """Pour de sélectionner dans le menu principale la vitesse (rapide) du serpent et donc le niveau de difficulté"""
        global delai
        btLent.config(bg=couleurBoutonDefaut)
        btMoyen.config(bg=couleurBoutonDefaut)
        btRapide.config(bg=couleurBoutonSelect)
        delai = delaiRapide
    global pseudo
    panMenu = tk.Frame(snake,bg=couleurFond)
    # Center la grille avec plusieurs colonnes
    panMenu.grid_columnconfigure((0,1,2), weight=1)
    labelPseudo = tk.Label(panMenu,text="Pseudo",font=fonte,bg=couleurFond)
    etryPseudo = tk.Entry(panMenu, width=15, font=fonte)
    etryPseudo.insert(tk.END,pseudo)
    labelVitesse = tk.Label(panMenu,text="Vitesse",font=fonte,bg=couleurFond)
    btLent = tk.Button(panMenu,text="Lent",font=fonte,bg=couleurBoutonDefaut, command=lent)
    btMoyen = tk.Button(panMenu,text="Moyen",font=fonte,bg=couleurBoutonDefaut, command=moyen)
    btRapide = tk.Button(panMenu,text="Rapide",font=fonte,bg=couleurBoutonDefaut, command=rapide)
    if(delai == delaiLent):
        btLent.config(bg=couleurBoutonSelect)
    elif(delai == delaiMoyen):
        btMoyen.config(bg=couleurBoutonSelect)
    else :
        btRapide.config(bg=couleurBoutonSelect)
    btJouer = tk.Button(panMenu,text="Jouer",font=fonte,command=jouer)
    btScore = tk.Button(panMenu,text="Tableau des scores",font=fonte,command=scores)
    panListe = tk.Frame(panMenu)
    labelNiveau = tk.Label(panMenu,text="Niveau",font=fonte,bg=couleurFond)
    barreDefilement = tk.Scrollbar(panListe)
    listeNiveaux = tk.Listbox(panListe,font=fonte,selectbackground=couleurBoutonSelect,yscrollcommand=barreDefilement.set)
    listeNiveaux.pack(side=tk.LEFT, fill=tk.BOTH)
    barreDefilement.pack(side=tk.RIGHT, fill=tk.BOTH)
    barreDefilement.config(command = listeNiveaux.yview)
    labelPseudo.grid(row=0,columnspan=3)
    etryPseudo.grid(row=1,columnspan=3)
    labelVitesse.grid(row=2,columnspan=3)
    btLent.grid(row=3,column=0)
    btMoyen.grid(row=3,column=1)
    btRapide.grid(row=3,column=2)
    labelNiveau.grid(row=4,columnspan=3)
    panListe.grid(row=5,columnspan=3)
    btJouer.grid(row=6,columnspan=3)
    btScore.grid(row=7,columnspan=3)
    importerNiveaux()
    return panMenu


def getPanScore():
    def importerScore(pseudo):
        """Permet d'importer les scores du joeur(en format ".txt") dans le tableau des scores"""
        file_path = "./scores/" + pseudo + ".txt"
        scores = []
        if os.path.exists(file_path):
            # récupérer le contenue du fichier score
            f = open(file_path, "r")
            scores = f.read().split('\n')[:10]
            f.close()
        for score in scores:
            listeScores.insert(tk.END,str(score) + " pts")
        if len(scores):
            listeScores.select_set(0)
        listeScores.config(height=10)
        return listeScores
    global pseudo
    panScore = tk.Frame(snake, bg=couleurFond)
    panScore.columnconfigure(0, weight=1)
    panListeScore = tk.Frame(panScore)
    labelScore = tk.Label(panScore,text=pseudo + " Votre tableau des scores",font=fonte)
    barreDefilementScore = tk.Scrollbar(panListeScore)
    listeScores = tk.Listbox(panListeScore,font=fonte,selectbackground=couleurBoutonSelect,yscrollcommand=barreDefilementScore.set)
    listeScores.pack(side=tk.LEFT, fill=tk.BOTH)
    barreDefilementScore.pack(side=tk.RIGHT, fill=tk.BOTH)
    barreDefilementScore.config(command = listeScores.yview)
    btMenu = tk.Button(panScore,text="Retour au Menu",font=fonte,command=lambda: switchPan(getPanMenu()))
    labelScore.grid(row=0,columnspan=3)   
    panListeScore.grid(row=1,columnspan=3)
    btMenu.grid(row=2,columnspan=3)
    importerScore(pseudo) 
    return panScore


def getPanPerdu():
    def rejouer():
        """Relance la partie dans une nouvelle fenêtre et suprimme la fenêtre "perdu". """
        global pseudo, env_jeu, score, currentNiveau
        # on recrée le canvas avec un nouveau pannel jeu
        newPanJeu = getPanJeu()
        env_jeu.destroy()
        env_jeu = tk.Canvas(newPanJeu, width=WIDTH, heigh=HEIGHT, bg=couleurFond)
        env_jeu.pack()
        # on remet les variables à leurs valeurs initiale
        score = 0
        decors(currentNiveau)
        deplacement_serpent_auto()
        switchPan(newPanJeu)

    panPerdu = tk.Frame(snake, bg="black")
    # Center la grille avec une seul colonne
    panPerdu.columnconfigure(0, weight=1)
    # Centrer la grille en laissant la line 0 et la ligne 5 prendre tout l'epace restant 
    panPerdu.grid_rowconfigure((0,5), weight=1)
    labelPerdu = tk.Label(panPerdu,text="PERDU",font=('system', '45'), fg="red", bg="black")
    labelScore = tk.Label(panPerdu,text="Votre score : "+str(score),font=('Lucida Console', '15'), fg="white", bg="black")
    replay=tk.Button(panPerdu, text="Rejouer", fg="white", bg="black", relief="raised", font=("Lucida Console","20"),command=rejouer )
    backto=tk.Button(panPerdu, text="Revenir au menu", fg="white", bg="black", relief="raised", font=("Lucida Console","20"), command=lambda: switchPan(getPanMenu()) )
    labelPerdu.grid(row=1, columnspan=1)   
    labelScore.grid(row=2, pady=10, columnspan=1)
    replay.grid(row=3,pady=4, columnspan=1)   
    backto.grid(row=4,pady=4, columnspan=1)
    panPerdu.pack(fill=tk.BOTH, expand=1)
    return panPerdu
    

def getPanJeu():
    panJeu = tk.Frame(snake)
    return panJeu

################################################################################################################ 

snake = tk.Tk()
snake.configure(bg=couleurFond)
snake.title("Snake")
snake.geometry(str(WIDTH)+"x"+str(HEIGHT))
panMenu = getPanMenu()
current_pan = panMenu
current_pan.pack()

# Canvas contenant le jeu dans un premier temps vide il sera rempli quand le jeu sera initialisé
env_jeu = tk.Canvas()


############PROGRAMME#######################################################################################

snake.bind('<Up>', lambda e:deplacement_serpent_up())
snake.bind('<Down>', lambda e:deplacement_serpent_down())
snake.bind('<Right>', lambda e:deplacement_serpent_right())
snake.bind('<Left>', lambda e:deplacement_serpent_left())

snake.mainloop()