# tuple assignment

# Tuple packing
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

# Tuple unpacking
(name, surname, year_born, movie, year_movie, profession, birthplace) = julia

print(julia)
print(name)
print(surname)

a = "ALE"
b = "HOLA"

(a, b) = (b, a)

print(b)

import math

def circle_stats(r):
	""" Return (Circumference, area) of a circle of radius r """
	circumference = 2 * math.pi * r
	area = math.pi * r * r
	return (circumference, area)

print(circle_stats(12))