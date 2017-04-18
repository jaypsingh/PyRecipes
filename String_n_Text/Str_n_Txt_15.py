'''
This program demostrate an intresting way to interpolate variable names
This is very hepful when you want to create a string in which variable names are substituted with a string representation of thevariable value.
'''

# This can be done using format() method
myStr = '{myName} is a {gender}'
print(myStr.format(myName='Jay', gender='Male'))

# Alternate way is to use format_map() and vars() method
myName = 'Batman'
gender = 'Male'
print(myStr.format_map(vars()))

# Good things about vars is that it can be used with class instance too.

class Identity(object):
    def __init__(self, myName, gender):
        self.myName = myName
        self.gender = gender
myObj = Identity('WonderWoman', 'Female')
print(myStr.format_map(vars(myObj)))

# To avoide the exception due to missing variable a wrapper can be used as below.

class safesub(dict):
    def __missing__(self, key):
        return('{'+key+'}')
del gender
print(myStr.format_map(safesub(vars())))


# Overall Solution
import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
#del myName
myName = "BatMan"
myGender = "Awesomee"
print(sub('Hi {myName}'))
print(sub('You are {myGender}'))
print(sub('Your real name is {realName}'))

# CAUTION : Alternate way.. this are old ways of doing things and NOT A SUGGESTED WAY
import string
realName = 'Peter'
charName = 'SpiderMan'
myStr = string.Template('$realName is $charName')
print(myStr.substitute(vars()))
