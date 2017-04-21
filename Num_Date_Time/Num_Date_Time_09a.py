'''
For any heavy computation using lists use numpy.
It gives python an array object that is much more suited for mathmetical calculations.
'''

x = [1,2,3,4]
y = [5,6,7,8]

# Traditional way
print (x*2)
#print(x+10) # this statement will generate error
print(x+y)

# Numpy way
import numpy as np
ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])
print(ax*2)
print(ax+10)
print(np.sqrt(ax))
print(np.cos(ax))

# More Complexx Exaple
grid = np.zeros(shape=(1000,1000), dtype=float)
print(grid)
grid = grid+10
print(grid)
