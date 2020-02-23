import random
joe = random.Random()

def sum1():
	""" Build a list of random nums, then add them """
	xs = []
	for i in range(100):
		num = joe.randrange(10) # geenerate one random
		xs.append(num)

	tot = sum(xs)
	return tot

# Preferred way

def sum2():
	""" Sum the random numberes as we generate them """
	tot = 0
	for i in range(100):
		num = joe.randrange(10)
		tot += num

	return tot

print(sum1())
print(sum2())