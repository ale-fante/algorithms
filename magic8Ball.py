import random

# def getAnswer(answerNumber):
# 	if answerNumber == 1:
# 		return "It is certain"
# 	elif answerNumber == 2:
# 		return "It is decidedly so"
# 	elif answerNumber == 3:
# 		return "Most definitely yes"
# 	elif answerNumber == 4:
# 		return "Reply hazy, try again"
# 	elif answerNumber == 5:
# 		return "As again later"
# 	elif answerNumber == 6:
# 		return "Concentrate and ask again"
# 	elif answerNumber == 7:
# 		return "My response is no"
# 	elif answerNumber == 8:
# 		return "Outlook not so good"
# 	elif answerNumber == 9:
# 		return "Very doubtful"

# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)

# or a shorter version:

def getAnswer(answerNumber):
	responses =  {
		1: "It is certain",
		2: "It is decidedly so",
		3: "Most definitely yes",
		4: "Reply hazy, try again",
		5: "As again later",
		6: "Concentrate and ask again",
		7: "My response is no",
		8: "Outlook not so good",
		9: "Very doubtful"
	}

	for k, v in responses.iteritems():
		r = random.randint(1, 9)
		chosen_value = r, v
	return chosen_value

getAnswer(1)



