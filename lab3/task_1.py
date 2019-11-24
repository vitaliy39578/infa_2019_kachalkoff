from graph import *

def draw_the_circle(x, y, r, g, b, radius):
	brushColor(r, g, b)
	circle(x, y, radius)

penColor(0, 0, 0)
draw_the_circle(250, 250, 255, 255, 0, 200)
input()