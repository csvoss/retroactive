from full import *
from partial import *
from basic import *
from dispatcher import PartiallyRetroactive, FullyRetroactive

def appendSix(lst):
    return lst + [6]
def appendOne(lst):
    return lst + [1]
def appendTen(lst):
    return lst + [10]
def deleteFirst(lst):
    del lst[0]
    return lst



def testGeneralPartiallyRetroactive():
    x = GeneralPartiallyRetroactive([1,2,3], 10)
    print x.query()
    x.insertAgo(appendSix, 0)
    x.insertAgo(appendSix, 0)
    print x.query()
    x.insertAgo(appendTen, 2)
    print x.query()
    x.insertAgo(deleteFirst, 1)
    print x.query()
    x.deleteAgo(2)
    print x.query()


def testPartiallyRetroactiveQueue():
    x = PartiallyRetroactive(Queue())
    ## INSERT the enqueueing of some things
    r = x.insertEnqueue(42)
    s = x.insertEnqueue(43)
    t = x.insertEnqueue(44)
    print x

    ## INSERT a enqueue of 1 BEFORE the enqueueing of 43
    u = x.insertEnqueue(1, s)
    print x

    ## INSERT a dequeue BEFORE the enqueueing of 44
    v = x.insertDequeue(t)
    print x

    ## DELETE the dequeue
    w = x.delete(v)
    print x

    ## DELETE the enqueue of 42
    y = x.delete(r)
    print x


def testPartiallyRetroactiveSDPS():
    x = PartiallyRetroactiveSDPS([1,2,3,4,5])
    print x.sums
    assert x.sums == [0,1,3,6,10]
    print x.state
    assert x.state == [1,2,3,4,5]
    x.insert(lambda i: i.update(2,7)) ## Add 7 to the second element
    print x.sums
    assert x.sums == [0,1,10,13,17]
    print x.state
    assert x.state == [1,2,10,4,5]
    x.delete(lambda i: i.update(2,7)) ## Delete the addition of 7
    print x.sums
    assert x.sums == [0,1,3,6,10]
    print x.state
    assert x.state == [1,2,3,4,5]

def all_tests():
    testPartiallyRetroactiveSDPS()
    testPartiallyRetroactiveQueue()
    testGeneralPartiallyRetroactive()
