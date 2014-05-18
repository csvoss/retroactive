import copy
from utils import *




  #####                                            
 #     # ###### #    # ###### #####    ##   #      
 #       #      ##   # #      #    #  #  #  #      
 #  #### #####  # #  # #####  #    # #    # #      
 #     # #      #  # # #      #####  ###### #      
 #     # #      #   ## #      #   #  #    # #      
  #####  ###### #    # ###### #    # #    # ###### 


class PartiallyRetroactive(object):
    """
    Use the rollback method to implement retroactivity. Uses logging;
    stores, as auxiliary information, all changes to the data structure
    made by each operation, so that every change could be REVERSED. 

    If operations take T(n) time, this supports those operations in O(T(n))
    time, and supports retroactive versions of those operations in O(rT(n))
    time.
    """
    ## PartiallyRetroactive<X>

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





######                                            
#     # #  ####  ##### #    #   ##   #####  #   # 
#     # # #    #   #   ##   #  #  #  #    #  # #  
#     # # #        #   # #  # #    # #    #   #   
#     # # #        #   #  # # ###### #####    #   
#     # # #    #   #   #   ## #    # #   #    #   
######  #  ####    #   #    # #    # #    #   #   

#TODO                                              
class PartiallyRetroactiveDictionary(object):
    ## Rephrase it as a searching problem!
    ## pg 11 of TALG
    
    ## Requires segment tree implementation.

    ## Also, it is unclear to me how a dictionary can be represented
    ## as a decomposable search problem...


    pass





 #####  ######  ######   #####  
#     # #     # #     # #     # 
#       #     # #     # #       
 #####  #     # ######   #####  
      # #     # #             # 
#     # #     # #       #     # 
 #####  ######  #        #####  


## SearchableDynamicPartialSums

class PartiallyRetroactiveSDPS(object):
    def __init__(self, state=[]):
        self.state = state
        self.sums = [sum(state[:i]) for i in range(len(state))]
    
    def update(self, i, c):
        def return_update(x):
            x.state[i] += c
            for j in range(i,len(x.state)):
                x.sums[j] += c
            return x
        return_update.c = c
        return_update.i = i
        return return_update

    def insert(self, operation):
        assert operation.__name__ == 'return_update'
        self = operation(self)
    
    def delete(self, operation):
        assert operation.__name__ == 'return_update'
        inverse_operation = self.update(operation.i, -operation.c)
        assert inverse_operation.__name__ == 'return_update'
        self = inverse_operation(self)

    def sum(self, i):
        """
        Returns the sum of the first i elements of the array.
        """
        return self.sums[i]

    def search(self, j):
        """
        Returns the SMALLEST i such that sum(i) >= j.
        """
        for i in range(len(self.sums)):
            if self.sum(i) >= j:
                return i




######                                        #####  
#     # #####  #  ####  #####  # ##### #   # #     # 
#     # #    # # #    # #    # #   #    # #  #     # 
######  #    # # #    # #    # #   #     #   #     # 
#       #####  # #    # #####  #   #     #   #   # # 
#       #   #  # #    # #   #  #   #     #   #    #  
#       #    # #  ####  #    # #   #     #    #### # 
                                                                                                                                 
class PartiallyRetroactivePriorityQueue(object):
    pass










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


 #####                              
#     # #    # ###### #    # ###### 
#     # #    # #      #    # #      
#     # #    # #####  #    # #####  
#   # # #    # #      #    # #      
#    #  #    # #      #    # #      
 #### #  ####  ######  ####  ###### 
                                                
class DLLNodeForPRQ(object):
    def __init__(self, prev, next, val=None):
        self.prev = prev
        self.next = next
        self.val = val
        self.isBeforeF = False

class PartiallyRetroactiveQueue(object):
    def __init__(self):
        self.init = False
        self.B = None
        self.F = None

    def front(self):
        if self.F != None:
            return self.F.val
        else:
            return None

    def back(self):
        if self.B != None:
            return self.B.val
        else:
            return None

    def insertEnqueue(self, val, tPtr=None):
        """
        val :: data
        tPtr :: represents the operation that occurs just AFTER
                the time when you want to insert this enqueue at.
        return :: a tPtr for this enqueue, for possible future use.
            a tuple: first element -- pointer to new node in list
                     second element -- whether or not the operation
                                       was an enqueue operation
        """

        if not self.init:
            node = DLLNodeForPRQ(None, None, val)
            self.B = node
            self.F = node
            node.isBeforeF = True
            self.init = True
            return (node, True)
        
        if tPtr == None:
            ## insert at t=now
            ## --> enqueue at back of list
            ## create a new node
            node = DLLNodeForPRQ(self.B, None, val)
            ## update its surroundings
            self.B.next = node
            ## update B
            self.B = node
            return (node, True)

        else:
            ## unpack tPtr
            tPtr, isEnq = tPtr
            ## create a new node
            ## insert the new node just prev to tPtr
            node = DLLNodeForPRQ(tPtr.prev, tPtr, val)
            ## update its surroundings
            if tPtr.prev != None:
                tPtr.prev.next = node
            tPtr.prev = node
            ## update F if relevant
            if tPtr.isBeforeF:
                self.F.isBeforeF = False
                self.F = self.F.prev
            return (node, True)

    def insertDequeue(self, tPtr=None):
        ## same procedure, retroactive or not
        ## --> tPtr does not matter
        self.F = self.F.next
        self.F.isBeforeF = True
        return (self.F, False)

    def delete(self, tPtr):
        ## unpack tPtr
        tPtr, isEnq = tPtr
        if isEnq:
            ## removing an enqueue
            ## delete it from the list
            if tPtr.next != None:
                tPtr.next.prev = tPtr.prev
            else:
                ## next is none -- so B needs to be updated,
                ## since this is the back and we're deleting it
                self.B = tPtr.prev
            if tPtr.prev != None:
                tPtr.prev.next = tPtr.next

            if tPtr.isBeforeF:
                self.F = self.F.next
                self.F.isBeforeF = True
        else:
            ## removing a dequeue
            self.F.isBeforeF = False
            self.F = self.F.prev

        return None


    def __str__(self):
        out = []
        ptr = self.B
        while ptr != None:
            out = out + [ptr.val]
            if ptr == self.F:
                break
            ptr = ptr.prev
        return "Front=%s, Back=%s, State=%s"%(self.front(), self.back(), str(out))

