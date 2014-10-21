class DLLNodeForPRQ(object):
    def __init__(self, prev, next, val=None):
        self.prev = prev
        self.next = next
        self.val = val
        self.isBeforeF = False

class TimePointer(object):
    def __init__(self, pointer, wasEnqueue):
        """
        a tuple: first element -- pointer to new node in list
                 second element -- whether or not the operation
                                   was an enqueue operation
        """
        self.pointer = pointer
        self.wasEnqueue = wasEnqueue

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

    def insertEnqueue(self, val, before=None):
        """
        val :: data
        before :: TimePointer.
                  Represents the operation that occurs just AFTER
                  the time when you want to insert this enqueue at.
                  That is, you're inserting this operation BEFORe that one.
        return :: TimePointer. For this enqueue, for possible future use.
        """
        if before is not None:
            assert isinstance(before, TimePointer)

        if not self.init:
            node = DLLNodeForPRQ(None, None, val)
            self.B = node
            self.F = node
            node.isBeforeF = True
            self.init = True
            return TimePointer(node, True)
        
        if before == None:
            ## insert at t=now
            ## --> enqueue at back of list
            ## create a new node
            node = DLLNodeForPRQ(self.B, None, val)
            ## update its surroundings
            self.B.next = node
            ## update B
            self.B = node
            return TimePointer(node, True)

        else:
            ## unpack tPtr
            tPtr = before.pointer
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
            return TimePointer(node, True)

    def insertDequeue(self, before=None):
        ## same procedure, retroactive or not
        ## --> tPtr does not matter
        if before is not None:
            assert isinstance(before, TimePointer)
            
        if self.F is None and self.B is None:
            self.init = False
            return TimePointer(self.F, False)
            

        self.F = self.F.next
        if self.F is not None:
            self.F.isBeforeF = True
        else:
            self.B = None
            self.init = False
        return TimePointer(self.F, False)

    def delete(self, time):
        """
        Delete the retroactive operation at `time`.
        time :: TimePointer.
        """
        ## unpack tPtr
        tPtr, isEnq = (time.pointer, time.wasEnqueue)
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

