'''
This program addresses a common problem when we need to match at the start and end of a string.
A simple way of doing that would be using str.startswith() and str.endswith() demo
'''
# Example #1
myStr = "ThisIsAFile.txt"
print(myStr.startswith('file'))
print(myStr.endswith('txt'))

#Example #2
myList = ['classFile.h', 'classFile.py', 'classFile.c', 'methodFile.h', 'methodFile.py', 'methodFile.c']

classList = [name for name in myList if name.startswith('class')]
ptFileList = [name for name in myList if name.endswith('.py')]
print (classList)
print (ptFileList)
