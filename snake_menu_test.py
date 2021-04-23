import tkinter as tk 

def choix_frame(frame):
    frame.tkraise()

def decors(title):
    choix_frame(frame_canvas)
    snake.geometry('800x600')
    x, y = 0, 0
    niveau = open(title)
    for ligne in niveau:
        for i in range(20):
            case = ligne[i]
            if case == "X":
                env_jeu.create_rectangle(x, y, x+40, y+40, fill='black')
            elif case == "P":
                env_jeu.create_oval(x, y, x+40, y+40, fill='red')
            elif case == "T":
                env_jeu.create_rectangle(x, y, x+40, y+40, fill='green')
            elif case == "Q":
                env_jeu.create_rectangle(x, y, x+40, y+40, fill='green')
            x += 40
        x = 0
        y += 40
    niveau.close()

snake = tk.Tk()
snake.title("jeu snake")
snake.geometry('300x300')

snake.rowconfigure(0, weight=1)
snake.columnconfigure(0, weight=1)

frame_menu = tk.Frame(snake)
frame_niveaux = tk.Frame(snake)
frame_score = tk.Frame(snake)
frame_canvas = tk.Frame(snake)
for frame in (frame_menu, frame_niveaux, frame_score, frame_canvas):
    frame.grid(row=0, column=0, sticky="nsew")

choix_frame(frame_menu)
nom=tk.StringVar()

############# menu ############
titre_menu = tk.Label(frame_menu, text='SNAKE', fg='green', font="Helvetica 26 bold italic")
titre_menu.place(x=80, y=20)
niveaux = tk.Button(frame_menu, text='Niveaux', bg='light gray', fg='green', font="Helvetica 16 bold italic", command=lambda:choix_frame(frame_niveaux))
niveaux.place(x=100, y=100)
score = tk.Button(frame_menu, text='Scores', bg='light gray', fg='green', font="Helvetica 16 bold italic", width=7, command=lambda:choix_frame(frame_score))
score.place(x=100, y=150)

######## niveaux ######
titre_niveaux = tk.Label(frame_niveaux, text='NIVEAUX', fg='green', font="Helvetica 18 bold italic")
titre_niveaux.place(x=100, y= 10)
niveau1 = tk.Button(frame_niveaux, text='niveau 1', bg='light gray', fg='green', font="Helvetica 14 bold italic", command=lambda:decors('niveau_1.txt'))
niveau1.place(x=100, y=100)
menu1 = tk.Button(frame_niveaux, text='menu', bg='light gray', fg='green', font="Helvetica 16 bold italic", width=7, command=lambda:choix_frame(frame_menu))
menu1.place(x=10, y=250)

######## score ##########
titre_score = tk.Label(frame_score, text='SCORES', fg='green', font="Helvetica 18 bold italic")
titre_score.place(x=100, y= 10)
nom = tk.Label(frame_score, text='entrer un pseudo', fg='green', font="Helvetica 14 bold italic")
nom.place(x=60, y= 50)
saisir_nom = tk.Entry(frame_score, textvariable=nom, width=40)
saisir_nom.place(x=25, y=100)
menu2 = tk.Button(frame_score, text='menu', bg='light gray', fg='green', font="Helvetica 14 bold italic", width=7, command=lambda:choix_frame(frame_menu))
menu2.place(x=10, y=250)

######## canvas #######
env_jeu = tk.Canvas(frame_canvas, width=800, heigh=600, bg="darkgray")
env_jeu.place(x=0, y=0)

snake.mainloop()