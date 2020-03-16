values = [2, 3, 8]
result = []
for x in values:
	result.append(2.1 * x)
	print(result)


# Better way:
# Must install pip3 install numpy

import numpy as np

a = np.array([2, 3, 8])

rslt = 2.1 * a
squared = a * a

print(rslt)
print(squared)

a = np.array([5, 5])
print(a)
dotted = np.dot(a, a)
print(dotted)

# 5 * 5 = 25 
# 25 + 25 = 50 

a = np.array([5, 5, 5])
print(a)
dotted = np.dot(a, a)
print(dotted)