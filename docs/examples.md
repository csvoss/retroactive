Example Usage
=============

General Partial Retroactivity
-----------------------------

To use one of these general transformations, simply initialize a Python class:

    >>> x = PartiallyRetroactive([1,2,3,4,5])

This creates a partially-retroactive list, initialized to [1,2,3,4,5]. We can add or remove operations in the present:

    >>> def appendOne(lst):
            return lst + [1]
			
    >>> x.insertAgo(appendOne, tminus=0)
    >>> x.insertAgo(appendOne, tminus=0)
    >>> x.insertAgo(appendOne, tminus=0)
	
    >>> x.query()
    [1, 2, 3, 4, 5, 1, 1, 1]   ## Three appendOnes!

...and we can add or remove operations from the past:

    >>> def appendSix(lst):
            return lst + [6]
			
    >>> x.insertAgo(appendSix, tminus=2)   ## Insert *two* operations ago
	
    >>> x.query()
    [1, 2, 3, 4, 5, 1, 6, 1, 1]
	
    >>> x.deleteAgo(tminus=3)   ## Delete the first appendOne
	
	>>> x.query()
    [1, 2, 3, 4, 5, 6, 1, 1]

General Full Retroactivity
--------------------------

Fully-retroactive data structures are similar, but permit querying into the past instead of just the present. Let us create a fully-retroactive list:

    >>> y = FullyRetroactive([1,2,3])
	
    >>> y.insertAgo(appendOne, tminus=0)
    >>> y.insertAgo(appendSix, tminus=0) ##This one should come last
    >>> y.insertAgo(appendTen, tminus=2) ##This one should come first
	
    >>> y.query()
    [1, 2, 3, 10, 1, 6]   ## The current state of the data structure
    >>> y.query(1)
    [1, 2, 3, 10, 1]
    >>> y.query(2)
    [1, 2, 3, 10]
    >>> y.query(3)
    [1, 2, 3]   ## The state of the data structure way back in the past

Looking back in time at the state of the data structures, we can see that the retroactive operations are taking place in the right order.



Partially Retroactive Queue
---------------------------

In contrast, the partialy retroactive queue is used somewhat differently from either transformation, because its optimizations have the quirk of requiring times to be specified using pointers.

    >>> queue = PartiallyRetroactive(Queue())
	
    ## INSERT enqueueings of some things
    >>> enq42 = queue.insertEnqueue(42)
    >>> enq43 = queue.insertEnqueue(43)
    >>> enq44 = queue.insertEnqueue(44)
	
    ## Manually query the entire state.
    ## (this is NOT the standard O(1) query)
    >>> print queue
    Front=42, Back=44, State=[44, 43, 42]
	
    ## INSERT an enqueue of 1
    ## BEFORE the enqueueing of 43
    >>> _ = queue.insertEnqueue(1, enq43)
    >>> print queue
    Front=42, Back=44, State=[44, 43, 1, 42]
	
    ## INSERT a dequeue
    ## BEFORE the enqueueing of 44
    >>> deq = queue.insertDequeue(enq44)
    >>> print queue
    Front=1, Back=44, State=[44, 43, 1]
	
    ## DELETE that dequeue
    >>> _ = queue.delete(deq)
    >>> print queue
    Front=42, Back=44, State=[44, 43, 1, 42]
	
    ## DELETE the enqueue of 42
    >>> _ = queue.delete(enq42)
    >>> print queue
    Front=1, Back=44, State=[44, 43, 1]
