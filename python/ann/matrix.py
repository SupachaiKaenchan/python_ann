import copy, numpy as np
np.random.seed(0)
a = list()
a.append([1,2,3])
a.append([4,5,6])

b = list()
b.append([7,8])
b.append([9,10])
b.append([11,12])

print a
print b

c = np.dot(a,b)
print c
