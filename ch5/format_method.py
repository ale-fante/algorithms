phrase = "His name is {0}!".format("Alejandra")
print(phrase)

name = "Martha"
age = 10
phrase = "I am {1} and I am {0} years old".format(age, name)
print(phrase)

x = 4
y = 5
phrase = "2 ** 10 = {0} and {1} * {2} = {3:f}".format(2**10, x, y, x * y)
print(phrase)

# format specification is always introduced by the : symbol.
# This modifies how the substitutions are made into the template, and control things like:
# Whether thee field is aligned to the left, centeer or right
# The width allocateed to the field within the reesult string(a number like 10)
# the type of convention like {3:f} for float
# if the type conversion is a float, you can also specify how many decimal places are wanted.

name1 = "Paris"
name2 = "Whitney"
name3 = "Hilton"

print("Pi to three decimal places is {0:.3f}".format(3.1415926))
print("123456789 123456789 123456789 123456789 123456789 123456789")
print("||| {0:<15} ||| {1:^15} ||| {2:>15} ||| Born in {3} |||".format(name1, name2, name3, 1984))
print("The decimal value {0} converts to hex value {0:x}".format(123456))