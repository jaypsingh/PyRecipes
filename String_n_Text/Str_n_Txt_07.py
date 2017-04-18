'''
This program demonstrates how can we specify a regular expression to search shortest possible match.
By Default regular expression gives the longest possible match.
'''
import re
myStr = 'My heart says "no." but mind says "yes."'

# Problem demonstration
'''
Here we ar etrying to match a text inside a quote.
So i expect an answer as 'yes.' and 'no.'
Lets see what it returns.
'''
myProblemPat = re.compile(r'\"(.*)\"')
print (myProblemPat.findall(myStr))

# Python returns ['no." but mind says "yes.']

# Solution
'''
To fix this, we just need to add a ? after the *
This will force python to search in a non gready way.
'''

mySolutionPat = re.compile(r'\"(.*?)\"')
print (mySolutionPat.findall(myStr))
