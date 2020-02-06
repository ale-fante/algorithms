def findSmallest(arr):
	# stores the smallest value
	smallest = arr[0]
	# stores the index of the smallest value
	smallest_index = 0

	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i

	return smallest_index

# sorts an array
def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		# finds the smallest element in the array, and adds it to the new array
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

print selectionSort([5,3,6,0,2,100,99,0,10,55])