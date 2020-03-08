def add_vector(vector_one, vector_two):
	sum_list = []
	for i in range(len(vector_one)):
		sum_of_vectors = vector_one[i] + vector_two[i]
		sum_list.append(sum_of_vectors)
	return sum_list

one = [2, 4, 6]
two = [1, 3, 5]

print(add_vector(one, two))