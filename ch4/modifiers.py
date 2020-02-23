def double_stuff(values):
	"""
	Return a new list which contains doubles of the elements in the list values.
	"""
	new_list = []
	for value in values:
		new_elem = 2 * value
		new_list.append(new_elem)

	return new_list

print(double_stuff("Alejandra"))

def el_doble(values):
	""" Double th elements of values in-place """
	for index, value in enumerate(values):
		values[index] = 2 * value

		print(values[index])

el_doble([1, 2, 3])

# Functions help us with our mental chunking: they allow us to group together statements for a high level purpose.
