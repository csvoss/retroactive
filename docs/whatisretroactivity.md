What is retroactivity?
======================

Unlike normal data structures, which only allow operations to be carried out in the present, **retroactive data structures** allow operations to be inserted or deleted at any point in the past.

In a **partially retroactive** data structure, queries may not be made into the past state of the data structure; however, in a *fully retroactive* data structure, queries may be made at any point along the timeline and history of operations.

Retroactive data structures were explored in [the 2007 paper](http://erikdemaine.org/papers/Retroactive_TALG/paper.pdf) "Retroactive Data Structures," by Demaine, Iacono, and Langerman.

The goal of this project is to turn known algorithms for various types of retroactive data structures into *implementations*, developing a Python library that can be imported into Python code to allow retroactive data structures to be created seamlessly.
