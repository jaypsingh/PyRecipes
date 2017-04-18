'''
This program demonstrates how we can split a string with
multiple deliminators in Python.
This program uses re.split() method instead of standard str.split()
'''
import re
myStr= "This, is a     test;                 :String"

# str.split() demo.
print(myStr.split(" "))

# re.split() demo.
print(re.split((r'[,;:\s]\s*'), myStr))
