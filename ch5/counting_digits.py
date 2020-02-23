def count_ñ(text):
	count = 0
	for letter in text:
		if letter == "ñ":
			count += 1
	return(count)

print(count_ñ("Después de años de engaños a la gente... vio a una señora "))


def find2(haystack, needle, start):
	for index, letter in enumerate(haystack[start:]):
		if letter == needle:
			return index
	return -1

print(find2("Alejandra", "a", 3))