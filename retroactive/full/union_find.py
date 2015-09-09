from retroactive.basic import LinkCutTree
class RetroactiveUnionFind(object):
    """description of class"""
    def __init__(self):
        self.forest = LinkCutTree()
        self.time = 0
    
    # unionAgo(a,b) links nodes a and b in the LinkCutTree if they weren't already linked. If they were it cuts the latest edge on the path between a and b. The new subtree will contain exactly one of a and b. We make that node the root
    # of the subtree and link it to the other node still in the main tree. This works because cutting the oldest node preserves all the pre-existing relationships in the tree that the new link doesn't overwrite.
    # Any node after the cut node X will node have its path go through the new connection between a and b, which is by definition earlier that X. Any node before that will remain unaffected.
    def unionAgo(self, a_data, b_data, tdelta = 0):
        # if the sets are already connected at the specified time return
        if self.sameSetAgo(a_data,b_data,tdelta):
            return

        #get node objects to work with
        a = self.forest.getNode(a_data)
        b = self.forest.getNode(b_data)
        union_time = self.time + tdelta
        if a is None:
            a = self.forest.makeTree(a_data)

        if b is None:
            b = self.forest.makeTree(b_data)

        
        # if the nodes are not connected at all, connect them. If they are connected at a later time, cut the oldest edge on the path between the two nodes, make the union'ed node the root of that tree and attach it to the other unioned node.
        if self.forest.getRoot(a) != self.forest.getRoot(b):
            self.forest.makeRoot(b)
            self.forest.link(a,b,union_time)
        else:
            lca = self.forest.lca(a,b)
            max_time = float("-inf")
            max_time_node = None
            for next in [a,b]:
                while next is not lca:
                    if next.parent_edge_weight > max_time:
                        max_time = next.parent_edge_weight
                        max_time_node = next
                    next = next.represented_parent

            self.forest.cut(max_time_node)
            if self.forest.getRoot(a) == next:
                self.forest.makeRoot(a)
                self.forest.link(b,a,union_time)
            else:
                self.forest.makeRoot(b)
                self.forest.link(a,b,union_time)
        self.time += 1

    # sameSetAgo(a,b,t) will find the lca of a and b and traverse the path from both to the lca, finding the largest edge on the path between a and b. If any edge is larger than time + tdelta then a, and b were not
    # connected at (time + tdelta)
    def sameSetAgo(self, a_data, b_data, tdelta = 0):
        # sameset is reflexive
        if a_data == b_data:
            return True

        a = self.forest.getNode(a_data)
        b = self.forest.getNode(b_data)
        query_time = self.time + tdelta

        if a is None or b is None:
            return False

        lca = self.forest.lca(a,b)
        if lca is None:
            return False

        for next in [a,b]:
            while next is not lca:
                if next.parent_edge_weight > query_time:
                    return False
                next = next.represented_parent
        
        return True

    # sameSetWhen(a,b) traverses the path between a and b and return the largest edge, which is the time at which a and b were connected.
    def sameSetWhen(self, a, b):
        lca = self.forest.lca(a,b)
        if lca is None:
            return float("-inf")

        max_time = float("-inf")
        for next in [a,b]:
            while next is not lca:
                if next.parent_edge_weight > max_time:
                    max_time = next.parent_edge_weight
                next = next.represented_parent
        
        return max_time



