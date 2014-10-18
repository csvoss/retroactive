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

