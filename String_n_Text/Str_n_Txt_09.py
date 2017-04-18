'''
This program demonstrates how we can normalize unicode strings.
'''
import unicodedata

s1 = "Spicey Jalape\u00f1o"
s2 = "Spicey Jalapen\u0303o"

# Problem demonstration
print (s1)
# Uncommening the below line will give encoding error. Hence it is commented.
# print (s2)
print (s1==s2)
print (len(s1))
print (len(s2))

# Solution
''' If we normalize the strings before we use it it solves the problem.'''
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print (t1==t2)
print (ascii(t1))
print (t1)

# Alternate Solution
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print (t3==t4)
print (ascii(t3))
# Uncommening the below line will give encoding error. Hence it is commented.
# print (t3)
