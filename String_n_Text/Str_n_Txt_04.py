'''
This program demonstrates matching and searching the text pattern. Here we use regular expressions, nothing fancy, but since we are on the topic of strings lets review this too.
'''
import re
text1 = '03/09/2017'
text2 = 'Mar-09-2017'
rePattern = re.compile(r'\d+/\d+/\d+')
if rePattern.match(text1):
    print('Yes')
else:
    print('No')

# Use findall methos to search all the instances.
testStr = "Today is 03/09/2016. Game of Thrones starts 21/07/2017"
m = rePattern.findall(testStr)
print (m)

#Extracting the group from a mattched patterm
grpPatern = re.compile(r'(\d+)/(\d+)/(\d+)')
grpDemo = grpPatern.match('21/07/2017')
print (grpDemo)
print(grpDemo.group(0))
print(grpDemo.group(1))
print(grpDemo.group(2))
print(grpDemo.group(3))

mm, dd, yyyy = grpDemo.groups()
