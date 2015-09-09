import unittest
from splay_tree import SplayNode

class NodeTest(unittest.TestCase):
    def test_left_zigzig_splay(self):
        #arrange
        a1 = SplayNode('a1')
        a2 = SplayNode('a2')
        a3 = SplayNode('a3')
        a1.addRight(a2)
        a2.addRight(a3)
        #act
        a3.splay()
        #assert
        self.assertEqual(a3.left,a2)
        self.assertEqual(a3.right,None)
        self.assertEqual(a3.parent, None)

        self.assertEqual(a2.left,a1)
        self.assertEqual(a2.right,None)
        self.assertEqual(a2.parent,a3)

        self.assertEqual(a1.left,None) 
        self.assertEqual(a1.right,None)
        self.assertEqual(a1.parent,a2)

                
      

    def test_left_zigzag_splay(self):
        #arrange
        a1 = SplayNode('a1')
        a2 = SplayNode('a2')
        a3 = SplayNode('a3')
        a3L = SplayNode('a3L')
        a3R = SplayNode('a3R')
        a1.addRight(a2)
        a2.addLeft(a3)
        a3.addLeft(a3L)
        a3.addRight(a3R)
        #act
        a3.splay()
        #assert
        self.assertEqual(a3.left,a1)        
        self.assertEqual(a3.right,a2)

        self.assertEqual(a1.right,a3L)
        self.assertEqual(a1.left,None)
        self.assertEqual(a1.parent,a3)

        self.assertEqual(a2.left,a3R)        
        self.assertEqual(a2.right,None) 
        self.assertEqual(a2.parent,a3)
        

    def test_right_zigzig_splay(self):
        #arrange
        a1 = SplayNode('a1')
        a2 = SplayNode('a2')
        a3 = SplayNode('a3')
        a1.addLeft(a2)
        a2.addLeft(a3)
        #act
        a3.splay()
        #assert
        self.assertEqual(a3.right,a2)
        self.assertEqual(a3.left,None)
        self.assertEqual(a3.parent, None)

        self.assertEqual(a2.right,a1)
        self.assertEqual(a2.left,None)
        self.assertEqual(a2.parent,a3)

        self.assertEqual(a1.right,None) 
        self.assertEqual(a1.left,None)
        self.assertEqual(a1.parent,a2)



    def test_right_zigzag_splay(self):
        #arrange
        a1 = SplayNode('a1')
        a2 = SplayNode('a2')
        a3 = SplayNode('a3')
        a3L = SplayNode('a3L')
        a3R = SplayNode('a3R')
        a1.addLeft(a2)
        a2.addRight(a3)
        a3.addLeft(a3L)
        a3.addRight(a3R)
        #act
        a3.splay()
        #assert
        self.assertEqual(a3.right,a1)        
        self.assertEqual(a3.left,a2)

        self.assertEqual(a1.left,a3R)
        self.assertEqual(a1.right,None)
        self.assertEqual(a1.parent,a3)

        self.assertEqual(a2.right,a3L)        
        self.assertEqual(a2.left,None) 
        self.assertEqual(a2.parent,a3)

if __name__ == '__main__':
    unittest.main()
