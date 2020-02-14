# Algorithm: A mechanical process for solving a category of problems

import random

joe = random.Random()

# Version 1
# Build a list of random numbers, then add them
numbers = []
for _ in range(100):
	num = joe.randrange(10) # Generate one random #
	numbers.append(num)

total = sum(numbers)
print(total)

# Version 2
# Sum the ramndom numbers as we generate them

tot = 0
for _ in range(100):
	number = joe.randrange(10)
	tot += number

print(tot)

# Does this list have odd numbers?

# % (modulo) Returns the decimal part (remainder) of the quotient.
numbers = [10, 5, 24, 3, 9, 12, 11]

count = 0

for number in numbers:
	count += number % 2 == 1
print(count > 0)
