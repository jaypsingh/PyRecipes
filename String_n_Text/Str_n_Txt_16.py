'''
This program demonstrates how an we wrap text in python.
This is a simple demonstration of textwrap() method.
'''
import textwrap

myStr = "We take a chance from time to time, And put our necks out on the line, And you have broken every promise that we made, And I have loved you anyway, Took a fine time to leave me hangin out to dry, Understand now I m greivin, So dont you waste my time, Cause you have taken, All the wind out from my sails, And I have loved you just the same, And you have broken every single fucking rule, And I have loved you like a fool"


print(textwrap.fill(myStr, 70))
print('---------------------------')
print(textwrap.fill(myStr, 40))
print('---------------------------')
print(textwrap.fill(myStr, 40, initial_indent='     '))
print('---------------------------')
print(textwrap.fill(myStr, 40, subsequent_indent='     '))

#Side Note : To get terminal Size
import os
tSize = os.get_terminal_size().columns
print (tSize)
