'''
This function demonstrates how can we search and replace strings, ignoring the case of the strings
'''
import re
myStr = "UPPER PYTHON, lower python, MiXeD Python"

def matchCase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

# Approach 1
print (re.sub('python', 'snake', myStr, flags = re.IGNORECASE))

# Approach 2 to make sure that the case remains as it were.
print (re.sub('python', matchCase('snake'), myStr, flags = re.IGNORECASE))
