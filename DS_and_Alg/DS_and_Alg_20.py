'''
This program demonstrates how we can combine the
mapping of two dictinory without actually combinig them.
'''
from collections import ChainMap
dictCaps = {'A':1,'B':2,'C':3}
dictSmall = {'a':1,'b':2,'c':3}
newDict = ChainMap(dictCaps, dictSmall)
print (newDict['a'])
print (newDict)
