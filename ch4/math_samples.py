def area(radius):
	return 3.14159 * radius * radius

# This wouldn't work because if the value passed in is 0, it would never work

def absolute_value(x):
	if x < 0:
		return -x
	else:
		return x

# OR better yet:

def absolute_val(x):
	if x < 0:
		return -x
	return x

print(area(10))
print(absolute_value(-20))
print(absolute_val(-10))

