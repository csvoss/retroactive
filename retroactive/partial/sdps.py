## (SearchableDynamicPartialSums)

class PartiallyRetroactiveSDPS(object):
    def __init__(self, state=[]):
        self.state = state
        self.sums = [sum(state[:i]) for i in range(len(state))]
    
    def update(self, i, c):
        def return_update(x):
            x.state[i] += c
            for j in range(i,len(x.state)):
                x.sums[j] += c
            return x
        return_update.c = c
        return_update.i = i
        return return_update

    def insert(self, operation):
        """
        operation ::
            e.g. lambda q: q.update(3, 555)
        """
        operation = operation(self)
        assert operation.__name__ == 'return_update'
        self = operation(self)
    
    def delete(self, operation):
        """
        operation ::
            e.g. lambda q: q.update(3, 555)
        """
        operation = operation(self)
        assert operation.__name__ == 'return_update'
        inverse_operation = self.update(operation.i, -operation.c)
        assert inverse_operation.__name__ == 'return_update'
        self = inverse_operation(self)

    def sum(self, i):
        """
        Returns the sum of the first i elements of the array.
        """
        return self.sums[i]

    def search(self, j):
        """
        Returns the SMALLEST i such that sum(i) >= j.
        """
        for i in range(len(self.sums)):
            if self.sum(i) >= j:
                return i
