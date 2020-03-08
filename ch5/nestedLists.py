nested = ["hello", 2.0, 5, [10, 20]]

# Two step approach
index_three = nested[3]
elem = index_three[0]

print(index_three)
print(elem)


# Single step approach
nested_two = ["hello", 2.0, 5, [10, 20]]
elem_two = nested[3][0]
print(elem_two)

# Matrix
mx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(mx[0])
print(mx[1][2])