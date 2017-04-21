'''
infinity and not a number demo
'''
import math
#Python has no special syntax to represent these special floating-point values,
# but they can be created using float(). For example:
a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
print(b)
print(c)
print(math.isinf(a))
print(math.isnan(c))
