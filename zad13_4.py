from graphics import *
import random

max_width = 500
max_height = 500

outlines = ('white', 'yellow', 'black')
fills = ('blue', 'purple', 'green')

win = GraphWin('Kamil Habrych zadanie 4', max_width, max_height)
win.setBackground('brown')

o = Oval(Point(50, 100), Point(125, 175))
o.setOutline(random.choice(outlines))
o.setWidth(5)
o.setFill(random.choice(fills))
o.draw(win)

r = Rectangle(Point(200, 400), Point(350, 450))
r.setOutline(random.choice(outlines))
r.setWidth(5)
r.setFill(random.choice(fills))
r.draw(win)

win.getMouse()
win.close()