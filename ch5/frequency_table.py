letter_counts = {}

input_string = "ThiS String with Upper and lower case Letters"

no_spaces = input_string.replace(" ", "")
lower_case_string = no_spaces.lower()
sorted_string = sorted(lower_case_string)


for letter in sorted_string:
	letter_counts[letter] = letter_counts.get(letter, 0) + 1


print(letter_counts)

