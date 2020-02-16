import turtle

def draw_square(animal, size):
	"""
	Make cursor draw a square with sides of length size
	"""
	for _ in range(4):
		animal.color("lightpink")
		animal.pensize(5)
		animal.forward(size)
		animal.left(90)


window = turtle.Screen() # set up window
window.bgcolor("lightgreen")
window.title("FUNCTIONS!")

alex = turtle.Turtle()
draw_square(alex, 50)


def draw_watermelon():
	"""
	Make cursor draw watermelon
	"""
	window.title("WATERMELON")
	window.bgcolor("purple")
	turtle.pensize(3)
	turtle.speed(0)
	turtle.up()
	turtle.circle(250,270)
	turtle.down()
	turtle.begin_fill()
	turtle.fillcolor("limegreen")
	turtle.circle(250,180)
	turtle.left(90)
	turtle.fd(50)
	turtle.left(90)
	turtle.circle(-200,180)
	turtle.left(90)
	turtle.fd(50)
	turtle.end_fill()
	turtle.left(180)
	turtle.fd(50)
	turtle.right(90)
	turtle.begin_fill()
	turtle.fillcolor("hotpink")
	turtle.circle(200,180)
	turtle.left(90)
	turtle.fd(400)
	turtle.end_fill()
	turtle.up()
	turtle.goto(-130,230)
	turtle.down()
	turtle.begin_fill()
	turtle.circle(15,-180)



draw_watermelon()

