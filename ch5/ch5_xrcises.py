# One
# range(Start, STOP, Step)
# Step is the interval between successive elements of a linear sequenence
exe_one = list(range(10, 50, 5))
print(exe_one)


#This would produce a runtime error
#exec_two = list(range(2, 10, 0)
# print(exec_two)

#And this too
# exec_three = list(range(10, 20, -2)
# print(exec_three)


# Two

import turtle

tess = turtle.Turtle()
alex = tess
alex.color("hotpink")
print(alex)
print(tess)

# This fragment creates two turtle instances. 
# Setting the color to alex changes the color of tess

# Three

a = [1, 2, 3]
b = a[:]
b[0] = 5
print(a)
print(b)

# Four

this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]

# Returns False
print("Test 1: {0}".format(this is that))
print(this)
print(that)
that = this
# Returns True
print("Test 2: {0}".format(this is that))
print(this)
print(that)


