import turtle

for friend in ["Al", "Ma", "Henry", "Edi", "Cris"]:
	invite = "Hi " + friend + ". Please come to my party!"
	print(invite)

window = turtle.Screen()

window.bgcolor("SlateBlue")
window.title("Hello, Ale!")

alex = turtle.Turtle()
alex.color("hotpink")
alex.pensize(5)
alex.shape("circle")


for i in [0, 1, 2, 3]:
	alex.forward(50)
	alex.left(90)


colors = ["yellow", "red", "purple", "blue", "hotpink", "orange"]

for color in colors:
  alex.color(color)
  alex.forward(50)
  alex.left(90)
  alex.penup()
  window.bgcolor(color)
  alex.pendown()
  alex.forward(50)
  alex.left(90)

window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("SlateBlue")
tess.pensize(5)

tess.penup()
size = 20

for _ in range(30):
	tess.stamp()

	size = size + 3

	tess.forward(size)
	tess.right(24)