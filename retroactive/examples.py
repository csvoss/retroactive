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

def testFullyRetroActiveUnionFind():
    x = RetroactiveUnionFind()
    # union a and b at the current time
    x.unionAgo('a','b')
    assert x.sameSetAgo('a', 'b', -2) == False

    # union a and b two steps earlier
    x.unionAgo('a', 'b' ,-2)
    assert x.sameSetAgo('a', 'b', -3) == True

    x.unionAgo('c','d')
    assert x.sameSetAgo('b', 'd') == False

    # union a and c before all other unions
    x.unionAgo('a','c',-10)
    assert  x.sameSetAgo('b', 'd',-9) == False
    assert  x.sameSetAgo('b','d', 0) == True

def all_tests():
    testPartiallyRetroactiveSDPS()
    testPartiallyRetroactiveQueue()
    testGeneralPartiallyRetroactive()
    testFullyRetroActiveUnionFind()

all_tests()