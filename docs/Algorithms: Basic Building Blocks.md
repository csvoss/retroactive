 Basic Building Blocks
---------------------

Many of the data structures mentioned in Demaine et al 2007 require, as a prerequisite, the implementation of more basic building blocks.

Building blocks which have been implemented:

* *Doubly-linked list*: required for **Partially-Retroactive Queue** and for **Partially-Retroactive Priority Queue.**

* *Binary search tree*: required for **Partially-Retroactive Priority Queue**.

Building blocks which have not yet been implemented:

* *Link-cut tree*: required for **Fully-Retroactive Union-Find**. (Sleator and Tarjan, 1983)

* *Modified (a,b)-tree*: required for **Fully-Retroactive Deque** and for **Partially-Retroactive Priority Queue**. (Fleischer, 1996)

* *Persistence*: required for O(√m)-overhead **General Full Retroactivity**. (Driscoll et al, 1989) (Fiat and Kaplan, 2001)

* *Order-statistic trees*: required for the improved **Fully Retroactive Queue**. (Cormen et al, 2001).
