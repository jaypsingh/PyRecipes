
'''
This program demonstrates how we can group dict item by its keys using itemgetter and groupby methods.
'''
myDict = [
{'show':'office','actor':'steve','char':'michel'},
{'show':'office','actor':'rainn','char':'dwight'},
{'show':'office','actor':'john','char':'jim'},
{'show':'GOT','actor':'peter','char':'tyrion'},
{'show':'GOT','actor':'lena','char':'cersi'},
{'show':'GOT','actor':'rose','char':'ygritte'},
{'show':'gotham','actor':'robin','char':'penguin'},
{'show':'gotham','actor':'ben','char':'james'},
{'show':'gotham','actor':'sean','char':'alferd'}
]
from operator import itemgetter
from itertools import groupby
myDict.sort(key=itemgetter('show'))
for actor, show in groupby(myDict, key=itemgetter('show')):
    print(actor)
    for i in show:
        print('     ', i)
