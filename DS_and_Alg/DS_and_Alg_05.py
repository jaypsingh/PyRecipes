import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    """This is the test class for priority uqeue implementation"""
    def __init__(self, item):
        self.item = item

    def __repr__(self):
        return 'Item({!r})'.format(self.item)
q = PriorityQueue()
q.push(Item('a'),4)
q.push(Item('s'), 1)
q.push(Item('y'), 3)
q.push(Item('p'), 2)
q.push(Item('jp'), 5)
q.push(Item('j'), 5)

#print (q._queue)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
