class DLLNodeForPRPQ(object):
    def __init__(self, prev, next, val=None):
        self.prev = prev
        self.next = next
        self.val = val

class PartiallyRetroactivePriorityQueue(object):

    ## TODO.
    ## Requires an implementation of modified (a,b)-tree of Fleischer.

    def __init__(self, initstate):
        """
        initstate :: a list of comparable items, initially in the priority queue
        """
        raise NotImplementedError()
        

        self.history = None ##doubly linked list
        self.Qnow ## = a new BST
            #associating with each key a pointer to its insert operation in the linked list (history)


        # After each update: ins/del element in Qnow according to rules.
        #Must be able to:
            #find last bridge before t or first bridge after t
            #find max key in I_{>=t'} - Qnow or the min key in I_{<=t'} INTERSECT Qnow
        #Assign weight of 0 to ins(k) operations with k \in Qnow
        #Assign weight of 1 to ins(k) with k \not \in Qnow
        #Assign weight of -1 to delete-min()
        #--> ea bridge corresp to pref with sum 0
        #Maintain list of insertions augmented by (a,b) tree...

