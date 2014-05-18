from utils import *
from full_retroactivity import *
from partial_retroactivity import *


def testPartiallyRetroactive():
    x = PartiallyRetroactive([1,2,3], 10)
    x.query()
    x.insertAgo(appendSix, 0)
    x.insertAgo(appendSix, 0)
    x.query()
    x.insertAgo(appendTen, 2)
    x.query()
    x.insertAgo(deleteFirst, 1)
    x.query()
    x.deleteAgo(2)
    x.query()

    def setKeyValue(k,v):
        def out(dic):
            dic[k] = v
            return dic
    x = PartiallyRetroactive({}, 10)
    x.query()


def testPartiallyRetroactiveQueue():
    x = PartiallyRetroactiveQueue()
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
    x.sums
    x.state
    x.insert(x.update(2,7))
    x.sums
    x.state
    x.delete(x.update(2,7))
    x.delete(x.update(2,7))
    x.sums
    x.state
    x.sum(3)
    x.search(0)
    x.search(1)
    x.search(2)
