for x in range(13):
	print(x, 2 ** x)


# for i in range(1, 7):
# 	print(2 * i, end="   ")
# print()

total = 0

while True:
	response = input("Enter the next number. (Leave blank to end) ")
	if response == "" or response == "-1":
		break
	total += int(response)

print("The total of the numbers you entered is ", total)