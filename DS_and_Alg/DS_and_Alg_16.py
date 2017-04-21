'''
This short program shows a demo of how we can
filter and compress sequence items.
ittertools.compress() takes a sequence and accompanying
boolean selector as input and returns a compressed list
as output.
'''

from itertools import compress
count= [2,1,5,7,9,0]
flatNo = ['A-102','B-321','C-211','D-111','E-008','F-321']

newList = [n < 5 for n in count]
output = list(compress(flatNo, newList))
print(output)
