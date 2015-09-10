from splay_tree import SplayNode

class LinkCutTree(object):

    def __init__(self):
        self.nodes = {}

    # access(n) makes n the root of the virtual tree, and its aux tree contains the path from root to v only. First we cut off the right child of the node we need to access (this is done by setting the value of prev to None initially). We then splay n to the root of its aux tree. After that
    # we attach n to its path parent (the node it points to outside of its own aux tree), we then splay the parent, and repeat the process untill we reach the root of the virtual tree. After this process we have a chain 
    # of right children all the way down to n. Splaying n now makes it the root of the virtual tree. It has no right child since we cut it off initially. The sub-tree to its left contains all its path parents in-order because the splay and
    # right link process preserves order, and the link function (defined elsewhere) always adds new children on the right.
    # Note: we return the last aux root so we can have an efficient lca algorithm
    def access(self, node):
        next = node
        prev = None
        while next is not None:
            next.splay()
            next.right = prev
            prev = next
            next = next.parent

        node.splay()
        return prev

    #
    # Mutate
    #

    # cut(n) accesses n, meaning it is the deepest node on the current preffered path and thus only has a left child ( no parent since it is the root of the virtual tree).
    # when n is accessed it becomes the head of the virtual tree. All nodes in its left subtree are its ancestors in the prefered path. All n's children in the represented tree currently have path parent pointers to n.
    # So removing n's left child severs the subtree rooted at n from the rest of the tree.
    def cut(self, node):
        self.access(node)

        # if the node is already a root return
        if node.left is None:
           return
        
       #virtual tree updates
        node.left.parent = None 
        node.left = None

        #represented tree updates
        node.represented_parent = None
        node.parent_edge_weight = None

    # link(p,c,e) Connects two represented trees by connecting the auxiliary trees containing the nodes p and c. p represents the node that will get a new child path in the represented tree, and c is the new sub-tree.
    # c needs to be the root of its  represented tree to ensure that it does not have multiple parents.
    # Since c can only have one unique parent in the new represented tree, p (the leaf node in the path that c was attached to), we store information about the represented edge between c and p in c.
    # Following a nodes represented parents up a tree is equivalent to doing a reverse in order traversal.
    def link(self, parent_node, child_root, edge_weight = None):      
        # make sure the two nodes are from different trees
        if self.getRoot(parent_node) ==  self.getRoot(child_root):
            return
            #raise Exception("link: Trying to ling two trees that are already linked")
        
        self.access(parent_node)
        self.access(child_root)
        # assert: child_root.isRoot() == True and child.left == None, because if not we will have two paths leading to the child node after linking (child_root.left and child_root.parent) violating the tree property
        if child_root.left is not None:
            raise Exception('Trying to link a child tree from an internal node')
        
        #virtual tree
        parent_node.right = child_root
        child_root.parent = parent_node

        #represented tree 
        child_root.parent_edge_weight = edge_weight
        child_root.represented_parent = parent_node

    def makeTree(self, data):
        if data in self.nodes:
            raise Exception("makeTree: Creating duplicate nodes")
        else:
            new_node = SplayNode(data)
            self.nodes[data] = new_node
            return new_node

    # makeRoot(node) flips the path from node to its root, inverting the path and making it a child path of node. All other connections are preserved.
    def makeRoot(self, node):
        self.access(node)
        flipped = None
        to_flip = node
        while to_flip is not None:
            next_edge_weight = to_flip.parent_edge_weight
            next_to_flip = to_flip.represented_parent or None
            next_edge_weight = to_flip.parent_edge_weight
            self.cut(to_flip)
            if flipped is not None:
                self.link(flipped, to_flip, edge_weight)
            flipped = to_flip
            to_flip = next_to_flip
            edge_weight = next_edge_weight
         
    

    #
    # Query
    #

    def getNode(self, data):
        if data in self.nodes:
            return self.nodes[data]
        else:
            return None

    # get root(n) accesses n, putting it in the preferred path from the root. Since the in order traversal of the aux tree represents the path, the leftmost node will be the root of the represented tree.
    def getRoot(self, node):
        self.access(node)
        while node.left is not None:
            node = node.left
        #splay the node (now root) so the cost of sequential requests for the same root is ammortized O(lg n)  
        node.splay()
        return node 

    # path aggregate follows the path in the represented tree from root to the chosen node ( under the hood this means traversing the aux tree containing the chosen node in order)
    def pathAggregate(self, node, fn):
        self.access(node)
        node.inOrder(fn)

    # lca(a,b) returns the least common ancestor of a and b. This works because after accessing a the last aux tree before b's tree becomes the root tree is the point at which the path from root to a and b diverges. This is because
    # each aux jump basically follows a path parent pointer. So if we access a and make it the root aux tree, the access to b will eventually have to jump into that aux tree. The path pointer it uses to do that will point to the node at which a and b
    # diverge.
    def lca(self, a, b):
        if self.getRoot(a) != self.getRoot(b):
           return None
        self.access(a)
        return self.access(b)
           
