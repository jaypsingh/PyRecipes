'''
This function demonstrates how can we search and replace strings
'''

import re

myStr = "Today is 03/09/2016. Game of Thrones starts 21/07/2017"

# Simple replace using str.replace()
print (myStr.replace('Today', 'Tomorrow'))

# Replace using re.sub() - Approach 1
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3\-2\-1', myStr))

# Replace using re.sub() - Approach 2
newStr = re.compile(r'(\d+)/(\d+)/(\d+)')
print(newStr.sub(r'\3\-2\-1', myStr))
