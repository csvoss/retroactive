import copy


def appendSix(lst):
    return lst + [6]
def appendTen(lst):
    return lst + [10]
def deleteFirst(lst):
    del lst[0]
    return lst



def compose(f, g):
    ## Return a function which passes its inputs first
    ## through f, then through g
    return lambda x: g(f(x))

def operate(init, functions):
        return reduce(compose, functions, lambda starter: init)("starter")



