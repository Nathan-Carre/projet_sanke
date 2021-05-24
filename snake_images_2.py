import tkinter as tk
import random as rd
import os.path

def choix_frame(frame):
    frame.tkraise()

def decors(title):
    global serpent, obstacles, pommes, directions
    choix_frame(frame_canvas)
    snake.geometry('800x600')
    x, y = 0, 0
    niveau = open(title)
    for ligne in niveau:
        for i in range(20):
            case = ligne[i]
            if case == "X":
                mur = env_jeu.create_image(x, y, image=parois, anchor="nw")
                obstacles.append(mur)
            elif case == "P":
                pomme = env_jeu.create_image(x, y, image=pomme1, anchor="nw")
                pommes.append(pomme)
            elif case == "T":
                tete = env_jeu.create_image(x, y, image=tete_gauche, anchor="nw")
                serpent.append(tete)
                directions.append('gauche')
            elif case == "Q":
                queue = env_jeu.create_image(x, y, image=queue_gauche, anchor="nw")
                serpent.append(queue)
                directions.append('gauche')
            x += 40
        x = 0
        y += 40
    niveau.close()

def bienvenue():
    global pseudo
    pseudo.set('bienvenue '+saisir_nom.get() + ' !')
    afficher_score()

def gauche(event):
    global x, y, direction
    x = -40
    y = 0
    direction = 'gauche'

def droit(event):
    global x, y, direction
    x = 40
    y = 0
    direction = 'droit'

def haut(event):
    global x, y, direction
    x = 0
    y = -40
    direction = 'haut'

def bas(event):
    global x, y, direction
    x = 0 
    y = 40
    direction = 'bas'

def vite(mesure, bouton):
    global vitess
    bouton_nom = ['lent', 'moyen', 'rapide']
    boutons = [lent, moyen, rapide]
    vitess = mesure
    num = bouton_nom.index(bouton)
    boutons[num].configure(bg='pink')
    for i in range(3):
        if i != num:
            boutons[i].configure(bg='light gray')

def mouvement():
    global serpent, x, y, obstacles, pommes, scores, directions, direction, jeu, vitess
    nouv_tete_serpent()
    if game_over() == True:
        t1, t2 = env_jeu.coords(serpent[0])
        p1, p2 = env_jeu.coords(pommes[0])
        if (t1 == p1 and t2 == p2):
            scores += 1
            manger_pomme()
        if len(pommes) == 1 : 
            effacer = serpent.pop()
            directions.pop()
            env_jeu.delete(effacer)
            c1, c2 = env_jeu.coords(serpent[len(serpent)-1])
            changer = serpent.pop()
            d = directions[len(serpent)-1]
            env_jeu.delete(changer)
            if d == 'gauche':
                nouveau = env_jeu.create_image(c1, c2, image=queue_gauche, anchor="nw")
                serpent.append(nouveau)
            elif d == 'droit':
                nouveau = env_jeu.create_image(c1, c2, image=queue_droit, anchor="nw")
                serpent.append(nouveau)
            elif d == 'haut':
                nouveau = env_jeu.create_image(c1, c2, image=queue_haut, anchor="nw")
                serpent.append(nouveau)
            elif d == 'bas':
                nouveau = env_jeu.create_image(c1, c2, image=queue_bas, anchor="nw")
                serpent.append(nouveau)
        else : 
            env_jeu.delete(pommes[1])
            pommes.pop()
        jeu = env_jeu.after(vitess, mouvement)


def afficher_score():
    texte1.delete('1.0', tk.END)
    fichier = 0
    if os.path.isfile('scores/'+saisir_nom.get()+'.txt'):
        fichier = open('scores/'+saisir_nom.get()+'.txt', 'w')
        fichier.close()
    else:
        pass


def ajouter_score():
    global scores
    fichier = 0
    if os.path.isfile('scores/'+saisir_nom.get()+'.txt'):
        fichier = open('scores/'+saisir_nom.get()+'.txt', 'a')
        fichier.write(str(scores))
        fichier.close()
    else:
        fichier = open('scores/'+saisir_nom.get()+'.txt', 'w')
        fichier.write(str(scores))
        fichier.close()
    afficher_score()


