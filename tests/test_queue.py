import unittest
from retroactive.partial import PartiallyRetroactiveQueue

class TestQueue(unittest.TestCase):

    def test_normal(self):
        q = PartiallyRetroactiveQueue()
        _ = q.insertEnqueue(1)
        self.assertEqual(q.front(), 1)
        self.assertEqual(q.back(), 1)
        _ = q.insertEnqueue(2)
        self.assertEqual(q.front(), 1)
        self.assertEqual(q.back(), 2)
        _ = q.insertEnqueue(3)
        self.assertEqual(q.front(), 1)
        self.assertEqual(q.back(), 3)
        _ = q.insertDequeue()
        self.assertEqual(q.front(), 2)
        self.assertEqual(q.back(), 3)
        _ = q.insertDequeue()
        self.assertEqual(q.front(), 3)
        self.assertEqual(q.back(), 3)
        _ = q.insertDequeue()
        self.assertEqual(q.front(), None)
        self.assertEqual(q.back(), None)

    def test_normal_big(self):
        q = PartiallyRetroactiveQueue()
        n = 100
        for i in range(n):
            _ = q.insertEnqueue(i)
        self.assertEqual(q.front(), 0)
        self.assertEqual(q.back(), n-1)
        
    def test_empty(self):
        q = PartiallyRetroactiveQueue()
        self.assertEqual(q.front(), None)
        self.assertEqual(q.back(), None)

    def test_empty_refill(self):
        q = PartiallyRetroactiveQueue()
        _ = q.insertEnqueue(1)
        self.assertEqual(q.front(), 1)
        self.assertEqual(q.back(), 1)
        _ = q.insertDequeue()
        self.assertEqual(q.front(), None)
        self.assertEqual(q.back(), None)
        _ = q.insertEnqueue(1)
        self.assertEqual(q.front(), 1)
        self.assertEqual(q.back(), 1)
        _ = q.insertEnqueue(2)
        self.assertEqual(q.front(), 1)
        self.assertEqual(q.back(), 2)
        
    def delete_dequeues(self):
        q = PartiallyRetroactiveQueue()
        _ = q.insertEnqueue()

    def test_retroactive_insert_enqueue(self):
        q = PartiallyRetroactiveQueue()
        enq1 = q.insertEnqueue(1)
        self.assertEqual(q.front(), 1)
        self.assertEqual(q.back(), 1)
        enq3 = q.insertEnqueue(3)
        self.assertEqual(q.front(), 1)
        self.assertEqual(q.back(), 3)
        enq2 = q.insertEnqueue(2, enq3)  ## Retroactive insert of enqueue BEFORE enq1
        self.assertEqual(q.front(), 1)
        self.assertEqual(q.back(), 3)
        _ = q.insertDequeue()
        self.assertEqual(q.front(), 2)
        self.assertEqual(q.back(), 3)
        _ = q.insertDequeue()
        self.assertEqual(q.front(), 3)
        self.assertEqual(q.back(), 3)
        _ = q.insertDequeue()
        self.assertEqual(q.front(), None)
        self.assertEqual(q.back(), None)
