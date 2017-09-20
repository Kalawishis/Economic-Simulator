#module to model producers and consumers
#also defines a tradeable


import sys
sys.path.append('C:/Python34/game_theory')
from sequential_game import *


INACTIVE = ";" #do nothing
INCREMENT = "++" #add a tradeable
DECREMENT = "--" #subtract a tradeable
INTERCHANGE = "~" #change one tradeable out for another

DECISION_LIST = [INACTIVE, INCREMENT, DECREMENT, INTERCHANGE]

ILLEGAL = float('-inf') #represents something an agent cannot physically do

INFINITY = float('inf')

EPSILON = sys.float_info.epsilon #for usefulness


#class for any good, service, factor of production, etc
class Tradeable:

    def __init__(self, name, cost):

        self.name = name
        self.cost = cost

    def __repr__(self):

        return self.name
