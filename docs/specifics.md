Specific Implementations
========================

*Specific implementations* are methods for taking certain data structures and converting them into retroactive data structures, using specific strategies outlined in Demaine et al 2007 in order to optimize for speed.

Queue
-----

A queue permits `enqueue` and `dequeue` operations on an ordered collection of data.

**Partial retroactivity**: O(1).

Creating a partially retroactive queue involves storing a doubly-linked list of items, inserting whenever an `enqueue` is made, but *not* deleting any old data when a `dequeue` is made – because that `dequeue` operation might be deleted later, for example.

Instead, two pointers, `F` and `B`, point to the items at the front and back of the queue when t=0; these two pointers are moved according to the proper logic whenever an `enqueue` or `dequeue` is retroactively inserted or removed. Then, querying is as simple as looking up those two pointers.

Unlike the other retroactive data structures, this data structure has a few quirks. First, the time at which a retroactive operation is inserted or deleted cannot be specified by an integer number: it must instead by specified by a pointer to a reference operation which occurs immediately after the time when the operation is to be retroactively inserted. Inserting an operation must therefore return a pointer to that operation, in case the operation is used later as a time reference. The pointer is used to instantly navigate to therelevant part of the doubly-linked list in O(1) time. One possibility is that the data structure could be converted to a form which uses integer times, with a binary tree on top of the doubly-linked list; to insert or remove an operation would then be O(log m), instead. A second quirk of the interface is that it does not have a single `query`() method: instead, there are two possible queries that can be made – `front`() and `back`().

**Full retroactivity**, O(log m): See *Deque*.

A better fully retroactive solution exists, which is O(log m) but O(1) for present-time operations. This requires an implementation of order-statistic trees (Cormen et al, 2001).

Stack
-----

**Partial retroactivity**, O(log m): See *Deque*.

**Full retroactivity**, O(log m): See *Deque*.

Deque
-----

**Partial retroactivity**, O(log m): Implied by fully retroactive solution.

**Full retroactivity**, O(log m). Requires an implementation of modified (a,b)-trees.

Union-Find
----------

**Partial retroactivity**, O(log m): Implied by fully retroactive solution.

**Full retroactivity**, O(log m). Requires an implementation of link-cut trees.

Priority Queue
--------------

**Partial retroactivity**, O(log m). Requires an implementation of modified (a,b)-trees.

**Full retroactivity**: Use the *General Transformation* from partial to full.

Searchable, Dynamic Partial Sums
--------------------------------

A searchable, dynamic partial sums (SDPS) data structure stores a sequence of numbers, and permits appending numbers at the end, computing the overall sum, or searching for the earliest point at which the sum exceeds a given threshold.

This data structure has commutative, invertible operations – allowing partial retroactivity to be achieved with no overhead.

**Partial retroactivity**: O(1).

Since operations on the “Searchable, Dynamic Partial Sums” data structure are commutative and invertible, partial retroactivity is easy: to `insert` an operation, perform it; to `delete` an operation, perform its inverse.

Some special wrapping was required to implement this in Python: it needs to be possible to determine the inverse of any operation. To fix this, the method `PartiallyRetroactiveSDPS.update(i,c)` was modified so that it returns a function to use as an operation to pass to `insert` and `delete`; this function remembers `c` as an attribute, enabling `delete` to apply the inverse operation, `update(i,-c)`.

It would be difficult to create a wrapper that works for all data structures with commutative, invertible operations, because of this same hurdle: determining the inverse of an arbitrary Python function. When the functions are defined beforehand, however, as with this implementation of partially-retroactive searchable dynamic sums, the task is more tractable.

**Full retroactivity**: Use the *General Transformation* from partial to full.