def jouer(title):
    global env_jeu, pommes, obstacles, directions, serpent, x, y, direction, scores
    pommes.clear()
    obstacles.clear()
    serpent.clear()
    directions.clear()
    direction = 'gauche'
    x, y = -40, 0
    scores = 0
    env_jeu = tk.Canvas(frame_canvas, width=800, heigh=600, bg="darkgray")
    env_jeu.place(x=0, y=0)
    decors(title)
    mouvement()


def game_over():
    global serpent, obstacles, x, y, pommes, jeu, env_jeu, ajour, scores, direction, directions
    t1, t2 = env_jeu.coords(serpent[0])
    over = env_jeu.find_overlapping(t1, t2, t1 +40, t2 +40)
    if (direction == 'haut' and directions[1] == 'bas') or (direction == 'bas' and directions[1] == 'haut') or (direction == 'gauche' and directions[1] == 'droit') or (direction == 'droit' and directions[1] == 'gauche'):
        env_jeu.after_cancel(jeu)
        jeu = None
        env_jeu.destroy()
        env_jeu = None
        choix_frame(frame_over)
        snake.geometry('300x300')
        ajour.set('score : ' +str(scores))
        return False
    elif len(over) > 0 : 
        for elem in over:
            if elem in pommes:
                pass
            elif elem in serpent[1::] or elem in obstacles :
                env_jeu.after_cancel(jeu)
                jeu = None
                env_jeu.destroy()
                env_jeu = None
                choix_frame(frame_over)
                snake.geometry('300x300')
                ajour.set('score : ' +str(scores))
                ajouter_score()
                scores = 0
                return False
    return True


def manger_pomme():
    global serpent, pommes, obstacles
    creer = False
    env_jeu.delete(pommes[0])
    while not creer:
        p1 = 40 * rd.randint(1,18)
        p2 = 40 * rd.randint(1, 13)
        over = env_jeu.find_overlapping(p1, p2, p1 +40, p2 +40)
        if len(over) == 0:
            creer = True
    po = env_jeu.create_image(p1, p2, image=pomme1, anchor="nw") # multiple de 40 attention
    pommes.insert(0, po)
    

def nouv_tete_serpent():
    """ serpent en dessin """
    global directions, direction, serpent, x, y 
    t1, t2 = env_jeu.coords(serpent[0])
    if direction == 'bas' and (directions[0] == 'gauche' or directions[0] == 'droit'):
        tete = env_jeu.create_image(t1+x, t2+y, image=tete_bas, anchor="nw")
        serpent.insert(0, tete)
    elif direction == 'haut' and (directions[0] == 'gauche' or directions[0] == 'droit'):
        tete = env_jeu.create_image(t1+x, t2+y, image=tete_haut, anchor="nw")
        serpent.insert(0, tete)
    elif direction == 'droit' and (directions[0] == 'haut' or directions[0] == 'bas'):
        tete = env_jeu.create_image(t1+x, t2+y, image=tete_droit, anchor="nw")
        serpent.insert(0, tete)
    elif direction == 'gauche' and (directions[0] == 'haut' or directions[0] == 'bas'):
        tete = env_jeu.create_image(t1+x, t2+y, image=tete_gauche, anchor="nw")
        serpent.insert(0, tete)
    elif directions[0] == 'gauche' and direction == 'gauche':
        tete = env_jeu.create_image(t1+x, t2+y, image=tete_gauche, anchor="nw")
        serpent.insert(0, tete)
    elif directions[0] == 'droit' and direction == 'droit':
        tete = env_jeu.create_image(t1+x, t2+y, image=tete_droit, anchor="nw")
        serpent.insert(0, tete)
    elif directions[0] == 'bas' and direction == 'bas':
        tete = env_jeu.create_image(t1+x, t2+y, image=tete_bas, anchor="nw")
        serpent.insert(0, tete)
    elif directions[0] == 'haut' and direction == 'haut':
        tete = env_jeu.create_image(t1+x, t2+y, image=tete_haut, anchor="nw")
        serpent.insert(0, tete)
    directions.insert(0, direction)
    if len(serpent) >= 3:
        env_jeu.delete(serpent[1])
        del(serpent[1])
        if (directions[1] == 'gauche' and directions[0] == 'gauche') or (directions[1] == 'droit' and directions[0] == 'droit'):
            corps = env_jeu.create_image(t1, t2, image=corps_droit, anchor="nw")
            serpent.insert(1, corps)
        elif (directions[1] == 'haut' and directions[0] == 'haut') or (directions[1] == 'bas' and directions[0] == 'bas'):
            corps = env_jeu.create_image(t1, t2, image=corps_bas, anchor="nw")
            serpent.insert(1, corps)
        elif (directions[1] == 'gauche' and directions[0] == 'haut') or (directions[1] == 'bas' and directions[0] == 'droit'):
            corps = env_jeu.create_image(t1, t2, image=tournant_droit_haut, anchor="nw")
            serpent.insert(1, corps)
        elif (directions[1] == 'gauche' and directions[0] == 'bas') or (directions[1] == 'haut' and directions[0] == 'droit'):
            corps = env_jeu.create_image(t1, t2, image=tournant_droit_bas, anchor="nw")
            serpent.insert(1, corps)
        elif (directions[1] == 'droit' and directions[0] == 'bas') or (directions[1] == 'haut' and directions[0] == 'gauche'):
            corps = env_jeu.create_image(t1, t2, image=tournant_gauche_bas, anchor="nw")
            serpent.insert(1, corps)
        elif (directions[1] == 'droit' and directions[0] == 'haut') or (directions[1] == 'bas' and directions[0] == 'gauche'):
            corps = env_jeu.create_image(t1, t2, image=tournant_gauche_haut, anchor="nw")
            serpent.insert(1, corps)
    

