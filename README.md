Fun with Time Travel: implementing retroactive data structures in Python
========================================================================

6.851 Advanced Data Structures final project, by Chelsea Voss, Spring 2014.


What is retroactivity?
----------------------

Unlike normal data structures, which only allow operations to be carried out in the present, **retroactive data structures** allow operations to be inserted or deleted at any point in the past.

In a **partially retroactive** data structure, queries may not be made into the past state of the data structure; however, in a *fully retroactive* data structure, queries may be made at any point along the timeline and history of operations.

Retroactive data structures were explored in [the 2007 paper](http://erikdemaine.org/papers/Retroactive_TALG/paper.pdf) "Retroactive Data Structures," by Demaine, Iacono, and Langerman.

The goal of this project is to turn known algorithms for various types of retroactive data structures into *implementations*, developing a Python library that can be imported into Python code to allow retroactive data structures to be created seamlessly.

Summary
-------
What was implemented:

* General transformations for any data structure:
    * Non-retroactive to partially retroactive, O(r) overhead
	* Partially retroactive to fully retroactive, O(m) overhead

* Queue:
    * Non-retroactive
    * Partially retroactive, O(1) overhead
	* Fully retroactive, O(m) overhead

* Searchable, Dynamic Partial Sums:
    * Non-retroactive
	* Partially retroactive, O(1) overhead
	* Fully retroactive, O(m) overhead

* Basic building blocks for more advanced data structures
    * *Doubly-linked list*: required for **Partially-Retroactive Queue** and for **Partially-Retroactive Priority Queue.**
    * *Binary search tree*: required for **Partially-Retroactive Priority Queue**.

Example Usage
-------------
### General Partial Retroactivity

General transformations can make any data structure retroactive. For example, the following initializes a partially-retroactive list, with initial state [1,2,3,4,5]. We can then add or remove operations in the present:

    >>> x = PartiallyRetroactive([1,2,3,4,5])
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

### General Full Retroactivity

Fully-retroactive data structures are similar to partially-retroactive data structures, in that they permit retroactive insertion and deletion of operations. However, fully-retroactive data structures also permit querying into the past instead of just the present. Here's a fully-retroactive list:

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


Future Developments
-------------------
Not all of the algorithms mentioned in Demaine et al 2007 have been implemented yet. The following remain unimplemented:

* **Fully-Retroactive Deque**
* **Fully-Retroactive Union-Find**
* **Partially-Retroactive Priority Queue**

Many of these require an implementation of certain *basic building blocks* before they can be constructed. Building blocks which have not yet been implemented:

* *Link-cut tree*: required for **Fully-Retroactive Union-Find**. (Sleator and Tarjan, 1983)

* *Modified (a,b)-tree*: required for **Fully-Retroactive Deque** and for **Partially-Retroactive Priority Queue**. (Fleischer, 1996)

* *Persistence*: required for O(√m)-overhead **General Full Retroactivity**. (Driscoll et al, 1989) (Fiat and Kaplan, 2001)

* *Order-statistic trees*: required for the improved **Fully Retroactive Queue**. (Cormen et al, 2001).


Read More
---------
Read the documentation at [Read The Docs](http://python-retroactive-data-structures.readthedocs.org/en/latest/).

Download the package at [PyPI](https://pypi.python.org/pypi/retroactive/).

Wikipedia: [Retroactive data structures](https://en.wikipedia.org/wiki/Retroactive_data_structures)
