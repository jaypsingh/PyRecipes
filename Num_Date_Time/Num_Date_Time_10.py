'''
This is a demonstration of how we can perform linear algebra and matrix operations in python.
for more please refer online documentation.
More packages are also found in numpy.linalg subpackage.
'''

# here we are using matrix objects from Numpy library.
# matrix are similar to arrays, but it follows linear algebra computation rule.
# here is an eample.

import numpy as np
m = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print(m)
#===> Transpose
print(m.T)
#===> Inverse
print(m.I)
#===> Create vector and multiply
v = np.matrix([[7,2,6]])
print(v*m)
