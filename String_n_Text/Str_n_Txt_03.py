'''
This program works with fnmatch() and fnmatchcase() methods. These two methods are very useful for string compraison with wildcard. If we need to use provide a simple solution to allow wildcards in data processing, this is a good way.
'''

from fnmatch import fnmatch, fnmatchcase

# Example 1
print (fnmatch('foo.txt', '*.txt'))
print (fnmatch('foo.txt', '?oo.txt'))
print (fnmatch('dat45.csv', 'dat[0-9][0-9]*'))
fileNames = ['fpyile.py', 'configfile.ini', 'DAT1.csv','DAT2.csv']
op = (name for name in fileNames if fnmatch(name, 'DAT[0-9]*'))
for item in op:
    print(item)
