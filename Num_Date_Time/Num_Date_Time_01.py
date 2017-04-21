# Round an numerical value
myInt = 1.12345
print(round(myInt, 1))
print(round(myInt, 2))
print(round(myInt, 3))
print(round(myInt, 4))

myInt2 = 12345
print(round(myInt2, -1))

# Fomatting is not rounding. here is formatting example
print ('myInt value is {:0.3f}'.format(myInt))

'''Also there is wiered thing that i will demo to you,  and you can figure out why this happens. '''
a = 2.1
b = 4.2
print(a+b)
