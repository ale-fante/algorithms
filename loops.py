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


n = 6

current_sum = 0
for i in range(n+1):

	current_sum += i

print(current_sum)

print("COLLATZ 3n + 1 Sequence:")

# collatz 3n + 1 sequence
''' The "computational rule" for creating the sequence is to start from
some given n, and to generate the next term of the sequnce from n, either by
halving n, (whenever n is even), or else by multiplying it by three and adding 1. 
The sequencee terminates wheen n reaches 1 '''
n = 102

# until n is equal to 1
while n != 1:
	# do this:
	print(n)
	# if th number is even, divide it into 2
	if n % 2 == 0:
		n = n // 2
	# if the number is not even, multiply by thre and add one
	else:
		n = n * 3 + 1

print(n)

