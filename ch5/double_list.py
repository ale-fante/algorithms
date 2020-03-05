
def double_stuff(stuff_list):
	""" Overwrite each element in a list with double it's value"""
	for (index, stuff) in enumerate(stuff_list):
		stuff_list[index] = 2 * stuff

		print(index, stuff)

fav_movies = ["horsegirl", "totoro", "cantinflas", "roma"]
double_stuff(fav_movies)

nums = [2, 5, 9]
double_stuff(nums)