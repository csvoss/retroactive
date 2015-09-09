class SplayNode(object):
    """Splay tree used by the link-cut tree."""
     
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        # there can only be a represented edge between two nodes if one is the in order successor of the other 
        self.represented_parent = None
        # stores the edge weight to the parent, since this is a tree this is enough to represent all edges uniquely
        self.parent_edge_weight = -1
        
        
    def inOrder(self, fn):
        if self.left is not None:
            self.left.inOrder(fn)
        
        fn(self.data)
                
        if self.right is not None:
            self.right.inOrder(fn)
            
    def printInOrder(self, fn):
        self.in_order(lambda x : print (x))
    
    def addLeft (self, other):
        self.left = other
        other.parent = self
    
    def addRight (self, other):
        self.right = other
        other.parent = self
        
    def isRoot(self):
        return (self.parent == None or (self.parent.left != self and self.parent.right != self))

    def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(self.data)

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret 

    def rotateRight(self):
        if self.isRoot():
            raise Exception("Trying to right rotate a root")
        old_parent = self.parent

        old_parent.left = self.right 
        if old_parent.left is not None:
            old_parent.left.parent = old_parent

        self.right =  old_parent
        self.parent = old_parent.parent
        old_parent.parent = self

        if self.parent is not None:
            if self.parent.left == old_parent:
                self.parent.left = self
            elif self.parent.right == old_parent:
                self.parent.right = self

        
    def rotateLeft(self):
        if self.isRoot():
             raise Exception("Trying to right rotate a root")

        old_parent = self.parent

        old_parent.right = self.left
        if old_parent.right is not None:
            old_parent.right.parent = old_parent

        self.left = old_parent
        self.parent = old_parent.parent
        old_parent.parent = self

        if self.parent is not None:
            # if neither of these cases is triggered it means self is the root of its splay tree and the parent pointer points to a path parent
            if self.parent.left == old_parent:
                self.parent.left = self
            elif self.parent.right == old_parent:
                self.parent.right = self


    def splay(self):
        while not self.isRoot():
            if self.parent.isRoot():
                if self.parent.left == self:
                    self.rotateRight()
                elif self.parent.right == self:
                    self.rotateLeft()
                else:
                    # this should never happen because an unacknowledged child is treated as a root, violating the loop condition
                    raise Exception("Splay: Attempting to rotate an unacknowledged (is not a left or right child) node ")
            else:
                # assert: grandparent != null because !parent.isRoot()
                grandparent = self.parent.parent
                if grandparent.left == self.parent:  

                   if self.parent.left == self: 
                       #zig-zig
                       self.parent.rotateRight()
                       self.rotateRight()
                   else:
                       #zig-zag
                       self.rotateLeft()
                       self.rotateRight()

                elif grandparent.right == self.parent: 
                    # assert: grandparent.right == self
                    if self.parent.right == self:
                        #zig-zig
                        self.parent.rotateLeft()
                        self.rotateLeft()
                    else:
                        #zig-zag
                        self.rotateRight()
                        self.rotateLeft()

                else:
                    # this should never be thrown since a node without a grandparent should be caught in the first if statement in the loop (self.parent.isRoot())
                    raise Exception("Splay: grandparent is not attached to parent")
