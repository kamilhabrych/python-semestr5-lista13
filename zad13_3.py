from graphics import *
import random

max_width = 500
max_height = 500

outlines = ('white', 'yellow', 'black')
fills = ('blue', 'purple', 'green')

win = GraphWin('Kamil Habrych zadanie 3', max_width, max_height)
win.setBackground('brown')
for c in range(5):
    width_circle = 5
    r = random.randint(5,50)
    dot = Point(random.randint(0 + r + width_circle, max_width - r - width_circle), 
    random.randint(0 + r + width_circle, max_height - r - width_circle))
    c = Circle(dot, r)
    c.setOutline(random.choice(outlines))
    c.setWidth(width_circle)
    c.setFill(random.choice(fills))
    c.draw(win)

win.getMouse()
win.close()