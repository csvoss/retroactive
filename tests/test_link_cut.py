import unittest
from link_cut_tree import LinkCutTree

class test_link_cut(unittest.TestCase):
    
    def test_getNode_nodeDoesntExist_returnsNone(self):
         tree = LinkCutTree()
         self.assertIsNone(tree.getNode('a1'))

    def test_getNode_nodeExists_returnsNode(self):
         tree = LinkCutTree()
         a1 = tree.makeTree('a1')
         self.assertEqual(a1,tree.getNode('a1'))

    def test_link_connectsTwoTrees(self):
        #arrange
        tree = LinkCutTree()
        a1 = tree.makeTree('a1')
        a2 = tree.makeTree('a2')
        
        #act
        tree.link(a1,a2)
        
        #assert
        self.assertEqual(a1, tree.getRoot(a2))

    def test_getRoot__returnsProperRootWhenRootHasMultipleChildren(self):
        #arrange
        tree = LinkCutTree()
        a1 = tree.makeTree('a1')
        a2 = tree.makeTree('a2')
        b1 = tree.makeTree('b1')
        tree.link(a1,a2)
        tree.link(a1,b1)
        #act / assert
        self.assertEqual(a1, tree.getRoot(a2))
        self.assertEqual(a1, tree.getRoot(b1))

    def test_cut__leaves_bothTreesIntact(self):
        # arrange
        tree = LinkCutTree()
        a1 = tree.makeTree('a1')
        a2 = tree.makeTree('a2')
        a3 = tree.makeTree('a3')
        a4 = tree.makeTree('a4')
        a5 = tree.makeTree('a5')
        a6 = tree.makeTree('a6')
        tree.link(a1,a2)
        tree.link(a2,a3)
        tree.link(a3,a4)
        tree.link(a4,a5)
        tree.link(a5,a6)

        c1 = tree.makeTree('c1')
        c2 = tree.makeTree('c2')
        c3 = tree.makeTree('c3')
        tree.link(c1,c2)
        tree.link(c2,c3)

        tree.link(a6,c1);

        #act
        tree.cut(c2)

        #assert
        self.assertEqual(a1, tree.getRoot(c1))
        self.assertEqual(c2, tree.getRoot(c3))
        
    def test_link__preservesRepresentedParent(self):
        ''' after linking all these tree's the represented_parent nodes should represent the paths in the represented tree
        '''
        #Arrange
        tree = LinkCutTree()
        a1 = tree.makeTree('a1')
        a2 = tree.makeTree('a2')
        a3 = tree.makeTree('a3')
        a4 = tree.makeTree('a4')
        a5 = tree.makeTree('a5')
        a6 = tree.makeTree('a6')
        tree.link(a1,a2)
        tree.link(a2,a3)
        tree.link(a3,a4)
        tree.link(a4,a5)
        tree.link(a5,a6)
        tree.access(a3)

        c1 = tree.makeTree('c1')
        c2 = tree.makeTree('c2')
        c3 = tree.makeTree('c3')
        tree.link(c1,c2)
        tree.link(c2,c3)

        tree.link(a4,c1);
        
        # act/assert
        self.assertEqual(a1,a2.represented_parent)
        self.assertEqual(a2,a3.represented_parent)
        self.assertEqual(a3,a4.represented_parent)
        self.assertEqual(a4,a5.represented_parent)
        self.assertEqual(a5,a6.represented_parent)
        
        self.assertEqual(c1,c2.represented_parent)
        self.assertEqual(c2,c3.represented_parent)

        self.assertEqual(a4,c1.represented_parent)

    def test_link_threeTrees_getRootShouldBeSameForAll(self):
        tree = LinkCutTree()
        #Arrange
        a1 = tree.makeTree('a1')
        a2 = tree.makeTree('a2')
        a3 = tree.makeTree('a3')
        a4 = tree.makeTree('a4')
        a5 = tree.makeTree('a5')
        a6 = tree.makeTree('a6')
        tree.link(a1,a2)
        tree.link(a2,a3)
        tree.link(a3,a4)
        tree.link(a4,a5)
        tree.link(a5,a6)
        
        b1 = tree.makeTree('b1')
        b2 = tree.makeTree('b2')
        b3 = tree.makeTree('b3')
        
        tree.link(b1,b2)
        tree.link(b2,b3)

        
        tree.link(a3,b1)
        
        c1 = tree.makeTree('c1')
        c2 = tree.makeTree('c2')
        c3 = tree.makeTree('c3')
        tree.link(c1,c2)
        tree.link(c2,c3)
        
        tree.link(a5,c1)

        # act/assert
        self.assertEqual(a1, tree.getRoot(c1))
        self.assertEqual(a1, tree.getRoot(b3))

    def test_lca_balancedTree_ShouldReturnRoot(self):
        #Arrange
        tree = LinkCutTree()
        a1 = tree.makeTree('a1')
        a2 = tree.makeTree('a2')
        a3 = tree.makeTree('a3')
        tree.link(a1,a2)
        tree.link(a1,a3)

        self.assertEqual(tree.lca(a2,a3),a1)
  
        
    def test_lca_path_shouldReturnOlderNode(self):
        #Arrange
        tree = LinkCutTree()
        a1 = tree.makeTree('a1')
        a2 = tree.makeTree('a2')
        a3 = tree.makeTree('a3')
        tree.link(a1,a2)
        tree.link(a2,a3)

        self.assertEqual(tree.lca(a2,a3),a2)

    def test_lca_query_order_doesnt_matter(self):
        #Arrange
        tree = LinkCutTree()
        a1 = tree.makeTree('a1')
        a2 = tree.makeTree('a2')
        a3 = tree.makeTree('a3')
        tree.link(a1,a2)
        tree.link(a2,a3)

        self.assertEqual(tree.lca(a2,a3),tree.lca(a3,a2))
              
    def test_lca_multipleLinks_shouldFindLCA(self):
        tree = LinkCutTree()
        #Arrange
        a1 = tree.makeTree('a1')
        a2 = tree.makeTree('a2')
        a3 = tree.makeTree('a3')
        a4 = tree.makeTree('a4')
        a5 = tree.makeTree('a5')
        a6 = tree.makeTree('a6')
        tree.link(a1,a2)
        tree.link(a2,a3)
        tree.link(a3,a4)
        tree.link(a4,a5)
        tree.link(a5,a6)
        
        b1 = tree.makeTree('b1')
        b2 = tree.makeTree('b2')
        b3 = tree.makeTree('b3')
        
        tree.link(b1,b2)
        tree.link(b2,b3)

        
        tree.link(a3,b1)
        
        c1 = tree.makeTree('c1')
        c2 = tree.makeTree('c2')
        c3 = tree.makeTree('c3')
        tree.link(c1,c2)
        tree.link(c1,c3)
        
        tree.link(a5,c1)

        
        self.assertEqual(tree.lca(c3,b3),a3)
   
    def test_makeRoot_path_shouldFlipPath(self):
        
        tree = LinkCutTree()
        a1 = tree.makeTree('a1')
        a2 = tree.makeTree('a2')
        a3 = tree.makeTree('a3')
        a4 = tree.makeTree('a4')
        a5 = tree.makeTree('a5')
        a6 = tree.makeTree('a6')
        tree.link(a1,a2,1)
        tree.link(a2,a3,2)
        tree.link(a3,a4,3)
        tree.link(a4,a5,4)
        tree.link(a5,a6,5)
    
        #act
        tree.makeRoot(a6)

        #assert
        self.assertEqual(a6, tree.getRoot(a1))
        self.assertEqual(a6, a5.represented_parent)
        self.assertEqual(a5, a4.represented_parent)
        self.assertEqual(a4, a3.represented_parent)
        self.assertEqual(a3, a2.represented_parent)
        self.assertEqual(a2, a1.represented_parent)



    def test_makeRoot_flip_tree(self):
        
        tree = LinkCutTree()
        a1 = tree.makeTree('a1')
        a2 = tree.makeTree('a2')
        a3 = tree.makeTree('a3')
        a4 = tree.makeTree('a4')
        a5 = tree.makeTree('a5')
        a6 = tree.makeTree('a6')
        tree.link(a1,a2,1)
        tree.link(a2,a3,2)
        tree.link(a3,a4,3)
        tree.link(a4,a5,4)
        tree.link(a5,a6,5)
    
         
        b1 = tree.makeTree('b1')
        b2 = tree.makeTree('b2')
        b3 = tree.makeTree('b3')
        
        tree.link(b1,b2)
        tree.link(b2,b3)

        
        tree.link(a3,b1)
        #act
        tree.makeRoot(b3)

        #assert
        
        self.assertEqual(b3, tree.getRoot(a6))

        # nodes on the flipped path still share root
        self.assertEqual(tree.getRoot(b1), tree.getRoot(a2))

        # node in flipped path and node out of path share root
        self.assertEqual(tree.getRoot(a6), tree.getRoot(a2))
       
        self.assertEqual(b2,b1.represented_parent)
        self.assertEqual(b3,b2.represented_parent)
        self.assertEqual(b1,a3.represented_parent)
        self.assertEqual(a3,a2.represented_parent)
        self.assertEqual(a2,a1.represented_parent)
        

if __name__ == '__main__':
    unittest.main()
