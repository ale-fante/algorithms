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