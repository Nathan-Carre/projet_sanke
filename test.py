from tkinter import *

fen = Tk()
c = Canvas(fen,width=500,height=500,bg="yellow")
c.pack()

tournantBasGauche = PhotoImage(file=r'images\tournant_bas_gauche.gif')
a = c.create_image(200,200,image=tournantBasGauche)
b = c.create_rectangle(300,300,360,360)
print(c.coords(a))
print(c.coords(b))

fen.mainloop()