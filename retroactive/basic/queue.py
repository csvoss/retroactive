## Simple, non-retroactive Queue implementation.

class Queue(object):
    def __init__(self, initstate=[]):
        self.list = initstate
    def front(self):
        if len(self.list) > 0:
            return self.list[0]
        else:
            return None
    def back(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
    def enqueue(self, val):
        self.list.append(val)
    def dequeue(self):
        return self.list.pop()
    def __str__(self):
        return self.list
