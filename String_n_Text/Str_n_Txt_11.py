'''
This program demonstrates stripping of unwanted charcters from a string
Stripping can be done from the begining or end.
'''

exampleStr = '    Hello   world \n  '
print(exampleStr.lstrip())
print(exampleStr.rstrip())
print(exampleStr.strip())

'''
Please note that the strip, lstrip and rstrip method
can also take arguments for charcter stripping.
Please see below example.
'''
myStr = '------------------myStr================'
print(myStr.strip('-'))
print(myStr.strip('='))
