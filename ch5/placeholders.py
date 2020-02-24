letter = """
Dear {0} {2}.
{0}, I have an interesting money making proposition for you!
If you deposit $10 million into my bank account, I can double
your money...
"""

print(letter.format("Paris", "Whitney", "Hilton"))
print(letter.format("Bill", "Henry", "Gates"))

print("i\t**2\t**3\t**5\t**10\t**20")

for i in range(1, 11):
	print(i, "\t", i ** 2, "\t", i ** 3, "\t", i ** 5, "\t", i ** 10, "\t", i ** 20)


# A much better approach

layout = "{0:>4} {1:>6} {2:>6} {3:>8} {4:>13} {5:>24}"

print(layout.format(i, i ** 2, i ** 3, i ** 5, i ** 10, i ** 20))

for i in range(1, 11):
	print(layout.format(i, i ** 2, i ** 3, i ** 5, i ** 10, i ** 20))