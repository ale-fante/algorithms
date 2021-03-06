def add_vector(vector_one, vector_two):
	sum_list = []
	for i in range(len(vector_one)):
		sum_of_vectors = vector_one[i] + vector_two[i]
		sum_list.append(sum_of_vectors)
	return sum_list

one = [2, 4, 6]
two = [1, 3, 5]

print(add_vector(one, two))

def scalar_mult(scalar, vector):
	scalar_result = []
	for i in range(len(vector)):
		multi = scalar * vector[i]
		scalar_result.append(multi)
	return scalar_result

print(scalar_mult(5, [1, 2]))

def dot_product(vec1, vec2):
	sum_of_prod = []
	for i in range(len(vec1)):
		prod_vec = vec1[i] * vec2[i]
		sum_of_prod.append(prod_vec)

	return sum(sum_of_prod)

print(dot_product([1, 2], [1, 4]))
print(dot_product([1, 1], [1, 1]))
print(dot_product([1, 2, 1], [1, 4, 3]))
