numbers = [17, 123]

# Any exprssion evaluating to an integer can b used as an index
print(numbers[9-8])

# list traversal
horsemen = ["war", "famine", "pestilence", "death"]

"""Don't do this"""
# for i in [0, 1, 2, 3]:
# 	print(horsemen[i])

"""Do this instead"""
for h in horsemen:
	print(h)

students = [
	("Jose", ["CompSci", "Physics", "Math"]),
	("Maria", ["Math", "CompSci", "Stats"]),
	("Chuy", ["InfSys", "Accounting", "Economics"]),
	("Pepe", ["InfSys", "Maths", "Economics"]),
	("Jorge", ["Sociology", "Law", "CompSci"]),
]

# Count how many students ar taking CompSci

counter = 0
for name, subjects in students:
	if "CompSci" in subjects:
		counter += 1

print("The number of students taking CompSci is ", counter)

first = [0, 1, 2, 3]
second = [4, 5, 6, 7]

print(first + second)

one = [1, 1, 1, 1, 1]
two = [2, 2, 2, 2, 2]

# Repeats list twice
print(one * 2)
# Repeats list thrice
print(two * 3)
