# Count the number of decimal digits in a positive integer

n = 293.03242

count = 0

while n != 0:
	count = count + 1
	n = n // 10

# When the loop exits, count contains the result
print(count)

# now only count the digits that are 0 or 5
n = 12345
print("Complete number sequnce: " + str(n))
count = 0
while n > 0:
	digit = n % 10
	print("Digit being looked at: " + str(digit))

	if digit == 0 or digit == 5:
		count = count + 1
		print("On iteration number: " + str(count))
	n = n // 10
	print("Numbers left on the string: " + str(n))

print(/n + "How many zeros of fives are in the sequence? " + str(count))