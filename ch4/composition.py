def is_divisible(x, y):
	"""
	Test if x is exactly divisible by y
	"""
	if x % y == 0:
		return True
	else:
		return False

# or


def is_num_divisible(x, y):

	return x % y == 0

print(is_num_divisible(6, 3))