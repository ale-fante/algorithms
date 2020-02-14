for i in [12, 16, 17, 24, 29, 30]:
	# Pares
	if i % 2:
		continue
	print(i)

print("Done")

celebs = [("Brad Pitt", 1963), ("Jack Nicholson", 1937), ("Betty White", 1920), ("Justin Bieber", 1994)]

print(celebs)
print(len(celebs))

# print the names of those ceelebrities born before 1980:
for name, year in celebs:
	if name == "Brad Pitt":
		print("Brad Pitt isn't as young as I thought...")
	elif year < 1980:
		print("Old peep: " + name, year)


students = ["John", ["CompSci", "Physics"],
			["Vusi", ["Maths", "Stats", "Music"],
			["Jess", ["Econ", "English", "Art"],
			["Sarah", ["Piano", "Law", "Italian", "Linguistics"],
			["John", ["Sociology", "Stats", "Music"]
]

for name, subjects in students:
oiutr   		  

counter = 0
for name, subjects in students:
	if "CompSci" in subjects:
		counter += 1