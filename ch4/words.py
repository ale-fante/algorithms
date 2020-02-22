def find_first_2_letter_word(words):
	for word in words:
		if len(word) == 2:
			return word
	return ""

print(find_first_2_letter_word(["This", "is", "a", "happy", "puppy"]))
print(find_first_2_letter_word(["I", "like", "beer"]))

def distance_1(x1, y1, x2, y2):
	return 0.0

print(distance_1(2, 4, 2, 4))

def distance_2(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	return 0.0

print(distance_2(2, 4, 2, 4))


def distance_3(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx * dx + dy * dy
	result = dsquared**0.5
	return result

print(distance_3(1, 2, 4, 6))

import math

def dist_math(x1, y1, x2, y2):
	return math.sqrt( (x2-x1)**2 + (y2-y1)**2)

print(dist_math(1, 2, 4, 6))