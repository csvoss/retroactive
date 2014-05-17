import copy

                                                                 

## partial retroactivity: view in present, modify anywhere
## full retroactivity: view anywhere, modify anywhere

## m = TOTAL # updates performed
## r = how retroactive-ago the update is
## n = MAX # elements in structure





 ######                                   
 #     # ###### ##### #####   ####        
 #     # #        #   #    # #    #       
 ######  #####    #   #    # #    # ##### 
 #   #   #        #   #####  #    #       
 #    #  #        #   #   #  #    #       
 #     # ######   #   #    #  ####        
                                          
                                          
   ##    ####  ##### # #    # ######      
  #  #  #    #   #   # #    # #           
 #    # #        #   # #    # #####       
 ###### #        #   # #    # #           
 #    # #    #   #   #  #  #  #           
 #    #  ####    #   #   ##   ######      

 ######
 #     #   ##   #####   ##
 #     #  #  #    #    #  #
 #     # #    #   #   #    #
 #     # ######   #   ######
 #     # #    #   #   #    #
 ######  #    #   #   #    #

  #####      
 #     # ##### #####  #    #  ####
 #         #   #    # #    # #    #
  #####    #   #    # #    # #
       #   #   #####  #    # #
 #     #   #   #   #  #    # #    #
  #####    #   #    #  ####   ####


 ##### #    # #####  ######  ####
   #   #    # #    # #      #
   #   #    # #    # #####   ####
   #   #    # #####  #           #
   #   #    # #   #  #      #    #
   #    ####  #    # ######  ####





def compose(f, g):
    ## Return a function which passes its inputs first
    ## through f, then through g
    return lambda x: g(f(x))

def operate(init, functions):
        return reduce(compose, functions, lambda starter: init)("starter")







 ######                                           ##        ##   
 #     #   ##   #####  ##### #   ##   #          #    ####    #  
 #     #  #  #  #    #   #   #  #  #  #         #    #    #    # 
 ######  #    # #    #   #   # #    # #         #    #         # 
 #       ###### #####    #   # ###### #         #    #  ###    # 
 #       #    # #   #    #   # #    # #          #   #    #   #  
 #       #    # #    #   #   # #    # ######      ##  ####  ##   


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
        if tminus == 0:
            self.operations.append(operation)
        else:
            self.operations.insert(-tminus, operation)
        self._refresh()

    def deleteAgo(self, tminus=0):
        """
        Delete the operation 'tminus' operations ago.
        tminus :: int
        """
        if tminus == 0:
            del self.operations[len(self.operations)-1]
        else:
            del self.operations[-tminus]
        self._refresh()

    def _refresh(self):
        ## Refresh currstate from paststate + operations.
        tempstate = copy.deepcopy(self.paststate)
        self.currstate = operate(tempstate, self.operations)

        ## If the number of operations is too long...
        ## reduce it down to r previous operations
        if len(self.operations) > self.r:
            pre = self.operations[:-self.r]
            post = self.operations[-self.r:]
            tempstate = copy.deepcopy(self.pxaststate)
            self.paststate = operate(tempstate, pre)
            self.operations = post


def testPartiallyRetroactive():
    def appendSix(lst):
        return lst + [6]
    def appendTen(lst):
        return lst + [10]
    def deleteFirst(lst):
        del lst[0]
        return lst
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








 #######                                 ##        ##   
 #       #    # #      #      #   #     #    ####    #  
 #       #    # #      #       # #     #    #    #    # 
 #####   #    # #      #        #      #    #         # 
 #       #    # #      #        #      #    #  ###    # 
 #       #    # #      #        #       #   #    #   #  
 #        ####  ###### ######   #        ##  ####  ##   


class FullyRetroactive(object):
    """
    Implements full retroactivity for a generic data structure.

    Does this by storing a sequence of versions of *partially* retroactive data structures, plus some logging for the operations in between two such data structures in sequence.

    m :: the total number of retroactive updates that have been performed so far.

    timeline :: a list of many items. Each item is either a PartiallyRetroactive object or an operation.

    states :: a list of pointers to only the PartiallyRetroactive objects, above.
    """
    ## FullyRetroactive<X>

    def __init__(self, initstate):
        self.m = 0
        state = PartiallyRetroactive(initstate)
        self.timeline = [state]
        self.states = [state]

    def insertAgo(self, operation, tminus=0):
        pass

    def deleteAgo(self, tminus=0):
        pass

    def query(self, tminus=0):
        pass

    ## I'mma come back to this. It's going to be hard to do it the right
    ## way -- for that, we need persistent data structures. Alternative
    ## is just to do it the lazy way. For that, you'll want to copy the code
    ## from PartiallyRetroactive and just insert back-in-time querying.




#   #####                              ###               
#  #     #  ####  #    # #    #         #  #    # #    # 
#  #       #    # ##  ## ##  ##         #  ##   # #    # 
#  #       #    # # ## # # ## #         #  # #  # #    # 
#  #       #    # #    # #    # ###     #  #  # # #    # 
#  #     # #    # #    # #    # ###     #  #   ##  #  #  
#   #####   ####  #    # #    #  #     ### #    #   ##   
#                               #                        
# class PartiallyRetroactiveCommutativeInvertible(object):
#     def __init__(self, state):
#         self.state = state
#     def apply(self, operation):
#         self.state = operation(self.state)
#     def query(self):
#         return self.state
#     ## This fun is done


