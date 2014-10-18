from basic import PriorityQueue, Deque, Queue, UnionFind, Stack, SDPS
from full import RetroactiveDeque, RetroactiveUnionFind
from partial import GeneralPartiallyRetroactive, PartiallyRetroactivePriorityQueue, PartiallyRetroactiveQueue, PartiallyRetroactiveSDPS
from full_retroactivity import GeneralFullyRetroactive

def PartiallyRetroactive(initstate):
    """
    Determine which implementation should be applied,
    and delegate to the corresponding code.

    initstate :: simple, non-retroactive data structure
    """
    if isinstance(initstate, SDPS):
        return PartiallyRetroactiveSDPS()
    elif isinstance(initstate, Queue):
        return PartiallyRetroactiveQueue()
    elif isinstance(initstate, Deque):
        return FullyRetroactive(initstate)
    elif isinstance(initstate, Stack):
        return PartiallyRetroactive(Deque())
    elif isinstance(initstate, PriorityQueue):
        return PartiallyRetroactivePriorityQueue(initstate)
    elif isinstance(initstate, UnionFind):
        return FullyRetroactive(initstate)
    else:
        return GeneralPartiallyRetroactive(initstate)

def FullyRetroactive(initstate):
    """
    Determine which implementation should be applied,
    and delegate to the corresponding code.

    initstate :: simple, non-retroactive data structure
    """
    if isinstance(initstate, SDPS):
        return GeneralFullyRetroactive(PartiallyRetroactive(initstate))
    elif isinstance(initstate, Deque):
        return RetroactiveDeque(initstate)
    elif isinstance(initstate, Queue):
        return FullyRetroactive(Deque())
    elif isinstance(initstate, Stack):
        return FullyRetroactive(Deque())
    elif isinstance(initstate, PriorityQueue):
        return GeneralFullyRetroactive(PartiallyRetroactive(initstate))
    elif isinstance(initstate, UnionFind):
        return RetroactiveUnionFind(initstate)
    else:
        return GeneralFullyRetroactive(PartiallyRetroactive(initstate))
