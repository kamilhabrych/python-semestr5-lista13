from graphics import *

win = GraphWin('Kamil Habrych zadanie 2', 250, 250)
win.setBackground('brown')

pt1 = Point(125,75)
pt2 = Point(125,125)
pt3 = Point(125,175)

pt1.setOutline('white')
pt2.setOutline('yellow')
pt3.setOutline('black')

pt1.draw(win)
pt2.draw(win)
pt3.draw(win)

win.getMouse()
win.close()