letters = list("Crunchy Frog")
print(letters)

back_together = "".join(letters)
print(back_together)

song = "The rain in Spain..."
words = song.split()
print(words)

first_split = song.split("ai")
print(first_split)

glue = "-"
phrase = glue.join(words)
print(phrase)

ellipsis = "... ".join(words)
print(ellipsis)

back_together = "".join(words)
print(back_together)


def f(n):
	""" Find the first positive integer between 101 and less than n that is divisible by 21"""
	for i in range(101, n):
		if (i % 21 == 0):
			return i

print(f(12))
print(f(1000000))
# Once the condition is met, no further elements are generated on "range.()" withing python3

"""
YMMV - Your Mileage may vary
"""

#Create lazy promise
print(range(10))
#Call in the promise to produce a list
print(list(range(10)))


import random

joe = random.Random()

def sum1():
	""" Build a list of random numbers, then sum them """
	xs = []
	for i in range(100000):
		num = joe.randrange(1000)
		xs.append(num)

	tot = sum(xs)
	return tot

print(sum1())


def sum2():
	""" Sum the random numbers as we generate them """
	tot = 0
	for i in range(100000):
		num = joe.randrange(1000)
		tot += num
	return tot

print(sum2())




