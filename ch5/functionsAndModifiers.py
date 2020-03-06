# Functions which take lists as arguments and change theem during execution are modifiers.
# The changes they makee are called modifiers.



# A pure function does not produce side effects. It communicates with the calling program only
# through parameters, which it does NOT modify, and a return value. Pure function

def double_stuff(a_list):
	""" Return a new list which contains 
	doubles of the elements in a_list.
	"""
	new_list = []
	for value in a_list:
		new_elem = 2 * value
		new_list.append(new_elem)


	return new_list

things = [2, 5, 9]
more_things = double_stuff(things)
print(things)
print(more_things)
