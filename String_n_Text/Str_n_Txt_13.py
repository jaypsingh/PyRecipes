'''
This program demonstrates diffrent ways of formating strings
'''
# Approach 1
myStr = 'Aling Test Demo'
print ('----------Using ljust rjust and center--------------')
print(myStr.ljust(20))
print(myStr.rjust(20))
print(myStr.center(20))

# Approach 1a if you wanna pad some chars
print ('----------Using padding in above approach--------------')
print(myStr.ljust(20, '*'))
print(myStr.rjust(20, '#'))
print(myStr.center(20, '='))

#Approach 2
print ('----------Using Format--------------')
print(format(myStr,'>20'))
print(format(myStr,'<20'))
print(format(myStr,'^20'))

#Approach 2
print ('----------Using padding in Format--------------')
print(format(myStr,'*>20'))
print(format(myStr,'#<20'))
print(format(myStr,'=^20'))
