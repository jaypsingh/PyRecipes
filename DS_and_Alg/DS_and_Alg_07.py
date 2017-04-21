from collections import OrderedDict

#Notes
'''Useful if we need the dictionary to main the order of inputs.
Internally the order is maintained by doubly linked list.
Size of OrderedDict is more than twice large from normal dict'''

#Example
od = OrderedDict()
od['j']=1
od['a']=2
od['y']=3
for key in od:
    print (key, od[key])
