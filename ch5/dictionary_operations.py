english_spanish = {
	"one" : "uno",
	"two" : "dos",
	"three" : "tres",
	"four" : "cinco",
	"five" : "cinco",
	"six" : "seis",
	"seven" : "siete",
	"eight" : "ocho",
	"nine" : "nueve",
	"ten" : "diez"
}

for key in english_spanish.keys():
	print("Got key", key, " which maps to value", english_spanish[key])

keys = list(english_spanish.keys())
print(keys)

for key in english_spanish:
	print("Got key", key)

print(list(english_spanish.values()))
print(list(english_spanish.items()))

for (key, value) in english_spanish.items():
	print("Got", key, "that maps to", value)