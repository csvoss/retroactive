import unittest
from retroactive.full import RetroactiveUnionFind

class Test_union_find(unittest.TestCase):
    '''
        for these tests let x denote the edge that was cut
        x = edge that was cut
        b = the branch that contains x
        preX = ancestors of x in b
        postX = children of x in b
        p = "parent" the part of the tree above the lca of the nodes to be cut
        c = the path from the lca to the the other unioned node that does not contain a max edge
    '''
    def test_unionAgo_unionAtSameTime_shouldHaveSameRoot(self):
        set = RetroactiveUnionFind()
        set.unionAgo('a1','a2') 
        a1 = set.forest.getNode('a1')        
        a2 = set.forest.getNode('a2')

        self.assertEqual(set.forest.getRoot(a1),set.forest.getRoot(a2))


    def test_unionAgo_unionAtTime_samesetBeforeShouldFail(self):
        set = RetroactiveUnionFind()
        set.unionAgo('a1','a2', tdelta = 5) 
        a1 = set.forest.getNode('a1')        
        a2 = set.forest.getNode('a2')

        self.assertEqual(set.sameSetAgo('a1','a2',2), False)

    def test_unionAgo_unionAtTime_samesetAfterShouldSucceed(self):
        set = RetroactiveUnionFind()
        set.unionAgo('a1','a2', tdelta = 5) 
        a1 = set.forest.getNode('a1')        
        a2 = set.forest.getNode('a2')

        self.assertEqual(set.sameSetAgo('a1','a2',7), True)

    def test_unionAgo_unionTwice_unionTimeShouldChange(self):
        set = RetroactiveUnionFind()
        set.unionAgo('a1','a2', tdelta = 5) 
        set.unionAgo('a1','a2', tdelta = 2) 

        self.assertEqual(set.sameSetAgo('a1','a2',2), True)


    def test_unionAgo_unionTwiceSubTree_unionTimeShouldChange(self):
        set = RetroactiveUnionFind()
        set.unionAgo('a1','a2', tdelta = 5) 
        set.unionAgo('a2','a3', tdelta = 14) 
        set.unionAgo('a3','a4', tdelta = 7) 
        
        set.unionAgo('a2','b1', tdelta = 7)
        set.unionAgo('b1','b2', tdelta = 7)
        set.unionAgo('b2','b3', tdelta = 7)

        self.assertEqual(set.sameSetAgo('b3','a4',6), False)
        set.unionAgo('b3','a4',6)
        self.assertEqual(set.sameSetAgo('b3','a4',6), True)

    def test_unionAgo_unionTwice_pToPreXIntact(self):
        set = RetroactiveUnionFind()
        set.unionAgo('a1','a2', tdelta = 5) 
        set.unionAgo('a2','a3', tdelta = 3) 
        set.unionAgo('a3','a4', tdelta = 7) 
        set.unionAgo('a4','a5', tdelta = 14) 
        set.unionAgo('a5','a6', tdelta = 7) 

        set.unionAgo('a3','b1', tdelta = 7)
        set.unionAgo('b1','b2', tdelta = 7)
        set.unionAgo('b2','b3', tdelta = 7)

        set.unionAgo('b3','a6',6)

        # p to preX
        self.assertEqual(set.sameSetAgo('a1','a4',7), True)
        # check the other branch for safety
        self.assertEqual(set.sameSetAgo('a1','b2',7), True)


    def test_unionAgo_unionTwice_pToPostXIntact(self):
        set = RetroactiveUnionFind()
        set.unionAgo('a1','a2', tdelta = 5) 
        set.unionAgo('a2','a3', tdelta = 3) 
        set.unionAgo('a3','a4', tdelta = 7) 
        set.unionAgo('a4','a5', tdelta = 14) 
        set.unionAgo('a5','a6', tdelta = 7) 
        set.unionAgo('a6','a7', tdelta = 7)
        set.unionAgo('a7','a8', tdelta = 7)


        set.unionAgo('a3','b1', tdelta = 7)
        set.unionAgo('b1','b2', tdelta = 7)
        set.unionAgo('b2','b3', tdelta = 7)

        set.unionAgo('b3','a8',6)

        # c to postX
        self.assertEqual(set.sameSetAgo('a1','a7',14), True)

    def test_unionAgo_unionTwice_insidePostXIntact(self):
        set = RetroactiveUnionFind()
        set.unionAgo('a1','a2', tdelta = 5) 
        set.unionAgo('a2','a3', tdelta = 3) 
        set.unionAgo('a3','a4', tdelta = 7) 
        set.unionAgo('a4','a5', tdelta = 14) 
        set.unionAgo('a5','a6', tdelta = 7) 
        set.unionAgo('a6','a7', tdelta = 7)
        set.unionAgo('a7','a8', tdelta = 7)


        set.unionAgo('a3','b1', tdelta = 7)
        set.unionAgo('b1','b2', tdelta = 7)
        set.unionAgo('b2','b3', tdelta = 7)

        set.unionAgo('b3','a8',6)

        # c to postX
        self.assertEqual(set.sameSetAgo('a5','a7',7), True)
        
    def test_unionAgo_unionTwice_cToPostXIntact(self):
        set = RetroactiveUnionFind()
        set.unionAgo('a1','a2', tdelta = 5) 
        set.unionAgo('a2','a3', tdelta = 3) 
        set.unionAgo('a3','a4', tdelta = 7) 
        set.unionAgo('a4','a5', tdelta = 14) 
        set.unionAgo('a5','a6', tdelta = 7) 

        set.unionAgo('a3','b1', tdelta = 7)
        set.unionAgo('b1','b2', tdelta = 7)
        set.unionAgo('b2','b3', tdelta = 7)

        set.unionAgo('b3','a6',6)

        # c to postX
        self.assertEqual(set.sameSetAgo('b2','a5',14), True)


    def test_unionAgo_unionTwice_cToPreXIntact(self):
        set = RetroactiveUnionFind()
        set.unionAgo('a1','a2', tdelta = 5) 
        set.unionAgo('a2','a3', tdelta = 3) 
        set.unionAgo('a3','a4', tdelta = 7) 
        set.unionAgo('a4','a5', tdelta = 14) 
        set.unionAgo('a5','a6', tdelta = 7) 

        set.unionAgo('a3','b1', tdelta = 7)
        set.unionAgo('b1','b2', tdelta = 7)
        set.unionAgo('b2','b3', tdelta = 7)



        set.unionAgo('b3','a6',6)


        # c to postX
        self.assertEqual(set.sameSetAgo('b3','a4',7), True)



if __name__ == '__main__':
    unittest.main()
