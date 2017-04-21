# file name : ComparingDict.py
'''purpose of this short program is to demo how we
compare values or keys in dictionary'''

aDict = {'a':1,
'b':2,
'c':3}

xDict = {'x':10,
'y':2,
'c':30}

print (aDict.keys() & xDict.keys())
print (aDict.items() & xDict.items())

# Say if you wanna a new dict with the filters
ax = {key:aDict[key] for key in aDict.keys() - {'c'}}
print (ax)
