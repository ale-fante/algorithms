s = "def Aliniacion"

def_pos = s.find("def ")

if def_pos == 0:
	op_index = s.find("(")

	fnname = s[4:op_index]

	print(fnname)