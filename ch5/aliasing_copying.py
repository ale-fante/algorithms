opposites = {
	"up" : "down",
	"right" : "left",
	"yes" : "no"
}

alias = opposites
copy = opposites.copy()

alias["right"] = "left"
print(opposites["right"])
copy["right"] = "privilege"

print("COPY")
print(copy)

print("ALIAS")
print(alias)
