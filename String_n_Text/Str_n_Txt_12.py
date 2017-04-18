'''
This program demonstrates cleaning up some text from a file or some other source.
While we can always use str.replace(), i also want to demo another way of doing that using str.translate()
'''

def cleanStr(myStr):
    myStr = myStr.replace('\t', ' ')
    myStr = myStr.replace('\f', ' ')
    myStr = myStr.replace('\r', ' ')
    myStr = myStr.replace('\n', ' ')
    return myStr

exampleStr = 'This\tis\fa\rstring\n'
mapStr = {ord('\t'):' ',
ord('\f'):' ',
ord('\r'):' ',
ord('\n'):' '}

print(exampleStr)

#Old Approach
print (cleanStr(exampleStr))

#New approach
print(exampleStr.translate(mapStr))
