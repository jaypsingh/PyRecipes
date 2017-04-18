'''
This program demonstrates how we can use Regular expression for multiline patterns.
Usually when a pattern uses a . to match a sequence of charcters (sometimes) it forgets to consider that the text can be scatterd in multiple line.
'''

import re

srchText = '''/* This is line 1 of a multiline comment
This is line 2 of a multiline comment
This is line 3 of a multiline comment. */
'''

# Problem demonstration
'''We expect to get the text between /* and */ but instead we get back noting '''
reExPat_Problem = re.compile(r'/\*(.*?)\*/')
print (reExPat_Problem.findall(srchText))

#Solution
'''To fix this, we need to update our reg ex pattern'''
reExPat_Solution = re.compile(r'/\*((?:.|\n)*?)\*/')
print (reExPat_Solution.findall(srchText))


#Solution 2
'''Oher option is to use the flag re.DOTALL, demoed below.
It will match all the reg ex without worrying about the newline. This solution too works well. But the limitation is that it might fail for complex pattern. And it is suggested to define your own reg ex which is guranteed to work instead of using additional flag'''
reExPat_Alternate_Solution = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print (reExPat_Alternate_Solution.findall(srchText))