# def testPartiallyRetroactiveCommutativeInvertible():
#     def addSix(s):
#         return s + 6
#     def delSix(s):
#         return s - 6
#     x = PartiallyRetroactiveCommutativeInvertible(123)
#     x.query()
#     x.apply(addSix)
#     x.query()
#     x.apply(delSix)
#     x.query()







 ######     ######                                            
 #     #    #     # #  ####  ##### #    #   ##   #####  #   # 
 #     #    #     # # #    #   #   ##   #  #  #  #    #  # #  
 ######     #     # # #        #   # #  # #    # #    #   #   
 #          #     # # #        #   #  # # ###### #####    #   
 #          #     # # #    #   #   #   ## #    # #   #    #   
 #          ######  #  ####    #   #    # #    # #    #   #   

#TODO                                              
class PartiallyRetroactiveDictionary(object):
    ## Rephrase it as a searching problem!
    ## pg 11 of TALG
    pass






 ######      #####  ######  ######   #####  
 #     #    #     # #     # #     # #     # 
 #     #    #       #     # #     # #       
 ######      #####  #     # ######   #####  
 #                # #     # #             # 
 #          #     # #     # #       #     # 
 #           #####  ######  #        #####  

#TODO
class SearchableDynamicPartialSums(object):
    def __init__(self, state):
        pass
    def sum(self, i):
        pass
    def search(self, j):
        pass
    def update(self, i, c):
        pass

#TODO
class PartiallyRetroactiveSearchableDynamicPartialSums(object):
    def __init__(self, state):
        self.state = state
    def insert(self, operation):
        pass
    def delete(self, operation):
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


 ######      #####                              
 #     #    #     # #    # ###### #    # ###### 
 #     #    #     # #    # #      #    # #      
 ######     #     # #    # #####  #    # #####  
 #          #   # # #    # #      #    # #      
 #          #    #  #    # #      #    # #      
 #           #### #  ####  ######  ####  ###### 
                                                
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







 ######                              
 #     # ######  ####  #    # ###### 
 #     # #      #    # #    # #      
 #     # #####  #    # #    # #####  
 #     # #      #  # # #    # #      
 #     # #      #   #  #    # #      
 ######  ######  ### #  ####  ###### 
                                                                       
class RetroactiveDeque(object):
    pass





  #####                             
 #     # #####   ##    ####  #    # 
 #         #    #  #  #    # #   #  
  #####    #   #    # #      ####   
       #   #   ###### #      #  #   
 #     #   #   #    # #    # #   #  
  #####    #   #    #  ####  #    # 
                                           
class RetroactiveStack(object):
    pass





                                                      
 #     #                        #######                 
 #     # #    # #  ####  #    # #       # #    # #####  
 #     # ##   # # #    # ##   # #       # ##   # #    # 
 #     # # #  # # #    # # #  # #####   # # #  # #    # 
 #     # #  # # # #    # #  # # #       # #  # # #    # 
 #     # #   ## # #    # #   ## #       # #   ## #    # 
  #####  #    # #  ####  #    # #       # #    # #####  
                                                                                                    
class RetroactiveUnionFind(object):
    pass






 ######     ######                                        #####  
 #     #    #     # #####  #  ####  #####  # ##### #   # #     # 
 #     #    #     # #    # # #    # #    # #   #    # #  #     # 
 ######     ######  #    # # #    # #    # #   #     #   #     # 
 #          #       #####  # #    # #####  #   #     #   #   # # 
 #          #       #   #  # #    # #   #  #   #     #   #    #  
 #          #       #    # #  ####  #    # #   #     #    #### # 
                                                                                                                                 
class PartiallyRetroactivePriorityQueue(object):
    pass







 #######    ######                                        #####  
 #          #     # #####  #  ####  #####  # ##### #   # #     # 
 #          #     # #    # # #    # #    # #   #    # #  #     # 
 #####      ######  #    # # #    # #    # #   #     #   #     # 
 #          #       #####  # #    # #####  #   #     #   #   # # 
 #          #       #   #  # #    # #   #  #   #     #   #    #  
 #          #       #    # #  ####  #    # #   #     #    #### # 
                                                                 
class FullyRetroactivePriorityQueue(object):
    pass





 #######       #                               
 #            # #   #####  #####    ##   #   # 
 #           #   #  #    # #    #  #  #   # #  
 #####      #     # #    # #    # #    #   #   
 #          ####### #####  #####  ######   #   
 #          #     # #   #  #   #  #    #   #   
 #          #     # #    # #    # #    #   #   
                                                                                                              
class FullyRetroactiveReadonlyArray(object):
    pass












 ######                            #######                            
 #     #   ##    ####  #  ####        #    #   # #####  ######  ####  
 #     #  #  #  #      # #    #       #     # #  #    # #      #      
 ######  #    #  ####  # #            #      #   #    # #####   ####  
 #     # ######      # # #            #      #   #####  #           # 
 #     # #    # #    # # #    #       #      #   #      #      #    # 
 ######  #    #  ####  #  ####        #      #   #      ######  ####  













 ######   #####  ####### 
 #     # #     #    #    
 #     # #          #    
 ######   #####     #    
 #     #       #    #    
 #     # #     #    #    
 ######   #####     #    
                         

## BST implementation
## from https://github.com/laurentluce/python-algorithms/blob/master/algorithms/binary_tree.py
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def delete(self, data):
        # get node containing data
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                # if node has no children, just remove it
                # check if it is not the root node
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif children_count == 1:
                # if node has 1 child
                # replace node by its child
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            else:
                # if node has 2 children
                # find its successor
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                # replace node data by its successor data
                node.data = successor.data
                # fix successor's parent node child
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right






