from graphics import *
import random

max_width = 500
max_height = 500

win = GraphWin('Kamil Habrych zadanie 5', max_width, max_height)
win.setBackground('brown')

first_point = Point(random.randint(0, max_width), random.randint(0, max_height))
start_point = first_point

for item in range(10):
    if item != 0: 
        start_point = next_point
    if item != 9: 
        next_point = Point(random.randint(0, max_width), random.randint(0, max_height))
    else: 
        next_point = first_point

    l = Line(start_point, next_point)

    if item != 0: 
        l.setFill('white')
    else: 
        l.setFill('black')

    l.setWidth('1')
    l.setArrow('last')
    l.draw(win)

win.getMouse()
win.close()