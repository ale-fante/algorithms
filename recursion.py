# Regular approach

def look_for_key(main_box):
	pile = main_box.make_a_pile_to_look_through()
	while pile is not empty:
		box = pile.grab_a_box()
		for item in box:
			if item.is_a_box():
				pile.append(item)
			elif item.is_a_key():
				print("found the key!")


# Recursion

def look_for_key(box):
	for item in box:
		if item.is_a_box():
			look_for_key(item) # <= Recursion!
		elif item.is_a_key():
			print("found the key!")


# Count down

def countdown(i):
	print(i)
	# Base case
	if i <= 0:
		return
	# Recursive case
	else:
		countdown(i-1)