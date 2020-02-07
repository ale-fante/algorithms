import turtle

window = turtle.Screen()

window.bgcolor("SlateBlue")
window.title("Hello, Ale!")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()
alex.color("white")
alex.pensize(2)

jorge = turtle.Turtle()
jorge.color("yellow")
jorge.pensize(3)

tess.forward(90)
tess.left(120)
tess.forward(90)
tess.left(120)
tess.forward(90)
tess.left(120) # Complete the triangle

# Draw square
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)


# Draw circle
# jorge.circle(50)
for i in range(100):
  jorge.circle(5+i, 10)
#window.mainloop()