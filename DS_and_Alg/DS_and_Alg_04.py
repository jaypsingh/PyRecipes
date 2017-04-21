'''This program demos how to get N number of elements
out of list in diffrent ways.'''

import heapq
import random
testList = []
#Build a testList of 100 items.
for i in range(100):
    testList.append(random.randint(1,999))
print (testList)

# Approach 1
# This approach can we taken when N is a large chunk of list.
# N Larget Number, where N=4
print(sorted(testList)[-80:])
# N Samllest Number, where N=4
print(sorted(testList)[:91])

# Approach 2
#'This approach can we taken when you really need only Max or Min.
# Max
print(max(testList))
# Min
print(min(testList))

# Approach 3
# This approach can we taken when when
# you need N elemets out of the List. Here N=3
# nlargest
print(heapq.nlargest(3,testList))
# nSmallest
print(heapq.nsmallest(3,testList))
