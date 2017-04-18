'''
This program demonstrates diffrent ways of comining or concaenating strings
'''

strLst = ['all', 'fries', 'are', 'not', 'fish']
mixStrList = ['sharp', 'between', 12.00, 'and', 12.5]

# Approach 1
print('-------------Approach 1: using join----------------')
print(' '.join(strLst))
# if you wanna add deliminetor
print(', '.join(strLst))
# joining strings of muxed type
# if you wanna add deliminetor
print(' '.join(str(item) for item in mixStrList))

# Approach 2 using '+' operator
print('-------------Approach 2: using +----------------')
a = 'all'
b = 'fries'
c = 'are'
d = 'not'
e = 'fish'
print (a+' '+b+' '+c+' '+d+' '+e+'.')

# Approach 3 using format
print('-------------Approach 3: using format----------------')
print('{} {} {} {} {}'.format(a,b,c,d,e))
