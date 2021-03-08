from graphics import *
import random
import math

max_width = 500
max_height = 500

n = int(input("Ile bokow: "))

win = GraphWin('Kamil Habrych zadanie 6', max_width, max_height)
win.setBackground('brown')

center = (250, 250)
r = 125

for item in range(n):
    start_point = Point(center[0] + r * math.cos(2 * math.pi * item / n), center[1] + r * math.sin(2 * math.pi * item / n))
    if item != n - 1: 
        next_point = Point(center[0] + r * math.cos(2 * math.pi * (item + 1) / n), center[1] + r * math.sin(2 * math.pi * (item + 1) / n))
    else: 
        next_point = Point(center[0] + r * math.cos(2 * math.pi * 0 / n), center[1] + r * math.sin(2 * math.pi * 0 / n))
    
    l = Line(start_point,next_point)
    
    print("{0} => {1}".format(start_point, next_point))
    
    l.draw(win)

win.getMouse()
win.close()