'''
One extremly useful function of numpy array is the manner in which we can extend python array's indexing ability.
'''

import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# Print complete array
print (a)

#Print row 1
print(a[1])
print("--------------------------------------")
# print column 1
print(a[:,1])
print("--------------------------------------")
# Print a subregion
print(a[1:3,1:3])
print("--------------------------------------")
# Select a subregion and change it
print(a[1:3,1:3]+10)
print("--------------------------------------")
# Broadcast a row vector to do operation on all row.
print(a+[101,102,103,104])
print
# Conditional assignment on an array
print (np.where(a<10),a,10)
