


def binary_search(list, item):
	# low and high keep track of which part of the list you'll search in
	low = 0
	high = len(list) -1

	# while you haven't narrowed it down to one element...
	while low <= high:

		# check the middle element
		mid = (low + high)
		guess = list[mid]

		# found the item
		if guess == item:
			return mid

		# the guess was too high
		if guess > item:
			high = mid - 1

		# the guess was too low
		else:
			low = mid + 1

	# the item doesn't exist
	return None

my_list = [1, 3, 5, 7, 9]

print binary_search(my_list, 3) # => 1 -- lists start at 0. The second slot has index 1
print binary_search(my_list, -1) # => None