snake = tk.Tk()
snake.title("JEU SNAKE")
snake.geometry('300x300')

snake.rowconfigure(0, weight=1)
snake.columnconfigure(0, weight=1)

frame_menu = tk.Frame(snake)
frame_niveaux = tk.Frame(snake)
frame_score = tk.Frame(snake)
frame_canvas = tk.Frame(snake)
frame_vitesse = tk.Frame(snake)
frame_over = tk.Frame(snake)
for frame in (frame_menu, frame_niveaux, frame_score, frame_canvas, frame_vitesse, frame_over):
    frame.grid(row=0, column=0, sticky="nsew")

choix_frame(frame_menu)
pseudo = tk.StringVar()
pseudo.set('')
ajour = tk.StringVar()
ajour.set('')
serpent =[]
directions = []
direction = 'gauche'
obstacles = []
pommes = []
scores = 0 
x, y = -40, 0
jeu = None
env_jeu = None
vitess = 200

parois = tk.PhotoImage(file='images/muraille.gif')
pomme1 = tk.PhotoImage(file='images/pomme.gif')
tete_gauche = tk.PhotoImage(file='images/tete_gauche.gif')
tete_droit = tk.PhotoImage(file='images/tete_droit.gif')
tete_haut = tk.PhotoImage(file='images/tete_haut.gif')
tete_bas = tk.PhotoImage(file='images/tete_bas.gif')
corps_droit = tk.PhotoImage(file='images/corps_droit.gif')
corps_gauche = tk.PhotoImage(file='images/corps_gauche.gif')
corps_haut = tk.PhotoImage(file='images/corps_haut.gif')
corps_bas = tk.PhotoImage(file='images/corps_bas.gif')
queue_gauche = tk.PhotoImage(file='images/queue_gauche.gif')
queue_droit = tk.PhotoImage(file='images/queue_droit.gif')
queue_haut = tk.PhotoImage(file='images/queue_haut.gif')
queue_bas = tk.PhotoImage(file='images/queue_bas.gif')
tournant_droit_bas = tk.PhotoImage(file='images/tournant_bas_droit.gif')
tournant_gauche_bas = tk.PhotoImage(file='images/tournant_bas_gauche.gif')
tournant_droit_haut = tk.PhotoImage(file='images/tournant_droit_haut.gif') 
tournant_gauche_haut = tk.PhotoImage(file='images/tournant_gauche_haut.gif')

