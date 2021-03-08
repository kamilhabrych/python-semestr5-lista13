from graphics import *
import random

max_width = random.randint(100,1000)
max_height = random.randint(100,1000)

colors = ('white', 'yellow', 'black')

win = GraphWin('Kamil Habrych zadanie 2 podpunkt 2', max_width, max_height)
win.setBackground('brown')

for point in range(1000):
    dot = Point(random.randint(0, max_width),random.randint(0, max_height))
    dot.setOutline(random.choice(colors))
    dot.draw(win)

win.getMouse()
win.close()