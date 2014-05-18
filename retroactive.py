import copy

                                                                 

## partial retroactivity: view in present, modify anywhere
## full retroactivity: view anywhere, modify anywhere

## m = TOTAL # updates performed
## r = how retroactive-ago the update is
## n = MAX # elements in structure













#   #####                              ###               
#  #     #  ####  #    # #    #         #  #    # #    # 
#  #       #    # ##  ## ##  ##         #  ##   # #    # 
#  #       #    # # ## # # ## #         #  # #  # #    # 
#  #       #    # #    # #    # ###     #  #  # # #    # 
#  #     # #    # #    # #    # ###     #  #   ##  #  #  
#   #####   ####  #    # #    #  #     ### #    #   ##   
#                               #                        

## The problem with this is that defining the inverse of an operation
## is impossible to do programmatically. Because of that, I assume that
## someone who wants to make a commutative, invertible data structure
## partially retroactive will not use this abstraction.


# class PartiallyRetroactiveCommutativeInvertible(object):
#     def __init__(self, state):
#         self.state = state
#     def apply(self, operation):
#         self.state = operation(self.state)
#     def query(self):
#         return self.state
#     ## This fun is done


# def testPartiallyRetroactiveCommutativeInvertible():
#     def addSix(s):
#         return s + 6
#     def delSix(s):
#         return s - 6
#     x = PartiallyRetroactiveCommutativeInvertible(123)
#     x.query()
#     x.apply(addSix)
#     x.query()
#     x.apply(delSix)
#     x.query()
