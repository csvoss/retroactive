General Transformations
=======================

*General transformations* are devices that allow us to convert any data structure into a retroactive data structure.

General transformation for partial retroactivity
------------------------------------------------

Implemented, with an O(r) overhead.

This implementation uses the rollback method to implement retroactivity. It stores up to r prior operations as well as the state of the data structure before those operations, so that these operations can be reversed. When an operation is removed or inserted, the current state of the data structure is “refreshed” from the past state by applying each operation in sequence.

Implementing this proved to be an entertaining exercise in abstraction: it needs to be able to wrap *any* data structure, and allow *any* form of operation on that data structure. So, operations are represented – and passed as input – using Python functions: an operation is any function which takes in a data structure and returns a new data structure.

General transformation from partial to full retroactivity
---------------------------------------------------------

Implemented, with an O(m) overhead.

This implementation stores a list of partially-retroactive data structures, applying or deleting operations from those partially-retroactive data structures when relevant. When the fully-retroactive data structure is queried, we simply query the relevant partially-retroactive data structure.

The better O(√m) implementation requires an implementation of persistence.
