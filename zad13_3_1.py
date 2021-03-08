from graphics import *
import random
import time

max_width = 500
max_height = 500

outlines = ('white', 'yellow', 'black')
fills = ('blue', 'purple', 'green')

win = GraphWin('Kamil Habrych zadanie 3 podpunkt 2', max_width, max_height)
win.setBackground('brown')

for c in range(50):
    width_circle = 10
    r = random.randint(5, 25)
    dot = Point(random.randint(0 + r + width_circle, max_width - r - width_circle),
    random.randint(0 + r + width_circle, max_height - r - width_circle))
    c = Circle(dot,r)
    c.setOutline(random.choice(outlines))
    c.setWidth(width_circle)
    c.setFill(random.choice(fills))
    c.draw(win)
    time.sleep(0.1)
    
win.getMouse()
win.close()