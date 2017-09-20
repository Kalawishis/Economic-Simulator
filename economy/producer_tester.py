from market import *
from random import *

#cobb-douglas testing
#p(k, l) = c*(k^a)*(l^b)
#optimal bundle k = (c*p*(b/wk)**(1-a)*(a/wl)**a)**(1/(1-a-b))
#optimal bundle l = (c*p*(a/wl)**(1-b)*(b/wk)**b)**(1/(1-a-b))
#where wk is price of k, wl is price of l

"""
c = 5
p = 10
a = 0.4
b = 0.4
wl = 5
wk = 20

opt_k = (c*p*(b/wk)**(1-a)*(a/wl)**a)**(1/(1-a-b))
opt_l = (c*p*(a/wl)**(1-b)*(b/wk)**b)**(1/(1-a-b))

print(opt_k)
print(opt_l)

k, l = symbols("k l")
capital = Tradeable("capital", 20)
labor = Tradeable("labor", 5)
good = Tradeable("good", 10)
pro = Producer("p", [capital, labor], good, 5*(k**a)*(l**b), {capital: k, labor: l})
pro.decision[capital] += 1
pro.decision[labor] += 1
for x in range(100):
    pro.change_decision([capital, labor])

print(pro.decision)
"""

#for each arg:
#arg[0] = a
#arg[1] = b
#arg[2] = wk
#arg[3] = wl

classical_list = []
simulator_list = []

count = 0

while count < 100:
    
    arg = [uniform(0.1,0.499), uniform(0.1,0.499), uniform(1,4), uniform(1,4)]
    c = 5
    p = 10
    a = arg[0]
    b = arg[1]
    wk = arg[2]
    wl = arg[3]

    classical_k = (c*p*(b/wk)**(1-a)*(a/wl)**a)**(1/(1-a-b))
    classical_l = (c*p*(a/wl)**(1-b)*(b/wk)**b)**(1/(1-a-b))

    if not 1 < classical_k < 100 or not 1 < classical_l < 100:
        continue
    
    count += 1
    
    k, l = symbols("k l")
    capital = Tradeable("capital", arg[2])
    labor = Tradeable("labor", arg[3])
    good = Tradeable("good", p)
    pro = Producer("p", [capital, labor], good, c*(k**arg[1])*(l**arg[0]), {capital: k, labor: l})
    pro.decision[capital] += 1
    pro.decision[labor] += 1
    for x in range(200):
        pro.change_decision([capital, labor])
        
    print("classical", classical_k, classical_l)
    print("simulation", pro.decision[capital], pro.decision[labor])

    classical_list.append([classical_k, classical_l])
    simulator_list.append([pro.decision[capital], pro.decision[labor]])
    
    print()
#"""
