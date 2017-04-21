'''
Working with Complex Number
'''
# represent complex Number
cNum1 = complex(2,3)
cNum2 = 4+5j
print(cNum1)
print(cNum2)

print(cNum1.real)
print(cNum1.imag)
print(cNum1.conjugate())

#Regular Math Operation
print(cNum1 + cNum2)
print(cNum2 - cNum1)

# Complex sin cos operation can be done using cmath module
import cmath
print(cmath.sin(cNum1))
print(cmath.cos(cNum1))
print(cmath.exp(cNum1))
