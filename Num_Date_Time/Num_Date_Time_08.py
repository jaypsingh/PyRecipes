'''
This is a simple recipie to demo how we can display fraction in python
'''
from fractions import Fraction
a = Fraction(8, 7)
b = Fraction(3, 14)

print(a*b)
print(a/b)
print (a+b)
print(a.numerator)
print(a.denominator)

#converting a fraction to a float
print(float(a/b))