############# menu ############
titre_menu = tk.Label(frame_menu, text='SNAKE', fg='green', font="Helvetica 26 bold italic")
titre_menu.place(x=80, y=20)
niveaux = tk.Button(frame_menu, text='Niveaux', bg='light gray', fg='green', font="Helvetica 16 bold italic", command=lambda:choix_frame(frame_niveaux))
niveaux.place(x=100, y=150)
score = tk.Button(frame_menu, text='Scores', bg='light gray', fg='green', font="Helvetica 16 bold italic", width=7, command=lambda:choix_frame(frame_score))
score.place(x=100, y=200)
vitesse = tk.Button(frame_menu, text='Vitesses', bg='light gray', fg='green', font="Helvetica 16 bold italic", width=7, command=lambda:choix_frame(frame_vitesse))
vitesse.place(x=100, y=250)
nom = tk.Label(frame_menu, text='entrer un pseudo :', fg='green', font="Helvetica 14 bold italic")
nom.place(x=60, y= 70)
saisir_nom = tk.Entry(frame_menu, width=35)
saisir_nom.place(x=25, y=100)
ok = tk.Button(frame_menu, text='OK', bg='light gray', fg='green', font="Helvetica 10 bold italic", width=2, command=bienvenue)
ok.place(x=250, y=95)
hello = tk.Label(frame_menu, textvariable=pseudo, fg='green', font="Helvetica 10 bold italic")
hello.place(x=80, y=120)

######## niveaux ######
titre_niveaux = tk.Label(frame_niveaux, text='NIVEAUX', fg='green', font="Helvetica 18 bold italic")
titre_niveaux.place(x=100, y= 10)
niveau1 = tk.Button(frame_niveaux, text='niveau 1', bg='light gray', fg='green', font="Helvetica 14 bold italic", command=lambda:jouer('niveaux/niveau_1.txt'))
niveau1.place(x=100, y=75)
niveau1 = tk.Button(frame_niveaux, text='niveau 2', bg='light gray', fg='green', font="Helvetica 14 bold italic", command=lambda:jouer('niveaux/niveau_2.txt'))
niveau1.place(x=100, y=125)
menu1 = tk.Button(frame_niveaux, text='menu', bg='light gray', fg='green', font="Helvetica 16 bold italic", width=7, command=lambda:choix_frame(frame_menu))
menu1.place(x=10, y=250)

######## score ##########
titre_score = tk.Label(frame_score, text='SCORES', fg='green', font="Helvetica 18 bold italic")
titre_score.place(x=100, y= 10)
texte1 = tk.Text(frame_score, width=25, height=10)
texte1.place(x=50, y=60)
menu2 = tk.Button(frame_score, text='menu', bg='light gray', fg='green', font="Helvetica 14 bold italic", width=7, command=lambda:choix_frame(frame_menu))
menu2.place(x=10, y=250)

#######vitesse#########
titre_vitesse = tk.Label(frame_vitesse, text='VITESSES', fg='green', font="Helvetica 18 bold italic")
titre_vitesse.place(x=100, y= 10)
menu3 = tk.Button(frame_vitesse, text='menu', bg='light gray', fg='green', font="Helvetica 16 bold italic", width=7, command=lambda:choix_frame(frame_menu))
menu3.place(x=10, y=250)
lent = tk.Button(frame_vitesse, text='lent', bg='light gray', fg='green', font="Helvetica 16 bold italic", width=7, command=lambda:vite(500, 'lent'))
lent.place(x=100, y=75)
moyen = tk.Button(frame_vitesse, text='moyen', bg='pink', fg='green', font="Helvetica 16 bold italic", width=7, command=lambda:vite(200, 'moyen'))
moyen.place(x=100, y=125)
rapide = tk.Button(frame_vitesse, text='rapide', bg='light gray', fg='green', font="Helvetica 16 bold italic", width=7, command=lambda:vite(100, 'rapide'))
rapide.place(x=100, y=175)

########game over################
frame_over.configure(bg='black')
titre_over = tk.Label(frame_over, text='GAME OVER', fg='red', bg='black', font="Helvetica 25 bold italic")
titre_over.place(x=50, y=100)
label_score = tk.Label(frame_over, textvariable=ajour, fg='red', bg='black', font="Helvetica 16 bold italic", width=8)
label_score.place(x=100, y=175)
menu4 = tk.Button(frame_over, text='menu', bg='black', fg='red', font="Helvetica 16 bold italic", width=7, command=lambda:choix_frame(frame_menu))
menu4.place(x=100, y=225)

snake.bind("<KeyPress-Left>", gauche)
snake.bind("<KeyPress-Right>", droit)
snake.bind("<KeyPress-Up>", haut)
snake.bind("<KeyPress-Down>", bas)

snake.mainloop()