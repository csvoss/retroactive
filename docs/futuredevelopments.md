Future Developments
===================
Not all of the Specific Implementations have been written yet. Many of these require an implementation of the above basic building blocks before they can be constructed:

* **Fully-Retroactive Deque**
* **Fully-Retroactive Union-Find**
* **Partially-Retroactive Priority Queue**

Also not yet written: Tests for each implementation.

On Abstraction and Elegance
---------------------------

Initially, I wanted to be able to unify *all* data structures under a single mechanism for creating retroactive versions of them: for example, `PartiallyRetroactive({'foo':3, 'bar':55})` or `FullyRetroactive(PriorityQueue())`, so that the interface for using retroactivity would be simple. However, there are some issues that create inelegance:

* Most data structures only allow exactly one sort of query, accessible via `query()`, but some must allow more (for example, the Partially Retroactive Queue must permit querying the elements at the front *and* back of the queue).
* Most data structures require a *number*, `tminus`, specifying how long ago to insert or delete an operation, but other data structures (again, Partially Retroactive Queue) require specifying this information with a pointer, instead.
* Most data structures require operations to be functions which take a data structure as an input and return a data structure as output, but some (for example, Partially Retroactive SDPS) require a different paradigm.

For these reasons, unifying the Specific Implementations under a single abstraction would have required adding extra options, making them more difficult for the user. For this reason, the Specific Implementations are presented as-is.
