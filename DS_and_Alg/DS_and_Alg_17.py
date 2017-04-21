

def rmdupfrmdict(items, key=None):
    for item in items:
        print (key(item))

b = [{'x':1,'y':2},{'x':1,'y':4},{'x':1,'y':2},{'x':2,'y':3}]
rmdupfrmdict(b, lambda d: (d['x'], d['y']))
