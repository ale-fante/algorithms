letters = list("Crunchy Frog")
print(letters)

back_together = "".join(letters)
print(back_together)

song = "The rain in Spain..."
words = song.split()
print(words)

first_split = song.split("ai")
print(first_split)

glue = "-"
phrase = glue.join(words)
print(phrase)

ellipsis = "... ".join(words)
print(ellipsis)

back_together = "".join(words)
print(back_together)


def f(n):
	""" Find the first positive integer between 101 and less than n that is divisible by 21"""
	for i in range(101, n):
		if (i % 21 == 0):
			return i

print(f(12))
print(f(200))

