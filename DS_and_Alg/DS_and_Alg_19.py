'''
This program explains how we can transform and reduce
in an elegent way by using generator expression.
'''

#example 1
num = [1,2,3,4,5]
sumOfSqures = sum(x*x for x in num)
print (sumOfSqures)

#example 2
# import os
# dirName = 'c:\\temp'
# fileNames = os.listdir('dirName')
# if any(name.endswith('.py') for file in fileNames):
#     print ("There is a hidden Python")
# else:
#     print ("Its Safe")

#example 3
strList = ['This', 'is' 'python', 3, 'demo', ':', 'GENERATOR']
print(' '.join(str(x) for x in strList))
