'''
This file demonstrates the use of Decimal Module
'''
# Problem : If we add two Decimal numbers a noise is inserted.
a = 1.1
b = 4.2
print (a+b)

'''To fix this, we use Decimal module.
But please remember that it comes with a cost of performance'''
from decimal import Decimal
c = Decimal('1.1')
d = Decimal('4.2')
print(c+d)

'''Decimal module can also control diffrent aspect of calculation. Including precision. Please see below example'''
from decimal import localcontext
print(c/d)
with localcontext() as ctx:
    ctx.prec = 3
    print(c/d)
with localcontext() as ctx:
    ctx.prec = 1
    print(c/d)
