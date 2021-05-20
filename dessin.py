import tkinter as tk
from PIL import Image, ImageDraw

dessin = tk.Tk()
dessin.title("créer un dessin")
dessin.geometry('400x400')

couleur = 'red'
oeuvre = []
coord = []

def quadrillage():
    i, j = 10, 10
    while i < 200:
            canevas.create_line(i, 0, i, 200, fill='olive drab')
            canevas.create_line(0, j , 200, j, fill='olive drab')
            j += 10
            i += 10

def dessiner(event):
    global couleur, oeuvre, coord
    x, y = event.x, event.y
    j = 0 
    for i in range(0, 200, 10):
        for j in range(0, 200, 10):
            if (i < x < i+10) and (j < y < j+10):
                pixel = canevas.create_rectangle(i, j, i+10, j+10, fill=couleur)
                coord.append([(i, j), (i+10, j+10), couleur])
                oeuvre.append(pixel)

def effacer():
    global oeuvre, coord
    if oeuvre == []:
        pass
    else : 
        pixel = oeuvre.pop()
        canevas.delete(pixel)
        coord.pop()

def image():
    global coord
    image1 = Image.new('RGB', (200, 200), 'DarkGray')
    draw = ImageDraw.Draw(image1)
    for elem in coord:
        draw.rectangle([elem[0], elem[1]], fill=elem[2])
    filename = "corps_lateral.gif"
    image1.save(filename)


def noir():
    global couleur
    couleur = 'black'

def violet():
    global couleur
    couleur = 'BlueViolet'

def mer():
    global couleur
    couleur = 'DodgerBlue'

def sapin():
    global couleur
    couleur = 'ForestGreen'

def rouge():
    global couleur
    couleur = 'FireBrick'

def orange():
    global couleur
    couleur = 'DarkOrange'

def jaune():
    global couleur
    couleur = 'yellow'

def blanc():
    global couleur
    couleur = 'white'

def gris():
    global couleur
    couleur = 'DarkGray'

def mauve():
    global couleur
    couleur = 'HotPink'

def bleu_ciel():
    global couleur
    couleur = 'LightSkyBlue'

def vert_clair():
    global couleur
    couleur = 'YellowGreen'

def carotte():
    global couleur
    couleur = 'IndianRed'

def orangee():
    global couleur
    couleur = 'chocolate'

def dore():
    global couleur
    couleur = 'gold'

def lavande():
    global couleur
    couleur = 'WhiteSmoke'
        

canevas = tk.Canvas(dessin, width=200, heigh=200, bg='white')
canevas.place(x=100, y=190)

noir = tk.Button(dessin, bg='black', padx=20, pady=20, command=noir)
noir.place(x=0, y=0)
violet = tk.Button(dessin, bg='BlueViolet', padx=20, pady=20, command=violet)
violet.place(x=50, y=0)
mer = tk.Button(dessin, bg='DodgerBlue', padx=20, pady=20, command=mer)
mer.place(x=100, y=0)
sapin = tk.Button(dessin, bg='ForestGreen', padx=20, pady=20, command=sapin)
sapin.place(x=150, y=0)
rouge = tk.Button(dessin, bg='FireBrick', padx=20, pady=20, command=rouge)
rouge.place(x=200, y=0)
orange = tk.Button(dessin, bg='DarkOrange', padx=20, pady=20, command=orange)
orange.place(x=250, y=0)
jaune = tk.Button(dessin, bg='yellow', padx=20, pady=20, command=jaune)
jaune.place(x=300, y=0)
blanc = tk.Button(dessin, bg='white', padx=20, pady=20, command=blanc)
blanc.place(x=350, y=0)

gris = tk.Button(dessin, bg='DarkGray', padx=20, pady=20, command=gris)
gris.place(x=0, y=65)
mauve = tk.Button(dessin, bg='HotPink', padx=20, pady=20, command=mauve)
mauve.place(x=50, y=65)
bleu_ciel = tk.Button(dessin, bg='LightSkyBlue', padx=20, pady=20, command=bleu_ciel)
bleu_ciel.place(x=100, y=65)
vert_clair = tk.Button(dessin, bg='YellowGreen', padx=20, pady=20, command=vert_clair)
vert_clair.place(x=150, y=65)
carotte = tk.Button(dessin, bg='IndianRed', padx=20, pady=20, command=carotte)
carotte.place(x=200, y=65)
orangee= tk.Button(dessin, bg='chocolate', padx=20, pady=20, command=orangee)
orangee.place(x=250, y=65)
dore = tk.Button(dessin, bg='gold', padx=20, pady=20, command=dore)
dore.place(x=300, y=65)
lavande = tk.Button(dessin, bg='WhiteSmoke', padx=20, pady=20, command=lavande)
lavande.place(x=350, y=65)

enregistrer = tk.Button(dessin, bg='white', text='enregistrer le dessin', padx=45, command=image)
enregistrer.place(x=100, y=135)
effacer = tk.Button(dessin, bg='white', text='effacer dernier pixel', padx=45, command=effacer)
effacer.place(x=100, y=155)

quadrillage()
dessin.bind('<Double-Button-1>', dessiner)

dessin.mainloop()