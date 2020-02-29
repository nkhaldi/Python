from tkinter import *
from random import *

size = 600
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()
diapason = 0

for i in range(10000):
    colors = choicecolors = choice(['red'])
    x0 = randint(0, size)
    y0 = randint(0, size)
    d = randint(0, size/20)
    canvas.create_oval(x0, y0, x0+d, y0+d, fill=colors)
    root.update()
