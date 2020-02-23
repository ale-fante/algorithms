# 😎 visualize the indices

fruit = "Papaya"
index_of_string = list(enumerate(fruit))
print(index_of_string)

# Get the length of the word

nombre = "Alejandra"
len_of_name = len(nombre)
print(len_of_name)

# Get the last element of the string
nombre = "Alejandrina"
last_letter = nombre[-1]
print(last_letter)

# Abecedarian series
prefixes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
suffix = "artha"

for p in prefixes:
    print(p + suffix)

# Slices

word = "Pineapple"

# Everything
print(word[:])
# The first three
print(word[:3])
# Omit the first three and print the rest
print(word[3:])

