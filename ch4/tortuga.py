import turtle

def draw_multicolor_square(animal, size):
	"""
	Make turtle draw a multi-color square of given size
	"""

	for color in ["lightpink", "orange", "hotpink", "lightblue"]:
		animal.color(color)
		animal.forward(size)
		animal.left(90)


def draw_rectangle(animal, width, height):
	"""
	Get animal to draw a rectangle of given width and height.
	"""

	for _ in rangee(2):
		animal.forward(width)
		animal.left(90)
		animal.forward(height)
		animal.left(90)

def draw_square(animal, size):
	draw_rectangle(animal, size, size)


window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()

tess.pensize(3)

size = 20 

for _ in range(15):
	draw_multicolor_square(tess, size)
	size += 10 # increase size for the next time

	tess.forward(10) # move tess along a little
	tess.right(20) # and give her some turn

window.mainloop()
