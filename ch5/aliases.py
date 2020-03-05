a = [1, 2, 3]

b = a

print(a is b)

# Because the same list has two names, a and b, we say that it is aliased. 
print(a)
print(b)

# cloning

a = [1, 2, 3]
b = a[:]
print(b)


for number in range(20):
	if number % 3 == 0:
		print(number)

for fruit in ["banana", "apple", "quince"]:
	print("I would like to eat " + fruit + "s!")


xs = [1, 2, 3, 4, 5]

for i in range(len(xs)):
	xs[i] = xs[i]**2
	print(xs[i])

# enumerate

xs = [1, 2, 3, 4, 5]

for (i, val) in enumerate(xs):
	xs[i] = val ** 2

# enumerate generates pairs of index and value during the list traversal. 

for (index, value) in enumerate(["banana", "apple", "pear", "lemon"]):
	print(index, value)