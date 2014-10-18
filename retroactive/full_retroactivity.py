import copy

class GeneralFullyRetroactive(object):
    """
    Implements full retroactivity for a generic data structure.

    Does this by storing a sequence of versions of *partially* 
    retroactive data structures, plus some logging for the operations
    in between two such data structures in sequence.

    m :: int.
         The total number of retroactive updates that have been performed so far.

    Currently, this implementation does not achieve the sqrt(m) overhead.
    For that, we need an implementation of persistence.

    timeline :: a list of PartiallyRetroactive objects.
    timeline[0] --> the MOST recent PartiallyRetroactive object.
    """
    ## GeneralFullyRetroactive<X>

    def __init__(self, partiallyretro):
        """
        partiallyretro :: a PartiallyRetroactive data structure
        """
        self.m = 0
        state = partiallyretro
        self.timeline = [state]

    def insertAgo(self, operation, tminus=0):
        if tminus > len(self.timeline):
            tminus = len(self.timeline)
        states = self.timeline[:tminus]
        mid = copy.deepcopy(self.timeline[tminus])
        for i in range(len(states)):
            state = states[i]
            # if i==0, then insert at tminus
            # if i==tminus, then insert at 0
            state.insertAgo(operation,tminus-i)
        mid.insertAgo(operation, 0)
        self.timeline.insert(tminus, mid)

    def deleteAgo(self, tminus=0):
        if tminus > len(self.timeline):
            tminus = len(self.timeline)
        states = self.timeline[:tminus]
        for i in range(len(states)):
            state = states[i]
            # if i==0, then delete at tminus
            # if i==tminus, then delete at 0
            state.deleteAgo(tminus-i)
        del self.timeline[tminus]

    def query(self, tminus=0):
        return self.timeline[tminus].query()

    def __str__(self):
        return str([str(foo) for foo in self.timeline])
