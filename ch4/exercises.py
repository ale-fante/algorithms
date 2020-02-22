def turn_clockwise(initial):
	for l in initial:
		if l == "N":
			print("E")
		elif l == "E":
			print("S")
		elif l == "S":
			print("W")
		elif l == "W":
			print("N")
		else:
			None

print(turn_clockwise("W"))
