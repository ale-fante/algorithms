import string

def remove_punctuation(phrase):
	phrase_sans_punct = ""
	# print(string.punctuation)
	# returns !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
	for letter in phrase:
		if letter not in string.punctuation:
			phrase_sans_punct += letter
	return phrase_sans_punct

phrase = "Well, I never did! Did you send me your em@il?"
print(remove_punctuation(phrase).split())