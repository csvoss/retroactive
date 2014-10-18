import copy

def compose(f, g):
    ## Return a function which passes its inputs first
    ## through f, then through g
    return lambda x: g(f(x))

def operate(init, functions):
        return reduce(compose, functions, lambda starter: init)("starter")

class GeneralPartiallyRetroactive(object):
    """
    Use the rollback method to implement retroactivity. Uses logging;
    stores, as auxiliary information, all changes to the data structure
    made by each operation, so that every change could be REVERSED. 

    If operations take T(n) time, this supports those operations in O(T(n))
    time, and supports retroactive versions of those operations in O(rT(n))
    time.
    """
    ## GeneralPartiallyRetroactive<X>

    def __init__(self, initstate, r=float('inf')):
        """
        Initialize the retroactive datastructure.
        initstate :: X
            The initial state of the datastructure. Can be *whatever
            type you want*! Just make sure that your operations use that
            type as input + output.
        r :: int
            This parameter determines how far back of a history the
            retroactive datastructure maintains. 

        operations :: a timeline of operations.
        operations[0] :: the MOST recent operation.
        currstate :: the current state of the retroactive data structure.
        """
        self.paststate = initstate
        self.r = r
        self.operations = []
        self.currstate = initstate

    def query(self):
        return self.currstate

    def insertAgo(self, operation, tminus=0):
        """
        Insert 'operation' BEFORE the previous 'tminus' operations.
        operation :: X -> X
            It's okay if it modifies the datastructure,
            so long as it RETURNS the output of the modification.
        tminus :: int
        """
        if tminus > len(self.operations):
            tminus = len(self.operations)
        self.operations.insert(tminus, operation)
        self._refresh()

    def deleteAgo(self, tminus=0):
        """
        Delete the operation 'tminus' operations ago.
        tminus :: int
        Zero-indexed. The 0th operation is the most recent one.
        """
        if tminus > len(self.operations):
            tminus = len(self.operations)
        del self.operations[tminus]
        self._refresh()

    def _refresh(self):
        ## Refresh currstate from paststate + operations.
        tempstate = copy.deepcopy(self.paststate)
        self.currstate = operate(tempstate, reversed(self.operations))

        ## If the number of operations is too long...
        ## reduce it down to r previous operations
        if len(self.operations) > self.r:
            pre = self.operations[:self.r]
            post = self.operations[self.r:]
            tempstate = copy.deepcopy(self.paststate)
            self.paststate = operate(tempstate, reversed(pre))
            self.operations = post

    def __str__(self):
        return str(self.currstate)

