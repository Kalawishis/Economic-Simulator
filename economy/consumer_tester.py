from market import *
from random import *

#cobb-douglas testing
#u(x, y) = (x^a)*(y^b)
#optimal bundle, (x, y) = ((a/(a+b))(m/px), (b/(a+b))/(m/py))
#where px is price of x, py is price of y, and m is income

#for each arg:
#arg[0] = a
#arg[1] = b
#arg[2] = px
#arg[3] = py
#income 100 for all cases

classical_list = []
simulator_list = []

for i in range(100):
    arg = [uniform(1,10) for x in range(4)]
    classical_x = (arg[0]/(arg[0] + arg[1]))*(100/arg[2])
    classical_y = (arg[1]/(arg[0] + arg[1]))*(100/arg[3])
    x, y = symbols("x y")
    xylo = Tradeable("xylo", arg[2])
    yacht = Tradeable("yacht", arg[3])
    u = Consumer("u", 100, [xylo, yacht], (x**arg[0])*(y**arg[1]), {xylo: x, yacht: y})
    for x in range(100):
        u.change_decision([xylo, yacht])
    print("classical", classical_x, classical_y)
    print("simulation", u.decision[xylo], u.decision[yacht])
    
    classical_list.append([classical_x, classical_y])
    simulator_list.append([u.decision[xylo], u.decision[yacht]])
    
    print()
