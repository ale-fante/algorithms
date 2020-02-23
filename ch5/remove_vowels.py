def remove_vowels(phrase):
	vowels = "aeiou"
	string_without_vowels = ""
	for letter in phrase:
		if letter.lower() not in vowels:
			string_without_vowels += letter

	return string_without_vowels

print(remove_vowels("Para cumplir con mi capricho, mi mama se lleno de valor y..."))


# Find function

def my_find(haystack, needle):
	"""
	Find and return the index of needle in haystack.
	Return -1 if needle does not occur in haystack.
	"""
	for index, letter in enumerate(haystack):
		if letter == needle:
			return index

	return -1

print(my_find("ALENAJÑDRITA", "Ñ"))

haystack = "BANAN@RAMA!"
print(haystack.find("@"))
print(my_find(haystack, "@"))