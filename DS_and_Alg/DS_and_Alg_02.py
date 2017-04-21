'''
Say you have to filter all the numbers tha are greater than 'x' in a list.
'''
myList = [2,46,12,71,11,81,62,15,31,63,2,49,9,6,55,12,43,54,56,65,89,0]
newList = [n for n in myList if n<50]
print (newList)

'''
What if output list is very big.
Instead we can use the generater object.
'''
myList = [2,46,12,71,11,81,62,15,31,63,2,49,9,6,55,12,43,54,56,65,89,0]
newList = (n for n in myList if n<50)
print (newList)
for item in newList:
    print(item)

'''
No what if the criteria of filter is complex.
We can always use an inbuild method filter.
'''
def is_Int(value):
    try:
        x = int(value)
        return True
    except Exception as e:
        return False

myList = ['a', 2,46,71,15,63,49,6,55,12,43,54,56,65,89,0,'x']
newList = list(filter(is_Int, myList))
print (newList)
