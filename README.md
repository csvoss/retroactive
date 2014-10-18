Fun with Time Travel:
=====================

Implementing retroactive data structures in Python
--------------------------------------------------

6.851 Advanced Data Structures final project

Chelsea Voss, Spring 2014

Introduction
------------

Unlike normal data structures, which only allow operations to be carried out in the present, **retroactive data structures** allow operations to be inserted or deleted at any point in the past.

In a **partially retroactive** data structure, queries may not be made into the past state of the data structure; however, in a *fully retroactive* data structure, queries may be made at any point along the timeline and history of operations.

Retroactive data structures were explored in [the 2007 paper](http://erikdemaine.org/papers/Retroactive_TALG/paper.pdf) "Retroactive Data Structures," by Demaine, Iacono, and Langerman.

The goal of this project is to turn known algorithms for various types of retroactive data structures into *implementations*, developing a Python library that can be imported into Python code to allow retroactive data structures to be created seamlessly.

General Transformations
-----------------------

In the below runtimes, *r* is a parameter describing how far back in the past retroactive operations are allowed to occur, and *m* is the total number of retroactive updates that are ever performed on a data structure.

Specific Implementations
------------------------

Basic Building Blocks
---------------------

Many of the data structures mentioned in Demaine et al 2007 require, as a prerequisite, the implementation of more basic building blocks.

Building blocks which have been implemented:

* *Doubly-linked list*: required for **Partially-Retroactive Queue** and for **Partially-Retroactive Priority Queue.**

* *Binary search tree*: required for **Partially-Retroactive Priority Queue**.

Building blocks which have not been implemented:

* *Link-cut tree*: required for **Fully-Retroactive Union-Fint**. (Sleator and Tarjan, 1983)

* *Modified (a,b)-tree*: required for **Fully-Retroactive Deque** and for **Partially-Retroactive Priority Queue**. (Fleischer, 1996)

* *Persistence*: required for O(√m)-overhead **General Full Retroactivity**. (Driscoll et al, 1989) (Fiat and Kaplan, 2001)
