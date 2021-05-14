import tkinter as tk
import random as rd

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
    print(serpent)

def bienvenue():
    global pseudo
    pseudo.set('bienvenue '+saisir_nom.get() + ' !')

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

def mouvement():
    global serpent, x, y, obstacles, pommes, scores, directions, direction
    nouv_tete_serpent()
    t1, t2 = env_jeu.coords(serpent[1])
    p1, p2 = env_jeu.coords(pommes[0])
    if (t1 == p1 and t2 == p2):
        scores += 1
        env_jeu.delete(pommes[0])
        p1 = 40 * rd.randint(1,18)
        p2 = 40 * rd.randint(1, 13)
        po = env_jeu.create_image(p1, p2, image=pomme1, anchor="nw") # multiple de 40 attention
        pommes.insert(0, po)    
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
    env_jeu.after(500, mouvement)

def jouer(title):
    decors(title)
    mouvement()

def nouv_tete_serpent():
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
    print(serpent)
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
for frame in (frame_menu, frame_niveaux, frame_score, frame_canvas, frame_vitesse):
    frame.grid(row=0, column=0, sticky="nsew")

choix_frame(frame_menu)
pseudo = tk.StringVar()
pseudo.set('')
serpent =[]
directions = []
direction = 'gauche'
obstacles = []
pommes = []
scores = 0 
x, y = -40, 0

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

######## canvas #######
env_jeu = tk.Canvas(frame_canvas, width=800, heigh=600, bg="darkgray")
env_jeu.place(x=0, y=0)

#######vitesse#########
titre_vitesse = tk.Label(frame_vitesse, text='VITESSES', fg='green', font="Helvetica 18 bold italic")
titre_vitesse.place(x=100, y= 10)
menu3 = tk.Button(frame_vitesse, text='menu', bg='light gray', fg='green', font="Helvetica 16 bold italic", width=7, command=lambda:choix_frame(frame_menu))
menu3.place(x=10, y=250)
lent = tk.Button(frame_vitesse, text='lent', bg='light gray', fg='green', font="Helvetica 16 bold italic", width=7)
lent.place(x=100, y=75)
moyen = tk.Button(frame_vitesse, text='moyen', bg='light gray', fg='green', font="Helvetica 16 bold italic", width=7)
moyen.place(x=100, y=125)
rapide = tk.Button(frame_vitesse, text='rapide', bg='light gray', fg='green', font="Helvetica 16 bold italic", width=7)
rapide.place(x=100, y=175)


snake.bind("<KeyPress-Left>", gauche)
snake.bind("<KeyPress-Right>", droit)
snake.bind("<KeyPress-Up>", haut)
snake.bind("<KeyPress-Down>", bas)

snake.mainloop()