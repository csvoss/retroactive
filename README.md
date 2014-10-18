Fun with Time Travel:
=====================

Implementing retroactive data structures in Python
--------------------------------------------------

6.851 Advanced Data Structures. Final project. Chelsea Voss, Spring 2014.

Introduction
------------

Unlike normal data structures, which only allow operations to be carried out in the present, **retroactive data structures** allow operations to be inserted or deleted at any point in the past.

In a **partially retroactive** data structure, queries may not be made into the past state of the data structure; however, in a *fully retroactive* data structure, queries may be made at any point along the timeline and history of operations.

Retroactive data structures were explored in [the 2007 paper](http://erikdemaine.org/papers/Retroactive_TALG/paper.pdf) "Retroactive Data Structures," by Demaine, Iacono, and Langerman.

The goal of this project is to turn known algorithms for various types of retroactive data structures into *implementations*, developing a Python library that can be imported into Python code to allow retroactive data structures to be created seamlessly.

In the below runtimes, *r* is a parameter describing how far back in the past retroactive operations are allowed to occur, and *m* is the total number of retroactive updates that are ever performed on a data structure.

General Transformations
-----------------------

*General transformations* are devices that allow us to convert any data structure into a retroactive data structure.

### General transformation for partial retroactivity

Implemented, with an O(r) overhead.

This implementation uses the rollback method to implement retroactivity. It stores up to r prior operations as well as the state of the data structure before those operations, so that these operations can be reversed. When an operation is removed or inserted, the current state of the data structure is “refreshed” from the past state by applying each operation in sequence.

Implementing this proved to be an entertaining exercise in abstraction: it needs to be able to wrap *any* data structure, and allow *any* form of operation on that data structure. So, operations are represented – and passed as input – using Python functions: an operation is any function which takes in a data structure and returns a new data structure.

### General transformation from partial to full retroactivity
Implemented, with an O(m) overhead. (The better O(√m) implementation requires an implementation of persistence.)

This implementation stores a list of partially-retroactive data structures, applying or deleting operations from those partially-retroactive data structures when relevant. When the fully-retroactive data structure is queried, we simply query the relevant partially-retroactive data structure.

Specific Implementations
------------------------

*Specific implementations* are methods for taking certain data structures and converting them into retroactive data structures, using specific strategies outlined in Demaine et al 2007 in order to optimize for speed.

### Queue

A queue permits `enqueue` and `dequeue` operations on an ordered collection of data.

**Partial retroactivity**: O(1).

Creating a partially retroactive queue involves storing a doubly-linked list of items, inserting whenever an `enqueue` is made, but *not* deleting any old data when a `dequeue` is made – because that `dequeue` operation might be deleted later, for example.

Instead, two pointers, `F` and `B`, point to the items at the front and back of the queue when t=0; these two pointers are moved according to the proper logic whenever an `enqueue` or `dequeue` is retroactively inserted or removed. Then, querying is as simple as looking up those two pointers.

Unlike the other retroactive data structures, this data structure has a few quirks. First, the time at which a retroactive operation is inserted or deleted cannot be specified by an integer number: it must instead by specified by a pointer to a reference operation which occurs immediately after the time when the operation is to be retroactively inserted. Inserting an operation must therefore return a pointer to that operation, in case the operation is used later as a time reference. The pointer is used to instantly navigate to therelevant part of the doubly-linked list in O(1) time. One possibility is that the data structure could be converted to a form which uses integer times, with a binary tree on top of the doubly-linked list; to insert or remove an operation would then be O(log m), instead. A second quirk of the interface is that it does not have a single `query`() method: instead, there are two possible queries that can be made – `front`() and `back`().

**Full retroactivity**, O(log m): See *Deque*.

A better fully retroactive solution exists, which is O(log m) but O(1) for present-time operations. This requires an implementation of order-statistic trees (Cormen et al, 2001).

### Stack

**Partial retroactivity**, O(log m): See *Deque*.

**Full retroactivity**, O(log m): See *Deque*.

### Searchable, Dynamic Partial Sums

A searchable, dynamic partial sums (SDPS) data structure stores a sequence of numbers, and permits appending numbers at the end, computing the overall sum, or searching for the earliest point at which the sum exceeds a given threshold.

This data structure has commutative, invertible operations – allowing partial retroactivity to be achieved with no overhead.

**Partial retroactivity**: O(1).

Since operations on the “Searchable, Dynamic Partial Sums” data structure are commutative and invertible, partial retroactivity is easy: to `insert` an operation, perform it; to `delete` an operation, perform its inverse.

Some special wrapping was required to implement this in Python: it needs to be possible to determine the inverse of any operation. To fix this, the method `PartiallyRetroactiveSDPS.update(i,c)` was modified so that it returns a function to use as an operation to pass to `insert` and `delete`; this function remembers `c` as an attribute, enabling `delete` to apply the inverse operation, `update(i,-c)`.

It would be difficult to create a wrapper that works for all data structures with commutative, invertible operations, because of this same hurdle: determining the inverse of an arbitrary Python function. When the functions are defined beforehand, however, as with this implementation of partially-retroactive searchable dynamic sums, the task is more tractable.

**Full retroactivity**: Use the *General Transformation* from partial to full.

Basic Building Blocks
---------------------

Many of the data structures mentioned in Demaine et al 2007 require, as a prerequisite, the implementation of more basic building blocks.

Building blocks which have been implemented:

* *Doubly-linked list*: required for **Partially-Retroactive Queue** and for **Partially-Retroactive Priority Queue.**

* *Binary search tree*: required for **Partially-Retroactive Priority Queue**.

Building blocks which have not yet been implemented:

* *Link-cut tree*: required for **Fully-Retroactive Union-Fint**. (Sleator and Tarjan, 1983)

* *Modified (a,b)-tree*: required for **Fully-Retroactive Deque** and for **Partially-Retroactive Priority Queue**. (Fleischer, 1996)

* *Persistence*: required for O(√m)-overhead **General Full Retroactivity**. (Driscoll et al, 1989) (Fiat and Kaplan, 2001)

* *Order-statistic trees*: required for the improved **Fully Retroactive Queue**. (Cormen et al, 2001).
