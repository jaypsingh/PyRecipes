def rmdupfrmlst(items):
    uniqLst = set()
    for item in items:
        if item not in uniqLst:
            yield item
            uniqLst.add(item)

def rmdupfrmdict(items, key=None):
    uniqLst = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in uniqLst:
            yield item
            uniqLst.add(val)
a = [1,5,2,1,9,1,5,10]
print (list(rmdupfrmlst(a)))

b = [{'x':1,'y':2},{'x':1,'y':4},{'x':1,'y':2},{'x':2,'y':3}]
c = list(rmdupfrmdict(b, lambda d: (d['x'], d['y'])))
print(c)


'''
How the above code will work is explained below:
def rmdupfrmdict(items, key=None):
    for item in items:
        print (key(item))

b = [{'x':1,'y':2},{'x':1,'y':4},{'x':1,'y':2},{'x':2,'y':3}]
rmdupfrmdict(b, lambda d: (d['x'], d['y']))
'''
